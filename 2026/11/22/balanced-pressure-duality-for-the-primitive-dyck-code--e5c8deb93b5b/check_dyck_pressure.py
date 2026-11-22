#!/usr/bin/env python3
"""Finite diagnostics for the primitive-excursion pressure classification.
No finite diagnostic replaces the entropy-density or variational proof.
"""
from itertools import product
from math import comb, exp, log, sqrt


def height(word):
    z=0; seq=[0]
    for c in word:
        z+= 1 if c=='+' else -1
        seq.append(z)
    return seq


def primitive(word):
    h=height(word)
    return len(word)>0 and h[-1]==0 and min(h[1:-1],default=1)>0


def narayana(m,p):
    if m==0: return int(p==1)
    return (comb(m,p)*comb(m,p-1)//m) if 1<=p<=m else 0


def energies(g, a,b,c,d):
    ww=g+g[0]
    sums={"++":a,"+-":b,"-+":c,"--":d}
    return sum(sums[ww[i:i+2]] for i in range(len(g)))


def close(x,y,eps=1e-10):
    assert abs(x-y)<eps,(x,y)


def root_N(N,a,b,c,d):
    # root of sum_g exp(E(g)-P length(g))=1 grouped by Narayana numbers
    E=[]
    for n in range(1,N+1):
        for p in range(1,max(1,n-1)+1):
            count=narayana(n-1,p)
            if count:
                E.append((2*n, p, count,(n-p)*(a+d)+p*(b+c)))
    def F(h):
        return sum(count*exp(Energy-ell*h) for ell,p,count,Energy in E)
    lo=-max(map(abs,[a,b,c,d]))-2; hi=max(map(abs,[a,b,c,d]))+2
    assert F(lo)>1 and F(hi)<1
    for _ in range(100):
        m=(lo+hi)/2
        if F(m)>1: lo=m
        else: hi=m
    return (hi+lo)/2


def surgery(w):
    z=sum(1 if c=='+' else -1 for c in w)
    u=w+('-'*z if z>0 else '+'*(-z))
    assert height(u)[-1]==0
    hs=height(u)[:-1]
    k=hs.index(min(hs))
    v=u[k:]+u[:k]
    g='+'+v+'-'
    assert primitive(g)
    return g


if __name__=='__main__':
    cases=0
    for n in range(1,8):
        generators=[ ''.join(w) for w in product('+-', repeat=2*n) if primitive(w)]
        assert len(generators)==comb(2*n-2,n-1)//n
        for p in range(1,n+1):
            cnt=sum(sum(g[i:i+2]=='+-' for i in range(len(g)-1))==p for g in generators)
            assert cnt==narayana(n-1,p),(n,p,cnt,narayana(n-1,p))
            cases+=1
        for a,b,c,d in [(0.2,-0.3,0.7,0.8),(0.5,0.2,0.1,0.5),(-0.4,0.4,0.8,1.3)]:
            for g in generators:
                p=sum(g[i:i+2]=='+-' for i in range(len(g)-1))
                close(energies(g,a,b,c,d),(n-p)*(a+d)+p*(b+c))
                cases+=1
    for a,b,c,d in [(.2,-.3,.7,.8),(.5,.2,.1,.5),(-.4,.4,.8,1.3)]:
        A,B,C,D=exp(a),exp(b),exp(c),exp(d)
        ps=log(sqrt(A*D)+sqrt(B*C))
        pf=log((A+D+sqrt((A-D)**2+4*B*C))/2)
        assert pf>=ps-1e-12
        assert (abs(pf-ps)<1e-12)==(abs(a-d)<1e-12)
        q=sqrt(B*C)/(sqrt(A*D)+sqrt(B*C))
        def h(q):return -q*log(q)-(1-q)*log(1-q)
        close(ps,h(q)+.5*(1-q)*(a+d)+.5*q*(b+c))
        last=-1e100
        for N in [1,2,4,8,16,32,48]:
            pr=root_N(N,a,b,c,d)
            assert pr>=last-1e-11 and pr<ps+1e-10,(N,pr,ps)
            last=pr;cases+=1
        print('field',a,b,c,d,'Pseq',ps,'Pfull',pf,'N48',last,'gap',pf-ps)
    for n in [8,10,12,14,16]:
        allbal=[''.join(w) for w in product('+-',repeat=n) if w.count('+')==n//2]
        image={surgery(w) for w in allbal}
        assert len(image)*n>=len(allbal)
        for g in image:
            assert primitive(g) and len(g)==n+2
        cases+=len(allbal)
        print('balanced surgery',n,len(allbal),len(image))
    print('PASS exact enumeration / pressure / surgery checks:',cases)
