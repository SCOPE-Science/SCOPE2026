"""Independent finite checks of the three-Zumkeller conductor theorem.
Only finite checks are performed; the infinite covering is in the proof.
"""
from math import gcd

Z = (6, 12, 20, 28, 40, 54, 80, 945)
W = {6:(6,), 12:(12,2), 20:(20,1), 28:(28,),
     40:(40,5), 54:(54,6), 80:(80,10,2,1), 945:(945,15)}

def divisors(n):
    return [d for d in range(1,n+1) if n%d==0]

def sigma(n):
    return sum(divisors(n))

def is_zumkeller(n):
    ds=divisors(n); s=sum(ds)
    if s%2:return False
    goal=s//2
    reach=1
    for d in ds:
        reach |= reach << d
    return bool((reach>>goal)&1)

for n in Z:
    ds=set(divisors(n))
    assert len(W[n])==len(set(W[n])) and set(W[n])<=ds
    assert 2*sum(W[n])==sigma(n)
    assert is_zumkeller(n)

for n in range(947,984,2):
    assert sigma(n)<2*n,(n,sigma(n))
assert all(not is_zumkeller(n) for n in (8,10,14,18,26,32))
assert not any(a+b==38 for a in (6,12,20,24,28,30) for b in (6,12,20,24,28,30))

smalls=(6,12,20,28,40,54,80)
even={r:min((6+e+v,e,v) for e in smalls for v in (6,12) if (6+e+v)%18==r) for r in range(0,18,2)}
odd={r:min((945+e+v,e,v) for e in smalls for v in (6,12) if (945+e+v)%18==r) for r in range(1,18,2)}
assert max(x[0] for x in even.values())==98
assert max(x[0] for x in odd.values())==1037
assert odd[11][0]==1037

def certificate(n):
    if n%2==0:
        base,e,v=even[n%18]
        if n<base:return None
        return (6,e,n-6-e)
    base,e,v=odd[n%18]
    if n>=base:return (945,e,n-945-e)
    if n==1001:return (945,28,28)
    if n==1019:return (945,20,54)
    return None

for n in range(984,50001):
    c=certificate(n)
    assert c is not None,(n,'missing certificate')
    assert sum(c)==n and all(i>0 for i in c)
    for item in c:
        assert item in Z or item%18 in (6,12), (n,c)
    for item in c:
        if item not in Z:
            assert item%6==0 and item%9!=0
            k=item
            while k%2==0:k//=2
            assert k%3==0 and k%9!=0

# Independently reconstruct the exact finite three-sum indicator, with
# the definition (subset-sum on divisors), not the modular covering rule.
L=1200
z=[n for n in range(1,L+1) if is_zumkeller(n)]
assert [n for n in z if n%2 and n<=983]==[945]
A=0
for n in z:A|=1<<n
B=0
for n in z:B|=A<<n
C=0
for n in z:C|=B<<n
assert not (C>>983)&1
assert all((C>>n)&1 for n in range(984,L+1))
print('VERIFY_OK','fixed_witnesses',len(Z),'mod18_classes',len(even)+len(odd),
      'checked_certificates',50001-984,'direct_values',L)
