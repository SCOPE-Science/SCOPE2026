"""Standalone exact and numerical checks for cactus spanning-tree cut/reconnect dynamics.
Run: python verify_cactus_chain.py
Requires only Python 3.9+ standard library.
"""
from fractions import Fraction
from itertools import combinations, product
from math import comb, exp, log, erf, sqrt, floor

checks = 0

def require(x, message):
    global checks
    assert x, message
    checks += 1

def cactus(lengths, bridges=0):
    """Cycles joined at an articulation vertex; optional pendant bridges."""
    edges=[]; cycles=[]; root=0; new_vertex=1
    for length in lengths:
        vertices=[root]+list(range(new_vertex, new_vertex+length-1))
        new_vertex += length-1
        group=[]
        for a,b in zip(vertices, vertices[1:]+[root]):
            group.append(len(edges));edges.append((a,b))
        cycles.append(group)
    for _ in range(bridges):
        edges.append((root,new_vertex));new_vertex+=1
    return new_vertex,edges,cycles

def tree_states(V,edges):
    states=[]
    for es in combinations(range(len(edges)),V-1):
        par=list(range(V))
        def rt(v):
            while par[v]!=v:v=par[v]
            return v
        valid=True
        for e in es:
            u,v=edges[e]; a,b=rt(u),rt(v)
            if a==b:valid=False;break
            par[a]=b
        if valid:states.append(frozenset(es))
    return states

def kernel(V,edges,T):
    row={}
    for e in T:
        par=list(range(V))
        def rt(v):
            while par[v]!=v:v=par[v]
            return v
        for h in T-{e}:
            a,b=edges[h];par[rt(a)]=rt(b)
        choices=[f for f,(a,b) in enumerate(edges) if rt(a)!=rt(b)]
        for f in choices:
            U=(T-{e})|{f}
            row[U]=row.get(U,Fraction(0))+Fraction(1,(V-1)*len(choices))
    return row

def predicted_row(V,T,cycles):
    row={T:Fraction(1)-sum(Fraction(len(C)-1,2*(V-1)) for C in cycles)}
    for C in cycles:
        missing=next(e for e in C if e not in T)
        for e in C:
            if e!=missing:
                U=(T-{e})|{missing}
                row[U]=Fraction(1,2*(V-1))
    return row

def coords(T,cycles):
    return tuple(next(j for j,e in enumerate(C) if e not in T) for C in cycles)

def spectral_check(lengths,bridges):
    V,edges,cycles=cactus(lengths,bridges)
    states=tree_states(V,edges)
    require(len(states)==__import__('math').prod(lengths),'bad tree count')
    transition={T:kernel(V,edges,T) for T in states}
    for T in states:
        expected=predicted_row(V,T,cycles)
        require(transition[T]==expected,'kernel mismatch')
        require(sum(transition[T].values())==1,'row sum')
        for U,p in transition[T].items():
            require(p==transition[U].get(T,0),'reversibility')
    for mask in range(1<<len(lengths)):
        S=[i for i in range(len(lengths)) if (mask>>i)&1]
        eigen=Fraction(1)-Fraction(sum(lengths[i] for i in S),2*(V-1))
        choices=product(*(range(1,lengths[i]) for i in S))
        for symbols in choices:
            def f(T):
                x=coords(T,cycles)
                ans=1
                for i,a in zip(S,symbols):
                    ans*=int(x[i]==a)-int(x[i]==0)
                return ans
            for T in states:
                pf=sum(prob*f(U) for U,prob in transition[T].items())
                require(pf==eigen*f(T),'eigenfunction')
    for t in (0,1,2,3,5):
        P={states[0]:Fraction(1)}
        for _ in range(t):
            new={}
            for T,p in P.items():
                for U,q in transition[T].items():new[U]=new.get(U,Fraction(0))+p*q
            P=new
        chi=Fraction(len(states))*sum(p*p for p in P.values())-1
        spec=Fraction(0)
        for mask in range(1,1<<len(lengths)):
            S=[i for i in range(len(lengths)) if (mask>>i)&1]
            mult=__import__('math').prod(lengths[i]-1 for i in S)
            lam=Fraction(1)-Fraction(sum(lengths[i] for i in S),2*(V-1))
            spec+=mult*(lam**(2*t))
        require(chi==spec,'chi-square identity')
    print('exact PASS',lengths,'bridges',bridges,'trees',len(states))

for example in [([3],0),([3,3],0),([3,4],1),([4,4],0),([3,3,3],1)]:
    spectral_check(*example)

def tv_born_dimers(c,length,s):
    N_minus_one=c*(length-1)
    t=int(floor(N_minus_one/length*(log(c)+s)))
    up=Fraction(length-1,2*N_minus_one)
    down=Fraction(1,2*N_minus_one)
    # count coordinates disagreeing with the starting spanning tree
    p=[0.0]*(c+1);p[0]=1.0
    u=float(up);d=float(down)
    for _ in range(t):
        nxt=[0.0]*(c+1)
        for k,pk in enumerate(p):
            nxt[k]+=pk*(1-(c-k)*u-k*d)
            if k<c:nxt[k+1]+=pk*(c-k)*u
            if k>0:nxt[k-1]+=pk*k*d
        p=nxt
    stationary=[comb(c,k)*((length-1)/length)**k*(1/length)**(c-k) for k in range(c+1)]
    tv=sum(abs(a-b) for a,b in zip(p,stationary))/2
    sigma=sqrt((length-1)*exp(-s))
    profile=erf(sigma/(2*sqrt(2))) # 2 Phi(sigma/2)-1
    return t,tv,profile

for c in [40,80,160,320]:
    t,tv,pred=tv_born_dimers(c,3,0.0)
    print('profile',c,'t',t,'tv',round(tv,6),'limit',round(pred,6),'error',round(abs(tv-pred),6))
    require(abs(tv-pred)<0.05,'profile numerical discrepancy')

print('PASS',checks,'assertions')

# Mixed-alphabet family: one triangle and c equal long cycles.
def mixed_profile(alpha,s):
    eta=exp(-3/(2*alpha));sig=sqrt(exp(-s))
    def Phi(x):return (1+erf(x/sqrt(2)))/2
    def g(a):
        z=log(a)/sig
        return a*Phi(z+sig/2)-Phi(z-sig/2)-(a-1)/2
    return (g(1+2*eta)+2*g(1-eta))/3

def two_family_tv(ell, alpha, s):
    c=floor(exp(ell/alpha))
    Nminus=2+c*(ell-1)
    t=floor(Nminus/ell*(log(c)+log(ell-1)+s))
    # q=0 means slow triangle in original symbol, q=1 one of two other symbols.
    # k counts fast coordinates not in original symbol.
    p=[[0.0]*(c+1) for _ in range(2)];p[0][0]=1.0
    up=(ell-1)/(2*Nminus)
    down=1/(2*Nminus)
    for _ in range(t):
        nxt=[[0.0]*(c+1) for _ in range(2)]
        for q in (0,1):
            rate_switch=(2 if q==0 else 1)/(2*Nminus)
            for k,v in enumerate(p[q]):
                nxt[q][k]+=v*(1-rate_switch-(c-k)*up-k*down)
                nxt[1-q][k]+=v*rate_switch
                if k<c:nxt[q][k+1]+=v*(c-k)*up
                if k>0:nxt[q][k-1]+=v*k*down
        p=nxt
    pi=[comb(c,k)*((ell-1)/ell)**k*(1/ell)**(c-k) for k in range(c+1)]
    tv=sum(abs(p[q][k]-(1 if q==0 else 2)*pi[k]/3) for k in range(c+1) for q in (0,1))/2
    return c,t,tv,mixed_profile(alpha,s)

for ell in [6,8,10,12]:
    c,t,tv,pred=two_family_tv(ell,2.0,0.)
    print('two-family',ell,c,'t',t,'tv',round(tv,6),'lim',round(pred,6),'err',round(abs(tv-pred),6))
    require(abs(tv-pred)<0.10,'mixed profile finite check')

print('PASS with mixed-profile tests',checks,'assertions')
