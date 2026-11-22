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

The finite checks use `verify.py` with Python 3 and standard-library modules only. Running `python verify.py` directly enumerates each partial injection of the tested degree rather than invoking the orbit-phase factorization. The program verifies the commuting relation including its domain, iterates partial maps to detect nilpotency and its exact index, compares the observed bivariate counts with a separate chain-multiplicity coefficient calculation, and runs the factor-reconstruction algorithm. It covers the explicitly listed cycle types, including all partial injections of degree six for the identity permutation, and tests an example of two permutations with identical polynomial but different cycle types. Its expected final line is `NILPOTENT_PERMUTATION_CENTRALIZER_CHECKS_PASSED`.

The proof for arbitrary degree is given in `RESULT.md`; bounded enumeration is not a substitute. In particular, correctness depends on the transitive-orbit and injectivity argument, on the acyclic-chain criterion for nilpotence, on the Lah block count, and on the triangular leading-coefficient reconstruction. No nonstandard library or external certificate is required.
