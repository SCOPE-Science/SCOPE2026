#!/usr/bin/env python3
"""Exact rational checks for BV stability of local affine L2 projection.
Only Python standard library, arbitrary nonuniform partitions and signed jumps.
"""
from fractions import Fraction as F
from random import Random


def local_affine_step_projection(mesh, jumps):
    """Exact local affine L2 orthogonal projection of sum a 1_(s,1)."""
    out=[]
    for l,r in zip(mesh,mesh[1:]):
        h=r-l
        m0=F(0); slope=F(0)
        for s,a in jumps:
            t=(s-l)/h
            if t<=0: m0+=a
            elif t<1:
                m0+=a*(1-t)
                slope+=6*a*t*(1-t)
        out.append((m0-slope/2,m0+slope/2))
    return out


def var_of_broken_affines(ab):
    result=sum(abs(b-a) for a,b in ab)
    result+=sum(abs(ab[i+1][0]-ab[i][1]) for i in range(len(ab)-1))
    return result


def step_tv(mesh,s):
    return var_of_broken_affines(local_affine_step_projection(mesh,[(s,F(1))]))


def check():
    # Verify the independent moment equations for the local L2 projection.
    # On (0,1), for a jump at t, the projected polynomial is A+B*u.
    for k in range(1,99):
        t=F(k,100)
        A,B=local_affine_step_projection([F(0),F(1)],[(t,F(1))])[0]
        slope=B-A
        assert A+slope/F(2)==1-t
        assert A/F(2)+slope/F(3)==(1-t*t)/2
        assert A==(1-t)*(1-3*t)
        assert B==(1-t)*(1+3*t)
    assert step_tv([F(0),F(1)],F(1,2))==F(3,2)
    assert step_tv([F(0),F(1),F(2)],F(4,9))==F(16,9)
    assert step_tv([F(0),F(1),F(2)],F(1)+F(5,9))==F(16,9)
    assert step_tv([F(0),F(1),F(2),F(3)],F(3,2))==F(2)
    assert step_tv([F(0),F(1,7),F(2,5),F(4,5),F(1)],F(3,5))==F(2)
    # Exhaustive fine rational grid over first, middle and last cells, nonuniform meshes.
    case_count=0
    for mesh in ([F(0),F(1)], [F(0),F(1),F(2)],
                 [F(0),F(2,5),F(3,2),F(7,4)],
                 [F(0),F(1,11),F(3,2),F(8,3),F(13)]):
        bound= {1:F(3,2),2:F(16,9)}.get(len(mesh)-1,F(2))
        for l,r in zip(mesh,mesh[1:]):
            for k in range(1,180):
                s=l+(r-l)*F(k,180)
                assert step_tv(mesh,s)<=bound,(mesh,s,step_tv(mesh,s),bound)
                case_count+=1
    rand=Random(20261118)
    for n in range(1,9):
        bound={1:F(3,2),2:F(16,9)}.get(n,F(2))
        for _ in range(300):
            widths=[F(rand.randrange(1,32),rand.randrange(1,30)) for j in range(n)]
            mesh=[F(0)]
            for h in widths:mesh.append(mesh[-1]+h)
            jumps=[]
            for j in range(rand.randrange(1,16)):
                s=mesh[-1]*F(rand.randrange(1,5000),5000)
                a=F(rand.randrange(-20,21),rand.randrange(1,11))
                jumps.append((s,a))
            var_in=sum(abs(a) for s,a in jumps)
            var_out=var_of_broken_affines(local_affine_step_projection(mesh,jumps))
            assert var_out<=bound*var_in,(n,mesh,jumps,var_out,var_in)
    print('EXACT_PROJECTION_NORMAL_EQUATIONS_AND_WITNESSES_PASS')
    print('EXACT_SINGLE_JUMP_MESH_SWEEP_PASS',case_count)
    print('EXACT_MULTIJUMP_NONUNIFORM_TESTS_PASS',8*300)
    print('ALL_SHARP_BV_BROKEN_AFFINE_PROJECTION_CHECKS_PASS')

if __name__=='__main__':check()
