#!/usr/bin/env python3
"""Supplemental exact algebraic checks for the rational cap-averaging theorem."""
import sympy as s
import mpmath as mp
z,n=s.symbols('z n'); count=0
for m in (2,3,6):
 f=s.cyclotomic_poly(m,z)
 for r in range(m):
  p=(n-1)*(z**((r+1)%m)-1)-(n+1)*(z**(r%m)-z)
  rem=s.rem(p,f,z)
  for nn in range(2,60):
   if nn % m != r: continue
   if m==2:
    assert (s.simplify(rem.subs(n,nn))==0)==(r==1)
   else:
    assert s.Poly(rem.subs(n,nn),z)!=s.Poly(0,z)
   count+=1
mp.mp.dps=45
for den in (2,3,4,5,6,7,8,9,10,11,12,13):
 for num in range(1,den):
  if s.gcd(num,den)!=1: continue
  theta=mp.pi*num/den
  vol=theta/2-mp.sin(2*theta)/4
  for ell in range(1,29):
   lam=(mp.sin(ell*theta)/ell-mp.sin((ell+2)*theta)/(ell+2))/(2*(ell+1)*vol)
   lam_int=mp.quad(lambda t:mp.sin((ell+1)*t)*mp.sin(t),(0,theta))/((ell+1)*vol)
   assert abs(lam-lam_int)<mp.mpf('1e-34')
   expected_zero=(den==2 and num==1 and ell%2==0)
   assert (abs(lam)<mp.mpf('1e-32'))==expected_zero
   count+=2
print('PASS',count,'symbolic and high-precision supplemental tests; universal proof independent of cutoff')
