#!/bin/bash
###setting hostname
printf "\nEnter Hostname:"
read hostname
echo $hostname /etc/hostname
##create user name
groupadd admin
useradd -g admin vals
passwd vals
###add to sudo
echo "%admin  ALL=(ALL) ALL" >>/etc/sudoers
su - vals
