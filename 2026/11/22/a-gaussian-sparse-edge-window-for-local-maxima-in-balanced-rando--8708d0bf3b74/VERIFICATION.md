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

# Reproducible verification

Execute `python3 verify_balanced_peaks.py` from the extracted package directory; it requires only the Python 3 standard library.

The checks are independently implemented as follows. For balanced bipartite shore sizes \(n=1,2,3\) and probabilities \(p=1/3,1/2,2/3\), direct enumeration of all balanced vertex side-words and all possible cross-edge sets yields an exact rational peak-count law. A separate conditional-product dynamic program evaluates that law using independent Bernoulli peak indicators, and the distributions agree. Exact expectations independently match \(2n[1-(1-p)^{n+1}]/[(n+1)p]\). The infinite fair-side interleaving moment identity is checked with rational arithmetic for five positive edge probabilities, including \(p=1/10001\).

The script does not numerically prove asymptotic normality, the Maclaurin inequality, or the word-coupling estimate. Those are established within the analytical proof in `RESULT.md`. The checks are reproducibility evidence, not an independent audit or an external certification.
