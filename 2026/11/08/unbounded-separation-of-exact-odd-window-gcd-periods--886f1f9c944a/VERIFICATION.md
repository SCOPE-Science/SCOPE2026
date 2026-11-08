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
# Verification

The standalone `verify.py` uses the Python standard library and requires no external files. Running `python3 verify.py` produces:

```
VERIFY_OK primes=12 tested_odd_window_lengths=852 largest_k=261
```

For each prime between 5 and 43 it checks the Lucas norm, coprimality, modulo-Lucas antipodal identity, and the stated first-power and squared-window GCDs for every odd window length through \(6h+3\). The GCD computation uses eight exact integer windows and is exhaustive over shifts because window sums obey reversible recurrences of order two and three, respectively. The calculations are finite confirmations; the proof in `RESULT.md` supplies the arbitrary-prime and arbitrary-odd-length quantifiers.

No independent audit has been performed. No claim of formal verification or universal computer enumeration is made.
