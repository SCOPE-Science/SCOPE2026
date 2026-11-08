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

# Reproducibility and mathematical verification

Run `python verify.py` from the same directory using Python 3; it needs no third-party dependencies. The script enumerates exactly all integer matrices whose rows can satisfy the optimal fitting threshold for dimensions \(1\) through \(4\), calculates determinants exactly by integer recursion, and confirms the predicted count and the fact that all nonsingular candidates are unimodular. It also computes the actual prefix-sum range for every permutation of each row in \(\{-2,-1,0,1,2\}^d\), for \(1\le d\le5\), and compares it to the formula based on positive and negative row sums. Expected terminal line: `CUBE_PACKET_EXACT_CHECKS_OK 165671`.

The universal proof is the coordinate range identity, the edge-incidence rank equivalence, a leaf-expansion determinant argument, and Prüfer coding, all in `RESULT.md`. The finite program checks these conclusions at small dimensions but is not evidence of exhaustive classification for all dimensions. The comparison to Xue, Lian–Xue, and Grozev–Nikolov is bibliographic and same-model, not independently audited. Historical novelty is subject to the stated risks.
