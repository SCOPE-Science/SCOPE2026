#!/usr/bin/env python3
"""Exact finite tests for the trace-zero obstruction; the general theorem is proved separately.

Over F3, checks the entire projective space of plane-filling quintic equations
and every all-smooth two-dimensional rational pencil. Over F9, checks every
binary quadratic form for the nonsquare-or-zero alternative. No numerical
sample is used as a proof of the all-finite-fields statement.
"""
import itertools


def add9(a,b):
    return ((a%3+b%3)%3)+3*((a//3+b//3)%3)

def neg9(a):
    return ((-a%3)%3)+3*((-(a//3)%3)%3)

def mul9(a,b):
    u,v=a%3,a//3
    x,y=b%3,b//3
    return ((u*x+2*v*y)%3)+3*((u*y+v*x)%3)


def check_f9_quadratics():
    squares={mul9(a,a) for a in range(1,9)}
    assert len(squares)==4
    for a,b,c in itertools.product(range(9),repeat=3):
        # Every nonzero 2-var quadratic form has zero or a nonsquare output.
        vals={add9(add9(mul9(a,mul9(x,x)),mul9(b,mul9(x,y))),mul9(c,mul9(y,y)))
              for x,y in itertools.product(range(9),repeat=2) if (x,y)!=(0,0)}
        assert 0 in vals or any(t not in squares for t in vals)
    print('F9_QUADRATIC_ALTERNATIVE_PASS 729')


def matmul(A,B):
    return tuple(sum(A[3*i+k]*B[3*k+j] for k in range(3))%3 for i in range(3) for j in range(3))


def det(A):
    a,b,c,d,e,f,g,h,i=A
    return (a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g))%3


def form(A):
    # Canonical projective nonzero matrix in M3(F3)/F3 I.
    c=A[8]
    M=tuple((A[i]-(c if i in (0,4,8) else 0))%3 for i in range(9))
    if not any(M):
        return None
    if next(t for t in M if t)==2:
        M=tuple((2*t)%3 for t in M)
    return M


def sm(A):
    return all(det(tuple(((t if j in (0,4,8) else 0)-A[j])%3 for j in range(9)))
               for t in range(3))


def tr(A):
    return (A[0]+A[4]+A[8])%3


def check_f3_pencils():
    classes={form(x+(0,)) for x in itertools.product(range(3),repeat=8)}
    classes.discard(None)
    assert len(classes)==(3**8-1)//2
    smooth=sorted(A for A in classes if sm(A))
    assert len(smooth)==576
    trace_zero=sum(tr(A)==0 for A in smooth)
    pencils=set()
    for i,A in enumerate(smooth):
        for B in smooth[i+1:]:
            C=form(tuple((a+b)%3 for a,b in zip(A,B)))
            D=form(tuple((a-b)%3 for a,b in zip(A,B)))
            if C in smooth_set and D in smooth_set:
                members=tuple(sorted((A,B,C,D)))
                assert len(set(members))==4
                assert sum(tr(M)==0 for M in members)==1
                pencils.add(members)
    assert len(pencils)==2016
    # Every trace-zero member of every smooth pencil is unique.
    print('F3_TALLINI_PENCILS_PASS',len(smooth),trace_zero,len(pencils))


if __name__=='__main__':
    check_f9_quadratics()
    # Set only used for O(1) membership, never as unverified mathematical evidence.
    classes={form(x+(0,)) for x in itertools.product(range(3),repeat=8)}
    smooth_set={A for A in classes if A is not None and sm(A)}
    check_f3_pencils()
    A=(0,0,1,1,0,1,0,1,0)
    B=matmul(A,A)
    assert tr(A)==0 and tr(B)!=0
    assert all(sm(tuple((s*a+t*b)%3 for a,b in zip(A,B)))
               for s,t in itertools.product(range(3),repeat=2) if (s,t)!=(0,0))
    print('F3_FIELD_MULTIPLICATION_WITNESS_PASS')
