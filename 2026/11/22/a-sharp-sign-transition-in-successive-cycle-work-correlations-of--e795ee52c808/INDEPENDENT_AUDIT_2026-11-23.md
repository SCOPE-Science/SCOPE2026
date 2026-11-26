# Independent mathematical audit

## correctness

PASS

Independently obtained Y_n=B_n−hε_(n−1) by resetting the relative displacement, not the active force. For lag ℓ≥1, the disjoint force integrals factor into the product of (1−exp(−(a+b)τ))/(a+b) and the positive integral of exp(−a(τ−v)−bv) on [0,τ], times A² exp(−b(ℓ−1)τ)/γ². The second integral is (exp(−bτ)−exp(−aτ))/(a−b) and gives τexp(−aτ) at resonance. Isserlis applied to the four terms of (Y_n²−ε_n²)(Y_(n+ℓ)²−ε_(n+ℓ)²) gives κ²[K²exp(−2b(ℓ−1)τ)−h²σ⁴ 1_{ℓ=1}]/2. Thermal integrals on distinct cycles are independent. Rescaling by h shows the adjacent sign is that of (A²/γ²)G−σ². G is a product of strictly increasing positive factors, with the equal-rate limit given in the record. Its range is (0,∞) if b≤a and (0,1/(b²−a²)) otherwise, proving the strict threshold and uniqueness. The amplitude equality when b>a gives no finite zero, as the theorem and proof explicitly state; the nearby phrase 'equality produces a single zero' must mean equality in the equation for the crossing period. For a=γ=κ=1, b=2, σ²=1, A²=6, the rescaled ratios to σ² at τ=log 2 and log 4 are 7/8 and 189/128, independently witnessing both signs. RESULT.md, VERIFICATION.md and verify.py were inspected; the uploaded script was not run and has no explicit exact-amplitude-equality test. The proof, not finite diagnostics, establishes the statement. The result is restricted to independent centered Gaussian noises, full shift, and stationary cycle statistics.

## originality

PASS

The closest inspected model contains the dynamical protocol but treats expectation and power. Marginal work fluctuations and the continuous-time active-work covariance in the closest indexed finding are different observables. No inspected result gives or immediately specializes to the full discrete lag hierarchy with its strict period-switch criterion; this is a bounded best-of-knowledge decision, not a priority claim.

## value

PASS

A one-cycle work law cannot distinguish anticorrelation of neighboring cycles from positive long-lag dependence. The exact all-lag result identifies two separately interpretable sources of serial variation and gives a strict, experimentally meaningful boundary for whether changing period alone can reverse the adjacent sign. It also separates thermal-noise effects on the marginal variance from the cross-cycle mechanism. This is a complete classification of a natural established protocol, without claiming behavior outside gain one or Gaussian bath assumptions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
