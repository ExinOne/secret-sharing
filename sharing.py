#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2019 Exin <robin@exin.one>
#
# Distributed under terms of the MIT license.
#
# Desc: Exin Secret Sharing based on Shamir's Secret Sharing Scheme
# User: Robin@Exin
# Date: 2019-08-18
# Time: 11:39:30

import sys
import argparse
from secretsharing import PlaintextToHexSecretSharer

def cmdline_args():
    p = argparse.ArgumentParser(description=
        """
        Exin Secret Sharing based on Shamir's Secret Sharing Scheme.
        """,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    p.add_argument("-s", "--split", action='store_true',
                   help="split private key")
    p.add_argument("-r", "--recover", action='store_true',
                   help="recover private key")
    p.add_argument("-k", "--keyfile", type=str, dest='keyfile',
                   help="private key or something sensitive file")
    p.add_argument("-m", "--min", type=int, choices=[2,3], default=3,
                   dest='min', help="multisig min")
    p.add_argument("-x", "--max", type=int, choices=[3,5], default=5,
                   dest='max', help="multisig max")

    return(p.parse_args())

# split private key, put your private key in key.log
def split(args):
    keyfile = args.keyfile
    min = args.min
    max = args.max

    print("Keep or send one or more subkey securely.\n")
    with open(keyfile, 'r') as filehandle:
        key = filehandle.read()
        shares = PlaintextToHexSecretSharer.split_secret(key, min, max)
        for share in shares:
            print(share)

# recover private key, put your subkey in key.log
def recover(args):
    min = args.min
    keyfile = args.keyfile

    parts = []
    for line in open(keyfile):
        parts.append(line.rstrip('\n'))

    result = PlaintextToHexSecretSharer.recover_secret(parts[0:min])
    print("The full private key is: " + result.rstrip('\n'))

def main():
    if sys.version_info<(3,0,0):
        sys.stderr.write("You need python 3.0 or later to run this script\n")
        sys.exit(1)

    try:
        args = cmdline_args()
        isSplit = args.split
        isRecover = args.recover

        if isSplit:
            split(args)
        elif isRecover:
            recover(args)
        else:
            pass
    except:
        print('Try python <script_name> -s/-r')

if __name__ == "__main__":
    main()