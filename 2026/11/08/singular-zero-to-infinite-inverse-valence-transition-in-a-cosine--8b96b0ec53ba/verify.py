#!/usr/bin/env python3
"""Standalone checks for the positive-preimage asymptotics of the cosine-flux Chialvo map.
Scientific evidence only; the all-parameter claim is proved analytically.
"""
import math
from scipy.optimize import brentq
from fractions import Fraction
import sympy as sp

def check():
    x, r, k, k0, k1, k2, ph, X, Phi = sp.symbols('x r k k0 k1 k2 ph X Phi', real=True)
    f1 = x*x*sp.exp(r-x)+k0+k*x*sp.cos(sp.pi*ph)
    f2 = k1*x-k2*ph
    Jac = sp.det(sp.Matrix([[sp.diff(f1,x),sp.diff(f1,ph)],[k1,-k2]]))
    induced = f1.subs(ph, (k1*x-Phi)/k2)
    assert sp.simplify(Jac.subs(ph, (k1*x-Phi)/k2)+k2*sp.diff(induced,x)) == 0
    assert sp.simplify(sp.diff(f1,ph)+sp.pi*k*x*sp.sin(sp.pi*ph)) == 0
    numerical = 0
    for kk in (0.05,0.7,-0.3):
      for a,b in ((0.2,0.7),(0.9,0.15),(1.3,2.2)):
       for rr,kb,tx,tp in ((-3,0.1,2.0,0.2),(0.5,2.1,-10.,-3.1)):
        for j in range(5000,5031):
          z = (tp+b*(j+0.5))/a
          def fun(xx):
            p=(a*xx-tp)/b
            return xx*xx*math.exp(rr-xx)+kb+kk*xx*math.cos(math.pi*p)-tx
          left=(tp+b*j)/a
          right=(tp+b*(j+1))/a
          if left<0: continue
          assert fun(left)*fun(right) < 0
          root = brentq(fun,left,right,xtol=1e-11)
          p=(a*root-tp)/b
          assert root>0 and p>0
          assert abs(fun(root)) < 5e-7 + 1e-9*abs(kk)*root
          leading = z + ((-1)**(j+1))*(tx-kb)*b/(math.pi*kk*a*z)
          assert abs(root-leading) <= 1000.0/z**2 + 1e-7
          jac = -b*((2-root)*root*math.exp(rr-root)+kk*math.cos(math.pi*p)) + math.pi*kk*a*root*math.sin(math.pi*p)
          assert abs(jac)>1e-3
          numerical +=1
    print('VERIFY_OK symbolic_Jacobian_identity=1 asymptotic_regular_positive_preimages=',numerical)
if __name__=='__main__': check()
