# -*- mode: python -*-
# This file is released under public domain
# Code 'extra_datas' is copied from StackOverflow:Q11322538.

import os
import site
import sys

PYTHON3 = (sys.version[0] == '3')
if PYTHON3:
    unicode = str

block_cipher = None

#if PYTHON3:
typelib_path = os.path.join(site.getsitepackages()[1], 'gi')
#else:
#    typelib_path = os.path.join(site.getsitepackages()[1], 'gnome','lib','girepository-1.0')

binaries=[(os.path.join(typelib_path, tl), 'gi_typelibs') for tl in os.listdir(typelib_path)]

a = Analysis(['ezhuthi.py'],
             pathex=[os.getcwd()],
             binaries=binaries,
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)

def extra_datas(mydir):
    def rec_glob(p, files):
        import os
        import glob
        for d in glob.glob(p):
            if os.path.isfile(d):
                files.append(d)
            rec_glob("%s/*" % d, files)
    files = []
    rec_glob("%s/*" % mydir, files)
    extra_datas = []
    for f in files:
        extra_datas.append((f, f, 'DATA'))

    return extra_datas
###########################################

# append the 'data' dir
a.datas += extra_datas('res')
a.datas += extra_datas('examples')
a.datas += extra_datas('xmlbook')

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='ezhuthi',
          debug=False,
          strip=False,
          upx=True,
          console=False , icon='ezhil16.ico')

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='ezhuthi')
