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

# Verification

The standalone, dependency-free `verify_gopel135.py` performs two complete and independently generated constructions of the 135 maximal isotropic three-spaces in the binary symplectic even-subset quotient of eight labels:

- all unordered triples of pairwise orthogonal vectors spanning an eight-element subspace;
- all 105 perfect matchings and the 30 distinct images of affine hyperplane systems under the 40,320 permutations of eight labels.

It proves the two sets equal, then calculates the complete orbit decomposition for the canonical permutation of each of 22 integer partitions of eight. It separately verifies fixed maximal isotropic groups in the matching/affine orbits, the 28-pair bitangent counts, and all row weighted sums. Run `python3 verify_gopel135.py`. The final output must be `GOPEL135_OCTAD_FROBENIUS_EXHAUSTIVE_OK`. The case coverage is exhaustive; it is not a statistical finite-field sample. The symbolic argument that the finite calculation models all geometric cases is in RESULT.md. No independently performed external audit is claimed.
