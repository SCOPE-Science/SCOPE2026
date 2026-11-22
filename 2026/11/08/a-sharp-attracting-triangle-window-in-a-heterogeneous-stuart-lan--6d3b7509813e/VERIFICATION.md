---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-19.md",
      "INDEPENDENT_AUDIT_2026-11-19.json"
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

The co-rotating substitution at Omega=1-12q gives dot w_j=(j-|w_j|^2)w_j+(q+4iq)sum_l w_l. Closure and moduli (1,2,3) are exact. Independently assembled real 6x6 J_jk=-2 delta_jk u_j u_j^T+q[[1,-4],[4,1]] and recomputed det(lambda I-J)=lambda Q(lambda) with exactly the five stated quintic coefficients. All five Hurwitz minors independently factor as 12-6q, -2P3(q), -16P5(q), -192qS(q), -313344q^3 S(q). Exact Sturm root counts on (0,2) give one P3 root at .785633..., one P5 root at .599452..., and two S roots at .1400529264... and .5858841911..., so all strict minors are positive exactly on that open interval; for q>=2 Delta1<=0. Q(0)=1632q^2>0 ensures simple symmetry zero. At each endpoint Delta2,Delta3,a4,a5>0 and the Routh auxiliary quadratic gives a simple imaginary pair while a residual cubic is strictly Hurwitz. Conjugate mirror has R J^T R, hence identical spectrum. Local smooth orbital linearization yields distinct open basins for the two chiral periodic orbits in their stated interval. Finite root/eigenvalue checks are corroboration, not an inference of the global q statement.

## originality

PASS

Best-of-knowledge originality attaches only to the exact two-threshold shape-preserving heterogeneous M=3 full-amplitude spectral classification. The original Zhao–Uchida polygon construction and conjugate mirror-isospectral argument are prior art. The published SCOPE triangle results concern either a fixed 7-13-17 heterogeneous geometry with reactive coupling varied at fixed real coupling, or an identical-growth equilateral splay with its distinct quadratic stability condition. Their theorems do not contain this 1-sqrt(2)-sqrt(3) geometry, coupling C=q+4iq, compensating beta_j=j+3q, or an implication that yields these two sextic threshold crossings. The universal noncollinear attraction theorem treats purely reactive coupling and perturbatively small positive dissipation; it does not establish this complete dissipative-to-reactive ratio-4 path.

## value

PASS

The minimal nondegenerate zero-mean polygon in a full-amplitude heterogeneous network permits two chirality states. An exact all-positive-q bounded stability window, with loss–gain–loss via an algebraic pair-crossing boundary and full six-real-dimensional transverse criterion, resolves a naturally motivated question left open by numerical M=8 polygon maps. The growth-rate shift holds the geometry fixed, isolating coupling-induced stabilization from shape variation. The two distinct thresholds are nontrivial compared with the earlier single-threshold or purely reactive results; the exact fact can guide small-network bifurcation analysis even without a broad universality theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
