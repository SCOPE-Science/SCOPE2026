# Review of secure-guard spectra and exact relocation distances on the Pappus incidence graph

## Correctness — PASS

The claim is finite and precisely scoped to the 18-vertex affine incidence graph with points \(P(x,y)\), lines \(L(m,b)\), and incidence \(y=mx+b\pmod3\). Security is equivalent to domination followed by a successful adjacent-guard swap against every unselected vertex; the private-neighborhood lemma justifies this directly. The primary certificate enumerates all \(262144\) vertex subsets, not a sample, and tests every possible candidate guard. The independent C++ checker reconstructs neighborhoods and recomputes domination afresh after each proposed guard replacement. Both run successfully. A separate complete search over the \(1755\) optima checks every jump or slide and uses breadth-first search from every optimum for the exact radii and diameters. The affine-plus-duality group action is explicitly verified on edges. The group order is independently known to equal \(216\), establishing that the computed orbit decomposition uses all graph automorphisms.

## Originality — PASS, with publication-priority risk

Full-text inspection of Haythorpe–Newcombe, arXiv:2103.01406, located graph-specific formulas for narrow Cartesian products of paths/cycles and Möbius ladders, not for the Pappus incidence graph. Full-text inspection of Křišťan–Svoboda, arXiv:2307.10847, found ordinary domination token-slide algorithms for trees/interval graphs, not secure-domination reconfiguration on Pappus. The exact Pappus affine model is classical (Stokes); its graph automorphism order is not new. Targeted bibliographic searches for Pappus secure domination, its polynomial, minimum-size count, and guard relocation found no covering statement. The closest indexed mathematical findings concern secure domination on **different** Levi graphs (Heawood and Möbius–Kantor), and semitotal or locating-total domination on Pappus, which impose different feasibility conditions and neither prove nor imply this security census. No priority claim is made over inaccessible, unpublished, or unindexed sources; direct full text for the closest indexed records was not available.

## Value — PASS

The Pappus graph is a canonical smallest 18-vertex cubic arc-transitive graph, with a concrete 9-point/9-line configuration. A scalar domination number would omit most of its secure-guard placement geometry. The complete labelled cardinality polynomial, the unexpected \(3224\) larger inclusion-minimal configurations, both optimal movement networks and their exact distances, and the 13 symmetry types provide a natural, reusable finite benchmark for guard-placement enumeration, robustness, symmetry and reconfiguration algorithms. In contrast to the previously indexed slide-frozen Pappus locating-total optima, secure optima are all slide-connected; that comparison highlights a substantive dependence of mobility on the feasibility rule rather than on the underlying graph alone. This is a precise finite classification, not a claimed infinite-family or general-algorithm breakthrough.

## Scope and residual risks

All numeric certificates depend on executable exhaustive enumeration, with a second independent direct-swap formulation included. Neither proof nor claim generalizes automatically to other configurations or multiple simultaneous guard displacements. The full text of several closest indexed mathematical records could not be retrieved; bibliographic coverage cannot establish global priority. An external independent mathematical audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
