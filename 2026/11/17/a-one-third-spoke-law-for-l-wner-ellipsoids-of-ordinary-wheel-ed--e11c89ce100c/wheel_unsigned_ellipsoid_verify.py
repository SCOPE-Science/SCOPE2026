"""Numerical reproduction for the ordinary wheel edge-polytope Loewner ellipsoid.

Requires only Python 3 standard library. Execute: python3 wheel_unsigned_ellipsoid_verify.py
Finite checks are corroborative; the paper supplies the all-orders proof.
"""
import math


def root_weight(m):
    c = [4.0 * math.cos(math.pi * k / m)**2 for k in range(1, m)]
    def derivative(a):
        return 1.0/a - 1.0/(1.0-a) + sum((1.0-z)/(a+(1-a)*z) for z in c)
    low, high = 0.000001, .999999
    assert derivative(low)>0 and derivative(high)<0
    for _ in range(90):
        mid = (low+high)/2
        if derivative(mid)>0:low=mid
        else:high=mid
    return (low+high)/2


def solve(A, b):
    n=len(A)
    rows=[list(row)+[v] for row,v in zip(A,b)]
    for k in range(n):
        pivot=max(range(k,n),key=lambda i:abs(rows[i][k]))
        rows[k],rows[pivot]=rows[pivot],rows[k]
        coeff=rows[k][k]
        assert abs(coeff)>1.e-12
        rows[k]=[z/coeff for z in rows[k]]
        for i in range(n):
            if i==k:continue
            scale=rows[i][k]
            for j in range(k,n+1): rows[i][j]-=scale*rows[k][j]
    return [row[-1] for row in rows]


def check_matrix(m):
    a=root_weight(m)
    n=m+1
    vectors=[]
    for i in range(1,m+1):
        v=[0.0]*n; v[0]=1;v[i]=1;vectors.append(v)
    for i in range(1,m+1):
        v=[0.0]*n;v[i]=1;v[1 if i==m else i+1]=1;vectors.append(v)
    weights=[a/m]*m+[(1-a)/m]*m
    mean=[sum(w*v[j] for w,v in zip(weights,vectors)) for j in range(n)]
    assert max(abs(mean[j]-(a if j==0 else (2-a)/m)) for j in range(n))<1e-13
    centered=[[v[j]-mean[j] for j in range(n)] for v in vectors]
    C=[[sum(w*v[i]*v[j] for w,v in zip(weights,centered)) for j in range(n)] for i in range(n)]
    B=[[C[i][j]+1/n for j in range(n)] for i in range(n)]
    errors=[]
    for v in centered:
        u=solve(B,v)
        q=sum(x*y for x,y in zip(v,u))
        errors.append(abs(q-m))
    assert max(errors)<1e-7,(m,max(errors))
    # Verify two spectral eigenfamilies against an independent matrix construction.
    axis=[1.0]+[-1.0/m]*m
    lam_axis=(m+1)/m*a*(1-a)
    actual=solve(B,axis)
    assert max(abs(x - y/lam_axis) for x,y in zip(actual,axis))<1e-7
    for k in range(1,m):
        x=[0.0]+[math.cos(2*math.pi*k*i/m) for i in range(m)]
        l=(a+4*(1-a)*math.cos(math.pi*k/m)**2)/m
        prod=[sum(C[j][t]*x[t] for t in range(n)) for j in range(n)]
        assert max(abs(prod[j]-l*x[j]) for j in range(n))<1e-9
    return max(errors)


def main():
    maxerr=0
    for m in range(3,25):maxerr=max(maxerr,check_matrix(m))
    for m in range(3,100):
        a=root_weight(m)
        c=[4*math.cos(math.pi*k/m)**2 for k in range(1,m)]
        spoke=(1-a)/a+sum(1/(a+(1-a)*z) for z in c)
        rim=a/(1-a)+sum(z/(a+(1-a)*z) for z in c)
        assert abs(spoke-m)<2e-9 and abs(rim-m)<2e-9
    assert abs(root_weight(3)-.5)<1e-12
    assert abs(root_weight(4)-(1-1/math.sqrt(5)))<1e-12
    assert abs(root_weight(5)-.5)<1e-12 and abs(root_weight(6)-.5)<1e-12
    asymptotic=[]
    for m in (100,300,1000,2000):
        a=root_weight(m)
        asymptotic.append((m,m*(a-1/3)))
        assert abs(m*(a-1/3)-5/3)<20/m
    print('WHEEL_UNSIGNED_LOEWNER_PASS matrix_orders=3..24 orbit_checks=3..99 max_contact_error=%.3g alpha_4=%.12f asymptotic=%s' % (maxerr,root_weight(4),asymptotic))


if __name__=='__main__':main()
