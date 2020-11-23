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

### Emacs Notes
* `C-x C-c` - save files and close session
* `C-x C-f` - open file
* `C-x C-s` - save file
* `C-x 0` - kill window
* `C-x left/right` - switch buffer
* `C-g` - abort partially entered command
* `C-x k` - kill buffer
* `M-f / M-b` - move a word forward/backward
* `M-< / M->` - move to beginning/end
* `C-c .` - insert date
* `C-u C-c .` - insert timestamp
* `S-left/right` - move between todo states
* `M-S-up/down` - move line up/down
* `C-Enter` - new line item
* `C-x b` - open buffer
* `C-c C-x C-a` - archive item
