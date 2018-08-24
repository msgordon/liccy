from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

setup(name='liccy',
      version='0.1',
      description="Stand-alone version of yt/scipy's cython line integral convolution implementation",
      author='Michael Gordon',
      author_email='msgordon.astro@gmail.com',
      cmdclass = {'build_ext': build_ext},
      ext_modules = [Extension("liccy",
                               ["liccy.pyx"])]
)
