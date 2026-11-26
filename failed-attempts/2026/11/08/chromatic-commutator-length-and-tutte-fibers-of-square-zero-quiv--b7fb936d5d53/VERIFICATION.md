---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Vertex coefficients commute, and arrow products vanish. For e:u→v the bracket coefficient is (a_u−a_v)s_e−(b_u−b_v)r_e, with no vertex component; an individual arrow arises from its source idempotent. In a sum of l brackets, a nonzero edge requires different endpoint labels in k^(2l). For a proper coloring by those labels a differing coordinate supplies a surjective one-variable arrow equation in one summand, independently for each edge. The empty sum at z=0 gives length zero, and full support attains the width. For one bracket the arrow variables contribute q choices per edge on unequal endpoint labels, q² on equal endpoints with zero target, and none on equal endpoints with nonzero target. Expansion in indicators of equality on nonsupported arrows gives the contracted chromatic count, loops excluded from admissible colorings. Parallel arrows are counted independently. For the zero target the chromatic factor is q^(2κ(F)); dividing the resulting count by q^(2(n+m)) yields the asserted probability. For fixed G, each numerator term (q−1)^|F| q^(2κ(F)) has leading coefficient one, so the maximum degree is 2n+d, counted exactly c times, with relative O_G(1/q). Empty F gives d≥0. The graphic-matroid rank is n−κ(F) including isolated vertices; d=0 iff the two-forest rank inequalities hold on every edge subset. The forest theorem uses the multigraph convention where a parallel pair is a cycle. Ran python3 /workspace/reproductions/quivers.py: path-basis products for 140,969 ordered pairs over F₂,F₃,F₄ verify every fiber in the three test cases; the independent expanded zero-fiber polynomials return (d,c)=(2,1) for K5, (0,2) for K4 and (0,4) for two disjoint parallel pairs. This includes an extension-field check beyond prime fields. Uploaded scripts/output were inspected, not run; finite checks do not prove the field-uniform theorem.

## originality

FAIL

The exact unrestricted support length, width and individual fibers are covered in the distinct same-day indexed and frozen companion f660f871aa43. No within-day priority is inferred. The zero fiber is already stated for these arbitrary loopless multiquivers on Nov. 2. The large-field edge-arboricity result is explicit on the height-two incidence subclass, and its multigraph extension is a direct leading-degree consequence of that earlier general zero-fiber state sum and the classical forest criterion. The residual distinction is not a separate repair.

## value

PASS

As a structural result, the combined graph description gives useful complete bracket fibers and elementwise widths for a natural class of algebras, and a precise connection between commuting probability and edge density. Those are meaningful invariants. After crediting the exact overlap and the earlier state sum, the leading-degree extraction and edge-arboricity restatement are not independently sufficient for a repaired finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
