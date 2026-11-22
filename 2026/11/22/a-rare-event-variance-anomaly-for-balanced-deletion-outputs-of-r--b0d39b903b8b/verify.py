#!/usr/bin/env python3
"""Independent finite checks for balanced two-deletion Dyck output statistics."""
from math import comb


def dyck(n):
    def rec(s, height, ups):
        if len(s) == 2*n:
            yield s
            return
        if ups < n:
            yield from rec(s+'1', height+1, ups+1)
        if height:
            yield from rec(s+'0', height-1, ups)
    yield from rec('', 0, 0)


def is_dyck(s):
    h = 0
    for v in s:
        h += 1 if v == '1' else -1
        if h < 0:
            return False
    return h == 0


def brute_degree(s):
    opens = [i for i,v in enumerate(s) if v=='1']
    closes = [j for j,v in enumerate(s) if v=='0']
    return len({''.join(c for k,c in enumerate(s) if k not in (i,j))
                for i in opens for j in closes
                if is_dyck(''.join(c for k,c in enumerate(s) if k not in (i,j)))})


def structural_degree(s):
    h = 0; last = 0; peaks = []
    for i,c in enumerate(s):
        h += 1 if c=='1' else -1
        if h == 0:
            factor = s[last:i+1]
            peaks.append(sum(factor[k:k+2]=='10' for k in range(len(factor)-1)))
            last = i+1
    p = sum(peaks)
    t = sum(s[i:i+3] in ('101','010') for i in range(len(s)-2))
    return (p*p+sum(x*x for x in peaks))//2-t


def moments_by_derivative(N):
    C = [comb(2*n,n)//(n+1) for n in range(N+1)]
    A = [0]+[n*C[n-1] for n in range(1,N+1)]
    B = [0]+[n*n*C[n-1] for n in range(1,N+1)]
    def mul(x,y):
        z=[0]*(N+1)
        for i,a in enumerate(x):
            if a:
                for j in range(N+1-i):
                    if y[j]: z[i+j]+=a*y[j]
        return z
    def powser(x,k):
        z=[1]+[0]*N
        for _ in range(k): z=mul(z,x)
        return z
    first=mul(powser(A,2),powser(C,3))
    x=mul(powser(B,2),powser(C,3))
    y=mul(mul(B,powser(A,2)),powser(C,4))
    z=mul(powser(A,4),powser(C,5))
    second=[x[i]+6*y[i]+6*z[i] for i in range(N+1)]
    return C,first,second


def factor_lengths(s):
    h=0;last=0;lengths=[]
    for i,c in enumerate(s):
        h+=1 if c=='1' else -1
        if h==0:
            lengths.append((i+1-last)//2)
            last=i+1
    return lengths


def main():
    C,S1,S2=moments_by_derivative(35)
    for n in range(1,11):
        count=xsum=xsum2=0
        for s in dyck(n):
            count+=1
            actual=brute_degree(s)
            predicted=structural_degree(s)
            assert actual==predicted, (n,s,actual,predicted)
            f=factor_lengths(s)
            x=sum(a*b for i,a in enumerate(f) for b in f[i+1:])
            xsum+=x
            xsum2+=x*x
        assert count==C[n]
        assert (xsum,xsum2)==(S1[n],S2[n]),(n,xsum,S1[n],xsum2,S2[n])
        print('EXACT_CHECK',n,'words',count,'sum_X',xsum,'sum_X2',xsum2)
    for n in (15,20,25,30,35):
        assert 0<=S1[n] and 0<=S2[n]
        print('SERIES_COEFFICIENT',n,'Catalan',C[n],'sum_X',S1[n],'sum_X2',S2[n])
    print('VERIFY_OK')

if __name__=='__main__': main()
