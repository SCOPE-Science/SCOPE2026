---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

With W=M_b T_a, the Hilbert–Schmidt coefficient tr(W* P_g) is exactly the specified ambiguity value. Under conjugation by M_s T_r the coefficient has character zeta^(sa-rb). These characters are distinct and can isolate each nonzero coefficient by Fourier averaging; the complex trace pairing is nondegenerate, so this is precisely the complex lift rank. The constant and modulus-squared terms of the ambiguity expansion give deltas on b=0 and b=2da, respectively; completing the squares gives z G_d zeta^(-b^2/(4d)) and its shifted conjugate. Consequently the nonorigin real-locus deficits are Q=-p and Q=-p|z|^2, and the remaining cancellation depends only on j=b^2/(2d)-ab. Off the two lines, j is nonzero and each j corresponds to one a per nonzero b. The norm at (0,0) is positive because the window cannot vanish at both 0 and 1. At z=0 there are p nonzero coefficients. For the unit seed, Q=2 sqrt(p) and h=kappa cannot lie in S_p as -1 is not a p-th root of unity. Both line deficits imply |z|=1 and p<=2 sqrt(p), excluding p>=5. At p=3,d=1,z=1+zeta, G=1+2zeta gives Q=-3 and z/conj(z)=zeta, so all three disjoint packets do occur. Rank deficiency is not asserted to imply nonlinear phase-retrieval failure.

## originality

FAIL

The exact all-complex-parameter discriminant, including the full-rank unit-amplitude seed and the exceptional prime, is already covered up to an invertible Weyl-covariant transform by the earlier one-coordinate cyclic Gabor rank theorem. The earlier single-impulse theorem separately yields the unit-amplitude choice. The frozen comparison of their coefficient profiles overlooks the equivalence.

## value

FAIL

The family is natural and the direct Gauss-sum proof is useful, but it neither produces a new invariant nor a parameter regime outside the known one-coordinate theorem. The unit-amplitude construction is likewise an equivalent presentation of an earlier full-rank instance. A new coordinate description does not establish a distinct scientific result under the exact-invariant criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
