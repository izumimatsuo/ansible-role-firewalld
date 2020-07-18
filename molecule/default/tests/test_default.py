import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_firewalld_is_installed(host):
    package = host.package('firewalld')
    assert package.is_installed
    assert package.version.startswith("0.6")


def test_firewalld_running_and_enabled(host):
    service = host.service('firewalld')
    assert service.is_running
    assert service.is_enabled


def test_firewalld_rules(host):
    cmd = 'iptables -L INPUT_direct | grep '
    rule1 = cmd + '"tcp flags:FIN,SYN,RST,PSH,ACK,URG/NONE"'
    rule2 = cmd + '"tcp flags:!FIN,SYN,RST,ACK/SYN state NEW"'
    rule3 = cmd + '"tcp flags:FIN,SYN,RST,PSH,ACK,URG/FIN,SYN,RST,PSH,ACK,URG"'
    assert 0 == host.run(rule1).rc
    assert 0 == host.run(rule2).rc
    assert 0 == host.run(rule3).rc
    assert '' == host.check_output('firewall-cmd --list-services')


def test_fail2ban_is_installed(host):
    package = host.package('fail2ban')
    assert package.is_installed
    assert package.version.startswith("0.10")


def test_fail2ban_running_and_enabled(host):
    service = host.service('fail2ban')
    assert service.is_running
    assert service.is_enabled
