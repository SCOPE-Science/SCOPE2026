#!/usr/bin/env python3
"""Direct truncated-algebra verification, independent of the cylindrical graph matrix."""

def rank(vectors):
    echelon = {}
    for v in vectors:
        while v:
            k = (v & -v).bit_length()-1
            if k in echelon:v ^= echelon[k]
            else:echelon[k] = v;break
    return len(echelon)

def multiply_u(poly,m,k):
    y = 0
    while poly:
        bit=poly&-poly
        idx=bit.bit_length()-1
        t,w=divmod(idx,k)
        if t+1<m:y ^= 1 << ((t+1)*k+w)
        if w+1<k:y ^= 1 << (t*k+w+1)
        poly ^= bit
    return y

def check(q,k):
    m=q-1
    power=[1 << i for i in range(m*k)]
    if k<q:blocks=[q]*(k-1)+[q-k]
    else:blocks=[k]*(q-1)
    for t in range(max(blocks)+2):
        nul=m*k-rank(power)
        exp=sum(min(t,b) for b in blocks)
        assert nul==exp,(q,k,t,nul,exp)
        power=[multiply_u(v,m,k) for v in power]
    return max(blocks)+2

if __name__=='__main__':
    tests=0;checks=0
    for q in (4,8,16,32):
        for k in (1,2,4,8,16,32):
            if (q-1)*k>600:continue
            checks+=check(q,k);tests+=1
    print('PASS: %d truncated-algebra examples; %d exact rank comparisons' % (tests,checks))
