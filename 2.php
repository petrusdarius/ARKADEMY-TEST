<?php
	function AceptableUsername($username){
		return preg_match('/^[aiueo]{3}[a-z]{2,6}$/,$username);}
		
	function AceptablePassword($password){
	return preg_match('/^[aiueo]{1,8}[a-z0-9]{1,8}[!#$]{1,8}$/i,$password);}
		
?>		

//cara penggunaan
// if (AceptableUsername ("download")) {
//	echo "Username is Valid" ; 
//} else {
//	echo "Username is Invalid";
//}

//untuk password
// if (AceptablePassword ("!25FaTkuai")){
	echo "Password is Valid";
} else {
//echo "Password Invalid";}
	