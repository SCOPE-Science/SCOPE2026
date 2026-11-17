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
# Verification details

The proof derives the arbitrary-metric bound solely from automorphism invariance and triangle inequalities and constructs a shortest-path metric attaining equality. The real \(L^1\) part follows from a layer-cake representation of absolute differences, the exact combinatorial edge-boundary formula, monotonicity of the closed real envelope, and an explicit parity-sensitive endpoint check. These analytical steps establish the universal quantifiers over all \(n\ge3\) and all permitted targets.

The reproducibility script `verify_crown_poincare.py` uses Python 3 standard-library exact rational arithmetic and breadth-first search. It checks all cuts modulo complement for \(3\le n\le8\), identifies every norming cut, verifies their predicted cardinalities, and checks all graph distances through \(n=39\). The observed terminal marker was `CROWN_POINCARE_DIAGNOSTICS_OK 125814`. The tested ranges are bounded and cannot establish the infinite theorem independently. There is no claim of independent external auditing.
