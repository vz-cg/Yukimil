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
    var loading_img_element = document.createElement("img");
    loading_img_element.src="../img/loading-02.gif";
    // ------------------------------------------------------------
    // XMLHttpRequest オブジェクトを作成
    // ------------------------------------------------------------
    var xhr = XMLHttpRequestCreate();
    xhr.responseType = "blob";

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
                loading_img_element.style.display="block";
                loading_img_element.style.position="absolute";
                loading_img_element.style.top=target.offsetTop + 120 + "px";
                loading_img_element.style.left=target.offsetLeft + 120 + "px";
                document.getElementById("timelapse_dl").appendChild(loading_img_element);
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

                        var blob = xhr.response;

                        document.getElementById("timelapse_dl").removeChild(loading_img_element);
                        target.setAttribute("src", window.URL.createObjectURL(blob));

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

