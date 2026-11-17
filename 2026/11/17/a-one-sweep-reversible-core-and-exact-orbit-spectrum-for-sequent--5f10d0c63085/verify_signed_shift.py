"""Independent check using packed-bit affine shift and cyclic orbit structure."""
from math import gcd

def update_by_truth_table(x,n):
    for i in range(n):
        left=(x>>((i-1)%n))&1
        middle=(x>>i)&1
        right=(x>>((i+1)%n))&1
        new=(0b00010111>>(4*left+2*middle+right))&1
        x=(x&~(1<<i))|(new<<i)
    return x

def signed_shift(z,L):
    interior=((~(z>>1)) & ((1<<(L-1))-1))
    return interior|((z&1)<<(L-1))

def expected_update_on_core(x,n):
    L=n-1
    z=x>>1
    out0=1-(z&1)
    return out0|(signed_shift(z,L)<<1)

def formula(n,t):
    L=n-1; g=gcd(L,t)
    return ((1<<g) if (t//g)*(L-1)%2==0 else 0)+(2 if n%2 and t%2==0 else 0)

for n in range(3,18):
    N=1<<n
    S=[x for x in range(N) if (x&1)!=((x>>(n-1))&1)]
    assert len(S)==(1<<(n-1))
    assert all(update_by_truth_table(x,n)==expected_update_on_core(x,n) for x in S)
    T={update_by_truth_table(x,n) for x in S}
    assert T==set(S)
    if n%2:
        alt=[sum(((j+i)%2)<<j for j in range(n)) for i in (0,1)]
        assert all(update_by_truth_table(alt[i],n)==alt[1-i] for i in (0,1))
    if n <= 11:
        for t in range(1,2*(n-1)+1):
            count=0
            for x in S:
                y=x
                for _ in range(t):y=update_by_truth_table(y,n)
                count+=y==x
            if n%2 and t%2==0:count+=2
            assert count==formula(n,t),(n,t,count)
    print('n',n,'core',len(S),'signed-shift conjugacy OK')
print('independent packed-bit and affine checks passed')
