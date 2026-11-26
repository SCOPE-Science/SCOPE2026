import sympy as s
from functools import lru_cache
x,y=s.symbols('x y')
@lru_cache(None)
def is_smooth(f):
 for u in range(2):
  for v in range(2):
   p=0
   for i in range(4):
    for j in range(4):
     if f>>(i*4+j)&1:p+=x**(i if u==0 else 3-i)*y**(j if v==0 else 3-j)
   q=s.Poly(p,x,y,modulus=2).as_expr()
   if s.groebner([q,s.diff(q,x),s.diff(q,y)],x,y,modulus=2).polys!=[s.Poly(1,x,y,modulus=2)]:
    return False
 return True
if __name__=='__main__':
 from tri_probe import form_test
 from collections import Counter
 import time
 t=time.monotonic(); d=Counter();tests=0
 for f in range(1,65536):
  n,m=form_test(f)
  if n>=5:
   tests+=1
   if is_smooth(f):d[n]+=1;print('SMOOTH HIGH',f,n,m)
 print('time',time.monotonic()-t,'tested',tests,'smooth',d)
