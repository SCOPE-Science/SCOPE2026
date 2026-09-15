"""Verify parity no-go for odd-n Chekanov-type torus bulk-deformed potential.
Vianna Lemma 5.2: w_i = eps_i * exp(k_i T^rho/2), u = eps_n exp(k_n T^rho/2) T^{1/2}(1+S),
S = sum_{i=1}^{n-1} eps_i exp(k_i T^rho/2). Each exp = 1 mod Lambda_+.
For odd n=2m+1, n-1=2m even, S = even integer mod Lambda_+, so 1+S = odd integer mod Lambda_+.
Hence 1+S is a unit (valuation 0), so val(u_crit)=1/2 always, never s>1/2.
Checks all 2^(n-1) sign choices for n=3,5,7 and spin-flip generalization.
"""
import itertools

def check(n):
    assert n % 2 == 1
    for signs in itertools.product([1, -1], repeat=n - 1):
        S0 = sum(signs)  # leading term of S
        assert (S0 % 2) == 0, (n, signs, S0)
        assert (1 + S0) % 2 == 1 and (1 + S0) != 0, (n, signs, S0)
    return True

for n in [3, 5, 7]:
    check(n)
    print(f"n={n}: all {2**(n-1)} sign choices give 1+S odd nonzero -> val(u)=1/2")

# spin-flip generalization: coefficients p_i = +/-1 from spin structure
for n in [3, 5]:
    for pm in itertools.product([1, -1], repeat=n - 1):
        for signs in itertools.product([1, -1], repeat=n - 1):
            c = 1 + sum(a*b for a, b in zip(pm, signs))
            assert c % 2 == 1 and c != 0
print("spin-flip generalization: 1 + sum p_i eps_i always odd/nonzero for odd n. No-go holds.")
