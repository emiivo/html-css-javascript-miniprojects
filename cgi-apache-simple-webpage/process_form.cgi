#!/usr/bin/perl -T
use strict;
use warnings;
use CGI qw(:all -utf8);
use Time::Piece;

my $cgi = CGI->new;

print $cgi->header(-charset => 'UTF-8');

my %url_params = $cgi->Vars;

my $dob = $url_params{'dob'};
my $email = $url_params{'email'};
my $education = $url_params{'education'};
my $phone = $url_params{'phone'};
my $motyvacija = $url_params{'motyvacija'};

my $error_message = '';

if (!$dob) {
    $error_message .= "Gimimo data yra privaloma.<br>";
} elsif ($dob !~ /^\d{4}-\d{2}-\d{2}$/) {
    $error_message .= "Neteisingas gimimo datos formatas. Turi būti YYYY-MM-DD.<br>";
} else {
    my ($year, $month, $day) = split('-', $dob);
    my $birthdate = Time::Piece->strptime($dob, "%Y-%m-%d");
    my $current_date = Time::Piece->new;

    my $age = $current_date->year - $birthdate->year;

if (
    $age < 18
    || ($age == 18 && $birthdate->mon > $current_date->mon)
    || ($age == 18 && $birthdate->mon == $current_date->mon && $birthdate->mday > $current_date->mday)
) {
    $error_message .= "Nepilnamečiai negali dalyvauti.<br>";
}

}

if (!$email || $email !~ /^[A-Za-z0-9._%+-]+@[A-Za-z0-9.9.-]+\.[A-Za-z]{2,}$/) {
    $error_message .= "Neteisingas elektroninio pasto adresas.<br>";
}

if (!$education) {
    $error_message .= "Išsilavinimas yra privalomas.<br>";
}

if (!$phone || $phone !~ /^\+3706\d{6}$/) {
    $error_message .= "Neteisingas telefono numerio formatas.<br>";
}

if (!$motyvacija) {
    $error_message .= "Privaloma parašyti savo motyvacijas.<br>";
}

if ($error_message) {
    print "<h1>Registracijos klaida:</h1>";
    print "<p>$error_message</p>";
} else {
    print "<h1>Registracija sėkminga</h1>";
    print "<p>Gimimo data: $dob</p>";
    print "<p>Elektroninio pašto adresas: $email</p>";
    utf8::encode($education);
    print "<p>Išsilavinimas: $education</p>";
    print "<p>Telefono numeris: $phone</p>";
    print "<p>Motyvacija: $motyvacija</p>";
}

my $back = $cgi->referer();
print qq(<a href="$back">Atgal</a>);
