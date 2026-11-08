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

The standalone Python standard-library checker `verify_coverage.py` is the executable finite verification artifact. Run `python3 verify_coverage.py` in the directory containing this document and the script. It examines **every** unweighted simple labeled graph on one through five vertices and **every** permutation of its players, independently comparing the permutation values with two subset dynamic programs (unconstrained and nonincreasing-original-degree constrained).

Expected output includes `Finite graph classification PASS: 1099 graphs` with counts `{1: 0, 2: 0, 3: 0, 4: 0, 5: 10}`, followed by nine exact \((k,q)\) family checks, all 138 clique component-size profiles through order ten, and the five-player optimum AUC \(17\) versus best Shapley AUC \(16\). Any assertion failure means the finite verification has failed.

The checker is genuinely exhaustive for its finite graph orders, but it cannot establish the infinite disjoint-clique and all-parameter family claims by itself. Those claims are supported by the marginal-gain rearrangement and exact counting proof in `RESULT.md`. The use of a standard minimum-sum vertex cover subset recurrence does not constitute a new general-purpose algorithm. No independent scientific validation is asserted.
