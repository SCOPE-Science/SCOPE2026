#!/usr/bin/env python3
"""Finite semantic verification of complete-bipartite noncontingency normal forms.
Run with Python 3; no external packages.
"""
from itertools import product

def supports(q):
    return [frozenset(i for i in range(q) if mask >> i & 1) for mask in range(1, 1 << q)]

def all_states(q):
    return [(s,t,c) for s in supports(q) for t in supports(q) for c in s]

def refine(states, previous):
    dictionary={s:i for i,s in enumerate(states)}
    labels={}
    result={}
    for state in states:
        s,t,c=state
        successor={previous[(t,s,d)] for d in t}
        signature=(previous[state], frozenset(successor) if len(successor)>=2 else None)
        if signature not in labels: labels[signature]=len(labels)
        result[state]=labels[signature]
    return result

def check_symbolic(q):
    states=all_states(q)
    p={s:s[2] for s in states}
    counts=[len(set(p.values()))]
    for depth in range(1,5):
        nxt=refine(states,p)
        counts.append(len(set(nxt.values())))
        if depth==2:
            def predicted(state):
                s,t,c=state
                return (c,None,None) if len(t)==1 else (c,tuple(sorted(t)),None if len(s)==1 else tuple(sorted(s)))
            for a in states:
                for b in states:
                    assert (nxt[a]==nxt[b]) == (predicted(a)==predicted(b))
        if depth>=3:
            assert len(set(nxt.values()))==counts[2]
        p=nxt
    expected=[q,q*((1<<q)-q),q+q*(1<<(q-1))*((1<<q)-q-1)]
    assert counts[:3]==expected,(q,counts,expected)
    assert counts[3]==counts[2] and counts[4]==counts[2]
    print('symbolic',q,'states',len(states),'depth profile',counts,'OK')

def independent_finite(q,max_side=3):
    # No reference to symbolic transition graph: build actual labelled models
    models=[]
    for m in range(1,max_side+1):
        for n in range(1,max_side+1):
            for lab in product(range(q), repeat=m+n):
                models.append((m,n,lab))
    states=[]
    neighbors=[]
    for m,n,lab in models:
        start=len(states)
        for i in range(m+n):
            own=lab[:m] if i<m else lab[m:]
            other=lab[m:] if i<m else lab[:m]
            states.append((frozenset(own),frozenset(other),lab[i]))
            neigh=range(m,m+n) if i<m else range(m)
            neighbors.append(tuple(start+j for j in neigh))
    def descriptor(s):
        own,other,color=s
        return (color,None,None) if len(other)==1 else (color,other,None if len(own)==1 else own)
    v=[s[2] for s in states]
    profiles=[len(set(v))]
    for depth in range(1,4):
        labelling={}
        w=[]
        for i,s in enumerate(states):
            successor={v[j] for j in neighbors[i]}
            signature=(v[i],frozenset(successor) if len(successor)>=2 else None)
            if signature not in labelling: labelling[signature]=len(labelling)
            w.append(labelling[signature])
        v=w
        profiles.append(len(set(v)))
        if depth==2:
            desc_label={}; pred=[]
            for st in states:
                d=descriptor(st)
                if d not in desc_label:desc_label[d]=len(desc_label)
                pred.append(desc_label[d])
            assert len(set(v))==len(set(pred))
            forward={}; backward={}
            for x,y in zip(v,pred):
                forward.setdefault(x,y);backward.setdefault(y,x)
                assert forward[x]==y and backward[y]==x
    if max_side >= q:
        assert profiles[:3]==[q,q*(2**q-q),q+q*2**(q-1)*(2**q-q-1)]
    print('independent finite',q,'max_side',max_side,'models',len(models),'pointings',len(states),'profile',profiles,'OK')

if __name__=='__main__':
    for q in (2,3,4):check_symbolic(q)
    independent_finite(2,3)
    independent_finite(3,3)
    print('VERIFY_OK')
