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

Equal residues allow the joint mass on each ordered index pair to be written as A_ij(t) dt, since the first marginal for each index is dt. Symmetry gives symmetric matrices and uniformity unit row sums, so the long mass is the integral of twice the unordered long-edge weight; there is no extra factor of the fiber size. On n vertices, comparing the two parity degree sums gives minimum long mass at least n mod 2, met by short pairs and, on an odd fiber, a half-weight triangle. For the maximum, nonzero imbalance of one pair of opposite classes modulo four, when n is not divisible by four, forces at least unit unordered short-edge weight. The rest can use length-two four-block matchings, with a short pair, half-weight triangle, or half-weight pentagon supplying the initial exceptional block as appropriate. Thus (min,max) is (n mod 2,n - 2 times the indicator that n is not divisible by four). Independently solved both graph LPs for n=2 through 80 and checked the resulting rational primal and dual certificates exactly, including all constraints; replay with python3 /workspace/reproductions/5.py. The all-real-d statement follows analytically by weighting the two fiber sizes by d-r and r; for r=0 the larger fiber has no mass, and at d=1/2 the interval is {0}. Measurable piecewise-constant endpoint constructions preserve both marginals; mixing fills the interval. A graph-supported exchangeable law is involutive a.e.; successful edges in each fiber are transpositions, losing at least one vertex on an odd fiber even under imperfect support. Short pairs and a fixed unmatched vertex attain the bound. The existence statement for a deterministic exact-support coupling is existential, as given in the proof; even at d=1/4, for example, mixing the perfect short and long matchings gives a nondeterministic coupling. For d>1/2 the interval (1-d,d) of first coordinates cannot take either jump.

## originality

PASS

Best-of-knowledge pass for simultaneous endpoint attainment and the complete interval under exact two-distance support. Explicit overlap: the separate indexed single-distance result already gives the numerical lower inequality and, through the adjacent involution, the deterministic envelope. Its evaluation at 2d is not in general the sharp upper endpoint of the simultaneous problem. The narrow supported novelty is not the residue-fiber method, parity or fractional matching in general.

## value

PASS

For uniform pairs with the simplest nontrivial commensurate displacement constraint, the full set of feasible mixture proportions is a natural dependence invariant. The upper endpoint is sensitive to more than parity and differs from unconstrained optimization of the long jump; explicit symmetric couplings show exactly which values are realizable. The meaningful gain is simultaneous feasibility, not rediscovery of the deterministic single-distance envelope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
