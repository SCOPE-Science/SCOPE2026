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

# Mathematical verification

The exact rational-arithmetic Python 3 program `verify_zariski.py` uses only the standard library, computes the intersection pairings in the basis of a pullback line and exceptional classes, and checks each constructed \(D_r=P_r+N_r\), its big counterpart, the negative definiteness of the specified support, and the nef intersection inequalities. The verifier checks all \(2\le n\le24\), as well as the chamber-support count and least common multiple; output is stored in `verification_output.txt` with final line `VERIFY_OK`.

The finite computation is corroboration, not an infinite proof. The general argument in `RESULT.md` uses the Bézout inequality, classification of the complete cone of negative curves, a Schur-complement calculation for mixed supports, exact orthogonality, and a family of explicit all-\(r\) effective/big witnesses. It is valid over every algebraically closed field with distinct proper collinear blow-up points. No external independent audit has taken place. Historical priority of the complete spectrum and universal clearing integer remains conditional on further specialist literature review.
