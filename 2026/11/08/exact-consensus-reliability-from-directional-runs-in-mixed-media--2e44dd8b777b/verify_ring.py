"""Standalone exhaustive finite checks for directional weighted-median ring theorem."""
from itertools import product
from fractions import Fraction
from math import comb


def cohesive(mask, types, n, tied=False):
    for i, mode in enumerate(types):
        if not (mask & (1 << i)):
            continue
        left = bool(mask & (1 << ((i-1) % n)))
        right = bool(mask & (1 << ((i+1) % n)))
        if mode == 'A' and not (left and right):
            return False
        if mode == 'R' and not right:
            return False
        if mode == 'L' and not left:
            return False
        if mode == 'T' and not (left or right):
            return False
    return True


def direct_consensus(types):
    n = len(types)
    good = [s for s in range(1, 1 << n) if cohesive(s, types, n)]
    for s in good:
        for t in good:
            if not (s & t):
                return False
    return True


def predicted(types):
    medians = [mode for mode in types if mode != 'A']
    if not medians:
        return True
    transitions = sum(x == 'R' and medians[(i+1) % len(medians)] == 'L'
                      for i, x in enumerate(medians))
    return transitions <= 1


def probability(n, a, r, l):
    assert a + r + l == 1
    if r == l:
        return 2*(a+r)**n - a**n + n*(n-1)*r*r*(a+r)**(n-2)
    return (a+r)**n + (a+l)**n - a**n + n*r*l*((a+r)**(n-1)-(a+l)**(n-1))/(r-l)



def closed_class_count(types):
    """Independently count closed communicating classes of the linear response graph."""
    n = len(types)
    adj = []
    for i, mode in enumerate(types):
        if mode == 'A':
            adj.append({(i-1)%n, (i+1)%n})
        elif mode == 'R':
            adj.append({(i+1)%n})
        elif mode == 'L':
            adj.append({(i-1)%n})
        else:
            raise ValueError(mode)
    reach=[]
    for i in range(n):
        seen={i}; stack=[i]
        while stack:
            for j in adj[stack.pop()]:
                if j not in seen:
                    seen.add(j); stack.append(j)
        reach.append(seen)
    remaining=set(range(n)); sinks=0
    while remaining:
        i=next(iter(remaining)); component={j for j in remaining if i in reach[j] and j in reach[i]}
        if all(adj[j]<=component for j in component):
            sinks+=1
        remaining-=component
    return sinks


def predicted_classes(types):
    medians=[mode for mode in types if mode!='A']
    if not medians:
        return 1
    transitions=sum(x=='R' and medians[(i+1)%len(medians)]=='L'
                    for i,x in enumerate(medians))
    return max(1, transitions)


def exact_distribution(n,a,r,l):
    """Probability mass function of number of R-to-L switches, with exact Fractions."""
    out=[(a+r)**n+(a+l)**n-a**n]
    for j in range(1,n//2+1):
        s=Fraction(0)
        for k in range(2*j,n+1):
            for t in range(j,k-j+1):
                s+=comb(n,k)*a**(n-k)*Fraction(k,j)*comb(t-1,j-1)*comb(k-t-1,j-1)*r**t*l**(k-t)
        out.append(s)
    assert sum(out)==1
    return out

if __name__ == '__main__':
    total = 0
    for n in range(3, 9):
        good_count = 0
        weighted_count = 0
        for modes in product('ARL', repeat=n):
            exact = direct_consensus(modes)
            assert exact == predicted(modes), (n, modes, exact)
            assert closed_class_count(modes)==predicted_classes(modes),(n,modes)
            good_count += exact
            weighted_count += exact * (2 ** modes.count('A')) * (3 ** modes.count('R')) * (5 ** modes.count('L'))
        assert Fraction(good_count, 3**n) == probability(n, Fraction(1,3),Fraction(1,3),Fraction(1,3))
        assert Fraction(weighted_count, 10**n) == probability(n,Fraction(1,5),Fraction(3,10),Fraction(1,2))
        for weights in ((Fraction(1,3),Fraction(1,3),Fraction(1,3)),(Fraction(1,5),Fraction(3,10),Fraction(1,2))):
            hist=[0]*(n//2+1)
            for modes in product('ARL',repeat=n):
                sub=[m for m in modes if m!='A']
                j=sum(m=='R' and sub[(i+1)%len(sub)]=='L' for i,m in enumerate(sub)) if sub else 0
                hist[j]+=weights[0]**modes.count('A')*weights[1]**modes.count('R')*weights[2]**modes.count('L')
            assert hist==exact_distribution(n,*weights),(n,weights,hist)
        print('strict', n, 'configurations', 3**n, 'consensus', good_count)
        total += 3**n
    for n in range(3, 10):
        for modes in product('AT', repeat=n):
            exact = direct_consensus(modes)
            assert exact == (modes.count('T') <= 3), (n, modes, exact)
        print('tied', n, 'configurations', 2**n)
        total += 2**n
    print('ALL CHECKS PASSED', total, 'exact network-type configurations')
