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
# Verification of the section polygon law

The analytic proof in `RESULT.md` establishes the claim for all real \(h>0\). The standalone `VERIFY.py` uses Python 3 standard-library `math` and `random` without external packages. It performs independent midpoint quadrature of the two geometric one-angle integrals, compares with the closed arctangent formulas, checks normalization, brackets the unique positive zero of the optimizing equation, and counts edges crossed by actual sampled intersecting planes. Width-weighted empirical ratios use the invariant \(d\sigma(u)\,ds\) measure rather than equal weighting of conditional orientations. Samples: 140,000 directions for each of \(h=0.2,0.9,2\); numerical comparison tolerance 0.009. It returned

`BIPYRAMID_AFFINE_SECTION_POLYGON_LAW_CHECKS_PASSED`

Its numerical root was approximately \(1.211448413824\) and the maximal pentagon probability approximately \(0.462970871315\). The last few displayed root digits depend on midpoint quadrature resolution. Finite checks cannot establish exact integrals, all-height positivity, global uniqueness, or historical novelty; those are separately addressed in the proof and review. No independent audit has been performed.
