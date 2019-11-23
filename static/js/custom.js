$(document).ready(function() {
  $(".alert-message-close").click(function showAlert() {
    $(".alert-message").fadeTo(2000, 500).slideUp(500, function() {
      $(".alert-message").slideUp(500);
    });
  });
});
