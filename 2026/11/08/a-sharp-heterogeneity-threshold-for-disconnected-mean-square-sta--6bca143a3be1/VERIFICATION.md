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

# Verification and limitations

The standalone `verify.py` requires Python 3 and SymPy. It directly constructs the exact two-state Markov moment matrix, verifies the determinant and both discriminant factorizations, the endpoint values and triple-root cusp identities, and checks exact rational signs and isolating intervals for the stated witness. `verification_output.txt` is the captured successful output from execution against the packaged source.

The conclusion for all real heterogeneities and anti-persistence parameters is mathematical, not based on finite random sampling or checking a grid: it additionally relies on Perron–Frobenius theory for the moment matrix, the cubic sign pattern, the real-root discriminant classifications, and continuity of simple roots. No independent scientific audit has been performed; no claim is made about models outside the declared scope.
