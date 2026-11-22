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

# Reproduction and verification

Execute `python3 verify.py` with SymPy 1.10 or later. This reproduces twelve exact algebraic identities, nine representative rational parameter checks, and three diameter-attainment identities. The program prints `PASS` upon completion. The continuous inequalities in the proof have rigorous monotonicity and positive-factor arguments in `RESULT.md`; neither the representative checks nor the printout substitutes for that proof.

The critical geometric fact is the corner lemma: a convex part containing the full left side, under the stated diameter inequalities, cannot touch the right side, and the other two parts must either share the two right corners or split them. In the first case the third part bridges top and bottom gaps; in the second there is a shared right-side point. Their two resulting inequalities force the sharp T or strip lower bounds. The horizontal long-side alternative is separately excluded using the exact positive factorizations given in `RESULT.md`. At \(\lambda=1\) this reduces to the classical \(\sqrt{65}/8\) value.

No finite computation determines optimality independently of the analytic geometric argument. No independent mathematical audit has been performed.
