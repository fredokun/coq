Name: coq_ext_for_pcoq
Version: 8.0
Release: 1
Summary: The Coq Extension for Pcoq
Copyright: freely redistributable
Group: Applications/Math
Vendor: INRIA & LRI
URL: http://coq.inria.fr
Source: ftp://ftp.inria.fr/INRIA/coq/V8.0/coq-8.0.tar.gz
Icon: petit-coq.gif
Requires: coq = 8.0
BuildRoot: /var/tmp/pcoq

%description
The Coq Extension for Pcoq provides all facilities to interface Coq with
Pcoq

%define debug_package %{nil}

%prep
%setup -n coq-8.0

%build
./configure -bindir %{_bindir} -libdir %{_libdir}/coq -mandir %{_mandir} \
   -emacslib %{_datadir}/emacs/site-lisp \
   -coqdocdir %{_datadir}/texmf/tex/latex/misc \
   -opt -reals all -coqide no
make pcoq

%clean
rm -rf %{buildroot}
make clean

%install
rm -rf %{buildroot}
make -e COQINSTALLPREFIX=%{buildroot} install-pcoq

%files
%{_bindir}/*
%{_mandir}/man1/*

%defattr(-,root,root)
