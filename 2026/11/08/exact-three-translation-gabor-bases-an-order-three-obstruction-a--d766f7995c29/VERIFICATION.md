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

# Verification and limits

The proof in `RESULT.md` verifies the precise three-translation family, the modulo-three order obstruction, six projective patterns per translation orbit, and the exact phase count. `CHECK.py` is standalone Python 3 and uses only its standard library; run `python CHECK.py` in the extracted package directory.

The checker independently enumerates complete normalized phase arrays over 44 small parameter cases (15,773,391 arrays), compares every result with the claimed count, constructs 7,488 witnesses at larger parameters, verifies six small constructive bijections, and checks all entries of 124 explicitly assembled complex synthesis Gramians. Its exhaustive statements concern only those finite parameter sets. The infinite-family claim follows from the written proof, not computation or an unexecuted formal certificate.

The continuous topology is established by isolated finite projective patterns and freely varying fiber phases. No numerical stability, arbitrary Gabor lattice or independent external audit is asserted.
