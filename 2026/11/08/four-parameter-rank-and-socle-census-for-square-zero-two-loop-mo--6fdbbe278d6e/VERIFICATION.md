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
# Verification of the four-parameter census

The proof reduces the exact matrix equations to \(W=\operatorname{im}A+\operatorname{im}B\subseteq U=\ker A\cap\ker B\). The Gaussian factors count image subspaces with fixed sum, then a chosen common kernel; subspace Möbius inversion on the quotient computes the remaining surjective map pairs with joint kernel zero. This is a complete all-dimensional finite-field proof, not an extrapolation from a table.

`verify.py` reconstructs the original products and the four dimensions independently. Exhaustive tests cover matrix sizes \(n=2,3,4\) over \(\mathbb F_2\) and \(n=2,3\) over \(\mathbb F_3\). Every nonzero profile coefficient agrees with the formula, including the three \(n=3,q=2,r=s=1\) profiles with counts \(42,21,42\). The exact totals are respectively \(10,148,8296,33,1665\), and the formula-only \(n=5,q=2\) total is \(1003936\). The extra symbolic checks include \(q=4\), but direct matrix enumeration in the checker uses prime-field modular arithmetic only.

The checker uses no external software dependencies and can be executed as `python3 verify.py`; the output is saved in `checks.txt`. Finite calculations provide corroboration, while the arbitrary-field feasibility statement follows from a constructive subspace argument. Priority against every possible general Hall-type formula is not established. No independent mathematical audit has been performed.
