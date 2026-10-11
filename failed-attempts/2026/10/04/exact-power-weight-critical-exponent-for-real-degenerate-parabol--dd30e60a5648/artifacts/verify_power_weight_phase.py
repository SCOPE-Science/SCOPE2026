#!/usr/bin/env python3
import sympy as sp
n,beta,p=sp.symbols('n beta p', positive=True)
# Use b=-beta>0 for the negative-power regime.
b=sp.symbols('b', positive=True)
pcrit=2*n/(2*n-b)
pconj=sp.simplify(pcrit/(pcrit-1))
assert sp.simplify(pconj-2*n/b)==0
# Substitute beta=-b: pcrit=2n/(2n+beta).
q=sp.symbols('q', positive=True)
qprime=q/(q-1)
# For q>1, b*q/(2*(q-1))<n is equivalent to q>2*n/(2*n-b) when 0<b<n.
assert sp.simplify((2*n-b)*pcrit-2*n)==0
# Critical Sobolev identity.
bcrit=n**2/(n+2)
twostar=2*(n+2)/(n+4)
assert sp.simplify(pcrit.subs(b,bcrit)-twostar)==0
# At beta=-bcrit, beta*(1+2/n)=-n.
assert sp.simplify((-bcrit)*(1+sp.Rational(2,1)/n)+n)==0
print('VERIFY_OK')
print('negative-power pcrit = 2*n/(2*n-b)')
print('conjugate pcrit = 2*n/b')
print('critical b = n^2/(n+2) gives 2_* = 2(n+2)/(n+4)')
