"""Exact rational and independent numerical checks of a sharp weighted graph-TV modulus.

Only the Python standard library is required.
"""
from fractions import Fraction as F
from itertools import combinations
from random import Random


def closed_modulus(m, w):
    k = len(w)
    assert len(m) == k+1 and all(t > 0 for t in (*m, *w))
    return max([F(1)] + [m[i+1]*sum(w[j] for j in range(k) if j!=i)/((m[0]+m[i+1])*w[i]) for i in range(k)])


def face_modulus(m, w, S):
    """Exact norm of the block-averaging differential on a fused-leaf set."""
    k=len(w)
    outside=[j for j in range(k) if j not in S]
    if not S: return F(1)
    M=m[0]+sum(m[i+1] for i in S)
    W=sum(w[j] for j in outside)
    return max([F(1) if outside else F(0)] + [m[i+1]*W/(M*w[i]) for i in S])


def all_faces_modulus(m, w):
    k=len(w)
    return max(face_modulus(m,w,{i for i in range(k) if mask>>i & 1}) for mask in range(1<<k))


def weighted_tv(x,w):
    return sum(w[i]*abs(x[i+1]-x[0]) for i in range(len(w)))


def kkt_center_and_leaves(x,m,penalty,center,leaves,dual):
    """Exact KKT equalities and the full subgradient inclusion."""
    k=len(leaves)
    assert m[0]*(center-x[0]) == sum(dual)
    for j in range(k):
        assert m[j+1]*(leaves[j]-x[j+1]) + dual[j]==0
        if leaves[j] == center: assert abs(dual[j]) <= penalty[j]
        else: assert dual[j] == penalty[j] * (1 if leaves[j]>center else -1)


def witness(m, w, penalty, i):
    """Exact pairs staying in an open face with the i-th spoke fused."""
    k=len(w)
    c=F(0)
    base_leaves=[F(0) if j==i else F(1) for j in range(k)]
    p=[F(0) if j==i else penalty[j] for j in range(k)]
    x=[c-sum(p)/m[0]]+[base_leaves[j]+p[j]/m[j+1] for j in range(k)]
    kkt_center_and_leaves(x,m,penalty,c,base_leaves,p)
    eps=min([F(1,10),penalty[i]*(m[0]+m[i+1])/(5*m[0]*m[i+1])])
    y=x.copy();y[i+1]+=eps
    shift=m[i+1]*eps/(m[0]+m[i+1]);c2=c+shift
    leaves2=[c2 if j==i else F(1) for j in range(k)]
    p2=[m[i+1]*(eps-shift) if j==i else penalty[j] for j in range(k)]
    assert abs(p2[i])<penalty[i] and c2<1
    kkt_center_and_leaves(y,m,penalty,c2,leaves2,p2)
    d_in=weighted_tv([y[t]-x[t] for t in range(k+1)],w)
    d_out=weighted_tv([leaves2[t-1]-base_leaves[t-1] if t else c2-c for t in range(k+1)],w)
    ratio=d_out/d_in
    expected=m[i+1]*sum(w[j] for j in range(k) if j!=i)/((m[0]+m[i+1])*w[i])
    assert ratio==expected
    return ratio


def soft(x,t):
    return max(x-t,0.0) + min(x+t,0.0)


def prox_numeric(x,m,a):
    """Independent scalar root solution of the full star minimization."""
    def g(c):
        return m[0]*(c-x[0])+sum(max(-a[j],min(a[j],m[j+1]*(c-x[j+1]))) for j in range(len(a)))
    lo=min(x)-sum(a)/m[0]-2
    hi=max(x)+sum(a)/m[0]+2
    for _ in range(95):
        mid=(lo+hi)/2
        if g(mid)>0:hi=mid
        else:lo=mid
    c=(lo+hi)/2
    return [c]+[c+soft(x[j+1]-c,a[j]/m[j+1]) for j in range(len(a))]


def run():
    rng=Random(529431)
    for k in range(1,10):
        for case in range(90):
            m=[F(rng.randint(1,13),rng.randint(1,10)) for _ in range(k+1)]
            w=[F(rng.randint(1,13),rng.randint(1,11)) for _ in range(k)]
            a=[F(rng.randint(1,13),rng.randint(1,9)) for _ in range(k)]
            assert all_faces_modulus(m,w)==closed_modulus(m,w)
            for i in range(k): witness(m,w,a,i)
    print('EXACT_ALL_2_POWER_K_FUSED_FACES_VS_SINGLE_SPOKE_FORMULA_PASS k=1..9 cases=810')
    print('EXACT_KKT_REALIZABLE_STRICT_WITNESSES_PASS 4050')
    for k in range(1,9):
        m=[F(1)]*(k+1);w=[F(1)]*k
        assert closed_modulus(m,w)==max(F(1),F(k-1,2))
        for hub in range(1,10):
            mm=[F(hub)]+[F(1)]*k
            assert closed_modulus(mm,w)==max(F(1),F(k-1,hub+1))
    print('UNWEIGHTED_DEGREE_FOUR_AND_HUB_MASS_PHASE_PASS')
    for k in range(2,9):
        for _ in range(100):
            m=[rng.uniform(.4,4) for j in range(k+1)]
            w=[rng.uniform(.2,5) for j in range(k)]
            a=[rng.uniform(.1,3) for j in range(k)]
            x=[rng.uniform(-8,8) for j in range(k+1)]
            y=[t+rng.uniform(-3,3) for t in x]
            xout=prox_numeric(x,m,a);yout=prox_numeric(y,m,a)
            raw=weighted_tv([xx-yy for xx,yy in zip(x,y)],w)
            gain=weighted_tv([xx-yy for xx,yy in zip(xout,yout)],w)
            K=float(closed_modulus([F(str(v)) for v in m],[F(str(v)) for v in w]))
            assert gain <= K*raw+5e-9, (k,raw,gain,K)
    print('INDEPENDENT_SCALAR_ROOT_TWO_INPUT_STRESS_PASS cases=700')
    print('ALL_STAR_GRAPH_TV_MODULUS_CHECKS_PASS')

if __name__=='__main__':run()
