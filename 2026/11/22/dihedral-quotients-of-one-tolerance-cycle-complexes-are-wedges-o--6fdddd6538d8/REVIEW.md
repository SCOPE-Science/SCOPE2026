# Mathematical review

## Correctness — PASS

The graph-edge tolerance convention and the genuine quotient are explicit. The one-skeleton is the complete graph, whose dihedral orbit is a star: each edge has a reflection swapping its endpoints, so its quotient is a radial interval. Every triangular orbit has either trivial stabilizer (one two-cell attached along the tree, giving a two-sphere) or a mirror stabilizer (one mirror edge canceled by its half-triangle). Nontrivial rotational stabilizers are impossible because their triangles have no cycle edge. The unique-adjacent-edge normalization reduces the orbit count to a length-\(n-4\) reflection involution with one fixed point for odd orders. No finite-case extrapolation is used.

An independent exact barycentric-quotient integral-chain checker passes at every \(4\le n\le20\): zero first homology, torsion-free second homology with the predicted rank, zero chain composition, and matching direct stabilizer orbit counts. The checker is not needed for the infinite proof.

## Originality — PASS, with residual risk

Kim–Lew (2023) develops tolerance and Leray bounds. Selvaraja (arXiv:2611.14384, first public 2026-11-10) proves symbolic-power and collapsibility/Leray theorems; the inspected introduction, definitions, and homological results do not state an equivalent integral dihedral quotient classification. An existing nonequivariant classification of one-tolerance complexes for arbitrary graphs covers the underlying cycle complex, which is explicitly excluded as new content. It does **not** determine a geometric symmetry quotient because stabilizer data and cell attachments are absent. Other published comparisons considered dihedral quotients of different cycle complexes (two-independence, matching, and neighborhood complexes); their objects and face conditions differ and no implication of this theorem was identified.

Search-based priority assessment is not proof of global uniqueness. The remaining risk is an unindexed equivalent statement or general quotient lemma already applied to these same cycle-tolerance faces.

## Mathematical value — PASS

The dihedral symmetry quotient is a canonical topological object, rather than an arbitrary finite slice. Its complete homotopy type, fundamental group, integral torsion statement and exact sphere count are simultaneously determined for every order. The quotient retains only a linearly growing number of spheres compared with quadratically many for the original space; rational character averaging alone would not establish its integral homotopy type.

## Boundaries

No formula is supplied for proper cyclic subgroup quotients, general graph automorphism quotients or higher tolerance parameters. The independent audit remains outstanding.

Self-review: passed. Independent audit: not yet performed.
