Ansible configuration for LinuxFR.org
=====================================

Prerequisites:

* A working libvirt/kvm installation on your computer, including virtinst;
* Ansible installed on your computer;
* About 5 GB of available disk space and 500 MB of RAM for the VM;
* This repository.

To install the requirements on Debian Sid (instructions are probably similar
with other distributions):

    # apt-get install qemu-kvm libvirt-bin virt-manager virtinst ansible
    # sudo adduser <your user> libvirt

Instructions to set up a [linuxfr.org](http://linuxfr.org) development server
using the Ansible configuration from this repository:

1. Create a new virtual machine with Debian Wheezy by running
   './preseed/install.py dlfp-dev'
2. Ensure the virtual machine is reachable using SSH
3. Put the IP address of the virtual machine in the 'hosts' file in this
   directory.
4. Run 'ansible-playbook -k -i hosts site.yml'
5. Follow the instructions from the linuxfr.org repository to create the
   first user.
6. Profit!

Description of the available Ansible roles:

* common: common stuff to have ansible work as expected.
* base: base configuration for the linuxfr server.
* img: the image cacher.
* linuxfr: the actual web site.

Some variables are defined in vars/default.yml, you can override them
by host or using a group. Have a look at the
[Ansible documentation](http://docs.ansible.com/intro_inventory.html).
