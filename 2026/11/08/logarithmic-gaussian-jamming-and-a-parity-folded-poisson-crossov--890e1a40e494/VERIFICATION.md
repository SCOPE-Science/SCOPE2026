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

The theorem reduces the full labeled process on the complete-graph corona to a Markov process whose only state is the number of remaining core vertices. The proof verifies the exact conditional edge rates, parity, a predictable compensator with uniformly controlled remainder, a bounded-increment martingale central limit theorem, and a Poisson generating-function argument in the weak-rate window.

Run `python3 verify_corona.py` from this package. The checker uses only the Python standard library and independently constructs all eligible labeled edges; it compares their exact-rational weighted terminal distributions with the reduced recurrence for six weights and sizes \(1\) through \(7\), checks parity and normalizations, verifies exact harmonic means, and tests illustrative moment scaling. A run on the packaged source completed 259 checks. No finite computation is used as a substitute for the limiting proofs.

Limitations: no elapsed-time law, no zero-rate process, and no claim of priority over inaccessible historical material. Independent audit has not been performed.
