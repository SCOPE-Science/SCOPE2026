"""Independent exact Fourier-word and torus-grid checks of a cat-map phase-sum identity.

Requires Python 3 standard library; numpy is optional for the independent grid stage.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import comb, pi, sin

def vseq(n):
    a,b=(1,0),(2,1)
    out=[]
    for _ in range(n):
        out.append(a)
        a,b=b,(3*b[0]-a[0],3*b[1]-a[1])
    return out

def signed_zero_counts(n,k):
    vs=vseq(n)
    states={(0,0,0):1}
    for _ in range(k):
        nxt=defaultdict(int)
        for (x,y,z),q in states.items():
            for u,w in vs:
                nxt[(x+u,y+w,z+1)]+=q
                nxt[(x-u,y-w,z-1)]-=q
        states=nxt
    return {z:q for (x,y,z),q in states.items() if x==y==0 and q}

def expected_fourier(n,k):
    # Sine expansion: E[S_n^k] = (2i)^-k sum_z counts[z] exp(i z alpha).
    if k==1 or k==3: return {}
    if k==5: return ({-1:-20*(n-2),1:20*(n-2)} if n>=3 else {})
    # For even moments the only zero-frequency Fourier character is alpha-free.
    if k==2:return {0:-2*n}
    if k==4:return {0: 6*n*(2*n-1)}  # positive sine fourth expansion uses (2i)^-4=1/16
    raise ValueError

def run():
    count=0
    for n in range(1,9):
        for k in range(1,6):
            found=signed_zero_counts(n,k)
            expected=expected_fourier(n,k)
            if found!=expected:
                raise AssertionError((n,k,found,expected))
            count+=1
    print('Exact signed Fourier-word checks: %d (n=1..8, k=1..5)'%count)
    try:
        import numpy as np
    except ImportError:
        print('numpy absent: optional independent torus-grid stage omitted')
        return
    q=401
    grid=np.arange(q,dtype=float)/q
    x,y=np.meshgrid(grid,grid,indexing='ij')
    frequencies=vseq(5)
    for n in (1,2,3,4,5):
        for alpha in (0.0,pi/6,pi/2):
            z=np.zeros_like(x)
            for a,b in frequencies[:n]:z+=np.sin(2*pi*(a*x+b*y)+alpha)
            targets={1:0,2:n/2,3:0,4:3*n*(2*n-1)/8,
                     5:5*max(n-2,0)*sin(alpha)/4}
            for k,t in targets.items():
                m=float(np.mean(z**k))
                if abs(m-t)>2e-9:
                    raise AssertionError(('grid',n,alpha,k,m,t))
                count+=1
    print('Independent Haar quadrature checks: %d (exact bandlimited 401x401 torus grid)'%(count-40))
    print('Total checked identities:',count)
if __name__=='__main__':run()
