#!/usr/bin/perl

use Mysql;
use DBI;


    local ($buffer, @pairs, $pair, $name, $value, %FORM);
    # Read in text
    $ENV{'REQUEST_METHOD'} =~ tr/a-z/A-Z/;
    if ($ENV{'REQUEST_METHOD'} eq "GET")
    {
	$buffer = $ENV{'QUERY_STRING'};
    }
    # Split information into name/value pairs
    @pairs = split(/&/, $buffer);
    foreach $pair (@pairs)
    {
	($name, $value) = split(/=/, $pair);
	$value =~ tr/+/ /;
	$value =~ s/%(..)/pack("C", hex($1))/eg;
	$FORM{$name} = $value;
    }
    $id= $FORM{id};





# MYSQL CONFIG VARIABLES
my $host = "172.30.79.105";
my $database = "sampledb";
my $tablename = "perl_db_1";
my $user = "admin";
my $pw = "root";

# PERL MYSQL CONNECT()
$connect = Mysql->connect($host, $database, $user, $pw);

# SELECT DB
$connect->selectdb($database);

# DEFINE A MySQL QUERY
my $myquery1 = "SELECT * FROM $tablename WHERE id='$id'";

# EXECUTE THE QUERY FUNCTION
my $execute = $connect->query($myquery1);
@results = $execute->fetchrow();

print "Content-type:text/html\r\n\r\n";

print <<HTML_PAGE;
<!DOCTYPE html>
<html>
<head>
<title>Perl ... Quite good edit page</title>
<style>
body {
	background-color: #DEDDD8;
}
.wrapper {
	width: 850px;
	margin: 10px auto;
	font-family: Arial;
	color: #999;
	padding:20px;
	background: #feffe8; /* Old browsers */
	background: -moz-linear-gradient(top,  #fff 0%, #d6dbbf 100%); /* FF3.6+ */
	background: -webkit-gradient(linear, left top, left bottom, color-stop(0%,#fff), color-stop(100%,#d6dbbf)); /* Chrome,Safari4+ */
	background: -webkit-linear-gradient(top,  #fff 0%,#d6dbbf 100%); /* Chrome10+,Safari5.1+ */
	background: -o-linear-gradient(top,  #fff 0%,#d6dbbf 100%); /* Opera 11.10+ */
	background: -ms-linear-gradient(top,  #fff 0%,#d6dbbf 100%); /* IE10+ */
	background: linear-gradient(to bottom,  #fff 0%,#d6dbbf 100%); /* W3C */
	filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#fff', endColorstr='#d6dbbf',GradientType=0 ); /* IE6-9 */
	box-shadow: 0 6px 12px #999999;
}
td {
	border-collapse: collapese;
	border-top: 0px;
	border-bottom: 1px;
	border-bottom: #000;
	border-left: 0px;
	border-right: 0px;
}

tr {
	border-collapse: collapese;
	border-top: 0px;
	border-bottom: 1px;
	border-bottom: #000;
	border-left: 0px;
	border-right: 0px;
}

table {
	border-collapse: collapese;
	border-top: 0px;
	border-bottom: 1px;
	border-bottom: #000;
	border-left: 0px;
	border-right: 0px;
}

.div_field {
	width: 150px;
	float: left;
	height: 20px;
	border-bottom: 1px solid #999;
	padding: 10px;
}

.div_field_input {
	width: 333px;
	float: left;
	height: 20px;
	padding: 10px 10px 10px 0;
}

.div_field_submit {
	width: 125px;
	float: left;
	height: 20px;
	padding: 10px 10px 10px 0;
}

.clear {
	clear: both;
	width: 100%;
}
#enter_form1 {
	border: 1px solid #999;
	padding: 40px 10px 40px;
	overflow: hidden;
	background: #ffffff; /* Old browsers */
	background: -moz-linear-gradient(top,  #ffffff 0%, #e9ede1 100%); /* FF3.6+ */
	background: -webkit-gradient(linear, left top, left bottom, color-stop(0%,#ffffff), color-stop(100%,#e9ede1)); /* Chrome,Safari4+ */
	background: -webkit-linear-gradient(top,  #ffffff 0%,#e9ede1 100%); /* Chrome10+,Safari5.1+ */
	background: -o-linear-gradient(top,  #ffffff 0%,#e9ede1 100%); /* Opera 11.10+ */
	background: -ms-linear-gradient(top,  #ffffff 0%,#e9ede1 100%); /* IE10+ */
	background: linear-gradient(to bottom,  #ffffff 0%,#e9ede1 100%); /* W3C */
	filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#ffffff', endColorstr='#e9ede1',GradientType=0 ); /* IE6-9 */
}

h1 {
	color: #999;
}

a {
	color: #999;
}
</style>
</head>
<body>
HTML_PAGE

print <<HTML_PAGE;
<div class='wrapper'>
<div id='enter_form1'>
<h1>Perl .... quite good</h1>
<form action='edit_row2.cgi' method='POST'>
<input type='hidden' name='id' value='$id'>
<div class = 'div_field_input'>First Name: <input type='text' name='first_name' value='$results[1]'></div>
<div class = 'div_field_input'>Last Name: <input type='text' name='last_name' value='$results[2]'></div>
<div class = 'div_field_submit'><input type='submit' value='Submit'></div>
</form>
</div>
</div>
</body>
</html>
HTML_PAGE

