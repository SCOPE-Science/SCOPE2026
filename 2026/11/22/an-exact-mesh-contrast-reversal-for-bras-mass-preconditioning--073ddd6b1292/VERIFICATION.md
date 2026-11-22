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

# Verification performed

The local \(P_1\) consistent mass and its inverse were computed symbolically from their \(2\times2\) definitions. Period-two Bloch reduction gives two explicit eigenvalue branches; their extrema were checked analytically using the derivatives of \(qu-t\sqrt{u^2-9}\), including the regime change at \(r=3\). The weighted BRAS formula was reduced to a quadratic polynomial in the assembled mass matrix. All endpoints and the contrast root satisfy their exact algebraic equalities.

`python3 verify.py` was executed using standard-library rational arithmetic. It passed 40 combinations of mesh sizes and exact positive contrast ratios. It independently assembles three matrices from their element contributions, checks the weighted polynomial identity, the Jacobi endpoint eigenvectors, and both zone-edge eigenvectors. It also confirms the exact witness \(r=4\): the unweighted eigenvalues at the relevant zone edge are \(169/48\) and \(49/48\), giving condition number \(169/49\), while the weighted condition number is \(91/75\).

# Limits

Finite checks neither establish the universal theorem nor verify historical priority; the general proof is the Bloch-symbol calculation in RESULT.md. Independent mathematical validation has not been performed. The identity-weighted BRAS definition and the weighted variant follow public primary literature; the new assertion concerns their exact finite-mesh spectral comparison.
