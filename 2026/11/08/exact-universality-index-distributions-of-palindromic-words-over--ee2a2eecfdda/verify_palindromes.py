"""Independent exact verifier for palindrome subsequence-universality enumerators."""
from itertools import product
from collections import defaultdict
from math import comb, factorial

def universality_index_by_subsequences(w,q):
    # Independent dynamic programming, no greedy arch factorization.
    # A word is k-universal iff the distinct subsequence set includes q^k words.
    seen={():True}
    for c in w:
        seen.update({s+(c,):True for s in list(seen)})
    k=0
    while sum(len(s)==k+1 for s in seen)==q**(k+1): k+=1
    return k

def greedy(word,q):
    ans=0; full=(1<<q)-1; m=0
    for c in word:
        m |= 1<<c
        if m==full: ans+=1; m=0
    return ans,m

def coeff_a(q,L):
    # length L arch has L-1 letters surjecting onto q-1 symbols and final missing
    return q*sum((-1)**j*comb(q-1,j)*(q-1-j)**(L-1) for j in range(q)) if L>=1 else 0

def coeff_r(q,L):
    # incomplete suffix of length L
    return sum((-1)**(q-1-j)*comb(q,j)*j**L for j in range(q)) if L else 1

def coeff_s(q,L):
    # residual with exactly q-1 distinct letters, central unique missing
    return coeff_a(q,L+1)

def conv(a,b,N):
    return [sum(a[k]*b[n-k] for k in range(n+1)) for n in range(N+1)]

def predicted(q,H):
    a=[coeff_a(q,j) for j in range(H+1)]
    r=[coeff_r(q,j) for j in range(H+1)]
    s=[coeff_s(q,j) for j in range(H+1)]
    # g_k(z) = A(z)^k
    pw=[1]+[0]*H
    E=defaultdict(int);O=defaultdict(int)
    for k in range(H//q+1):
        v=conv(pw,r,H)
        plus=conv(pw,s,H)
        for h in range(H+1):
            E[h,2*k]+=v[h]
            O[h,2*k]+=q*v[h]-plus[h]
            O[h,2*k+1]+=plus[h]
        pw=conv(pw,a,H)
    return E,O

if __name__=='__main__':
    checked=0; independently_checked=0
    for q,H in ((2,11),(3,7),(4,6)):
        E,O=predicted(q,H)
        for h in range(H+1):
            obs_e=defaultdict(int);obs_o=defaultdict(int)
            for v in product(range(q),repeat=h):
                w=v+v[::-1]
                idx=greedy(w,q)[0]
                if h<=3:
                    assert idx==universality_index_by_subsequences(w,q)
                    independently_checked+=1
                obs_e[idx]+=1;checked+=1
                for c in range(q):
                    w=v+(c,)+v[::-1]
                    idx=greedy(w,q)[0]
                    if h<=3:
                        assert idx==universality_index_by_subsequences(w,q)
                        independently_checked+=1
                    obs_o[idx]+=1;checked+=1
            for k in range(2*H+3):
                assert obs_e[k]==E[h,k],('EVEN',q,h,k,obs_e[k],E[h,k])
                assert obs_o[k]==O[h,k],('ODD',q,h,k,obs_o[k],O[h,k])
            assert sum(obs_e.values())==q**h
            assert sum(obs_o.values())==q**(h+1)
            print('q=%d h=%d: even %s odd %s'%(q,h,sorted(obs_e.items()),sorted(obs_o.items())))
    print('PASS:',checked,'palindrome-index evaluations;',independently_checked,'independent direct subsequence-set evaluations')
