#!/usr/bin/env python3
"""Independent finite tests for a geometric constraint-response operator.
Pure Python standard library. Finite checks are corroboration, not an infinite proof.
"""
import math


def matrices(n, m):
    if n < 5 or n % 2 != 1 or not 0 <= m < n:
        raise ValueError('odd n>=5 and 0<=m<n required')
    x = math.pi / n
    k = (n - 1) // 2
    a = m*x
    b = k*a
    return ((2*math.sin(x)*math.cos(a), -2*math.cos(x)*math.sin(a)),
            (2*math.cos(x/2)*math.cos(b), -2*math.sin(x/2)*math.sin(b)))


def singular_values_2(M):
    (a,b),(c,d)=M
    tr=a*a+b*b+c*c+d*d
    determinant=a*d-b*c
    discr=max(0.,tr*tr-4*determinant*determinant)
    large=math.sqrt(max(0.,(tr+math.sqrt(discr))/2))
    small=abs(determinant)/large if large>0 else 0.
    return (large, small)


def analytic_spectrum(n):
    out=[]
    for m in range(n):
        out.extend(singular_values_2(matrices(n,m)))
    return sorted(out)


def jacobi_eigenvalues(matrix):
    A=[list(map(float,r)) for r in matrix]; dim=len(A)
    for sweep in range(100):
        changed=False
        for i in range(dim):
            for j in range(i+1,dim):
                if abs(A[i][j]) < 1.e-14: continue
                changed=True
                theta=0.5*math.atan2(2*A[i][j],A[j][j]-A[i][i])
                # Orthogonal column rotation: Q_ii=cos, Q_ij=sin; Q_ji=-sin, Q_jj=cos.
                c=math.cos(theta); s=math.sin(theta)
                ai=A[i][i];aj=A[j][j];aij=A[i][j]
                A[i][i]=c*c*ai-2*c*s*aij+s*s*aj
                A[j][j]=s*s*ai+2*c*s*aij+c*c*aj
                A[i][j]=A[j][i]=0.
                for k in range(dim):
                    if k==i or k==j: continue
                    aki=A[k][i]; akj=A[k][j]
                    A[k][i]=A[i][k]=c*aki-s*akj
                    A[k][j]=A[j][k]=s*aki+c*akj
        if not changed: break
    return sorted(A[i][i] for i in range(dim))


def direct_spectrum(n):
    # Full (2n x 2n) Jacobian of the side and diametral edge lengths.
    R=1/(2*math.cos(math.pi/(2*n)))
    pts=[(R*math.cos(2*math.pi*i/n), R*math.sin(2*math.pi*i/n)) for i in range(n)]
    edges=[(i,(i+1)%n) for i in range(n)] + [(i,(i+(n-1)//2)%n) for i in range(n)]
    rows=[]
    for i,j in edges:
        dx=pts[j][0]-pts[i][0];dy=pts[j][1]-pts[i][1]
        length=math.hypot(dx,dy)
        r=[0.]*(2*n)
        r[2*i]=-dx/length;r[2*i+1]=-dy/length
        r[2*j]=dx/length;r[2*j+1]=dy/length
        rows.append(r)
    gram=[[sum(rows[k][i]*rows[k][j] for k in range(2*n)) for j in range(2*n)] for i in range(2*n)]
    values=jacobi_eigenvalues(gram)
    return sorted(math.sqrt(max(v,0)) for v in values)


def main():
    checks=0
    for n in [5,7,9,11,13]:
        s=analytic_spectrum(n);t=direct_spectrum(n)
        assert max(abs(a-b) for a,b in zip(s,t))<2e-7,(n,max(abs(a-b) for a,b in zip(s,t)))
        assert sum(v<1e-7 for v in s)==3
        checks+=2
    for n in range(7,302,2):
        values=[]
        for m in range(n):
            large,small=singular_values_2(matrices(n,m))
            if small>1e-8: values.append((small,m))
            if large>1e-8: values.append((large,m))
        best=min(values)
        assert best[1] in (3,n-3),(n,best)
        checks+=1
    target=math.pi*math.sqrt(25-math.sqrt(369))
    values=[]
    for n in [101,201,401,801,1601]:
        mode3=singular_values_2(matrices(n,3))[1]
        values.append(n*mode3)
    assert all(values[i]>values[i+1]>target for i in range(len(values)-1)),values
    assert abs(values[-1]-target)<1e-4,(values[-1],target)
    checks+=2
    # Distinct arithmetic proof identities for determinants of the parity matrices.
    for n in [5,7,11,27,101]:
        x=math.pi/n; g=math.cos(x/2);h=math.sin(x/2)
        for m in range(1,(n-1)//2+1):
            M=matrices(n,m);det=(M[0][0]*M[1][1]-M[0][1]*M[1][0])/4
            alpha=m*x; beta=alpha/2
            d=(2*g*math.cos(beta)*(math.sin(beta)**2-h*h)) if m%2 else (2*g*math.sin(beta)*(g*g-math.sin(beta)**2))
            assert abs(abs(det)-d)<1e-10, (n,m,det,d)
            checks+=1
    print(f'PASS: {checks} finite independent tests; leading constant {target:.12f}; n*sigma_3={values[-1]:.12f}.')

if __name__=='__main__':main()
