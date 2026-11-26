"""Independent numerical and rational checks for cactus-graph volume products."""
from math import comb, factorial, sqrt
from fractions import Fraction
from itertools import combinations
from scipy.linalg import null_space
from scipy.spatial import ConvexHull
import numpy as np


def cycle_factor(n):
    assert n >= 3
    density = sum(Fraction((-1) ** j * comb(n, j) * (n-2*j) ** (n-1), (2 ** (n-1)) * factorial(n-1)) for j in range(n // 2+1))
    return Fraction(n * comb(n-1,(n-1)//2), 2 ** (n-1)) * density


def independent_hull_ratio(n, edges):
    basis = null_space(np.ones((1,n)))
    roots = []
    for i,j in edges:
        x = np.zeros(n); x[i]=1; x[j]=-1
        roots.extend((basis.T @ x, -basis.T @ x))
    points = np.array(roots)
    primal_hull = ConvexHull(points)
    planes=primal_hull.equations
    pv=np.array([-row[:-1]/row[-1] for row in planes])
    polar_hull=ConvexHull(pv)
    product=primal_hull.volume*polar_hull.volume
    return product * factorial(n-1) / 4**(n-1),primal_hull.volume, polar_hull.volume


def check():
    expected={3:Fraction(9,8),4:Fraction(1),5:Fraction(575,512),6:Fraction(33,32),7:Fraction(41209,36864),8:Fraction(151,144),9:Fraction(2337507,2097152),10:Fraction(78095,73728)}
    for n, target in expected.items():
        value=cycle_factor(n)
        assert value == target,(n,value,target)
    assert cycle_factor(3)>cycle_factor(5)>cycle_factor(7)>cycle_factor(9)
    assert cycle_factor(4)<cycle_factor(6)<cycle_factor(8)<cycle_factor(10)
    count=0
    for n in range(3,9):
        edges=[(i,(i+1)%n) for i in range(n)]
        r,p,q=independent_hull_ratio(n,edges)
        target=float(cycle_factor(n))
        assert abs(r/target-1)<2e-7,(n,r,target,p,q)
        print('cycle',n,'ratio',r,'primal',p,'polar',q)
        count+=1
    trees=[(4,[(0,1),(1,2),(1,3)]),(5,[(0,1),(1,2),(1,3),(3,4)])]
    for n,edges in trees:
        r,p,q=independent_hull_ratio(n,edges)
        assert abs(r-1)<1e-7,(n,r,p,q)
        count+=1
        print('tree',n,r)
    # two cycles meet at a vertex, and cycle with bridge
    examples=[(4,[(0,1),(1,2),(2,0),(2,3)],cycle_factor(3)),
              (5,[(0,1),(1,2),(2,0),(2,3),(3,4)],cycle_factor(3)),
              (5,[(0,1),(1,2),(2,0),(2,3),(3,4),(4,2)],cycle_factor(3)**2),
              (6,[(0,1),(1,2),(2,0),(2,3),(3,4),(4,5),(5,2)],cycle_factor(3)*cycle_factor(4))]
    for n,edges,target in examples:
        r,p,q=independent_hull_ratio(n,edges)
        assert abs(r/float(target)-1)<5e-7,(n,r,target,p,q)
        print('cactus',n,'ratio',r,'target',target)
        count+=1
    for n in range(3,20):
        assert cycle_factor(n)>0
    print('CACTUS_MAHLER_CHECKS_PASSED',count, 'hull tests, rational cycles 3..19')

if __name__=='__main__':
    check()
