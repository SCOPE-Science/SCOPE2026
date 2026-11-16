#!/usr/bin/env python3
"""Exact integer verification of height-three Dyck path Walsh identities.
All public methods and definitions are mathematical; no external dependencies.
"""
from collections import Counter


def enumerate_dyck(n):
    results = []
    def visit(pos, height, ups):
        if pos == 2*n:
            if height == 0:
                results.append(ups)
            return
        if height < 3:
            visit(pos+1, height+1, ups | (1 << pos))
        if height > 0:
            visit(pos+1, height-1, ups)
    visit(0,0,0)
    return results


def fibonacci_strings(m):
    return [q for q in range(1 << m) if not q & (q << 1)]


def dyck_to_fibonacci(path, n):
    height = 0
    y = 0
    for j in range(1,2*n+1):
        height += 1 if path & (1 << (j-1)) else -1
        if 2 <= j <= 2*n-2:
            v=(height - (j % 2))//2
            bit=v ^ int(j % 2 == 0)
            y |= bit << (j-2)
    assert height == 0
    return y


def fibonacci_to_dyck(y,n):
    values=[0]*(2*n+1)
    values[0]=values[1]=values[2*n-1]=values[2*n]=0
    for j in range(2,2*n-1):
        values[j] = ((y>>(j-2))&1) ^ int(j%2==0)
    heights=[2*values[t]+t%2 for t in range(2*n+1)]
    path=0
    for j in range(1,2*n+1):
        delta=heights[j]-heights[j-1]
        assert delta in (-1,1), (n,y,j,heights)
        if delta==1:path |=1 <<(j-1)
    return path


def hadamard(a):
    a=list(a)
    step=1
    while step<len(a):
        for base in range(0,len(a),2*step):
            for i in range(base,base+step):
                left=a[i]; right=a[i+step]
                a[i]=left+right; a[i+step]=left-right
        step*=2
    return a


def fibonacci_multiplier(m,q):
    # Independent enumeration logic: include or exclude vertex with signed weight.
    z_prev2=1
    z_prev1=1 + (1 if not q&1 else -1)
    if m==1:return z_prev1
    for i in range(1,m):
        sign=-1 if q>>i&1 else 1
        z_prev2,z_prev1 = z_prev1,z_prev1+sign*z_prev2
    return z_prev1


def signed_height_dp(n,sign_mask):
    row=[0,0,0,0]
    row[0]=1
    for j in range(2*n):
        nextrow=[0,0,0,0]
        sign=-1 if (sign_mask>>j)&1 else 1
        for h,value in enumerate(row):
            if h<3:nextrow[h+1]+=sign*value
            if h>0:nextrow[h-1]+=value
        row=nextrow
    return row[0]


def q_of_steps(s,n):
    q=0
    for t in range(2,2*n-1):
        if ((s>>(t-1)) ^ (s>>t))&1:
            q |= 1<<(t-2)
    return q


def run():
    expected_zeros={1:0,2:8,3:0,4:0,5:216,6:0,7:0,8:7032}
    expected_minzero={1:None,2:1,3:None,4:None,5:2,6:None,7:None,8:3}
    for n in range(1,9):
        paths=enumerate_dyck(n)
        if n>=2:
            m=2*n-3
            fib=set(fibonacci_strings(m))
            assert {dyck_to_fibonacci(p,n) for p in paths} == fib
            assert {fibonacci_to_dyck(y,n) for y in fib} == set(paths)
        f=[0]*(1<<(2*n))
        for p in paths:f[p]=1
        spectrum=hadamard(f)
        assert sum(x*x for x in spectrum) == (1<<(2*n))*len(paths)
        zeros=sum(v==0 for v in spectrum)
        assert zeros==expected_zeros[n],(n,zeros)
        degree=min((w.bit_count() for w,z in enumerate(spectrum) if z==0), default=None)
        assert degree==expected_minzero[n]
        assert min(abs(v) for v in spectrum if v) == (2 if n%3==2 else 1)
        if n>=2:
            # Checks all 2^(2n) frequencies against an independent signed path recurrence.
            for s,w in enumerate(spectrum):
                assert w==signed_height_dp(n,s), (n,s,w)
                assert abs(w)==abs(fibonacci_multiplier(m,q_of_steps(s,n))), (n,s,w)
        if n==8:
            minzeros=[s for s,v in enumerate(spectrum) if v==0 and s.bit_count()==3]
            assert len(minzeros)==10, len(minzeros)
            assert sum(v==0 and s.bit_count()<=2 for s,v in enumerate(spectrum))==0
        print(f'n={n} paths={len(paths)} frequencies={len(spectrum)} zero={zeros} rank={len(spectrum)-zeros} min_zero_weight={degree} min_nonzero_abs={min(abs(v) for v in spectrum if v)}')
    # Check all-order witness recurrences on many sample dimensions.
    for n in range(2,151):
        m=2*n-3
        all_negative=(1<<m)-1
        z=fibonacci_multiplier(m, all_negative)
        if n%3==2:
            assert z==0
            z2=fibonacci_multiplier(m, all_negative ^ (1<<(m-1)))
            assert abs(z2)==2
        else:
            assert abs(z)==1
    print('HEIGHT3_DYCK_FIBONACCI_WALSH_PASS')

if __name__=='__main__':run()
