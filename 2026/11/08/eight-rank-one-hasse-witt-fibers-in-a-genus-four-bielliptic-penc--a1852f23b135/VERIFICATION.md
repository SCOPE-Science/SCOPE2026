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

# Exact verification and scope

The public standalone Python 3 programs `verify_expand.py` and `verify_strata.py` require only standard-library modules. They were executed successfully from the corresponding source paths, and each printed `VERIFY_OK`.

`verify_expand.py` explicitly expands \(P^{18}\) and \(Q^{18}\), multiplies their sparse five-variable dictionaries over \(\mathbb F_{19}\), and independently extracts all 16 Hasse–Witt coefficients. It creates 190 nonzero terms in each separate power and 36,100 in their product.

`verify_strata.py` derives the matrix entries by nested multinomial sums, checks the symbolic determinant \(-8t^6(t^4-6)(t^4-7)\), the coprimality of the exceptional and singular parameter equations, the squarefreeness of the rank-drop polynomial, and the nonnilpotent rank-one blocks at \(t=7,9\). The geometric classification beyond those prime-field representatives follows from the explicitly proved fourth-root isomorphisms, not from finite enumeration.

Limitations: the code does not classify geometric isomorphism classes between the two parameter orbits, calculate full Newton polygons, or provide independent mathematical validation. The 2024 Hasse–Witt coefficient lemma and standard smooth-cover/p-rank principles are mathematical inputs established in the cited literature.
