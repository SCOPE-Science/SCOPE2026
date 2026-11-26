---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Eliminating the last exponent on the affine congruence sum u_i=b leaves an average of independent characters, so the Gram entry vanishes unless the two frequency vectors differ by a constant. In that case its unit phase can be removed by rephasing the columns. The diagonal action is free and each occupied orbit gives one positive Gram eigenvalue equal to its occupancy, with one fewer zero eigenvalues. Each shift contributing has at least d-k zero coordinates, giving the stated multinomial count divided by M. For k<d, r admissible labels need at least r(d-k) positions and this bound is attainable with exactly r labels; for k=d each whole orbit is present. Two distinct qualifying shifts must cover all d positions with their nonzero supports and a balanced two-label assignment attains the first collision. Across orbits, the minimum possible largest occupancy is ceil(d/M), attained by balancing all M counts. These give both sharp thresholds and the two boundary corollaries. The additive comparison is a span comparison using a redundant spanning list, not an invertible transformation of the raw q-column frame. The supporting files report 124 combinatorial and 56 direct complex Gram checks; they were inspected but not executed. The reference to zero and nonzero product levels in the verification paragraph is really to exponent residues 0 and 1; both give nonzero product levels.

## originality

FAIL

The distinct indexed checksum theorem 75b261de521c gives the exact same normalized spectrum and thresholds over all finite abelian alphabets. Discrete logarithms identify the product fiber with a cyclic checksum coset; translating that coset changes only column phases. The full-band endpoint is an immediate complete-orbit case. This is equivalent coverage in the indexed corpus, not a historical priority judgment based on publication-path dates.

## value

FAIL

The spectrum and thresholds are useful invariants of normalized restriction. As a standalone addition to the checked results, however, this version contributes a cyclic checksum specialization under a coordinate reparametrization and column rephasing. The extra endpoint and equality-of-spans observation are routine and neither provide a new spectral invariant nor solve the distinct additive-frame problem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
