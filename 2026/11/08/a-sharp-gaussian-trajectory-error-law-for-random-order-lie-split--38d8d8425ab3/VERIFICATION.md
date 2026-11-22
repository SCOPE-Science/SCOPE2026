---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-19.md",
      "INDEPENDENT_AUDIT_2026-11-19.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The correct local Taylor coefficients give M_±(h)=E(h)±h²[A,B]/2+O(h³) in every finite-dimensional norm. An exact noncommutative subset expansion about E=e^{h(A+B)} bounds all ≥2 perturbation terms by O(n²h⁴ exp(O(nh²)))=O(h²) uniformly in signs and higher-order single-step terms by n O(h³)=O(h²). Hence the exact product error equals (h²/2)Σ ε_j E^{n-j}[A,B]E^{j-1}+O(h²) uniformly. Dividing by h^(3/2), the remainder vanishes and the coefficient array is bounded O(sqrt(h)); its independent centered signs satisfy the Cramér–Wold/Lindeberg CLT with covariance (1/4)∫vec(e^{(T-s)C}Ke^{sC})vec(...)^T ds, including singular support. Orthogonality gives the exact leading Frobenius second moment; an O(h²) L² remainder contributes o(h³). Invertible matrix exponentials show positivity iff K≠0; commuting generators yield exact equality for every path. Sign symmetry and local cancellation also give O(h²) mean difference. For oscillator A=[[0,1],[0,0]], B=[[0,0],[-1,0]], C is skew and K=diag(-1,1), so G(s) has squared Frobenius norm 2 for all s and T=1 gives exactly 1/2. Independently recomputed covariance by a 4-vector/16-second-moment transfer rather than executing submitted check.py, including a nonnormal matrix pair: oscillator normalized risks n=8,16,32,64 were 0.5072623814,0.5035147300,0.5017415971,0.5008687525, while the integral is 0.5; for a nonnormal pair the integral trace was 9.11305153335 and direct exact second-moment transfer converged toward it. Finite checks corroborate but do not prove the all-n statement.

## originality

PASS

Best-of-knowledge: Zhang Algorithm 2 and Childs–Ostrander–Su §2 precede the fair forward/reverse Lie algorithm, its local commutator cancellation on averaging, and its mean-order benefit. Berger proves general near-identity random-matrix product CLTs, including stochastic Lie–Trotter formulas, and closely related 2026 published results give h^(3/2) commutator Gaussian covariance for *paired implicit Euler*, with deterministic O(h) bias and restricted positive-semidefinite matrices. The inspected statements do not imply the asserted full random-matrix Gaussian defect and exact Frobenius risk for independent explicit exponential forward/reverse products at h^(3/2) scale: this requires the separate centered-error expansion around e^{T(A+B)}. No exact dominating coverage identified, but general stochastic product CLTs may imply it under an as-yet-unworked reduction; priority is not certified.

## value

PASS

The fundamental numerical-analysis question is whether a randomized first-order splitting whose ensemble mean has second-order accuracy is second-order for a single realization; the result proves no, generically its RMS defect is sharp h^(3/2). The matrix-wide nonzero-if-and-only-if commutator criterion, explicit propagated covariance and exact Frobenius risk coefficient quantify the distinction for arbitrary finite-dimensional real matrices without stability assumptions; the harmonic oscillator supplies a natural concrete benchmark. The fact is not merely a small numerical improvement or a renamed finite example, while the old random-order algorithm and basic CLT/commutator techniques are explicitly credited as prior. No optimality among randomized schemes or extension to infinite-dimensional problems follows.

The dated certificate retains the supplied scientific assessment, sources and limitations.
