# Scientific assessment: doubled joined polygon boundaries

## Correctness — PASS
The source \(X_{m,n}=C_m*C_n\) is a three-dimensional simplicial sphere; its tetrahedral facets are precisely products of a cycle edge in each factor. Each tetrahedron contributes exactly three complementary-edge pairs. Their edge-type decomposition proves the full simplicial graph isomorphism \(D^2(X_{m,n})\cong K_{m,n}\sqcup(C_m\times C_n)\). The connectivity of the categorical cycle product is proved directly by parity and synchronized walks, and integral graph homotopy is determined by spanning-tree contraction. The dihedral geometric quotient argument explicitly accounts for edge inversions. A standalone code package reconstructs the double independently from all facets for 49 ordered finite parameter pairs and checks the graph formula, component ranks and symmetry orbit claims; those finite checks corroborate but do not substitute for the unrestricted proof.

## Originality — PASS (best knowledge, residual literature risk)
The primary introducing source (Lesh–Schreiner–Wahl, arXiv:2506.10436, first public 2025-06-12) provides the definition and a weak Cohen–Macaulay connectivity theorem, not this graph decomposition or quotient. The closest indexed exact 3-sphere-double calculation concerns cyclic four-polytope boundaries, which have complete one-skeleton unlike \(C_m*C_n\) for \(m,n\ge4\). Another indexed join-double example has a six-dimensional source sphere and a two-dimensional double; a separate iterated-tupling theorem is inapplicable to a first double. Searches under 'opposite-edge graph', 'categorical/direct/Kronecker product', joins of cycles/polygon boundaries and the exact graph formula found no equivalent theorem. The special direct-product connectivity step is classical; novelty is claimed only for its precise appearance in this double and the resulting full topological and orbit-space classification. Unindexed work under related terminology could still cover the statement; absence from searched records is not a uniqueness proof.

## Mathematical value — PASS
This is a uniform two-parameter classification of a natural polytopal three-sphere family for a recently introduced construction. It exhibits a parity-sensitive transition from two to three homotopy components and gives explicit integral circle multiplicities, in a family where the general connectivity theorem is too weak to distinguish these possibilities. It additionally determines the genuine factorwise dihedral orbit spaces, avoiding a subtle false circle produced by forgetting edge inversion. This exact combination supplies structural information for comparing doubles across natural source-sphere families; it does not assert a general result for arbitrary joins or higher tuples.

## Closest literature and limitations
- Lesh, Schreiner and Wahl, *The double of a simplicial complex*, arXiv:2506.10436, Definition 2.1 and Theorem A; primary full-text sections inspected.
- *Parity and dihedral homology of the doubled cyclic four-polytope boundary*, published mathematical record: distinct neighborly three-sphere family; full result and proof inspected.
- *A 710-sphere double of a join of two simplex boundaries*, published mathematical record: different source dimension and double dimension; full result and proof inspected.
- *Partition inflation and a composition law for iterated simplicial doubles*, published mathematical record: applies to iterated, not first, doubling; full result and proof inspected.

The proof does not identify full automorphism groups of the joined cycles in exceptional cases, nor a representation decomposition on first homology. The result is susceptible to an unindexed equivalent special case in older opposite-edge-graph research. Independent mathematical validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
