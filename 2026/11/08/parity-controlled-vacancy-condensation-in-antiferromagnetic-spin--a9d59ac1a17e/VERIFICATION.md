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

The two standalone programs `verify_exhaustive.py` and `verify_transfer.py` require only a standard Python 3 installation. In the directory containing these files, execute:

```sh
python verify_exhaustive.py
python verify_transfer.py
```

The exhaustive checker enumerates all \(3^{n+1}\) assignments at every rim size \(3\le n\le10\), comparing exact rational energies, the occupancy distributions and degeneracies at representative parameter points and on both coexistence boundaries. The independent contraction checker computes exact occupancy-sector minima and multiplicities for all \(3\le n\le70\) and verifies the asserted envelopes and boundary counts. Both programs completed successfully in a clean local run.

The all-size theorem does not rest on finite enumeration. Its mathematical proof relies on an exact local-bond identity, the path-endpoint defect cost and parity obstructions on odd cycles; see `RESULT.md`. These computations cannot verify inaccessible literature, establish historical priority, or justify claims outside the uniform classical zero-field model.
