---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

FAIL

As written, RESULT.md:8 puts the imaginary eigenvalues on the amplitude generator. With the equation stated at line 31, the time-evolution generator is iH, not H. In the window its three eigenvalues are distinct real negative numbers; the imaginary-axis statement is true of H. Indeed for every positive parameter, an H eigenvector x gives Im(E)=Lambda |x_3|^2/||x||^2>0, since x_3=0 forces x_2=x_1=0 by the row equations, so the generator has no purely imaginary eigenvalue at all. The intended geometric result for H is correct: the normalized cubic is y^3-y^2+(u+v)y-u; its repeated roots obey u=r^2(1-2r), v=2r(1-r)^2 and 0<r<1/2. The two branches straddle r=1/3 and the discriminant has signs negative, positive, negative for increasing v below, between and above the folds. Irreducible tridiagonality forces geometric multiplicity one. The displaced parameter r=1/3+s gives delta=1/27-u=s^2+2s^3 and v-2u-2/9=6s^3, hence width 12 delta^(3/2). Replay: python3 /workspace/reproductions/independent_checks.py 4. The frozen checks/check_spectrum.py was inspected; its sampled eigenvalues illustrate, rather than prove, the window. Correcting the generator name would not cure the originality and value findings.

## originality

FAIL

The trimer matrix and EP3 are prior. For the stated linear spectral claim the remaining result is a direct specialization of the real depressed-cubic discriminant to the already published physical coordinates. An independently indexed finding gives the exact same positive-parameter cubic and the full fold locus after a bijective parameter substitution; its later catalogue date is not evidence of earlier priority. The width coefficient is the coordinate-dependent form of the standard cubic cusp, recovered by one shift and the explicit discriminant, not an additional model-specific spectral mechanism.

## value

FAIL

An exact spectral window is a sensible physical question, but this record's remaining claim is just the known cubic cusp, globally expressed in the two coefficients of an already specified cubic and locally rescaled to the supplied coordinates. Neither the canonical exponent nor its rescaled constant resolves an independent model-specific difficulty in this setting. The proof adds no transient, observable, or dynamical distinction to the prior spectral mechanism; the factor 12 is obtained directly from the canonical fold substitutions. The objection is to the routine deduction actually delivered, not to narrow exact phase diagrams or to the prior potential value of the physical model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
