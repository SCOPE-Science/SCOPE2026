"""Independent exact spanning-tree enumeration for one-edge perturbations.

Tests pairwise leaf probabilities against an analytic checkerboard formula.
No external packages required.
"""
from fractions import Fraction
from itertools import combinations


def enumerate_trees(a,b,w):
    vertices=range(a+b)
    edges=[(i,a+j) for i in range(a) for j in range(b)]
    weights=[w if (i,j)==(0,a) else 1 for i,j in edges]
    total=Fraction(0)
    leaf=[Fraction(0) for _ in vertices]
    joint=[[Fraction(0) for _ in range(b)] for _ in range(a)]
    leaf_counts={}
    trees=0
    for subset in combinations(range(len(edges)),a+b-1):
        parent=list(vertices)
        def root(x):
            while parent[x]!=x:
                x=parent[x]
            return x
        degrees=[0]*(a+b)
        okay=True
        for eid in subset:
            x,y=edges[eid]
            rx,ry=root(x),root(y)
            if rx==ry:
                okay=False
                break
            parent[ry]=rx
            degrees[x]+=1;degrees[y]+=1
        if not okay: continue
        trees+=1
        weight=Fraction(1)
        for eid in subset: weight*=weights[eid]
        total+=weight
        counts=(sum(degrees[i]==1 for i in range(a)),sum(degrees[a+j]==1 for j in range(b)))
        leaf_counts[counts]=leaf_counts.get(counts,Fraction(0))+weight
        for i in vertices:
            if degrees[i]==1:leaf[i]+=weight
        for i in range(a):
            for j in range(b):
                if degrees[i]==degrees[a+j]==1:joint[i][j]+=weight
    return trees,total,leaf,joint,leaf_counts


def predicted(a,b,w,i,j):
    pA=Fraction(a-1,a)**(b-1)
    pB=Fraction(b-1,b)**(a-1)
    p=Fraction(a+b-1,a*b)
    alpha=Fraction(1,1) if i==0 else Fraction(-1,a-1)
    beta=Fraction(1,1) if j==0 else Fraction(-1,b-1)
    return -pA*pB*w*(w-1)*alpha*beta/Fraction(a*b)/(1+(w-1)*p)**2


def verify():
    assertions=0
    baseline={}
    for a,b in [(2,2),(2,3),(3,2),(3,3),(2,4),(4,2),(3,4),(4,3),(4,4)]:
        for w in [Fraction(1),Fraction(0),Fraction(1,3),Fraction(2),Fraction(7)]:
            trees,z,leaves,joints,count_weights=enumerate_trees(a,b,w)
            count_probs={key: val/z for key,val in count_weights.items()}
            if w==1:
                baseline[(a,b)]=count_probs
                countA={}; countB={}
                for (x,y),prob in count_probs.items():
                    countA[x]=countA.get(x,0)+prob
                    countB[y]=countB.get(y,0)+prob
                for (x,y),prob in count_probs.items():
                    assert prob==countA[x]*countB[y]
                    assertions+=1
            elif (a,b) in baseline:
                assert count_probs==baseline[(a,b)]
                assertions+=1
            p=Fraction(a+b-1,a*b)
            assert z==a**(b-1)*b**(a-1)*(1+(w-1)*p);assertions+=1
            for i in range(a):
                for j in range(b):
                    cov=joints[i][j]/z-leaves[i]*leaves[a+j]/z**2
                    assert cov==predicted(a,b,w,i,j),(a,b,w,i,j,cov,predicted(a,b,w,i,j));assertions+=1
            print(a,b,w,'trees',trees,'checked')
    print('PASS exact assertions:',assertions)
if __name__=='__main__':verify()
