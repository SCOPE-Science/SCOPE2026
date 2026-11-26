"""Exact independent fan test for canonical tensor-generation chambers.
Pure Python; finite grid checks are diagnostic, not a universal proof.
"""
from fractions import Fraction as Q
from itertools import combinations

def dot(v,w):
    return sum(x*y for x,y in zip(v,w))

def det(v,w,z):
    return (v[0]*(w[1]*z[2]-w[2]*z[1])
            -v[1]*(w[0]*z[2]-w[2]*z[0])
            +v[2]*(w[0]*z[1]-w[1]*z[0]))

def fan(m,a,b):
    rays=[(0,1,-a),(1,0,-b),(0,-1,0),(-1,m,0),(0,0,1),(0,0,-1)]
    pairs=[(0,1),(1,2),(2,3),(3,0)]
    cones=[tuple(sorted((i,j,z))) for i,j in pairs for z in (4,5)]
    assert all(abs(det(*[rays[i] for i in c]))==1 for c in cones)
    return rays,cones

def one_dim_feasible(ineqs):
    lo,hi=None,None
    for aa,bb in ineqs:
        if aa==0:
            if bb<=0:return False
        elif aa>0:
            bd=-bb/aa
            if lo is None or lo<bd:lo=bd
        else:
            bd=-bb/aa
            if hi is None or hi>bd:hi=bd
    return lo is None or hi is None or lo<hi

def two_dim_feasible(ineqs):
    lower=[];upper=[];one=[]
    for a,b,c in ineqs:
        if b==0:one.append((a,c))
        elif b>0:lower.append((-a/b,-c/b))
        else:upper.append((-a/b,-c/b))
    for al,bl in lower:
        for au,bu in upper:
            one.append((au-al,bu-bl))
    return one_dim_feasible(one)

def local_bigness(rays,cones,rho,sgn):
    # Solve <m,v_rho>=-sgn and <m,v_i>>-sgn for all i in star(rho).
    v=rays[rho]
    p=next(i for i,x in enumerate(v) if x)
    idx=[i for i in range(3) if i!=p]
    inequalities=[]
    neighbors={j for co in cones if rho in co for j in co if j!=rho}
    for j in neighbors:
        w=rays[j]
        aa=Q(w[idx[0]])-Q(w[p])*v[idx[0]]/v[p]
        bb=Q(w[idx[1]])-Q(w[p])*v[idx[1]]/v[p]
        cc=Q(sgn)-Q(w[p])*sgn/v[p]
        inequalities.append((aa,bb,cc))
    return two_dim_feasible(inequalities)

def walls_nonzero(rays,cones):
    walls={tuple(sorted(p)) for co in cones for p in combinations(co,2)}
    for u,v in walls:
        adjacent=[co for co in cones if u in co and v in co]
        assert len(adjacent)==2
        e1,e2=[next(j for j in co if j not in (u,v)) for co in adjacent]
        vu,vv,ve=rays[u],rays[v],rays[e1]
        target=tuple(rays[e1][k]+rays[e2][k] for k in range(3))
        denominator=det(vu,vv,ve)
        alpha=Q(det(target,vv,ve),denominator)
        beta=Q(det(vu,target,ve),denominator)
        gamma=Q(det(vu,vv,target),denominator)
        assert gamma==0
        if 2-alpha-beta==0:return False
    return True

def independent_fan_criterion(m,a,b):
    rays,cones=fan(m,a,b)
    return (all(local_bigness(rays,cones,i,1) or local_bigness(rays,cones,i,-1)
                 for i in range(6)) and walls_nonzero(rays,cones))

def closed_form(m,a,b):
    l=b-a*m
    return ((a-2)*(b-m-2)>0
            and (a+2)*(b+m+2)>0
            and abs(l)>m-2
            and abs(l)!=abs(m-2))

def main():
    n=0;passing=0
    for m in range(5):
        for a in range(-6,7):
            for b in range(-9,10):
                got=independent_fan_criterion(m,a,b)
                want=closed_form(m,a,b)
                assert got==want,(m,a,b,got,want)
                n+=1;passing+=want
    assert independent_fan_criterion(2,3,5)
    assert not (5>2*3)  # the positive section slope is not ample
    print('VERIFY_OK exact_integer_fan_local_polytopes_and_wall_degrees',n)
    print('TRUE_CHAMBER_CASES',passing)
    print('UNSUPPORTED_BY_SIMPLE_ANTIAMPLE_CRITERION F2 3S+5F')

if __name__=='__main__':main()
