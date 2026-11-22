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
# Verification of the preimage-twin distance law

Run `python3 verify.py` with the Python 3 standard library from the extracted directory. No installed numerical or symbolic packages are needed.

The checker enumerates every input for each cyclic length \(1\le n\le11\), verifies the deck-partner and common-output equations, compares each exact Hamming-distance generating polynomial against the eight-state transfer trace, and confirms the rational moments and consecutive-triple probability for \(7\le n\le11\). It checks the defining seven-bit involution identity on every possible Boolean neighborhood, verifies the five-bit cellular-automaton factorization, and verifies single-coordinate conditional balance.

For the characteristic polynomial, it independently constructs the matrix over integers and evaluates both the determinant and displayed factorization on the full \(9\times9\) grid \((z,t)\in\{0,\ldots,8\}^2\). Both sides have degree at most eight in each variable, so two applications of polynomial interpolation prove equality over \(\mathbb Z[z,t]\). Its output is `VERIFY_OK checks= 4403` followed by the complete histogram at length eleven.

The infinite family of mean/variance identities is established by the conditional-independence proof, not extrapolation; the asymptotic normal distribution is established by the independent-block Lindeberg argument. This package contains no independent mathematical validation.
