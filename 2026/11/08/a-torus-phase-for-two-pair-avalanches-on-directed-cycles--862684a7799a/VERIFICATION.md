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

## Reproducible finite checks

Run `python3 verify.py` with Python 3.10 or later. The self-contained Python script uses only standard-library modules, regenerates the genuine parallel firing dynamics for sampled binary inputs, and enumerates the simplicial complex directly from the firing sets. It then performs each free-face collapse on the actual face poset and compares the surviving faces against the formula in RESULT.md.

For stable-range examples the script checks every link is a six-cycle, each edge is used by two oppositely oriented triangles, the face vector is \((n,3n,2n)\), and the Euler characteristic is zero. In sampled boundary cases it verifies \(\chi=n/2\). The verifier independently computes mod-two chain-boundary ranks and resulting Betti numbers for 49 parameter pairs, including boundary examples.

The attached output is `verification_output.txt` and records 575 torus structural cases, 23 boundary cases, 49 actual firing simulations and 49 finite-field homology checks. Finite checks are not evidence of the universal statement by themselves; the all-parameter proof is in RESULT.md. No external mathematical validation or independent audit has been performed.
