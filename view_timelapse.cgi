#!/bin/sh

#parse query
target=`echo ${QUERY_STRING} | sed -e "s/name=\([^&]*\).*/\1/"`

#query unexpected ch test
[ `echo $target | sed 's/\([a-z]|[-/]*[0-9]*\).*/\1/'` != $target ] && exit 1;

#if movie.gif exsists and that made if this 2hour,
#just show that. else make gif movie.
if [ `find ../img/ski/archive/${target} -name "movie.gif" -mtime -2h | wc -l` -eq 0 ]; then
    #choose pictures in this 3days.
    if [ -e ../img/ski/archive/${target} ] ; then
        cd ../img/ski/archive/${target}
    else
        exit 1;
    fi
    files=`find . -mtime -3d | tr -d "./" | sort`

    #make gif anime
    convert ${files} -resize 30% resize_%06d.gif
    convert -loop 1 -delay 40 resize_*.gif movie.gif
    rm resize_*.gif
fi


echo "Content-Type: text/html"
echo ""
echo "<!doctype html>"
echo "<html>"
echo "<head>"
echo "<meta charset=\"UTF-8\">"
echo "<title>${target}のタイムラプス</title>"
echo "<script type=\"text/javascript\" src=\"gifffer.min.js\"></script>"
echo "<script type=\"text/javascript\">"
echo "window.onload = function() {"
echo "  Gifffer();"
echo "}"
echo "</script>"
echo "</head>"
echo "<body>"
echo "<h1>"
echo "${target}"
echo "</h1>"
echo "<img data-gifffer=\"http://akimil-sapporo.sakura.ne.jp/img/ski/archive/${target}/movie.gif\" />" 
echo "</body>"
echo "</html>"
