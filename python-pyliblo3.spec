Name:		python-pyliblo3
Version:	0.16.3
Release:	1
Source0:	https://github.com/gesellkammer/pyliblo3/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Summary:	Python bindings for the liblo OSC library
URL:		https://github.com/gesellkammer/pyliblo3
License:	LGPL-2.1
Group:		Development/Python

BuildRequires:  pkgconfig(liblo)
BuildRequires:  python%{pyver}dist(cython)

BuildSystem:    python

%description
Python bindings for the liblo OSC library

%files
%{_bindir}/__pycache__/dump_osc.cpython-311.pyc
%{_bindir}/__pycache__/send_osc.cpython-311.pyc
%{_bindir}/dump_osc.py
%{_bindir}/send_osc.py
%{py_platsitedir}/%{uname}-%{version}.dist-info/INSTALLER
%{py_platsitedir}/%{uname}-%{version}.dist-info/METADATA
%{py_platsitedir}/%{uname}-%{version}.dist-info/RECORD
%{py_platsitedir}/%{uname}-%{version}.dist-info/REQUESTED
%{py_platsitedir}/%{uname}-%{version}.dist-info/WHEEL
%{py_platsitedir}/%{uname}-%{version}.dist-info/direct_url.json
%{py_platsitedir}/%{uname}-%{version}.dist-info/licenses/COPYING
%{py_platsitedir}/%{uname}-%{version}.dist-info/top_level.txt
%{py_platsitedir}/%{uname}/__init__.py
%{py_platsitedir}/%{uname}/__pycache__/__init__.cpython-311.pyc
%{py_platsitedir}/%{uname}/_liblo.cpython-311-x86_64-linux-gnu.so
%{py_platsitedir}/%{uname}/_liblo.pyi
