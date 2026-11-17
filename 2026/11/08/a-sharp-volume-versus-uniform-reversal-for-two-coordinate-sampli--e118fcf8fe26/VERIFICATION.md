---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

For exact minimization over all but omitted coordinate j, the residual is (e_jᵀe)H^-1 e_j/K_jj; its energy is (e_jᵀe)^2/K_jj. Gram reduction gives λmax(Q^{1/2}GQ^{1/2}). A sign-conjugated nonnegative Gram with r=G^-1 1>0 yields universal fixed-vector Rayleigh lower bound 1/R; q=r/R attains it by positive Perron eigenvector and is unique since equality forces Wq=Wq*. For H_c, direct matrix inversion gives signed G=[[1,s,s],[s,1,s²],[s,s²,1]] and q*=(1−s,1,1)/(3−s). Closed eigenvalues show opt<uniform<determinant law for all 0<s<1, with decrement ratio 4/3 near s→1. Independently computed spectra for s=.1,.5,.9 and verified signed Gram algebra; samples are not the universal proof.

## originality

PASS

Earlier single-coordinate E-optimal sampling and multi-step volume-sampler analysis are related but use different Gram extremal eigenvalues/objectives; the frustrated signed Gram three-variable result is a different family. The specific strict opt<uniform<volume reversal on the three-variable SPD star with exact 4/3 decrement limit was not implied by the inspected sources.

## value

PASS

Volume/determinant sampling has established theoretical appeal but provably underperforms an inexpensive baseline on a natural three-variable SPD star in a precisely stated worst-direction energy metric, and the exact 4/3 limiting decrement loss quantifies a concrete design tradeoff. The signed-Gram certificate gives a motivated sufficient class for general optimal omission probabilities; no wall-clock claims.

The dated certificate retains the supplied scientific assessment, sources and limitations.
