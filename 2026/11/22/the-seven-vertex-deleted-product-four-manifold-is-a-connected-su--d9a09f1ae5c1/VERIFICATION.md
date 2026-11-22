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

# Reproducibility and scope
Run `python3 verify.py` with standard Python 3.9 or newer. The script uses only the standard library and derives all cells from seven labels. Exact integer and binary arithmetic avoid floating-point approximation. The expected output is `CHECK_OUTPUT.txt`.

The script checks all 42, 210, 490, 420 and 140 cells in dimensions zero through four, respectively; every mod-two differential composition; all mod-two coboundary ranks; the signed 140-facet fundamental cycle's full integral boundary; and an explicit orientation-reversing vertex transposition. It constructs a complete 209-element basis of degree-two cocycles, evaluates all their cup squares with the Alexander–Whitney diagonal on the two simplex factors, and checks the induced full 40-dimensional nondegenerate alternating pairing.

The external theorems supplying connectedness, the four-manifold structure and Freedman's classification are invoked mathematically rather than implemented by the script. The displayed mod-two rank and parity identities do not by themselves imply a homeomorphism without those topological hypotheses. No calculation is claimed for other deleted products or for smooth structure.
