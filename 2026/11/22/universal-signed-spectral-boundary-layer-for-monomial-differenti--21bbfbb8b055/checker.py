#!/usr/bin/env python3
"""Reproducibility checks for the signed spectral law of monomial derivative-composition."""
import math

def weights_sq(m, s, h, n):
    if n == 0: return 0.0
    if n == 1: return 1.0
    return (n ** (2.0-s)) * ((m*(n-1)) ** s) * math.exp(-2*h*(n-1))

def diag(m,s,h,N):
    w=[weights_sq(m,s,h,n) for n in range(N+1)]
    d=w.copy()
    d[0]-=1.0
    for j in range(1, N//m+1):
        d[m*j]-=w[j+1]
    return d

def limiting_constants(m,s):
    x=m*math.log(m)/(m-1)
    c1=2*(m**(s-1))*(m-1)*math.exp(-2*x)*(
        x*x/2 +(m+1)*x/2+(m*m+m+1)/4)
    c2=3*m**(2*s)/64-3*m**(2*s+2)/(2*(m+1)**5)
    return c1,c2,m**s/math.e**2,x

def finite_matrices():
    checks=0
    for m in (2,3,5):
        for s in (-1.0, 0.0, 1.0, 2.5):
            h=.22
            K=13
            N=m*(K-1)+1
            rows=[[0.0]*K for _ in range(N)]
            for n in range(1,K):
                rows[m*(n-1)][n]=math.sqrt(weights_sq(m,s,h,n))
            d=diag(m,s,h,K-1)
            for k in range(K):
                g1=sum(rows[r][k]**2 for r in range(N))
                g2=sum(rows[k][n]**2 for n in range(K))
                assert abs(g1-g2-d[k])<1e-10*(1+abs(d[k]))
                checks+=1
            for k in range(K):
                for j in range(K):
                    if k==j: continue
                    g1=sum(rows[r][k]*rows[r][j] for r in range(N))
                    g2=sum(rows[k][n]*rows[j][n] for n in range(K))
                    assert g1==g2==0
                    checks+=1
    return checks

def asymptotic_tests():
    count=0
    for m in (2,3,4):
        for s in (-1.0,0.0,1.0,2.5):
            C1,C2,Cinf,xstar=limiting_constants(m,s)
            errors=[]
            for h in (.02,.008,.003):
                N=math.ceil(28*m/h)
                d=diag(m,s,h,N)
                c1=h**3*sum(abs(t) for t in d)
                c2=h**5*sum(t*t for t in d)
                cmax=h*h*max(abs(t) for t in d)
                errors.append([abs(c1/C1-1),abs(c2/C2-1),abs(cmax/Cinf-1)])
                count+=3
                for delta,positive in ((-.5,True),(.5,False)):
                    j=round((xstar+delta)/(h*m))
                    k=m*j
                    assert (d[k]>0)==positive, (m,s,h,k,d[k])
                    count+=1
            for i in range(3):
                assert errors[2][i]<.025, (m,s,'limit',i,errors)
                assert errors[2][i]<errors[1][i]<errors[0][i],(m,s,'trend',i,errors)
                count+=2
            # Fixed parameter: residue classes supply both infinite signs.
            h=.13
            d=diag(m,s,h,math.ceil(40*m/h))
            assert all(d[k]>0 for k in range(1,len(d)) if k%m!=0)
            assert any(d[k]<0 and k%m==0 for k in range(1,len(d)))
            count+=2
    return count

def main():
    c=finite_matrices()+asymptotic_tests()
    print(f'PASS {c} finite exact-structure and numerical diagnostic comparisons; limits are proved analytically')
if __name__=='__main__':main()
