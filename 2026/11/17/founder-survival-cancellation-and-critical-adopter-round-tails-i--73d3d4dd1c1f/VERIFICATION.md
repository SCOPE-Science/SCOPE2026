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

# Verification of the claimed founder law

Run `python3 verify.py` with the Python standard library. A successful run prints:

`VERIFY_OK numerical_pgf_and_moment_checks=270 finite_population_one_round_limits=18 critical_variance_identities=9`

Checks include independent quadrature for the offspring PGF, centered numerical derivative of the mean, exact supercritical fixed-point substitution, algebraic critical-variance equality, and convergence of the finite-population single-round PGF toward its Poisson limit for increasing population sizes. Verification uses finite numerical parameters and is not an exhaustive proof. The analytical justification is in `RESULT.md`, including the precise order of population and threshold limits, the uniform stopping-time bound, and the sharp critical local-limit argument.

The motivation source and its transition rules were read in the complete HTML text of arXiv:2611.08353v2, Sections 4.2–5 and Appendix S2. The full text of older plausible age-dependent branching references could not be obtained; their abstracts/bibliographic records, not supposed complete contents, are the basis for that part of the literature comparison. Independent validation has not been performed.
