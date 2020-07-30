---
layout: post
title: "Short Notes and Snippets"
date: 2020-07-30
---

### Connecting to WiFi on Startup

* `sudo apt install network-manager nm-tray`
* add `exec --no-startup-id /usr/bin/nm-tray` to `~/.config/i3/config`
* configure nm-tray to auto-connect to preferred WiFi

### Do Not Require Sudo Password for a Given Command
* `sudo visudo`
* add line `<username> ALL = NOPASSWD: <command1>, <command2>` to end of file
* use full command path (from `which`)
