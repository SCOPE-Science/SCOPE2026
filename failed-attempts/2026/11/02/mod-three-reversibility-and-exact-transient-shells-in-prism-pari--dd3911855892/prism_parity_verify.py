"""Exact independent checks of binary neighbor-XOR dynamics on prism graphs.

Run: python prism_parity_verify.py
"""
from collections import Counter


def rotl(a,n):
    mask=(1<<n)-1
    return ((a<<1)&mask)|(a>>(n-1))

def rotr(a,n):
    return (a>>1)|((a&1)<<(n-1))

def update(x,n):
    mask=(1<<n)-1
    a=x&mask
    b=(x>>n)&mask
    return (rotl(a,n)^rotr(a,n)^b)|((rotl(b,n)^rotr(b,n)^a)<<n)

def brute(n):
    tot=1<<(2*n)
    first=Counter(); periods=Counter()
    for x in range(tot):
        seen={}; curr=x
        while curr not in seen:
            seen[curr]=len(seen)
            curr=update(curr,n)
        entry=seen[curr]
        period=len(seen)-entry
        first[entry]+=1
        if entry==0: periods[period]+=1
    return dict(sorted(first.items())),dict(sorted(periods.items()))

def dimker(matrix_cols, n):
    piv={}
    for c in matrix_cols:
        a=c
        while a:
            bit=a.bit_length()-1
            if bit in piv: a^=piv[bit]
            else:
                piv[bit]=a
                break
    return n-len(piv)

def rank_checks(n,maximum):
    size=2*n
    cols=[1<<i for i in range(size)]
    out=[]
    for t in range(maximum+1):
        if t:
            cols=[update(c,n) for c in cols]
        out.append(dimker(cols,size))
    return out

def expected_entry(n):
    if n%3:
        return {0:1<<(2*n)}
    e=n & -n
    nperiodic=1<<(2*n-4*e)
    if e==1:
        return {0:nperiodic,1:3*nperiodic,2:12*nperiodic}
    ans={0:nperiodic}
    for t in range(1,e+1):
        ans[t]=15*(1<<(2*n-4*e+4*(t-1)))
    return ans

def fixed_dim_power(n,j):
    # For spatial lengths 2^s, number of F^(2^j)-fixed configurations.
    if j==0:
        return 4
    return min(1<<(j+2),2*n)

def linear_fixed_dim(n,t):
    # Independently build F^t-I and calculate rank.
    size=2*n
    cols=[]
    for i in range(size):
        v=1<<i
        for _ in range(t):
            v=update(v,n)
        cols.append(v^(1<<i))
    return dimker(cols,size)


def main():
    total=0
    for n in range(3,9):
        sh,periods=brute(n)
        exp=expected_entry(n)
        assert sh==exp,(n,sh,exp)
        assert sum(sh.values())==(1<<(2*n))
        print('exhaustive',n,sh,'periodic_periods',periods)
        total+=1<<(2*n)
    print('exhaustive_configuration_count',total)
    for n in (3,4,5,6,7,8,9,10,12,15,18,24):
        e=n & -n
        cutoff=(max(2,e) if n%3==0 else 0)
        rows=rank_checks(n,cutoff+2)
        if n%3:
            assert all(r==0 for r in rows),(n,rows)
        else:
            target=4*e
            for t,r in enumerate(rows):
                if e==1:
                    ex={0:0,1:2}.get(t,4)
                else: ex=4*min(t,e)
                assert r==ex,(n,t,r,ex)
        print('kernel_profile',n,rows)
    for s in range(2,8):
        n=1<<s
        for j in range(s):
            k=1<<j
            got=linear_fixed_dim(n,k)
            expected=fixed_dim_power(n,j)
            assert got==expected,(n,j,got,expected)
        assert update(1,n)!=1
        print('power_two_orbits',n,{'fixed':16,**{2**j:(2**(2**(j+2))-2**(2**(j+1)))//(2**j) for j in range(1,s)}})
    print('PRISM_PARITY_VERIFY_OK')

if __name__=='__main__':main()
