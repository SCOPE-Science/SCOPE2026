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

# Verification of complete directed flow inballs

The mathematical proof is presented in `RESULT.md`. The script `check_flow_inball.py` is independently executable with Python 3, NumPy, and SciPy. Running `python check_flow_inball.py` returned:

`COMPLETE_FLOW_INBALL_CUT_AND_LOCUS_CHECKS_PASSED 63`

The script tests 63 flow instances with \(3\leq n\leq11\), including unit-source/unit-sink and randomly generated positive rational proper prefix-sum cases. It checks exact rational feasible-flow certificates, solves 63 independent linear programs for the maximal common coordinate floor, directly constructs the orthogonal projection onto the incidence kernel using numerical singular-value decomposition, and compares critical-cut block-rank dimensions. It additionally checks the closed middle-cut parity formulas for \(3\leq n\leq17\).

The all-dimensional proof relies on an explicit positive-flow construction, the complete-graph Laplacian pseudoinverse, elementary cut conservation, and independent-block rank counting. The finite computational checks do not certify the proof or its novelty. Alternative Euclidean embeddings and degenerate zero-prefix netflow cases are outside the stated theorem.
