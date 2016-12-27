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
    files=`find . -name "${target}*" -mtime -3d | tr -d "./" | sort`

    #make gif anime
    for file in $files; do
        if [ ! -e resize_${file}* ]; then
            convert ${file} -resize 250x resize_${file}.gif
        fi
    done
    files=`find . -name "resize_${target}*" -mtime -3d | tr -d "./" | sort`
    convert -loop 1 -delay 40 ${files} movie.gif
fi

echo "Content-Type: image/gif"
echo ""
