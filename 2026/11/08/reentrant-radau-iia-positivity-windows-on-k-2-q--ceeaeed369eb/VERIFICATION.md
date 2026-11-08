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

# Reproducible mathematical checks

Run `python verify.py` with Python 3.10+ and SymPy 1.12+. The exact symbolic checker returned `VERIFY_OK 281` on the assembled proof script before packaging. It proves the quartic identities by symbolic simplification, uses exact Sturm root counts to exclude positive zeros for sizes 2 through 9, verifies polynomial sign-witness inequalities, and checks the full Sylvester resultant factorization in the continuous parameter. It also performs exact rational matrix identities for sizes 2 through 13 at five sample steps and confirms strictly positive off-diagonal entries on that finite grid.

The all-size assertion relies on the analytic spectral decomposition, Descartes root bound, continuous dependence of simple roots, and the one-sign-change argument for the resultant factor; the finite matrix grid is not presented as an infinite proof. The step parameter is real nonnegative, and the claim is limited to completed Radau endpoints and the complete bipartite family with one part of size two. No independent audit was performed.
