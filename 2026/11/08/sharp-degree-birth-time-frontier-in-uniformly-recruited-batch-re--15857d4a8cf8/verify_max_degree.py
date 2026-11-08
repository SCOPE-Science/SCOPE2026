"""Finite exact checks for the batch-recruitment tree degree-age theorem.

This script tests exact finite marginal and two-vertex distributions,
the negative-quadrant relation used in the second-moment argument,
and independent numerical identities defining the asymptotic frontier.
Finite checks do not constitute proofs of asymptotic results.
"""
from fractions import Fraction
from math import log, isclose

checks = 0

def check(cond, msg):
    global checks
    if not cond:
        raise AssertionError(msg)
    checks += 1

def marginal(m, n, birth):
    p = [Fraction(1)]
    for t in range(max(birth + 1, 1), n + 1):
        q = Fraction(1, 1 + m*(t - 1))
        nxt = [Fraction(0)]*(len(p)+1)
        for r, pr in enumerate(p):
            nxt[r] += pr*(1-q)
            nxt[r+1] += pr*q
        p = nxt
    return p

def joint(m, n, b1, b2):
    d = {(0,0):Fraction(1)}
    for t in range(1,n+1):
        q = Fraction(1,1+m*(t-1))
        e1 = t>b1
        e2 = t>b2
        # Birth time 0 denotes the root; birth step j>=1 follows recruitment j.
        out={}
        for (a,b), v in d.items():
            opts=[(a,b,1-int(e1)*q-int(e2)*q)]
            if e1:opts.append((a+1,b,q))
            if e2:opts.append((a,b+1,q))
            for x,y,weight in opts:
                out[x,y]=out.get((x,y),Fraction(0))+v*weight
        d=out
    return d

for m in range(1,5):
    for n in range(2,11):
        for i in range(n):
            pi=marginal(m,n,i)
            check(sum(pi)==1, ('one marginal norm',m,n,i))
            for j in range(i+1,n):
                pj=marginal(m,n,j)
                d=joint(m,n,i,j)
                check(sum(d.values())==1,('joint norm',m,n,i,j))
                for a in range(len(pi)):
                    check(sum(v for (x,y),v in d.items() if x==a)==pi[a], ('first marginal',m,n,i,j,a))
                for b in range(len(pj)):
                    check(sum(v for (x,y),v in d.items() if y==b)==pj[b], ('second marginal',m,n,i,j,b))
                for k in range(1, min(len(pi),len(pj))+1):
                    p_pair=sum(v for (x,y),v in d.items() if x>=k and y>=k)
                    pprod=sum(pi[k:])*sum(pj[k:])
                    check(p_pair<=pprod, ('tail negative quadrant',m,n,i,j,k))

for m in range(1,21):
    q=log(m+1)
    xstar=1/q
    ustar=1-m/((m+1)*q)
    check(0<ustar<1,('critical exponent range',m))
    a=1-ustar
    check(isclose(a,m*xstar/(m+1),rel_tol=1e-12),('saddle',m))
    for u in [0.01,0.1,0.25,0.5,0.75,0.99]:
        if u>=ustar:continue
        lo=(1-u)/m
        high=xstar
        for _ in range(100):
            x=(lo+high)/2
            J=x*log(m*x/(1-u))-x+(1-u)/m
            if J>u:high=x
            else:lo=x
        x=(lo+high)/2
        J=x*log(m*x/(1-u))-x+(1-u)/m
        check(isclose(J,u,abs_tol=1e-10),('frontier level',m,u))
        check(1/m<x<xstar,('frontier range',m,u))
    for u in [0,ustar,1]:
        if u==1:continue
        phi=u-(xstar*log(m*xstar/(1-u))-xstar+(1-u)/m)
        check(phi<=1e-10,('sharp variational upper',m,u,phi))
        if u==ustar:
            check(abs(phi)<1e-10,('sharp variational maximum',m,u))

print('PASS:',checks,'exact rational and numerical assertions')
