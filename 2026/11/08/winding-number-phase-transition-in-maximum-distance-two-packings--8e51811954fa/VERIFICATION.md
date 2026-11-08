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
The mathematical proof gives a complete cyclic-gap encoding, a closed three-coloring count, a sign-swap connectivity argument for even orders, and a constructive gap-transfer argument for odd orders. These establish the infinite statement.

The bundled `check_direct.py` independently constructs Cartesian distances between all \(3n\) vertices, enumerates each size-\(\lfloor n/2\rfloor\) candidate for \(5\le n\le11\), then constructs the entire legal slide graph. The bundled `check_gaps.py` uses the derived but independently implemented gap encoding to enumerate every maximum state and legal move for \(5\le n\le19\). All tests reproduce the exact predicted counts and component profiles. Inspect `direct.log` and `gaps.log` for full results. Run with `python3 check_direct.py` and `python3 check_gaps.py` using standard Python 3 only.

Computational enumeration stops at the stated finite orders; no inference of universal truth is made from those runs. The published three-color winding obstruction predates this finding, which concerns its exact packing interpretation and the odd-versus-even reconfiguration transition. No independent verification or audit has been conducted.
