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

# Verification of the stated path law

The proof checks the probability normalization of every full expanding-base branch, the independence of successive branch codes, the finite intersection set of distinct center transition graphs, stationarity of uniform Lebesgue measure under the center kernel, the exact operator adjunction, the likelihood factorization, and the binomial identities. The proof requires a product-Lebesgue initial condition and interior probabilities; it does not establish assertions for other initial measures or noisy observations.

Run `python check.py` using Python 3 standard library. It performs exact rational checks for 25 combinations of branch counts and probabilities. For every case it verifies stationarity and the parameter-reflection adjoint identity on all test monomial pairs up to degree five, normalization of all branch words through length four, the finite binomial fluctuation-probability ratios, and noncoincidence of distinct branch outputs at a generic rational point. It also traces 450 rational initial conditions through the deterministic two-dimensional map for eight iterations and checks that observed contracting edges decode the base branch decisions. The program is finite verification only; it is not a proof of all parameter and time cases. Independent audit has not been performed.
