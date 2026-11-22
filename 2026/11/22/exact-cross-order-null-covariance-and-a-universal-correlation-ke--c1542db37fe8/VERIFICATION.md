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

# Verification record

The mathematical proof in `RESULT.md` identifies its full domain, exact trace identity, moving-window normalization, long-run overlap sums, and restricted order of limits. Run `python3 check_multiscale_spacings.py` with standard Python 3. The checked script produced 989 passing assertions, including exact rational reconstruction of the centered window matrices, independently evaluated Dirichlet fourth monomials for every admissible order pair with 4–9 spacings, 361 overlap-sum identities, marginal asymptotic cross-checks, and an independent random sample from normalized exponential variables. The simulation is a consistency check, not a proof of the limiting theorem. Finite enumeration does not prove all integer instances; those follow from the explicit moment expansion and overlap-count argument in `RESULT.md`.

Unproved limits: simultaneous large-sample and growing-window joint CLT, fitted-null extensions, combined-test quantiles, and power. Independent audit has not been performed.
