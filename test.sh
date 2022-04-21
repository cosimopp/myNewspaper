page="$(wget -O - 'google.com')"
## display the page ##
echo "$page"
## or pass it to lynx / w3m ##
echo "$page" | links2 -dump google.com
#echo "$page" | lynx -dump -stdin