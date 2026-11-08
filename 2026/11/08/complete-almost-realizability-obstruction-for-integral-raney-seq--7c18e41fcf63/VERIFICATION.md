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

# Verification of Raney Dold obstruction

`verify.py` performs exact integer binomial computations and checks all critical congruences, rather than testing a candidate cycle detector. Run `python3 verify.py` from the directory containing the file. The output reproduced in `verify_output.txt` records 513 congruence comparisons for \(1\leq P\leq7\), \(1\leq R\leq P+3\) and primes \(17\leq\ell<60\), excluding those at or below the Lucas digit threshold. The exceptional \((1,1)\) case was checked through 99 terms. The proof of universal validity is in RESULT.md and depends only on exact identities, Lucas congruence and arbitrarily large primes. Finite checks cannot certify the infinite theorem, and no independent external audit has been conducted.
