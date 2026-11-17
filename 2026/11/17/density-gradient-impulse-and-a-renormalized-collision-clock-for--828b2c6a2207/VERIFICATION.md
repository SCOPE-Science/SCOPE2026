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

# Verification notes

The analytical verification consists of the five steps in RESULT.md. The boundary assumptions explicitly exclude rod endpoints; positivity makes the transverse acceleration point inward; \(C^1\) regularity makes the subtractively renormalized potential finite and makes the tangential acceleration logarithmic. Conservation of energy identifies the radial speed's \(O(1)\) constant. Integration of the reciprocal radial speed identifies the subleading clock coefficient; integration of the axial acceleration gives both axial correction limits. No other-run numerical or source artifact is needed.

For a finite, separately reproducible check, execute `python check_impact.py` using NumPy and SciPy. It verifies the elementary exact potential/force expressions against quadrature for four interior configurations; it also uses a trajectory integrated in the logarithmic radial coordinate to compare the predicted finite-part energy constant and the tangential logarithmic acceleration at four increasing log-radius scales. Expected output starts with `VERIFY_OK`. This only checks finite instances and approximate calculations, not the universal asymptotic claims or historical priority.

The novelty comparison used the full available text of the motivating variable-density paper and the earlier linear-density manuscript. Abstract-only access to Alberti–Vidal (2010) is insufficient to exclude all possible implications of that paper. No independent audit has been performed.
