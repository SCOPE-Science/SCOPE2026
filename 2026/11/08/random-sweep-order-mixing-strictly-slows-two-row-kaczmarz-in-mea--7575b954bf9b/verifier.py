"""Exact rational checks for two-line projection sweeps; standard-library only.
The infinite-horizon result relies on the proof, not on finite enumeration.
"""
from fractions import Fraction as Q
from itertools import product
from math import sqrt

def dot(u,v): return sum(a*b for a,b in zip(u,v))
def matmul(a,b): return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)) for i in range(2))
def mv(a,v): return tuple(sum(a[i][j]*v[j] for j in range(2)) for i in range(2))
def outer(v): return tuple(tuple(v[i]*v[j] for j in range(2)) for i in range(2))
def matvec2(a,v): return (a[0][0]*v[0]+a[0][1]*v[1],a[1][0]*v[0]+a[1][1]*v[1])

def run():
    checks=0
    for c,s in [(Q(3,5),Q(4,5)),(Q(5,13),Q(12,13)),(Q(15,17),Q(8,17))]:
      u=(Q(1),Q(0));v=(c,s)
      P=outer(u); R=outer(v)
      F=matmul(R,P);B=matmul(P,R)
      assert F==tuple(tuple(c*v[i]*u[j] for j in range(2)) for i in range(2))
      assert B==tuple(tuple(c*u[i]*v[j] for j in range(2)) for i in range(2))
      checks+=2
      for p in [Q(1,4),Q(1,3),Q(1,2),Q(2,3),Q(3,4)]:
       K=((p*c**4,p*c**2),((1-p)*c**2,(1-p)*c**4))
       tr=c**4;dt=p*(1-p)*(c**8-c**4)
       assert K[0][0]+K[1][1]==tr
       assert K[0][0]*K[1][1]-K[0][1]*K[1][0]==dt
       assert dt<0
       checks+=3
       for x0 in [(Q(1),Q(2)),(Q(3),Q(-1)),(Q(0),Q(1))]:
        first=(p*dot(mv(F,x0),mv(F,x0)), (1-p)*dot(mv(B,x0),mv(B,x0)))
        w=first
        for n in range(1,9):
         # Independent sum over all 2^n possible epoch orders.
         brute=Q(0)
         for choice in product((0,1),repeat=n):
          xx=x0;prob=Q(1)
          for choice_i in choice:
           if choice_i==0: xx=mv(F,xx);prob*=p
           else: xx=mv(B,xx);prob*=(1-p)
          brute+=prob*dot(xx,xx)
         assert brute==sum(w),(c,s,p,x0,n,brute,sum(w))
         checks+=1
         if p==Q(1,2):
          rho=(c**2+c**4)/2
          assert brute==rho**(n-1)*sum(first)
          checks+=1
         w=matvec2(K,w)
       rho=(float(c)**4+sqrt(float(c)**8+4*float(p*(1-p))*float(c)**4*(1-float(c)**4)))/2
       assert rho>float(c)**4 and rho<1
       assert rho<=(float(c)**2+float(c)**4)/2+1e-14
       checks+=2
    print('CHECK_OK exact rational exhaustive order histories + rate identities')
    print('assertions:',checks)
    for c in [0.5,0.9]:
     det=c**4;fair=(c*c+c**4)/2
     print('overlap',c,'fixed squared-epoch rate',det,'fair shuffled rate',fair,'ratio',fair/det)
if __name__=='__main__':run()
