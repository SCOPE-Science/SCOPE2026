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

# Exact arithmetic verification and proof limits

The complete analytic argument is in `RESULT.md`. It proves the statement for all odd \(m\ge5\), including arbitrary multivalued correspondences, from parity on odd cycles of the permutation \(j\mapsto j+s\), together with three exhaustive classes of pairs in the constructed four-block correspondence.

Run `python check_odd_polygon.py` using Python's standard library. The executed checks returned `PASS`: exact distortion after scaling all distances by \(4m\) for every odd order \(5\) through \(401\), all odd-cycle step checks over those orders, and searches of all surjective single-valued maps with one fixed square-image label in orders \(5,7,9\). The map searches cover \(60\), \(2100\), and \(46620\) maps respectively. The integer output \(m-1\) is the distortion in the \(4m\)-scaled metric, hence \(2\pi(m-1)/(4m)\) in the original unit-circle metric.

**Limits:** finite tests do not establish the uniform claim, exclude all other multivalued correspondences, or prove scholarly priority. Uniformity and the multivalued case follow from the parity proof, independently of those tests. Chord distances and polygon-perimeter intrinsic metrics were not checked and are not claimed.
