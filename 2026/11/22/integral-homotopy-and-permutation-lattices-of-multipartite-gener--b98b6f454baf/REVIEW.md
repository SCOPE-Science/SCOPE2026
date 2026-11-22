# Self-review

## Correctness — PASS
For every complete multipartite graph with at least two nonempty parts, the known general-position face condition gives the exact simplicial union \(X=(D_1*\cdots*D_t)\cup\bigcup_i\Delta(V_i)\). The simplex intersections are exactly their discrete vertex sets. Attaching a contractible simplex along \(a_i\) disconnected vertices adds \(a_i-1\) circles. The join of discrete vertex sets has \(\prod_i(a_i-1)\) top-dimensional spheres. The natural relative homology sequence and integral join chains identify the actual augmentation modules, including the signed factor exchanges. For two parts the independent collapse to a two-vertex multigraph proves the separate integral cross-edge cycle lattice. Maximal-face sizes and the low-degree homology obstruction prove the non-shellability assertion.

The standalone `verify.py` independently checked all 112 eligible labelled part-size vectors with 2–4 parts, part sizes 1–3 and total order at most 10; tested 6,984 candidate faces against graph distances; compared all Betti ranks over two prime fields; and checked the signed two-cycle symmetry. Result: `VERIFY_OK cases= 112 faces_checked= 6984 primes=2,101 orientation=PASS`. The computer checks support but do not replace the all-order proof or certify torsion-freeness.

## Originality — PASS, with priority risk
Rather, *Explicit Formulas and Unimodality Phenomena for General Position Polynomials*, arXiv:2603.06930 (2026), **already proves the full multipartite general-position face characterization and polynomial**. These are inputs, not new results. Earlier Iršič–Klavžar–Rus–Tuite, arXiv:2401.05696, develops the general-position-polynomial framework, while Anand–Chandran–Changat–Klavžar–Thomas, arXiv:1812.08460, establishes the foundational geodesic-set characterization. Their accessible relevant texts did not give the integral homotopy classification, signed part-permutation lattices, or pure non-shellable families. Comparison with indexed complete-multipartite total-visibility, path-avoidance, and induced-forest complexes found different defining faces, not an implication to this theorem. Some indexed records could not be inspected in full and mathematical priority remains provisional.

## Mathematical value — PASS
This is a complete, all-order integral topological and group-action classification for the natural configuration complex of an established graph-position invariant. It simultaneously gives exact fundamental groups, torsion-free homology in two dimensions, the actual integer (not only rational-character) permutation modules, and an infinite family of pure but non-shellable complexes. The lattice and purity statements are not recoverable merely from a face-count polynomial. The result is not presented as a new enumerator.

## Closest literature and limitations
- Iršič et al., *General Position Polynomials*, https://arxiv.org/abs/2401.05696 (first public 2024-01-11).
- Rather, *Explicit Formulas and Unimodality Phenomena for General Position Polynomials*, https://arxiv.org/abs/2603.06930 (first public 2026-03-06), especially multipartite statements.
- Anand et al., *Characterization of general position sets and its applications to cographs and bipartite graphs*, https://arxiv.org/abs/1812.08460 (first public 2018-12-20).

The wedge decomposition is nonequivariant; its separate homology modules identify automorphism actions. No claim is made about more general graphs or other visibility variants. Equivalent topological formulations may have escaped indexing. Independent validation and comprehensive publication-priority review remain outstanding.

Self-review: passed. Independent audit: not yet performed.
