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

The standalone file `verify_centered_cycle.py` uses only the Python 3 standard library. Run `python3 verify_centered_cycle.py` beside this document. It enumerates exactly all \(262{,}424\) combinations of graph-ball radius masks and nonempty proper input cuts on the cycles \(C_3\) through \(C_6\), without floating-point arithmetic, checks the three exceptional upper-envelope masks, and verifies four explicit nonnegative pairs with strict active radius choices.

The logical reductions from an arbitrary real perturbation to binary cuts, and from arbitrary nonnegative input pairs to strictly feasible linear branches, are proved in `RESULT.md`. The three excluded radius masks are ruled out by simultaneous strict inequalities on two opposite three-site sums; the checker does not assume that a numerically failed feasibility test proves impossibility.

No assertion is made for larger cycles or signed-input absolute-value maximal maps. Independent mathematical validation is not yet performed.
