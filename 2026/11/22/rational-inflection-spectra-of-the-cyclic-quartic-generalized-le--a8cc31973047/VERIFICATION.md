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

# Reproduction and limits

Run `python3 verify_legendre_flex.py` with Python 3.8+; it uses the standard library only. It independently enumerates the direct quartic roots and fourth-power lifts of all generic coefficient parameters over each prime \(p\equiv3\pmod4\) through \(211\). The expected terminal marker is `GENERALIZED_LEGENDRE_RATIONAL_FLEX_SPECTRUM_VERIFIED`.

Run `python3 verify_symbolic.py` with SymPy installed to reproduce the exact polynomial identities, obtaining `GENERALIZED_LEGENDRE_EXACT_POLYNOMIAL_CERTIFICATES_VERIFIED`.

The algebraic proof in RESULT.md supplies the all-prime-power argument: the Hessian factor, its nonzero discriminant/resultant, the three Klein-four transformations and fixed-point exclusion, a split-resolvent criterion, three explicit quadratic-character sums, and a square/nonsquare parameter-pairing involution. Separately, a symbolic polynomial algebra check evaluated the Hessian determinant, \(\operatorname{disc}_x Q_\lambda\), \(\operatorname{Res}_x(Q_\lambda,g_\lambda)\), the three involution identities, and their fixed-point resultants; all agreed with the displayed expressions.

The finite checks do not exhaust arbitrary extension fields. No independent mathematical audit has been performed. The theorem is restricted to fields \(q\equiv3\pmod4\) and nonexceptional marked coefficients.
