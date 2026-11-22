#!/usr/bin/env python3
"""Exact and numerical checks for three-state Jordan RK2 norm classification.

Requires only the Python standard library. A rational tensor-product interpolation
check proves the displayed determinant identity: both sides have degree at most
12 in each variable and agree on 13 distinct rational values in each variable.
"""
from fractions import Fraction as Q
from math import sqrt


def det3(A):
    a, b, c = A[0]
    d, e, f = A[1]
    g, h, k = A[2]
    return a * (e * k - f * h) - b * (d * k - f * g) + c * (d * h - e * g)


def matrix(h, g):
    r = 1 - h + h*h/2
    b = g*h*(1-h)
    c = g*g*h*h/2
    return [[r,b,c],[0,r,b],[0,0,r]]


def gram_defect(T):
    return [[(1 if i==j else 0) - sum(T[k][i]*T[k][j] for k in range(3))
             for j in range(3)] for i in range(3)]


def factored(h,g):
    P=(2-h)**2*(h*h-2*h+4)
    return (h**3*(h-2)/64 *
            (6*g*g*h*h + (h*h-2*h+4)**2) *
            ((6*h*h-12*h+8)*g*g - P))


def frontier(h):
    return (2-h)**2*(h*h-2*h+4)/(6*h*h-12*h+8)


def derivative_direct(h):
    P=(2-h)**2*(h*h-2*h+4)
    dP=-2*(2-h)*(h*h-2*h+4)+(2-h)**2*(2*h-2)
    D=6*h*h-12*h+8
    dD=12*h-12
    return (dP*D-P*dD)/(D*D)


def derivative_factored(h):
    return h*(h-2)*(3*h**3-12*h*h+20*h-8)/(3*h*h-6*h+4)**2


def eigenmax_symmetric(A):
    # Cyclic Jacobi rotations for a real symmetric 3x3 matrix.
    import math
    M=[list(map(float,row)) for row in A]
    for _ in range(75):
        i,j=max(((0,1),(0,2),(1,2)),key=lambda ij:abs(M[ij[0]][ij[1]]))
        if abs(M[i][j])<1e-14:
            break
        tau=(M[j][j]-M[i][i])/(2*M[i][j])
        t=(1 if tau>=0 else -1)/(abs(tau)+math.sqrt(1+tau*tau))
        co=1/math.sqrt(1+t*t); si=t*co
        x=M[i][j]
        M[i][i]-=t*x; M[j][j]+=t*x; M[i][j]=M[j][i]=0.
        for k in range(3):
            if k!=i and k!=j:
                u,v=M[k][i],M[k][j]
                M[k][i]=M[i][k]=co*u-si*v
                M[k][j]=M[j][k]=si*u+co*v
    return max(M[k][k] for k in range(3))


def check():
    identity_count=0
    # 13x13 exact interpolation grid: max individual degree of the
    # determinant difference is 12 in h and 12 in g.
    for i in range(13):
        h=Q(i+1,20)
        for j in range(13):
            g=Q(j,7)
            assert det3(gram_defect(matrix(h,g)))==factored(h,g)
            identity_count+=1

    for i in range(1,45):
        h=Q(i,23)
        assert derivative_direct(h)==derivative_factored(h)
    assert frontier(Q(0))==2
    assert frontier(Q(2))==0
    assert frontier(Q(1,2))==Q(117,56)
    assert Q(117,56)-Q(100,49)==Q(133,2744)

    def cubic(h):return 3*h**3-12*h*h+20*h-8
    assert cubic(Q(563,1000))<0<cubic(Q(564,1000))
    def poly(z):return 81*z**3-126*z*z-80*z-24
    assert poly(Q(20946,10000))<0<poly(Q(20947,10000))

    numerical_count=0
    for i in range(1,28):
        h=i/15.0
        for j in range(0,25):
            g=j/16.0
            T=matrix(h,g)
            norm2=eigenmax_symmetric([[sum(T[k][a]*T[k][b] for k in range(3))
                                     for b in range(3)] for a in range(3)])
            criterion=(g*g<=frontier(h))
            if abs(norm2-1)>3e-10:
                assert (norm2<1)==criterion,(h,g,norm2,frontier(h))
            numerical_count+=1
    print('VERIFY_OK', 'determinant_interpolation_points',identity_count,
          'rational_derivative_checks',44,
          'singular_norm_comparisons',numerical_count,
          'rational_false_contractivity_witness','10/7 at h=1/2')


if __name__=='__main__':
    check()
