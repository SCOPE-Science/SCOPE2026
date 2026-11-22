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

# Reproducible checks and limitations

Execute `python3 check_hardy.py` with a standard Python 3 installation. The checker passed 188 assertions for exact rational-polynomial cancellation and numeric quadratures/root brackets. It does not certify the infinite mathematical statements by finite enumeration: those follow from the written measure representation, Gamma identity, monotonicity proof, and asymptotic estimates.

The exact symbolic cancellations tested are \(P_m-P_m'=S_{m-1}^2\) for the incomplete-Gamma polynomial representation of the single-jump squared error, and the polynomial derivative identity for the cumulative root equation. The numerical tests compare independent root and norm expressions and sample iteration indices. Boundary behavior \(L=0\) and \(L\to\infty\) is proved in the text, not inferred from a finite cutoff.

No independent mathematical audit has been performed. No numerical experiment is presented as a uniqueness proof or an asymptotic certificate.
