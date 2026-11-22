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

# Verification and scope

The proof is analytically self-contained in `RESULT.md`. Run `python checker.py` using Python 3.10 or later. The checker performs exact rational tests of the cubic cancellation and quadratic maximum, a 65-digit independently solved scalar minimizer, strict evaluation of both basin witnesses, a rational-time extinction comparison, and finite-time numerical integrations illustrating their very different fates. Those numerical integrations do not prove convergence or replace the exact analytic inequalities.

The logarithmic entropy function is defined only for strictly positive populations. The extinction proof uses positivity and a comparison valid for all time until the Allee threshold is crossed. The positive invariant entropy sublevel is compact. The result intentionally makes no claim at the boundaries of the sufficient inequalities, makes no assertion about the entire basin partition, and assumes constant carrying-capacity parameter.

The source mathematical model is credited to Hennessy, Popović and Sattar (arXiv:2610.12319v1). Earlier broad strong-Allee phase portraits and separatrix geometry are credited to Wang, Shi and Wei (2010/2011) and van Voorn et al. (2007). No outside or independent scientific validation has been performed.
