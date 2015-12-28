$(document).ready(function(){
    $(".input-busca").focus(function(){
        if ("Escreva aqui sua pergunta" == $(this).val())
            $(this).val("");
    });

    $(".input-busca").blur(function(){
        if ("" == $(this).val().trim())
            $(this).val("Escreva aqui sua pergunta");
    });
});
