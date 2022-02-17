/*
line below tells JSHint that the code uses ECMAScript 6 specific syntax:https://stackoverflow.com/questions/27441803/why-does-jshint-throw-a-warning-if-i-am-using-const
*/
/*jshint esversion: 6 */

let countrySelected = $('#id_default_country').val();
if (!countrySelected) {
   $('#id_default_country').css('color', '#aab7c4');
}
$('#id_default_country').change(function () {
   countrySelected = $(this).val();
   if (!countrySelected) {
      $(this).css('color', '#aab7c4');
   } else {
      $(this).css('color', '#000');
   }
});