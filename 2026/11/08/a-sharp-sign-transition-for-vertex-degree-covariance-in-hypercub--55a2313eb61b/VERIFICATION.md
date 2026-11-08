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

# Reproduction of calculations

Run `python3 verify_hypercube.py` using Python 3 and only the standard library. The script enumerates all spanning trees of \(Q_1\), \(Q_2\), \(Q_3\), obtaining counts 1, 4, 384, and verifies the exact degree covariances directly from the enumerations. It then independently calculates the zero-mean Laplacian Green function on \(Q_d\) from all Walsh-character eigenfunctions, using eigenvalue \(2|S|\) for the character indexed by nonempty subset \(S\), and compares star-to-star transfer currents with the binomial flux formula. For every \(2\le d\le8\), \(1\le t\le d\), it checks the exact adjacent rational factorization and sign classification. The program reports 105 exact spectral/formula/sign assertions.

The output includes \(\operatorname{Cov}(D_u,D_v)=1/96,-5/32,-1/32\) at distances 1, 2, 3 in \(Q_3\), and \(1/64,-59/576,-1/64,-1/192\) at distances 1 through 4 in \(Q_4\).

The infinite-dimensional statement rests on the analytic Hamming-ball flux proof, the known transfer-current determinant and the sign factorization; finite enumeration and spectral comparisons cannot certify every dimension. Historical-priority assessment is separate from arithmetic verification.
