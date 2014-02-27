Ansible configuration for LinuxFR.org
=====================================

Instructions to set up a linuxfr.org development server:

1. Create a new virtual machine with Debian Wheezy by running
   './preseed/install.py dev'
2. Ensure the virtual machine is reachable using SSH
3. Put the IP address of the virtual machine in the 'hosts' file in this
   directory.
4. Run 'ansible-playbook -k -i hosts site.yml'
5. Profit!
