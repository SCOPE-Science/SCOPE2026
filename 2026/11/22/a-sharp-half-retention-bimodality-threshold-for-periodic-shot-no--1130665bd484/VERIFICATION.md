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

# Computational and analytical verification

Run `python proof_check.py` using Python's standard library. The checker reports 21,199 successful finite rational checks and reproduces strict mode indices \(1\) and \(5\) at \(q=3/4\), \(x=15/2\). It verifies finite algebraic instances, not all infinite indices or real parameters.

The full proof consists of (i) the established exact periodic-renewal MFPT expansion; (ii) the adjacent-ratio identity and strictly decreasing sequence \(F_n\); (iii) sign transitions of the ratios, including strict-boundary and isolated-tie handling; and (iv) attainment and bracketing of the global crossing minimizer. All quantifiers and boundary arguments are in RESULT.md.

No external computational dependencies, independent mathematical audit, or formal proof certificate are claimed.
