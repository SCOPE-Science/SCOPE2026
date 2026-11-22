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

# Reproducible arithmetic checks

Execute `python3 verify_wendt_binary.py` using Python 3 and SymPy. The script independently generates the integer binomial circulants, extracts the first two levels of their Smith valuations over \(\mathbb Z/4\mathbb Z\), and checks both claimed families. It also computes exact integral Smith forms at seven small orders, and checks the binomial congruence supporting the all-exponent proof.

Verified minus exponents: \(1\le r\le7\), with matrix orders through \(127\). Verified plus exponents: \(1\le r\le6\), with orders through \(65\). Exact Smith forms at orders \(1,3,5,7,9,15,17\). Binomial-coefficient mod-four identity at \(1\le r\le11\).

These finite assertions confirm implementation and boundary values only. The complete proof for arbitrary positive \(r\) is the characteristic-two root classification, the exact cubic-root evaluation, and the mod-four coefficient lemma in RESULT.md. No external or independent audit is asserted.
