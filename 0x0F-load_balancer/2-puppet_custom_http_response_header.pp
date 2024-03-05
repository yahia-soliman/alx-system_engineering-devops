# setup loadbalancer with HAProxy
include stdlib

file_line {'custom_header':
  ensure => 'present',
  path   => 'etc/nginx/sites-available/default',
  line   => '	add_header X-Served-By ${HOSTNAME};'
}
package { 'nginx':
  ensure   => installed,
  name     => 'nginx',
  provider => 'apt'
}
service { 'nginx':
  ensure  => running,
  name    => 'nginx',
  restart => ''
}
