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

Run `python3 verify_kneser.py` and `python3 verify_spoked.py` using Python 3 without third-party dependencies. Both recompute all 252 labelled five-up spin states and permitted nearest-neighbor exchanges, with exact integer level counts and rational hitting probabilities. The scripts were executed successfully on the assembled package sources prior to inclusion. They independently build the Petersen adjacency graph in different representations. A finite all-state enumeration proves the stated fixed-size result, but makes no claims about larger graphs or finite-temperature escape rates.
