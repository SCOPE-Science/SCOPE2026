"""Independent labelled-state test for synchronous tie-retaining majority.

The graph is K_{a,b} with an edge added between vertices 0 and 1
in the a-vertex shore. No formulas are used in the dynamics code.
"""
from itertools import product
from math import comb


def formulas(a, b):
    if a % 2:
        return (2, 1)
    if b % 2:
        return (2 + 2*comb(b,(b-1)//2) if a == 4 else 2, 1)
    t = comb(a-2, a//2-1)*comb(b,b//2)
    h = 2+(comb(a-2,a//2)+comb(a-2,a//2-2))*comb(b,b//2)
    return h, 1+t


def count(a,b):
    n=a+b
    neighbors = [list(range(a,n)) for _ in range(a)] + [list(range(a)) for _ in range(b)]
    neighbors[0].append(1)
    neighbors[1].append(0)
    def update(x):
        y=0
        for i, nb in enumerate(neighbors):
            ones=sum((x>>j)&1 for j in nb)
            if ones*2>len(nb) or (ones*2==len(nb) and ((x>>i)&1)):
                y|=1<<i
        return y
    h=p=0
    for x in range(1<<n):
        y=update(x);z=update(y)
        if z==x:
            if y==x: h+=1
            else:p+=1
    assert p%2==0
    return h,p//2

if __name__=='__main__':
    total=0;cases=0
    for a in range(3,10):
        for b in range(3,11):
            if a+b>17:continue
            got=count(a,b);want=formulas(a,b)
            assert got==want, (a,b,got,want)
            cases+=1;total+=1<<(a+b)
    print(f'PASS direct labelled-state check: {cases} graphs, {total} configurations')
    for a,b in [(3,3),(4,3),(4,4),(4,5),(4,6),(6,4),(6,6),(8,8)]:
        print(f'({a},{b}) fixed={count(a,b)[0]} primitive_two_cycles={count(a,b)[1]}')
