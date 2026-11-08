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

# Reproducible verification

Run `python3 verify_complement_spectrum.py` with ordinary Python 3. No third-party dependencies are needed. The checker directly enumerates contiguous factors of the periodic host for every ordered run-length pair from 1 through 16, at lengths 1 through \(3(a+b)+2\) inclusive, and intersects the sets with their bitwise complements. It independently constructs the predicted language for unequal runs, and obtains the full periodic factor language for equal runs. It asserts exact *word-set* equality, per-length multiplicities, and total count for each unequal-run pair.

Observed output: `PASS 256 parameter pairs, 13568 length profiles, 41616 total per-length complemented-word occurrences checked`.

This is not an exhaustive check over unbounded run lengths or factor lengths. The infinite claim relies on the structural transition-count argument in RESULT.md. The equal-run case uses the half-period bit-flip symmetry. No independent external review or audit has been performed.
