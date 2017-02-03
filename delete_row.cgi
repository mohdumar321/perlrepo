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

$myquery = "DELETE FROM $tablename WHERE id='$id'";

# EXECUTE THE QUERY FUNCTION
$execute = $connect->query($myquery);

print "Location: create.cgi\n\n";

