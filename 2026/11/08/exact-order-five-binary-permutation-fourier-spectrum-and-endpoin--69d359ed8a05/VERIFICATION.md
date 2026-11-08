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

The certificate `check_permutation_wiener.py` uses only standard-library integer arithmetic. Execute `python check_permutation_wiener.py` under Python 3.10 or newer. It evaluates all \(16^4\) normalized order-five sign matrices, compares the direct \(120\)-matching permanent with the column-subset inclusion–exclusion permanent for each instance, and separately checks a weighted \(3876\)-multiset census. It requires exact equality of the full eight-level multiplicity table, the sum of multiplicities \(65536\), the second moment \(120\), the endpoint norm \(33045/4096\), the zero probability \(2525/8192\), and the complete Walsh zero/support counts. Output marker: `THREE_ENUMERATION_CERTIFICATES_PASS`.

Normalization is justified algebraically by the \(2^9\)-element row/column sign gauge action and the invariance of the absolute permanent under that action. The finite calculation is exhaustive, not extrapolative. These checks do not constitute an independent mathematical review, and historical novelty is assessed only against the stated inspected sources.
