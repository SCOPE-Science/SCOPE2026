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

# Reproduction and scope

Run `python3 verify.py` with standard Python 3. It implements the free-Lie degree-three polynomial by three-fold tensor words, not by assuming the theorem's image formula, then compares exact results to the claimed cardinalities for eight configurations with \(d=2,3,4\) and fields of order \(q=2,3,4,5\) where applicable.

The program enumerates all \(q^{2d}\) pairs in the generating space, checks the zero fiber, the nonzero attained fiber multiplicities, the total image size, and pairwise intersection of all line-indexed image spaces. The entire program's output from this run is embedded as `verify_output.txt`.

The checker covers selected finite cases only. The all-dimension, all-characteristic assertion follows instead from tensor embedding of the free Lie algebra, explicit independent multidegree supports, and the exact rank/linear-kernel argument in `RESULT.md`. In characteristic two, the middle tensor coefficient vanishes but the unit leading tensor term remains, so no division by two or three is used. No independent audit has been performed.
