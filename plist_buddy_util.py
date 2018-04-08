#!/usr/bin/python3

import subprocess


class PlistBuddy:
    def __init__(self, plist):
        self.__plist = plist

    @property
    def plist(self):
        return self.__plist

    def _cmd(self, cmd, key, value):
        return ['/usr/libexec/PlistBuddy', '-c', '{0} :{1} {2}'.format(cmd, key, value), self.__plist]

    def _cmd_set(self, key, value):
        return self._cmd('Set', key, value)

    def _cmd_print(self, key):
        return self._cmd("Print", key, '')

    def set_value(self, key, value):
        subprocess.check_output(self._cmd_set(key, value))

    def get_value(self, key):
        out_bytes = subprocess.check_output(self._cmd_print(key))
        return out_bytes.decode('utf-8').rstrip()
