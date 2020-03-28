# Exin Secret Sharing

> Exin Secret Sharing based on Shamir's Secret Sharing Scheme.

[![Build Status](http://img.shields.io/travis/badges/badgerbadgerbadger.svg?style=flat-square)](https://travis-ci.org/badges/badgerbadgerbadger) [![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Contributing](#contributing)
- [Team](#team)
- [FAQ](#faq)
- [Support](#support)
- [License](#license)

## Features

- Split private key into multisig
- Recover private key via multiple multisig subkey

## Installation

- Python 3.7+ required

### Clone

- Clone this repo to your server using:

``` bash
$ git clone https://github.com/ExinOne/secret-sharing
```

### Setup

Install related dependencies.

``` bash
$ apt-get -y install pip
$ pip install git+https://github.com/blockstack/secret-sharing
```

### Usage

``` bash
$ python sharing.py --help
usage: sharing.py [-h] [-s] [-r] [-k KEYFILE] [-m {2,3}] [-x {3,5}]

Exin Secret Sharing based on Shamir's Secret Sharing Scheme.

optional arguments:
  -h, --help            show this help message and exit
  -s, --split           split private key (default: False)
  -r, --recover         recover private key (default: False)
  -k KEYFILE, --keyfile KEYFILE
                        private key or something sensitive file (default:
                        None)
  -m {2,3}, --min {2,3}
                        multisig min (default: 3)
  -x {3,5}, --max {3,5}
                        multisig max (default: 5)
Try python <script_name> -s/-r
```

Create a file named `key.log` and put your private key in the file as a single line.

``` bash
$ touch key.log
$ vim key.log
```

Split private key into 3/5 multisig:

``` bash
$ python sharing.py -s -k key.log -m 3 -x 5
```

Recover private key via multiple multisig subkey(put your multiple subkey in `key.log` line by line, the example required 3 subkey):

``` bash
$ python sharing.py -r -k key.log -m 3
```

## Contributing

To be continued.

## Team

@Exin

## FAQ

To be continued.

## Support

Reach out to us at one of the following places!

- Website at <a href="https://exin.one" target="_blank">`exin.one`</a>
- Twitter at <a href="https://twitter.com/Exin_One" target="_blank">`@ExinOne`</a>
- Email at `robin@exin.one`

## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- **[MIT license](https://opensource.org/licenses/mit-license.php)**
- Copyright 2019 © <a href="https://exin.one" target="_blank">Exin</a>.