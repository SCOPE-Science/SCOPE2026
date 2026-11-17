#!/usr/bin/env python3
"""Standalone exact algebraic identity and independent subsequence checks."""
import json,itertools,sys
from pathlib import Path


def add(a,b):
    c=[0]*max(len(a),len(b))
    for i,v in enumerate(a):c[i]+=v
    for i,v in enumerate(b):c[i]+=v
    while len(c)>1 and c[-1]==0:c.pop()
    return c

def neg(a):return [-i for i in a]
def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        for j,w in enumerate(b):c[i+j]+=v*w
    while len(c)>1 and c[-1]==0:c.pop()
    return c

def drop(a):
    while len(a)>1 and a[-1]==0:a.pop()
    return a

def test_certificate(cert):
    q=cert['q'];assert q==4
    pairs=[tuple(p) for p in cert['pairs']]
    assert pairs==[(i,j) for i in range(q) for j in range(q)]
    H=cert['H'];D=cert['denominator'];N=cert['numerator']; assert D[0]==1
    assert len(H)==q*q
    for idx,(a,b) in enumerate(pairs):
        rhs=[D[i]*(a>=b) for i in range(len(D))]
        lhs=list(H[idx]);
        for c in range(q):
            if int(a>=b)+int(b>=c)-int(a>=c)==1:
                term=mul([0,1] if b>=c else [1],H[pairs.index((b,c))])
                lhs=add(lhs,neg(term))
        assert drop(lhs)==drop(rhs),('matrix identity',idx)
    total=[0]
    for idx,(a,b) in enumerate(pairs):
        if a>=b:total=add(total,mul([0,1],H[idx]))
    assert drop(total)==drop(N),'numerator identity'

def local_counts(q,k):
    # Dynamic count by (last two letters, number of weak descents, length)
    counts={}
    state={(a,b,int(a>=b),2):1 for a in range(q) for b in range(q) if a>=b}
    # initial pairs are unique
    for ell in range(2,2*k+1):
        for (a,b,d,l),v in state.items():
            if l==ell and d==k and a>=b:counts[ell]=counts.get(ell,0)+v
        new={}
        for (a,b,d,l),v in state.items():
            for c in range(q):
                if int(a>=b)+int(b>=c)-int(a>=c)==1 and d+int(b>=c)<=k:
                    key=(b,c,d+int(b>=c),l+1)
                    new[key]=new.get(key,0)+v
        state=new
    return counts

def is_subseq(v,w):
    pos=0
    for c in v:
        while pos<len(w) and w[pos]!=c:pos+=1
        if pos==len(w):return False
        pos+=1
    return True

def brute_counts(q,k):
    w=tuple(range(q))*k
    out={}
    for n in range(2,2*k+1):
        tally=0
        for v in itertools.product(range(q),repeat=n):
            if is_subseq(v,w):continue
            if all(is_subseq(v[:i]+v[i+1:],w) for i in range(n)):
                tally+=1
        if tally:out[n]=tally
    return out

def recurrence(D,N,terms=45):
    a=[0]*(terms+1)
    for k in range(terms+1):
        a[k]= (N[k] if k<len(N) else 0)-sum(D[j]*a[k-j] for j in range(1,min(k,len(D)-1)+1))
    return a

def main():
    cert=json.loads(Path(sys.argv[1] if len(sys.argv)>1 else 'certificate.json').read_text())
    test_certificate(cert)
    seq=recurrence(cert['denominator'],cert['numerator'])
    known=[10,40,165,653,2585,10201,40289,159196,629004,2485317,9819749,38798730]
    assert seq[1:len(known)+1]==known
    for q,k in [(2,1),(2,2),(2,3),(2,4),(2,5),(3,1),(3,2),(3,3),(3,4),(4,1),(4,2),(4,3),(4,4),(5,1),(5,2)]:
        local=local_counts(q,k)
        brute=brute_counts(q,k)
        assert local==brute,(q,k,local,brute)
        if q==4:assert sum(local.values())==seq[k],(k,local,seq[k])
    print('PASS exact polynomial transfer identity; 15 exhaustive word configurations; 45 recurrence coefficients')
if __name__=='__main__':main()
