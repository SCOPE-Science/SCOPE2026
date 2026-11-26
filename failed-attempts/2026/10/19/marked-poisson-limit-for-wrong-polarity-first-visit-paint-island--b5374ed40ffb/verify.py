"""Independent finite-difference check of orientation-resolved first-hit boundary values.

Uses the original two-state diffusion backward generator on a spatial grid,
rather than assuming the proposed spatial paint chain. Also checks the
renewal constants and deterministic coupling scales.
"""
import numpy as np
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import spsolve
from scipy.linalg import expm

def exact(y,D,v,f):
    s=np.sqrt(v*v+2*D*f)
    q=s/D
    p=(s+v)/(2*s)
    return np.array([p+(1-p)*np.exp(-q*y),p*(1-np.exp(-q*y))])

def lattice_bvp(D,v,f,L=8.,n=3000):
    h=L/n
    # Coordinate y = distance to the target; original drift is -v*sigma.
    # Equations: D u+'' - v u+' + f(u- -u+) = 0,
    # D u-'' + v u-' + f(u+ -u-) = 0.
    s=np.sqrt(v*v+2*D*f); p=(s+v)/(2*s)
    A=lil_matrix((2*(n-1),2*(n-1))); b=np.zeros(2*(n-1))
    for j in range(1,n):
      for sig in range(2):
        row=2*(j-1)+sig
        vel= -v if sig==0 else v
        A[row,row]=-2*D/h**2-f
        A[row,2*(j-1)+1-sig]=f
        cL=D/h**2-vel/(2*h); cR=D/h**2+vel/(2*h)
        if j>1:A[row,2*(j-2)+sig]=cL
        else:b[row]-=cL*(1 if sig==0 else 0)
        if j<n-1:A[row,2*j+sig]=cR
        else:b[row]-=cR*p
    z=spsolve(A.tocsr(),b)
    def at(y):
      j=int(round(y/h));return np.array([z[2*(j-1)],z[2*(j-1)+1]])
    return h,at

def main():
    maxerr=0
    for D,v,f in [(0.17,1.1,0.8),(0.43,1.7,0.5),(0.8,0.9,1.2)]:
      h,numeric=lattice_bvp(D,v,f)
      for mult in (80,200,400):
        y=mult*h
        err=np.max(abs(numeric(y)-exact(y,D,v,f)))
        maxerr=max(maxerr,err)
        assert err<1.2e-4,(D,v,f,y,err)
      s=np.sqrt(v*v+2*D*f);q=s/D
      a=(s-v)/(2*D);b=(s+v)/(2*D)
      G=np.array([[-a,a],[b,-b]])
      for length in (0.1,0.8,2.0):
        K=expm(G*length)
        e=np.exp(-q*length);p=b/q
        target=np.array([[p+(1-p)*e,(1-p)*(1-e)],
                         [p*(1-e),(1-p)+p*e]])
        assert np.allclose(K,target,atol=3e-14)
      assert abs((a+b)-q)<1e-12
      print('D,v,f =',D,v,f,'lattice spacing=',h,'max BVP error controlled')
    # Coupling constants: positive spacings have rate a_D -> f/(2v),
    # rescaled negative run lengths (v/D) E/b_D -> unit-mean exp.
    for D in (1e-2,1e-3,1e-4,1e-5):
       v=1.3;f=0.7;s=np.sqrt(v*v+2*D*f)
       a=(s-v)/(2*D);b=(s+v)/(2*D)
       assert abs(a-f/(2*v)) < 0.002
       assert a>0 and b>0
       print('D=',D,'a_D=',a,'limit=',f/(2*v),'scaled neg mean=',v/(D*b))
    print('PASS: finite-difference hit orientations, matrix semigroup and singular constants. Max BVP error:',maxerr)
if __name__=='__main__':main()
