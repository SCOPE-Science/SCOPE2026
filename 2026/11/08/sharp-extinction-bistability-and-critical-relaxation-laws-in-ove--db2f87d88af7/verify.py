"""Finite checks for a homogeneous exponential-hazard hypergraph map.

Run with Python 3.10+: python verify.py
These finite tests do not establish the infinite-parameter theorem.
"""
from itertools import combinations
from fractions import Fraction as Q
from math import comb, log, exp, isclose
from random import Random


def motif_counts(n, edges):
    E = [set(edge) for edge in edges]
    ds, ts, qs = [], [], []
    for i in range(n):
        inc = [e for e in E if i in e]
        deg = sum(any({i,j} <= e for e in E) for j in range(n) if j != i)
        overlaps = sum(len((a & b) - {i}) for a,b in combinations(inc, 2))
        codegree_overlaps = sum(comb(sum({i,j} <= e for e in E), 2) for j in range(n) if j != i)
        assert overlaps == codegree_overlaps
        ds.append(deg); ts.append(len(inc)); qs.append(overlaps)
    return ds,ts,qs


def e_series(mu, B, C, size=5):
    # Formal power series of exp(-(mu*x+B*x**2+C*x**3)) with rational coefficients.
    g = [Q(0), -mu, -B, -C] + [Q(0)]*(size-3)
    e = [Q(1)]
    for n in range(1, size+1):
        e.append(sum(Q(k)*g[k]*e[n-k] for k in range(1,n+1))/n)
    # F(x)-x = -mu*x + (1-x)*(1-exp(-h(x)))
    u = [Q(0)] + [-e[k] for k in range(1,size+1)]
    coeff = [Q(0)] + [u[k] - u[k-1] - (mu if k==1 else 0) for k in range(1,size+1)]
    return coeff


def hfunc(x, m, B, C):
    return m*x+B*x*x+C*x*x*x


def F(x,m,B,C):
    return (1-m)*x+(1-x)*(-__import__('math').expm1(-hfunc(x,m,B,C)))


def T(x,m,B):
    return (log((1-x)/(1-(1+m)*x))-m*x-B*x*x)/(x*x*x)


def tderiv(x,m,B):
    L=log((1-x)/(1-(1+m)*x))
    Lp=(1+m)/(1-(1+m)*x)-1/(1-x)
    return (x*Lp-3*L+2*m*x+B*x*x)/(x**4)


def bisect(fun, a, b, reps=95):
    fa=fun(a)
    assert fa*fun(b)<=0,(a,b,fa,fun(b))
    for _ in range(reps):
        mid=(a+b)/2
        if fa*fun(mid) <= 0:b=mid
        else:a=mid;fa=fun(mid)
    return (a+b)/2


def run():
    tests=0
    for n in range(4,9):
        ds,ts,qs=motif_counts(n,combinations(range(n),3))
        assert ds == [n-1]*n
        assert ts == [comb(n-1,2)]*n
        assert qs == [(n-1)*comb(n-2,2)]*n
        tests+=n
    for n in range(6,11):
        edges={tuple(sorted({i,(i+1)%n,(i+2)%n})) for i in range(n)}
        ds,ts,qs=motif_counts(n,edges)
        assert (ds,ts,qs)==([4]*n,[3]*n,[2]*n), (n,ds,ts,qs)
        tests+=n
    fano=[(0,1,2),(0,3,4),(0,5,6),(1,3,5),(1,4,6),(2,3,6),(2,4,5)]
    ds,ts,qs=motif_counts(7,fano)
    assert ds==[6]*7 and ts==[3]*7 and qs==[0]*7
    tests+=7
    for m in [Q(1,10), Q(2,5), Q(3,4), Q(99,100)]:
        Bc=m+m*m/2;Cc=m+m*m+m**3/3;D=((1+m)**4-1)/4
        for B,C in [(Q(0),Q(0)),(Bc/2, Cc*2),(Bc,Cc/2),(Bc,Cc),(Bc*2,Cc*2)]:
            z=e_series(m,B,C)
            assert z[1]==0 and z[2]==B-Bc
            if B==Bc: assert z[3]==C-Cc
            if B==Bc and C==Cc: assert z[4]==-D
            tests+=1
    for m in [0.15,0.4,0.8]:
        Bc=m+m*m/2;Cc=m+m*m+m**3/3
        for B in [0, Bc/2, Bc*0.92]:
            xmax=1/(1+m)
            xstar=bisect(lambda x:tderiv(x,m,B), 1e-7, xmax-1e-8)
            cstar=T(xstar,m,B)
            assert cstar>Cc
            for C in [0, Cc, cstar*.95, cstar*1.05, cstar*1.7]:
                cuts=[xmax*i/3001 for i in range(1,3001)]
                roots=sum((T(a,m,B)-C)*(T(b,m,B)-C)<0 for a,b in zip(cuts,cuts[1:]))
                assert roots == (2 if C>cstar else 0),(m,B,C,cstar,roots)
                tests+=1
            assert abs(F(xstar,m,B,cstar)-xstar)<2e-12
            tests+=1
        for B,C,roots in [(Bc,Cc/2,0),(Bc,Cc,0),(Bc,Cc*1.2,1),(Bc*1.1,0,1)]:
            xmax=1/(1+m)
            cuts=[xmax*i/3001 for i in range(1,3001)]
            # The sign of F(x)-x near zero may be lost at machine precision; avoid x < 1e-4.
            cnt=sum((F(a,m,B,C)-a)*(F(b,m,B,C)-b)<0 for a,b in zip(cuts,cuts[1:]))
            assert cnt==roots,(m,B,C,roots,cnt)
            tests+=1
    # Direct demonstration of disjoint critical exponents with small initial prevalence.
    m=0.4; Bc=m+m*m/2; Cc=m+m*m+m**3/3
    D=((1+m)**4-1)/4
    for B,C,k,coef in [(Bc*.5,0,1,Bc*.5),(Bc,Cc*.5,2,Cc*.5),(Bc,Cc,3,D)]:
        x=.03
        for _ in range(400000):x=F(x,m,B,C)
        predicted=(1/(k*coef*400000))**(1/k)
        assert abs(x/predicted-1)<0.08,(k,x,predicted)
        tests+=1
    print('PASS',tests,'check groups (with numerical sign scan samples); exact rational series and motif counts passed')

if __name__=='__main__':run()
