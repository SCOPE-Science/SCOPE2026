"""Exact standalone checks for the Catalan-matroid vertex inertia identity.
No third-party packages required. Finite checks are not a proof of asymptotics.
"""
from fractions import Fraction
from itertools import product
from math import comb, pi, log, lgamma, exp

def dyck_bits(n):
    def visit(prefix, height, ups):
        if len(prefix) == 2*n:
            if height == 0:
                yield tuple(prefix)
            return
        if ups < n:
            yield from visit(prefix+[1],height+1,ups+1)
        if height:
            yield from visit(prefix+[0],height-1,ups)
    return list(visit([],0,0))

def formula(n):
    central = comb(2*n,n)
    mu = [Fraction(1)]
    for j in range(1,n):
        d = Fraction(n-2*j,n)*Fraction(comb(2*j,j)*comb(2*(n-j),n-j), central)
        mu.extend([d,d])
    mu.append(Fraction(-1))
    assert len(mu)==2*n
    inertia = sum((1-z*z)/4 for z in mu)
    distance=2*inertia
    return mu,inertia,distance

def inspect_exact(n):
    words=dyck_bits(n)
    C=comb(2*n,n)//(n+1)
    assert len(words)==C
    means=[Fraction(sum(2*w[k]-1 for w in words),C) for k in range(2*n)]
    inertia=sum(Fraction(1,4)*(1-z*z) for z in means)
    mu,form_inertia,form_distance=formula(n)
    assert mu==means,(n,mu,means)
    assert inertia==form_inertia,(n,inertia,form_inertia)
    assert form_distance==sum(sum(x!=y for x,y in zip(a,b)) for a in words for b in words)/Fraction(C*C),(n,form_distance)
    return C,form_distance

def asymptotic(n):
    mu,inertia,distance=formula(n)
    target=n/2-log(n)/pi+0.5-(0.5772156649015328606+log(16)-2)/pi
    return float(inertia),target,float(inertia)-target

if __name__=='__main__':
    for n in range(1,8):
        c,d=inspect_exact(n)
        print('n',n,'vertices',c,'mean_squared_distance',str(d))
    for n in (10,100,1000):
        i,t,e=asymptotic(n)
        print('asymptotic',n,'observed_inertia',f'{i:.10f}','approx',f'{t:.10f}','difference',f'{e:.10f}')
    print('CATALAN_VERTEX_INERTIA_EXACT_PASS n=1..7')
