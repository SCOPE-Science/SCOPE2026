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

# Verification

The file `check.py` uses only the Python standard library. Run `python check.py` from this directory.

The checker verifies 864 exact rational input/output, inverse reduction and Jacobian factorization identities for positive and negative values of \(a\) in \((-1,\infty)\); two exact cusp-cubic factorizations for \(a=2\); one exact three-preimage witness; and twelve finite numerical fold-separation asymptotic checks across both signs of \(a\). These computations do not prove the infinite theorem. The proof's global premises, monotonicity, critical point count, cusp nondegeneracy, asymptotic coefficient and properness are established analytically in RESULT.md.

No external independent verification has been performed. Literature comparisons establish inspected-scope originality only, not guaranteed publication priority.
