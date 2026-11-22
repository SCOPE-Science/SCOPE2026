# Independent mathematical audit

## correctness

PASS

For T on (Z/5)^2 with exactly six adjacency increments ±(1,0), ±(0,1), ±(1,1), independently enumerated all cyclic row-compatible independent sets and obtained exactly 4216 faces including empty, with f=(25,225,900,1600,1140,300,25). A newly authored row-transfer/bitmask checker reconstructed the deterministic vertex-by-vertex matching on all 4215 nonempty faces: exactly 2074 disjoint genuine Hasse pairs, and unmatched cells 1x dimension 0, 51x dimension 3, 15x dimension 4. It traversed all 17225 nonempty Hasse covers and a Kahn topological sort visited all 4215 faces, proving exact acyclicity. Separately propagated integer incidence signs through all 1236 needed degree-3 gradient elimination states: every one of the 51x15 integral Morse differential entries vanishes. Independent direct GF2 boundary elimination returned ranks (24,201,699,850,275,25) in degrees 1..6. The Morse CW 3-skeleton is a wedge of 51 S^3 (no 1/2 cells) and its 15 4-cell attaching maps have zero classes in π3 ≅ H3 by Hurewicz, hence are null; the claimed integral wedge follows. This finite exhaustive certificate covers precisely this 25-vertex torus, not other sizes; archived VERIFY_OK alone is not used as proof.

## originality

PASS

Best-of-knowledge PASS for the nontrivial integral homotopy equivalence, not for already-known rational homology. The exact same 5x5 periodic triangular graph and its 66=51+15 ground-state ranks occur in Huijse et al. 2011, Appendix B.4; they do not establish nullity of all 4-cell attaching maps. Adamaszek 2012 proves homotopical splittings from dominating-transversal induced matchings but for separately specified lattice families, with no complete 5x5 triangular-torus decomposition. Jonsson 2010 concerns cross-cycle homology; original full text was not obtained this run, so full-document noncoverage is not asserted. The closest inspected earlier published SCOPE 5x5 hard-square result is the square Cartesian torus (4-regular), not the triangular (6-regular) torus. Specific exact-result and implication searches located this assigned record but no earlier dominating integral homotopy calculation. Residual historical priority risk remains material; absence of search hits does not certify novelty.

## value

PASS

The 5x5 periodic triangular hard-hexagon graph is a natural small two-dimensional frustrated fermion lattice already studied with exactly 66 rational ground-state classes. Those known ranks, especially in adjacent homological degrees 3 and 4, leave a genuine unstable integral homotopy ambiguity: 4-cell maps into a wedge of 3-spheres are not determined by rational ranks alone. A complete explicit acyclic Morse matching and integral zero attaching map resolve that exact natural finite invariant, yielding the full non-equivariant homotopy type and excluding torsion/other attachments for this specific physically motivated torus. The exact fact can be needed as a benchmark for larger triangular tori and further symmetry studies without pretending to solve an infinite-lattice problem. It is not merely recomputation of Huijse numbers or a renamed hard-square theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
