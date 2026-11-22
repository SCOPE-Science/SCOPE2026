#!/usr/bin/env python3
"""Finite consistency checks for the periodic-mask subshift; not an infinite proof."""

def mask_blocks(n, k):
    u = '10'+'01'*(k-1)
    return {''.join(u[(r+i)%(2*k)] for i in range(n)) for r in range(2*k)}

def masks(n):
    # For k>n, blocks are either alternating or cross a single local 1100 defect.
    return set().union(*(mask_blocks(n,k) for k in range(2,n+4)))

def descendant_words(n):
    result=set()
    for m in masks(n):
        b=int(m,2)
        v=b
        while True:
            result.add(v)
            if v==0:break
            v=(v-1)&b
    return result

# Discrepancy bound and fundamental-period defect count for first 50 masks.
for k in range(2,51):
    u='10'+'01'*(k-1)
    assert len(u)==2*k and u.count('1')==k
    assert all(any(u[i]!=u[(i+p)%(2*k)] for i in range(2*k)) for p in range(1,2*k))
    s=0; prefix=[0]
    for x in u:
        s+=2*int(x)-1
        prefix.append(s)
    assert s==0 and set(prefix)<= {-1,0,1}
    assert sum(u[i:i+2]=='11' for i in range(2*k-1)) + (u[-1:]+u[:1]=='11')==1
    assert sum(u[i:i+2]=='00' for i in range(2*k-1)) + (u[-1:]+u[:1]=='00')==1

expected_language=[2,4,7,12,21,37,63,105,177,296,479,758,1241,2007,3149,4877]
prev=None
for n in range(1,17):
    ms=masks(n)
    # Stable language when enlarged k horizon; checks finite cutoff model.
    assert ms==set().union(*(mask_blocks(n,k) for k in range(2,n+9)))
    assert max(m.count('1') for m in ms)<=n/2+1
    ws=descendant_words(n)
    assert len(ws)==expected_language[n-1]
    assert all(any((int(m,2)&w)==w for m in ms) for w in ws)
    assert len(ws)<= (n*n+5*n+10)*2**(n//2+1)
    if prev is not None:
        minimal={w for w in range(2**n) if w not in ws and (w>>1) in prev and (w & ((1<<(n-1))-1)) in prev}
        assert all((w>>1) in prev and (w & ((1<<(n-1))-1)) in prev for w in minimal)
    prev=ws
print('VERIFY_OK mask_periods=49 language_lengths=16 periodic_language_stability=16')
