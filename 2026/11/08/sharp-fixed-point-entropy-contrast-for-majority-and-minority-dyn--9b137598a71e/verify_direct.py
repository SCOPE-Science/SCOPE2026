#!/usr/bin/env python3
"""Independent labelled-state bit simulator for minority/majority fixed states of helms."""
from itertools import product

def simulator(n,minority):
    N=2*n+1
    neighbors=[list(range(1,n+1))]
    for i in range(n):
        neighbors.append([0,1+(i-1)%n,1+(i+1)%n,1+n+i])
    for i in range(n): neighbors.append([i+1])
    fixed=0
    for bits in product((0,1),repeat=N):
        good=True
        for v,neigh in enumerate(neighbors):
            same=sum(bits[u]==bits[v] for u in neigh)
            opposite=len(neigh)-same
            if (opposite<same if minority else same<opposite):
                good=False;break
        fixed+=good
    return fixed

def cyclic_word_count(n,minority):
    total=0
    for w in product((0,1),repeat=n):
        if sum(w)>n//2:continue
        if minority:
            valid=all(not(w[i] and w[(i+1)%n] and w[(i+2)%n]) for i in range(n))
        else:
            valid=all(not(w[(i-1)%n]==0 and w[i]==1 and w[(i+1)%n]==0) for i in range(n))
        if valid:total+=1
    return total*2

configurations=0
for n in range(3,10):
    m=simulator(n,True);a=simulator(n,False)
    em=cyclic_word_count(n,True);ea=cyclic_word_count(n,False)
    assert (m,a)==(em,ea),(n,m,a,em,ea)
    configurations+=2**(2*n+1)
    print('n=%d minority=%d majority=%d full_states=%d' %(n,m,a,2**(2*n+1)))
print('DIRECT EXHAUSTIVE PASS: %d configurations over seven helm sizes (two rules each)' % configurations)
