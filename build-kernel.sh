#fakeroot make-kpkg --initrd --append-to-version=25jan17 kernel-image kernel-headers
sudo fakeroot make-kpkg --initrd --append-to-version=$1 kernel-image kernel-headers
