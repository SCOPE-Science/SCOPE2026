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

# Reproducibility

Run `python3 verify_q3_recolouring.py`. Python 3 and its standard library are sufficient; no network, packages, random choices, floating-point arithmetic or external data files are needed.

The checker regenerates all proper named-palette assignments for the eight-vertex cube for the four palette sizes from \(2\) through \(5\), reconstructs every allowed one-vertex move, checks all \(48\) cube automorphisms, forms exact combined automorphism-and-palette orbits, runs unweighted breadth-first search on orbit representatives, sums distance histograms with integer orbit weights, checks component orders, edges and all eccentricities, and independently checks every mobile four-colour state's eccentricity by direct BFS without orbit reduction. It tests the four-colour rainbow-face/frozen equivalence directly on the entire enumerated configuration set.

Observed concluding output: `VERIFY_OK`. Assertions halt the process on any mismatch. The certificate is exhaustive for the stated finite domain, but it is not a machine-verified proof of the Python language implementation or of the underlying physical hardware. Independent mathematical audit has not been performed.
