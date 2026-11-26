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

For the unnormalized real exponential kernels on complex L2(0,L), the omitted full-line tails give exactly the antisymmetric boundary kernel at lines 48–59. Even and odd reflection sectors are orthogonal; independent cosine-hyperbolic and sine-hyperbolic pairs generate rank two in each. In an orthonormal basis of each span, its real skew matrix has off-diagonal modulus equal to its two-vector Gram area divided by 2(a+b); the orthogonal complement gives zero. On 0<s<t the ratios cosh(bt)/cosh(at) and sinh(bt)/sinh(at) strictly increase (x tanh x and x coth x strictly increase). The corresponding wedge minors C and S are negative and C−S=cosh(at−bs)−cosh(as−bt)<0. Parity symmetry and the squared-minor integrals therefore give strict modulus ordering, hence simple nonzero eigenvalues. Centered Taylor wedge coefficients are 2(b²−a²) and 2ab(b²−a²)/3. The squared polynomial wedge norms are L^6/180 and L^10/33600, giving exactly the displayed cubic and quintic constants, with remainders of higher order after rescaling to a fixed interval. The Gram matrices converge entrywise to diagonals 1/a,1/b and cross entry 2/(a+b), proving the common large-length value. Own replay /workspace/branches/independent-replays.py 3 checks the signed kernel via piecewise elementary integration and cancellation-free area quadrature (small-length ratios about 0.995014 and 0.995013 at L=0.004); it does not prove the universal assertion. The frozen checker was inspected but not executed.

## originality

PASS

The distinct content is the strict parity-resolved spectrum of this pair and the exact unequal short-interval scales and coalescent long-interval limit. Commutativity on the full line and the finite-rank boundary-product mechanism are not new. The checked individual-operator and half-line studies are not the asserted two-compression invariant.

## value

PASS

The pair is naturally motivated by stationary exponential smoothing, and reflection distinguishes the two boundary contributions. The exact rank and strict ordering on every finite interval, with a quintic weak mode invisible at the cubic scale, give quantitative information about finite-window noncommutativity beyond the abstract rank mechanism.

The dated certificate retains the supplied scientific assessment, sources and limitations.
