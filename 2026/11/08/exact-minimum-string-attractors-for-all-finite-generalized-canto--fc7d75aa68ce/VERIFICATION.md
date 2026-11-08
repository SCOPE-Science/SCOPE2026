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

# Reproducibility checks

The standalone `VERIFY.py` script uses only the Python standard library. Execute it in the same directory as this file using `python3 VERIFY.py`.

It independently expands the word morphism and enumerates every distinct contiguous factor of each chosen finite instance. For every factor, it forms the union of positions covered by **all** of its occurrences and asserts that this union intersects the explicit proposed attractor. Independently, it checks that each of the lower-bound witness factors occurs and that their all-occurrence support sets are pairwise disjoint. Thus the two directions of the optimum are checked without using an optimization library or an assumed minimum.

Actual packaged-script execution yielded `VERIFY_OK cases=23 factors=264990`. The selected cases cover bases \(3\) through \(9\), depths one through six where computationally tractable, and length up to \(729\). Verification enumerates finitely many examples only. The universal proof for all bases and depths is in `RESULT.md` and is not replaced by the script.

Scientific limitations: the script is finite, its enumeration costs are quadratic or higher, and no independently produced audit or formal proof certificate is asserted. The theorem does not address all arbitrary prefix lengths of the infinite fixed point.
