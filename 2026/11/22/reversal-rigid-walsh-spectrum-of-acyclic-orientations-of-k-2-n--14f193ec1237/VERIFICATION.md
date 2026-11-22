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

# Exact verification and reproducibility

Run `python3 verify.py` using Python 3 and the standard library. The script checks every edge-orientation bit vector for \(2\le n\le7\), computes the full Walsh transform by integer butterfly operations, and compares each coefficient against the closed formula. For \(n\le5\), it additionally verifies the underlying acyclicity condition with a separately coded directed-cycle test on the graph; this avoids taking the forbidden-pattern characterization for granted. The run printed `All exact checks passed.`

The exact integer output is: \(n=2,3,4,5,6,7\) have respectively \(14,46,146,454,1394,4246\) acyclic orientations and Fourier ranks \(8,32,128,512,2048,8192\). In every checked case the least nonzero multiplier magnitude was \(2\) and the largest equalled the acyclic-orientation count. Proof for all \(n\ge2\) is supplied in `RESULT.md`, rather than inferred from finite computations.

The checker is deterministic, has no external dependencies, makes no network requests and uses exact integers. Independent external mathematical validation has not been performed.
