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
# Reproducibility and verification
Run the included standalone `verify.py` with Python 3. The script has no external dependencies and reconstructs the graph's entire arm-word and central-particle vertex sets, every transfer edge, connectivity, fixed A/B cells and fixed edges for every element of the indicated permutation groups. It then checks both the universal character expression at each element and Burnside averages against independently constructed Young-cover graphs. The output stored in `verify_output.txt` is the exact captured stdout of execution.

The finite cases are \((m,k)=(3,2),(3,3),(4,4),(3,5)\). Checks include the full group of \(576\) elements at four particles and \(720\) elements at five particles. Smaller cases are only control cases; they are not offered as new priority claims. The proof's universal quantifier comes from the radial-order graph argument and the cycle-index enumeration, not from induction on the displayed experiments.

The equivariant topological model uses equal-length arms and all-permutation-invariant radial choices. The homotopy equivalence on the quotient is not a claim about integral equivariant representations or about the Borel construction. Direct replay checks executable computations but does not replace independent mathematical audit or complete literature priority review.
