var element = document.getElementsByTagName('input');
element[1].placeholder = ' Username';
element[2].placeholder = ' Email';
element[3].placeholder = ' Password';
element[4].placeholder = ' Confirm Password';

for(var field in element)
{
  element[field].className += 'form-control'
}
