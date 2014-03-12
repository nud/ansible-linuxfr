#!/usr/bin/python

import os
import sys

if len(sys.argv) < 2:
    print("Usage: %s <hostname>" % sys.argv[0])
    sys.exit(1)

HOSTNAME = sys.argv[1]
DOMAIN_NAME = 'linuxfr.org'
PRESEED_TEMPLATE = os.path.join(os.path.dirname(sys.argv[0]), 'preseed-vm-wheezy.cfg.j2')

HYPERVISOR='qemu:///system'
NETWORK='bridge:virbr0'

DISTRO='wheezy'
ARCH='amd64'


import jinja2
import os
import shutil
import subprocess
import tempfile


tempdir = tempfile.mkdtemp('preseed')

template_vars = {
    'hostname': HOSTNAME,
    'domain_name': DOMAIN_NAME,
    'password': 'root'
}

cmd = [
    '/usr/bin/virt-install',
    '--connect=%s' % HYPERVISOR,
    '--location=http://ftp.fr.debian.org/debian/dists/%s/main/installer-%s' % (DISTRO, ARCH),
    '--initrd-inject=%s' % os.path.join(tempdir, 'preseed.cfg'),
    '--name=%s' % HOSTNAME,
    '--ram=512',
    '--disk=pool=default,size=4,format=raw,bus=virtio',
    '--network=%s' % NETWORK,
    '--extra-args=auto'
]

print("Running %s" % ' '.join(cmd))

template = jinja2.Template(open(PRESEED_TEMPLATE).read())
open(os.path.join(tempdir, 'preseed.cfg'), 'w').write(template.render(template_vars))

subprocess.call(cmd)

shutil.rmtree(tempdir)
