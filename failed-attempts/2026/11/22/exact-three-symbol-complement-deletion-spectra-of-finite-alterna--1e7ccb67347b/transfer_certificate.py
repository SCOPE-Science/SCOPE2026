#!/usr/bin/env python3
"""Exact finite-state certificate for triple-pattern deletion from alternating words.

The matrix identity is checked over integers. The proof that finitely many
identities suffice is the Cayley-Hamilton argument in RESULT.md.
"""
from collections import deque
from itertools import product
from math import comb

EVEN = {
    '000':(0,1,0,0), '001':(1,-1,1,0), '010':(1,-2,2,0),
    '011':(1,-1,1,0), '100':(0,1,-1,1), '101':(1,-2,2,0),
    '110':(0,1,-1,1), '111':(0,1,0,0),
}
ODD = {
    '000':(0,1,0,0), '001':(0,1,-1,1), '010':(1,-2,2,0),
    '011':(0,1,-1,1), '100':(0,1,-1,1), '101':(0,1,-2,2),
    '110':(0,1,-1,1), '111':(0,0,1,0),
}

def machine(u):
    """Determinize epsilon-closure of interleaving NFA (phase, used letters)."""
    def closure(s):
        s=set(s)
        todo=list(s)
        while todo:
            p,j=todo.pop()
            if j < len(u) and int(u[j]) == p and (1-p,j+1) not in s:
                s.add((1-p,j+1))
                todo.append((1-p,j+1))
        return frozenset(s)
    start=closure([(0,0)])
    known={start:0}
    pending=deque([start])
    edges=[]
    while pending:
        subset=pending.popleft()
        row=[]
        for symbol in (0,1):
            after=closure((1-p,j) for p,j in subset if p==symbol)
            if after not in known:
                known[after]=len(known)
                pending.append(after)
            row.append(known[after])
        edges.append(row)
    states=list(known)
    return states,edges

def counts(edges, accepted, max_length):
    vec=[0]*len(edges)
    vec[0]=1
    out=[]
    for _ in range(max_length+1):
        out.append(sum(vec[i] for i in accepted))
        nxt=[0]*len(edges)
        for i,count in enumerate(vec):
            for j in edges[i]:
                nxt[j]+=count
        vec=nxt
    return out

def numerator_from_four(v):
    return tuple(sum((-1)**j*comb(4,j)*v[i-j] for j in range(i+1)) for i in range(4))

def delta4(v,t):
    return sum((-1)**(4-j)*comb(4,j)*v[t+j] for j in range(5))

if __name__=='__main__':
    total=0
    for seq in map(''.join,product('01', repeat=3)):
        states,edges=machine(seq)
        q=len(states)
        assert q<=10
        even_acc={i for i,s in enumerate(states) if (0,3) in s}
        odd_acc={i for i,s in enumerate(states) if (1,3) in s}
        cc_even=counts(edges, even_acc, 2*(q+3)+1)
        cc_odd=counts(edges, odd_acc, 2*(q+3))
        f=[cc_even[2*t+1] for t in range(q+4)]
        g=[cc_odd[2*t] for t in range(q+4)]
        assert numerator_from_four(f[:4])==EVEN[seq],(seq,'even',numerator_from_four(f[:4]))
        assert numerator_from_four(g[:4])==ODD[seq],(seq,'odd',numerator_from_four(g[:4]))
        assert all(delta4(f,t)==0 for t in range(q)),(seq,'even-CH')
        assert all(delta4(g,t)==0 for t in range(q)),(seq,'odd-CH')
        total+=2*q
        print(seq, 'states',q, 'edges',edges, 'accept-even',sorted(even_acc),
              'accept-odd',sorted(odd_acc))
        print('  first4-even',f[:4],'GF numerator',EVEN[seq],
              'first4-odd',g[:4],'GF numerator',ODD[seq])
    print('TRANSFER_CERTIFICATE_OK 8 patterns 16 rational identities',total,'exact fourth-difference zero checks')
