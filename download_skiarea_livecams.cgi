#!/bin/sh

#download live cam images
column=0
date=`date "+%Y%m%d%H%M"`
date_with_sepa=`date "+%Y/%m/%d %H:%M"`
while read line; do

    name=`echo $line | cut -d ',' -f 1`;
    site=`echo $line | cut -d ',' -f 2`;

    dir=./img/ski/archive/${name}
    [ ! -e $dir ] && mkdir -p $dir
    
#download livecam only when image does not updated within 10min.
    if test ! -e ./img/ski/$name; then
        wget -nv -O ./img/ski/$name $site;
        cp ./img/ski/$name ${dir}/${name}${date};
        #insert label
        convert ./img/ski/$name -geometry 250x250 -background Khaki  label:"${name} ${date_with_sepa}" -pointsize 16 -gravity Center -append    ./img/ski/labeled/`printf %d $column`_${name}_label.jpg
        #save laveled image to make time lapse
        cp ./img/ski/labeled/`printf %d $column`_${name}_label.jpg ${dir}/resize_${name}${date}
    elif [ `find ./img/ski/$name -mmin -10 | wc -l` -eq 0 ]; then
        wget -nv -O ./img/ski/$name $site;
        cp ./img/ski/$name ${dir}/${name}${date};
        #insert label
        convert ./img/ski/$name -geometry 250x250 -background Khaki  label:"${name} ${date_with_sepa}" -pointsize 16 -gravity Center -append    ./img/ski/labeled/`printf %d $column`_${name}_label.jpg
        #save laveled image to make time lapse
        cp ./img/ski/labeled/`printf %d $column`_${name}_label.jpg ${dir}/resize_${name}${date}
    fi

     column=$((column+1))

done < ski_livecams.conf  

#montage images
montage -geometry 250x250+5+5 -tile 3x ./img/ski/labeled/* -background "#999999" ./img/ski/thumbnail.jpg

echo "Content-Type: text/html"
echo ""
echo "<!doctype html>"
echo "<html><head><title>ski area live cams</title></head>"
echo "<body>"
echo "<p><img src="./img/ski/thumbnail.jpg" alt=\"live cams of ski area\" usemap=\"#links\"></p>"

echo "<map name=\"links\">"

i=0
while read line; do
    site=`echo $line | cut -d ',' -f 3`;
    name=`echo $line | cut -d ',' -f 1`;

    x1=`expr 5 + $i % 3 \* 260`
    y1=`expr 5 + $i / 3 \* 260`

    echo "<area shape=\"rect\" coords=\"${x1}, ${y1}, $((${x1} + 250)), $((${y1} + 250))\" href=\"$site\" target=\" _blank\" alt=\"$name\">"

    i=$(($i+1))
done < ski_livecams.conf

echo "</map>"

echo "</body>"
echo "</html>"
