# Twisted half-turn fixed matching complexes of twelve- and fourteen-column circular ladders

## Finding

For \(k\ge3\), set \(P_{2k}=C_{2k}\square K_2\), where \(C_{2k}\) has vertices \(i\in\mathbb Z/(2k)\), and let the involution \(\tau\) act by \(\tau(i,a)=(i+k,1-a)\) on the two layers. Let \(\mathcal M(G)\) be the **ordinary matching complex**: its vertices are all graph edges and its simplices are **all** collections of pairwise disjoint graph edges. Then

\[
|\mathcal M(P_{2k})|^{\langle\tau\rangle}\cong_{\mathrm{PL}}|\mathcal M(M_{2k})|,
\]

where \(M_{2k}\) has vertices \(0,\ldots,2k-1\), rim edges \(\{i,i+1\}\) (indices modulo \(2k\)) and antipodal chords \(\{i,i+k\}\), \(0\le i<k\). For the two widths \(2k=12,14\), the **integral homotopy types** are

\[
|\mathcal M(P_{12})|^{\langle\tau\rangle}\simeq\bigvee^{10}S^3,
\qquad
|\mathcal M(P_{14})|^{\langle\tau\rangle}\simeq\bigvee^{16}S^4.
\]

All reduced integral homology vanishes outside the indicated degrees and is respectively \(\mathbb Z^{10}\) and \(\mathbb Z^{16}\) in those degrees.

## Assumptions and scope

The metric plays no role: these are **ordinary simplicial matching complexes**, not Vietoris--Rips complexes and not complexes generated only by perfect matchings. The fixed space is the *geometric* fixed set after realization, not the subcomplex of individually fixed edge vertices. The PL identification holds for every integer \(k\ge3\); the sphere-wedge homotopy computations are asserted only for \(k=6\) and \(k=7\). The involution rotates the cycle by exactly half its circumference **and exchanges its two layers**.

## Proof

**Orbit model.** The involution is free on the \(4k\) graph vertices. Its vertex orbits can be labelled by \(i\in\mathbb Z/(2k)\) using \(\{(i,0),(i+k,1)\}\). Each horizontal edge at the upper layer is paired with one horizontal edge in the lower layer; this orbit projects to one rim edge of \(M_{2k}\). Each vertical rung at column \(i\) is paired with the rung at \(i+k\), and the pair projects to one antipodal chord of \(M_{2k}\). The resulting \(3k\) graph-edge orbits are precisely the \(3k\) edges of \(M_{2k}\). Each edge orbit consists of two disjoint edges.

A point in the geometric realization of a simplicial complex is fixed by a vertex permutation exactly when its barycentric coordinates are constant along each vertex orbit, with the support a union of full orbits. Thus the fixed space is PL-homeomorphic to the simplicial complex whose vertices are *admissible complete graph-edge orbits*. Two such orbit vertices can appear together exactly when their four-vertex supports in \(P_{2k}\) are disjoint. Since the supports are unions of free graph-vertex orbits, this happens exactly when their projected quotient edges are disjoint. Consequently the orbit complex is the ordinary matching complex of \(M_{2k}\), proving the natural PL identification. This argument has no finite-enumeration restriction.

**Complete acyclic face-poset reduction.** For \(k=6\) or \(k=7\), enumerate all graph matchings of \(M_{2k}\), including the empty simplex. Index its \(3k\) edges in the order: \(2k\) successive rim edges \(\{i,i+1\}\) for \(i=0,\ldots,2k-1\), followed by the \(k\) chords \(\{i,i+k\}\) for \(i=0,\ldots,k-1\). In stage \(j\), among the faces not paired in earlier stages, pair every face \(\sigma\) not containing edge \(e_j\) with \(\sigma\cup\{e_j\}\), if the latter is present. Remove all stage-\(j\) pairs, and continue. This matching is fully specified by the preceding deterministic rule, without a hidden certificate or arbitrary choices.

For \(k=6\), there are \(1102\) faces including the empty face, with nonempty face vector \((18,117,336,420,192,18)\), indexed by dimensions \(0\) through \(5\). The procedure gives \(546\) pairs and exactly \(10\) unmatched faces, all of dimension \(3\).

For \(k=7\), there are \(3546\) faces including the empty face, with nonempty face vector \((21,168,644,1225,1085,371,31)\), indexed by dimensions \(0\) through \(6\). The procedure gives \(1765\) pairs and exactly \(16\) unmatched faces, all of dimension \(4\).

To check *global* acyclicity rather than merely count unmatched faces, orient every codimension-one Hasse edge upwards, reversing the edge of each matched pair. A complete topological sort of these directed graphs terminates after all \(1102\), respectively all \(3546\), faces; the checked Hasse edge counts are \(4008\) and \(15057\). The standalone program reproduces the enumeration, pairing and full directed acyclicity test from the graph definitions.

Because the empty face is paired, the augmented acyclic matching gives a CW model with a basepoint and only the \(10\) critical \(3\)-cells in the first case, or only the \(16\) critical \(4\)-cells in the second. For positive-dimensional spheres, attaching a cell to a single \(0\)-cell without intermediate positive-dimensional cells is necessarily by a nullhomotopic map. Hence these CW models are the stated wedges of spheres. This is a homotopy-type argument over \(\mathbb Z\), not an inference from field Betti numbers alone.

## Verification

Run `python verify_twisted.py` (Python standard library only). The independent routine constructs all graph edges in both layers and their actual orbits under \(\tau\), and checks that the full orbit-face complex equals the Möbius graph matching complex, not just that the two have the same face counts. It then regenerates all faces, constructs the deterministic matching, verifies every full-Hasse reversal is acyclic by topological sorting, and calculates independent reduced mod-two boundary ranks. Its reproducible terminal output is included in `verification_output.txt`. The mod-two Betti dimensions and multiplicities agree with the unrestricted integral consequences of the acyclic matching.

## Relationship to prior work

Agarwal and Basak, *The Homotopy Types of the Independence and Perfect Matching Complexes of Möbius and Circular Ladder Graphs* (first publicly available August 31, 2026; arXiv:2608.30601), determine homotopy types of **independence** and **perfect matching** complexes. Their use of the phrase 'perfect matching complex' denotes the complex generated by extendable perfect matchings, a proper subcomplex of the **ordinary** matching complex studied here. Their results do not imply the present exact ordinary matching complexes at twelve and fourteen vertices, or the twisted fixed-set identification. Nearby published computations for other Möbius ladder lengths and symmetry characters concern different graphs or spaces; these do not imply the two stated integral wedge types. Equivalence under alternative nomenclature remains a literature-overlap risk.

## Limitations

The all-width structural statement identifies the fixed complex with a Möbius-ladder matching complex, but does **not** classify that matching complex for every width. Only widths twelve and fourteen have the computed wedge types, and only the combined half-turn/layer-exchange involution is considered. Nothing is claimed about all other automorphisms, equivariant homotopy splittings or simple-homotopy uniqueness. Literature coverage cannot exclude every unindexed equivalent result. Independent mathematical audit has not been performed.

## References

1. A. Agarwal and B. Basak, *The Homotopy Types of the Independence and Perfect Matching Complexes of Möbius and Circular Ladder Graphs*, arXiv:2608.30601, initial public posting 2026-08-31, revised 2026-09-14. https://arxiv.org/abs/2608.30601
2. Standard discrete-Morse theory for face-poset acyclic matchings and reduced CW models; the complete finite matching and verification algorithm here are self-contained in `verify_twisted.py`.
