---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Each inverse branch has Jacobian modulus 1/2 and is defined off null boundaries. Averaging the inverse pullbacks gives the transfer adjoint under the invariant normalized Lebesgue law. In the centered coordinate and centered square basis the inverse pullbacks only permute coordinates or apply affine maps to one coordinate; squaring therefore produces no mixed coordinate terms. Substitution gives the only quadratic-to-affine row (-1/4, 1/2, 0, ...), in the first square. The first-coordinate uniform law and independence of the centered coordinates give V_M(n)=0 from affine transfer and U_M(n) equal to the first-square to first-coordinate entry of the nth transfer power divided by 3. In the affine and square blocks the sole nondiagonal determinant term is the closing cycle. Cofactors yield the diagonal entries t_M/D_A and t_M/D_Q and affine (2,1) entry -z^(M-1)/(2^M D_A); the off-block resolvent gives the claimed numerator. M=2 uses the same rows with the interior row range empty. Removing the wrap terms gives -z/[12(1-z/4)(1-z/8)]; the corrections in the two denominators cannot affect this series until lag M+1, while the extra numerator first contributes -1/(3*2^(M+1)) at lag M. The cycle identities exclude every eigenvalue of modulus at least 1: the two left-side products have lower bounds 3/2^(M+1) and 7/2^(M+2), respectively, larger than the cycle products. Thus absolute convergence permits z=1, where D_A=t_M and D_Q=3t_M/4 and the sum is -2/9. At n=1 the unequal cubic moments already disprove time reversibility. Replay: python -B branches/independent_reproductions.py 1 from /workspace, an exact raw inverse-branch integration (not a centered transfer-matrix reproduction) checking both directions for M=2,...,8 and n=0,...,9. These finite results corroborate, not replace, the general proof. No claims about perturbations, later-lag signs, or entropy production follow.

## originality

PASS

Pass the all-dimensional forward mixed cubic transfer, sharp dimension-sensitive onset, and its integrated -2/9. The affine transfer is established, and it directly gives the vanishing reverse moment by parity and independence; do not credit that part alone as distinct. There is also real overlap with previous degree-two transfer for M=2. The inspected strongest earlier statements do not supply the all-M mixed cross-degree calculation and its evaluated response.

## value

PASS

A two-time moment detects irreversible dependence that ordinary stationary covariance cannot. The sharp onset of spatial feedback and the exactly dimension-independent integrated response give complementary information for a standard studied family of maps. These quantitative statements require the quadratic-to-affine mechanism, not merely the single easy witness of nonreversibility.

The dated certificate retains the supplied scientific assessment, sources and limitations.
