#!/usr/local/bin/perl

use strict;
use warnings;

my $process = `ps aux | grep -i "gphoto"`;
my ($pid) = $process =~ /\npi\s+(\d+).+gphoto2 --spawner.+/s;

if ($pid) {
    `kill -9 $pid`;
    `ps aux | grep -i "gphoto"`;
    print "Camera unmounted and ready to use."
}
else {
    print "Nothing to unmount."
}

