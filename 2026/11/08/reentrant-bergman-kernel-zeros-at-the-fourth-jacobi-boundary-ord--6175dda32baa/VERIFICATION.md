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

# Verification of the fourth-order Jacobi kernel classification

The proof starts from \(\|z^n\|^2=B(n+t,5)\), obtains \(K_t(s)=Q_t(s)/(24(1-s)^6)\), and applies the Cayley map \(s=(w-1)/(w+1)\). The exact first Routh column and its two sign thresholds determine the full all-parameter root count. At \(t=\tau\) a simple root lies at \(s=-1\); at \(t=2\), factorization shows a conjugate pair at \(e^{\pm i\pi/3}\). The transformed quartic at the first threshold is strictly Hurwitz stable.

To reproduce the actual algebra checks, execute `python jacobi_reentrance_check.py` with SymPy and NumPy. Observed output: `JACOBI_REENTRANCE_CHECK_PASS exact_identities=9 numerical_root_cases=8`. Exact identities check the Beta-series numerator, Routh formulas, boundary polynomial and factorizations. Eight numerical root sets check sample regimes, but do not certify all parameter values. The universal claim is justified by the displayed proof, not by numerical enumeration.

Limitations: The theorem applies to the stated disk radial weight and scalar-product disk, not arbitrary radial weights, arbitrary Jacobi orders, or kernels on other domains. Independent external validation has not been performed.
