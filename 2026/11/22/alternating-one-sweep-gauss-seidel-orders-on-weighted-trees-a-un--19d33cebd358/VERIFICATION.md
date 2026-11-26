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

In visit coordinates L=εN is the strict lower part of εW. Successive exact coordinate minimizations give (I−L)P=Lᵀ. Since H=(I−L)ᵀ(I−L)−LᵀL, taking the trace against initial second moment I yields the exact doubled objective R=||L||_F²−||LP||_F². This uses only zero mean and identity covariance, not a Gaussian assumption. In the finite triangular expansion LP=ε²NNᵀ+ε³N²Nᵀ+…, the even- and odd-length factors have disjoint bipartition supports, eliminating the order-five cross term. Diagonal squares of NNᵀ count the edge fourth powers and wedges with center last; its off-diagonal squares count wedges with center first, since two distinct rows of N cannot share two predecessors on a tree. Each unmixed wedge contributes twice and each mixed wedge contributes zero. Thus the leading difference in doubled risk is 2ε⁴M_π, with O(ε⁶) remainder (the coefficient for the undoubled objective is M_π). In original labels the oriented edges determine all entries of N, so orders with the same edge orientation have the same risk. Positivity makes M_π=0 exactly when every vertex is a pure source or sink, giving precisely the two orientations of the connected bipartition. There N²=0, so the common quartic risk is exact throughout the SPD range; the finite number of other orders and their positive fourth-order gaps give a common weak-coupling interval of strict separation, not global optimality for arbitrary SPD coupling. On a path the inverse visit-time permutation alternates in either direction, yielding 2E_n. An independent weighted three-vertex check gives the mixed-order gap 2ε⁴u²v²−ε⁶u⁴v² when the sweep follows the two edges of weights u,v in that order. The frozen verification/verify.py and output.txt were inspected, not executed; the 1,590 reported exact-rational checks are supplemental, not proof for all trees.

## originality

PASS

The distinct claim is the sharp weighted mixed-wedge penalty for a single sweep under isotropic initialization, with both source–sink orientation classes and no others optimal at weak coupling. Red–black scheduling and its spectral analysis are not new; the previously compared one-sweep arrowhead and four-cycle rankings use worst-case, not averaged, quadratic energy. No inspected statement subsumes the claimed risk law.

## value

PASS

A single exact sweep is a natural finite-work budget, and expected energy from an isotropic start is distinct from familiar worst-case or asymptotic criteria. Relating the first order-dependent term to weighted directed wedges gives a useful structural invariant and a complete weak-coupling optimizer classification uniformly over all orders of a fixed weighted tree. This is not just the observation that bipartite scheduling is feasible, nor a finite-case recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
