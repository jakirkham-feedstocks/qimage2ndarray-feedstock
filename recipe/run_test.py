# Need to import Python-bindings first
# so that qimage2ndarray recognizes them.
import PyQt5
import qimage2ndarray

import os
import sys

import nose

sys.path.append(os.path.join(os.getcwd(), "test"))
nose.main("test")
