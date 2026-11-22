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

Run `python3 verify_forests.py` from the same directory. It uses only the Python standard library and performs complete finite enumeration of ordered connector neighbour-set tuples for shore widths three, four, and five. Independent edge-subset cycle detection checks five small bicliques; integer calculations check every comparison below the three thresholds and the strictly increasing tail criterion, and then check all lower-width cases up to seventeen vertices. Verified output ends with `VERIFY_OK`.

The infinite implications are justified by the counting bijection and analytic monotonicity proof in `RESULT.md`. The higher-width part of the global biclique minimality claim cites and depends on the strict minimum-degree theorem in Wu–Lu–Dong (arXiv:2611.18076v1); this independent published theorem is not reproved by the script. Originality is a literature-based assessment and not a machine-checkable certificate. An independent mathematical audit has not been performed.
