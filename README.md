Ansible Role: mergerfs
=========

A simple role for installing [_mergerfs_](https://github.com/trapexit/mergerfs) on supported platforms and manage mounting union filesystems.

Requirements
------------

None.

Role Variables
--------------

Available variables are listed below, along with default values (see `defaults/main.yml`):

````
unions: []
````
A list of unions to mount with _mergerfs_. See the commented example in `defaults/main.yml` for available options and the _mergerfs_ documentation for all the relevant [options](https://github.com/trapexit/mergerfs#options) and [policies](https://github.com/trapexit/mergerfs#functions--policies--categories).

````
unions:
  - mountpoint: "/mnt/union1"
    sources:
      - '/mnt/disk1'
      - '/mnt/disk2'
    opts: 'defaults,allow_other,direct_io,use_ino,category.create=eplfs,minfreespace=20G'
````
An example of a fully-populated union entry, mounting two source mounts into a single pool, with the default options and setting the **creation policy** to _**eplfs**_ and the **minimum free space** to keep to 20GB free space on each source mount.

Dependencies
------------

None.

Example Playbook
----------------

    - hosts: server
      roles:
        - role: mergerfs
          vars:
            unions:
              - { mountpoint: "/mnt/drivepool1", sources: ["/mnt/disk1", "/mnt/disk2"] }
              - mountpoint: "/mnt/drivepool2"
                sources:
                  - "/mnt/disk3"
                  - "/mnt/disk4"
                opts: defaults,allow_other,direct_io,use_ino,moveonenospc=true

Testing
-------

This role is manually tested with [Molecule](https://molecule.readthedocs.io/en/latest/) and [Docker](https://www.docker.com/) (check the `molecule` directory for the details). Automated CI testing is in the works.

This role is tested against the following platforms:

````
- name: CentOS
  versions:
    - 7
- name: Fedora
  versions:
    - 27
    - 29
- name: Debian
  versions:
    - jessie
    - stretch
- name: Ubuntu
  versions:
    - trusty
    - xenial
    - bionic
````

License
-------

MIT

Author Information
------------------

This role was created in 2018 by [Francesco Spilla](https://github.com/francescospilla/ansible-role-mergerfs).
