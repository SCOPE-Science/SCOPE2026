from math import gcd


def primes_upto(n):
    primes = []
    for x in range(2, n + 1):
        if all(x % p for p in primes if p * p <= x):
            primes.append(x)
    return primes


def rank_and_period(modulus):
    a, b = 0, 1
    rank = None
    n = 0
    while True:
        if n > 0 and a == 0 and rank is None:
            rank = n
        if n > 0 and a == 0 and b == 1:
            return rank, n
        a, b = b, (a + b) % modulus
        n += 1
        if n > 6 * modulus * modulus + 10:
            raise ValueError(f"search bound exceeded for modulus {modulus}")


checked = []
for q in primes_upto(200):
    if q in (2, 5):
        continue
    z, period = rank_and_period(q)
    z2, _ = rank_and_period(q * q)
    wall_sun_sun = z2 == z
    if wall_sun_sun:
        assert z2 == z
    else:
        assert z2 == q * z
        assert gcd(z2, period) == z
        assert period % q != 0
    checked.append((q, z, period, z2, wall_sun_sun))

q = 3
z, period = rank_and_period(q)
z2, _ = rank_and_period(q * q)
flags = []
for j in range(1, 13):
    m = j * period
    flags.append(int(m % z2 == 0))
assert flags == [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1]

print(f"checked_primes={len(checked)}")
print("all_non_WSS_rank_lifts_and_gcd_identity=OK")
print(f"q=3: z(q)={z}, pi(q)={period}, z(q^2)={z2}")
print(
    "q=3, class 0 mod pi(q), q^2-divisibility flags for first 12 terms:",
    "".join(map(str, flags)),
)
