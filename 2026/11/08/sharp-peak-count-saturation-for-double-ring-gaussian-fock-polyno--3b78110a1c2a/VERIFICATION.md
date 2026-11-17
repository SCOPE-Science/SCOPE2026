---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

With F(z)=(z^n−a)(z^n−b), F′(z)=conj(z)F(z) gives a quadratic in w=z^n whose discriminant is (a−b)²t(t−2n)+n²(a+b)²>0 for t>0, hence w real (including t=2n). At positive rays angular log-H curvature is positive and cannot yield local maxima; on negative rays it is strictly negative. Radial stationarity is P(u)=u^{2n}−2nu^{2n−2}+(a+b)u^n−n(a+b)u^{n−2}+ab, with four alternating Descartes signs; the radial derivative starts and ends negative, giving at most two maxima on each of n negative rays, plus origin. Exact n=11 rational sign sequence (−,+,−,+,−) for a=50000,b=4800000 yields four simple roots, hence 23 nondegenerate maxima. For every n≥12, at a=0 the B_n curve has two distinct turns (discriminant n²−12n+4>0), and perturbing small positive a produces four simple stationary roots and open saturation. Finite independently computed n=11/12 signs corroborate, while analytic proof covers all n≥3.

## originality

PASS

The same-day published multiring theorem already proves the upper bound 2n+1 as k=2 and saturation for n≥ceil(16log16)=45. It does NOT establish saturation for the sharper n=11..44 range, including the explicit first shown n=11 witness; no within-day priority is assumed. Abreu proves random-Gaussian critical-point density, and Chabaud et al. supplies Husimi stellar correspondence, not this deterministic low-degree attainment. Best-of-knowledge originality is limited to sharper constructive saturation range and precise witnesses, not general two-ring ceiling.

## value

PASS

A two-shell local-peak realization at degree n=11 and a family for every larger n is a motivated sharp complexity result for deterministic Gaussian Fock fields: it significantly lowers the previously general sufficient degree bound (45 at two rings), with exact nondegenerate configurations. This is a meaningful concrete finite-to-infinite improvement, not merely renaming the multiring formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
