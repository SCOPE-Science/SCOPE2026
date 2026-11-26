"""Exact finite checks of cactus forest connectivity correlations.

The universal claims are proved analytically; this script checks independent
small examples and the positive-polynomial identity at integer test points.
"""
from fractions import Fraction
from itertools import combinations, product


def connected(n, edges, s, t):
    if s == t:
        return True
    seen = {s}; frontier = [s]
    while frontier:
        v = frontier.pop()
        for a,b in edges:
            if a == v and b not in seen: seen.add(b); frontier.append(b)
            if b == v and a not in seen: seen.add(a); frontier.append(a)
    return t in seen


def cyclic(n, edges):
    parent = list(range(n))
    def root(i):
        while parent[i] != i:
            i = parent[i]
        return i
    for a,b in edges:
        ra,rb=root(a),root(b)
        if ra == rb: return True
        parent[ra]=rb
    return False


def exact_forest_probabilities(n, weighted_edges):
    m=len(weighted_edges)
    choices=[]; denom=0
    for mask in range(1 << m):
        chosen=[(a,b) for j,(a,b,w) in enumerate(weighted_edges) if mask>>j&1]
        if cyclic(n,chosen):continue
        weight=Fraction(1)
        for j,(_,_,w) in enumerate(weighted_edges):
            if mask>>j&1:weight*=w
        denom+=weight;choices.append((chosen,weight))
    pairs=list(combinations(range(n),2))
    probs={}
    for p in pairs:
        probs[p]=sum((w for es,w in choices if connected(n,es,*p)),Fraction(0))/denom
    for p in pairs:
        for q in pairs:
            both=sum((w for es,w in choices if connected(n,es,*p) and connected(n,es,*q)),Fraction(0))/denom
            assert both>=probs[p]*probs[q],(weighted_edges,p,q,both-probs[p]*probs[q])
    return len(choices),len(pairs)**2


def symbolic_form(a,b,c,d):
    Z=(1+a)*(1+b)*(1+c)*(1+d)-1
    R=(1+a)*(1+b)+(1+c)*(1+d)-2
    C=(1+a)*(1+c)+(1+b)*(1+d)-2
    H=a+b+c+d
    X=a+d;Y=b+c;P=a*d;Q=b*c
    pos=P*X*(1+Y+Q)+Q*Y*(1+X+P)+P*Y+Q*X+4*P*Q
    assert Z*H-R*C==pos
    assert (pos>0) == (P>0 or Q>0)


def main():
    count=0
    for a,b,c,d in product(range(4),repeat=4):
        symbolic_form(a,b,c,d);count+=1
    cases=[]
    for n in range(3,9):
        cycle=[(i,(i+1)%n,Fraction((i*7+n)%5+1)) for i in range(n)]
        cases.append((n,cycle))
    cases.extend([
       (5, [(0,1,Fraction(2)),(1,2,Fraction(1,3)),(2,0,Fraction(4)),
            (2,3,Fraction(5)),(3,4,Fraction(2)),(4,2,Fraction(1,2))]),
       (6, [(0,1,Fraction(2)),(1,2,Fraction(3)),(2,0,Fraction(4)),
            (2,3,Fraction(5)),(3,4,Fraction(6)),(4,5,Fraction(2)),
            (5,3,Fraction(1,3))]),
       (6, [(0,1,Fraction(2)),(1,2,Fraction(3)),(2,0,Fraction(4)),
            (2,3,Fraction(5)),(3,4,Fraction(6)),(4,5,Fraction(2))]),
    ])
    forest_count=0;pair_tests=0
    for n,ed in cases:
        f,t=exact_forest_probabilities(n,ed)
        forest_count+=f;pair_tests+=t
    print('PASS: {} exact polynomial evaluations; {} forest graphs; {} proper forests; {} ordered pair-pair covariance checks'.format(count,len(cases),forest_count,pair_tests))


if __name__=='__main__':main()
