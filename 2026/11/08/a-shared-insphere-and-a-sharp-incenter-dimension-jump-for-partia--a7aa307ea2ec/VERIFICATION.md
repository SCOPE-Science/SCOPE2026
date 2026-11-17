---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

Heuer–Striker Theorem 3.5 supplies exactly 0<=every initial row/column sum<=1; each length-k prefix normal has Frobenius norm sqrt(k). For a radius rho inball, first-row n coordinates are at least rho and sum <=1-rho sqrt(n), giving rho<=1/(n+sqrt(n)); transpose yields the m bound. Uniform entries r attain all inequalities. At optimum, the longer first row/column is fixed to r; perturbations with appropriate opposite signed small increments make every other prefix inequality strict, yielding affine dimensions mn-max(m,n) for rectangular and (n-1)^2 for square. Matching polytope has every coordinate >=rho so full row/column sum saturation forces the unique uniform center. Contact counts arise from exactly those active facets. Explicit 2-by-2 interval r(sqrt2-1)<=z<=r agrees. Full dimensionality and m=n=1 endpoints checked.

## originality

PASS

The prefix-facet and face-lattice theorems of Heuer–Striker are premises, not novel contributions. Independent statement/implication comparisons found no cited theorem giving the common Frobenius inradius, full partial-ASM center locus, tangent-facet classification and contrast with matching incenter. PASS is best-of-knowledge, not historical priority certification.

## value

PASS

The full optimal-center locus of a natural lattice/combinatorial matrix polytope is a nontrivial metric geometric invariant. Its jump from a unique matching-polytope incenter to mn-M or (n-1)^2 dimensional families is a structured distinction not a routine face count or an arbitrary small computation. Exact tangencies are geometrically useful; the result does not claim affine-invariance or a John ellipsoid.

The dated certificate retains the supplied scientific assessment, sources and limitations.
