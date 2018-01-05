# Buildroot Quick-Pi

A super stripped down Raspberry Pi Web Radio image

## Introduction

[Buildroot](https://buildroot.org/) is a simple, efficient and easy-to-use tool
to generate embedded Linux systems through cross-compilation.

## QuickPi config

This is a buildroot configuration optimized for Raspberry Pi 1. The kernel has
been extremely stripped down to optimize boot times without having to go to a
custom init system. Measured boot time with a 1GB Sandisk Extreme III SD Card
from plug in to login prompt is around 5.5 seconds, with mpd and DHCP based
Ethernet configuration it takes around 10 seconds till the webradio is playing.

## Note

The image assumes an Adafruit compatible LCD Keypad

    https://learn.adafruit.com/adafruit-16x2-character-lcd-plus-keypad-for-raspberry-pi

If it is not installed please remove the related init script

    rm board/raspberrypi/overlay/etc/init.d/S97lcd

before beginning with the build process

## How to build

Run the following commands from the project root folder:

For Raspberry Pi 1

    make raspberrypi_minimal_mpd_defconfig

For Raspberry Pi 3

    make raspberrypi3_minimal_mpd_defconfig

Now run

    make

and you may get a cup of tea or coffee because this takes some time.

## How to flash to SD card

Be careful with the dd command otherwise you might overwrite some important data!
Plug the SD card into the card reader find out the correct device /dev/sdX and run

    sudo dd if=output/images/sdcard.img of=/dev/sdX
    sync

After flashing insert the SD card into you Raspberry and power it up.
