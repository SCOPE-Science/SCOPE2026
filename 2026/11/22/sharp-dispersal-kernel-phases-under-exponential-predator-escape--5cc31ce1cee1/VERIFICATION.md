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
# Verification and reproducibility

The analytic proof in `RESULT.md` establishes the global classifications. To reproduce the finite checks, run `python3 verify.py` using a standard Python interpreter (no third-party packages). This verifies derivative signs, a uniquely bracketed tangent, concave-envelope upper bounds against many point distances and feasible two-point laws, and the sharp numerical example. The checks are deterministic and are **not** claimed to exhaust all parameters or distributions; equality and nonattainment follow from the written proof.

Exact hypotheses: \(c,\beta>0\); \(m\ge0\); \(R\) an arbitrary Borel law on \([0,\infty)\) with finite prescribed mean. Dimorphic optimality assumes \(\beta>c+1/2+\sqrt{c+1/4}\) and \(0<m<t\). The critical equality and all boundary means are included in `RESULT.md`.

Literature priority is not independently certified. The two older lattice/seed-size studies accessible only in abstract remain residual historical-comparison risks. No ecological field data or evolutionary validation is supplied.
