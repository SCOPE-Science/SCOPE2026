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

# Verification of the stated theorem

Run `python3 checker.py` with Python 3. No external dependencies are needed.

The checker independently enumerates every distinct one-symbol supersequence of every root-doubled word over alphabets of sizes two through four in the declared finite ranges. It checks every inverse-list size, both positive histogram cells, the exact rotation-confusability edges, and the maximum independent-set sizes and multiplicities on every rotation orbit. The final line must be `VERIFY_OK`. This calculation checks finite examples only; it cannot establish formulas for arbitrary \(q\) and \(m\). The all-parameter proof is in `RESULT.md`.

No independent mathematical audit has been conducted.
