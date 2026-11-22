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

# Verification and limits

Run from a directory containing the script with `python3 VERIFY.py`. The checker uses only the Python standard library and is deterministic. It evaluates an exact integer Sylvester determinant and verifies the complete common-root sets modulo \(5\) and \(11\), plus the absence of simultaneous zeros modulo \(25\) and \(121\). It independently computes fifth-index binomial transforms for \(1\le k\le50\), checks exact gcds over all bases \(-500\le b\le20000\), and verifies that the gcd-residue sequences have least periods \(55\) and \(20\) with the stated multiplicities.

The general result depends on the finite-field argument and prime-power exclusion proved in `RESULT.md`; no finite computational bound is extrapolated into an infinite theorem. The proof does not address indices other than five. External independent audit has not been performed.
