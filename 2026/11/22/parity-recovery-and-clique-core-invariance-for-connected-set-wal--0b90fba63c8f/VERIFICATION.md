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

# Verification details

The complete standalone script `verify_split_connected.py` runs under Python 3 and requires no third-party packages. It enumerates connected subsets from the core/leaf split, rather than invoking the claimed Walsh formula to construct the input, and applies an in-place integer Walsh–Hadamard transform. It compares 44,936 exact frequencies with the formula for clique sizes one through four and independent sizes two through ten (total dimension at most thirteen), checks every zero count and smallest nonzero spectral magnitude, then independently inverts the support indicator to obtain exact rational optimal range-projection norms for all tested even sizes. It also compares the combinatorial central Krawtchouk formula with direct binomial sums through independent size thirty-two. The script's result was `PASSED` on every assertion.

The all-size proof uses only the connected-set characterization, exact Walsh summation, translation averaging, Krawtchouk duality and Stirling's formula. Numerical checks do not prove the infinite statements. The literature comparison is bounded; a source equivalence may remain unindexed. No independent external validation is asserted.
