"""Reproduce finite checks for the regular-bipyramid microscopic-mass theorem.
Dependencies: Python 3, NumPy.
"""
import math
import numpy as np


def formulas(n,h):
    s=2*math.cos(math.pi/(2*n))/(n*math.sin(math.pi/(2*n)))
    T=math.hypot(1,h)
    den=2*T-h-s
    a=(T-h)/(n*den)
    b=(T-s)/(2*den)
    energy=(T*T-h*s)/den
    return a,b,energy,math.sqrt(s*s-1),den

def points(n,h):
    return np.array([(math.cos(2*math.pi*j/n),math.sin(2*math.pi*j/n),0.) for j in range(n)]+[(0.,0.,h),(0.,0.,-h)])

def run():
    checks=0
    for n in range(3,26):
        s=2*math.cos(math.pi/(2*n))/(n*math.sin(math.pi/(2*n)))
        hn=math.sqrt(s*s-1)
        for h in [0.04,0.3,0.7,hn*0.7,hn,hn*1.2,1.0,2.5,8.0]:
            a,b,e,threshold,den=formulas(n,h)
            D=np.linalg.norm(points(n,h)[:,None,:]-points(n,h)[None,:,:],axis=2)
            from_matrix=np.linalg.solve(D,np.ones(n+2))
            w=from_matrix/from_matrix.sum()
            expected=np.array([a]*n+[b,b])
            assert np.max(np.abs(w-expected))<2e-9, (n,h, np.max(np.abs(w-expected)))
            checks+=1
            assert abs(expected.sum()-1)<2e-12;checks+=1
            assert np.max(np.abs(D@expected-e))<1e-11;checks+=1
            assert e>0 and den>0;checks+=1
            assert (b>0)==(h>threshold) if abs(h-threshold)>1e-10 else abs(b)<1e-12;checks+=1
            M=np.eye(n+2)-np.ones((n+2,n+2))/(n+2)
            l=np.linalg.eigvalsh(M@D@M)[:-1]
            assert l[-1]<-1e-11;checks+=1
            rng=np.random.default_rng(n)
            for _ in range(4):
                z=rng.normal(size=n+2)
                z-=z.mean()
                assert z@D@z<0;checks+=1
        # monotonic cutoff
        if n>3:
            assert hn>formulas(n-1,0.5)[3];checks+=1
    H=math.sqrt(16/math.pi**2-1)
    for n in [50,100,200,500,1000,10000]:
        hn=formulas(n,0.5)[3]
        assert abs(n*n*(H-hn)-4/(3*H))<3, (n,hn);checks+=1
    for h in [0.1,0.4,0.8,1.,3.,9.]:
        s=4/math.pi
        T=math.hypot(1,h)
        d=2*T-h-s
        A=(T-h)/d
        b=(T-s)/(2*d)
        E=(T*T-h*s)/d
        assert abs(A+2*b-1)<1e-13;checks+=1
        assert abs(s*A+2*T*b-E)<1e-13;checks+=1
        assert abs(T*A+2*h*b-E)<1e-13;checks+=1
        # True circular numerical quadrature: signed energy potential at equator.
        N=80000
        theta=(2*np.pi/N)*np.arange(N)
        csum=(2*np.abs(np.sin(theta/2))).mean()
        assert abs(A*csum+2*b*T-E)<1e-8;checks+=1
        for n in [30,100,600]:
            aa,bb,ee,_,_=formulas(n,h)
            assert abs(n*aa-A)<6/n**2
            assert abs(bb-b)<6/n**2
            checks+=2
    print('PASS',checks,'assertions')
    print('limit threshold:',H)
    for n in (3,4,6,12,100):
        print(n, 'threshold',formulas(n,0.5)[3])
if __name__=='__main__':run()
