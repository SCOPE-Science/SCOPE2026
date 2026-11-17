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

# Reproducibility and checks

The full proof is mathematical and covers all integers \(n\ge2\) and \(r\ge3\). The finite checks independently enumerate allowed Cartesian product cells, build their mod-two cellular boundaries, and calculate reduced Betti numbers. They also exercise exact inverse centering and row normalization using rational arithmetic, compare the determinant of permutation generators against the predicted integral sign, and compare subgroup-fixed matrix dimensions against an independent orbit computation.

Run `python verification/check.py` in an environment with Python 3 and SymPy to reproduce `verification/check_output.txt`. Eight finite cell complexes containing a total of 3,660 cells passed the homology comparison (five of the eight lie in the asserted three-or-more-factor range; the two-factor instances are additional boundary checks). Across four larger parameter pairs, 16 generators and 28 subgroup conditions passed exact calculations. The finite checks cannot establish an unbounded theorem, integer torsion absence, or literature novelty by themselves; those conclusions instead rest respectively on the representation-sphere proof and qualified literature comparison. No independent audit has been performed.
