#!/usr/bin/env python3
"""Independent finite checks of exact circular scattered-subsequence universality orbit formulas."""
import itertools, math
from collections import Counter

def divs(n):
    return [e for e in range(1,n+1) if n%e==0]

def phi(n):
    return sum(math.gcd(j,n)==1 for j in range(1,n+1))

def mobius(n):
    p=0
    for d in range(2,math.isqrt(n)+1):
        if n%d==0:
            n//=d; p+=1
            if n%d==0:return 0
            while n%d==0:n//=d
    if n>1:p+=1
    return -1 if p%2 else 1

def theoretical_P(q,k):
    ans=0
    for mask in range(1,1<<q):
        ts=[i for i in range(q) if mask>>i&1]
        gs=[(ts[(i+1)%len(ts)]-ts[i])%q or q for i in range(len(ts))]
        val=math.factorial(q)
        for g in gs:val*=math.factorial(g)**(k-1)
        ans+=(-1)**(len(ts)+1)*val
    return ans

def compositions(n,t):
    if t==1:
        yield (n,)
    else:
        for first in range(1,n-t+2):
            for rest in compositions(n-first,t-1):
                yield (first,)+rest

def theoretical_P_compositions(q,k):
    # The cyclic root-factor q/t must divide the total at each t, not each composition.
    total=0
    for t in range(1,q+1):
        subtot=sum(math.prod(math.factorial(g)**(k-1) for g in c)
                    for c in compositions(q,t))
        assert (q*subtot)%t==0
        total+=(-1)**(t+1)*q*subtot//t
    return math.factorial(q)*total

def theoretical_N(q,k):
    s=sum(phi(k//e)*theoretical_P(q,e) for e in divs(k))
    assert s%(q*k)==0
    return s//(q*k)

def theoretical_R(q,k):
    s=sum(mobius(k//e)*theoretical_P(q,e) for e in divs(k))
    assert s%(q*k)==0
    return s//(q*k)

def rotations(w):
    return tuple(w[i:]+w[:i] for i in range(len(w)))

def canonical(w):
    return min(rotations(w))

def is_universal(w,k,q):
    # Independent dynamic-programming subsequence checker, not the permutation-block property.
    for pattern in itertools.product(range(q),repeat=k):
        pos=0
        for c in w:
            if pos<k and c==pattern[pos]:pos+=1
        if pos<k:return False
    return True

def direct_S(q,k):
    n=q*k
    perms=list(itertools.permutations(range(q)))
    all_words=set()
    for blocks in itertools.product(perms,repeat=k):
        w=tuple(itertools.chain.from_iterable(blocks))
        for rot in rotations(w):all_words.add(rot)
    return all_words

cases=0; inspected=0
for q,kmax in [(2,9),(3,5),(4,3),(5,2)]:
    for k in range(1,kmax+1):
        S=direct_S(q,k)
        P=theoretical_P(q,k)
        assert P==theoretical_P_compositions(q,k)
        assert len(S)==P,(q,k,len(S),P)
        necklaces={canonical(w) for w in S}
        assert len(necklaces)==theoretical_N(q,k)
        primitive={w for w in necklaces if all((w!=w[i:]+w[:i]) for i in range(1,len(w)))}
        assert len(primitive)==theoretical_R(q,k)
        cases+=1; inspected+=len(S)
        if q<=3 and k<=3 or q==4 and k<=2:
            # Directly check scattered-subsequence definition against formula for *all* words.
            for w in itertools.product(range(q),repeat=q*k):
                flag=any(is_universal(x,k,q) for x in rotations(w))
                assert flag==(w in S),(q,k,w)
        if q==2:
            binaryneck=sum(phi(k//e)*2**e for e in divs(k))//k
            assert len(necklaces)==binaryneck-1
        print('OK',q,k,'marked',len(S),'necklaces',len(necklaces),'primitive',len(primitive))
for q in range(2,9):
    for k in range(1,6):
        assert theoretical_P(q,k)==theoretical_P_compositions(q,k)
print(f'VERIFY_OK orbit_cases={cases} marked_word_memberships={inspected} formula_identities=35 direct_subsequence_crosschecks=q2_k1to3_q3_k1to3_q4_k1to2 PASS')
