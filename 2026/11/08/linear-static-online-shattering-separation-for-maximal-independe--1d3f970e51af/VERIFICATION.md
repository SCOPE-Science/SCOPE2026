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

## Reproducibility

Run `python3 verify.py` from the directory containing `tree_P10.json`. The script uses the Python standard library only. It enumerates maximal independent sets directly from independence and domination constraints, confirms the explicit depth-four complete tree, and enumerates all combinations of ten-vertex witnesses across up to three connected blocks. It calculates exact VC dimensions for path lengths through twelve and independent Littlestone recurrences through ten.

The script prints `MIS_PATH_SHATTERING_CERTIFICATE_PASS` on success. The count of realizers at ten vertices is sixteen, and the tree has fifteen internal nodes and sixteen distinct valid leaf words.

## Mathematical limits

Enumeration at bounded path lengths does not establish arbitrary-length claims. The arbitrary-length VC upper bound uses the suffix-restriction induction in `RESULT.md`; the unbounded adaptive gap follows from the proved connector rule and the explicit gadget. No claim of optimal Littlestone dimension beyond ten vertices is made. Independent mathematical audit has not been performed.
