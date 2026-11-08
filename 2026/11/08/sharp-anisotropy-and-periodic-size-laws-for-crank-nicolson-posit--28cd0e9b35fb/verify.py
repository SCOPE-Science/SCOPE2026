#!/usr/bin/env python3
"""Reproduce exact and supplementary checks for honeycomb Crank--Nicolson positivity.
Requires Python 3 standard library only. Finite tests do not prove infinite statements.
"""
import cmath
import math
from fractions import Fraction as Q
from math import comb


def moment(k):
    return sum(comb(k, j)**2 * comb(2*(k-j), k-j) for j in range(k+1))


def series_interval(s, terms=45):
    # Exact rational lower and upper bounds for the infinite isotropic return.
    z = (s/(1+3*s))**2
    summ = Q(0)
    power = Q(1)
    for k in range(terms+1):
        if k:
            power *= z
        summ += moment(k)*power
    low = summ/(1+3*s)
    tail = (9*z)**(terms+1)/(1-9*z)/(1+3*s)
    return low, low+tail


def return_integral(s, w=(1.,1.,1.), slices=4096):
    # Analytic integration in the second Bloch angle; trapezoidal in first.
    a,b,c=map(float,w)
    degree=a+b+c
    v=1+s*degree
    total=0.
    for j in range(slices):
        theta=2*math.pi*j/slices
        u=a*a+b*b+2*a*b*math.cos(theta)
        t=v*v-s*s*(u+c*c)
        den=(t*t-4*(s**4)*(c*c)*u)**0.5
        total+=1./den
    return v*total/slices


def return_torus(s,n,w=(1.,1.,1.)):
    a,b,c=map(float,w)
    degree=a+b+c
    v=1+s*degree
    total=0.
    for i in range(n):
        for j in range(n):
            z=a+b*cmath.exp(2j*math.pi*i/n)+c*cmath.exp(2j*math.pi*j/n)
            total+=v/(v*v-s*s*(z.real*z.real+z.imag*z.imag))
    return total/(n*n)


def root(func):
    low,high=0.,1.
    while func(high)>.5:
        high*=2.
    for _ in range(65):
        mid=(low+high)/2.
        if func(mid)>.5: low=mid
        else:high=mid
    return (low+high)/2


def invert_matrix(A):
    # Exact Gauss--Jordan inversion with rational arithmetic.
    n=len(A)
    M=[row[:]+[Q(int(i==j)) for j in range(n)] for i,row in enumerate(A)]
    for k in range(n):
        pivot=next(i for i in range(k,n) if M[i][k]!=0)
        M[k],M[pivot]=M[pivot],M[k]
        z=M[k][k];M[k]=[v/z for v in M[k]]
        for i in range(n):
            if i==k:continue
            z=M[i][k]
            if z:
                M[i]=[x-z*y for x,y in zip(M[i],M[k])]
    return [row[n:] for row in M]


def rational_torus(n,w,s):
    # Each A(i,j) links to B(i,j), B(i-1,j), B(i,j-1).
    dim=2*n*n
    L=[[Q(0) for _ in range(dim)] for _ in range(dim)]
    def idx(x,y,typ):return (x%n)*n+y%n+typ*n*n
    for x in range(n):
        for y in range(n):
            u=idx(x,y,0)
            for (xx,yy),weight in zip([(x,y),(x-1,y),(x,y-1)],w):
                v=idx(xx,yy,1)
                L[u][u]+=weight;L[v][v]+=weight
                L[u][v]-=weight;L[v][u]-=weight
    A=[[Q(int(i==j))+s*L[i][j] for j in range(dim)] for i in range(dim)]
    return invert_matrix(A)


def main():
    checks=0
    left=Q(41705524440007830,10**17)
    right=Q(41705524440007831,10**17)
    gl,_=series_interval(left,45)
    _,gr=series_interval(right,45)
    assert gl>Q(1,2) and gr<Q(1,2)
    checks+=2
    # Exact formula moments begin with one, three, fifteen, ninety-three.
    assert [moment(k) for k in range(4)]==[1,3,15,93]
    checks+=4
    iso=root(lambda s:return_integral(s))
    assert float(left)<iso<float(right) or abs(iso-.4170552444000783)<2e-14
    checks+=1
    for weights in [(Q(1),Q(1),Q(1)),(Q(1),Q(2),Q(3)),(Q(2),Q(1),Q(4))]:
        for n in (2,3):
            for s in (Q(1,5),Q(2,5),Q(7,5)):
                R=rational_torus(n,weights,s)
                val=return_torus(float(s),n,tuple(map(float,weights)))
                for k in range(2*n*n):
                    assert R[k][k]==R[0][0]
                    assert R[k][k]>0
                    checks+=2
                assert abs(float(R[0][0])-val)<2e-12
                checks+=1
                assert all(R[i][j]>0 for i in range(2*n*n) for j in range(2*n*n))
                checks+=1
    lasts=[]
    for n in range(2,9):
        r=root(lambda s:return_torus(s,n))
        assert r>iso
        lasts.append((n,r))
        checks+=1
    for n,r in lasts:
        assert abs(return_torus(r,n)-.5)<1e-12
        checks+=1
    # Strict Schur ordering on fixed-weight sums, supplementary numerical samples.
    anisotropies=[(1,1,1),(2,.5,.5),(2.5,.25,.25),(2.9,.05,.05)]
    horizons=[root(lambda s,w=w:return_integral(s,w,8192)) for w in anisotropies]
    assert all(x<y for x,y in zip(horizons,horizons[1:]))
    checks+=3
    # Singular law with fixed total conductance, independent weak-weight split.
    for ratio in (.15,.5,.85):
        for e in (.01,.001,.0001):
            w=(3-e,ratio*e,(1-ratio)*e)
            s=root(lambda t:return_integral(t,w,8192))
            normalized=s*math.sqrt(6*e)
            assert .95<normalized<1.04
            checks+=1
    print('PASS',checks,'supplementary checks')
    print('exact rational interval:',str(left),'< threshold <',str(right))
    print('isotropic threshold',format(iso,'.16f'))
    print('finite torus roots:',lasts)
    print('anisotropy roots:',list(zip(anisotropies,horizons)))

if __name__=='__main__':main()
