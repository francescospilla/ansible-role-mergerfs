import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_files_on_disks(host):
    files = ['/mnt/disk' + str(i) + '/file-' + str(i) for i in range(1, 4)]

    files_on_host = [host.file(path) for path in files]

    for file in files_on_host:
        assert file.exists


def test_files_on_union(host):
    files = ['/mnt/mergeunion/file-' + str(i) for i in range(1, 4)]

    files_on_host = [host.file(path) for path in files]

    for file in files_on_host:
        assert file.exists
