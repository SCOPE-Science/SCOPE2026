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

The included `check_exact.py` uses exact rational count-state dynamic programming to compare the theorem's finite sum against Markov absorption probabilities for every initial count pair on all complete bipartite graphs with both part sizes at most eight. The included `check_vertex.py` independently performs exact rational absorption recursion on individually labelled binary states, without using the count-state transition algorithm; it covers all 33 graph sizes with part sizes at most six and total size at most ten. Both checks completed successfully, including all boundary tie cases. The outputs are embedded as `exact_output.txt` and `vertex_output.txt`.

The universal probability identity is derived from first-flip exponential clocks, a finite uniformly shuffled race and an explicit last-symbol count. The odd-even parity consequences follow from beta-order-statistic symmetry and stochastic ordering; the large-camp limit follows from median concentration. These infinite claims are mathematical deductions, not extrapolations from enumeration. No independent external audit or formal proof assistant certification was performed.
