"""Finite exact checks for isolated three-vertex tree components of a cycle-power bond graph.
Python 3.9+; no third-party packages. These tests do not certify a limiting theorem.
"""
from itertools import combinations
from fractions import Fraction
from math import log, exp, ceil

checks = 0

def test(condition, message):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)

def host(n, m):
    return {frozenset((i, (i+k) % n)) for i in range(n) for k in range(1, m+1)}

def conn(vertices, chosen):
    seen = {vertices[0]}
    while True:
        add = set()
        for e in chosen:
            if e & seen:
                add |= e
        if add <= seen:
            break
        seen |= add
    return len(seen) == len(vertices)

def exact_triple_table(n, m, p):
    q = 1-p
    edges = host(n,m)
    triple_sum = Fraction(0)
    trees = [Fraction(0),Fraction(0),Fraction(0)] # center left, middle, right
    cycles = Fraction(0)
    count_t2 = count_t3 = 0
    found = set()
    for i in range(n):
        for a in range(1,m+1):
            for b in range(1,m+1):
                v=(i,(i+a)%n,(i+a+b)%n)
                S=frozenset(v)
                test(S not in found, 'duplicate geometric triple')
                found.add(S)
                internal=[e for e in edges if e <= S]
                t=len(internal)
                test(t==(3 if a+b<=m else 2),'incorrect host induced triple')
                count_t3 += (t==3)
                count_t2 += (t==2)
                border=sum(1 for e in edges if len(e&S)==1)
                test(border==6*m-2*t,'wrong cut cardinality')
                total=Fraction(0)
                for z in range(1<<t):
                    selected=[internal[j] for j in range(t) if z&(1<<j)]
                    if not conn(v,selected):
                        continue
                    k=len(selected)
                    contribution=p**k * q**(t-k+border)
                    total+=contribution
                    if k==2:
                        deg={x:0 for x in v}
                        for e in selected:
                            for x in e:deg[x]+=1
                        centers=[j for j,x in enumerate(v) if deg[x]==2]
                        test(len(centers)==1,'tree has one center')
                        trees[centers[0]]+=contribution
                    else:
                        test(k==3,'unexpected cycle size')
                        cycles+=contribution
                predicted=(p*p*q**(6*m-4) if t==2 else
                           (3*p*p-2*p*p*p)*q**(6*m-6))
                test(total==predicted,'triple component weight mismatch')
                triple_sum+=total
    test(len(found)==n*m*m,'wrong geometric triple count')
    test(count_t3==n*m*(m-1)//2,'triangle host count')
    test(count_t2==n*m*(m+1)//2,'path host count')
    expectation=(n*m*(m+1)//2)*p*p*q**(6*m-4)+(n*m*(m-1)//2)*(3*p*p-2*p*p*p)*q**(6*m-6)
    test(expectation==triple_sum,'exact mean mismatch')
    expected_center_mid=n*m*(m+1)//2*p*p*q**(6*m-4)+n*m*(m-1)//2*p*p*q**(6*m-5)
    expected_center_end=n*m*(m-1)//2*p*p*q**(6*m-5)
    test(trees[1]==expected_center_mid,'middle center probability')
    test(trees[0]==expected_center_end and trees[2]==expected_center_end,'endpoint center probability')
    test(cycles==n*m*(m-1)//2*p**3*q**(6*m-6),'triangle cycle probability')
    test(sum(trees)+cycles==triple_sum,'tree/cycle partition')
    return len(found)

for n,m in [(13,2),(19,2),(25,3),(31,3),(37,4)]:
    for p in [Fraction(1,7),Fraction(2,5)]:
        exact_triple_table(n,m,p)

# Compare the exact cross-edge correction for pairs of vertex-disjoint tree witnesses.
for n,m in [(25,2),(37,3),(45,4)]:
    edges=host(n,m)
    q=Fraction(4,5);p=1-q
    tuples=[]
    for i in range(n):
        for a,b in [(1,1),(1,m),(m,1)]:
            S=frozenset((i,(i+a)%n,(i+a+b)%n))
            chosen={frozenset((i,(i+a)%n)),frozenset(((i+a)%n,(i+a+b)%n))}
            if all(e in edges for e in chosen):
                tuples.append((S,chosen))
    for x,y in combinations(tuples,2):
        S,A=x;T,B=y
        if S & T:continue
        closed_x={e for e in edges if e&S and e not in A}
        closed_y={e for e in edges if e&T and e not in B}
        # Both witness events are compatible unless an open edge belongs to another event's closed set.
        test(not (A&closed_y or B&closed_x),'disjoint witnesses incompatible')
        exact=p**4 * q**len(closed_x|closed_y)
        separate=(p**2*q**len(closed_x))*(p**2*q**len(closed_y))
        cross=len(closed_x&closed_y)
        test(exact==separate*q**(-cross),'cross-edge factor')
        test(cross<=9,'at most nine cross host edges')

# Limiting weighted gap-region law: 3 tree choices below the diagonal, 1 above.
for m in [20,50,100,500]:
    A=m*(m-1)//2
    B=m*(m+1)//2
    total=B+3*A
    test(total==2*m*m-m,'tree embedding count')
    test(abs(3*A/total-.75)<2/m,'host-triangle conditioning')
    test(abs((A+B)/total-.5)<2/m,'middle-center conditioning')
    test(abs(A/total-.25)<2/m,'endpoint-center conditioning')

# Exact centering numerical check; this is NOT a proof of convergence.
for n in [10**7,10**9,10**11]:
    m=ceil(log(n)**3)
    c=0.6
    p=1-exp(-(log(n)+2*log(log(n))+c)/(6*m))
    q=1-p
    mu=n*m*(m+1)/2*p*p*q**(6*m-4) + n*m*(m-1)/2*(3*p*p-2*p**3)*q**(6*m-6)
    target=exp(-c)/18
    test(0<mu<1 and abs(mu-target)<target,'unreasonable finite-centering mean')

print(f'PASS {checks} assertions; exact triple enumeration, topology marks, pair-event corrections, limiting weights')
