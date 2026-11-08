#!/usr/bin/env python3
"""Independent finite checks for distinct square-subsequence spectrum.
Only uses Python's standard library. Not a proof of the all-parameter theorem.
"""
from math import comb
from collections import defaultdict
from itertools import combinations, product


def gf_coefficients(q, kmax, mmax):
    """Compute [t^k z^m] of the claimed rational generating function.

    Uses the coefficient recurrence for (1-t^2 B^q)F =
    z t^2 (sum_{j=0}^{q-1} B^j + q t B^(q-1)), B=1+(1-t^2)z.
    """
    a = defaultdict(int)
    for k in range(1, kmax+1):
        for m in range(1, mmax+1):
            c=0
            r=m-1
            if r<=q-1:
                for h in range(r+1):
                    sgn=(-1)**h * comb(r,h)
                    if k==2+2*h:
                        c+=sgn*sum(comb(j,r) for j in range(r,q))
                    if k==3+2*h:
                        c+=sgn*q*comb(q-1,r)
            for d in range(min(q,m)+1):
                for h in range(d+1):
                    k0=k-2-2*h
                    if k0>=1:
                        c+=comb(q,d)*comb(d,h)*(-1)**h*a[k0,m-d]
            a[k,m]=c
    return a


def actual_subsequences(word):
    """Position-wise enumeration, not a greedy-period computation."""
    found={''}
    for c in word:
        found |= {v+c for v in tuple(found)}
    return found


def square_roots(word):
    sub=actual_subsequences(word)
    return {v[:len(v)//2] for v in sub if v and len(v)%2==0 and v[:len(v)//2]==v[len(v)//2:]}


def greedy_contains(word, v):
    pos=0
    for x in v:
        while pos<len(word) and word[pos]!=x:
            pos+=1
        if pos==len(word):
            return False
        pos+=1
    return True


def check():
    tested_profiles=0
    tested_coeffs=0
    tested_embeds=0
    for q in range(2,6):
        K=6 if q<=3 else 4 if q==4 else 3
        a=gf_coefficients(q,K,q*K//2)
        for k in range(1,K+1):
            word=''.join(str(i) for i in range(q))*k
            actual=square_roots(word)
            bylen=defaultdict(int)
            for v in actual:bylen[len(v)]+=1
            for m in range(1,q*k//2+1):
                assert a[k,m]==bylen[m],(q,k,m,a[k,m],bylen[m])
                tested_coeffs+=1
            if k==1:
                assert not actual
            elif k%2==0:
                t=k//2
                maximal={v for v in actual if len(v)==q*t}
                assert maximal=={''.join(str(i) for i in range(q))*t}
            else:
                t=(k-1)//2
                target=''.join(str(i) for i in range(q))*t
                maxima={v for v in actual if len(v)==q*t}
                assert maxima=={(target+target)[j:j+len(target)] for j in range(q)}
            # Distinct second method: test actual embedding against descent criterion.
            if q*k<=16:
                for m in range(1,min(q*k//2,5)+1):
                    for tpl in product(range(q),repeat=m):
                        v=''.join(str(i) for i in tpl)
                        d=sum(tpl[j]>=tpl[j+1] for j in range(m-1))
                        beta=tpl[-1]>=tpl[0]
                        predicted=2*d+int(beta)+1<=k
                        actual_embed=greedy_contains(word,v+v)
                        assert predicted==actual_embed,(q,k,v,predicted,actual_embed)
                        tested_embeds+=1
            tested_profiles+=1
    print('PASS: %d complete position-enumerated (q,k) profiles; %d rational coefficients; %d independent greedy/descents decisions.'%(tested_profiles,tested_coeffs,tested_embeds))
    print('Examples: q=3, k=4 ->', [gf_coefficients(3,4,6)[4,m] for m in range(1,7)])
    print('          q=4, k=3 ->', [gf_coefficients(4,3,4)[3,m] for m in range(1,5)])

if __name__=='__main__':check()
