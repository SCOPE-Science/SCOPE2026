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

Execute `python3 check.py` with the Python standard library. The script checks exact rational moment recurrences by evaluating the original jump generator directly; two independent symbolic expressions for the fourth-order cross-square covariance; the finite/infinite example; the polynomial threshold gap across rational grids; high-order cutoff scaling; and the first two moments of a Poisson-integral simulation. All comparisons are deterministic except the pseudorandom Monte Carlo check, which uses a fixed seed. Finite checks support, but do not establish, all-parameter or infinite-order assertions. The proof in RESULT.md provides the universal reasoning. Self-review was performed; independent audit has not been performed.
