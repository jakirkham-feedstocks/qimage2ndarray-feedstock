# Need to import Python-bindings first
# so that qimage2ndarray recognizes them.
import PyQt5
import qimage2ndarray

import nose

nose.main("test")
