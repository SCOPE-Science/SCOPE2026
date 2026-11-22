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

Run `python3 checks/verify.py` from the root of this package. The implementation requires only Python 3 standard-library modules. `checks/verification_output.txt` is the recorded exact output for all tested instances.

For each \(7\le n\le11\) and each of the three thresholds, the program independently builds the graph's open-neighborhood sets, checks every subset of one shore by intersection of its actual common-neighbor sets, and forms its complete boundary matrices over \(\mathbb F_2\). It verifies the precise face vector and reduced ranks, and explicitly checks that the original cycle survives in first homology at the middle stage but bounds at the final stage. The tetrahedron free-face multiplicities are checked as well. For every nonempty cross-shore pair, the program verifies that the common-neighbor intersection is empty.

The finite calculations do not prove the infinite theorem, integral torsion-freeness, or novelty. The proof in RESULT.md independently establishes the uniform coverage formula, the elementary collapses, simple connectivity, the integral wedge type, and the inclusion-map statements for every \(n\ge7\). External independent mathematical audit has not been performed.
