# This Puppet maniffest creates a file at /tmp/school with specific properties

file { 'school':
ensure  => 'present',
path    => '/tmp/school',
mode    => '0744',
owner   => 'www-data',
group   => 'www-data',
content => 'I love Puppet'
}
