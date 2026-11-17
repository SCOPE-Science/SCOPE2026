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

The analytic curvature proof covers all integer dimensions \(n\ge3m\), all \(m\ge2\), all orthonormal blocks, and every real coefficient choice. It derives both upper and lower bounds for the curvature operator through exact great-circle Fourier decomposition and a sharp energy-allocation inequality. The equalities identify the complete endpoint kernel-normal set and all minimum-brightness projection planes.

`verify_blocks.py` is independently runnable with Python, NumPy, and SymPy (`python verify_blocks.py`). It performs exact symbolic checks of threshold identities, endpoint witnesses and kernel ranks; numerical Stiefel-frame checks including spare dimensions; and exact-formula versus Fourier-integration projection-area checks. The run produced **29,819 passing checks**. The numerical probes are not exhaustive and provide no independent audit or certification of the unrestricted proof.
