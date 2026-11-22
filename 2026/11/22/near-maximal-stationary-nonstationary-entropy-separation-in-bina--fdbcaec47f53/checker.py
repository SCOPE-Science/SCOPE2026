"""Finite sanity checks for the alternating-marker Ruelle-channel theorem.

Run with Python 3; finite tests supplement, and do not replace, its analytic proof.
"""
import itertools
import math


def circular_markers(bits, m):
    n = len(bits)
    return sum(
        tuple(bits[(i+j) % n] for j in range(m))
        in {(0,) + (1,) * (m-1), (1,) + (0,) * (m-1)}
        for i in range(n)
    )


def minimal_period(bits):
    n=len(bits)
    return min(d for d in range(1,n+1) if n % d == 0 and all(bits[i]==bits[i%d] for i in range(n)))


def entropy(p):
    return -p*math.log(p) - (1-p)*math.log1p(-p)


def main():
    count = 0
    equal_count = 0
    for m in range(3,7):
        q=m-1
        special=(0,)*q + (1,)*q
        rotations={tuple(special[(i+j)%(2*q)] for j in range(2*q)) for i in range(2*q)}
        for n in range(1,15):
            for bits in itertools.product((0,1),repeat=n):
                occurrences=circular_markers(bits,m)
                assert occurrences*q <= n,(m,n,bits,occurrences)
                if occurrences*q == n:
                    assert n%(2*q)==0
                    assert minimal_period(bits)==2*q
                    assert tuple(bits[:2*q]) in rotations
                    equal_count+=1
                count+=1
        for p in (0.1,math.exp(-m),0.4):
            hp=entropy(p)
            stationary=hp+(math.log(2)-hp)/q
            unrestricted=math.log(2)
            assert 0 < hp < stationary <= unrestricted
            assert abs((unrestricted-stationary) - (math.log(2)-hp)*(1-1/q)) < 1e-13
        # Both balanced maximizing input laws have fair one-coordinate marginals.
        assert sum(special)/len(special)==0.5
        assert len(rotations)==2*q
    print(f"PASS: {count} cyclic-word cases, {equal_count} exact-equality checks, 12 entropy comparisons")
    print("Limits: finite-period enumeration is not a proof for all stationary measures.")


if __name__=='__main__':
    main()
