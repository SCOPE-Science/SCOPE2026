#!/usr/bin/env python3
"""Separate literal mutation enumeration and Euler-trail witness checker."""
from itertools import product
from collections import Counter, defaultdict

def profile(word,q):
    c=[0]*(q*q)
    for i in range(len(word)-1):c[q*word[i]+word[i+1]]+=1
    return tuple(c)

def count_mutants(word,q):
    seen=set()
    for i in range(len(word)):
        for replacement in range(q):
            if replacement==word[i]:continue
            x=list(word)
            x[i]=replacement
            seen.add(profile(x,q))
    return len(seen)

def euler_debruijn(q):
    # Deterministic Hierholzer traversal on the q-ary order-two graph.
    adj={(a,b):list(reversed(range(q))) for a in range(q) for b in range(q)}
    stack=[(0,0)]
    end=[]
    while stack:
        v=stack[-1]
        if adj[v]:
            c=adj[v].pop()
            stack.append((v[1],c))
        else:
            end.append(stack.pop())
    vertices=list(reversed(end))
    assert len(vertices)==q**3+1
    word=tuple(vertices[0])+tuple(v[1] for v in vertices[1:])
    return word

for q,nmax in ((2,11),(3,8),(4,6)):
    last=[]
    for n in range(1,nmax+1):
        best=0
        num=0
        for w in product(range(q),repeat=n):
            z=count_mutants(w,q)
            if z>best:best=z;num=1
            elif z==best:num+=1
        last.append(best)
    print('q=%d exhaustive n=1..%d max_by_length=%s' % (q,nmax,','.join(map(str,last))))
for q in (2,3,4,5,6):
    w=euler_debruijn(q)
    assert len(w)==q**3+2
    assert len(set(w[i:i+3] for i in range(len(w)-2)))==q**3
    cap=(q-1)*(q*(q*q-1)+2)
    assert count_mutants(w,q)==cap
    print('q=%d independent_euler_witness n=%d capacity=%d' % (q,len(w),cap))
# For q=2, independently count every shortest-order-3 de Bruijn linear word.
number=0
for w in product(range(2),repeat=10):
    if len(set(w[i:i+3] for i in range(8)))==8:
        number+=1
assert number==16
print('order3 binary debruijn linear count=16')
print('ENUMERATION_CHECK_PASS')
