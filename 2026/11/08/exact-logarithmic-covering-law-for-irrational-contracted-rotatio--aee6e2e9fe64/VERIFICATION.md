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

# Verification record

**Analytic proof checks:** Two branch image hulls are separated by \(1-\lambda\). If final branch differs, the gap is at least this value. With a common final branch, distances between disjoint predecessor atoms are multiplied by \(\lambda\), yielding the uniform \(n\)-atom gap. Irrational Sturmian coding supplies \(n+1\) atoms intersecting the Cantor component; each has diameter at most \(\lambda^n\). The inequalities in RESULT.md then yield the claimed additive-error logarithmic law.

**Finite reproduction:** Run `python3 CHECKER.py` with Python 3 standard library. This checks a golden irrational rotation with \(\lambda=1/2\) at 105 decimal digits over generations 1–18 and is **not** an infinite-parameter proof. The output is `CONTRACTED_ROTATION_STURMIAN_ATOMS_OK n=1..18; last_atoms=19`.

**Unproved and external limits:** Other irrational parameters are covered by the analytic argument, not by this finite check. No independent audit has been performed. No exact additive constant, rational-mode-locking classification, or publication-priority certificate is asserted.
