# Project raspberry-pico 

First development, aiming to automate fan speed depending on temperature.

## Description

Getting familiar with the hardware and software. Implementation of a python toolkit containing most useful methods. Concret use case prototyping: temperature driven 

## Getting Started

### Dependencies

* Use ressources folder to get the necessary GUI (Thonny) as well as the binary


### Installing

1. Press the boot button on the rapsberry pico and plug in to computer
2. Copy the .uf2 binary on the device
3. Use instructions from [Bibliography(2.)](https://www.electroniclinic.com/raspberry-pi-pico-rp2040-programming-in-micropython-with-examples/) to install modules if needed (OLED Display eg.)
4. install Thonny (available from /ressources)

### Executing program

* How to run the program
* Step-by-step bullets
```
code blocks for commands
```

### Hardware setup

* See figure bellow to use the correct pins:
<img src="raspberry-pi-pico-gpio.png" width="500" height="300"/>

## Help

Advise for common issues:
- issue with oled display: make sure the i1c wires are connected to the right outputs
```
command to run if program contains helper info
```

## Authors

Contributors names and contact info:

Jean Boehm [@jboehm1](https://github.com/jboehm1) All rights reserved

## Version History

* 0.2
    * Various bug fixes and optimizations
    * See [commit change]() or See [release history]()
* 0.1
    * Initial Release

## License

This project is licensed under the [NAME HERE] License - see the LICENSE.md file for details

## Bibliography

Inspiration, code snippets, etc.
1. [Build a weather station with pico](https://www.youtube.com/watch?v=vfp0B1IW7yI&list=LL&index=2&ab_channel=WexterHome) ( using "def" and main() )
2. [Easy intro course to pico](https://www.electroniclinic.com/raspberry-pi-pico-rp2040-programming-in-micropython-with-examples/)
