---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-21.md",
      "INDEPENDENT_AUDIT_2026-11-21.json"
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

The classical Birkhoff adjacency criterion identifies edges with single k-cycle multipliers, of Frobenius length sqrt(2k). For a single nontrivial cycle, direct edge length is the ambient Frobenius distance and thus shortest. On moved support <=5 the only multi-cycle types are 2+2 and 2+3; any >=3-edge path costs at least 6, while for 2+3 parity rules out a cheaper pair of transposition generators. For a product rho of three disjoint transpositions and any two generator cycles alpha,beta of supports A,B with intersection I, each cycle of alpha beta on U=A∪B meets I. Therefore v−3<=|I|=k+l−v, giving k+l>=2v−3>=9 and odd parity. k+l>=11 costs at least 2+sqrt18>sqrt6+sqrt12; for sum9 the only length types are (3,6) or (4,5), and (3,6) is cheaper. A three-cycle taking one point from each transposition pair times its complementary six-cycle realizes equality, giving 2^3·2=16 paths per order and exactly 32 total; equality forces U six symbols, excluding outside motion. Separate Dijkstra on the full 720-vertex S6 weighted graph and independent cycle-factorization enumeration confirmed the six-point assertions; the support argument establishes the n-independent lower bounds.

## originality

PASS

Best-of-knowledge original after comparing exact statements and implications, excluding the mirror of this very submission as independent prior; primary-source limitations and exact residual risks below.

## value

PASS

Weighted shortest paths in polytopal 1-skeleta are geometrically distinct from unweighted graph distances and relevant to length-optimal permutation transformations. The smallest moved-support failure of additivity and a complete count of all its minimizing 2-edge paths are sharp structural statements, not a generic shortest-path computation or a marginal numerical gain. The result pinpoints why overlapping moves can beat disjoint cycle moves and supplies a reusable support-intersection lemma.

The dated certificate retains the supplied scientific assessment, sources and limitations.
