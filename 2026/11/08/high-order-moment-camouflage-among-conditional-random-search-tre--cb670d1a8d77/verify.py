"""Independent finite checks of the leaf and conditional root-split formulas."""
from fractions import Fraction
from itertools import permutations
from collections import defaultdict
from math import factorial, comb

def leaf_distribution(n):
    probs = [{0: Fraction(1)}]
    for m in range(1, n+1):
        d = defaultdict(Fraction)
        if m == 1: d[1] = Fraction(1)
        else:
            for a in range(m):
                for x, px in probs[a].items():
                    for y, py in probs[m-1-a].items():
                        d[x+y] += px*py/Fraction(m)
        probs.append(dict(d))
    return probs

def cumul(d, r):
    moms = [Fraction(1)] + [sum(Fraction(k**j)*p for k,p in d.items()) for j in range(1, r+1)]
    cs = [Fraction(0)]*(r+1)
    for j in range(1, r+1):
        cs[j] = moms[j] - sum(comb(j-1, i-1)*cs[i]*moms[j-i] for i in range(1,j))
    return cs[r]

def convolution(p,q):
    d=defaultdict(Fraction)
    for x,px in p.items():
        for y,py in q.items():d[x+y]+=px*py
    return dict(d)

def peak_count(perm):
    n=len(perm)
    return sum(perm[i] > perm[(i-1)%n] and perm[i] > perm[(i+1)%n] for i in range(n))

def tree_leaf_count(perm):
    # Construct an insertion-order BST with actual key comparisons.
    if not perm: return 0
    root = [perm[0], None, None]
    for val in perm[1:]:
        node=root
        while True:
            k=1 if val<node[0] else 2
            if node[k] is None:
                node[k]=[val,None,None];break
            node=node[k]
    stack=[root];cnt=0
    while stack:
        node=stack.pop()
        if node[1] is None and node[2] is None:cnt+=1
        for child in node[1:]:
            if child is not None:stack.append(child)
    return cnt

def main():
    tests=0
    p=leaf_distribution(26)
    for m in range(1,27):
        assert sum(p[m].values())==1;tests+=1
        assert p[m].get(1,0)==Fraction(2**(m-1),factorial(m));tests+=1
    for r in range(1,9):
        cr=Fraction(cumul(p[2*r],r),2*r+1)
        for m in range(2*r,27):
            assert cumul(p[m],r)==(m+1)*cr;(tests:=tests+1)
    for r in range(1,5):
        for n in range(4*r+3,25):
            prior=None
            for a in range(2*r,(n-1)//2+1):
                b=n-1-a
                c=convolution(p[a],p[b])
                for j in range(1,r+1):
                    assert cumul(c,j)==(n+1)*cumul(p[2*j],j)/(2*j+1);tests+=1
                assert c.get(2,0)==Fraction(2**(n-3),factorial(a)*factorial(b));tests+=1
                if prior is not None:
                    assert c[2]>prior[2];tests+=1
                prior=c
    for n in range(1,9):
        hist=defaultdict(int)
        for perm in permutations(range(1,n+1)):
            k=tree_leaf_count(perm)
            hist[k]+=1
            arrival=[0]*n
            for rank,key in enumerate(perm, start=1):arrival[key-1]=rank
            assert k==sum(arrival[i] > (arrival[i-1] if i else 0) and arrival[i] > (arrival[i+1] if i+1<n else 0) for i in range(n));tests+=1
        for k,mult in hist.items():
            assert Fraction(mult,factorial(n))==p[n][k];tests+=1
        if n>=2:
            # Cyclic peaks on n+1 samples with artificially fixed minimum.
            for perm in permutations(range(1,n+1)):
                arrivals=[0]*n
                for rank,key in enumerate(perm,1):arrivals[key-1]=rank
                assert tree_leaf_count(perm)==peak_count([0]+arrivals);tests+=1
    assert cumul(convolution(p[4],p[6]),1)==4;tests+=1
    assert cumul(convolution(p[5],p[5]),1)==4;tests+=1
    assert cumul(convolution(p[4],p[6]),2)==Fraction(8,15);tests+=1
    assert cumul(convolution(p[5],p[5]),2)==Fraction(8,15);tests+=1
    assert convolution(p[4],p[6])[2]==Fraction(2,135);tests+=1
    assert convolution(p[5],p[5])[2]==Fraction(4,225);tests+=1
    print('PASS:',tests,'exact identities, including exhaustive independent insertion histories through n=8')
if __name__=='__main__': main()
