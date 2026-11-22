"""Reproduce exact additive energy of the base-five Franel nondivisibility support.
This program is a finite sanity checker, not a substitute for the infinite proof.
"""
from collections import Counter
from math import comb
D = (0, 1, 3, 4)
C = Counter(a+b for a in D for b in D)
carry = (-1, 0, 1)
T = tuple(tuple(sum(C[x]*C[y] for x in C for y in C if x-y+cin == 5*cout)
                for cout in carry) for cin in carry)
assert T == ((17,28,6),(8,36,8),(6,28,17)), T
assert (T[0][0]+T[0][2], T[0][1], T[1][0]+T[1][2], T[1][1]) == (23,28,16,36)
assert 23+36 == 59 and 23*36-28*16 == 380
P=[(1 if i==j else 0) for i in range(3) for j in range(3)]
def mul(A,B):
    return [sum(A[3*i+k]*B[3*k+j] for k in range(3)) for i in range(3) for j in range(3)]
M=[t for row in T for t in row]
energies=[]
for r in range(14):
    energies.append(P[4]); P=mul(P,M)
assert energies[:6]==[1,36,1744,89216,4601024,237558336]
for r in range(12):
    assert energies[r+2] == 59*energies[r+1]-380*energies[r]
for n in range(513):
    # Direct exact binomial sums check the actual Franel support.
    # Exact binomial arithmetic is feasible at this finite test depth.
    actual=sum(comb(n,k)**3 for k in range(n+1))%5
    m=n
    expected=True
    while m:
        if m%5==2:expected=False;break
        m//=5
    assert (actual != 0)==expected, (n,actual,expected)
checks=0
for r in range(6):
    A=[0]
    place=1
    for _ in range(r):
        A=[a+place*d for a in A for d in D]
        place*=5
    assert len(A)==4**r and len(set(A))==4**r
    sum_counts=Counter(a+b for a in A for b in A)
    assert set(sum_counts)==set(range(2*(5**r-1)+1)), (r,len(sum_counts))
    direct=sum(v*v for v in sum_counts.values())
    assert direct==energies[r],(r,direct,energies[r])
    checks+= len(A)*len(A)
print('VERIFY_OK matrix='+str(T)+' exact_pascal_terms=513 energy_levels=6 pair_enumerations='+str(checks)+' E='+str(energies[:8]))
