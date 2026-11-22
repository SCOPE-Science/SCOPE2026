#!/usr/bin/env python3
"""Exact finite-wheel occupation enumerator and asymptotic bracket checks."""
import math


def padd(a,b):
    return [((a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0)) for i in range(max(len(a),len(b)))]

def pmul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return c

def path_polys(upto):
    p=[[1],[1,1]]
    for i in range(2,upto+1):p.append(padd(p[-1], [0]+p[-2]))
    return p

def direct_wheel_counts(n):
    assert n>=7
    Z=[0]*(n+2); A=[0]*(n+2); B=[0]*(n+2)
    edges=[(i,(i+1)%n) for i in range(n)]+[(n,i) for i in range(n)]
    for bit in range(1<<(n+1)):
        if any((bit>>u)&(bit>>v)&1 for u,v in edges):continue
        k=bit.bit_count();Z[k]+=1
        if bit&1:A[k]+=1
        if (bit&1) and (bit&(1<<3)):B[k]+=1
    return Z,A,B

def polynomial_check():
    total=0
    for n in (7,9,11,13):
        p=path_polys(n)
        c=padd(p[n-1],[0]+p[n-3]);z=padd(c,[0,1]);a=[0]+p[n-3];b=[0,0]+p[n-6]
        dz,da,db=direct_wheel_counts(n)
        for actual,expected in [(dz,z),(da,a),(db,b)]:
            assert actual[:len(expected)]==expected
            assert not any(actual[len(expected):]);total+=1
        f=padd(pmul(p[n-6],z),[-x for x in pmul(p[n-3],p[n-3])])
        assert f[0]==0 and f[1]==1
        m=(n-1)//2
        assert f[2*m-2]==n-m*m
        assert all(x==0 for x in f[2*m-1:]);total+=3
        assert sum(f)<0;total+=1
    print('EXACT_BRUTE_POLYNOMIAL_ASSERTIONS',total)


def lambertw_pos(x):
    """Principal Lambert W at x>0, by a logarithmic Newton iteration."""
    assert x>0
    w=max(0.1,math.log1p(x)-math.log1p(math.log1p(x)))
    for _ in range(25):
        step=(w+math.log(w)-math.log(x))/(1+1/w)
        w-=step
        if abs(step)<1e-14:break
    assert abs(w*math.exp(w)/x-1)<1e-11
    return w

def wheel_covariance(n,z):
    d=math.sqrt(1+4*z)
    lp=(1+d)/2
    q=(1-d)/(1+d)
    C=lp**n*(1+q**n)
    rho=z/(lp*d)*(1-q**(n-1))/(1+q**n)
    R=1-(1-q*q)*(1-q**(n-4))*(1+q**n)/(1-q**(n-1))**2
    t=C/(C+z);ph=z/(C+z)
    return t*rho*rho*(ph-R)

def asymptotic_test():
    total=0
    for n in (101,301,1001,3001):
        w=lambertw_pos(n)
        for shift in (-2.0,-1.0,-0.5,0.5,1.0,2.0):
            z=(w+shift)/n
            assert (wheel_covariance(n,z)>0)==(shift<0);total+=1
        lo=(w-.5)/n;hi=(w+.5)/n
        for _ in range(90):
            mid=(lo+hi)/2
            if wheel_covariance(n,mid)>0:lo=mid
            else:hi=mid
        offset=n*(lo+hi)/2-w
        print('ROOT_APPROX',n,format((lo+hi)/2,'.16g'),'n_root_minus_W',format(offset,'.9g'))
        total+=1
    n=10001
    for shift in (-1.0,1.0):
        z=lambertw_pos(n*math.exp(shift))/n
        normalized=wheel_covariance(n,z)/z**4
        target=math.exp(-shift)-1
        assert abs(normalized-target)<.02
        total+=1
        print('PROFILE_CHECK',shift,format(normalized,'.12g'),format(target,'.12g'))
    print('ASYMPTOTIC_BRACKET_ASSERTIONS',total)

if __name__=='__main__':
    polynomial_check()
    asymptotic_test()
    print('ALL_NEW_WHEEL_CHECKS_PASSED')
