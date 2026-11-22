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

# Verification and reproducibility

The proof of the quantified claim is entirely analytic and is given in `RESULT.md`; the numerical regression is a consistency check. From within this directory, run `python verify.py` using Python 3.10 or later and SymPy. The executable checks in generic triangle coordinates that the outward normals obey the claimed matrix relation, that second-order edge-strip moments combine to area times the identity matrix, that the centroid correction has the required form, and that the full second-order covariance determinant agrees with the claimed area/perimeter expression when squared edge-length definitions are imposed.

It then constructs 20 independently specified rounded triangle boundaries from offset segments and sampled circular arcs, evaluates exact polygon formulas for area and second moments, and checks the predicted approach to the quadratic coefficient at three small radii. This regression uses 1,000 arc segments per corner and a deterministic random seed. A passed run prints `PASS: symbolic identities and 100 geometric regression assertions; verified components: 126.`

**Limits:** the geometric integration of circular arcs uses polygonal approximation and cannot certify a statement for all positive radii. The symbolic checks validate algebraic identities, but the geometric meaning of the decomposition and its coverage of arbitrary nondegenerate triangles rests on the proof. No independent external validation is claimed.
