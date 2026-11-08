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

# Verification and limits

Run `python3 check_four_row.py` in a Python 3 standard-library environment. A verified execution printed:

```
CERTIFIED_SMALL_ORDER 7 nonconsecutive_s_upper< 6.34 consecutive_beta> 2.91
CERTIFIED_SMALL_ORDER 8 nonconsecutive_s_upper< 8.01 consecutive_beta> 3.69
CERTIFIED_SMALL_ORDER 9 nonconsecutive_s_upper< 10.0 consecutive_beta> 4.34
FOUR_ROW_THREE_ERASURE_PASS exact_small_orders=3 direct_masks= 91355 orders=7..39
```

The first three lines are based on rational interval enclosures for \(\pi\), \(\cos\), and the complete finite list of nonconsecutive masks (after a cyclic translate); they justify the small orders. The last line uses ordinary floating-point checks at larger orders and is corroborative only. All \(N\ge10\) cases are established by the analytical cosine sidelobe inequality and strict spectral-radius comparison in the proof. Reproducing the finite check alone is not a proof of this general inequality. No independent mathematical audit has been performed.
