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

Execute `python3 verify_prism_forest.py` with Python 3.10 or later. No third-party packages are required. The accompanying `verification_output.txt` is the actual output of the included verifier.

The verifier independently recovers all graph automorphisms among 720 vertex permutations, checks the forest counts, constructs all actual orbit flags, and uses a separate fixed-flag dynamic program to verify every orbit count via Burnside. It checks integer boundary compositions before and between exact unit-pivot reductions. The surviving integral free-chain ranks are `(1,0,0,0,2)`. It also checks 365 generator-eliminating Tietze substitutions of the full quotient one- and two-skeleton presentation. All checks terminate for the specified six-vertex graph.

The program does not assert a homeomorphism, a result for arbitrary graphs, or a general group action. The homotopy classification additionally requires the group fixed-point or fundamental-group argument, the matroid shellability theorem, successive Hurewicz isomorphisms, and homological Whitehead, as explained in `RESULT.md`. This is reproducible self-review; external independent auditing remains unperformed.
