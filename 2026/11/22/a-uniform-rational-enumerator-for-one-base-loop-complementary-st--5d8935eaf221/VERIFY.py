#!/usr/bin/env python3
"""Exact polynomial-state verification for fixed-point-free-complement 5-factor avoidance.
No external packages are required. Execute: python3 VERIFY.py
"""
from collections import Counter
from itertools import product

# A polynomial in q is represented by ascending integer coefficients.
def trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0: a.pop()
    return tuple(a)

def add(a,b):
    return trim([(a[i] if i < len(a) else 0)+(b[i] if i < len(b) else 0)
                 for i in range(max(len(a),len(b)))])
def neg(a): return tuple(-x for x in a)
def sub(a,b): return add(a,neg(b))
def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return trim(c)
def evaluate(a,q): return sum(x*q**i for i,x in enumerate(a))
ZERO=(0,); ONE=(1,); Q=(0,1)

def canonical(w):
    first={};out=[]
    for x in w:
        pair, bit=divmod(x,2)
        if pair not in first: first[pair]=(len(first),bit)
        j,initial_bit=first[pair]
        out.append(2*j+(bit^initial_bit))
    return tuple(out)

STATES=tuple(sorted({canonical(w) for w in product(range(8),repeat=4)}))
assert len(STATES)==49
assert Counter(len({x//2 for x in w}) for w in STATES)=={1:8,2:28,3:12,4:1}
index={w:i for i,w in enumerate(STATES)}
# Formally weighted transitions. Labels 0..2k-1 already occurred, and
# one placeholder 2k for a fresh complementary letter pair.
TRANS=[];WEIGHTS=[]
for w in STATES:
    k=len({x//2 for x in w}); edges=[]
    for x in range(2*k+1):
        if w[0] == (x^1) and w[1] == (w[3]^1): continue
        new=canonical(w[1:]+(x,))
        edges.append((index[new], sub(Q,(2*k,)) if x==2*k else ONE))
    TRANS.append(edges)
    p=ONE
    for j in range(k): p=mul(p,sub(Q,(2*j,)))
    WEIGHTS.append(p)

def step(u):
    return tuple(sum_poly(mul(coeff,u[j]) for j,coeff in edges) for edges in TRANS)
def sum_poly(vals):
    out=ZERO
    for v in vals:out=add(out,v)
    return out

vectors=[tuple(ONE for _ in STATES)]
for _ in range(11):vectors.append(step(vectors[-1]))
# Symbolic identity in Z[q] for every canonical four-letter state.
for i in range(len(STATES)):
    lhs=sub(vectors[5][i],mul(Q,vectors[4][i]))
    lhs=add(lhs,vectors[3][i]);lhs=sub(lhs,vectors[2][i])
    lhs=add(lhs,mul(sub(Q,(2,)),vectors[1][i]))
    lhs=add(lhs,mul(sub(Q,(1,)),vectors[0][i]))
    assert lhs==ZERO,(i,STATES[i],lhs)

seq=[]
for u in vectors:
    seq.append(sum_poly(mul(v,a) for v,a in zip(WEIGHTS,u)))
assert seq[0]==(0,0,0,0,1)  # q^4
# D(z)=(1,-q,1,-1,q-2,q-1), N(z)=sum_{i=0}^4 N_i(q) z^i.
D=(ONE, neg(Q), ONE, (-1,), sub(Q,(2,)), sub(Q,(1,)))
N=(mul(Q,mul(Q,mul(Q,Q))), neg(mul(Q,mul(Q,Q))), mul(Q,Q),
   neg(mul(mul(Q,mul(Q,Q)),sub(Q,ONE))),
   neg(mul(mul(Q,Q),add(sub(mul(Q,Q),Q),ONE))))
for i in range(5):
    value=sum_poly(mul(D[j],seq[i-j]) for j in range(i+1))
    assert value==N[i],(i,value,N[i])
# All later coefficients of D(z) * sum_{k>=0}a_{4+k}z^k vanish.
for i in range(5,len(seq)):
    value=sum_poly(mul(D[j],seq[i-j]) for j in range(6))
    assert value==ZERO,(i,value)

# Independently count by ordinary length-four suffix states, and by brute force.
def avoids(w):
    return all(not (w[j]==(w[j+4]^1) and w[j+1]==(w[j+3]^1))
               for j in range(len(w)-4))
def dp_counts(q,N):
    total={w:1 for w in product(range(q),repeat=4)}
    arr=[1,q,q*q,q**3,q**4]
    for n in range(5,N+1):
        nd={}
        for w,count in total.items():
            for x in range(q):
                if w[0] == (x^1) and w[1] == (w[3]^1):continue
                v=w[1:]+(x,)
                nd[v]=nd.get(v,0)+count
        total=nd;arr.append(sum(total.values()))
    return arr

for q,N,brute_max in [(2,25,16),(4,25,9),(6,20,7),(8,15,5)]:
    dp=dp_counts(q,N)
    a=[evaluate(x,q) for x in seq]
    assert dp[4:4+len(a)]==a
    # Compute all coefficients with the symbolic universal recurrence.
    for n in range(4+len(a),N+1):
        dp_prev=dp[n-5:n]
        expected=q*dp[n-1]-dp[n-2]+dp[n-3]-(q-2)*dp[n-4]-(q-1)*dp[n-5]
        assert dp[n]==expected
    for n in range(brute_max+1):
        count=sum(avoids(w) for w in product(range(q),repeat=n))
        assert count==dp[n],(q,n,count,dp[n])
    print('PASS q=%d: DP up to n=%d; exhaustive words to n=%d'%(q,N,brute_max))

# An independent check that the DNA four-letter-suffix digraph is strongly
# connected and aperiodic, allowing Perron-Frobenius capacity interpretation.
q=4;nodes=list(product(range(q),repeat=4)); ids={w:i for i,w in enumerate(nodes)}
graph=[];rev=[[] for _ in nodes]
for i,w in enumerate(nodes):
    successors=[ids[w[1:]+(x,)] for x in range(q)
                if not(w[0]==(x^1) and w[1]==(w[3]^1))]
    graph.append(successors)
    for j in successors:rev[j].append(i)
def visit(g):
    seen={0};stack=[0]
    while stack:
        for j in g[stack.pop()]:
            if j not in seen: seen.add(j);stack.append(j)
    return len(seen)
assert visit(graph)==visit(rev)==256
assert any(i in ar for i,ar in enumerate(graph))
print('PASS symbolic recurrence on 49 canonical states, all even alphabet sizes; DNA graph primitive')
