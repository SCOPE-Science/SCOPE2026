#!/usr/bin/env python3
"""Canonical states, explicit Myhill–Nerode separating words, and CRT reachability."""
from math import gcd
from itertools import product


def step(r,s,st,c):
    i,S=st
    if c=='a': return ((i+1)%r, frozenset((j+1)%s for j in S))
    return (i, S|frozenset((0,)) if i==0 else S)

def accepts(r,s,st,w):
    for c in w: st=step(r,s,st,c)
    return 0 in st[1]

def signature(r,s,st):
    i,S=st;g=gcd(r,s)
    full=frozenset(j for j in range(s) if j%g==i%g)
    if S==full: return ('sat',i%g)
    return ('unsat',i,tuple(sorted(S)))

def separator(r,s,u,v):
    i,S=u;h,T=v
    if S!=T:
        j=next(iter(S^T)); t=(-j)%s
        assert accepts(r,s,u,'a'*t)!=accepts(r,s,v,'a'*t)
        return 'a'*t
    if i==h: return None
    # Same subsets, different C-cycle phases.
    # If unsaturated, choose a residue missing from S that aligns i to 0.
    g=gcd(r,s)
    missing=next((j for j in range(s) if j%g==i%g and j not in S),None)
    if missing is None:
        # Empty S with differing coset residues: any j in current phase is missing.
        assert not S
        missing=i%g
    # A suitable nonnegative t exists by CRT; finite brute search is only
    # checker logic (the proof uses CRT for every r,s).
    t=next(k for k in range(r*s+1) if (i+k)%r==0 and (j:=((-k)%s)) not in S)
    # We need target's S not to have D0 either; since S=T, fine.
    w='a'*t+'b'
    assert accepts(r,s,u,w) != accepts(r,s,v,w),(r,s,u,v,w)
    return w

def generated_prefix(r,s,target):
    i,S=target
    # Explicit constructive reachability via marks at selected a-counts.
    # Increase total T by multiples of r until all CRT positions lie below T.
    T=i
    positions=[]
    for _ in range(3*s+3):
        positions=[]
        for j in sorted(S):
            k=next((k for k in range(T+1) if k%r==0 and (T-k)%s==j), None)
            if k is None: break
            positions.append(k)
        if len(positions)==len(S):break
        T+=r
    assert len(positions)==len(S),(r,s,target)
    assert len(set(positions))==len(positions)
    marks=set(positions)
    w=''.join(('b' if k in marks else '') + ('a' if k<T else '') for k in range(T+1))
    st=(0,frozenset())
    for c in w: st=step(r,s,st,c)
    assert st==target,(r,s,target,w,st)
    return w

def main():
    targets=0; compared=0; max_witness=0
    for r in range(1,7):
        for s in range(1,7):
            g=gcd(r,s)
            st=[]
            for i in range(r):
                J=[j for j in range(s) if j%g==i%g]
                st.extend((i,frozenset(J[k] for k in range(len(J)) if (m>>k)&1)) for m in range(1<<len(J)))
            assert len(st)==r*2**(s//g)
            for v in st:
                witness=generated_prefix(r,s,v)
                max_witness=max(max_witness,len(witness));targets+=1
            for a in range(len(st)):
                for b in range(a):
                    u,v=st[a],st[b]
                    same=signature(r,s,u)==signature(r,s,v)
                    if same:
                        # Saturated-coset pairs or identical physical state.
                        assert u==v or (len(u[1])==s//g and u[1]==v[1])
                        for w in ('','a','b','aab','babaa','bbaaaab'):
                            assert accepts(r,s,u,w)==accepts(r,s,v,w)
                    else:
                        w=separator(r,s,u,v)
                        assert w is not None
                    compared+=1
    print('PASS canonical-state CRT reachability and distinguishing suffixes')
    print('parameters r,s in [1,6], reachable states tested:',targets)
    print('ordered state-pair comparisons:',compared)
    print('maximum constructed prefix length:',max_witness)
    print('all inequivalent canonical states separated and saturated coset mergers confirmed')

if __name__=='__main__':main()
