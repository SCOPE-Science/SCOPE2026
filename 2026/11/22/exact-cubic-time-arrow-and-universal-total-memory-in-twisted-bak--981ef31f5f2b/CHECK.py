#!/usr/bin/env python3
"""Exact finite-dimensional checks for stationary twisted-baker cubic moments.

Python 3 standard library only. The all-dimension proof is in RESULT.md.
"""
from fractions import Fraction as Q


def convolution(a, b, length):
    c = [Q(0)] * length
    for i, v in enumerate(a[:length]):
        for j, w in enumerate(b[:length-i]):
            c[i+j] += v*w
    return c


def reciprocal(a, length):
    assert a[0] == 1
    out = [Q(1)] + [Q(0)]*(length-1)
    for k in range(1, length):
        out[k] = -sum(a[j]*out[k-j] for j in range(1, min(k+1,len(a))))
    return out


def closed_coefficients(m, length):
    t = [Q(1)] + [Q(0)]*(length-1)
    for _ in range(m-1):
        t = convolution(t, [Q(1),-Q(1,2)],length)
    da = convolution(t,[Q(1),-Q(1,4)],length)
    dq = convolution(t,[Q(1),-Q(1,8)],length)
    if m < length:
        da[m] += Q(1,2**(m+1))
        dq[m] -= Q(1,2**(m+2))
    bracket = [v/4 for v in t]
    bracket[m-1] += Q(1,2**(m+1))
    inner = convolution(t,bracket,length)
    num = [Q(0)] + [-v/3 for v in inner[:-1]]
    return convolution(convolution(num,reciprocal(da,length),length),
                       reciprocal(dq,length),length)


def polynomial_transfer_coefficients(m,length):
    # Row coordinates are (q_1,...,q_m,h_1,...,h_m).
    b = [[Q(0) for _ in range(2*m)] for _ in range(2*m)]
    b[0][0]=Q(1,8); b[0][1]=Q(1,2)
    b[0][m]=-Q(1,4); b[0][m+1]=Q(1,2)
    for i in range(1,m-1):
        b[i][i]=Q(1,2);b[i][i+1]=Q(1,2)
    b[m-1][0]=Q(1,8);b[m-1][m-1]=Q(1,2)
    b[m][m]=Q(1,4);b[m][m+1]=Q(1,2)
    for i in range(1,m-1):
        b[m+i][m+i]=Q(1,2);b[m+i][m+i+1]=Q(1,2)
    b[2*m-1][m]=-Q(1,4);b[2*m-1][2*m-1]=Q(1,2)
    v=[Q(0)]*(2*m);v[0]=Q(1)
    out=[]
    for _ in range(length):
        out.append(v[m]/3)
        v=[sum(v[i]*b[i][j] for i in range(2*m)) for j in range(2*m)]
    return out


def validate_transfer(m):
    # Check Pq and Ph identities by the two inverse branches at rational points.
    u=[Q((3*i+2) % 11 - 5, 11) for i in range(m)]
    left=[(u[0]-1)/2]+u[1:]
    right=[u[1]+Q(1,2)]+u[2:]+[-u[0]/2]
    var=[Q(1,3)]+[Q(1,12)]*(m-1)
    h=lambda x,i:x[i]
    q=lambda x,i:x[i]**2-var[i]
    for i in range(m):
        actual=(q(left,i)+q(right,i))/2
        if i==0:
            expected=q(u,0)/8+q(u,1)/2-h(u,0)/4+h(u,1)/2
        elif i==m-1:
            expected=q(u,m-1)/2+q(u,0)/8
        else:
            expected=(q(u,i)+q(u,i+1))/2
        assert actual==expected, (m,i,'quadratic',actual,expected)
        actual=(h(left,i)+h(right,i))/2
        if i==0:
            expected=h(u,0)/4+h(u,1)/2
        elif i==m-1:
            expected=-h(u,0)/4+h(u,m-1)/2
        else:
            expected=(h(u,i)+h(u,i+1))/2
        assert actual==expected, (m,i,'linear',actual,expected)


def main():
    checks=0
    for m in range(2,15):
        length=m+15
        a=polynomial_transfer_coefficients(m,length)
        b=closed_coefficients(m,length)
        assert a==b,(m,'generating-function')
        assert a[0]==0
        for n in range(1,m):
            assert a[n]==-Q(2,3)*(Q(1,4**n)-Q(1,8**n)),(m,n)
        assert a[m]==-Q(2,3)*(Q(1,4**m)-Q(1,8**m))-Q(1,3*2**(m+1)),m
        t=Q(1,2**(m-1))
        da=Q(3,4)*t+Q(1,2**(m+1))
        dq=Q(7,8)*t-Q(1,2**(m+2))
        g1=-t*(t/4+Q(1,2**(m+1)))/(3*da*dq)
        assert g1==Q(-2,9),m
        validate_transfer(m)
        checks+=length+3*m+2
    print('PASS: %d exact rational comparisons for M=2,...,14' % checks)
    print('All-lag coefficients, sharp first-return correction, and total -2/9 verified.')

if __name__ == '__main__':
    main()
