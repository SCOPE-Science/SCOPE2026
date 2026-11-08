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

Run `python3 verification.py` from a directory containing the standalone file. This requires only the Python standard library; it has no network or external data dependencies.

Observed output:
```
PASS exact-rational branch, limit, basin-length and tail threshold checks: 9365
```

The code evaluates the two source-defined maps independently from their derived four-branch return, for rational parameters \(\delta=1/2,13/24,7/12,3/5,5/8,2/3\). It checks branch boundaries and 9365 exact-arithmetic assertions including sample-orbit limits after 64 iterates, the exact two-component basin length, and initial expanding-prefix probabilities up to 18 steps. It also handles the collapsing-gap endpoint.

The finite check does not prove uniqueness of all invariant measures or all-real-parameter behavior; those require the analytic facts that the normalized gap map satisfies \(0\leq Q(z)<z\) for \(0<z<1\), its expansion branch cannot iterate forever, and the invariant-measure argument via bounded convergence. The actual proof is given in RESULT.md. No independent audit or certification has been performed.
