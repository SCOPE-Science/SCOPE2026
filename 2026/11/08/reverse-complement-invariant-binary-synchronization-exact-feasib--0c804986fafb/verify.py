"""Direct finite checks for binary reverse-complement-invariant non-overlapping codes.
The all-length results are proved in RESULT.md, not inferred from this bounded script.
"""
from itertools import product
from math import ceil, log2

def rc(w):
    return ''.join('1' if c == '0' else '0' for c in reversed(w))

def conflict(u, v):
    return any(u[:t] == v[-t:] or v[:t] == u[-t:] for t in range(1, len(u)))

def legal_orbit(w):
    orb = {w, rc(w)}
    return all(not conflict(u, v) for u in orb for v in orb)

def criterion(w):
    return (all(w[:t] != w[-t:] for t in range(1,len(w)))
            and all(w[:t] != rc(w[:t]) for t in range(1,len(w)))
            and all(w[-t:] != rc(w[-t:]) for t in range(1,len(w))))

def families(n):
    # All nonempty codes must use one of two endpoint orientations.
    if n == 1:
        return [frozenset({'0','1'})]
    ws = ['0'+''.join(mid)+'1' for mid in product('01', repeat=n-2)]
    return sorted({tuple(sorted({w, rc(w)})) for w in ws
                   if legal_orbit(w)})

# Match independent orbit testing with the border/antipalindrome criterion.
for n in range(2, 15):
    for w in map(''.join, product('01',repeat=n)):
        assert legal_orbit(w) == criterion(w), (n,w)

expected={1:1,2:1,3:0,4:1,5:0,6:2,7:0,8:4,9:2}
for n, number in expected.items():
    got=len(families(n))
    assert got == number,(n,got,number)

for n in range(8,81):
    w='0'*(n-5)+'11011'
    assert legal_orbit(w),(n,w)
for n,w in [(2,'01'),(4,'0011'),(6,'000111')]:
    assert legal_orbit(w)

# Full bounded guard-family enumeration, coupled with a direct certificate for
# the claim that 0^k occurs only in the prefix and that RC maps the set to itself.
for n in (14,16,20,24,28,32):
    k=ceil(log2(4*n)); length=n-2*k-2
    if length<0:continue
    valid=[]
    for bits in product('01', repeat=length):
        u=''.join(bits)
        if '0'*k in u or '1'*k in u:continue
        if u.startswith('1'*(k-1)) or u.endswith('0'*(k-1)):continue
        w='0'*k+'1'+u+'0'+'1'*k
        valid.append(w)
        assert w.count('0'*k) == 1 and w.startswith('0'*k)
        assert legal_orbit(w)
    assert len(valid)>= 2**(length-1), (n,k,len(valid),length)
    got=set(valid)
    assert all(rc(w) in got for w in valid)
    if len(got)<=1024:
        assert all(not conflict(w,v) for w in got for v in got)
    print('guard_family',n,'k',k,'count',len(valid),'lower_bound',2**(length-1))
print('DIRECT_ALL_CHECKS_OK')
