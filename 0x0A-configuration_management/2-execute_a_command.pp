# executing a command
exec { 'killer':
  command => 'pkill killmenow',
  onlyif  => 'test `pgrep killmenow`'
}
