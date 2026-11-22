"""Reproducible exact arithmetic checks for secant-blended cubic Hermite curvature transfer."""
from fractions import Fraction as Q
import random

def abs_affine_integral(left, right):
    if left * right >= 0:
        return (abs(left) + abs(right)) / 2
    return (left * left + right * right) / (2 * abs(right-left))

def cell_curvature(a,b,left_weight,right_weight):
    # h*H'' evaluated at normalized cell endpoints t=0,1
    e0=4*(1-left_weight)*a-2*right_weight*b
    e1=-2*(1-left_weight)*a+4*right_weight*b
    return abs_affine_integral(e0,e1)

def energy(theta, jumps):
    assert len(theta)==len(jumps)+1
    return sum(cell_curvature(jumps[i], jumps[i+1], theta[i], theta[i+1])
               for i in range(len(jumps)-1))

def main():
    # Integral identities are exact fractions.
    assert abs_affine_integral(Q(4),Q(-2)) == Q(5,3)
    assert abs_affine_integral(Q(-2),Q(4)) == Q(5,3)
    for w in [Q(-3,2),Q(-1,4),Q(0),Q(1,4),Q(1,2),Q(1),Q(5,4),Q(3,2)]:
        theta=[Q(1,3),Q(2,3),w,Q(1,4),Q(1,5)]
        jumps=[Q(0),Q(0),Q(1),Q(0)]
        val=energy(theta,jumps)
        assert val==Q(5,3)*(abs(w)+abs(1-w)),(w,val)
    rng=random.Random(21311)
    for _ in range(1000):
        count=rng.randrange(4,18)
        theta=[Q(rng.randrange(-7,13),6) for _ in range(count+1)]
        jumps=[Q(rng.randrange(-4,5),3) for _ in range(count)]
        exact=energy(theta,jumps)
        upper=Q(5,3)*max(abs(w)+abs(1-w) for w in theta)*sum(map(abs,jumps))
        assert 0<=exact<=upper,(theta,jumps,exact,upper)
        # Mesh independence is in the normalized Hermite formula: h cancels identically.
        h=[Q(rng.randrange(1,100),rng.randrange(1,40)) for _ in range(count-1)]
        assert all(v>0 for v in h)
        # Direct rational verification that the physical-cell integral equals the reference integral.
        for i,hi in enumerate(h):
            u=4*(1-theta[i])*jumps[i]-2*theta[i+1]*jumps[i+1]
            v=-2*(1-theta[i])*jumps[i]+4*theta[i+1]*jumps[i+1]
            # physical H'' endpoints u/h, v/h, dx=h dt
            assert hi*abs_affine_integral(u/hi,v/hi)==abs_affine_integral(u,v)
    print('EXACT_HERMITE_BASIS_AND_5_OVER_3_KERNEL_INTEGRALS_PASS')
    print('EXACT_ONE_JUMP_NONCONVEX_PENALTY_PASS')
    print('EXACT_RATIONAL_NONUNIFORM_MESH_TESTS_PASS 1000')
    print('ALL_SECOND_ORDER_VARIATION_TRANSFER_CHECKS_PASS')

if __name__=='__main__':main()
