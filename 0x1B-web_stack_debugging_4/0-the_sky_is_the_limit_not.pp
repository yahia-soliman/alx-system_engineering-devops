# executing a command
exec { 'increase ULIMIT':
  command => "sed -i 's/15/1024/g' nginx",
  cwd     => '/etc/default/',
  path    => ['/usr/bin', '/bin']
}
