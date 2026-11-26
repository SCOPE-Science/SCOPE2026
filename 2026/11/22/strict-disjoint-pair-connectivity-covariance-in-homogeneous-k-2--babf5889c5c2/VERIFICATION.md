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

In homogeneous K_{2,n}, a leaf with two occupied spokes is exactly a bridge between the hubs. Per-leaf local weights are q,v,v,v², with an additional hub factor q² if no such leaf exists and q otherwise. For j=1,2 disjoint marked pairs the unnormalized event weight is q[(v(2+v))^{2j} B^{n-2j}+(q-2^j)2^j v^{2j} A^{n-2j}]: the first term allows all marked leaves to attach, the correction restores weight to exactly the 2^j same-hub choices in the disconnected sector. At j=0 this gives the partition function. Expanding the covariance numerator uses ((2+v)A/B)²=2y and (q-4)(q-1)-(q-2)²=-q, giving the frozen bracket q(1-r^n)+(y-2)[2+(q-1)y]. All factors are positive: for q<1, u<q/2 and (1-q)(2+q/2)²<4, while q>=1 is immediate. Taking r^n to zero at fixed q,v gives the claimed asymptotic with nonzero coefficient. The proof works from n=4, hence covers the stated lower boundary n=6. Independent exact replay at (q,v)=(1/2,1), via component search over 2^(2n) edge masks with integer weights 2^(n+2-k), gave scaled (Z,H_X,H_Y,H_XY)=(219673,157872,157872,115808) at n=6, with covariance numerator 516322400, and (4177,2928,2928,2144) at n=4. This tests the exact count, not the universal sign. The bundled verifier was inspected, not executed.

## originality

PASS

The closest indexed same-day result treats exactly the disjoint leaf-pair observable on the same graph, but only for unrooted forests. Its fixed-fugacity n^(-1) decay is not the fixed-positive-random-cluster exponential law. The broader random-cluster connection conjecture below q=1 motivates the tested case, while FKG already covers nonnegativity above q=1. PASS credits the strict homogeneous all-positive-parameter random-cluster formula, its previously uncovered below-one range, and its fixed-parameter equivalent, not the general conjecture or priority for positivity at q>=1.

## value

PASS

This is a strict check of a recognized general conjectural sign in the below-one regime on a natural family with arbitrarily many overlapping cycles, not another cactus instance or finite table. The explicit rate and positive prefactor further distinguish finite positive dependence from asymptotic independence. The result is valuable without extrapolating to general graphs or inhomogeneous edges.

The dated certificate retains the supplied scientific assessment, sources and limitations.
