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

## How to build

Run the following commands from the project root folder

    make raspberrypi_minimal_mpd_defconfig
    make

## How to flash to SD card

    sudo dd if=output/images/sdcard.img of=/dev/sdX

