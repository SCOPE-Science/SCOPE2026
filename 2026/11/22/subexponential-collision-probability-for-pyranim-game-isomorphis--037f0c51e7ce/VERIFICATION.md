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

# Verification

## Executed checks

Run `python3 verify.py` with Python 3.8 or newer, standard library only. The checker enumerates all ideals of the triangular interval poset at \(n=1,2,3,4,5,6\) and verifies the totals \(2,5,14,42,132,429\) against \(C_{n+1}\). For each of those \(n\), it independently classifies graphs on a full bottom row by brute-force permutations and verifies the connected-type counts \(1,1,2,4,10,26\) against the closed form. It constructs the two distinct six-bottom-chip legal configurations whose connected graph components are \(P_3\) and \(K_3\) in opposite orders, checking that the resulting graphs are isomorphic. Finally it evaluates the component supply inequality for representative larger inputs and prints `VERIFY_OK`.

## Proof-critical checks and limits

The exhaustive small cases validate the correspondence and one representative class-size mechanism, but do not prove the infinite claim. The unrestricted proof uses the exact literature theorem for \(c_m\), the elementary central-binomial lower bound, the legal component-block construction, and Stirling's formula. Its quantifiers are all sufficiently large integers \(n\), with a finite \(n_0\) allowed. The logarithms are natural unless subscripted. The upper bound for collision probability is the trivial \(1\); only a subexponential lower estimate is asserted. No independent mathematical audit has been performed.
