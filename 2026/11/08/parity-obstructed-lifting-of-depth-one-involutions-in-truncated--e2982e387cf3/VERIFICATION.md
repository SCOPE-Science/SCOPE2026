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

Run `python check.py` with Python 3 standard library only. The included `checked_output.txt` is the actual captured output of this program. The checker explicitly implements multiplication in binary extension fields, composes every eligible truncated series, compares the count of involutions with the theorem, and checks the next possible obstruction to lifting. Cases cover \(N=2,\ldots,10\) over \(\mathbb F_2\), \(N=2,\ldots,7\) over \(\mathbb F_4\), and \(N=2,\ldots,5\) over \(\mathbb F_8\).

These calculations verify only finite sampled fields and degrees. The theorem for all fields and degrees is proved algebraically in `RESULT.md` by the commutator-parity lemma and triangular coefficient construction. The geometric statements concern reduced schemes only.
