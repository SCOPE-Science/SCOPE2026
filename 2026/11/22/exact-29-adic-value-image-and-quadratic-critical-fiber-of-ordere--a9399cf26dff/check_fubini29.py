"""Independent exact modular checks for the ordered-Bell 29-adic image theorem."""
from collections import Counter
from math import factorial
P=29
REGULAR = {0:1,1:3,3:1,9:2,10:2,13:1,14:3,15:1,17:1,18:1,19:3,20:1,22:1,23:2,25:2,26:2}
B = [21,3,15,18,4,22,12,19,12,14,3,19,23,11,4,28,23,2,0,6,11,25,20,11,6,6,12,13]
C = [1,24,16,21,19,18,1,6,8,26,24,15,22,7,5,28,4,18,9,10,26,5,8,23,20,21,0,5]
RESIDUES = [0,1,3,13,17,19,14,23,26,9,1,10,19,15,22,14,26,19,24,9,10,25,23,20,25,18,14,1]

def fubini_mod(limit,mod):
    M=1
    while factorial(M)%mod: M+=1
    fac=[factorial(j)%mod for j in range(M+1)]
    s=[0]*(M+1);s[0]=1
    out=[]
    for n in range(limit):
        out.append(sum(s[j]*fac[j] for j in range(M+1))%mod)
        s=[0]+[(s[j-1]+j*s[j])%mod for j in range(1,M+1)]
    return out

mod=P**3
v=fubini_mod(225,mod)
for a in range(28):
    A,D,E=v[140+a],v[168+a],v[196+a]
    assert A%P==RESIDUES[a]
    assert ((D-A)%mod)//P%P == B[a]
    assert ((E-2*D+A)%mod)//(P*P)%P==C[a]
assert sorted(a for a in range(28) if B[a]==0)==[18]
assert Counter(RESIDUES[a] for a in range(28) if a!=18)==Counter(REGULAR)
assert sum(REGULAR.values())==27
assert v[158]%(P*P)==488
# Critical normal form modulo p^3 and its unique derivative-zero input
A=v[158]
assert (A+P*P*(4*21+9*21*20//2))%mod == 20672
assert (9*pow(2,-1,P))%P==19

def sq_residues(m):
    return {i*i%m for i in range(m)}

for k in [1,2,3]:
    q=P**k; per=28*P**(k-1)
    z=fubini_mod(per+35,q)
    c=Counter(z[35:35+per])
    # The sufficient late-bound n>=k and per exact shift should not be assumed for all n,
    # but the proposed period is checked directly against an independent 35-index tail.
    assert z[29:35]==z[29+per:35+per]
    if k==1:
        assert len(c)==17
        assert set(c)==set(REGULAR)|{24}
    if k>=2:
        allowed={x for x in range(q) if x%P in REGULAR}
        critical={ (20672+P*P*19*s)%q for s in sq_residues(P**max(k-2,0)) }
        # delta modulo 29^3 known, so can evaluate critical model only up to k=3
        assert set(c)==allowed|critical
        for x in allowed:
            assert c[x]==REGULAR[x%P]
        assert len(c)==16*P**(k-1)+len(critical)
    print('k=',k,'period=',per,'image=',len(c),'max-fiber=',max(c.values()))
print('verified 28 branches / 3 levels / singular normal form')
