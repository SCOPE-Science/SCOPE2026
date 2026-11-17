"""Exact-rational diagnostics for the star maximal-averaging two-input BV theorem.
Run with python verify_star_two_input.py (standard library only).
Finite tests supplement, rather than replace, the analytical proof.
"""
from fractions import Fraction as Q
from itertools import product
from random import Random


def bound(k):
    return Q(1,2) if k==1 else Q(1) if k==2 else Q(5,4) if k==3 else Q(k,2)


def graph_balls(x):
    k=len(x)-1
    balls=[(0,),tuple(range(k+1))]
    for i in range(1,k+1): balls.extend([(i,), (0,i)])
    return sorted(set(balls))


def direct_M(x):
    balls=graph_balls(x)
    return tuple(max(sum(x[a] for a in b)/len(b) for b in balls if i in b) for i in range(len(x)))


def TV(x):return sum(abs(x[i]-x[0]) for i in range(1,len(x)))


def F(d):
    k=len(d); mu=sum(d)/Q(k+1)
    H=max([Q(0),mu]+[z/2 for z in d])
    return tuple(max(z,z/2,mu)-H for z in d)


def sample_witness(k):
    if k==1: d=[Q(1)]
    elif k in (2,3): d=[Q(1)]*k
    else: d=[Q(1)]+[Q(-3)]*(k-1)
    e=d.copy(); e[0]+=Q(1,10)
    baseline=max([Q(0)]+[-z for z in d+e])
    x=(baseline,)+tuple(baseline+z for z in d)
    y=(baseline,)+tuple(baseline+z for z in e)
    assert min(x+y)>=0
    assert TV(tuple(a-b for a,b in zip(x,y)))==Q(1,10)
    gain=TV(tuple(a-b for a,b in zip(direct_M(x),direct_M(y))))
    return gain/Q(1,10)


def assert_formula(k,d):
    baseline=max([Q(0)]+[-v for v in d])
    x=(baseline,)+tuple(baseline+z for z in d)
    m=direct_M(x)
    assert F(d)==tuple(m[i]-m[0] for i in range(1,k+1))


def jacobian_column_norm(k,d):
    # Inspect a nearby exact rational perturbation; use only strict-branch points.
    mu=sum(d)/Q(k+1); hub=[(Q(0),('zero',0)),(mu,('mean',0))]
    hub.extend([(v/2,('half',i)) for i,v in enumerate(d)])
    hub.sort(key=lambda z:z[0],reverse=True)
    if hub[0][0]==hub[1][0]:return None
    rows=[]
    for i,v in enumerate(d):
        opts=sorted([(v,'direct'),(v/2,'half'),(mu,'mean')],reverse=True)
        if opts[0][0]==opts[1][0]:return None
        rows.append((i,opts[0][1]))
    def vec(kind,idx):
        if kind=='zero':return [Q(0)]*k
        if kind=='mean':return [Q(1,k+1)]*k
        return [(Q(1) if kind=='direct' else Q(1,2)) if a==idx else Q(0) for a in range(k)]
    hv=vec(*hub[0][1]); mat=[]
    for i,kind in rows:mat.append([v-h for v,h in zip(vec(kind,i),hv)])
    return max(sum(abs(mat[i][j]) for i in range(k)) for j in range(k))


def check():
    grid=0; random_cases=0; jac_cases=0
    for k in range(1,24):
        assert sample_witness(k)==bound(k),(k,sample_witness(k),bound(k))
        if k<=5:
            for d0 in product(range(-2,3),repeat=k):
                d=[Q(x) for x in d0]; assert_formula(k,d); grid+=1
        rng=Random(449+k)
        for t in range(1700):
            d=[Q(rng.randint(-90,90),rng.randint(1,11)) for _ in range(k)]
            e=[Q(rng.randint(-90,90),rng.randint(1,11)) for _ in range(k)]
            if d==e:continue
            assert sum(abs(a-b) for a,b in zip(F(d),F(e)))<=bound(k)*sum(abs(a-b) for a,b in zip(d,e))
            random_cases+=1
            if t%3==0:
                assert_formula(k,d)
                j=jacobian_column_norm(k,d)
                if j is not None:
                    assert j<=bound(k),(k,d,j,bound(k));jac_cases+=1
    print('EXACT_ATTAINING_NONNEGATIVE_PAIRS_PASSED',23)
    print('DIRECT_BALL_VS_BRANCH_FORMULA_PASSED',grid)
    print('TWO_INPUT_EXACT_RATIONAL_CHECKS_PASSED',random_cases)
    print('STRICT_BRANCH_COLUMN_NORMS_PASSED',jac_cases)
    print('ALL_STAR_UNCENTERED_TWO_INPUT_DIAGNOSTICS_PASSED')

if __name__=='__main__':check()
