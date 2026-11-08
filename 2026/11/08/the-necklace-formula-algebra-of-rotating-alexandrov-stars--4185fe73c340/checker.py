#!/usr/bin/env python3
"""Finite checks for Boolean DTL on a rooted Alexandrov star with rotating leaves.

Usage: python3 checker.py
The general theorem is proved in RESULT.md; this checks finite parameters,
formula characteristics, and independent bisimulation refinements.
"""
from itertools import product
from math import gcd
from functools import lru_cache


def word_necklace(w):
    n = len(w)
    return min(w[i:] + w[:i] for i in range(n))


def predicted(Q, m):
    necklaces = {word_necklace(w) for w in product(range(Q), repeat=m)}
    return Q**m + Q*len(necklaces) - Q


def semantic_profile(colors, x):
    m = len(colors)-1
    if x:
        word = colors[x:] + colors[1:x]
        return ('leaf', word)
    word = word_necklace(colors[1:])
    if len(set(colors)) == 1:
        return ('leaf', (colors[0],)*m)
    return ('root', colors[0], word)


def all_states(k, m):
    Q = 2**k
    return [(v,x) for v in product(range(Q), repeat=m+1) for x in range(m+1)]


def bisim_partition(k, m):
    states = all_states(k,m)
    index = {t:i for i,t in enumerate(states)}
    nxt = [index[(v,0 if x==0 else x%m+1)] for v,x in states]
    closure = [tuple(index[(v,y)] for y in (range(m+1) if x==0 else (x,)))
               for v,x in states]
    cls = [v[x] for v,x in states]
    for t in range(3*m+10):
        sig = [(cls[i], cls[nxt[i]], tuple(sorted({cls[y] for y in closure[i]})))
               for i in range(len(states))]
        labels = {s:i for i,s in enumerate(sorted(set(sig)))}
        new = [labels[s] for s in sig]
        if len(set(new)) == len(set(cls)):
            cls = new
            break
        cls = new
    else:
        raise AssertionError('partition not stable')
    profiles = [semantic_profile(*s) for s in states]
    table = {}
    reverse = {}
    for p,c in zip(profiles,cls):
        if p in table: assert table[p] == c
        else: table[p] = c
        if c in reverse: assert reverse[c] == p
        else: reverse[c] = p
    expected = predicted(2**k, m)
    assert len(table)==len(reverse)==expected
    return states, profiles

# Formula syntax and evaluation are distinct from bisimulation refinement.
TRUE=('true',)
FALSE=('false',)

def Atom(j): return ('p',j)
def Not(a): return ('not',a)
def And(*a): return ('and',a)
def Or(*a): return ('or',a)
def Next(a): return ('next',a)
def Diamond(a): return ('diamond',a)
def Box(a): return ('box',a)
def Eventually(a): return ('eventually',a)

def color_expr(c,k):
    return And(*tuple(Atom(j) if ((c>>j)&1) else Not(Atom(j)) for j in range(k)))

def temporal_word_expr(w,k):
    terms=[]
    for j,c in enumerate(w):
        a=color_expr(c,k)
        for _ in range(j): a=Next(a)
        terms.append(a)
    return And(*terms)

def difference_expr(k):
    return Or(*[Or(And(Atom(j),Diamond(Not(Atom(j)))),
                   And(Not(Atom(j)),Diamond(Atom(j)))) for j in range(k)])

def profile_expr(profile,k,m):
    if profile[0]=='leaf':
        w=profile[1]
        a=temporal_word_expr(w,k)
        if len(set(w))==1:
            a=And(a,Box(color_expr(w[0],k)))
        return a
    _,c,w=profile
    delta=difference_expr(k)
    rotations={w[j:]+w[:j] for j in range(m)}
    leaf_test=Or(*[temporal_word_expr(v,k) for v in sorted(rotations)])
    return And(delta,color_expr(c,k),Box(Or(delta,leaf_test)))

@lru_cache(maxsize=None)
def evaluate(phi,v,x):
    op=phi[0];m=len(v)-1
    if op=='true':return True
    if op=='false':return False
    if op=='p':return bool((v[x]>>phi[1])&1)
    if op=='not':return not evaluate(phi[1],v,x)
    if op=='and':return all(evaluate(p,v,x) for p in phi[1])
    if op=='or':return any(evaluate(p,v,x) for p in phi[1])
    if op=='next':return evaluate(phi[1],v,0 if x==0 else x%m+1)
    if op=='diamond':return any(evaluate(phi[1],v,y) for y in (range(m+1) if x==0 else (x,)))
    if op=='box':return all(evaluate(phi[1],v,y) for y in (range(m+1) if x==0 else (x,)))
    if op=='eventually':
        return any(evaluate(phi[1],v,y) for y in ((0,) if x==0 else (1+(x-1+j)%m for j in range(m))))
    raise ValueError(op)


def check_characteristics(k,m):
    states, ps=bisim_partition(k,m)
    names=set(ps)
    formulas={p:profile_expr(p,k,m) for p in names}
    for (v,x),p in zip(states,ps):
        hits=[key for key,f in formulas.items() if evaluate(f,v,x)]
        assert hits==[p],(k,m,v,x,p,hits)
    # Verify that adding eventuality does not separate bisimulation types.
    base=[Atom(j) for j in range(k)]+[TRUE,FALSE]
    terms=base[:]
    for j in range(2):
        a=terms[-1];b=terms[max(0,len(terms)//2)]
        terms.extend([Not(a),Next(a),Diamond(a),Box(a),Eventually(a),And(a,b),Or(a,b)])
    for f in terms:
        byprofile={}
        for (v,x),p in zip(states,ps):
            val=evaluate(f,v,x)
            if p in byprofile: assert byprofile[p]==val,(f,p)
            else: byprofile[p]=val
    return len(states),len(names)


def run():
    cases=[(0,1),(0,3),(1,1),(1,2),(1,3),(1,4),(1,5),(2,1),(2,2),(2,3),(3,1)]
    for k,m in cases:
        states,profs=bisim_partition(k,m)
        if (k,m) in [(0,1),(0,3),(1,1),(1,2),(1,3),(1,4),(2,1),(2,2)]:
            count,types=check_characteristics(k,m)
            assert count==len(states) and types==len(set(profs))
        print('k=',k,'m=',m,'pointed=',len(states),'types=',len(set(profs)))
    print('DYNAMIC_ALEXANDROV_NECKLACE_ALGEBRA_OK')

if __name__=='__main__': run()
