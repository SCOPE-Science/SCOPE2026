#!/usr/bin/env python3
"""Exact checks of four-site stochastic SIR peak-capacity ranking theorem.
Requires Python 3 and SymPy. Run: python verify.py
All rates are recovery-normalized; no simulation is used.
"""
import itertools
from functools import lru_cache
from fractions import Fraction
import sympy as S

b=S.Symbol('b',positive=True)

def canonical(n,edges):
    e={tuple(sorted(x)) for x in edges}
    mask=[]
    for p in itertools.permutations(range(n)):
        mask.append(tuple(sorted(tuple(sorted((p[i],p[j]))) for i,j in e)))
    return min(mask)

def connected(n,edges):
    seen={0}
    while 1:
        nxt=seen|{v for u,v in edges if u in seen}|{u for u,v in edges if v in seen}
        if nxt==seen: return len(seen)==n
        seen=nxt

def small_graphs():
    count=0; reps={}
    for n in range(2,5):
        all_edges=list(itertools.combinations(range(n),2))
        for mask in range(1<<len(all_edges)):
            e=[pair for j,pair in enumerate(all_edges) if mask>>j&1]
            if not connected(n,e):continue
            count+=1; reps.setdefault((n,canonical(n,e)),(n,e))
    assert count==43 and len(reps)==9,(count,len(reps)) # 1 + 2 + 6 nonisomorphic = 9, see below
    return reps

def probabilities(n,edges):
    adj=[0]*n
    for u,v in edges:adj[u]|=1<<v;adj[v]|=1<<u
    @lru_cache(None)
    def F(s,i):
        if i==0:return (S.Integer(0),)*n
        k=i.bit_count(); moves=[]; total=S.Integer(k)
        for v in range(n):
            bit=1<<v
            if i&bit:moves.append((S.Integer(1),s,i^bit))
            elif s&bit:
                wt=b*(adj[v]&i).bit_count()
                if wt: moves.append((wt,s^bit,i|bit));total+=wt
        ans=[S.Integer(1)]*k+[S.Integer(0)]*(n-k)
        for wt,s1,i1 in moves:
            vals=F(s1,i1)
            for j in range(k,n):ans[j]+=wt*vals[j]/total
        return tuple(S.cancel(x) for x in ans)
    return [F(((1<<n)-1)^(1<<r),1<<r) for r in range(n)]

def positive_coeff_ratio(expr):
    expr=S.cancel(expr)
    if expr==0:return True
    num,den=S.fraction(expr)
    num=S.Poly(num,b);den=S.Poly(den,b)
    return all(x>=0 for x in num.all_coeffs()) and all(x>=0 for x in den.all_coeffs()) and num.eval(1)>0 and den.eval(1)>0

def score_degree(n,edges):
    d=[0]*n
    for u,v in edges:d[u]+=1;d[v]+=1
    return d


def symbolic_check():
    # All 43 connected labeled graphs are represented by 9 unlabeled graph classes.
    reps=small_graphs(); nclasses={2:0,3:0,4:0}; totals=0
    q=2*b**4-32*b**3-58*b**2-33*b-6
    for n,edges in reps.values():
        nclasses[n]+=1
        probs=probabilities(n,edges)
        deg=score_degree(n,edges)
        pairs={tuple(sorted((u,v))) for u,v in edges}
        # The paw (triangle with a single leaf) has degree sequence (1,2,2,3).
        paw=(n==4 and sorted(deg)==[1,2,2,3])
        if paw:
            hub=deg.index(3); tris=[v for v in range(n) if deg[v]==2];leaf=deg.index(1)
            assert len(tris)==2
            for k in range(1,n):
                if k==2:
                    # Unique switch: sign(triangle minus hub) = sign(q)
                    dif=S.factor(probs[tris[0]][k]-probs[hub][k])
                    den=S.factor(S.fraction(S.cancel(dif))[1]); num=S.factor(S.fraction(S.cancel(dif))[0]);
                    assert S.simplify(num/(b*b*q))==1
                    assert positive_coeff_ratio(den)
                    assert positive_coeff_ratio(probs[tris[0]][k]-probs[leaf][k])
                    assert S.simplify(probs[tris[0]][k]-probs[tris[1]][k])==0
                else:
                    for r in range(n):
                        assert positive_coeff_ratio(probs[hub][k]-probs[r][k]),(n,edges,k,r)
                        totals+=1
        else:
            # For every other connected class up to size four, every maximum-degree
            # vertex is a maximizer for every peak threshold, at every b>0.
            mx=max(deg); winner=deg.index(mx)
            for k in range(1,n):
                for r in range(n):
                    assert positive_coeff_ratio(probs[winner][k]-probs[r][k]),(n,edges,k,r)
                    totals+=1
    assert nclasses=={2:1,3:2,4:6},nclasses
    assert q.subs(b,17)<0 and q.subs(b,18)>0
    assert S.Poly(q,b).count_roots(0,S.oo)==1
    print('Symbolic graph classes:',nclasses,'; certified analytic comparisons:',totals)
    return q

def path_enumeration(n,edges,root,K,beta):
    """Independent sum over all finite event paths (no cached state recursion)."""
    adj=[set() for _ in range(n)]
    for u,v in edges:adj[u].add(v);adj[v].add(u)
    def walk(s,i,weight):
        if len(i)>=K:return weight
        if not i:return Fraction(0)
        ev=[]
        for v in i:ev.append((1, s, i-{v}))
        for v in s:
            rate=beta*len(adj[v]&i)
            if rate:ev.append((rate,s-{v},i|{v}))
        denom=sum(w for w,_,_ in ev)
        return sum((walk(s1,i1,weight*Fraction(w,denom)) for w,s1,i1 in ev),Fraction(0))
    return walk(set(range(n))-{root},{root},Fraction(1))

def exact_witness():
    edges=[(0,3),(1,2),(1,3),(2,3)]
    symbolic=probabilities(4,edges)
    for root in range(4):
        for K in (2,3,4):
            x=path_enumeration(4,edges,root,K,18)
            y=S.Rational(symbolic[root][K-1].subs(b,18))
            assert S.Rational(x.numerator,x.denominator)==y,(root,K,x,y)
    expected={0:(Fraction(18,19),Fraction(233604,253783),Fraction(3888,4693)),
              1:(Fraction(36,37),Fraction(16595604,17297315),Fraction(361584,447811)),
              3:(Fraction(54,55),Fraction(24668064,25712225),Fraction(559872,665665))}
    for root,values in expected.items():
        for K in (2,3,4):
            assert path_enumeration(4,edges,root,K,18)==values[K-2]
    print('Independent exact path enumeration: 12 seed/threshold comparisons passed')
    print('Witness at b=18: capacity 2 -> hub 3, capacity 3 -> triangle 1 or 2, capacity 4 -> hub 3')

if __name__=='__main__':
    symbolic_check();exact_witness();print('PASS: exact finite classification and independent witness')
