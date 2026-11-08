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

# Direct reproducibility

Run `python3 verify.py` with standard-library Python 3; no third-party packages are required. The verifier constructs each middle graph from its root independently of the mathematical proof. It enumerates every selected set and compares ordinary domination and semitotal domination, then checks the coefficient sequence against a separately computed edge-subset polynomial. It covers all connected labeled simple roots of orders 3–5 (4, 38, and 728 cases), plus 114 connected rooted instances on 6 vertices and 120 on 7 vertices. It exhaustively enumerates every candidate minimum-size set of middle paths and cycles for orders 3 through 12, comparing against the exact stated classifications. It also checks the connected two-vertex exception.

Observed output ended with `GENERAL_CONNECTED_ROOTS_OK {3: 4, 4: 38, 5: 728, 6: 114, 7: 120} 1004`, the path/cycle lines concluding `MINIMUM_CLASSIFICATION_OK cycle 12 6 2`, `SHARP_TWO_VERTEX_BOUNDARY_OK`, and `VERIFY_OK`.

The implementation samples rather than exhausts all connected roots of orders 6–7, and stops the complete path/cycle comparison at order 12. Accordingly these finite tests are not an infinite proof. The proof in `RESULT.md` supplies that unrestricted argument. No independent mathematical audit or external certification has been performed.
