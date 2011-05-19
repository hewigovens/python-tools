#!/usr/bin/env python
# coding:utf-8

import sys, os, re
import distutils.core, py2exe
import optparse
import shutil

manifest_template = '''
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0">
<assemblyIdentity
    version="5.0.0.0"
    processorArchitecture="x86"
    name="%(prog)s"
    type="win32"
/>
<description>%(prog)s Program</description>
<dependency>
    <dependentAssembly>
        <assemblyIdentity
            type="win32"
            name="Microsoft.Windows.Common-Controls"
            version="6.0.0.0"
            processorArchitecture="X86"
            publicKeyToken="6595b64144ccf1df"
            language="*"
        />
    </dependentAssembly>
</dependency>
</assembly>
'''

RT_MANIFEST = 24

class Py2exeUPX(py2exe.build_exe.py2exe):
    '''from http://www.py2exe.org/index.cgi/BetterCompression'''
    def initialize_options(self):
        # Add a new "upx" option for compression with upx
        py2exe.build_exe.py2exe.initialize_options(self)
        self.upx = 1
    def copy_file(self, *args, **kwargs):
        # Override to UPX copied binaries.
        (fname, copied) = result = py2exe.build_exe.py2exe.copy_file(self, *args, **kwargs)
        basename = os.path.basename(fname)
        if (copied and self.upx and
            (basename[:6]+basename[-4:]).lower() != 'python.dll' and
            fname[-4:].lower() in ('.pyd', '.dll')):
            os.system('upx --best "%s"' % os.path.normpath(fname))
        return result
    def patch_python_dll_winver(self, dll_name, new_winver=None):
        # Override this to first check if the file is upx'd and skip if so
        if not self.dry_run:
            if not os.system('upx -qt "%s" >nul' % dll_name):
                if self.verbose:
                    print "Skipping setting sys.winver for '%s' (UPX'd)" % \
                          dll_name
            else:
                py2exe.build_exe.py2exe.patch_python_dll_winver(self, dll_name, new_winver)
                # We UPX this one file here rather than in copy_file so
                # the version adjustment can be successful
                if self.upx:
                    os.system('upx --best "%s"' % os.path.normpath(dll_name))

def optparse_options_to_dist_options(filename, options):
    basename = os.path.splitext(os.path.basename(filename))[0]

    mode = 'windows' if options.windowed else 'console'
    mode_options = {'script'          : filename,
                    'version'         : options.version or '1.0',
                    'name'            : options.name or basename,
                    'company_name'    : options.company or None,
                    'icon_resources'  : [(1, options.icon)] if options.icon else [],
                    'other_resources' : [(RT_MANIFEST, 1, manifest_template % dict(prog=basename))] if mode == 'windows' else [],
                    }

    py2exe_options = {'dist_dir'     : 'dist',
                      'compressed'   : 1,
                      'optimize'     : 1,
                      'dll_excludes' : ['w9xpopen.exe', 'MSVCP90.dll', 'mswsock.dll', 'powrprof.dll'],
                      'ascii'        : options.ascii or False,
                      'bundle_files' : options.bundle or 3,
                     }

    zipfile = options.zipfile
    cmdclass = Py2exeUPX if options.upx else py2exe.build_exe.py2exe

    return { mode      :  [mode_options],
            'zipfile'  :  zipfile,
            'options'  :  {'py2exe' : py2exe_options},
            'cmdclass' :  {'py2exe' : cmdclass},
            }

def finalize(windows=None, console=None, service=None, com_server=None, ctypes_com_server=None, zipfile=None, options=None, cmdclass=None):
    shutil.rmtree('build')
    mode = [x for x in (windows, console, service, com_server, ctypes_com_server) if x is not None][0][0]
    py2exe_options = options['py2exe']
    basename = os.path.splitext(os.path.basename(mode['script']))[0]
    if py2exe_options['bundle_files'] == 1 and zipfile is None:
        exefile = '%s.exe' % basename
        dist_dir = py2exe_options.get('dist_dir', 'dist')
        shutil.move(os.path.join(dist_dir, exefile), exefile)
        shutil.rmtree(dist_dir)

def main():
    parser = optparse.OptionParser(usage='usage: %prog [options] filename')
    parser.add_option("-w", "--windowed", dest="windowed", action="store_true", default=False, help="Use the Windows subsystem executable.")
    parser.add_option("-a", "--ascii",    dest="ascii",    action="store_true", default=False, help="do not include encodings.")
    parser.add_option("-b", "--bundle",   dest="bundle",   type="int",    metavar="LEVEL",  help="produce a bundle_files deployment.")
    parser.add_option("-v", "--version",  dest="version",  type="string", metavar="number", help="add version number to the executable.")
    parser.add_option("-n", "--name",     dest="name",     type="string", help="add name string to the executable.")
    parser.add_option("-c", "--company",  dest="company",  type="string", help="add company string to the executable.")
    parser.add_option("-i", "--icon"   ,  dest="icon",     type="string", metavar="file.ico", help="add file.ico to the executable's resources.")
    parser.add_option("-z", "--zipfile",  dest="zipfile",  type="string", metavar="file.zip", help="add file.zip to the extra resources.")
    parser.add_option("-X", "--upx"   ,   dest="upx",      action="store_true", default=False, help="if you have UPX installed (detected by Configure), this will use it to compress your executable.")

    options, args = parser.parse_args()
    if len(args) == 0:
        parser.print_help()
        sys.exit(0)
    else:
        print options, args

    filename = args[0]
    dist_options = optparse_options_to_dist_options(filename, options)
    print dist_options

    sys.argv[1:] = ['py2exe', '-q']
    distutils.core.setup(**dist_options)
    finalize(**dist_options)

    if sys.version_info[:2] > (2, 5):
        print "you need vc2008redist['Microsoft.VC90.CRT.manifest', 'msvcr90.dll']"

if __name__ == '__main__':
    main()