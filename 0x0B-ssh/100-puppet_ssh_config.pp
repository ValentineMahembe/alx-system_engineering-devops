#Configure ssh using puppet

file_line { 'Declare identity file':
  path => '/etc/ssh/ssh_config',
  line => '  IdentityFile ~/.ssh/school',
  match => '^  IdentityFile',
  ensure => 'present',
}

file_line { 'Turn off passwd auth':
  path => '/etc/ssh/ssh_config',
  line => '  PasswordAuthentication no',
  match => '^  PasswordAuthentication',
  ensure => 'present',
}
