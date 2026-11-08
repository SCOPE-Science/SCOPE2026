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

The supplementary `verify.py` uses only Python 3 standard-library functions. Execute `python3 verify.py` alongside `boundary_certificate.tsv`.

Checks performed:

- All assigned colours in every closed neighbourhood of the constructed three-domatic colourings for \(n=3\) and \(6\le n\le140\).
- Reproduction of all 50 boundary-certificate rows for \(n=7,8,10,11\); direct matching of boundary profiles under \(n\mapsto n+3\) on the indicated representative ranges.
- Exhaustive absence of three-domatic colourings among 729 assignments at \(n=4\) and 59049 assignments at \(n=5\).

Observed output:

```
EXPLICIT_3_DOMATIC_OK n=3 and every 6<=n<=140
BOUNDARY_CERTIFICATE_AND_MOD3_STABILITY_OK 7 8 10 11; lifts 10->13 11->14 13->16 14->17
EXHAUSTIVE_NO_3_DOMATIC_OK n=4 (729 assignments), n=5 (59049 assignments)
VERIFY_OK
```

The infinite assertion rests on the proof's exhaustive classification of untouched and boundary-affected token pairs and on its modular boundary-stability argument, not on these finite calculations alone. This verification is not an independent mathematical audit.
