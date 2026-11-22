#!/usr/bin/env python3
"""Exact Eisenstein-integer character transform of rectangular three-row ballot words.

No numerical tolerance or external package is used. The group is (Z/3Z)^(3n),
with 0/1/2 encoding of row labels. Fourier phase convention uses omega^sum(t_i*w_i).
"""
from collections import Counter
from itertools import combinations, product
from math import factorial

EXPECTED = {
 1: (1, 0, {}),
 2: (5, 0, {}),
 3: (42, 1134, {2: 6, 3: 46, 4: 130, 5: 204, 6: 282, 7: 314, 8: 144, 9: 8}),
 4: (462, 3996, {3: 8, 4: 62, 5: 204, 6: 456, 7: 776, 8: 870, 9: 796, 10: 680, 11: 144})
}

def ballot_words(n):
    """All words with n copies of each row 0,1,2 and c0>=c1>=c2 in every prefix."""
    counts = [0, 0, 0]
    word = [0]*(3*n)
    def visit(depth):
        if depth == 3*n:
            yield tuple(word)
            return
        for digit in range(3):
            if counts[digit] == n:
                continue
            counts[digit] += 1
            if counts[0] >= counts[1] >= counts[2]:
                word[depth] = digit
                yield from visit(depth+1)
            counts[digit] -= 1
    return list(visit(0))


def pair_fft(words, length):
    """Exact tensor Fourier transform in Z[omega] = Z + Z*omega, omega^2=-1-omega."""
    m = 3**length
    a = [0]*m
    b = [0]*m
    for word in words:
        idx = sum(d*3**j for j,d in enumerate(word))
        a[idx] += 1
    stride = 1
    for digit_position in range(length):
        jump = 3*stride
        for block in range(0,m,jump):
            for offset in range(stride):
                i = block + offset
                j = i + stride
                k = j + stride
                u,v,w = a[i],a[j],a[k]
                U,V,W = b[i],b[j],b[k]
                a[i] = u+v+w
                b[i] = U+V+W
                a[j] = u-V+W-w
                b[j] = U+v-V-w
                a[k] = u+V-v-W
                b[k] = U-v+w-W
        stride *= 3
    return a,b


def freq_index(t):
    return sum(d*3**i for i,d in enumerate(t))


def direct_pair(words,t):
    cnt = [0,0,0]
    nonzero = [(i,x) for i,x in enumerate(t) if x]
    for w in words:
        e = sum(x*w[i] for i,x in nonzero) % 3
        cnt[e] += 1
    return cnt[0]-cnt[2], cnt[1]-cnt[2], tuple(cnt)


def run():
    results = {}
    for n in (1,2,3,4):
        words = ballot_words(n)
        length=3*n
        assert len(words)==EXPECTED[n][0]
        # Hook product for (n,n,n).
        hooks = 1
        for row in range(3):
            for col in range(n):
                hooks *= (n-1-col) + (2-row) + 1
        assert len(words)==factorial(length)//hooks
        a,b=pair_fft(words,length)
        m=len(a)
        zeros=Counter()
        checksum=0
        for index in range(m):
            aa,bb=a[index],b[index]
            # Algebraic norm of aa+bb*omega: aa^2-aa*bb+bb^2.
            checksum += aa*aa-aa*bb+bb*bb
            if aa==bb==0:
                x=index
                deg=0
                for _ in range(length):
                    deg += (x%3!=0)
                    x//=3
                zeros[deg]+=1
        assert checksum == m*len(words), (n, checksum, m*len(words)) # Parseval.
        assert sum(zeros.values())==EXPECTED[n][1]
        assert dict(sorted(zeros.items()))==EXPECTED[n][2]
        assert a[0]==len(words) and b[0]==0
        # Independent direct phase-bin verification of *all* frequency weight <= 3.
        direct_ct=0
        for k in range(4):
            for positions in combinations(range(length),k):
                for phases in product((1,2),repeat=k):
                    t=[0]*length
                    for i,x in zip(positions,phases):
                        t[i]=x
                    i=freq_index(t)
                    aa,bb,_=direct_pair(words,t)
                    assert (a[i],b[i])==(aa,bb), (n,t,aa,bb,a[i],b[i])
                    direct_ct+=1
        # Nonlocal independent phase counts for deterministic high-weight samples.
        for j in range(67):
            t=tuple((17*j+11*i*i+3*i+j*i) %3 for i in range(length))
            aa,bb,_=direct_pair(words,t)
            i=freq_index(t)
            assert (a[i],b[i])==(aa,bb)
        # Fourier conjugacy for every frequency, no floating-point tolerances.
        for i in range(m):
            x=i; neg=0; stride=1
            for _ in range(length):
                d=x%3; x//=3
                if d:neg+=(3-d)*stride
                stride*=3
            assert a[neg]==a[i]-b[i] and b[neg]==-b[i], (n,i)
        results[n]={'words':len(words),'group_size':m,'zeros':sum(zeros.values()),
          'rank':m-sum(zeros.values()),'zero_degree_counts':dict(sorted(zeros.items())),
          'direct_low_degree_tests':direct_ct,'Parseval_squared_sum':checksum}
        print(f'n={n} tableaux={len(words)} frequencies={m} zeros={sum(zeros.values())} rank={m-sum(zeros.values())} low_frequency_tests={direct_ct}')
    words=ballot_words(4)
    expected_cubic={
      ((2,5,8),(1,2,2)), ((2,5,8),(2,1,1)),
      ((2,5,9),(1,2,2)), ((2,5,9),(2,1,1)),
      ((4,8,11),(1,1,2)), ((4,8,11),(2,2,1)),
      ((5,8,11),(1,1,2)), ((5,8,11),(2,2,1)),
    }
    observed_cubic=set()
    for positions in combinations(range(1,13),3):
        for phases in product((1,2),repeat=3):
            t=[0]*12
            for i,phase in zip(positions,phases):
                t[i-1]=phase
            a,b,cnt=direct_pair(words,t)
            if a==0 and b==0:
                observed_cubic.add((positions,phases))
                assert cnt==(154,154,154)
    assert observed_cubic==expected_cubic, (observed_cubic,expected_cubic)
    print('exact_cubic_witness_list_verified:',len(observed_cubic))
    print('ALL_CHECKS_PASS')
    return results

if __name__ == '__main__':
    run()
