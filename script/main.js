function onclick(me){
$(function() {
        $(".live-cam").css("display", "none");
        $("#" + me + " .live-cam").css("display", "block");
        });
        $(".map").on("click", function(){
                $(".live-cam").css("display","none");
        });
}
