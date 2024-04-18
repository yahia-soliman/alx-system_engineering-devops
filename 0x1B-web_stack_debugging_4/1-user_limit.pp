# executing a command
exec { 'delete hoberton limits':
  command => "sed -i '/holberton/d' limits.conf",
  cwd     => '/etc/security/',
  path    => ['/usr/bin', '/bin']
}
