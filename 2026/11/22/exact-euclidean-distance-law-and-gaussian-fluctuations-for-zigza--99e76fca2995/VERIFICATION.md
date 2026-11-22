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
# Reproducible verification

Run `python3 verify_zigzag_flow.py` with Python 3 and its standard library. The script independently enumerates every path-incidence vector on the length-one/two directed zigzag graph and compares all ordered-pair squared edge-Euclidean distances with the four-state polynomial transfer calculation for \(1\le n\le12\). It verifies the exact rational generating-function coefficient recurrence for \(1\le n\le40\). Its expected final output contains `ZIGZAG_FLOW_DISTANCE_EXACT_PASS n=1..12; RATIONAL_GF_PASS n<=40`.

The infinite limit statements are established analytically by the primitive Perron eigenvalue and its derivatives; the finite checks cannot certify convergence or historical novelty. The formula holds in the specified original graph edge-coordinate realization and is not automatically preserved under integral affine polytope equivalences.
