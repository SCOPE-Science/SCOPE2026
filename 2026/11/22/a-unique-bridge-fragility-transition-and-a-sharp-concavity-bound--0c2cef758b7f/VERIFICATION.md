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

Any cycle must use both terminals and exactly two full paths, even when the retained spanning subgraph is disconnected. Thus the count by which M exceeds B is the completed-pair length sum minus m on the all-open event (where every edge was counted twice). Correcting the all-bridges PGF on the three disjoint exactly-two-path events and on the all-open event gives the stated polynomial. As a separate first-moment check, an edge in arm a has bridge probability p−p^{a+b}−p^{a+c}+p^m; summing and applying the Bernoulli likelihood derivative yields the covariance. Its bracket Q has exactly two coefficient sign changes after equal degrees are merged, Q(0)>0, Q(1)=m−a²−b²−c²<0, and positive leading coefficient. Descartes therefore forces one simple root in (0,1) and one simple root above 1, proving the physical signs. Conditioning on k open edges changes each pair event to a hypergeometric inclusion probability. Pascal's identity twice makes all preterminal curvature terms nonpositive; the final plus-m correction leaves numerator 6abc−sum a²(a−1), with the sum over arms. Independently, for m−2 open edges the two missing edges on the same arm of length a leave a−2 bridges, whereas missing edges on distinct arms leave all m−2 as bridges; this gives the same terminal curvature together with f(m)=0 and f(m−1)=sum a(a−1)/m. The equal-arm root equation bounds p_L^{2L−1} between (4L)^{-1} and L^{-1}, hence p_L^L=O(L^{-1/2}); taking logarithms and expanding proves the stated two-term order of the error. Independent replay: python /workspace/independent_checks.py (theta routine), using rank drops on edge deletion, confirmed full exact coefficient counts on (2,2,5), (2,2,6), and (3,4,5); their terminal curvatures are 1/6, −22/45, and 97/66. Read the submitted checker and verification notes without executing them. Enumeration does not certify the all-arm classification.

## originality

PASS

The prior bridge-response identities, cactus law, and theta reliability marginal are established material. The supported distinct result is the explicit joint statistic and sharp covariance/curvature classification for overlapping cycles in the three-arm family. No checked primary or catalog statement covers that theorem; theta reliability counts terminal connection alone, and the cactus result depends on edge-disjoint cycles.

## value

PASS

This is a natural minimally overlapping-cycle family for testing limits of cactus bridge results. It preserves a unique fragility maximum for all arm lengths but can violate fixed-edge concavity, with the violation pinned to one budget and decided by a sharp explicit inequality. That contrast and the equal-arm threshold scaling are more informative than isolated reliability or enumeration values.

The dated certificate retains the supplied scientific assessment, sources and limitations.
