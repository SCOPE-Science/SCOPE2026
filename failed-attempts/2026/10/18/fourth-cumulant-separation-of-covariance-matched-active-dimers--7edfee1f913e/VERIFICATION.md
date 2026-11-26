---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

At ordered gaps a,b,c let L=mu+nu, m=exp(−2mu b), n=exp(−2nu b). With the common factor P²Q² exp(−L(a+c)) removed, the four-moment factors are (1+2m)(1+2n) and (1+2n), and the covariance-pair subtraction is 1+2mn. Thus the kernels are 2(m+n+mn) and 2n(1−m), both positive for interior gaps, with strictly positive difference. Integrating on the 24 ordered simplexes, with the factor 1/16 and combining outer gaps into u, gives precisely the frozen prefactor 3P²Q² and integrals. Dividing by t and dominating by the exponentially integrable kernels yields the exact linear rates and ratio. The simplex integrals t⁴/24 and t⁵/120 and the telegraph factor 2mu b yield the coefficients 3/8 and mu/20. The common covariance PQ exp(−L|t−s|) integrates to the stated variance with independent D_x t. The physical map nu=2 kbar, Q=D_x/kbar, P=4D_kappa/mu=4kappa_0² matches the source's Eqs. (13) and (19) to P/nu; this is not entropy inferred from X alone. Replay: frozen RESULT.md Proof §§1–5 and the reconstruction here. The bound verification file reports finite assertions, not independent/Lean certification; the advertised checks/verify.py was not supplied as a bound artifact and was not executed.

## originality

FAIL

The separate indexed 15c61d1928ee record gives the equivalent central theorem with the same all-time ordering, exact integrals, linear slopes and ratio, short-time coefficients and matched MSD. Its catalogue path is later; this is a judgment of demonstrable equivalent coverage among distinct indexed findings, not an assertion of which was obtained or published first. The remaining entropy equality is mechanically obtained by matching the original dimer covariances in Cocconi et al.'s already published rates, so it does not provide a genuinely distinct surviving theorem. No repair is justified by relabeling these claims.

## value

PASS

The mathematical comparison itself is scientifically informative: an observable with the same complete second-order and source-defined dissipation data has distinct fourth-order behavior at every nonzero time, with different short-time exponents. It is a motivated structural distinction, not an arbitrary computed parameter example. This value does not restore distinctness of the covered finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
