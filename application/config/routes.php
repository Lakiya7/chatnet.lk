<?php
defined('BASEPATH') OR exit('No direct script access allowed');

/*
| -------------------------------------------------------------------------
| URI ROUTING
| -------------------------------------------------------------------------

|
| -------------------------------------------------------------------------
| RESERVED ROUTES
| -------------------------------------------------------------------------

*/
$route['default_controller'] = 'Authenticate/login';
$route['signup'] = 'Authenticate/signup';
$route['404_override'] = '';
$route['translate_uri_dashes'] = FALSE;
$route['insert'] = 'Authenticate/signupData';
$route['search'] = 'Authenticate/loginData';
$route['message'] = 'Message';
$route['logout'] = 'Message/logout';
$route['sent'] = 'Message/sendMessage';
$route['getmessage'] = 'Message/getMessage';