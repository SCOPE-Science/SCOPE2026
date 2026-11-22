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

# Reproduction and verification

Execute `python3 VERIFY.py` with a standard Python 3 installation. The script uses `math.comb` and an exact integer-partition recursion; no external packages, input files, networking or datasets are required. The expected final line is `VERIFY_OK`, and the exact recorded output is supplied in `VERIFY_OUTPUT.txt`.

The checker uses two distinct finite calculations: an integer-partition/binomial-formula enumeration through order 16 and an explicit relational extension-state enumeration through order 8. It enumerates 914 unordered integer partitions through order 16, identifies the unique failing profile at order 16, checks the witness through order 100, and verifies the early-rise implication of the proof on every enumerated profile.

These runs cannot establish completeness beyond the finite test range. That is supplied by the exact type correspondence and combinatorial inequalities in `RESULT.md`. There is no claim of formal verification or third-party certification.
