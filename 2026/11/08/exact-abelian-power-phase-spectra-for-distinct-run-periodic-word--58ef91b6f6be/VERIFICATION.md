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

# Verification details

Run `python3 verify.py` from the same directory as `RESULT.md`. The script requires only the Python standard library. It constructs a periodic host, compares the Parikh vectors of every block at every phase modulo the host length, collects distinct qualifying factor strings, and compares the observed phase set and two counts to the asserted formulas.

Observed completed tests:

```
PASS exhaustive: 74112
PASS independent large randomized: 800
PASS sharp two-letter exclusion
```

The exhaustive configurations use three to five distinct symbols, all run lengths from one through four, every period from one through the full period length plus two, and exponents two through five. The additional reproducible cases use a fixed seed and up to eight distinct symbols, larger run lengths and longer periods. These finite checks are not an exhaustive proof for arbitrary parameters. The paper proof supplies the infinite argument; no external independent audit or formal prover certificate is claimed.
