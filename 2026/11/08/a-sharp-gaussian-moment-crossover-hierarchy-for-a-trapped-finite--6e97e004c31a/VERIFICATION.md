---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Mathematical verification and boundaries

The standalone standard-library script `check.py` recomputes the moment recurrence using all three stationary internal-state generator equations in exact rational arithmetic. It then compares that recurrence against the closed moment product at multiple rational rate pairs through order \(24\). Further diagnostics evaluate the exact fourth-moment crossing, locate the unique Gaussian-normalized crossing numerically at selected higher orders, and compare the critical rate against its high-order asymptotic law. The replayed script reports **206 finite diagnostic assertions passed**.

The proof of monotonicity is the strict decrease of \(R/[x(x+R)]\) in \(x>0\), applied factor by factor; this yields a true all-order statement without numerical enumeration. The singular asymptotic derives from uniform gamma-ratio expansions with \(T=c/n\), then a log-ratio root equation. Finite numerical checks corroborate these identities but do not prove uniqueness or infinite-order convergence.

The exact moment product and stationary characteristic function belong to the previously published source. No independent scientific audit, empirical finite-sample certification, multidimensional generalization, or simultaneous varying-\(R\) asymptotic is claimed.
