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

The pullback of (1,1) is anticanonical, so every line maps isomorphically to one ruling fiber. Its branch quadratic is a square, giving exactly two choices above each branch point of either ruling map; a smooth (2,2) curve gives four branch points in each ruling. To check genericity independently, coefficient evaluation at any fixed t is surjective onto (2,2) forms, and evaluation of the first t derivative is independently surjective. At a prescribed singular point three jet conditions hold; a degenerate Hessian adds one condition by surjectivity on two-jets. For two distinct singular points the two first jets impose six conditions if both coordinates differ (move the points to (0,0) and (∞,∞)), and five when they share a ruling (three along the ruling, two normal derivatives). Point and pair dimensions are respectively two, four and three, so these bad fiber loci have codimension at least two; they are avoided by a general one-parameter family. Requiring a singular point with zero t derivative adds an independent fourth condition for (t,u,v) of dimension three. Thus the total branch surface is smooth with at most one ordinary node per singular fiber. A common zero of the three quadratic coefficients is excluded by three independent conditions at a point of the two-dimensional ruling base. Completing the square then gives the finite double cover locally as z²=D. Smoothness of the total branch surface implies smoothness of D=0, and either ruling quartic has a repeated root exactly at a singular fiber, then a unique double root giving simple projection ramification. A smooth (4,4) divisor is connected by the restriction sequence and has genus nine. For each ruling the étale splitting cover corresponds to η=O_B(1,1)⊗r*O(−1), using the Veronese square map. The section divisor of r*O(1) is precisely the transverse intersection a=b=0: at c≠0 the root coordinate is proportional to b/c, which vanishes simply on B. Restriction from the surface in degree (1,1) is an isomorphism on sections, and the Koszul sequence excludes any such section vanishing on that intersection. Thus η is nontrivial, giving connectedness, genus 17 and degree eight in each ruling. Over smooth fibers these two covers identify the relative lines, so the normalized closure has exactly these two components. Riemann–Hurwitz gives 24 distinct branch values, identical for the two rulings since the nodal fibers are the same; étaleness doubles each simple ramification point, giving local double transpositions. A branch node gives A1 on the del Pezzo double cover.

## originality

PASS

The line-cover theorem is a distinct concrete calculation in the (2,2,2) branch family. The ambient fibration, individual surface lines, general component-cover method, and the 24-value discriminant datum are known or overlap an indexed result. The material surviving content is the identification of the two connected moving line curves in this family, their genera and the synchronized ramification. No inspected distinct result establishes this package for this family; this is not a claim that the conic-bundle pattern or the number 24 is new by itself.

## value

PASS

Determining how all sixteen fiberwise lines assemble into moving curves in a natural Fano threefold gives their minimal connected families and genuine base-change information. The two connected splitting covers and the synchronization of their ramifications are more informative than merely counting lines or singular fibers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
