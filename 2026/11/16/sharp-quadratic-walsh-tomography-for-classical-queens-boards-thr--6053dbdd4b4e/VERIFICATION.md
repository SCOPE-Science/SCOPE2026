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

The exact files `verify_pair_rank.py`, `check_certificate.py` and `rank_certificate.json` constitute a self-contained computational proof of the finite claims. Both scripts require only Python 3 standard-library facilities. Execute them from the same directory:

```
python3 verify_pair_rank.py
python3 check_certificate.py
```

The first program enumerates all valid placements by fixed difference/sum diagonal masks and computes high-bit binary pivots of the two-queen incidence matrix. It produces the complete witness for board orders seven through eleven. The second program independently uses shifted diagonal masks, reversed within-pair encoding and low-bit pivots, then checks the supplied high-bit pivot sequence and the absence of singleton pairs at order eleven. The recorded outputs are `verify_first.json` and `verify_second.json`.

Observed solution counts for orders seven through twelve are 40, 92, 352, 724, 2680 and 14200. Their modular-two pair-incidence ranks for the first five orders equal the corresponding counts. At order eleven, 5280 pair patterns occur; the smallest positive completion count is two. At order twelve, the degree-two real rank is at most 8712 by a column count, so no modular rank of the full matrix is needed. Algebraic steps passing from modular pivots to real interpolation, the degree-one exclusion and distinct probability laws are detailed in `RESULT.md`.

These checks establish the stated finite-window theorem only. A modular certificate of an integer minor is not a claim of formal mechanized proof or independent expert validation. No check of orders beyond twelve or of noise stability is included.
