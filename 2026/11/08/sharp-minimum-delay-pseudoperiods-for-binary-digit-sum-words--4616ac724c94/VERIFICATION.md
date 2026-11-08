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

# Reproducibility and limits

Run `python3 verify.py` alongside this document. The program uses only Python's standard library and performs finite independent checks of the proposed shift set, of the compulsory-shift witnesses, and of the pairwise-disjoint lower-bound witness families. It tests each modulus \(2\le m\le10\), 4,000 consecutive starting positions for each modulus, and 700 additional deterministic pseudorandom starting positions (up to 180 binary digits each), together with all candidate shifts in every specified finite witness.

Observed output:

```
VERIFY_OK moduli=9 assertions=79047
```

The full infinite assertion follows from the explicit carry dichotomy in `RESULT.md`. The lower-bound certificate is a formula for \(2m-1\) disjoint families for every integer \(m\ge2\), not a claim that a finite computation proves an infinite fact. No independent scientific audit has been performed. The claim does not establish the unrestricted minimum number of pseudoperiod shifts when a larger maximum delay is allowed.
