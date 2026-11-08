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

The standalone `check_sl2.py` tests primes \(p=2,3,5,7\) using exact finite-field row elimination after mapping a primitive complex \(p\)-th root to an element of order \(p\) in \(\mathbb F_\ell^\times\). Its output must report full ranks \(6,24,120,336\) for the respective primes. This confirms four exact instances, not the all-prime theorem. The proof's representation-degree and cyclotomic minimal-polynomial steps are noncomputational inputs requiring the cited theory.

Run with `python check_sl2.py` from the extracted directory. Requires Python 3, NumPy, and SymPy. Independent mathematical audit has not been performed.
