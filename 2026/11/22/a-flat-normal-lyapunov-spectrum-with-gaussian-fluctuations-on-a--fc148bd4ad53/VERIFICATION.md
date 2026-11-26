---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Independent reconstruction: writing y=N−1/2 gives y'=y+8(1/4−y²)y=3y−8y³, hence z'=3z−4z³. Haar measure for T(t)=3t+π projects by z=cos t to the ergodic arcsine law (mixing follows first on Fourier modes by escape of frequencies). The derivative normal to the axis as a quotient is ∂P'/∂P=1+h(N−m)=A+2z; ∂P'/∂N=0 at P=0. The proof's prose reverses the label of the off-diagonal entry, but its quotient and formulas are correct. The integral is the circle mean of log|w²+Aw+1|: Jensen contributes log max(1,|root|) for each root. Both roots have modulus one for |A|≤2, including the double-root endpoints, and otherwise only one contributes. Birkhoff applies for each fixed m; zero-multiplier seeds and their finite-level preimages form a countable null set. At A=0 the centered L² logarithm φ has cosine coefficients (−1)^(r+1)/r at frequency 2r. Averaging over the three inverse branches gives Pφ=φ/3 because division of compatible frequencies preserves coefficient sign and the π translation gives phase 1. Thus lag k covariance is 3^(−k)||φ||²=π²/(12·3^k); summing gives the stated variance (at n=1 it gives π²/12). With ψ=φ−φ∘T/3, Pψ=0 and ||ψ||²=(8/9)||φ||². For the reversed differences the row quadratic variation is an ergodic average of E(ψ²|T^(−1)B) along T; the expected normalized conditional Lindeberg sum is E[ψ² 1{|ψ|>ε√n}]→0. The telescoping endpoint term is uniformly L²-bounded, giving the claimed π²/6 Gaussian variance. This is an ensemble normal-quotient law on the real invariant interval, not a fixed-seed CLT or positive-population assertion. Read the included verifier as evidence; the reconstruction does not depend on running it.

## originality

PASS

Best of knowledge, for the exact source-map locus and its quantified normal law only. The Fourier and martingale mechanisms are classical, and the known doubling calculation uses precisely the same centered logarithmic cosine observable, not merely a similar one. The odd arithmetic changes the correlation sign and removes the cancellation, and the exact parameter/cocycle identification in the Hong–Zhang map was not covered by the sources inspected.

## value

PASS

The tuned midpoint is intrinsic to the mortality plateau: the linear normal multiplier there is centered on the symmetric invariant interval. The exact finite-time correction and positive diffusive variance quantify a distinction lost by the Lyapunov exponent, with a concrete contrast to bounded logarithmic amplitudes in the classical degree-two derivative case. The invariant interval is not wholly biologically admissible; value here is an exactly solved normal cocycle for real dynamics, not evidence of predator invasion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
