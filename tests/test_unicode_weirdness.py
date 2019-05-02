# coding=utf-8
# Copyright 2019 Ram Rachum and collaborators.
# This program is distributed under the MIT license.

import io
import textwrap

from python_toolbox import sys_tools
from python_toolbox import temp_file_tools
from pysnooper.third_party import six
import pytest

import pysnooper
from pysnooper.third_party import six
from .utils import (assert_output, VariableEntry, CallEntry, LineEntry,
                    ReturnEntry, OpcodeEntry, ReturnValueEntry, ExceptionEntry)


def test_unicode_weirdness():
    weird_string = 's*&F.。、]}】df'

    @pysnooper.snoop()
    def foo():
        d = weird_string
        return d


    with sys_tools.OutputCapturer(stdout=False,
                                  stderr=True) as output_capturer:
        result = foo()
    assert result == weird_string
    output = output_capturer.string_io.getvalue()
    # assert_output(
        # output,
        # (
            # VariableEntry('Foo'),
        # )
    # )





