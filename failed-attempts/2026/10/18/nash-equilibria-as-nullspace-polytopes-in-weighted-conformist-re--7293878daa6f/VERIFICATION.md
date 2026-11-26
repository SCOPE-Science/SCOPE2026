---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Let Delta=(W z_R,-W^T z_C) be the action payoff differences. At any binary best response z_i Delta_i=|Delta_i|, also for pure actions and when Delta_i=0. The sum z^T Delta is identically zero by skew symmetry, so each difference vanishes; the converse is immediate. This verifies every boundary and interior equilibrium, including isolated vertices. The central cube intersection spans the two kernels, giving the dimension, uniqueness and sign-cube claims. Maximum matching bounds rank for every weighting and provides a nonzero determinant monomial for generic equality. A nonzero polynomial of independent atomless variables vanishes with probability zero by induction on variables, conditioning on the nonzero univariate specialization. For any given pure sign profile and one incident vertex, conditioning on all but one incident weight leaves at most one possible value; take a finite union over signs. At least one edge is essential to this last conclusion. Frozen VERIFICATION.md and verify.py were inspected but not executed. The code tests best responses for all 256 listed 2x2 weightings but does not recompute rank on each of those 256; the analytical theorem does not depend on that broader description of the checker.

## originality

FAIL

The headline full-equilibrium characterization is a mechanical specialization of classical zero-sum optimal strategies, not an extension from fully mixed equilibria that requires a new classification theorem. Aggregate each no-within-side team: single-player best responses are equivalent to team best responses by separability. The value-zero bilinear saddle set is exactly the product of the two cube kernels, because the coordinate sign deviations test every residual. The dimension and generic uniqueness then specialize rank–nullity and structural rank, and almost-sure lack of pure points reduces to a finite family of nontrivial linear equalities. This is demonstrated implication of standard results, not a finding that one inspected article gives the entire graph-specific package verbatim. The inspected Pei–Cao–Zhang preprint also directly covers the unweighted pure-equilibrium balance criterion, but that narrower observation alone would not cover the mixed result.

## value

FAIL

The generic uniqueness question is natural and the nullspace formula is useful exposition, but in this unbiased separable zero-sum setting it is the immediate saddle feasibility description. The graph conclusion just substitutes structural rank and rank–nullity; the pure genericity statement is a single weight per sign profile. There is no additional nonroutine classification, obstruction, or methodological claim in the frozen result that survives those standard implications.

The dated certificate retains the supplied scientific assessment, sources and limitations.
