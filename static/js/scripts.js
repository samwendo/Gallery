$(document).ready(function(){
    $('#me').click(function(event){
      event.preventDefault()
      var copyText = document.getElementById("imageUrl");
      copyText.select();
      document.execCommand("copy");
      alert("Copied the url: " + copyText.value);
    })
  
    // Modals
    $('.selectedImage').click(function(){
      $('#myModal').css('display', "block")
      $("#modal-con").attr('src',$(this).attr('src'))
    })
  
    $(".close").click(function() {
      $('#myModal').css('display', "none");
      $('#modal-details').css('display', 'none')
    })
  })
  
  function myFunction() {
    /* Get the text field */
    var copyText = document.getElementById("myInput");
  
    /* Select the text field */
    copyText.select();
  
    /* Copy the text inside the text field */
    document.execCommand("copy");
  
    /* Alert the copied text */
    alert("Copied the text: " + copyText.value);
  }
  