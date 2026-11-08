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

Run `python3 check.py` beside `CERTIFICATE.json` with Python 3.9 or later. Both files are included in the same package. The checker reconstructs all binary words and output subsequences, verifies every witness code, checks all dual-coverage inequalities by exact rational arithmetic, and computes the eight upper bounds independently from the certificate entries.

Verified output:

```
PASS n=3 optimum=2 upper=2 source_words=8 outputs=1 witness=2 slack=0
PASS n=4 optimum=3 upper=3 source_words=16 outputs=2 witness=3 slack=1
PASS n=5 optimum=4 upper=4 source_words=32 outputs=4 witness=4 slack=0
PASS n=6 optimum=4 upper=4 source_words=64 outputs=8 witness=4 slack=0
PASS n=7 optimum=4 upper=4 source_words=128 outputs=16 witness=4 slack=0
PASS n=8 optimum=7 upper=22/3 source_words=256 outputs=32 witness=7 slack=2
PASS n=9 optimum=10 upper=659/60 source_words=512 outputs=64 witness=10 slack=6
PASS n=10 optimum=14 upper=2693/180 source_words=1024 outputs=128 witness=14 slack=13
ALL EIGHT EXACT OPTIMA VERIFIED
```

The finite verification does not claim any value beyond length ten. The dual certificates are exact and complete, not optimization status logs. Independent mathematical audit has not been performed.
