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

The complete parameter proof is given in `RESULT.md`, Steps 1–8. The reproducible standard-library program `reproducibility/check.py` was run on seven finite parameter pairs with no external libraries. It checks the predicted composition-centralizer spectrum, exact image-order counts, retractions, and the number of automorphism-conjugacy classes, as well as the equality between the summed spectrum and the ordered commuting-pair count.

For \((p,r)=(7,3),(13,3),(13,4),(13,6)\), all maps were independently evaluated as functions on the actual semidirect product; the group-homomorphism property was exhaustively tested on all ordered pairs of group elements, and the commuting relation was also compared against full function composition for every pair of maps. Three further cases including the composite complement \(r=15\) checked the derived complete parameter composition algebra. Saved exact output is included in `reproducibility/check-output.txt`, ending `FROBENIUS_ENDOMORPHISM_CENTRALIZER_CHECKS_PASSED`.

The code is a finite independent check of the written formulas, not an infinite proof and not an independent mathematical audit. No assertions are made about the full generality of the result based only on these samples. Scientific limitations and historical-priority risks are in `RESULT.md` and `REVIEW.md`.
