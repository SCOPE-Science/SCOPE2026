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

Run `python3 artifacts/verify.py` with Python 3.10+ and no external dependencies. It exhaustively enumerates named-square subsets on eleven small boards, and separately checks the formula, upper bound and explicit constructions for every board with 1–39 rows and columns. It also checks the previously known PUMaC 2010 \(6\)-by-\(6\) optimum of eight rooks in exactly 8100 ways, and prints `VERIFY_OK` only on success. The finite checks do not certify the infinite theorem; the proof is in RESULT.md. Independent audit has not been performed.
