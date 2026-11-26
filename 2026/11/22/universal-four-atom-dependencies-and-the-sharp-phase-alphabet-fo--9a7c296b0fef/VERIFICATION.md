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

With distinct four labels the differences a,b,c are all nonzero and distinct, so their only possible dependence is a+b+c=0. Moving the anchor from zero to a sends the three differences to a,a+b,a+c and preserves the all-one pairings and linear independence. For a fixed anchor the nondegenerate symplectic form gives 15 choices of a, 8 of b, and four solutions for c of which the dependent a+b is the only excluded solution. Divide 16·15·8·3 by 24 to obtain 240. The independent fraction-free polynomial Bareiss computation, unlike the submitted signed-permutation expansion, visited every one of the 1820 four-sets and found exactly that geometric zero-polynomial locus. Evaluation at (1,2,3,5) gives 1580 nonzero determinants. Normalizing the first coordinate by a scalar seventh root or, in the lower-bound search, a scalar qth root preserves every rank. Exact cyclotomic remainders exhaust all 441 normalized assignments for orders 1 through 6 and reproduce all six positive minima. At order 7 the exact quartet check gives only the universal failures. For a separate independent rank check, reduction Z[zeta_7] to F_71 via the element 20 of order seven gives rank three on every triple, and 1580 rank-four plus 240 rank-three quartets. Nonzero minors in the field lift to complex nonvanishing; universal determinant identities supply the upper bounds on rank. These together establish all complex ranks and minimal alphabet order. The threshold is the size of the common root alphabet, not use of seven distinct values by a four-entry window.

## originality

PASS

Pfander's explicit dependent quartet is in precisely the binary symplectic type tested here, so the already known obstruction is substantial. With standard symplectic covariance up to column phases and symplectic extension of the isometry between two triples with matching Gram matrices, that example already gives the entire one orbit of dependent quartets in the proposed type. It does not show that this is the only dependent type or give a simultaneous nonsingularity witness for the complement, and none of the inspected statements provides the sharp common-root alphabet census. The distinct contribution is the complete converse/attainable complement and exact phase-constrained classification, not the existence of a universal obstruction.

## value

PASS

A four-channel finite frame is invertible or not on a chosen quartet. Knowing exactly which selections must fail, rather than just that full spark is impossible, is a meaningful complete finite invariant of the canonical smallest noncyclic Gabor case. The flat alphabet result adds an exact design cutoff for retaining every attainable quartet under quantization and certifies all triples at that cutoff. Neither component is inferred solely from the motivation or a bare computation count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
