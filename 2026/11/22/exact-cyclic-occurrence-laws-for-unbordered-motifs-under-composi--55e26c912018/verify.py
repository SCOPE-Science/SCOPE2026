"""Independent finite tests of exact circular unbordered-motif occurrence laws.
Public code uses plain exhaustive enumeration, not the proof's graph reduction.
"""
from itertools import product, combinations
from collections import Counter
from fractions import Fraction
from math import factorial, comb

def is_unbordered(u):
    m=len(u)
    return all(u[:r]!=u[m-r:] for r in range(1,m))

def A(n,m,j):
    if j==0: return 1
    if j>n//m:return 0
    h=n-(m-1)*j
    return n*comb(h,j)//h

def multi(K):
    if min(K)<0: return 0
    n=sum(K)
    d=1
    for k in K:d*=factorial(k)
    return factorial(n)//d

def cyclic_occ(w,u):
    n=len(w);m=len(u)
    return sum(all(w[(i+j)%n]==u[j] for j in range(m)) for i in range(n))

def predicted_by_composition(K,c,m):
    n=sum(K)
    rmax=n//m
    out=[0]*(rmax+1)
    for j in range(rmax+1):
        N=A(n,m,j)*multi([K[i]-j*c[i] for i in range(len(K))])
        for r in range(j+1):
            out[r]+=(-1)**(j-r)*comb(j,r)*N
    return tuple(out)

def predicted_iid(n,m,pi):
    out=[Fraction(0)]*(n//m+1)
    for j in range(n//m+1):
        v=A(n,m,j)*pi**j
        for r in range(j+1): out[r]+=(-1)**(j-r)*comb(j,r)*v
    return tuple(out)

cases_fixed=0;cases_iid=0;placement_tests=0
for alphabet_size in (2,3):
    alphabet=tuple(range(alphabet_size))
    max_len=10 if alphabet_size==2 else 8
    probs=(Fraction(2,5),Fraction(3,5)) if alphabet_size==2 else (Fraction(1,2),Fraction(1,3),Fraction(1,6))
    for m in range(2,6):
        motifs=[u for u in product(alphabet,repeat=m) if is_unbordered(u)]
        for n in range(1,max_len+1):
            if alphabet_size**n>20000:continue
            brute_by_u=[Counter() for _ in motifs]
            brute_iid=[ [Fraction(0)]*(n//m+1) for _ in motifs]
            for word in product(alphabet,repeat=n):
                K=tuple(word.count(a) for a in alphabet)
                weight=Fraction(1)
                for a in word:weight*=probs[a]
                for h,u in enumerate(motifs):
                    r=cyclic_occ(word,u)
                    brute_by_u[h][K,r]+=1
                    brute_iid[h][r]+=weight
            for h,u in enumerate(motifs):
                c=tuple(u.count(a) for a in alphabet)
                for K in product(range(n+1),repeat=alphabet_size):
                    if sum(K)!=n:continue
                    predicted=predicted_by_composition(K,c,m)
                    observed=tuple(brute_by_u[h][K,r] for r in range(n//m+1))
                    assert predicted==observed,(u,n,K,predicted,observed)
                    cases_fixed+=1
                pi=Fraction(1)
                for a in u:pi*=probs[a]
                predicted=predicted_iid(n,m,pi)
                observed=tuple(brute_iid[h])
                assert predicted==observed,(u,n,predicted,observed)
                cases_iid+=1
for m in range(2,7):
    for n in range(m,min(19,3*m+5)):
        for j in range(n//m+1):
            if comb(n,j)>400000:continue
            val=0
            for starts in combinations(range(n),j):
                occupied=[{(s+h)%n for h in range(m)} for s in starts]
                val+=int(all(not occupied[a]&occupied[b] for a in range(j) for b in range(a+1,j)))
            assert val==A(n,m,j),(n,m,j,val,A(n,m,j))
            placement_tests+=1
print('PASS fixed-composition exact distribution:',cases_fixed,'cases against exhaustive circles')
print('PASS iid distribution under biased law:',cases_iid,'cases against exhaustive circles')
print('PASS cyclic placement counts:',placement_tests,'cases against independent subset enumeration')
print('PASS boundary example: binary n=4, 001 vs 010:')
for u in ((0,0,1),(0,1,0)):
 counts=Counter(cyclic_occ(w,u) for w in product((0,1),repeat=4))
 print(' ',''.join(map(str,u)),sorted(counts.items()))
