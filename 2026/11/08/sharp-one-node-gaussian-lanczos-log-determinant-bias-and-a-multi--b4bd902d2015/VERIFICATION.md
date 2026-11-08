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

# Reproduction and mathematical verification

Execute `python3 verify.py` from this package directory; Python standard library is the only dependency. It reports `VERIFY_OK 3934` when all tests complete, with selected numerical values for the beta-integral sharp bound.

The tests check the closed-form dimension-two arcsine integral at eight condition numbers; evaluate the integral for all nontrivial endpoint multiplicities in dimensions two through seven; compare with all small endpoint spectra and randomized interior spectra; check small- and large-condition-number multiplicity selections; and compare four Gaussian Monte Carlo means against the exact beta integrals.

These are finite numerical checks and do not certify the theorem. Universal correctness rests on the explicit first-node formula, Gaussian polar decomposition, strict coordinatewise convexity, beta aggregation, Taylor expansion and dominated-convergence argument in RESULT.md. The script has bounded loops, deterministic seed and no network or nonstandard dependencies. Experimental tolerances accommodate quadrature and sampling noise; they are not theoretical error bounds.

Independent mathematical audit: not performed.
