# -*- coding: utf-8 -*-
import copy
import os
import time

import pyperclip
from wox import Wox

result_template = {
    'Title': '{}',
    'SubTitle': '+++ Click To Copy It +++',
    'IcoPath': 'time.png',
    'JsonRPCAction': {
        'method': 'copy_to_clipboard',
        'parameters': ['{}'],
    }
}


class WoxGetCurrentTime(Wox):
    def query(self, query):
        now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        res = copy.deepcopy(result_template)
        res['Title'] = res['Title'].format(now)
        res['JsonRPCAction']['parameters'][0] = res['JsonRPCAction']['parameters'][0].format(now)

        return [res]

    def copy_to_clipboard(self, value):
        """
        Copies the given value to the clipboard.
        WARNING:Uses yet-to-be-known Win32 API and ctypes black magic to work.
        """
        try:
            pyperclip.copy(value)
        except IOError:
            command = 'echo ' + value + '| clip'
            os.system(command)


if __name__ == "__main__":
    WoxGetCurrentTime()
