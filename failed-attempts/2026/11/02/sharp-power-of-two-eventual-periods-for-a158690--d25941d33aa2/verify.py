#!/usr/bin/env python3
"""Exact arithmetic checks for the A158690 power-of-two period theorem."""
from math import comb, factorial

def coefficients(modulus, degree):
    total = [0] * (degree + 1)
    total[0] = 1
    product = [1] + [0] * degree
    for m in range(1, degree + 1):
        factor = [0] + [(-1)**(j + 1) * comb(2*m + j - 2, j) for j in range(1, degree + 1)]
        new = [0] * (degree + 1)
        for a in range(degree + 1):
            for b in range(1, degree + 1 - a):
                new[a+b] = (new[a+b] + product[a]*factor[b]) % modulus
        product = new
        total = [(x+y)%modulus for x,y in zip(total, product)]
    return total

def values(modulus, bound):
    c = coefficients(modulus, bound)
    stirling = [1] + [0]*bound
    result = [1]
    for n in range(1, bound+1):
        for m in range(n, 0, -1):
            stirling[m] = (stirling[m-1] + m*stirling[m]) % modulus
        stirling[0] = 0
        result.append(sum(c[m]*factorial(m)*stirling[m] for m in range(n+1)) % modulus)
    return result

if __name__ == '__main__':
    c = coefficients(32, 7)
    assert c == [1, 1, 2, 7, 1, 5, 11, 30], c
    b = [sum(c[m]*(-1)**(m-j)*comb(m,j) for m in range(j,8)) % 32 for j in range(8)]
    assert b == [4, 23, 16, 19, 19, 25, 25, 30], b
    baseline = [sum(b[j]*pow(j,n,32) for j in range(8))%32 for n in range(5,13)]
    assert baseline == [31,17,31,1,31,17,31,1], baseline
    assert values(1<<12, 10)[:8] == [1,1,5,55,1073,32671%4096,1431665%4096,85363615%4096]
    cases = 0
    for r in range(5, 11):
        modulus = 1 << r
        step = 1 << (r-4)
        bound = max(2*step+40, 2*r+40)
        seq = values(modulus, bound)
        for n in range(r,bound-step+1):
            assert (seq[n+step]-seq[n])%modulus == ((modulus//2) if n%2==0 else 0)
            cases += 1
    for r, expected in [(1,1),(2,2),(3,2),(4,2)]:
        modulus=1<<r
        seq=values(modulus,35)
        assert all(seq[n]==seq[n+expected] for n in range(5,35-expected))
        if expected>1: assert any(seq[n]!=seq[n+1] for n in range(5,34))
    print(f'VERIFY_OK mod32_coefficients=8 mod32_residue_classes=8 dyadic_levels=6 shifts_checked={cases} exact_arithmetic=yes')
