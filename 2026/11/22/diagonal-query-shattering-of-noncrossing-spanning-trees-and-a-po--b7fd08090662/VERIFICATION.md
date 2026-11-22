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

To reproduce the combinatorial checks, place `verify.py` alongside this file and run `python3 verify.py` with Python 3. No external packages, internet connection, input database, or random seeds are required. The accompanying `verification_data.txt` captures the recorded terminal output of one successful replay.

The verifier independently obtains the histograms of **all** noncrossing diagonal forests for each polygon order \(3\le n\le12\) using chord-crossing tests and union-find acyclicity. It then evaluates the two algebraic formal-series recursions and requires coefficientwise equality across that range. For polygon orders three through six, it additionally enumerates all noncrossing spanning trees from all candidate straight-line edge sets and directly tests all binary traces on every diagonal query support; exactly \(549\) supports are checked. The top coefficient is checked against \(n2^{n-5}\) for all checked orders \(n\ge4\).

The proof for unbounded \(n\) is the forest-extension theorem, face/cycle equivalence, reversible rooted-dissection bijection, and the ear-counting recurrence in `RESULT.md`. Finite enumeration is a test of these steps and is not a substitute for them. The calculation does not independently verify unindexed bibliographic priority or apply to arbitrary point configurations.
