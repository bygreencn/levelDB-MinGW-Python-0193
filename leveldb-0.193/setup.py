#!/usr/bin/python

# Copyright (c) Arni Mar Jonsson.
# 
# Updates to setup.py/PyPi - Russell Power (power@cs.nyu.edu)
#
#
# See LICENSE for details.

import glob
import platform
import sys

from setuptools import setup, Extension

system,node,release,version,machine,processor = platform.uname()
common_flags = [
      '-I./leveldb',
      '-I./snappy',
      '-I.',
      '-fno-builtin-memcmp',
      '-O2',
      '-fPIC',
      '-DNDEBUG',
      '-DSNAPPY',
]

if system == 'Darwin':
  extra_compile_args = common_flags + [
      '-DOS_MACOSX',
      '-DLEVELDB_PLATFORM_POSIX',
      '-Wno-error=unused-command-line-argument-hard-error-in-future',
      ]
elif system == 'Linux':
  extra_compile_args = common_flags + [
      '-pthread',
      '-Wall', 
      '-DOS_LINUX',
      '-DLEVELDB_PLATFORM_POSIX',
      ]
else:
  extra_compile_args = common_flags
  extra_link_args = ['-L.',]

setup(
	name = 'leveldb',
	version = '0.193',
	maintainer = 'Arni Mar Jonsson',
	maintainer_email = 'arnimarkj@gmail.com',
	url = 'http://code.google.com/p/py-leveldb/',

	classifiers = [
		'Development Status :: 4 - Beta',
		'Environment :: Other Environment',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: BSD License',
		'Operating System :: POSIX',
		'Programming Language :: C++',
		'Programming Language :: Python',
		'Programming Language :: Python :: 2.4',
		'Programming Language :: Python :: 2.5',
		'Programming Language :: Python :: 2.6',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3.0',
		'Programming Language :: Python :: 3.1',
		'Programming Language :: Python :: 3.2',
		'Programming Language :: Python :: 3.3',
		'Topic :: Database',
		'Topic :: Software Development :: Libraries'
	],

	description = 'Python bindings for leveldb database library',

	ext_modules = [
		Extension('leveldb',
			sources = [
				# python stuff
				'leveldb_ext.cc',
				'leveldb_object.cc',
			],
			libraries = ['stdc++',],
			extra_compile_args = extra_compile_args,
			extra_link_args = extra_link_args + ['-lleveldb',]
		)
	]
)
