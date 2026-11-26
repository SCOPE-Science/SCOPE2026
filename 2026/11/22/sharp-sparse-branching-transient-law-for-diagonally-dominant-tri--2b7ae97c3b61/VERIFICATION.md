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

The residual is exactly G^k b. Absolute-value domination reduces the maximum to nonnegative H. Independently, choose each parent row at random: choose tau at column j with probability H_ij/tau, and the zero row with the remaining probability. Rows are independent. Each strictly triangular length-k path uses different rows, so the expected kth power of the resulting parent matrix is H^k. By convexity of the spectral norm some realization does at least as well as H; its support is a subset of the original support, so no column-cap violation is possible. In a parent forest, each kth-power row has at most one entry tau^k, making the squared power norm tau^(2k) times the largest number of exact-depth-k descendants. The ancestors of these m descendants at distance j must number at least ceil(m/d^j), on disjoint generations. Conversely, grouping consecutive children into groups of at most d realizes the successive ceilings; ceil(ceil(m/d^j)/d)=ceil(m/d^(j+1)). Layer ordering and isolated padding give the claimed n-dimensional extremizer. The strict amplification threshold is floor(tau^(-2k))+1; complete trees attain the d^k envelope, and a chain covers d=1 and the minimum feasible n=k+1. The 7-vertex example has four residual coordinates of size 9/16, yielding 9/8.

## originality

PASS

The supported distinct result is the sharp finite dimension/column-cap/sweep law with attaining forests and the exact dimension threshold. Neither truncated Neumann iteration, the dimension-free bound, nor orthogonality of forest-power columns is claimed independently novel. The indexed alternatives do not establish coverage; the closest primary and indexed full texts were not retrievable, which limits the priority comparison.

## value

PASS

Few-sweep Jacobi triangular solves can amplify a Euclidean residual despite nilpotency and infinity-norm contraction. The exact dependence on n, d and k decides whether a finite-size factor can amplify and when that first becomes possible. That answers a structural question the dimension-free bound cannot decide.

The dated certificate retains the supplied scientific assessment, sources and limitations.
