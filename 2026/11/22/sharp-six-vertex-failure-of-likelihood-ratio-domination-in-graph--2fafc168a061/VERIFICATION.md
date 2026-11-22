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

The package contains `checker.py`, a standalone Python 3.10+ exact-rational certificate. Run `python3 checker.py` in the extracted directory. It enumerates every labeled simple graph on one through five vertices using all \(2^{\binom n2}\) edge masks; it verifies all 772 neighboring-support likelihood-ratio cross products, and independently compares sequential recursion against direct enumeration of all priority orders in each of the 1,099 graph cases. It checks the sharp six-vertex example with exact fractions and the predicted family formula for fourteen further parameters. All these checks completed successfully at preparation.

The infinite family statement is justified symbolically in `RESULT.md`; fourteen computations do not constitute its proof. The five-vertex universal statement is covered by a complete finite certificate, not a sample. The finite enumeration depends on the correctness of the clearly stated graph-generation, independence, maximality and recursion algorithms; code has not been independently audited. Historical priority has not been independently established.
