"""Independent elementary diagnostics for a finite-core interval-map entropy law.
Run: python3 CHECK.py. Requires only the Python standard library.
"""
from math import sqrt, isfinite

def branches(k):
    m=k+2
    if k==0:
        vertices=[0]+[v for _ in range(m) for v in (1,2,1,0)]+[1]
    else:
        vertices=[k]+[v for _ in range(m) for v in (k-1,k,k+1,k+2,k+1,k)]+[k+1]
    return vertices

def W(kmax):
    return [[(2*(i+2)+1 if i==j else 2*(i+2) if abs(i-j)==1 else 0)
             for j in range(kmax+1)] for i in range(kmax+1)]

def sturm_less_than(x, kmax):
    # LDL pivots of J - xI; count negatives (i.e. eigenvalues below x).
    eps=1e-12
    pivot=5.0-x
    negative=int(pivot<0.0)
    for i in range(1,kmax+1):
        if abs(pivot)<eps:
            pivot=eps if pivot>=0 else -eps
        b2=4*(i+1)*(i+2)
        pivot=2*i+5-x-b2/pivot
        negative+=int(pivot<0.0)
    return negative

def largest_root(kmax):
    lo=0.0
    hi=6.0*(kmax+3)
    for _ in range(65):
        mid=(lo+hi)/2
        if sturm_less_than(mid,kmax)==kmax+1: hi=mid
        else: lo=mid
    return (lo+hi)/2

def determinant_rec(x,kmax):
    a,b=1.0,x-5
    for i in range(1,kmax+1):
        a,b=b,(x-(2*i+5))*b-4*(i+1)*(i+2)*a
    return b

def run():
    checks=0
    for kmax in range(1,25):
        mat=W(kmax)
        for k in range(kmax+1):
            v=branches(k)
            histogram=[0]*(kmax+1)
            for a,b in zip(v,v[1:]):
                target=min(a,b)
                if 0<=target<=kmax: histogram[target]+=1
            assert histogram==mat[k],(k,kmax,histogram,mat[k])
            checks+=1
        assert sturm_less_than(largest_root(kmax)+0.001,kmax)==kmax+1
        checks+=1
    for kmax,root in [(0,5.0),(1,11.0)]:
        assert abs(largest_root(kmax)-root)<1e-7
        checks+=1
    for kmax in [2,3,4,5,6,7,8,9,10]:
        r=largest_root(kmax)
        assert abs(determinant_rec(r,kmax)) < 1e-3*(abs(r)**(kmax+1))
        checks+=1
    print('VERIFY_OK', 'checks='+str(checks))
    for kmax in [20,50,100,200,500,1000,2000,4000]:
        r=largest_root(kmax)
        print('K',kmax,'rho',f'{r:.9f}', 'edge_scaled',f'{(6*kmax-r)/kmax**(1/3):.9f}')
    print('limit_edge',2.338107410459767*(72.0**(1.0/3.0)))

if __name__=='__main__': run()
