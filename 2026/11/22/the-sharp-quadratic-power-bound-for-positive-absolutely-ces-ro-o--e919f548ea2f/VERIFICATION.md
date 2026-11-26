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

Reviewed RESULT.md:5–56, VERIFICATION.md, and checks/check_extremizers.py. Positivity and the order-unit norm make the same unit vector norm all powers, including in the complex case by the lattice modulus inequality. Hence the optimum absolute Cesàro constant is the supremum of the prefix averages of a_j = ||T^j||. For each j between 0 and n, submultiplicativity gives a_j a_(n-j) >= a_n; AM–GM summed over j gives (n+1)sqrt(a_n) <= sum a_j <= (n+1)K. This includes zero powers and n=0. The finite backward shift with endpoint weights c and interior weights 1 has powers with norms 1, c (N−1 terms), c², then zero. The largest prefix average includes c² and equals c+(c−1)²/(N+1). For each exact K>1 the tuning equation has one c_N>1 by strict monotonicity and unboundedness in c, and 0<K−c_N<=(K−1)²/(N+1); thus c_N² tends to K². K=1 is attained by the identity. Independent bounded replay: python3 /workspace/branches/replay_frozen_review.py 2 checked 16 exact rational matrix orbits using basis vectors and row sums. That tests the construction, not the infinite-dimensional inequality or the quantifier over real K; these are proved algebraically.

## originality

PASS

The upper estimate and qualitative power boundedness are not counted as original. The supported distinction is the exact best function of the optimal one-sided absolute Cesàro constant at the positive order-unit endpoint, with finite-dimensional nilpotent witnesses at each prescribed K. The closest verified results give finite-exponent improvements, different finite-horizon estimates, or a two-sided power-boundedness argument without this optimality. This is a bounded conclusion, not historical priority.

## value

PASS

The exact amplification allowed by an optimal average bound is a natural quantitative operator invariant. The upper inequality alone is simple; the exact-K finite-dimensional witnesses are what make this a useful sharp endpoint. They rule out improving the bound at any K>1, not merely improving the exponent as K grows.

The dated certificate retains the supplied scientific assessment, sources and limitations.
