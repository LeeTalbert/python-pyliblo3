Name:		python-pyliblo3
Version:	0.16.3
Release:	1
Source0:	https://github.com/gesellkammer/pyliblo3/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Summary:	Python bindings for the liblo OSC library
URL:		https://github.com/gesellkammer/pyliblo3
License:	LGPL-2.1
Group:		Development/Python

BuildRequires:  lib64lo-devel
BuildRequires:  python-cython0

BuildSystem:	python

%description
Python bindings for the liblo OSC library

%files
%{_bindir}/__pycache__/dump_osc.cpython-311.pyc
%{_bindir}/__pycache__/send_osc.cpython-311.pyc
%{_bindir}/dump_osc.py
%{_bindir}/send_osc.py
%{py_platsitedir}/pyliblo3-0.16.3.dist-info/INSTALLER
%{py_platsitedir}/pyliblo3-0.16.3.dist-info/METADATA
%{py_platsitedir}/pyliblo3-0.16.3.dist-info/RECORD
%{py_platsitedir}/pyliblo3-0.16.3.dist-info/REQUESTED
%{py_platsitedir}/pyliblo3-0.16.3.dist-info/WHEEL
%{py_platsitedir}/pyliblo3-0.16.3.dist-info/direct_url.json
%{py_platsitedir}/pyliblo3-0.16.3.dist-info/licenses/COPYING
%{py_platsitedir}/pyliblo3-0.16.3.dist-info/top_level.txt
%{py_platsitedir}/pyliblo3/__init__.py
%{py_platsitedir}/pyliblo3/__pycache__/__init__.cpython-311.pyc
%{py_platsitedir}/pyliblo3/_liblo.cpython-311-x86_64-linux-gnu.so
%{py_platsitedir}/pyliblo3/_liblo.pyi
