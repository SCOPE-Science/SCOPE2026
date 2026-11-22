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

# Verification record

The proof is analytic: local derivatives are weighted averages on contiguous pooling blocks, the weighted variation norm reduces to step inputs, every chord is attained by a realizable pooling pattern, and piecewise-affine integration gives the global sharp value.

The included `verify.py` requires Python 3 and only its standard library. Execute `python verify.py` after extracting the files in this record. The supplementary exact-rational checker enumerates all contiguous partitions for dimensions two through seven with three positive observation-mass profiles and four variation-weight profiles, plus deterministic weighted-PAVA two-input tests and an exact four-site witness. Output observed in this package: `PASS: 8680 exact rational comparisons`.

Finite arithmetic checks are supplementary and do not certify arbitrary real parameters or all dimensions. The exact infinite family is supported by the preceding analytic proof, not extrapolation. Historical novelty is qualified by earlier equal-mass NUNA contraction theory. Independent audit is not performed.
