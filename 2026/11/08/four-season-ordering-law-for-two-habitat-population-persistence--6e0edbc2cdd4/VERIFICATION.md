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

# Reproduction and verification

Execute `python3 verify.py` with Python 3's standard library. It recomputes the explicit four-phase sink example using exact rational matrix arithmetic, enumerates all 24 orderings, checks all six three-phase orderings and both four-phase adjacent-swap identities, and proves strict growth/decay signs using a certified exponential-tail error bound.

The critical certificate expands each matrix exponential through order 30. For a phase generator with infinity norm at most \(15/4\), the first omitted term and subsequent geometric ratio bound give \(\epsilon=(15/4)^{31}/(31!\,[1-(15/4)/32])\). The product trace error is bounded by \(8(56)^3\epsilon<10^{-7}\). The value \(e^4<55\) used to control intermediate products is itself checked using a rational finite sum plus tail. The finite rational calculations establish strict inequalities for the example, while the exact symbolic proof in RESULT.md applies to all admissible model parameters.

No external validation or independent audit was performed. The program does not attempt to certify five or more phase schedules, asymmetric migration, or nonlinear demographic dynamics.
