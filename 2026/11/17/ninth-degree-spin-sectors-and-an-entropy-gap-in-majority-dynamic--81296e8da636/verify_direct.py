"""Independent bitwise exhaustive majority-fixed test on GP(n,k), 5<=n<=10.
Usage: python verify_direct.py. Requires numpy for vectorised exhaustive enumeration.
"""
import numpy as np

# Distinct construction: each vertex has three explicitly indexed neighbors.
def census(n,k):
    # Outer vertices 0,...,n-1; inner vertices n,...,2*n-1.
    nbr=[]
    for i in range(n):nbr.append(((i-1)%n,(i+1)%n,n+i))
    for i in range(n):nbr.append((n+(i-k)%n,n+(i+k)%n,i))
    assert all(len(set(v))==3 for v in nbr)
    total=0
    for start in range(0,1<<(2*n),1<<16):
        a=np.arange(start,min(start+(1<<16),1<<(2*n)),dtype=np.uint32)
        good=np.ones(len(a),dtype=bool)
        for i,adj in enumerate(nbr):
            bit=(a>>i)&1
            equal=((bit==((a>>adj[0])&1)).astype(np.uint8)+
                   (bit==((a>>adj[1])&1)).astype(np.uint8)+
                   (bit==((a>>adj[2])&1)).astype(np.uint8))
            good &= (equal>=2)
        total += int(good.sum())
    return total

p2=[14,14,32,48,76,118]
p1=[14,22,32,48,76,124]
for n in range(5,11):
    got2=census(n,2);got1=census(n,1)
    assert got2==p2[n-5] and got1==p1[n-5],(n,got2,got1)
    print('n',n,'GP(n,2)',got2,'GP(n,1)',got1,'checked',2*(1<<(2*n)),'configurations')
print('DIRECT BITWISE ENUMERATION PASS')
