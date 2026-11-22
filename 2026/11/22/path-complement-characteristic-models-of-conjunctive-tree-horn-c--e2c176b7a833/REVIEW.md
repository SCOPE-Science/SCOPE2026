# Scientific review

## Correctness

PASS. The closure condition in omission coordinates forces a downward missing path from each missing vertex. These paths are exactly the inclusion-minimal omission sets containing their start vertex; the finite-lattice maximal-omitter characterization then gives all and only meet-irreducibles. Each leaf supplies one path of every possible length from one to its depth plus one, giving the exact spectrum, inversion and total count. The sharp lower and upper bounds follow from descendant-leaf incidence counting and are attained by the specified rooted paths and brooms. A separately programmed brute-force checker verified all 18,249 rooted labelled trees on at most seven vertices, covering 2,238,526 candidate subsets. Universal claims rest on the proof, not this finite enumeration.

## Originality

PASS within inspected evidence. Babin (2026), arXiv:2607.18534, gives general closure-representation hardness and the standard maximal-omitter lemma; it does not give the tree-path spectrum or exact extremal count. Defrain–Ohana–Vilmin (2025), DOI 10.4230/LIPIcs.ISAAC.2025.24, prove general incremental-polynomial enumeration under bounded conclusion-degree, a superclass of these tree systems, but their relevant full HTML sections do not specialize to this exact polynomial or the extremal brooms. Nourine–Vilmin (2023), arXiv:2202.05536v2, has a recursive acyclic-split decomposition framework; the full accessible HTML was inspected, especially Sections 3 and 4.2. Its tree represents partitions of an implicational base, not the input dependency graph, and the exact leaf-depth polynomial and sharp extremum are not stated. Its broad recurrence may nonetheless be specialized to recover the claim, an acknowledged historical-scope risk. No matching title or equivalent statement appeared in six meaning-based published-finding corpus searches or searched literature phrases. An absence of matches is not proof of novelty.

## Value

PASS. Characteristic models are the unique irredundant intersection representation of finite Horn closure systems. For a natural degree-at-most-two tree-dependency class, the result specifies every model without generic enumeration, gives an exact size distribution that recovers the tree's leaf-depth histogram, and identifies sharp best- and worst-case canonical output sizes. This is a complete structural classification with a natural inverse invariant, rather than a numeric computation or a restatement of a general decidability result.

## Scope and limits

The premises are whole child sets; the theorem is not about arbitrary acyclic Horn bases, separate unary child rules, or shared-subgraph DAGs. The earlier enumeration theorem covers algorithmic feasibility, not the claimed exact classification. A broadly implicit earlier derivation remains possible. Independent mathematical and priority audits have not been performed.

Self-review: passed. Independent audit: not yet performed.
