---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-20.md",
      "INDEPENDENT_AUDIT_2026-11-20.json"
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

Reconstructed the exact conditional positive-Gaussian fourth moments: multiplying by d(d+2), the five quartic exponent types are (4)→3, (2,2)→1, (3,1)→4/pi, (2,1,1)→2/pi, (1,1,1,1)→4/pi². In the normalized tracefree u plus edge-v basis, the form equals ||u||²+(1−a)²||v||²+a(1−a)||Bv||²+a²|Σv|²+2Re[(a/√2)〈u,Bv〉], a=2/pi. BB^T=(d−2)I+J splits edge space into constants, standard sector B^T(1-perp), and ker B (dimension d(d−3)/2). The standard 2×2 block is exactly M_d; the constant edge mode gives tau_d. det M=alpha+(d−2)a(1−3a/2)>0 since pi>3, and det(M−alpha I)=(d−2)a²[(2−a)(1−a)−1/2]<0 since 7/11<a. Therefore 0<mu−<alpha<mu+<tau for d≥4, omitting absent alpha at d=3. tau−tr M=d beta+a²d(d−1)/2−1>0. Positive analytic unique continuation gives every eigenvalue below one. tau~a²d²/2, mu−→(pi−3)/(pi−2), giving exact asymptotic 2(pi−2)/[pi²(pi−3)] for the energy concentration ratio, with sqrt for restriction. Degree-one Gram (1−a)I+aJ gives linear contrast. Independently reconstructed full conditional monomial Gamma Gram matrices in d=3..12 and compared all eigenvalues (maximum absolute error <1.2e−14), plus d=100,1000,10000,100000 asymptotic values. Numerical checks only corroborate the all-dimensional analytic argument; initial oversized multiset expansion was avoided in corrected large-d branch-only check.

## originality

PASS

Best-of-knowledge: the exact positive-orthant pure-degree-two 2^d-scaled four-sector spectrum, strict ordering, top symmetric mode, bottom (d−1)-dimensional sector and sharp d² conditioning constant were not present in full material of the relevant earlier primary sources. Original mathematical evaluation uses fourth-moment incidence reduction, not a mere citation of a generic Slepian eigenmatrix. Closest 2026-11-16 larger-band same-mask result is explicitly later and credits the audited 2026-11-08 pure-degree result. The October 25 pure-H2 lune and November 2 quadratic quarter-wedge concern different masks and cannot force the hyperorthant spectrum. Historical priority is provisional.

## value

PASS

The positive orthant is the canonical spherical simplex/fundamental sign chamber, and the exact pure-H2 restriction spectrum is an intrinsic, nonaxisymmetric all-dimensional operator invariant. The full multiplicities/extremizers and proof of d² energy-conditioning growth, versus d for H1, provide a sharp mathematically meaningful stability separation for a natural observation region. Unlike a trivial finite table, this classifies every dimension and extracts the sharp universal coefficient from a nontrivial moment/incidence decomposition; the analysis does not claim more general bands, noise models or arbitrary regions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
