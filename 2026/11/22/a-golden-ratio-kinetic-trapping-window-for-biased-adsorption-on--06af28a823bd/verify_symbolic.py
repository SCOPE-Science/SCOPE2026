#!/usr/bin/env python3
"""Optional SymPy certificate for the explicit algebraic identities."""
import sympy as s
N, w, c = s.symbols('N w c', positive=True)
sfirst = 2*w/(N-2+2*w)
p = sfirst*(w/((w+1)*(1+(N-3)*w))+w/((w+1)*(w+N-3))) + (1-sfirst)*(w*w+N-3)/(w+N-3)**2
f = c*c/((1+2*c)*(1+c)**2)
assert s.simplify(p.subs(w,1)-1/(N-2))==0
assert s.simplify(s.limit(p.subs(w,c*N),N,s.oo)-f)==0
assert s.simplify(s.diff(f,c)/f-2*(1+c-c*c)/(c*(1+c)*(1+2*c)))==0
phi=(1+s.sqrt(5))/2
assert s.simplify(f.subs(c,phi)-(5*s.sqrt(5)-11)/2)==0
print('PASS: unbiased identity, linear-bias limit, derivative, golden-ratio maximum')
