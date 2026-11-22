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

The attached `verify_ice_winding.py` independently reconstructs the \(2970\) configurations satisfying all 16 ice-rule equations and enumerates every allowed directed face or short winding cycle. Its exact integer union–find calculations test all \(256\) subsets of the eight designated winding cycles. The separate `verify_ice_hypercube.py` uses a Gray-coded four-cube and a two-outgoing-arcs-at-even-vertices construction, independently checks all ice configurations and tests the entire 256-subset criterion. To replay:

```sh
python3 verify_ice_winding.py
python3 verify_ice_hypercube.py
```

Both require standard Python 3 only, with no third-party packages or external files. Expected checks include 2970 states, 8768 face-only undirected edges, 69 face-only components, 19 after one fixed winding loop, 11 with two distinct parallel ones, and one after any transverse pair. Of all 256 designated subsets, precisely 225 are connected. The exactness is finite: no proof for larger tori or random dynamic mixing rates is supplied. The attached checkers are reproducibility evidence, not an independent scholarly audit.
