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

# Verification evidence and limits

The independent proof gives a forest factorization for the joint threshold probabilities at two distinct palindrome centers; the finite word checks verify this factorization in special cases but are not substituted for the proof. The proof checks exact cross-length covariances from nested indicators and counts eligible centers, and derives variance asymptotics using a bounded, explicitly summable geometric truncation deficit. The standalone `check_palindromes.py` computes the observable statistics by a separate brute-force procedure and performs 13,735 exact assertions over binary words through length eight, ternary words through length six, and graph-forest configurations through length fourteen. It includes counterexamples to nonuniform independence and uniform mutual independence. Its expected final line is `PASS: 13735 independently computed exact checks`.

No external mathematical certification was performed. Historical-priority comparisons are limited to the cited accessible works; a directly relevant 2013 reverse-complement DNA paper was checked by abstract only.
