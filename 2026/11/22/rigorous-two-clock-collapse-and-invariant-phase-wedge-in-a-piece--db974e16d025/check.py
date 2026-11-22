"""Exact rational checks for critical two-player maximal-presence map.

Run: python3 check.py . All tests are finite; proofs are in RESULT.md.
"""
from fractions import Fraction as Q


def step(u, v):
    A = 2*u-v-u*v
    B = 2-v-u*v
    C = 2*v-u-u*v
    D = 2-u-u*v
    return abs(A)/B, abs(C)/D


def two_passive(u, v):
    num_u = 3*u+u*v-2*v*v-2*u*v*v
    den_u = 4+u-u*v-2*v*v-2*u*v*v
    num_v = v*(3-u-v-u*v)
    den_v = 4-v-v*v-u*v-u*v*v
    return num_u/den_u, num_v/den_v


def check():
    tested = 0
    passive = 0
    all_active = 0
    for d in range(3, 34):
        for i in range(1, d):
            u=Q(i,d)
            for j in range(i+1):
                v=Q(j,d)
                a,b=step(u,v)
                assert a >= b >= 0
                assert a <= u
                if v>0:
                    assert a < u
                if 2*v-u-u*v <= 0:
                    passive += 1
                    assert 2*b-a-a*b <= 0, (d,i,j)
                    assert step(a,b)==two_passive(u,v)
                else:
                    all_active +=1
                    if u <= Q(1,4) and u>v:
                        q=(u-v)/u
                        q1=(a-b)/a
                        assert q1 >= Q(39,32)*q
                tested += 1
    for d in range(3, 101):
        for i in range(1,d):
            u=Q(i,d)
            a,b=step(u,u)
            assert a==b==u/(2+u)
            w=u
            for t in range(8):
                assert w==1/(2**t*(1/u+1)-1)
                w=step(w,w)[0]
    # One nonsymmetric exact-rational orbit near the corner:
    u,v=Q(7,13),Q(2,13)
    for _ in range(150):
        if 2*v-u-u*v <=0:
            break
        u,v=step(u,v)
    else:
        raise AssertionError('No passive entry')
    t0u,t0v=u,v
    for k in range(12):
        U,V=step(*step(u,v))
        assert U>0 and V>=0
        u,v=U,V
    print('PASS exact_grid_pairs=',tested,'passive_cases=',passive,
          'active_cases=',all_active,'diagonal_checks=',sum(d-1 for d in range(3,101)))
    print('PASS example_passive_entry=',str(t0u),str(t0v))
    print('PASS two-step_sample_ratio=',float(u/t0u)**(1/12))

if __name__=='__main__':
    check()
