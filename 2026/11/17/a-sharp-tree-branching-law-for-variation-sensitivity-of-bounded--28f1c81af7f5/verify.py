#!/usr/bin/env python3
"""Exact finite diagnostics for graph-variation stability of bounded-slope regression.
Only finite cases are checked; all-order results rely on the accompanying proof.
"""
from fractions import Fraction as F
from itertools import product
from collections import deque

def prufer_edges(sequence):
    n=len(sequence)+2
    deg=[1]*n
    for v in sequence: deg[v]+=1
    E=[]
    for v in sequence:
        leaf=min(i for i in range(n) if deg[i]==1)
        E.append((leaf,v));deg[leaf]-=1;deg[v]-=1
    a,b=(i for i in range(n) if deg[i]==1)
    E.append((a,b))
    return E

def adj(n,E):
    A=[[] for _ in range(n)]
    for i,(u,v) in enumerate(E):
        A[u].append((v,i));A[v].append((u,i))
    return A

def side(n,A,e,u):
    seen={u};q=[u]
    for x in q:
        for y,j in A[x]:
            if j!=e and y not in seen:
                seen.add(y);q.append(y)
    return seen

def components(n,E,mask):
    pa=list(range(n))
    def root(u):
        while pa[u]!=u: u=pa[u]
        return u
    for i,(u,v) in enumerate(E):
        if mask>>i&1: pa[root(u)]=root(v)
    return [root(i) for i in range(n)]

def exact_derivative_gain(n,E,mask):
    A=adj(n,E); cls=components(n,E,mask)
    groups={}
    for i,c in enumerate(cls): groups.setdefault(c,[]).append(i)
    values=[]
    for e,(u,v) in enumerate(E):
        U=side(n,A,e,u)
        m={c:F(sum(i in U for i in group),len(group)) for c,group in groups.items()}
        q=[m[cls[i]] for i in range(n)]
        gain=sum(abs(q[x]-q[y]) for x,y in E)
        values.append(gain)
        if mask>>e&1:
            S=set(groups[cls[u]]);a=len(S&U);b=len(S)-a
            dU=sum(1 for x,y in E if (x in S) != (y in S) and (x if x in S else y) in U)
            dV=sum(1 for x,y in E if (x in S) != (y in S) and (x if x in S else y) not in U)
            predicted=F(b*dU+a*dV,len(S))
        else: predicted=F(1)
        assert gain==predicted,(n,E,mask,e,gain,predicted)
    return max(values)

def formula_connected(n,E):
    A=adj(n,E)
    val=F(1)
    # all nonempty connected subtrees, using induced connectivity
    for mask in range(1,1<<n):
        S={i for i in range(n) if mask>>i&1}
        eS=[(k,u,v) for k,(u,v) in enumerate(E) if u in S and v in S]
        if len(eS)!=len(S)-1: continue
        d=[(u,v) for u,v in E if (u in S)!=(v in S)]
        for k,u,v in eS:
            U=side(n,A,k,u)
            a=len(S&U);b=len(S)-a
            deltaU=sum(1 for x,y in d if (x if x in S else y) in U)
            deltaV=len(d)-deltaU
            val=max(val,F(b*deltaU+a*deltaV,len(S)))
    return val

def envelope(n):
    return max([F(1)]+[F((s-1)*(n-s),s) for s in range(2,n)])

def is_path_or_claw(n,E):
    deg=[0]*n
    for u,v in E:deg[u]+=1;deg[v]+=1
    return max(deg)<=2 or (n==4 and sorted(deg)==[1,1,1,3])

def exact_kkt_broom_witness(n,s):
    assert 2 <= s < n
    # Path S=(0,1,...,s-1), with n-s additional leaves at 0.
    E=[(i,i+1) for i in range(s-1)]+[(0,i) for i in range(s,n)]
    active=E[:s-1]
    z=[F(0)]*n
    for i in range(1,s): z[i]=F(i)
    lam=[F(1)]*(s-1)
    x=z.copy()
    for i in range(s-1): x[i]-=lam[i];x[i+1]+=lam[i]
    h=[F(int(i==0 or i>=s)) for i in range(n)]
    q=[F(1,s) if i<s else F(1) for i in range(n)]
    eps=F(1,10*n)
    x1=[x[i]+eps*h[i] for i in range(n)]
    z1=[z[i]+eps*q[i] for i in range(n)]
    # The exact stationarity residual equals the incidence transpose
    # of the following strictly positive Lagrange multipliers.
    mu=[]
    for i in range(s-1):
        coeff=sum((h[j]-q[j] for j in range(i+1,s)),F(0))
        mu.append(lam[i]+eps*coeff)
    assert all(v>0 for v in mu)
    residual=[x1[i]-z1[i] for i in range(n)]
    modeled=[F(0)]*n
    for i,c in enumerate(mu): modeled[i]-=c;modeled[i+1]+=c
    assert modeled==residual
    for j,(u,v) in enumerate(E):
        diff=abs(z1[v]-z1[u]);assert diff <=1
        if j<s-1: assert z1[v]-z1[u]==1
        else: assert diff < 1
    delta_in=sum(abs(h[v]-h[u]) for u,v in E)
    delta_out=sum(abs(q[v]-q[u]) for u,v in E)
    assert delta_in==1
    assert delta_out==F((s-1)*(n-s),s)
    return delta_out

def check():
    count=0; faces=0
    for n in range(2,7):
        maximum=F(0)
        for seq in product(range(n),repeat=n-2):
            E=prufer_edges(seq)
            L=formula_connected(n,E)
            assert (L==1)==is_path_or_claw(n,E), (n,E,L)
            for mask in range(1<<(n-1)):
                val=exact_derivative_gain(n,E,mask)
                assert val<=L,(n,E,mask,val,L)
                faces+=1
            maximum=max(maximum,L);count+=1
        assert maximum==envelope(n),(n,maximum,envelope(n))
        print('ALL_LABELLED_TREES_AND_ACTIVE_FACES_PASS',n,'max',maximum)
    print('TOTAL_TREES_PASS',count,'TOTAL_ACTIVE_FACES_PASS',faces)
    for n in range(2,501):
        U=envelope(n)
        # each size s is realized by a broom whose central active component has size s
        for s in range(2,n):
            f=F((s-1)*(n-s),s)
            assert f<=U
        # optimizer s near sqrt n by discrete difference
        if n>=3:
            scores=[(F((s-1)*(n-s),s),s) for s in range(2,n)]
            maxscore=max(v for v,s in scores)
            for v,s in scores:
                if v==maxscore:
                    assert s*(s-1)<=n<=s*(s+1)
        if n>=4: assert float(U)<=n+1-2*(n**.5)+1e-8
        assert U>=F(1)
    print('GLOBAL_ENVELOPE_CANDIDATE_AND_INTEGER_OPTIMIZER_PASS',499)
    for n,s in ((5,2),(6,2),(9,3),(16,4),(50,7)):
        print('EXPLICIT_TWO_INPUT_KKT_WITNESS_PASS',n,s,exact_kkt_broom_witness(n,s))
    print('ALL_TREE_LIPSCHITZ_BV_CHECKS_PASS')

if __name__=='__main__': check()
