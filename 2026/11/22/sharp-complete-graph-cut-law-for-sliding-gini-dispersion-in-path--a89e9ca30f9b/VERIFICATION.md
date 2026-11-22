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
# Reproducibility and verification

`check_gini_window.py` uses only the Python standard library; invoke `python3 check_gini_window.py` in the directory containing this file. It checks the complete-graph cut upper bound for every abstract pair-response sign pattern of widths \(2\) through \(6\), rational achieving pairs for widths \(2\) through \(32\) at signal lengths \(2m\) and \(2m+3\), 1200 rational random input pairs, 300 truncated-distance kernel examples and 200 separate step tests. Its deterministic random seed is `240117`.

The mathematical proof uses no computational enumeration: the upper bound follows from the complete-graph maximum-cut identity and the global reduction to steps; sharpness follows from explicit inputs. Enumeration does not constitute proof for arbitrary dimensions. Testing does not establish literature priority or the best coefficient in the shorter-input regime.
