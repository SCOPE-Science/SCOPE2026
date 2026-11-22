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

# Reproducibility

Run `python3 checker.py` using Python 3 with no third-party dependencies. The script builds all 1920 even signed permutations of type \(D_5\), their shortest Coxeter words and exact Bruhat intervals, then exhaustively evaluates the necessary coefficient bounds from the cited universal theorem. It checks the 572 qualifying intervals, the seven fourth-degree candidate Kazhdan–Lusztig polynomials, all nine degree-three candidate polynomials, and the exact witness vectors.

It also verifies the defining \(R\)-polynomial recurrence by all possible right descents on each of the seven degree-four candidate intervals. Two small cross-checks use the familiar \(4231\) type-\(A_3\) example and the published type-\(D_4\) length-four singularity entries.

All tests completed successfully on the embedded source. No probabilistic test, numerical approximation or external verification is claimed. The necessary general coefficient inequalities are deduced in RESULT.md from classical intersection-cohomology Poincaré duality, Kazhdan–Lusztig positivity/monotonicity, and full-flag rank unimodality. The later published universal inequality is cited only as supporting comparison. A fresh independent mathematical audit has not been performed.
