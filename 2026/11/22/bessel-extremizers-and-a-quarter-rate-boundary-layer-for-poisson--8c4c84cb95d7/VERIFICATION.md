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

# Verification

The embedded `checker.py` is executable with Python 3 and `mpmath`; it tests the exact Bessel-kernel integral against a separately summed Poisson mixture of classical Hardy-power jump errors. At 45-digit working precision it returned `PASS 108 numerical comparisons`, including six positive Poisson parameters and three large-time values.

The proof in `RESULT.md` establishes the signed-measure reduction, unique Bessel-defined maximizing jump, equality classification, and both asymptotics with an explicit dominating envelope. The finite computational checks do not certify the asymptotic theorem or completeness of historical search. No independent mathematical audit has been performed.
