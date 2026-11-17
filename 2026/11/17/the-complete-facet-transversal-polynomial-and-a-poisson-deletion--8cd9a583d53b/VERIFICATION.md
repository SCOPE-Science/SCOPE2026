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

# Reproducibility and verification

The supplied `verify.py` runs with Python 3 standard library. It independently builds every facet of small cyclic polytopes using Gale's evenness criterion; it does not assume the adjacent-matching facet description. Exhaustive vertex-subset tests then compare entire transversal-size counts to the finite formula. An additional recursive graph-matching oracle independently checks equivalence of the facet condition and the no-\(k\)-matching condition in smaller cases.

Command: `python3 verify.py`. Observed result: PASS with 295 coefficient comparisons and 1,368 direct matching comparisons. Small finite tests cannot establish the theorem for unbounded \(n\) or the asymptotic Poisson limit. The main proof gives the corresponding general arguments, including the empty-set and simplex boundaries.

Self-review: passed. Independent mathematical audit has not been performed.
