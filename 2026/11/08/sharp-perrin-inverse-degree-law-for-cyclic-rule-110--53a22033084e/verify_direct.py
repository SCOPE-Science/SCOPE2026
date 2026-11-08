"""Independent direct-bit enumeration of Rule 110 on cyclic rings.

Run: python3 verify_direct.py
No matrix arithmetic, no third-party packages.
"""
from collections import Counter

def next_bits(x,n):
    output=0
    for i in range(n):
        left=(x>>((i-1)%n))&1
        center=(x>>i)&1
        right=(x>>((i+1)%n))&1
        t=left*4+center*2+right
        output|=((110>>t)&1)<<i
    return output

perrin=[3,0,2]
for k in range(3,22):
    perrin.append(perrin[k-2]+perrin[k-3])
for n in range(1,19):
    c=Counter(next_bits(x,n) for x in range(1<<n))
    maximum=max(c.values())
    maximizers={y for y,v in c.items() if v==maximum}
    if n==1: assert (maximum,maximizers)==(2,{0})
    elif n==2: assert (maximum,maximizers)==(2,{0,3})
    elif n==3: assert (maximum,maximizers)==(3,{7})
    elif n==4: assert (maximum,maximizers)==(2,{0,15,7,11,13,14})
    else:
        assert maximum==perrin[n], (n,maximum,perrin[n])
        assert maximizers=={(1<<n)-1}, (n,maximizers)
    assert c.get((1<<n)-1,0)==perrin[n]
    print('length',n,'maximum',maximum,'maximizers',len(maximizers))
print('DIRECT_OK: direct complete enumeration n=1..18')
