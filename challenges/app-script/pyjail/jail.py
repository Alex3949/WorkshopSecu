#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sys, cmd, os
from hashlib import md5
from random import random

"""
Author: zM
Desc: PyJail challenge for root-me.org
"""


intro   = """                     __     _ __
       ___  __ ____ / /__ _(_) /\tWelcome on PyJail
      / _ \/ // / // / _ `/ / /
     / .__/\_, /\___/\_,_/_/_/  \tUse getout() function if you want to
    /_/   /___/                 \tescape from here and get the flag !\n"""

passwd = md5(str(random())).hexdigest()

#del __builtins__.__dict__['__import__']
del __builtins__.__dict__['eval']
del __builtins__.__dict__['execfile']
del __builtins__.__dict__['input']

def execute(command):
    def getout(password):
        """ check if arg is equal to the random password """
        if(password == passwd):
            print "Well done ! Here is your so desired flag : "
            os.system("cat flag")
            print
            sys.exit()
        else:
            print "Hum ... no."

    exec(command) in locals()

class Jail(cmd.Cmd):

    prompt     = '>>> '
    filtered    = '\'|"|.|input|if|else|eval|exit|import|quit|exec|code|const|vars|str|chr|ord|local|global|join|format|replace|translate|try|except|with|content|frame|back'.split('|')

    def do_EOF(self, line):
        sys.exit()

    def emptyline(self):
        return cmd.Cmd.emptyline(self)

    def default(self, line):
        sys.stdout.write('\x00')

    def postcmd(self, stop, line):
        if any(f in line for f in self.filtered):
            print "You're in jail dude ... Did you expect to have the key ?"
        else:
            try:
                execute(line)
            except NameError:
                print "NameError: name '%s' is not defined" % line
            except Exception:
                print "Error: %s" % line
        return cmd.Cmd.postcmd(self, stop, line)

if __name__ == "__main__":
    try:
        Jail().cmdloop(intro)
    except KeyboardInterrupt:
        print "\rBye bye !"
