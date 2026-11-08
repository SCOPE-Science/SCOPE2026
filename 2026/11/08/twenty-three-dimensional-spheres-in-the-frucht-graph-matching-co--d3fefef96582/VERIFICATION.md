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

The standalone program `frucht_matching_verify.py` uses only the Python 3 standard library; no third-party graph database is required. It builds the Frucht graph from the fully specified LCF list and independently enumerates all 1,025 nonempty matching faces by two algorithms. It checks the f-vector \((18,117,333,397,152,8)\), facet-size counts \((21,104,8)\), the explicit connected \(K_4\)-minor branch sets, all 502 discrete-Morse pairs, their 21 critical faces, and every one of 3,629 covering relations. Complete directed acyclicity is independently checked by a topological sort reaching 1,025 face nodes, giving the integral homotopy proof through Forman's theorem. Direct simplicial boundary ranks over three finite fields offer secondary consistency checks; these alone would not prove the infinite-order integral claim.

To rerun from the included files:

```sh
python3 frucht_matching_verify.py > observed.out
```

Compare `observed.out` with the embedded `frucht_matching_verify.out`. The successful final marker is `FRUCHT_MATCHING_WEDGE_20_S3_PASS`. All mathematical assertions are specific to the displayed Frucht graph and ordinary edge-matching complex. No external independent mathematical audit or publication-priority certification is asserted.
