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

Run `python3 checker.py` from the directory containing the supplied files, using Python 3 with only standard-library modules. The checker independently enumerates all possible length-\(b\) block strings and insertion locations for a collection of small parameter instances. For each center it compares the actual numbers of output words with \(s\) valid deletion locations against the closed finite-difference formula, checks contiguity of valid positions, conservation of operation histories, the known total ball size, and the formula for the maximal multiplicity. Further exact rational comparisons average over all short words and test the independent Bernoulli run recurrence.

The checker passing is a finite test of the formulas, not an exhaustive proof over unbounded center length. The general proof and boundary conventions are in `RESULT.md`. The period-\(b\) equality criterion and previously known insertion-ball size are expressly not newly claimed.
