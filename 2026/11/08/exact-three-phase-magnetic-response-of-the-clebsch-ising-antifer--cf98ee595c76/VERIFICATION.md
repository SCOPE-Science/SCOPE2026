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

# Reproducibility and limits

Run `python3 verify.py` with a standard Python 3 interpreter. It uses no external dependencies and enumerates all 65,536 configurations of the 16-vertex graph. Every assertion must pass and the final printed line begins `PASS`.

The checks cover graph degree and common-neighbor constants, minimum exchange energy for every cardinality, the full independence polynomial, maximum independent neighborhoods, the sharp induced-edge lower bounds for six through eight selected vertices, and complete ground states at representative rational fields including \(7/3\) and \(5\).

The analytical graph-theoretic proof in `RESULT.md` is needed to establish the statements uniformly for every real magnetic field. The computation is exhaustive for this fixed finite graph, but it is not a theorem for other folded cubes, other couplings, or finite temperature. Bibliographic priority and independent scientific audit remain open.
