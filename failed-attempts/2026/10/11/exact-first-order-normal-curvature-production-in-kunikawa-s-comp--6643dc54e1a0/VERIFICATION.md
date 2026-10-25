---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

For rho=2+cos(theta), z=sin(theta), rho_prime=-sin(theta), z_prime=cos(theta), source (3.7) gives C=2 kappa_prime sin(theta)/rho^4 [[0,-1],[1,0]]. The initially-flat identity (2.8) yields Kperp_t=-4 kappa_prime sin(theta)/rho^4; frame time derivatives vanish since Rperp(0)=0. Nonconstant smooth geodesic curvature has integral of (kappa_prime)^2 strictly positive; conditional for kappa_prime!=0 the only profile zeros are theta=0,pi. h=sin(theta)/rho^4 is positive on (0,pi), h_prime=(4+2cos(theta)-3cos(theta)^2)/rho^5, with the unique admissible cosine (1-sqrt(13))/3 and corresponding reflected pair of absolute maxima. Elementary substitutions yield maximum coefficient 108 sqrt(2sqrt(13)-5)/(7-sqrt(13))^4, numerically 1.2096262067386667. From compact smooth MCF, Kperp=t Kperp_t(0)+o(t) uniformly and dmu_t=rho ds dtheta+o(1); therefore E(t)=16t^2 integral(kappa_prime^2 ds) times I+o(t^2), I=int_0^{2pi}sin^2(theta)/(2+cos(theta))^7 dtheta. Independently derived J_1=2pi/sqrt(a^2-1), J_{n+1}=-(1/n) dJ_n/da: J5=227sqrt3pi/972, J6=101sqrt3pi/486, J7=1103sqrt3pi/5832; I=-J5+4J6-3J7=59sqrt3pi/1944, giving 16I=118sqrt3pi/243 and E double-prime=236sqrt3pi/243 integral(kappa_prime)^2. These symbolic identities were independently recomputed with SymPy from the explicit mathematics and the seven-file source package and verify.py inspected. The checks are exact symbolic corroboration; the universal conclusion follows from the analytic proof and published geometric identities. Orientation reversal changes scalar sign but not its squared energy.

## originality

FAIL

Kunikawa arXiv:2609.34291v1 already gives the exact initial flat-bundle normal-curvature evolution identity (2.8), the entire compact-torus source matrix (3.7) at every (s,theta), the chosen profile rho=2+cos(theta), z=sin(theta), and the initial induced metric. Combining these published identities by direct substitution yields the whole claimed pointwise derivative, not just a single witness. The zero set and unique profile extremum require only differentiating sin(theta)/(2+cos(theta))^4; the quadratic L2 energy is the standard fact that K(t)=tK_t(0)+o(t) and dmu_t=dmu_0+o(1), followed by an elementary trigonometric integral. Thus every substantive conclusion is a direct, mechanically computable corollary of the known complete source tensor and initial geometry. Exact numerical constants not printed in the primary paper do not rescue a mechanically implied claim. This is a mathematical implication comparison, not an attribution of copying or authorship. The same Resultary entry is excluded as self-evidence.

## value

FAIL

It is natural to measure how normal flatness fails on Kunikawa's compact torus, and the scalar squared L2 energy is a legitimate geometric quantity. Nevertheless, the prior paper already supplies the full pointwise curvature-production field and the entire metric; the proposed zero set, two maximizing latitudes, and global leading energy are routine one-variable differentiation and integration of that known function. The work has no new structural lemma, nontrivial geometric bound, classification, mechanism, or independently unknown/non-implied invariant; its proposed exact constants are mechanical postprocessing of the published source, with only speculative value as a future numerical benchmark. This is mathematically a correct worked quantitative illustration, but not an independent contribution satisfying the uniform V bar. The calculation is not rejected just for being finite or narrow: it fails because the exact facts are automatically recoverable from existing complete same-object formulas without a substantive new step.

The dated certificate retains the supplied scientific assessment, sources and limitations.
