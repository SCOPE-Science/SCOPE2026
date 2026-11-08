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

Run `python3 CHECK.py` in an ordinary Python 3 installation. The script uses only the standard library. Its output is provided verbatim in `CHECK_OUTPUT.txt` and terminates in `VERIFY_OK`.

It checks \(2^{mn}-1\) nonempty subsets and the pairwise product identity for five finite dimension pairs; tests the inclusion-exclusion fiber sizes; tests deterministically sampled **noninvertible and invertible** endomorphisms by exact exhaustive multiplication tables; and checks the complete sum over \(729\) pairs of support maps when \(m=n=2\), obtaining \(9\,530\,217\). It does not enumerate all endomorphisms by brute force, and cannot prove the universal claim for all \(m,n\). The universal result is proved in `RESULT.md`.

The endomorphism composition/idempotence formula follows from composition of the independently chosen support/fiber maps, and is not asserted to have undergone an independent external audit.
