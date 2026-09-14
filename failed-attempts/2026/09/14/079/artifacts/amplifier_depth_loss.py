"""Bounded recovery test: target exponent 5/24 vs known depth exponent ~1/4,
and amplifier gain-vs-depth-loss model for N = p^{4n+2} (p=3,5; n=1..6)."""
import math

def report(p):
    print(f"p = {p}")
    print(f"{'n':>2} {'N':>10} {'N^(5/24)':>10} {'N^(1/4)':>10} {'ratio N^(1/24)':>14} {'local peak N^-1/4':>17}")
    for n in range(1, 7):
        N = p ** (4 * n + 2)
        t = N ** (5 / 24)
        k = N ** 0.25
        print(f"{n:>2} {N:>10} {t:>10.3f} {k:>10.3f} {k/t:>14.3f} {N**-0.25:>17.6f}")
    print()
    # Amplifier model: gain L^{1/2} with L=(N lam)^d, d=0.1; depth loss ~ p^{2n}=N^{n/(4n+2)}~N^{1/4}
    lam = 1e6
    d = 0.1
    print(f"  amplifier model d={d}, lambda={lam:.0e}:")
    print(f"  {'n':>2} {'gain L^1/2':>12} {'depth loss':>12} {'net':>10}")
    for n in range(1, 7):
        N = p ** (4 * n + 2)
        gain = (N * lam) ** (d / 2)
        loss = float(p ** (2 * n))
        print(f"  {n:>2} {gain:>12.3f} {loss:>12.1f} {gain/loss:>10.2e}")
    print()

for p in (3, 5):
    report(p)
print("Conclusion: target beats known 1/4 exponent by unbounded factor N^{1/24}; "
      "fixed-d amplifier net gain < 1 for all n>=1 and decays with n.")
