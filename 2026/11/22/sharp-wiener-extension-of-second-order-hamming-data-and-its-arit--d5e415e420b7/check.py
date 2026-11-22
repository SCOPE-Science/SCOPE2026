"""Exact-rational finite checks for Hamming-shell Fourier interpolation.
The mathematical proof is independent of these finite checks.
"""
from fractions import Fraction
from math import comb


def solve(n, d):
    assert n >= 2 and Fraction(0) <= d <= 2
    Q = Fraction(n * (n - 1), 4) * d
    r = (Q / n).__floor__()
    D = (n - r) * (n - r - 1)
    br = (n * (r + 1) - Q) / (n - r)
    bs = (Q - n * r) / (n - r - 1)
    bn = -(r * br + (r + 1) * bs) / n
    total = br + bs + bn
    first = r * br + (r + 1) * bs + n * bn
    second = r * (n - r) * br + (r + 1) * (n - r - 1) * bs
    val = abs(br) + abs(bs) + abs(bn)
    formula = 1 + 2 * (Q - r * (r + 1)) / D
    return Q,r,D,br,bs,bn,total,first,second,val,formula


def calc_val(n,d,j):
    Q,r,D,br,bs,bn,*_ = solve(n,d)
    if j == r: b=br
    elif j == r+1:b=bs
    elif j == n:b=bn
    else:b=Fraction(0)
    return b

checks = 0
for n in range(2,101):
    ds = [Fraction(j,20) for j in range(41)]
    ds += [Fraction(4*j,n-1) for j in range(1,(n-1)//2+1)]
    for d in set(ds):
        Q,r,D,br,bs,bn,total,first,second,val,formula = solve(n,d)
        assert 0 <= r <= (n-1)//2
        assert D > 0 and br >= 0 and bs >= 0 and bn <= 0
        assert total == 1 and first == 0 and second == Q and val == formula
        for j in range(n+1):
            P = 1 - Fraction(2*(j-r)*(j-r-1),D)
            assert abs(P) <= 1
        dual = 1 - Fraction(2*r*(r+1),D) + Fraction(2*Q,D)
        assert dual == val
        checks+=n+7

# Fully independent Walsh transform from inverse spectral construction at n <= 7.
for n in range(2,8):
    for d in [Fraction(0), Fraction(1,3), Fraction(1), Fraction(3,2), Fraction(2)]:
        Q,r,D,br,bs,bn,total,first,second,val,formula=solve(n,d)
        weights=[Fraction(0)]*(1<<n)
        for k,b in [(r,br),(r+1,bs),(n,bn)]:
            for S in range(1<<n):
                if S.bit_count()==k: weights[S]+=b/comb(n,k)
        arr=[]
        for x in range(1<<n):
            v=sum((weights[S] if ((x&S).bit_count()%2)==0 else -weights[S]) for S in range(1<<n))
            arr.append(v)
            if x.bit_count()==0 or x.bit_count()==1:assert v==1
            if x.bit_count()==2:assert v==1-d
            checks+=1
        for S in range(1<<n):
            actual=sum((arr[x] if ((x&S).bit_count()%2)==0 else -arr[x]) for x in range(1<<n))/2**n
            assert actual==weights[S]
            checks+=1
        assert sum(abs(v) for v in weights)==formula

print('HAMMING_WIENER_EXACT_CHECKS_OK',checks)
