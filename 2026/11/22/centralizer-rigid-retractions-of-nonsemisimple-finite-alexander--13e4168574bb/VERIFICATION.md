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

# Reproduction of the mathematical checks

Run `python3 verify.py` with Python 3. The checker constructs each truncated-polynomial ring, exhaustively enumerates matrices for five small parameter cases, tests \(A^2=A\), identifies the rank modulo the radical and tests \(BA=AB\) independently for each displayed rank. It checks the affine translation factor, as well as complete quandle set-map homomorphisms for three- and five-element cases. For the nine-element case the explicitly verified quandle generation by \(0,1\) bounds the number of homomorphisms by \(9^2\), attained by the exhibited and directly tested affine maps, so no untested set maps remain. Finally the mixed-block commutation dimensions are obtained by finite-field Gaussian elimination rather than the claimed closed formula.

Expected final line: `JORDAN_ALEXANDER_RETRACTIONS_CHECKS_PASSED`.

Mathematical limits: the finite checks do not verify the theorem in arbitrary dimension; that follows from the proof in RESULT.md. This is a reproducibility record, not an independent mathematical audit.
