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

The proof establishes the claimed universality, critical-length necessity, and sharp onset for every integer \(t\ge2\). The independent literal-deletion implementation in `verify.py` covers \(60\) construction parameter pairs (\(27113\) deletion masks), \(4461\) exhaustive critical source words (\(44358\) masks), and the separate quaternary two-deletion diagnostic at lengths \(5,6,7\). The run returned `VERIFY_OK`; the exact output is included as `verification_output.txt`.

Run `python verify.py` with a standard Python 3 interpreter. Enumeration is finite corroboration; only the symbolic cyclic-arc collision lemma and unique-marker proof yield the all-length theorem. No external, formal, or independent mathematical audit has been performed.
