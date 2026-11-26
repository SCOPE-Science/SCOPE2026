---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Differentiating the catenoid coordinates gives area density a²cosh²(v); the change z=−tanh(v) gives the stated latitude density w_b, with independent uniform azimuth and no dependence on a. The addition theorem gives E[P_l(T_b)]=α_l². Since w_b is in L² for each fixed finite b, Legendre Parseval already gives summability of (2l+1)α_l²/2; with |P_l|≤1 this proves absolute uniform convergence. The series represents the law because it has the same polynomial moments on a compact interval. At t=1 the sum is the squared latitude L² norm, H(b)^−2 times the integral of cosh⁶(v); its expansion gives the stated linear-tail coefficient. Antipodal invariance gives the other tail. For the critical window, if r_i=sqrt(1−z_i²) and δ is the wrapped azimuthal gap, 1−T_b is [(z_1−z_2)²+(r_1−r_2)²]/2+r_1r_2(1−cos δ). The last term bounds |δ| by a constant times b at fixed s, since r_1r_2≥sech² b and δ is in [−π,π]. Scaling z_i and δ by b gives uniform Taylor convergence on this bounded domain and bounded latitude densities tending to 1/2 on [−1,1]. Dominated convergence, off a null quadratic boundary, gives the stated disk-section integral and its triangular factor 2−|w|. The antiderivatives yield the two branches at r=sqrt(2s)=2, and the stated small- and large-s laws. The axial moment m=(sinh(2b)/2−b)/(sinh(2b)/2+b) increases strictly from 0 to 1, since sinh(2b)/(2b) does. The pair second moment is exactly 1/3+(3/2)(m−1/3)²; its strict branch monotonicity proves the minimum, unique height and the two-height interval. Isotropy here is of second moments, not of the full law. RESULT.md lines 48–82 checked; VERIFICATION.md, checker.py and CHECKS.txt inspected, not executed. The fixed-b, fixed-s and subsequent profile limits are not claimed jointly uniform.

## originality

PASS

Credit classical catenoid geometry, spherical-harmonic pair reconstruction, and the Euclidean strip-distance mechanism. The supported distinct result is the normalized critical-window connection for area-pushed catenoid normals together with the unique isotropic-moment truncation, not a new Legendre addition formula or a new flat-strip law.

## value

PASS

The exact profile resolves the competing two-dimensional cap and one-dimensional equatorial mechanisms in a canonical collapsed normal geometry, not just the separate endpoint exponents. The unique tensor-isotropic but nonuniform height gives a concrete limit on what a second-moment normal statistic detects. Both rely specifically on area sampling, and neither is claimed for arbitrary surfaces.

The dated certificate retains the supplied scientific assessment, sources and limitations.
