"""Exact identities and deterministic finite-case checks for the 2-nearest-neighbor component law.

Run with Python 3, standard library only. The infinite assertions require the mathematical
proof in RESULT.md; the finite checks are evidence for its cut characterization.
"""
from fractions import Fraction as Q
from itertools import permutations
from math import factorial
from random import Random

checks = 0

def check(ok, why):
    global checks
    checks += 1
    if not ok:
        raise AssertionError(why)


def eint(rate, coefficients):
    """Integral of exp(-rate*t)*sum(coefficients[j]*t**j) over t >= 0."""
    return sum((Q(c)*factorial(j)/rate**(j+1) for j,c in enumerate(coefficients)), Q(0))


def poly(a, b):
    c = [Q(0)]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += Q(x)*Q(y)
    return c

p = eint(1,[1])-2*eint(2,[1,1])+eint(3,[1,2,1])
r = [Q(3,4),Q(1,2)]
q3 = eint(3,[0,1])-2*eint(4,[0]+r)+eint(5,[0]+poly(r,r))
s = [Q(11,36),Q(1,6)]
q4 = eint(3,[Q(1,4)])-eint(4,s)+eint(5,poly(s,s))
variance_rate = p*(1-p)+2*(-2*p*p + (q3-p*p) + (q4-p*p))
check(p==Q(7,54),'p integration')
check(q3==Q(2071,90000),'lag3 integration')
check(q4==Q(6389,324000),'lag4 integration')
check(variance_rate==Q(5747,90000),'variance integration')
check(variance_rate>0,'non-degenerate CLT')
check(variance_rate/p==Q(17241,35000),'Fano ratio')

def predicted(n):
    m=max(n-5,0)
    mean=1+m*p
    variance=m*p*(1-p)
    q={1:Q(0),2:Q(0),3:q3,4:q4}
    for h in range(1,5):
        variance += 2*max(m-h,0)*(q[h]-p*p)
    return mean,variance

for n in range(3,30):
    mean,var=predicted(n)
    check(mean>=1 and var>=0, 'finite moments '+str(n))
    if n>=10:
        check(var==(n-5)*variance_rate+Q(146737,3645000),'linear variance '+str(n))


def actual_components(gaps):
    n=len(gaps)+1
    xs=[0]
    for g in gaps: xs.append(xs[-1]+g)
    adjacency=[set() for _ in range(n)]
    for i in range(n):
        candidates=sorted((abs(xs[j]-xs[i]),j) for j in range(n) if j!=i)
        check(len(candidates)<2 or candidates[1][0]!=candidates[2][0] if len(candidates)>2 else True,
              'second-neighbor distance tie')
        for _,j in candidates[:2]:
            adjacency[i].add(j)
            adjacency[j].add(i)
    seen=set();components=0
    for i in range(n):
        if i in seen: continue
        components+=1
        seen.add(i)
        stack=[i]
        while stack:
            for j in adjacency[stack.pop()]:
                if j not in seen:
                    seen.add(j);stack.append(j)
    return components


def cut_components(gaps):
    return 1+sum(gaps[i]>gaps[i-1]+gaps[i-2] and gaps[i]>gaps[i+1]+gaps[i+2]
                 for i in range(2,len(gaps)-2))

# Every permutation of distinct binary-power gaps has unique sums and hence no distance ties.
for n in range(3,9):
    for gaps in permutations([1<<k for k in range(n-1)]):
        check(actual_components(gaps)==cut_components(gaps), 'exhaustive '+str(n)+' '+str(gaps))

rng=Random(20261121)
for n in range(9,18):
    for _ in range(400):
        gaps=[1<<k for k in range(n-1)]
        rng.shuffle(gaps)
        check(actual_components(gaps)==cut_components(gaps),'random '+str(n))

print('PASS:',checks,'exact assertions')
print('density:',p)
print('lag 3:',q3,'lag 4:',q4)
print('variance rate:',variance_rate)
print('limiting variance/mean:',variance_rate/p)
for n in (6,8,10,20):
 print('n=',n,'mean,variance=',predicted(n))
