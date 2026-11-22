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

# Reproducible checks

Run `python3 verify_wheel.py` with Python 3.9+ and no third-party packages. The checker enumerates every nontrivial cut and computes exact rational squared width for all wheel sizes \(3\le m\le9\); verifies 3-connected cut inequalities and the complete minimizing cut-type multiplicities at those sizes; independently enumerates every spanning tree for \(m=3,4\) and confirms the greedy rank-support width identity for all nonconstant objective vectors in \(\{-1,0,1\}^{2m}\); and checks a constructed balanced two-separation of matroid connectivity two for \(3\le m\le64\). The success marker is `WHEEL_SPANNING_TREE_WIDTH_EXACT_PASS`.

# Analytical verification and limits

The proof in RESULT.md supplies the exact all-dimensional greedy support identity, norm comparison with strict equality, the published wheel three-connectivity premise, the explicit balanced-cut witness in both parities, and the comparison \(m^2-8m+4\le0\). Thus finite tests support the proof but are neither infinite certification nor substitutes for the argument. The source comparison and self-review are recorded separately; independent review remains unperformed.
