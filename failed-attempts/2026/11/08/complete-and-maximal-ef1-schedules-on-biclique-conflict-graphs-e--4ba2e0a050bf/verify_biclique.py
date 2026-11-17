"""Independent exhaustive checks for unit-cost conflict allocations on bicliques.

Run: python verify_biclique.py
Requires only Python 3 standard library. A check enumerates every assignment of
labeled items to a labeled agent or to the unallocated category, rather than
assuming an equilibrium or a structural classification.
"""
from itertools import product
from math import factorial, comb


def formula(a, b, n):
    """Complete count, maximal-incomplete count and maximum assigned jobs."""
    m = a+b
    q, r = divmod(m, n)
    complete = 0
    if q == 0:
        complete = factorial(n)//factorial(n-m)
    else:
        for s in range(1, n):
            ra = a-s*q
            rb = b-(n-s)*q
            if not (0 <= ra <= s and 0 <= rb <= n-s and ra+rb == r):
                continue
            d = (factorial(q)**(n-r)) * (factorial(q+1)**r)
            complete += comb(n,s)*comb(s,ra)*comb(n-s,rb)*factorial(a)*factorial(b)//d
    incomplete = 0
    for z in (a,b):
        if z >= n:
            t,h=divmod(z,n)
            incomplete += comb(n,h)*factorial(z)//((factorial(t)**(n-h))*(factorial(t+1)**h))
    best = m if complete else max(a,b)
    return complete, incomplete, best


def direct(a, b, n):
    """Check actual graph conflicts, unit EF1, and inclusion maximality."""
    m=a+b
    total_complete=total_incomplete=0
    best=0
    for assignment in product(range(-1,n), repeat=m):
        countA=[0]*n
        countB=[0]*n
        unA=unB=0
        for j, agent in enumerate(assignment):
            if agent == -1:
                if j < a: unA+=1
                else: unB+=1
            elif j < a:
                countA[agent]+=1
            else:
                countB[agent]+=1
        if any(x and y for x,y in zip(countA,countB)):
            continue
        load=[x+y for x,y in zip(countA,countB)]
        if max(load)-min(load)>1:
            continue
        if unA and not all(countB):
            continue
        if unB and not all(countA):
            continue
        if unA or unB:
            total_incomplete+=1
        else:
            total_complete+=1
        best=max(best,sum(load))
    return total_complete,total_incomplete,best


def run():
    cases = assignments = 0
    for n in (2,3,4):
        for a in range(1,6):
            for b in range(1,6):
                if a+b>8 or (n==4 and a+b>7):
                    continue
                predicted=formula(a,b,n)
                actual=direct(a,b,n)
                assert actual==predicted, (a,b,n,predicted,actual)
                cases+=1
                assignments+=(n+1)**(a+b)
    assert formula(4,5,3)==(0,126,5)
    assert formula(5,7,4)==(0,2760,7)
    # Infinite parametric boundary: K_(2h-1,2h+1), four agents.
    for h in range(3,70):
        complete,_,best=formula(2*h-1,2*h+1,4)
        assert complete==0 and best==2*h+1
    print(f'PASS {cases} complete parameter cells; {assignments} entire labeled assignments checked')
    print('PASS both 3-agent and 4-agent arithmetic-gap examples')
    print('PASS 67 further arithmetic-family instances')

if __name__=='__main__':
    run()
