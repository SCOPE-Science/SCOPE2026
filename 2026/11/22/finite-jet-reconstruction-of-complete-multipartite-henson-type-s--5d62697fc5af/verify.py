#!/usr/bin/env python3
"""Exact rational checks for low-degree Henson-neighborhood reconstruction."""
from fractions import Fraction as F
from math import comb, factorial
from itertools import combinations_with_replacement

def mul(p,q,M=None):
    ans=[0]*(len(p)+len(q)-1)
    for i,x in enumerate(p):
        for j,y in enumerate(q):
            if M is None or i+j<=M: ans[i+j]+=x*y
    return ans[:M+1] if M is not None else ans

def q_poly(parts,M=None):
    q=[1]
    for a in parts: q=mul(q,[0]+[comb(a,k) for k in range(1,a+1)],M)
    return q

def type_poly(parts):
    n=sum(parts);q=q_poly(parts)
    return [comb(n,k)-(q[k] if k<len(q) else 0) for k in range(n+1)]

def brute(parts):
    n=sum(parts); grp=[]
    for i,a in enumerate(parts):grp.extend([i]*a)
    out=[0]*(n+1)
    for mask in range(1<<n):
        seen={grp[i] for i in range(n) if mask>>i&1}
        if len(seen)<len(parts):out[mask.bit_count()]+=1
    return out

def stirling(M):
    S=[[0]*(M+1) for _ in range(M+1)];S[0][0]=1
    for n in range(1,M+1):
        for k in range(1,n+1):S[n][k]=k*S[n-1][k]+S[n-1][k-1]
    return S

def bernoulli(M):
    B=[F(1)]
    for m in range(1,M+1):B.append(-sum(comb(m+1,k)*B[k] for k in range(m))/F(m+1))
    return B

def reconstruct_squares(parts):
    r=len(parts); M=2*r-2; q=q_poly(parts,3*r-2); product=q[r]
    assert product>0
    # n follows from the immediately following coefficient, no external size needed.
    n=F(r)+F(2*q[r+1],product) if r+1<len(q) else F(r)
    S=stirling(3*r-2)
    # A(t) = Q(exp(t)-1)/(product * t^r), through order M.
    a=[F(0)]*(M+1)
    for j in range(M+1):
        m=r+j
        a[j]=sum(F(q[k]*factorial(k)*S[m][k],factorial(m)) for k in range(r,min(m,len(q)-1)+1))/product
    assert a[0]==1
    L=[F(0)]*(M+1)
    for m in range(1,M+1): L[m]=a[m]-sum(F(k,m)*L[k]*a[m-k] for k in range(1,m))
    assert L[1]==n/2
    assert all(L[j]==0 for j in range(3,M+1,2))
    B=bernoulli(M)
    power=[F(0)]*r
    for j in range(1,r):
        k=2*j
        assert B[k]
        power[j]=L[k]*k*factorial(k)/B[k]
    e=[F(1)]
    for j in range(1,r):
        e.append(sum((-1)**(k-1)*e[j-k]*power[k] for k in range(1,j+1))/j)
    e.append(F(product*product))
    target=[1]
    for v in parts:
        square=v*v
        target=[target[0]]+[target[i]+square*(target[i-1] if i>0 else 0) for i in range(1,len(target))]+[target[-1]*square]
    assert e==target,(parts,e,target)
    return e

def main():
    direct=0; profiles=0
    for r in range(2,6):
        for n in range(r,13):
            for parts in combinations_with_replacement(range(1,n+1),r):
                if sum(parts)!=n:continue
                p=type_poly(parts)
                assert p==brute(parts),(parts,p,brute(parts))
                direct+=1
                reconstruct_squares(parts); profiles+=1
    # Slightly larger profiles check moment inversion beyond brute range.
    for r in range(2,9):
        for parts in combinations_with_replacement(range(1,6),r):
            reconstruct_squares(parts); profiles+=1
    # Degree-three and degree-four loss has the first fixed-order collision at 13.
    first=None; thirteen=[]
    for n in range(3,40):
        m={}
        for a in range(1,n//3+1):
            for b in range(a,(n-a)//2+1):
                c=n-a-b; p=type_poly((a,b,c))
                m.setdefault((p[3],p[4] if n>=4 else 0),[]).append((a,b,c))
                prod=a*b*c; e2=a*b+a*c+b*c
                assert p[3]==comb(n,3)-prod
                if n>=4: assert p[4]==comb(n,4)-prod*(n-3)//2
                if n>=5: assert p[5]==comb(n,5)-prod*(2*n*n-12*n-e2+21)//12
        collisions=[v for v in m.values() if len(v)>1]
        if collisions and first is None:first=n;thirteen=collisions
        if first is None: assert not collisions
    assert first==13 and thirteen==[[(1,6,6),(2,2,9)]],(first,thirteen)
    a=type_poly((1,6,6));b=type_poly((2,2,9))
    assert a[:5]==b[:5] and a[5]==822 and b[5]==798
    for r in range(3,11):
        left=(1,6,6)+(1,)*(r-3); right=(2,2,9)+(1,)*(r-3)
        x=type_poly(left);y=type_poly(right)
        assert x[:r+2]==y[:r+2] and x[r+2]-y[r+2]==24,(r,x[r+2],y[r+2])
    print('VERIFY_OK direct_profiles=%d reconstructed_profiles=%d first_collision=%d witness_p3_p4=%s witness_p5=%s'%(direct,profiles,first,a[3:5],(a[5],b[5])))
if __name__=='__main__':main()
