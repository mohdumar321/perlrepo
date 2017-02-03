#!/usr/bin/perl

use Mysql;
use DBI;

    local ($buffer, @pairs, $pair, $name, $value, %FORM);
    # Read in text
    $ENV{'REQUEST_METHOD'} =~ tr/a-z/A-Z/;
    if ($ENV{'REQUEST_METHOD'} eq "POST")
    {
        read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
    }else {
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
    $first_name = $FORM{first_name};
    $last_name  = $FORM{last_name};

print "Content-type:text/html\r\n\r\n";

# MYSQL CONFIG VARIABLES
my $host = "172.30.79.105";
my $database = "sampledb";
my $tablename = "perl_db_1";
my $user = "admin";
my $pw = "root";

# PERL MYSQL CONNECT()
my $connect = Mysql->connect($host, $database, $user, $pw);

# SELECT DB
$connect->selectdb($database);


if ($ENV{'REQUEST_METHOD'} eq "POST" && $first_name)
    {


# DEFINE A MySQL QUERY
$myquery = "INSERT INTO $tablename (id, first_name, last_name) VALUES (DEFAULT,'$first_name','$last_name')";

# EXECUTE THE QUERY FUNCTION
$execute = $connect->query($myquery);
}

# DEFINE A MySQL QUERY
$myquery1 = "SELECT * FROM $tablename";

# EXECUTE THE QUERY FUNCTION
$execute = $connect->query($myquery1);

print <<HTML_PAGE;
<!DOCTYPE html>
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
#enter_form {
	border: 1px solid #999;
	padding: 10px;
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
<h1>Perl .... quite good</h1>
<div id='enter_form'>
<p>Add name</p>
<form action='create.cgi' method='POST'>
<div class = 'div_field_input'>First Name: <input type='text' name='first_name'></div>
<div class = 'div_field_input'>Last Name: <input type='text' name='last_name'></div>
<div class = 'div_field_submit'><input type='submit' value='Submit'></div>
</form>
</div>
<div class='clear'></div>

<div class = 'div_field'><strong>id</strong></div>
<div class = 'div_field'><strong>First name</strong></div>
<div class = 'div_field'><strong>Last name</strong></div>
<div class = 'div_field'><strong>Edit</strong></div>
<div class = 'div_field'><strong>Delete</strong></div>
<div class = 'clear'></div>
HTML_PAGE

while (@results = $execute->fetchrow()) {
	print "
	<div class = 'div_field'>".$results[0]."</div>
	<div class = 'div_field'>".$results[1]."</div>
	<div class = 'div_field'>".$results[2]."</div>
	<div class = 'div_field'><a href='edit_row.cgi?id=".$results[0]."'>edit</a></div>
	<div class = 'div_field'><a href='delete_row.cgi?id=".$results[0]."'>delete</a></div>";
}

print <<HTML_PAGE;
<div class='clear'></div>

</div>
</body>
</html>
HTML_PAGE

