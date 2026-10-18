#!/usr/bin/env python3
from itertools import product
from pathlib import Path
import json

def fib(n):
    a,b=1,1
    if n in (1,2): return 1
    for _ in range(3,n+1):
        a,b=b,a+b
    return b

def iota_binary(w):
    # This routine is used only when alph(w)={0,1}.
    seen=set()
    k=0
    for c in w:
        seen.add(c)
        if seen=={"0","1"}:
            k+=1
            seen.clear()
    return k

def is_subseq(u,w):
    j=0
    for c in w:
        if j<len(u) and c==u[j]:
            j+=1
    return j==len(u)

def sas_direct(w):
    k=iota_binary(w)
    return {
        ''.join(t) for t in product("01", repeat=k+1)
        if not is_subseq(''.join(t),w)
    }

def A(k, first="01"):
    other="10" if first=="01" else "01"
    return ''.join(first if i%2==0 else other for i in range(k))

# Engine 1: the two-state inequality automaton for a prescribed sequence
# of minimal binary arches.
def dp_count(blocks):
    p=q=1
    for b in blocks:
        if b=="01":
            p,q=p+q,q
        elif b=="10":
            p,q=p,p+q
        else:
            raise AssertionError(b)
    return p+q

# Check exact Fibonacci counts directly and by DP.
for k in range(1,16):
    w=A(k)
    assert iota_binary(w)==k
    assert dp_count([w[2*i:2*i+2] for i in range(k)])==fib(k+3)
    if k<=10:
        assert len(sas_direct(w))==fib(k+3)

# Engine 2: exhaust all 2^k minimal-arch orientation patterns.
# It independently verifies the equality pattern for a substantial prefix.
for k in range(1,13):
    vals=[]
    for bits in product((0,1), repeat=k):
        blocks=["01" if b==0 else "10" for b in bits]
        vals.append((dp_count(blocks),bits))
    m=max(v for v,_ in vals)
    maxbits=[b for v,b in vals if v==m]
    assert m==fib(k+3)
    assert len(maxbits)==2
    assert all(maxbits[j][i] != maxbits[j][i+1]
               for j in range(2) for i in range(k-1))

# Engine 3: brute-force arbitrary binary words through length 12.
# Universality and absence are computed directly, with no DP reduction.
# This checks the global bound in all accessible small cases and the exact
# equality classification at every minimum length 2k in this range.
for n in range(2,13):
    for tup in product("01", repeat=n):
        w=''.join(tup)
        if set(w)!={"0","1"}:
            continue
        k=iota_binary(w)
        if k<1:
            continue
        c=len(sas_direct(w))
        assert c<=fib(k+3), (w,k,c)
        if n==2*k and c==fib(k+3):
            assert w in {A(k,"01"),A(k,"10")}, (w,k,c)

# A symbolic finite-step check of the inductive Fibonacci envelope:
# from any p,q with sorted bounds F_{i+1},F_{i+2}, either update keeps
# one old coordinate and replaces the other by p+q.
for i in range(1,12):
    lo,hi=fib(i+1),fib(i+2)
    for p in range(1,lo+1):
        for q in range(p,hi+1):
            for x,y in ((p+q,q),(p,p+q)):
                a,b=sorted((x,y))
                assert a<=fib(i+2) and b<=fib(i+3)

cert=json.loads((Path(__file__).resolve().parent/"certificate.json").read_text(encoding="utf-8"))
assert cert["direct_values"]=={str(k):fib(k+3) for k in range(1,11)}
print("VERIFY_OK fib_max_k=1..15 direct_sas_k=1..10 "
      "orientation_census_k=1..12 arbitrary_words_length<=12 "
      "minimum_length_equality=alternating+complement dp_engines=3")
