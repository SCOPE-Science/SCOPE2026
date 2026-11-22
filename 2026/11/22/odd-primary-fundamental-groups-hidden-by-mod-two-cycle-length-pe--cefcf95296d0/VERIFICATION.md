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

# Reproducibility and mathematical boundaries

Run `python check.py` using Python 3 and only its standard library. Its recorded stdout is `check_output.txt`. The script constructs every vertex of the \(q=3,d=4\) quotient graph, verifies there are 2,187 vertices with degree eight and no triangles, checks every coordinate loop of length nine and the diagonal loop of length twelve is embedded, and independently enumerates the lattice vectors inside the \(\ell_1\)-ball of radius twelve. It verifies that the only nonzero periods of length at most nine are the eight signed coordinate vectors, and that the first period outside their lattice has length twelve.

The all-parameter result is established by the proof in `RESULT.md`. In particular, the proof uses the integer-cube universal cover after the elementary-square stage, a lower bound for coordinate-wise residues in the period lattice, and explicit simple cycles realizing the two periods. The finite script checks representative instances and does not claim to enumerate infinite parameter ranges, classify arbitrary fundamental groups computationally, or independently prove the universal covering-space lemma.

Same-model correctness, originality and mathematical-value assessments are reported in `REVIEW.md` and `AUDIT.json`. No independent mathematical audit has been performed.
