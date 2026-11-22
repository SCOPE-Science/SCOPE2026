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

Run `OPENBLAS_NUM_THREADS=1 python checks/check_pq_lowner.py` from the extracted artifact root, with Python 3, NumPy and SymPy installed. This standalone script checks 25 parameter pairs \(3\le r\le7\), \(2\le s\le6\), including complete enumeration of every allowed vertex, the vertex probability measure, the centered full covariance matrix, all four positive eigenvalue families, inverse-covariance contact for every vertex, the Euclidean enclosing-ball radius, the ellipsoid volume determinant and the uniform-weight threshold. Symbolic computations check the exact contact-polynomial and threshold identities. Its successful final output is `BALANCED_MULTIPARTITE_PQ_LOEWNER_PASS cases= 25`.

The actual proof for all dimensions relies on the displayed covariance eigenspaces, the exact two-orbit contact identity, the equality of the positive quadratic root, and the global trace–determinant optimality certificate. Finite numerical checks verify only their stated parameter range. The source comparison does not certify historical priority and independent mathematical audit has not been performed.
