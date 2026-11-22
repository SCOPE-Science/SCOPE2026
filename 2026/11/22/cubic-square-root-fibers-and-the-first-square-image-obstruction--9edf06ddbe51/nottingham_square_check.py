"""Independent finite-field checks for a square-word formula in truncated substitution groups."""
from collections import Counter
from itertools import product

IRREDUCIBLE = {1: 0b11, 2: 0b111, 3: 0b1011, 4: 0b10011}


def gf_mul(x, y, e):
    mask = (1 << e) - 1
    poly = IRREDUCIBLE[e]
    z = 0
    while y:
        if y & 1:
            z ^= x
        y >>= 1
        x <<= 1
        if x & (1 << e):
            x ^= poly
    return z & mask


def convolution(p, q, e, n=5):
    ans = [0] * (n+1)
    for i, a in enumerate(p):
        if a:
            for j, b in enumerate(q[:n+1-i]):
                if b:
                    ans[i+j] ^= gf_mul(a,b,e)
    return ans


def compose(f, g, e, n=5):
    ans = [0] * (n+1)
    power = [1]+[0]*n
    for i in range(1,n+1):
        power = convolution(power,g,e,n)
        for j in range(n+1):
            ans[j] ^= gf_mul(f[i], power[j],e)
    return tuple(ans)


def test(e):
    q=1<<e
    target_counts=Counter()
    power_hist=Counter()
    for a,b,c,d in product(range(q),repeat=4):
        f=(0,1,a,b,c,d)
        ff=compose(f,f,e)
        u=gf_mul(a,a,e)^b
        A=gf_mul(a,u,e)
        B=gf_mul(b,u,e)
        assert ff==(0,1,0,0,A,B), (e,f,ff,A,B)
        target_counts[A,B]+=1
    for A,B in product(range(q),repeat=2):
        n=target_counts[A,B]
        power_hist[n]+=1
        if A==0 and B==0:
            assert n==q**3
        elif A==0:
            assert n==q**2
        else:
            roots=0
            for u in range(1,q):
                val=gf_mul(gf_mul(u,u,e),u,e)^gf_mul(B,u,e)^gf_mul(A,A,e)
                roots+=(val==0)
            assert n==roots*q**2
    expected=Counter({0:(q*q-1)//3, q*q:(q-1)+q*(q-1)//2,3*q*q:(q-1)*(q-2)//6, q**3:1})
    # q=2: q^3=8 differs from q^2=4; q=4: q^3=64 differs from 3 q^2=48
    assert power_hist==expected,(q,power_hist,expected)
    assert len(target_counts)==(2*q*q+1)//3
    assert sum(target_counts.values())==q**4
    print('q=',q,'image=',len(target_counts),'fiber_hist=',dict(sorted(power_hist.items())), 'OK')

if __name__ == '__main__':
    for e in (1,2,3,4):
        test(e)
    print('NOTTINGHAM_SQUARE_FIBERS_OK')
