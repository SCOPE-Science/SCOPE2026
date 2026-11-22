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

Run `python verify_path_design.py` using Python 3 standard library. The checker uses exact `fractions.Fraction` arithmetic, implements continuant recurrences and independent dense Gauss–Jordan elimination, verifies Schur-complement and Jacobi identities, and exhaustively enumerates subsets on paths of up to eleven vertices at several rational screening values. Its actual run reported **33,437 exact rational matrix and partition assertions passed**.

At \(n=6\), \(k=2\), \(\mu=1/4\), the endpoint design gives trace error \(8208/2929\); the inward design gives \(176/65\); their difference is \(18016/190385\). All numerical evidence is finite. The universal assertions rely on the analytic strict inequalities in `RESULT.md`, particularly the tail-to-interior increment comparison at \(\mu\ge1/2\). No formal proof assistant or independent auditing was used.
