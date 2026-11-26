---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Adjacent differences identify the quotient by constants with ℓ¹, with tail steps as the coordinate vectors. The sampled orthogonal basis 1, u, u²−mean(u²) gives the exact signed differences in (1); taking absolute column sums gives the attained norm. Independently formed D X(XᵀX)⁻¹Xᵀ H in rational arithmetic for n=3,…,22 (230 jump columns); all entries and the displayed small norms agreed. Directly from (1), at t=k/n the columns converge uniformly to 6t(1−t) times the integral on [0,1] of |1+5(2t−1)(2x−1)|: the absolute-value integrands are uniformly Lipschitz and the discrete factors differ uniformly by O(1/n). For a=5|2t−1| this integral is 1 if a≤1 and (a+1/a)/2 otherwise. On the latter branch put z=|2t−1|; the stationary equation is 75z⁴−24z²+1=0. The two interior roots, branch endpoints, and the test t=1/4 give the unique maximizing pair. Density and the strict maximum gap away from this pair establish localization of every maximizing index sequence. n=3 is the identity case.

## originality

PASS

Pass for the discrete theorem: the exact finite-grid adjacent-variation norm and its convergence and maximizing-index localization. Do not credit the continuous norm as a separate distinct finding. A same-day symmetric Jacobi indexed theorem describes the continuous operator at α=0 (after affine rescaling); that parameter specialization necessarily concerns the same continuous invariant, not the discrete sequence. The available evidence does not settle priority or show that the Jacobi result also treats the finite-grid theorem.

## value

PASS

An exact sharp stability coefficient at every sample size for the usual quadratic smoother quantifies amplification invisible to Euclidean stability. Interior asymptotic maximizing jumps explain how the smoother amplifies variation and distinguish the result from endpoint sensitivity. The finite-grid sequence is itself reusable, even granting the overlapping continuous invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
