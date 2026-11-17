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

## Reproduction

Execute `python3 check_opening.py` using Python 3 with no third-party dependencies. The script was executed from the packaged source during this review and verified all expected assertions.

Expected summary:

```
EXHAUSTIVE_LOCAL_SELECTOR_PATTERNS {3: 6, 4: 12, 5: 30, 6: 60, 7: 126, 8: 252}
EXACT_SHARP_TWO_INPUT_WITNESSES_N_8_TO_60_PASSED
EXACT_RATIONAL_TWO_INPUT_CHECKS_PASSED 14500
TWO_SITE_CONSTANT_OUTPUT_PASSED
ALL_CYCLIC_OPENING_HILBERT_CHECKS_PASSED
```

## Analytic checks and limits

The proof must be checked separately from finite enumeration: (i) the max-min opening identity on periodic indices, including the two-site cycle; (ii) classification of local maxima and row-selection; (iii) centered-operator replication bound; (iv) equality requiring two independent triple-copy coordinates; (v) four strict peaks impossible on cycles of length at most seven; (vi) the all-dimension exact witness. The checker samples no infinitely large range and does not prove the unrestricted theorem. Published-source comparison and mathematical review are not independent certification.
