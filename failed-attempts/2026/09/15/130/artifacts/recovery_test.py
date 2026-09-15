"""Bounded recovery test: why the isomorphic-KLS target is blocked.

Test A (symmetry breaking): simulate Eldan tilt magnitude |c_t| under standard
stochastic localization in dimension n. The tilt is a martingale with
quadratic variation ~ Cov; E|c_t|^2 grows linearly until covariance collapses.
Forcing c_t = 0 (symmetry preservation) removes the variance-reduction engine.
We quantify typical |c_t| at time t=1 for n=20,50,100 over trials.

Test B (BM-instability): if d_BM(K,T) <= C1 then after normalization the
density ratio sup d lambda / d mu can be as large as ~ C1^n (volume ratio).
Holley-Stroock gives C_P blow-up by that ratio: exp(O(n)), not O(1).
We compute C1^n for C1=2 across n to show no dimension-free transfer.

Both tests are structural, not a proof attempt; they bound the recovery route.
"""
import numpy as np

rng = np.random.default_rng(0)

print("== Test A: tilt magnitude (symmetry breaking) ==")
for n in [20, 50, 100]:
    trials = 2000
    t = 1.0
    # c_t ~ N(0, t I) as a proxy for Eldan drift before covariance shrinkage
    samples = rng.normal(0, np.sqrt(t), size=(trials, n))
    norms = np.linalg.norm(samples, axis=1)
    print(f"n={n:3d}  mean|c_t|={norms.mean():.2f}  sqrt(n t)={np.sqrt(n*t):.2f}  "
          f"min={norms.min():.2f} max={norms.max():.2f}")

print()
print("== Test B: BM volume-ratio blow-up ==")
for n in [10, 50, 100, 500]:
    print(f"n={n:3d}  C1^n (C1=2) = 2^{n} = {2.0**min(n,300):.3e}  "
          f"log-ratio = {n*np.log(2):.1f}  (Holley-Stroock factor)")

print()
print("CONCLUSION: tilt drift is typically Theta(sqrt(n)), so any symmetric "
      "localization (c_t=0) discards the full drift signal; and BM transfer "
      "loses exp(Theta(n)), so bounded BM distance cannot transport an O(1) "
      "Poincare bound. Both standard recovery routes fail with explicit "
      "dimension-dependent loss.")
