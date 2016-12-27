function XMLHttpRequestCreate(){
    try{
        return new XMLHttpRequest();
    }catch(e){}
    try{
        return new ActiveXObject('MSXML2.XMLHTTP.6.0');
    }catch(e){}
    try{
        return new ActiveXObject('MSXML2.XMLHTTP.3.0');
    }catch(e){}
    try{
        return new ActiveXObject('MSXML2.XMLHTTP');
    }catch(e){}

    return null;
};


function start_timelapse(target){
    var target_name=target.getAttribute("class");
    var loadingImgElemet = document.getElementById("loading");
    // ------------------------------------------------------------
    // XMLHttpRequest オブジェクトを作成
    // ------------------------------------------------------------
    var xhr = XMLHttpRequestCreate();

    // ------------------------------------------------------------
    // XHR 通信の状態が変化するたびに実行されるイベント
    // ------------------------------------------------------------
    xhr.onreadystatechange = function (){

        switch(xhr.readyState){
            // ------------------------------------------------------------
            // XHR 通信中
            // ------------------------------------------------------------
            case 1:
            case 2:
            case 3:
                //target.setAttribute("src", "../img/loading-20.gif");
                loadingImgElemet.style.display="block";
                loadingImgElemet.style.top=target.offsetTop + 120 + "px";
                loadingImgElemet.style.left=target.offsetLeft + 120 + "px";
                break;
            case 4:
                // ------------------------------------------------------------
                // XHR 通信失敗
                // ------------------------------------------------------------
                if(xhr.status == 0){

                    alert("XHR 通信失敗");

                    // ------------------------------------------------------------
                    // XHR 通信成功
                    // ------------------------------------------------------------
                }else{

                    // ------------------------------------------------------------
                    // リクエスト成功
                    // ------------------------------------------------------------
                    if((200 <= xhr.status && xhr.status < 300) || (xhr.status == 304)){

                        loadingImgElemet.style.display="none";
                        target.setAttribute("src", "../img/ski/archive/"+target_name+"/movie.gif");

                        // ------------------------------------------------------------
                        // リクエスト失敗
                        // ------------------------------------------------------------
                    }else{

                        alert("その他の応答:" + xhr.status);

                    }
                }
                break;
        }
    }
    xhr.open("GET", "make_timelapse.cgi?name="+target_name);
    xhr.send(null);
};

