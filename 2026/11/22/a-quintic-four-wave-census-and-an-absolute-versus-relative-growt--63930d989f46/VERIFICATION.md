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

# Reproducibility

The theorem follows from the explicit local phase-successor condition and the 16-state/9-state rim transfer construction, not from finite sampling. `checks/verify_transfer.py` recomputes both integer characteristic polynomials by Faddeev–LeVerrier and verifies their Cayley–Hamilton matrix equations before computing exact traces. `checks/verify_direct.py` implements the original four-state update separately and checks every one of the \(4^{n+1}\) initial configurations for each \(3\le n\le8\), classifying period-one, period-two and primitive period-four states. Results agree with the theorem: primitive four-state populations are \(24,80,200,480,1232,3024\), respectively. The included code is finite and makes no external validation claim. Asymptotic root inequalities and all-length generating identities are proved mathematically in RESULT.md; neither a failed computation nor a finite cutoff is treated as an infinite proof.

The all-rest fixed state is not included in primitive four-orbit counts. No claim is made about eventual attraction basins, or exclusion of other long temporal periods. The 1978 original article's full text could not be accessed; historical priority remains qualified.
