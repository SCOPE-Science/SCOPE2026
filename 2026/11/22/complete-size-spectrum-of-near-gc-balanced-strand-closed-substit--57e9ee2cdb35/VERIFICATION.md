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

# Reproduction

Place `verify.py` and `certificate.json` in the same directory and run `python3 verify.py`. The program generates every near-balanced five-mer from the literal alphabet, forms the Watson–Crick pairs, checks the full compatibility graph, checks the seven-class coloring and 14-word witness, traverses all cliques by a canonical recurrence, and computes the symmetry orbits of the 56 optimal codebooks.

Expected verified counts: 640 near-balanced words; 320 two-word complement orbits; 104 internally admissible orbits; 1068 compatible vertex pairs; size polynomial coefficients `(1, 104, 1068, 3472, 4648, 2776, 720, 56)`; 56 maxima in 7 orbits of size 8. External scientific and historical-priority review has not been performed.
