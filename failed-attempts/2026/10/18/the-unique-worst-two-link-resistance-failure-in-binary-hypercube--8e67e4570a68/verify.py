"""Exact rational verification of two-edge resistance damage on binary cubes.
Python 3 standard library; run: python3 verify.py
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb

def polyint(d, j, k, shift, square=False):
    # Integrates z^shift (1-z)^j (1+z)^k, optionally times -log(z).
    coeff = [0] * (j + k + 1)
    for a in range(j + 1):
        for b in range(k + 1):
            coeff[a+b] += (-1)**a*comb(j,a)*comb(k,b)
    return sum((F(v,(shift+i+1)**(2 if square else 1))
                for i,v in enumerate(coeff)),F(0))

def parameters(d):
    n = 2**d
    r = F(2,n)*sum((F(comb(d-1,j),j+1) for j in range(d)),F(0))
    s = F(1,n)*sum((F(comb(d-1,j),(j+1)**2) for j in range(d)),F(0))
    def pair(j,k,shift):
        return (F(2,n)*polyint(d,j,k,shift),
                F(1,n)*polyint(d,j,k,shift,True))
    tp,up = pair(1,d-2,0)
    tt,ut = pair(0,d-2,1)
    c=1-r
    assert c>tt and c>tp
    def loss(t,u): return F(2)*(c*s+t*u)/(c*c-t*t)
    return r,s,tp,up,tt,ut,loss(tp,up),loss(tt,ut)

def edges(d):
    return [(v,v^(1<<i)) for i in range(d)
            for v in range(1<<d) if not (v>>i)&1]

def corr(d,e,f,square):
    n=1<<d
    z=F(0)
    for w in range(1,n):
        fw=2*w.bit_count()
        a=((w&e[0]).bit_count()&1)
        b=((w&e[1]).bit_count()&1)
        c=((w&f[0]).bit_count()&1)
        dd=((w&f[1]).bit_count()&1)
        z+=F((((-1)**a-(-1)**b)*((-1)**c-(-1)**dd)),n*fw**(2 if square else 1))
    return z

def inv(M):
    n=len(M)
    A=[[F(M[i][j]) for j in range(n)]
       +[F(i==j) for j in range(n)] for i in range(n)]
    for i in range(n):
        p=next(k for k in range(i,n) if A[k][i])
        A[i],A[p]=A[p],A[i]
        fac=A[i][i]
        A[i]=[z/fac for z in A[i]]
        for k in range(n):
            if k!=i:
                c=A[k][i]
                if c:
                    A[k]=[a-c*b for a,b in zip(A[k],A[i])]
    return [row[n:] for row in A]

def direct_kf(d, removed):
    N=1<<d
    L=[[F(0) for _ in range(N)] for _ in range(N)]
    for a,b in edges(d):
        if (a,b) in removed or (b,a) in removed: continue
        L[a][a]+=1;L[b][b]+=1
        L[a][b]-=1;L[b][a]-=1
    mat=[[L[i][j]+F(1,N) for j in range(N)] for i in range(N)]
    P=inv(mat)
    return N*(sum((P[i][i] for i in range(N)),F(0))-1)

def main():
    checks=0
    for d in range(3,12):
        r,s,tp,up,tt,ut,fp,ft=parameters(d)
        assert tt>tp>0 and ft>fp>0
        if d==3:
            assert ft-fp==F(1,35)
        if d==4:
            assert ft-fp==F(299,10540)
        if d>=5:
            assert tt*ut>tp*up
        checks+=6
    for d in range(3,6):
        E=edges(d);N=1<<d
        r,s,tp,up,tt,ut,fp,ft=parameters(d)
        c=1-r
        K=N*sum((F(comb(d,k),2*k) for k in range(1,d+1)),F(0))
        best=K+N*ft
        achievers=0
        for e,f in combinations(E,2):
            t=corr(d,e,f,False)
            u=corr(d,e,f,True)
            den=c*c-t*t
            assert den>0
            damage=N*F(2)*(c*s+t*u)/den
            assert K+damage<=best
            common=set(e)&set(f)
            if common:
                assert K+damage==best
                achievers+=1
            else:
                assert K+damage<best
            checks+=2
        assert achievers==N*comb(d,2)
        checks+=1
    for d in (3,4):
        E=edges(d)
        e,f=next((e,f) for e,f in combinations(E,2) if set(e)&set(f))
        K=F(2**d)*sum((F(comb(d,k),2*k) for k in range(1,d+1)),F(0))
        assert direct_kf(d,{e,f})==K+(2**d)*parameters(d)[-1]
        checks+=1
    print('VERIFY_OK',checks,'exact rational Fourier, rank-two, all-pair and direct-inverse identities')

if __name__=='__main__': main()
