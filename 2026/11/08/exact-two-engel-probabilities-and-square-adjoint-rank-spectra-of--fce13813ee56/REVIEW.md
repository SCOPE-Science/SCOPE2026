# Scientific assessment: square-adjoint rank and two-Engel laws on star-graph Lie algebras

## Correctness — PASS

The source [1] specifies every nonzero star bracket, including in characteristic two. Expanding \(N_x^2\) shows it depends only on the hub coefficient and leaf vector, not on the edge and central components. The proof explicitly solves all kernel equations \(u_i v_j+u_j v_i=0\), including support sizes zero, one, two, and at least three, with the characteristic-two rank change. Multiplicities count every possible vector in the full finite Lie algebra. Conditioning on \(X\) and applying rank-nullity proves the probability formula, and the limits follow from the exact expression. No finite computation is used to infer the unrestricted theorem. The independently constructed basis-bracket checker verified all 1,477 tested \((t,u)\) profiles in ten cases, and a separate direct two-variable enumeration confirmed the two smallest characteristic tests. The main boundary is \(m\ge 2\).

## Originality — PASS, with priority risk

The closest primary text [1] gives structural invariants of graph Lie algebras, explicit star brackets, and tensor and retraction descriptions, but contains no enumerator of ranks of \(\operatorname{ad}_x^2\) and no two-Engel law probability. The general threshold bounds of Mann–Martínez [2] and Larsen–Shalev [3] control whether a large law probability forces an identity; they do not imply the exact probability or the distinct even/odd characteristic limits. Other calculations for the same star family concerning ordinary commutativity or coadjoint alternating-form ranks do not imply the square-adjoint rank enumerator from their published statements, because they measure different linear maps. Searches under two-Engel pairs, adjoint squares, star-graph nilpotent Lie algebras, and equivalent probability formulations found no covering formula. A historically unindexed exact calculation, or an identity hidden in a broader framework, remains possible; these searches do not prove absolute priority.

## Mathematical value — PASS

Two-Engel probability is a natural measure of how close a class-three algebra is to a two-Engel identity. The result gives its exact full-field values and, more strongly, the entire square-adjoint rank distribution for a canonical infinite family introduced in [1]. Its characteristic dependence is structural: in even characteristic a proportion tending to \(q^{-1}\) of elements have square-zero adjoint operators, whereas in odd characteristic that proportion tends to zero. Consequently the two-Engel pair probability has distinct limiting powers \(q^{-1}\) and \(q^{-2}\). This distinction is invisible to lower-central-series dimensions alone. It is not merely a recomputation of a known order or a generic rank bound.

## Closest literature and scope limits

[1] Gallo–Videla, arXiv:2610.33963v1, sections 2–6; [2] Mann–Martínez, *Archiv der Mathematik* 71 (1998), publisher abstract and stated threshold; [3] Larsen–Shalev, arXiv:2005.11594, introduction and Theorem 3. The result concerns finite fields and stars with at least two leaves; it does not classify all graph algebras, all Engel word values, or general Lie polynomial identity probabilities. The 1998 paper's complete text was not inspected, leaving a bounded historical-priority risk rather than a claimed whole-paper exclusion.

Self-review: passed. Independent audit: not yet performed.
