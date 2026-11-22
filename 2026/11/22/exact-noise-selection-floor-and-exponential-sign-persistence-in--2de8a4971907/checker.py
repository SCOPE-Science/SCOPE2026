"""Exact-rational checks for a noise-selection theorem in scalar Kaczmarz.
No network or external packages are needed. Finite checks illustrate, not replace,
the infinite-family proof in RESULT.md.
"""
from fractions import Fraction as Q
from math import comb, log, exp


def exact_a(m, h):
    assert 1 <= h <= m and h % 2
    return sum((Q(comb(m, j), 2**m) * (Q(2*min(j,h),h)-1)**2
                for j in range(m+1)), Q(0))


def exact_reused(m, h, s):
    assert s % 2 and h % 2
    out = Q(0)
    for j in range(m+1):
        p = Q(min(j,h),h)
        for b in range(s+1):
            w = Q(comb(m,j),2**m)*comb(s,b)*p**b*(1-p)**(s-b)
            out += w*Q((2*b-s)**2,s*s)
    return out


def exact_flip_full(m,h):
    assert h%2
    return sum((Q(comb(m,j),2**m) for j in range((h-1)//2+1)),Q(0))


def exact_flip_sampled(m,h,s):
    assert h%2 and s%2
    return sum((Q(comb(m,j),2**m)*comb(s,b)*
                Q(min(j,h),h)**b*(1-Q(min(j,h),h))**(s-b)
                for j in range(m+1) for b in range((s-1)//2+1)), Q(0))


def fresh_exact(s):
    return sum((Q(comb(s,b),2**s)*Q((2*b-s)**2,s*s)
                for b in range(s+1)),Q(0))


def KLD(u):
    return log(2)+u*log(u)+(1-u)*log(1-u)


def main():
    count=0
    for m in range(2,13):
        for h in range(1,m+1,2):
            a=exact_a(m,h)
            assert a>0; count+=1
            for s in range(1,12,2):
                val=exact_reused(m,h,s)
                target=Q(1,s)+(1-Q(1,s))*a
                assert val==target, (m,h,s,val,target)
                assert fresh_exact(s)==Q(1,s)
                assert exact_flip_sampled(m,h,s)>0
                count+=3
            p=exact_flip_full(m,h)
            assert p == sum((Q(comb(m,j),2**m) for j in range((h-1)//2+1)),Q(0))
            assert 0<p<=Q(1,2)
            count+=2
    assert exact_a(5,3)==Q(7,12)
    assert exact_reused(5,3,3)==Q(13,18)
    assert exact_flip_full(5,3)==Q(3,16)
    assert exact_flip_sampled(5,3,3)==Q(197,864)
    count+=3
    for q in (0.25, 0.5, 0.75):
        lim = 1.0 if q<=0.5 else ((1-q)/q)**2
        seq=[]
        for m in (201,401,801):
            h = min(m-2, int(q*m))
            if not h%2:h-=1
            x = sum((comb(m,j)*(2*min(j,h)/h-1)**2 for j in range(m+1)))/2**m if m<500 else None
            if x is not None: seq.append((m,x))
        assert abs(seq[-1][1]-lim)<0.1, (q,seq,lim)
        count+=1
    print(f'VERIFY_OK {count}')
    print('example m=5 h=3 s=3: a=7/12, reused=13/18, fresh=1/3, full-sign-flip=3/16')

if __name__=='__main__':
    main()
