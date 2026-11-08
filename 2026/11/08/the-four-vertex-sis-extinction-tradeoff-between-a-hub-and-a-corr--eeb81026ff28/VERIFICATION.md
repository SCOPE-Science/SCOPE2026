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

Use Python 3 with SymPy and run `python verify.py`. The script builds each of the complete 16-state generators from its own edge list and evaluates the exact matrix formulas, with no supplied external data. Checks include: all generator row sums; zero differences in every earlier Taylor coefficient; four exact first nonzero Taylor terms; four exact rational mean differences for symbolic positive rate; positivity certificates for their numerator and denominator polynomials; and twelve exact rational calculations at transmission rates \(1/4\), \(1\), and \(5/2\) using separately implemented fraction-based Gaussian elimination.

The script prints one final PASS line when all assertions hold. It is finite, reproducible symbolic computation and proves the specified four-vertex claim when the explicit matrix definitions are accepted. It is not a general-graph or non-Markovian theorem, and it does not determine the number or exact locations of deadline crossings. Independently performed verification has not occurred.
