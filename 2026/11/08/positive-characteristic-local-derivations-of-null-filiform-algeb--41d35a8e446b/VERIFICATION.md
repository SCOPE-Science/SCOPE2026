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

Run `python3 verify.py` with Python 3.9 or newer; the script uses only the standard library. It ends with `VERIFY_OK` on success. It checks finite fields \(\mathbb F_2\) and \(\mathbb F_3\), dimensions one through five as specified in the script, and includes two logically different checks.

First, every structurally permitted coefficient matrix in the tested cases is enumerated, with rank computed by finite-field Gaussian elimination and compared against the independently evaluated descending-column recurrence and maximal-rank product. Second, when the total vector space of all linear maps is small enough (at most one million matrices), *all* linear maps are enumerated, and each is tested on every algebra element against the set of outputs of every ordinary derivation. Only the proposed matrices satisfy the literal local condition.

Representative exact results: \(n=3,q=2\) yields rank histogram \((1,9,6)\) out of 16; \(n=4,q=2\) gives \((1,21,42)\) out of 64; \(n=4,q=3\) gives \((1,176,2928,3456)\) out of 6561; \(n=5,q=2\) gives \((1,49,294,168)\) out of 512. The script's direct local checks include the small-dimensional cases over both prime fields.

This finite verification does not test every prime power, dimension, or element of an infinite family. The proof for all \(q=p^f\) and \(n\ge1\) is in RESULT.md. It does not constitute external validation or establish literature priority.
