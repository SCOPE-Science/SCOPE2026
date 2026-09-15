"""PPP bubble experiment: continuum-proxy quantification of the small-bubble obstruction.

Model: swallowed bubbles along a chordal exploration arrive (per unit quantum-natural
time) as a PPP with Levy intensity nu(dx) = x^{-5/2} dx on (0, M] (the 3/2-stable
peeling boundary-length jumps behind Gwynne-Miller Thm 1.2; constants omitted).
Truncate below at eta > 0 and study eta -> 0 scaling of:
  N(eps)      = #{jumps in (eta, eps]}            (microscopic bubble count)
  S_len(eps)  = sum of sizes in (eta, eps]        (total swallowed boundary length)
  S_diam(eps) = sum of sqrt(sizes) in (eta, eps]  (diameter proxy, since disk
                diameter scales as (boundary length)^{1/2})
Also N_macro(delta) = #{jumps >= delta} (macroscopic bubbles: should stay tight).

Predictions: N(eps) ~ eps^{-3/2}, S_len ~ eps^{-1/2}, S_diam ~ eps^{-1} as eta->0,
i.e. INFINITE variation: no summable route can absorb microscopic bubbles.
"""
import math
import random

random.seed(20378)

M = 1.0
T = 1.0

def rate(a, b):
    # integral_a^b x^{-5/2} dx = (2/3)(a^{-3/2} - b^{-3/2})
    return (2.0 / 3.0) * (a ** (-1.5) - b ** (-1.5))

def sample_sizes(eta, size_cap=M):
    n = random.poisson(rate(eta, size_cap)) if hasattr(random, 'poisson') else None
    return n

# random.poisson does not exist in stdlib; implement Knuth/PTRS via exponential spacings
# Instead: sample count ~ Poisson(mu) with a simple normal-approx-free sampler.
def sample_poisson(mu):
    # Knuth for small mu, normal approx for large mu
    if mu < 30:
        L = math.exp(-mu)
        k = 0
        p = 1.0
        while True:
            k += 1
            p *= random.random()
            if p <= L:
                return k - 1
    else:
        # normal approximation, round (fine for scaling-law demonstration)
        return max(0, int(random.gauss(mu, math.sqrt(mu)) + 0.5))

def sample_size_truncated(eta, size_cap=M):
    # density proportional to x^{-5/2} on [eta, size_cap]; CDF: F(x) = (eta^{-3/2}-x^{-3/2})/(eta^{-3/2}-cap^{-3/2})
    A = eta ** (-1.5) - size_cap ** (-1.5)
    u = random.random()
    return (eta ** (-1.5) - u * A) ** (-1.0 / 1.5)

def run(eta):
    mu = T * rate(eta, M)
    n = sample_poisson(mu)
    sizes = [sample_size_truncated(eta) for _ in range(n)]
    return sizes

print("eta      | N_total | N(<=0.01) | S_len(<=0.01) | S_diam(<=0.01) | N_macro(>=0.25)")
for eta in [0.01, 0.003, 0.001, 0.0003]:
    sizes = run(eta)
    small = [x for x in sizes if x <= 0.01]
    macro = [x for x in sizes if x >= 0.25]
    print(f"{eta:<9} | {len(sizes):>7} | {len(small):>10} | {sum(small):>13.3f} | "
          f"{sum(math.sqrt(x) for x in small):>14.3f} | {len(macro):>14}")

print()
print("Analytic rates (per unit time, jumps in (eta, eps]], eps=0.01):")
for eta in [0.01, 0.003, 0.001, 0.0003]:
    N = rate(eta, 0.01)
    # E S_len = int_eta^eps x^{-3/2} dx = 2(eta^{-1/2} - eps^{-1/2})
    Sl = 2.0 * (eta ** (-0.5) - 0.01 ** (-0.5))
    # E S_diam = int_eta^eps x^{-2} dx = 1/eta - 1/eps
    Sd = 1.0 / eta - 100.0
    print(f"eta={eta:<8}: E[N]={N:>10.1f}  E[S_len]={Sl:>9.1f}  E[S_diam]={Sd:>9.1f}")
print()
print("Conclusion: microscopic-bubble mass diverges (infinite variation). Macroscopic")
print("count stays O(1). Any proof must control INFINITELY many microscopic loops per")
print("unit time geometrically (uniform smallness + equicontinuity), not by summation.")
