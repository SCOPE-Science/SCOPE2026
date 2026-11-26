---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The vertex and orthant formulas give vol(K_t)=2^n/[n!∏(1−t_i²)]. The projective change y↦y/(1−s·y) has inverse x↦x/(1+s·x) on the translated polar and Jacobian (1−s·y)^−(n+1), giving the uniform-box expectation. Its Hessian in s is positive definite throughout the feasible interior because the box law has full-dimensional support and the differentiated integrand is a positive weight times (U+t)(U+t)ᵀ. The Hessian at zero is (n+1)(n+2)I/3; the mixed s,t derivative is (n+1)I, so the analytic stationary branch is globally minimizing and starts at s_0=−3t/(n+2). Independent reflection gives the cubic error. For replay of the Taylor coefficients let c=n+1, A=c(c+1)/6, B=c(c+1)(c+2)(c+3)/24, b=s·t, v=∑s_i², w=∑s_i⁴. Factoring (1−b)^−c out of the expectation before taking logs yields cb+Av+(c/2)b²+2Abv+(B/3−A²/2)v²−2Bw/15+O_n(‖t‖⁶) for s=O(t). This uses E[(s·U)^4]=v²/3−2w/15 and evenness. Completing the square in cb+Av shows that replacing s(t) by s_0 in the minimum changes it only by order six; quartic terms change by order six as well. Substituting s_0 and adding −∑log(1−t_i²) gives all three displayed coefficients (separately simplified by exact symbolic arithmetic). Analyticity and separate reflection yield a real-analytic symmetric function of q on a full neighborhood, so derivative differences have analytic factors q_i−q_j, even on coordinate faces. The quotient is 2β_n+O(‖q‖₁); its numerator test gives p(15)=−118 and p(16)=180, with just one positive turning point of p between 9 and 10 and p(2)<0. The sign therefore persists on a sufficiently small fixed-dimension simplex. Along a nontrivial averaging transfer of unequal q_i,q_j the derivative is strict until equality, yielding strict Schur comparison (up to permutations) and exactly the two stated extremal classes. At zero imbalance they coalesce, and no claim is made at larger radii. See RESULT.md (1)–(6). check_anisotropy.py was inspected, not executed; its truncated moment series and finite samples are supporting evidence only, not a certified radius.

## originality

PASS

The geometry, rational polar-volume machinery and the exact one-axis response are established. The surviving contribution is the fourth-order separation of distinct allocations and the dimension-16 change of the strict fixed-squared-shift Schur order. Neither the axial formula nor coordinatewise shadow monotonicity gives the mixed fourth-order coefficient. Best-of-knowledge assessment, not a priority certificate.

## value

PASS

At fixed squared imbalance the entire quadratic variation cancels. The first informative comparison is therefore the signed quartic anisotropy, and its dimension threshold reverses the optimizing geometry. The proof gives a strict order between all locally majorization-comparable allocations, not just two numerical examples. This is useful for the natural coordinate cross-polytope family; the proved neighborhood is fixed-dimension and existential, not a global optimization result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
