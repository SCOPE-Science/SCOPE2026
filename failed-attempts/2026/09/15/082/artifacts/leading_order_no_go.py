"""Leading-order parity obstruction for odd-n Chekanov-type torus bulk potential.

Potential (Vianna Prop 4.5, + spin): P = u + (T/u) * B, B = sum_{i,j=1..n} s_{ij} m_{ij},
m_{ij} = w_j/w_i (w_n = 1), s_{ij} = +/-1 (spin) times a bulk unit (1 mod Lambda_+).
Constant term B_0 = sum of n^2 signs. For odd n, n^2 is odd -> B_0 is an odd integer -> nonzero.
Hence B is a unit (val 0) for ANY unit w_i, ANY spin, ANY positive-valuation bulk.
u-critical equation: 1 - (T/u^2) B = 0 -> u^2 = T B -> 2 val(u) = 1 -> val(u) = 1/2.
Weak bounding cochain needs val(u) = s > 1/2: impossible.
"""
import itertools

for n in [3, 5, 7]:
    assert (n * n) % 2 == 1
    # worst case: signs arranged to try to cancel; min |sum| over all sign choices
    min_abs = min(
        abs(sum(s)) for s in itertools.product([1, -1], repeat=n * n)
    ) if n <= 3 else 1  # for n=5,7 use parity argument directly
    # parity argument: sum of odd count of +/-1 is odd, hence nonzero
    print(f"n={n}: n^2={n*n} odd -> B_0 odd -> nonzero for every spin pattern (min|B_0|={min_abs} for n=3)")
    # valuation consequence
    print(f"  u-equation u^2=T*B with B a unit => val(u)=1/2, incompatible with s in (1/2,1)")

# n=3 exhaustive: confirm B_0 never 0 over all 2^9 spin patterns
n = 3
bad = [s for s in itertools.product([1, -1], repeat=n * n) if sum(s) == 0]
print(f"n=3 exhaustive: {len(bad)} of {2**(n*n)} spin patterns give B_0=0 (must be 0)")
assert len(bad) == 0
print("OK: leading-order no-go holds for every spin structure and every unit bulk deformation.")
