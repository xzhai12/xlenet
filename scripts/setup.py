
from distutils.core import setup, Extension
from Cython.Build import cythonize
import numpy as np

ext = Extension("cy_regularized_linreg",
                sources=["cy_regularized_linreg.pyx","cpp_regularized_linreg.cpp"],
                libraries=["m"],
                language=["c++"],
                extra_compile_args=["-std=c++11","-static"])

setup(name = "cy_regul_linreg",
      ext_modules = cythonize(ext))
