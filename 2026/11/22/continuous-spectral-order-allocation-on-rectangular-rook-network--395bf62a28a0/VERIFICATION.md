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

On the orthogonal complement of constants, strict trace convexity follows from the positive divided differences of the scalar derivative, including coincident eigenvalues, for t^(-p) and -log(t). Edge weights determine the restricted Laplacian injectively, since the full operator kills constants and its off-diagonal entries determine the edges. A connected feasible point exists; at disconnected limits the vanishing eigenvalue causes blowup, with the other eigenvalues bounded by the fixed trace 2. Existence and uniqueness therefore precede symmetry reduction. Coordinate automorphisms force the two edge classes, and both are positive to ensure connectivity. The rates a=mx and b=ny occur with multiplicities m-1 and n-1, and a+b with (m-1)(n-1); the costs of a and b are n(m-1)/2 and m(n-1)/2. Equating the negative marginal derivatives per unit cost gives the stated root with s=p+1, common factor p canceled for p>0; the logarithmic case has s=1. The left side is strictly decreasing, and its value at q=1 equals n only for m=n. At s=1 clearing denominators gives nq^2=m. At fixed m and s>1, q tends to zero and q≥(m/n)^(1/s) makes m/n negligible compared to q in the balance (m/n)q^(-s)=1-(1-m/n)(1+q)^(-s)~sq. This gives the stated powers and constants after using x/y=nq/m and the exact class cost share. For fixed m and s_n/log n→alpha in (0,infinity), the same lower bound stays positive, so the second term of the divided root equation vanishes, and log q=(log(m/n)+o(1))/s_n. If alpha is infinite the lower bound tends to one; if alpha is zero any subsequence q≥epsilon makes the first term n^(-1+o(1)) and bounds the second strictly below one. These arguments also give the two unequal iterated limits; at fixed n the same lower bound tends to one. The crossover is for fixed smaller factor m and for q, not for x/y or for arbitrary growing m.

## originality

PASS

The identified direct overlap is the unit-price p=1, m=2 prism optimization and its n^(2/3)/2 per-edge ratio; do not credit that subcase. The supported distinct contribution is the complete-factor all-real-order allocation, including its general fixed-order laws and logarithmic order crossover for the normalized rate ratio. Related same-day high-order and fixed-order results were compared by actual family, objective, variable and limit, not by date.

## value

PASS

For a natural anisotropic network and independently controllable weighted edges, the optimum shows that the direction with a diminishing aggregate budget share can have diverging relative individual conductance. The all-order solution yields a continuously varying exponent and an exact logarithmic crossover with unequal iterated limits. These distinctions are useful beyond reducing an optimization by symmetry or recovering the priced-prism subcase.

The dated certificate retains the supplied scientific assessment, sources and limitations.
