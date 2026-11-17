"""Reproduce exact fixed-population equilibrium and welfare formulae for two-color Schelling rings.

Scientific calculation only. No external dependencies. Python >= 3.9.
"""
from itertools import combinations
from math import comb, ceil
from fractions import Fraction


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def predicted_count(b, r):
    n = b+r
    def one_short(x, y):
        return sum((Fraction(n, k)*choose(k, x-k)*choose(y-1,k-1)
                    for k in range(1, min(x,y)+1)), Fraction())
    intersection = sum((Fraction(n,k)*choose(k,b-k)*choose(k,r-k)
                        for k in range(1,min(b,r)+1)), Fraction())
    answer = one_short(b,r)+one_short(r,b)-intersection
    assert answer.denominator == 1
    return int(answer)


def utility(colors, i):
    n = len(colors)
    # The triangular, peak-one-half utility is p(1/3)=p(2/3)=2/3 and p(1)=0.
    # Multiply by 3 to use exact integers.
    same = 1 + (colors[(i-1)%n] == colors[i]) + (colors[(i+1)%n] == colors[i])
    return 0 if same == 3 else 2


def direct_equilibrium(colors):
    n=len(colors)
    for i in range(n):
        for j in range(i+1,n):
            if colors[i] == colors[j]:
                continue
            vi, vj = utility(colors,i),utility(colors,j)
            modified=list(colors)
            modified[i],modified[j]=modified[j],modified[i]
            # Track the moving agents, now in the other positions.
            if utility(modified,j)>vi and utility(modified,i)>vj:
                return False
    return True


def monochrome_triple(colors, typ):
    n=len(colors)
    return any(colors[i]==colors[(i-1)%n]==colors[(i+1)%n]==typ for i in range(n))


def verify(max_n=15):
    instances = profiles = equilibria = 0
    for n in range(3,max_n+1):
        for b in range(1,n//2+1):
            r=n-b
            count=0
            bottom=n+1
            top=0
            for spots in combinations(range(n),b):
                colors=[0]*n
                for index in spots: colors[index]=1
                profiles+=1
                actual=direct_equilibrium(colors)
                criterion = not(monochrome_triple(colors,0) and monochrome_triple(colors,1))
                assert actual == criterion, ('criterion', n, b, spots)
                welfare=sum(utility(colors,i)>0 for i in range(n))
                top=max(top,welfare)
                if actual:
                    equilibria+=1
                    count+=1
                    bottom=min(bottom,welfare)
            assert count == predicted_count(b,r), ('census',n,b,count,predicted_count(b,r))
            assert top == min(n,3*b), ('maximum welfare',n,b,top)
            assert bottom == b+min(r,ceil(b/2)+1), ('minimum stable welfare',n,b,bottom)
            instances += 1
    print(f'PASS: {instances} population instances, {profiles} distinct fixed-count cyclic color profiles, {equilibria} equilibria.')
    print(f'Exact swap condition, stable census, minimum and maximum degree of integration verified through n={max_n}.')

if __name__ == '__main__':
    verify()
