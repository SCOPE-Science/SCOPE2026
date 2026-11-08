#!/usr/bin/env python3
"""Independent exact-arithmetic tests of fan matrices and gap-order formula.
The tests illustrate finite dimensions; the universal theorem uses the proof.
"""
import itertools

def determinant(a):
    a=[list(row) for row in a]
    n=len(a); sign=1; denom=1
    for k in range(n-1):
        if not a[k][k]:
            ii=next((i for i in range(k+1,n) if a[i][k]),None)
            if ii is None:return 0
            a[k],a[ii]=a[ii],a[k];sign=-sign
        p=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                x=a[i][j]*p-a[i][k]*a[k][j]
                assert x%denom==0
                a[i][j]=x//denom
            a[i][k]=0
        denom=p
    return sign*a[-1][-1]

def columns(n,bits):
    v=lambda i:[int(i==k) for k in range(1,n+1)]
    e=[None]+[v(i) for i in range(1,n+1)]
    u=[-1]*n
    rho=lambda j:([0]*(n-j))+list(range(1,j+1))
    c=[rho(n) if bits[0] else u]
    c += [rho(n-i) if bits[i] else e[i] for i in range(1,n-1)]
    c += [e[n] if bits[n-1] else e[n-1]]
    return c

def gaps(bits):
    i=[j for j,v in enumerate(bits) if v]
    return [b-a for a,b in zip(i,i[1:])]+([len(bits)-i[-1]] if i else [])

def integer_break(n):
    if n%3==0:return 3**(n//3),1
    if n%3==2:return 2*3**((n-2)//3),(n-2)//3+1
    a=(n-1)//3
    return 4*3**(a-1),a*(a+3)//2

def check():
    tests=0
    for n in range(2,9):
        maxima=[]
        for bits in itertools.product((0,1),repeat=n):
            cc=columns(n,bits)
            matrix=[[c[k] for c in cc] for k in range(n)]
            actual=abs(determinant(matrix))
            expected=1
            for g in gaps(bits):expected*=g
            assert actual==expected,(n,bits,actual,expected)
            maxima.append(actual);tests+=1
        m,c=integer_break(n)
        assert max(maxima)==m,(n,m,max(maxima))
        assert maxima.count(m)==c,(n,c,maxima.count(m))
        print('n=%d cones=%d max_index=%d maximizers=%d' %(n,2**n,m,c))
    print('VERIFY_OK all_fixed_cone_determinants=%d'%tests)
if __name__=='__main__':check()
