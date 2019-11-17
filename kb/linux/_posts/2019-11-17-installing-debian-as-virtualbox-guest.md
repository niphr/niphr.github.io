---
layout: post
title: "Installing Debian as VirtualBox guest"
date: 2019-11-17
---
Notes from the last installation of Debian 10 guest inside Win10 host. Goal was to have a lightweight desktop environment intended mostly for programming and studying.

### VirtualBox settings
* at least 30 GB for guest partition
* increase processor count (to at least 2)
* max out graphics memory
* set graphics controller to VBoxSVGA
* allow 3D acceleration
* disable shared folders and clipboard (security)

### After installation
#### Install sudo
```
su
apt install sudo
usermod -aG sudo <username>
```
Then login and logout for changes to take effect.

#### Install VirtualBox Guest Additions
```
sudo apt install build-essential module-assistant
sudo m-a prepare
<VirtualBox menu -> Insert Guest Additions CD>
<Navigate to CD folder, probably in /media/cdrom0. If the folder seems empty, try opening it in file manager - no idea why, but it made the files appear.>
sudo sh ./VBoxLinuxAdditions.run
reboot
```

#### Make sure NumLock is turned on during boot
In host:
```
VBoxManage.exe setextradata <machineName> GUI/HidLedsSync "0"
```

In guest:
```
sudo apt install numlockx
<Add "numlockx on" to applications run on startup - Xfce settings.>
```

#### Set terminal color theme
Gruvbox - [Github](https://github.com/morhetz/gruvbox-contrib/tree/master/xfce4-terminal)

#### Install essential packages
```
sudo apt install vim emacs git keepass2 tmux
```

#### Configure git
```
git config --global user.email "<email>"
git config --global user.name "<name surname>"
```