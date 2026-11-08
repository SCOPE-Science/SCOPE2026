#!/usr/bin/env python3
"""Exact checks for enumeration of optimal total outer-independent coalitions on cycles."""
from itertools import combinations

def matmul(a,b):
    n=len(a); p=len(b); m=len(b[0])
    return [[sum(a[i][k]*b[k][j] for k in range(p)) for j in range(m)] for i in range(n)]

def ident(n):return [[int(i==j) for j in range(n)] for i in range(n)]

def charpoly(A):
    n=len(A);B=ident(n);co=[1]
    for k in range(1,n+1):
        AB=matmul(A,B); tr=sum(AB[i][i] for i in range(n))
        assert tr%k==0
        c=-tr//k;co.append(c)
        B=[[AB[i][j]+(c if i==j else 0) for j in range(n)] for i in range(n)]
    return co

def trace_seq(A,high):
    B=ident(len(A)); out=[]
    for n in range(high+1):
        out.append(sum(B[i][i] for i in range(len(A))))
        B=matmul(B,A)
    return out

def trans_matrices():
    colors=(0,1,2)
    st=[(a,b) for a in colors for b in colors if (a!=b or a==0)]
    T=[[int(b==bb and (c==0 or (c!=a and c!=b))) for (bb,c) in st] for (a,b) in st]
    bstates=[(0,0),(0,1),(1,0)]
    U=[[2**c if b==bb and not (a==c==1) else 0
        for (bb,c) in bstates] for (a,b) in bstates]
    return T,U

def expected(n):
    a=[4,1,3,10]; b=[3,0,-2]; f=[3,1,1]
    for j in range(4,n+1):a.append(a[j-1]+a[j-2]+2*a[j-3]+a[j-4])
    for j in range(3,n+1):b.append(-b[j-2]+b[j-3]);f.append(f[j-1]+2*f[j-3])
    alpha=a[n]+b[n]-f[n]
    assert alpha%2==0
    return alpha//2-2*(n%3==0), (alpha//2-3*(n%3==0)),int(n%3==0)

def brute(n):
    universe=(1<<n)-1
    neighbors=[(1<<((i-1)%n))|(1<<((i+1)%n)) for i in range(n)]
    # Direct definition, no reduction to 2-packings or transfer matrices.
    def toi(D):
        outside=universe^D
        for v in range(n):
            if not (neighbors[v]&D):return False
            if outside&(1<<v) and neighbors[v]&outside:return False
        return True
    hist={2:0,3:0}
    def rec(masks,used,pos):
        if pos==n:
            if used!=3:return
            a,b,c=masks
            if toi(a) or toi(b) or toi(c):return
            e=int(toi(a|b))+int(toi(a|c))+int(toi(b|c))
            if e in hist:hist[e]+=1
            return
        v=1<<pos
        for j in range(min(used+1,3)):
            masks[j]|=v
            rec(masks,max(used,j+1),pos+1)
            masks[j]^=v
    rec([1,0,0],1,1)
    return hist[2]+hist[3],hist[2],hist[3]

def main():
    T,U=trans_matrices()
    assert len(T)==7 and len(U)==3
    assert charpoly(T)==[1,-1,0,-4,-1,-1,1,1]
    assert charpoly(U)==[1,-1,0,-2]
    print('EXACT_CHARACTERISTIC_POLYNOMIALS_OK',len(T),len(U))
    t=trace_seq(T,45);f=trace_seq(U,45)
    for n in range(3,46):
        pred,stars,triangles=expected(n)
        assert (t[n]-f[n])%2==0
        assert pred==(t[n]-f[n])//2-2*(n%3==0)
        assert pred==stars+triangles
    print('INDEPENDENT_TRACE_RECURRENCES_OK 3..45')
    for n in range(3,13):
        actual=brute(n)
        want=expected(n)
        assert actual==want,(n,actual,want)
        print('DIRECT_UNORDERED_PARTITIONS_OK',n,*actual)
    print('VERIFY_OK')

if __name__=='__main__':main()
