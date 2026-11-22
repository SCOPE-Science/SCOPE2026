# Self-review

## Correctness — PASS

The claim concerns the coprime packet parameter, not unrestricted group generation. For a cyclic action each nontrivial stabilizer quotient is cyclic, with one minimal base generator of intrinsic order equal to the orbit index. Thus valid packets correspond bijectively to graph independent sets. The squarefree prime construction has unique vertex primes and edge primes, proving the exact adjacency relation and distinct stabilizers. The associated automorphism group is a product of cyclic quotients, with Sylow ranks one or two, so its rank is exactly two whenever the input graph has an edge. The binary-size polynomial reduction uses at most \(|V|+|E|\) small primes, and same-packet gcds provide NP membership. A separate finite checker confirms the construction on all \(1099\) labelled graphs on at most five vertices, the two generators in the \((6,10,15)\) example, and complete-graph families through eight vertices. Computation is finite corroboration, not the proof of universality or NP-completeness.

## Originality — PASS, with priority limitations

The motivating 2026 preprint and journal article were inspected at their definitions of packets, coprime merging lemma, grouping procedure, and open problem. They supply the **definition and criterion**, but do not state the cyclic-action graph-universality theorem, an NP-hardness reduction for the packet parameter, or the two-generated unbounded inefficiency construction. The 2022/2023 Castillo-Ramírez–Ruiz-Medina theorem concerns relative rank of the full equivariant endomorphism monoid modulo its unit group, which does not determine minimum coprime packet partitions. published-finding corpus searches for the source, aliases, chromatic formulations, and complexity did not reveal a covering record. The closest wreath-product relative-rank item likewise targets a different generation invariant. The proof deliberately credits the classical universality of intersection graphs, elementary finite-abelian rank, and NP-completeness of three-colorability. Priority remains provisional because records can be unindexed and one related published research record was available only in summary.

## Mathematical value — PASS

The recent source explicitly asks for a structural understanding of its packet parameter. This result gives the complete answer for cyclic actions as a graph invariant, identifies a computational boundary even on squarefree cyclic groups with very simple orbit data, and demonstrates that optimal **packet** generation can be arbitrarily worse than genuine generation of the same abelian unit group. These are not merely a finite census or a rephrasing of the paper's upper bound: the family realizes every graph while holding true unit-group rank equal to two. The result is limited to this packet method and to the stated succinct complexity encoding.

## Closest literature and limitations

- Lara-Gómez, Romero-Rosales and Ruiz-Medina, *Finite generating sets for monoids of \(G\)-equivariant functions*, arXiv:2607.04053 (2026-07-04), Sections 2.1 and the packet open problem; and *Semigroup Forum* (2026-11-02), DOI:10.1007/s00233-026-10690-y, Section 3.1.
- Castillo-Ramírez and Ruiz-Medina, *The relative rank of the endomorphism monoid of a finite \(G\)-set*, arXiv:2203.12158, introduction and relative-rank theorem.
- Classical graph chromatic number/three-colorability and finite-abelian-group generator-rank results are used as known input.

The complexity theorem is for a binary quotient-index input, **not** a permutation list of all points. The new result does not provide the unrestricted rank of all equivariant endomorphism monoids, nor a choice-independent formula for the packet parameter of noncyclic groups. Independent mathematical validation and a comprehensive historical-priority audit remain unperformed.

Self-review: passed. Independent audit: not yet performed.
