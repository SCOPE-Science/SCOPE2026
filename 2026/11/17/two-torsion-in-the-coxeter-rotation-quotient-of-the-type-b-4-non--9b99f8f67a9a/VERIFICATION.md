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

Run `python3 verify_b4.py` with SymPy. The checker reconstructs all signed permutations and their shortest reflection lengths, the full absolute interval and its proper-part chains, the Coxeter-conjugation chain orbits, both signed integer incidence matrices, and their exact Smith normal forms. It checks \(\partial_1\partial_2=0\), the boundary ranks and nonunit Smith entry \(2\). Its exact observed output is included in `CHECKS.txt`.

The orbit quotient is computed as a genuine geometric quotient: each rank-increasing chain has no nontrivial vertex permutation by any stabilizer, and every face coefficient is transported to its geometric orbit-cell representative. Exhaustive integer linear algebra establishes the specified finite homology groups. This verifies neither an infinite family nor any unclaimed homotopy or \(\pi_1\) statement. These are reproducibility checks, not an independent audit.
