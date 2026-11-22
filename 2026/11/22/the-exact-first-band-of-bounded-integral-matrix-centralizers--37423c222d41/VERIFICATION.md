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

# Direct finite checks and limits

The included `edge_checker.py` runs without dependencies beyond the standard Python library, using exact integer and rational arithmetic. It exhaustively checks commutation against the parametrized formula for all 3107 matrices in the boxes \(H\in\{1,2,3\}\). Across 35 combinations \(H=1,\ldots,7\) and \(z\in\{2,5/2,3,7/2,4\}\), it checks the cumulative event against both the direct primitive-gcd count and a separate Möbius inversion implementation. Its success line is `CENTRALIZER_EDGE_OK 3107 35`; the implementation also prints three larger samples for \(H=50,100,200\) at \(z=3\).

These finite tests are not a certificate for infinitely many \(H\). The proof in `RESULT.md` independently supplies the exact parametrization, forcing of the first band, arithmetic-progression estimate, and absolute-series bound necessary for the uniform asymptotic. No independent audit or external certification is claimed.
