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

# Reproduction and limits

Execute `python3 verify.py`. Its only dependencies are Python 3 standard-library modules. The file `verification_output.txt` is the actual output of the included verifier; its final line must read `ALL_CHECKS_PASS`.

The verifier builds both systems from two cyclic base triples and a four-block Pasch exchange, checks every pair once, and enumerates the complexes by both bitmask filtering and independent recursive extension. It finds, for cyclic/noncyclic respectively, 1,157/1,152 nonempty faces, 4,550/4,520 ordinary face incidences and 566/563 acyclic Morse pairs, leaving critical-cell counts (one zero-cell, 6/4 three-cells, 18/21 four-cells). The two gradient-boundary implementations agree. The signed top Morse matrices have maximal unimodular minors with zero-based critical-four-cell column indices (0,1,3,4,5,8) and (0,1,2,7), both of determinant +1. Exact determinants use the fraction-free Bareiss algorithm, not floating point. Mod-two ordinary chain ranks independently give degree-four Betti numbers 12 and 17 and no other positive-degree Betti numbers.

The transition from the Morse data to the integral homotopy classification uses the standard discrete-Morse CW theorem and the third Hurewicz isomorphism, detailed in `RESULT.md`. The script does not independently prove the published classification of all Steiner triple systems at order thirteen and cannot establish absence of parallel unpublished discoveries. No independent audit has been performed.
