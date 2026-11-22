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

# Reproduction

With standard Python 3, execute `python3 verify_bitmask.py` and `python3 verify_sets.py` in this directory. Each verifier is standalone, uses only the standard library, enumerates every candidate of size zero through four, and constructs its own optimal-configuration graph. Expected, separately captured outputs are `bitmask.out` and `sets.out`.

The bitmask verifier checks all \(247\) minima, all jump and slide distances, the six affine orbits, all \(26\) identifying codes and the thirteen explicit antipodal translates. The independent edge-list verifier checks the same optimum count and all distances using tuple sets, plus the identifying-code/eccentricity equivalence and the translated far-pair formula. The checks provide finite exhaustive evidence only for the thirteen-vertex graph.
