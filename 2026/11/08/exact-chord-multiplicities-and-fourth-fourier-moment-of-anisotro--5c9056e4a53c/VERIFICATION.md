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
# Reproducibility and checks

Run `python3 verify.py` with Python 3 and no additional packages. It enumerates \(C\subset(\mathbb Z/p^k\mathbb Z)^2\) and all ordered pair sums for \((p,k)=(3,1),(3,2),(3,3),(3,4),(7,1),(7,2),(11,1),(11,2)\), compares exact positive/zero multiplicities against the independent closed-form histogram, and checks sum of multiplicities and the fourth-energy identity. The field cases are regression controls, not the claimed new range. On success the script prints `ANISOTROPIC_CIRCLE_PRIME_POWER_HISTOGRAM_PASS`.

The all-prime proof is contained in `RESULT.md`; brute force on eight finite rings does not prove it. In particular, the analytic argument establishes norm-fiber lifting and the square-congruence count for arbitrary \(k\ge2\). The fourth Fourier moment follows by exact finite-character orthogonality, not a floating-point numerical Fourier transform. The delivered files have no independent mathematical audit.
