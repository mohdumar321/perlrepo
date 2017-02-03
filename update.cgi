#!/usr/bin/perl

use Mysql;


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
$myquery1 = "SELECT * FROM $tablename WHERE id='$id'";

# EXECUTE THE QUERY FUNCTION
$execute = $connect->query($myquery1);
@results = $execute->fetchrow();


print "Content-type:text/html\r\n\r\n";
print "<html>";
print "<head>";

print "<title>Sixth -  CGI Program</title>";
print "</head>";
print "<body>";
print "</body>";
print "</html>";

print "<form action='create.cgi' method='POST'>";
print "First Name: <input type='text' name='first_name' value='$results[1]'>  <br>";

print "Last Name: <input type='text' name='last_name' value='$results[2]'>";
print "<input type='submit' value='Submit'>";
print "</form>";

