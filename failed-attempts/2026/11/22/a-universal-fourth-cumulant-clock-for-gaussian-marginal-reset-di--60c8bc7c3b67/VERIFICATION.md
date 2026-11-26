---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

At positive lag the event of no refresh has probability p=e^(−rt) independent of X0. Conditional on it, the vector pair is jointly centered Gaussian with cross-covariance B=Σexp(−Aᵀt); after at least one refresh, X0 and Xt are independent. Stationarity gives C=pB and cancels the terminal conditional covariance in the within-time Wick pairing. Thus subtracting the unconditional pairings leaves (p−p²)(B_ik B_jl+B_il B_jk), as claimed. C is invertible, so the two C-inverse contractions are d² and d, proving the logarithmic inversion and a strictly positive squared-probe witness for a pair with uᵀCv≠0. The stationary adjoint equation makes the refresh density a quadratic times the Gaussian. Nonnegativity along rays implies Q=(AΣ+ΣAᵀ)/2−D is positive semidefinite, so the matched Gaussian OU twin with drift matrix A+rI and diffusion D+Q+rΣ is admissible. The explicit isotropic positive quadratic density integrates to one, satisfies the stationary equation and is non-Gaussian when the chosen δ>0; a reset couples different starts, so the invariant law is unique. The result concerns exact ensemble moments, not estimation from one trajectory segment. The supplied scalar polynomial-generator and 2D conditioning checks were inspected, not executed; the proof is not dependent on them.

## originality

FAIL

The claimed tensor and rate inversion are mechanically covered as consequences of the earlier exact transition-function theorem for arbitrary Markov processes with independent fixed-distribution restart. Its assumptions include non-Gaussian vector refreshes without any extra premise. With the separately known feasibility and covariance of Gaussian stationary targets, only ordinary Gaussian pairings and matrix contractions remain. This is established stronger-result coverage, not a failure based on an unavailable exact-phrase match.

## value

FAIL

The observable is physically interpretable and is a useful way to illustrate the distinction between Gaussian marginals and Gaussian temporal laws. As the asserted scientific advance, however, it is a routine linear/quadratic moment evaluation of a known exact kernel with a scalar inversion already exemplified in equilibrium rethermalization. The contraction repackages that scalar ratio; it adds no new identifiable regime beyond the direct kernel calculation, no inferential guarantees, and no independent nonmechanical result that could survive a narrower claim here.

The dated certificate retains the supplied scientific assessment, sources and limitations.
