"""Exact rational checks for four-box central-section zonoid classification.

Run: python3 verify.py; standard library only. Finite checks support but do
not replace the arbitrary-real-parameter proof of the theorem.
"""
from fractions import Fraction as F
from itertools import product


def vertices(a):
    # Every vertex of a hyperplane slice is the intersection with a cube edge
    # (or a cube vertex); exact rational coordinates avoid degeneracy errors.
    v = set()
    for j in range(4):
        for others in product((-1, 1), repeat=3):
            xs = list(others)
            xs.insert(j, F(-1))
            fneg = sum(F(aa)*xx for aa,xx in zip(a,xs))
            xs[j] = F(1)
            fpos = fneg + 2*a[j]
            if a[j] == 0:
                if fneg == 0:
                    xx=list(xs)
                    xx[j]=F(-1)
                    v.add(tuple(xx))
                    v.add(tuple(xs))
            elif fneg <= 0 <= fpos:
                xx=list(xs)
                xx[j] = F(-1) - fneg/F(a[j])
                v.add(tuple(xx))
    return v


def noncollinear(points):
    if len(points)<3: return False
    a=points[0]
    for b in points[1:]:
        for c in points[1:]:
            u=[bb-aa for aa,bb in zip(a,b)]
            w=[cc-aa for aa,cc in zip(a,c)]
            if any(u[i]*w[j] != u[j]*w[i] for i in range(4) for j in range(i+1,4)):
                return True
    return False


def symmetric(points):
    n=len(points)
    ctr=[sum(p[i] for p in points)/n for i in range(4)]
    ss=set(points)
    return all(tuple(2*ctr[i]-p[i] for i in range(4)) in ss for p in points)


def facet_result(a):
    v=vertices(a)
    facets=[]
    for j in range(4):
        for sign in (-1,1):
            f=[p for p in v if p[j]==sign]
            if noncollinear(f):
                facets.append((j,sign,len(f),symmetric(f)))
    return v,facets


def main():
    total=0; cases_non_z=0; cases_z=0
    for a in product(range(6),repeat=4):
        if sum(a)==0: continue
        v,facets=facet_result(a)
        observed=all(x[3] for x in facets)
        expected=0 in a or max(a)>=sum(a)-max(a)
        assert observed==expected, (a, facets,expected)
        if expected: cases_z+=1
        else: cases_non_z+=1
        total+=1
    print('checked',total,'nonzero coefficient quadruples,',cases_z,'zonoid,',cases_non_z,'nonzonoid')
    for a, expected in [((2,1,1,1),False),((3,1,1,1),True),((3,2,2,0),True),((1,1,1,0),True),((1,1,1,1),False),((4,4,4,1),False)]:
        v,facets=facet_result(a)
        assert all(f[3] for f in facets)==expected,(a,facets)
        print('example',a,'vertices',len(v),'facet sizes',[p[2] for p in facets])
    print('FOUR_CUBE_ZONOID_CLASSIFICATION_RATIONAL_CHECKS_PASSED')


if __name__=='__main__':main()
