"""Supplementary finite checks for exact Schatten-four trace of radial monomial differences.
Purely finite diagnostics, not a proof of infinite-dimensional claims.
Run with Python 3, numpy and scipy.
"""
import math
import numpy as np
from scipy.special import gammaln

def ratio(alpha,n,k):
    beta=alpha+1
    if n==0:return 1.
    logmu=lambda j:gammaln(alpha+2)+gammaln(j+1)-gammaln(j+alpha+2)
    return math.exp(logmu(k*n)-logmu(n))

def analytic(alpha,p,q,a,b,r,N):
    g=math.gcd(p,q); pp=p//g;qq=q//g
    d=sum((r**(2*a*n)*ratio(alpha,n,p)+r**(2*b*n)*ratio(alpha,n,q))**2 for n in range(1,N+1))
    off=2*sum(r**(2*(a*qq+b*pp)*k)*ratio(alpha,qq*k,p)*ratio(alpha,pp*k,q) for k in range(1,N//max(pp,qq)+1))
    return d+off

def direct(alpha,p,q,a,b,r,N,theta=0.0,phi=0.0,return_singular=False):
    B=np.zeros((max(p,q)*N+1,N+1),dtype=complex)
    for n in range(1,N+1):
       B[p*n,n]+=r**(a*n)*complex(math.cos(n*theta), math.sin(n*theta))*math.sqrt(ratio(alpha,n,p))
       B[q*n,n]-=r**(b*n)*complex(math.cos(n*phi),math.sin(n*phi))*math.sqrt(ratio(alpha,n,q))
    G=B.conj().T@B
    if return_singular: return np.sqrt(np.maximum(0.0,np.linalg.eigvalsh(G)))
    return float(np.sum(np.abs(G)**2))

def lim(alpha,p,q,a,b):
   beta=alpha+1; A=p**(-beta); B=q**(-beta)
   g=math.gcd(p,q);pp=p//g;qq=q//g
   return A*A/(4*a)+B*B/(4*b)+A*B/(a+b)+A*B/(a*qq+b*pp)

def main():
   count=0
   for alpha in [-0.5,0.,0.6,2.]:
    for p,q in [(1,2),(2,1),(2,3),(3,2),(2,4),(4,2),(3,6),(6,3)]:
     for a,b in [(1.,1.),(.7,1.3)]:
      for r in [.3,.68,.93]:
       for N in [8,18]:
        f=analytic(alpha,p,q,a,b,r,N)
        h=direct(alpha,p,q,a,b,r,N)
        assert abs(f-h)<2e-10*max(1.,f,h),(alpha,p,q,a,b,r,N,f,h)
        count+=1
   for alpha,p,q,a,b in [(0,2,3,1,1),(1,2,4,.7,1.3),(-.5,1,3,.8,1.2)]:
    base=direct(alpha,p,q,a,b,.83,12,return_singular=True)
    for theta,phi in [(.1,.8),(.62,-.41),(2.8,-2.1)]:
     other=direct(alpha,p,q,a,b,.83,12,theta,phi,return_singular=True)
     assert np.max(np.abs(base-other))<1e-10,(alpha,p,q,theta,phi)
     count+=1
   # For r near 1, untruncated exact series should approach Abelian coefficient.
   for alpha,p,q,a,b in [(0,2,3,1,1),(0,2,4,1,1),(-.5,1,3,.7,1.3),(2,3,5,1,1)]:
    L=lim(alpha,p,q,a,b)
    for r,N,tol in ([(.9999,180000,.06)] if alpha>=2 else [(.985,5000,.17),(.997,17000,.06),(.999,40000,.03)]):
     v=(1-r)*analytic(alpha,p,q,a,b,r,N)
     assert abs(v-L)<tol*L,(alpha,p,q,a,b,r,v,L)
     count+=1
   print('RADIAL_MONOMIAL_S4_MOMENT_DIAGNOSTIC_OK',count)
   print('example p=2 q=3 a=b=1 alpha=0:',lim(0,2,3,1,1),'expected 149/720',149/720)

if __name__=='__main__':main()
