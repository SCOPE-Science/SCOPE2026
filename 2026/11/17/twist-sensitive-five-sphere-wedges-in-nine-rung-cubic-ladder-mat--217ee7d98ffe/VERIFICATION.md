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
Run `python3 check_ladder18.py` and compare its exact JSON result with `check_ladder18_output.json`. The script needs only Python's standard library. Each graph is defined by explicit sorted endpoint pairs; every independent edge set is enumerated. For the Möbius graph, there are 36,627 nonempty matching faces, 18,301 matching pairs, 199,908 oriented face-poset covers, 23 critical five-cells, one critical six-cell and a signed unit degree. For the prism graph, there are 36,625 nonempty matching faces, 18,298 pairs, 199,890 covers, 26 critical five-cells, two critical six-cells and an integral two-by-two minor of determinant one. The complete boundary matrices and mod-two Betti numbers are printed in JSON. No random seeds, external packages, remote services, or partial data are needed.

The proof applies only to these two exact finite graphs. Complete enumeration is not evidence of an infinite-width classification. The signed Morse matrices and unit minors, rather than mod-two homology alone, are what establish the integral homotopy equivalences. Independent audit has not been performed.
