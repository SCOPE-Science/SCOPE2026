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

The included `verify.py` is standalone Python 3 and requires only its standard library. Run `python verify.py` from the directory in which it is extracted. It does not depend on any earlier investigation, external database, user account or arbitrary working directory.

The verifier generates all unlabeled trees through order nine by complete leaf augmentation and canonical rooted-code deduplication, checks expected counts and independently computes their edge and vertex distance counts. For the two nine-vertex collisions it compares exact two-point CDF values at twelve rational radii. It computes \(Q(T)=\mathbb E[d(X,Y)d(X,Z)]\) using exact rational integration in two ways: (1) branch-component formulas, (2) direct arclength integrals for each fixed-edge source point at the three locations \(0,1/2,1\) followed by exact quadratic interpolation. Both methods agree for **every** enumerated tree. The exact moment gaps are \(3/64\) and \(1/16\), and the combined invariants yield unique signatures throughout the census.

Expected terminal markers: `VERIFY_OK` and `THREE_POINT_VERIFY_OK`. These are not independently audited computational certificates, nor do the finite tests prove facts beyond order nine. The completeness proof is the leaf-removal induction, not a presumption based on computation time.
