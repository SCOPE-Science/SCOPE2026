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

# Verification and limitations

Run `python3 verify_tetrads.py` beside `tetrad_frobenius_22.csv` using Python 3 standard library. It enumerates 315 four-edge tetrads directly from 20,475 possible four-edge subsets; independently identifies all 315 isotropic two-planes of the 6-dimensional binary symplectic quotient; verifies the explicit equivariant bijection for all 22 eight-label conjugacy class representatives, every relevant cyclic power, and all full and component-wise cycle profiles. It regenerates `tetrad_frobenius_22.csv` deterministically, compares all 22 full zeta profiles, all first-four and first-five fixed counts, and proves the unique full-profile collision and the sharp five-extension statistic by complete finite classification. It also establishes the irreducibility of the explicit characteristic-three factors by exhaustive monic trial division.

The checker prints two distinct verification markers, `315_TETRADS_105_MATCHINGS_210_FOUR_CYCLES_22_PARTITIONS_21_SPECTRA_VERIFIED` and `FIVE_EXTENSION_RECOVERY_SHARP_ONE_COLLISION_VERIFIED`. The underlying theta and hyperelliptic branch-point correspondences are mathematical lemmas explained in `RESULT.md` and in the cited literature, not facts obtained from finite software sampling.

No independent mathematical audit has been performed. The result does not infer curve isomorphism classes, branch coordinates, generalized isogenies or realizability of every formal cycle class over a fixed small finite field.
