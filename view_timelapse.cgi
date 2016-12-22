#!/bin/sh

target=`echo ${QUERY_STRING} | sed -e "s/name=\([^&]*\).*/\1/"`

#query unexpected ch test
[ `echo $target | sed 's/\([a-z]|[-/]*[0-9]*\).*/\1/'` != $target ] && exit 1;

cat <<EOF
Content-Type: text/html

<html>
<head>
<meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
<title> Yukimilユキミル Time Lapse</title>
<script type="text/javascript" src="./main.js"></script>
</head>
<body>
<div id="header">
    <div class="title">
        <h1>
           スキー場ライブカメラ タイムラプス
        </h1>
    </div>
    <div class="sub_title">
        <h2>
EOF
echo "${target}"
cat <<EOF
        </h2>
</div><!--header-->
EOF
cat <<EOF
<div id="contents">
EOF
echo "<img src=\"../img/ski/archive/${target}/movie.gif\" alt=\"time lapse movie\" />"
cat <<EOF
</div>
</body>
</html>
EOF
