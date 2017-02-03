#!/usr/bin/perl

use Mysql;

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
	$id = $FORM{id};
    $first_name = $FORM{first_name};
    $last_name  = $FORM{last_name};

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

$myquery = "UPDATE $tablename SET first_name ='$first_name', last_name ='$last_name' WHERE id ='$id'";

# EXECUTE THE QUERY FUNCTION
$execute = $connect->query($myquery);

print "Location: create.cgi\n\n";




