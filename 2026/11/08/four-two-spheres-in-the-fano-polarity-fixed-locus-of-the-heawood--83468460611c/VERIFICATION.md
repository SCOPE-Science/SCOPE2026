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

# Reproduction and scientific limits

With Python 3.10 or later, run `python3 verify_polarity.py` in the directory containing `verify_polarity.py` and `morse_certificate.json`. The checker requires only the standard library.

It constructs all twenty-one incidences of the Heawood graph, the twelve edge orbits of the binary-dot-product polarity, every original matching, every orbit-model matching, and checks equality of the fixed original face set and the orbit face set. It then generates the complete staged 66-pair Morse matching from the supplied deterministic order, verifies its critical-face list and every cover of the complete Hasse diagram, and performs a full directed acyclicity test. Exact mod-two matrix ranks are recomputed independently.

The recorded successful run is stored in `verification_output.txt`. A successful replay ends with `geometric_fixed_homotopy=wedge_of_four_2_spheres`. The integral homotopy claim uses the fully verified discrete-Morse certificate and the no-one-cells CW argument; mod-two Betti numbers alone are insufficient. This finite certificate does not prove an analogous result for other projective planes, automorphisms or graphs.
