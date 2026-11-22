"""Exact checks for covered-vertex matching Fourier convolution on K_{3,n}.

Run: python3 verify.py. Uses only Python's standard library.
"""
from itertools import product
from math import comb, factorial


def e_sign(length, negative, degree):
    """Elementary symmetric sum of length many +/-1 signs."""
    return sum(
        (-1)**j * comb(negative, j) * comb(length-negative, degree-j)
        for j in range(max(0, degree-(length-negative)), min(degree,negative)+1)
    )


def krawtchouk_multiplier(n, a, b):
    return sum(
        factorial(k) * e_sign(3, a, k) * e_sign(n, b, k)
        for k in range(min(3,n)+1)
    )


def cubic_multiplier(n, a, b):
    x = n - 2*b
    if a == 0:
        return x**3+3*x*x+(5-3*n)*x+1-3*n
    if a == 1:
        return (3*x+1)*n+1-x-x*x-x**3
    return cubic_multiplier(n, 3-a, n-b)


def brute_matchings(n):
    """Independent enumeration, row by row, of all matchings in K_{3,n}."""
    cover = []
    def rec(row, used_columns, covered_rows):
        if row == 3:
            cover.append(covered_rows | (used_columns << 3))
            return
        rec(row+1, used_columns, covered_rows)
        for col in range(n):
            if not (used_columns >> col)&1:
                rec(row+1, used_columns | (1 << col), covered_rows | (1 << row))
    rec(0,0,0)
    return cover


def main():
    assertions=0
    for n in range(1,8):
        mats=brute_matchings(n)
        assert len(mats)==n**3+2*n+1
        assertions+=1
        for character in range(1<<(n+3)):
            a=(character&7).bit_count()
            b=(character>>3).bit_count()
            direct=sum((-1)**((character&mask).bit_count()) for mask in mats)
            assert direct==krawtchouk_multiplier(n,a,b)==cubic_multiplier(n,a,b), (n,a,b,direct)
            assertions+=1
    for n in range(1,161):
        zero_pairs=[]
        for a in range(4):
            for b in range(n+1):
                v=krawtchouk_multiplier(n,a,b)
                assert v==cubic_multiplier(n,a,b)
                if not v:zero_pairs.append((a,b))
                assertions+=1
        expected=([(1,1),(2,0)] if n==1 else
                  [(1,16),(2,27)] if n==43 else [])
        assert sorted(zero_pairs)==expected, (n,zero_pairs)
        assertions+=1
    for n in [1,2,3,4,5,11,42,43,44,80,160]:
        lhs=sum(comb(3,a)*comb(n,b)*krawtchouk_multiplier(n,a,b)**2
                for a in range(4) for b in range(n+1))
        rhs=2**(n+3)*sum(comb(3,k)*comb(n,k)*factorial(k)**2
            for k in range(min(3,n)+1))
        assert lhs==rhs
        assertions+=1
    # Finite arithmetic certificates used by the proof, not a substitute for it.
    x_candidates=[]
    for t in (-34,-17,-2,-1,1,2,17,34):
        if (t-1)%3==0:
            x=(t-1)//3
            numer=x**3+x*x+x-1
            if numer%t==0:
                x_candidates.append((x,numer//t))
    assert x_candidates==[(-6,11),(-1,1),(0,-1),(11,43)] or sorted(x_candidates)==sorted([(-6,11),(-1,1),(0,-1),(11,43)])
    assertions+=1
    expected_valid=[(x,n) for x,n in x_candidates if n>=1 and abs(x)<=n and (x-n)%2==0]
    assert sorted(expected_valid)==[(-1,1),(11,43)]
    assertions+=1
    for y in (-2,-1,1,2):
        assert (y**3+2*y-2)%(3*y)!=0
        assertions+=1
    n=43
    zero_count=6*comb(n,16)
    assert zero_count==1591092895308
    assert (1<<(n+3))-zero_count==68777651282356
    assert min(abs(krawtchouk_multiplier(n,a,b)) for a in range(4) for b in range(n+1) if krawtchouk_multiplier(n,a,b))==2
    assert krawtchouk_multiplier(n,0,22)==-2
    assert n**3+2*n+1==79594
    assertions+=5
    print('MATCHED_VERTEX_K3N_EXACT_PASS',assertions)

if __name__=='__main__':
    main()
