# Review of the generic fixed-point pedal-simplex nonreturn theorem

## Correctness (C): PASS

Directly projecting the origin onto every facet plane of an axially symmetric simplex gives the exact rational recurrence in `RESULT.md`. Positive parameters remain positive at every iteration, so all iterates are genuine simplices with interior observation point. Exact differentiation at the regular centred configuration gives determinant one and trace \(-2/d\); the algebraic-integer obstruction proves the multipliers have infinite order in every dimension \(d\ge3\). Cayley–Hamilton gives a nonzero first-coordinate derivative for every positive iterate count. Real analyticity then yields a countable union of discrete exceptional sets. The 411 checks in the reproducible verifier independently support particular algebraic and finite-step identities, but are not substituted for the analytical proof.

## Originality (O): PASS, provisional

The most relevant primary paper is Zwierzyński, *When Pedal Shapes Come Back: a Complex Story* (arXiv:2611.01247v1), especially its complete Section 3 and Section 4. It gives a single four-step tetrahedral nonreturn example and special conditional two-step return results, not an all-dimensional, all-iterate generic nonreturn theorem. A previously established tetrahedral local fourth-step nonreturn does not imply the simultaneous infinite-time conclusion. The apparently close Abu-Saris–Hajja 2009 paper concerns feet dropped *from the vertices*, not projections of one fixed point. Retrieved neighboring fixed-point projection results concern other operators or prism shapes. The searches and implication comparisons are documented in `AUDIT.json`.

Unindexed historical equivalents remain a priority risk. No assertion of independent expert validation or exhaustive database uniqueness is made.

## Mathematical value (V): PASS

The new quantifier is a natural geometric one: for every dimension \(d\ge3\), almost every axial observation position (indeed all but countably many) admits **no regular-shape return at any finite positive time**. The exact two-parameter map and non-root-of-unity multipliers reveal why planar return does not extend to this higher-dimensional family. The exceptional set is not classified, and no arbitrary nonaxial statement is made.

Self-review: passed. Independent audit: not yet performed.
