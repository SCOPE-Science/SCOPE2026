"""Integer combinatorial checks, independently enumerating multiplier multiplicities.
Run: python3 check_symbolic.py
"""
from math import comb

def central_min(m):
    return (m+1)*comb(m,(m-1)//2)//m

def old_period_upper(m):
    return sum(comb(2*d,d) for d in range(1,m//3+1))

# Validate the infinite-rank proof's finite exceptional base cases.
for m in (3,5,7,9,11):
    assert old_period_upper(m)<central_min(m)

# Verify the rational/exponential bound for the first 400 odd parameters.
for m in range(13,402,2):
    assert old_period_upper(m)<central_min(m)

for p in (3,5,7,11,13):
    n=2*p
    B=comb(n,p)
    M=central_min(p)
    pairs=[]
    total=0
    min_count=0
    for j in range(p+1):
        t=2*j
        assert (B*comb(p,j))%comb(n,t)==0
        K=(-1)**j*B*comb(p,j)//comb(n,t)
        for eps in (1,-1):
            count=(comb(n,t)+eps*(-1)**j*comb(p,j))//2
            assert 2*count==comb(n,t)+eps*(-1)**j*comb(p,j)
            assert count>=0
            total+=count
            if abs(K-2*eps)==M-2:
                min_count+=count
            pairs.append((K-2*eps,count))
    assert total==(1<<(n-1))
    assert min_count==comb(n,p-1)+comb(p,(p-1)//2)
    assert max(abs(x) for x,c in pairs if c)>0
    assert max(abs(x) for x,c in pairs if c)==B-2
    assert min(abs(x) for x,c in pairs if c)==M-2
    print('prime',p,'rank',total,'minmult',min_count,'condition',f'{B-2}/{M-2}')
print('CHECK_SYMBOLIC_PASS')
