# Review of exact residual entropy in the three-state Apollonian Potts antiferromagnet

## Correctness — PASS
The object is the triangular Apollonian graph obtained by splitting only newly created bounded faces, with three labeled spin colors and equal positive cost on every monochromatic edge. The proof isolates the outer boundary edges, gives an exact minimum-plus-multiplicity recursion on all 27 fixed boundary triples, proves the invariant boundary-energy pattern \((x,x+1,x+2)\), and enumerates all possible minimizing center colors. The cubic count recurrence and root multiplicity follow with no hidden independence assumptions because descendants share only fixed boundary spins. The entropy expansion follows from explicit scalar log recurrences and their summable errors. The independently encoded small-graph and transfer-state checks agree. Neither finite enumeration nor numerical evaluation is used as proof of the infinite-genesis result. No unresolved correctness premise was found.

## Originality — PASS on examined evidence
Andrade–Herrmann, arXiv:cond-mat/0411364v1 (2004-11-14), studies the two-state Ising model including antiferromagnetism and a different residual-entropy number, not three-state minimum-frustration colorings. Araújo–Andrade–Herrmann, arXiv:1007.4494v1 (2010-07-26), develops Potts transfer matrices but explicitly evaluates homogeneous ferromagnetic interactions; its cited general machinery does not give the explicit three-state antiferromagnetic degeneracy recurrence, the entropy density, or the \(2^t\) finite-size correction. The chromatic-polynomial special case is inapplicable because this graph contains \(K_4\) and has no proper three-coloring. Published research-index and focused literature searches produced no claim implying this theorem. Historical literature not indexed or recovered remains a genuine priority risk; searching is not proof of uniqueness.

## Mathematical value — PASS
Three-state coloring is exactly the first Potts alphabet above the Ising case while remaining frustrated by the graph's four-cliques. The complete minimum-energy degeneracy is a natural zero-temperature observable for a scale-free hierarchical planar network already studied in the statistical-physics literature. Besides an all-generation exact census, the theorem identifies a nonzero intensive residual entropy and a universal-for-this-model stretched correction of order \(2^t\), i.e. a nontrivial system-size exponent \(\log_3 2\); neither reduces to a textbook proper-coloring count or a routine parameter substitution. It provides a quantitative benchmark for future treatments of frustration and boundary effects. There is no claim of finite-temperature criticality.

## Closest literature and residual limitations
- R. F. S. Andrade and H. J. Herrmann, *Magnetic models on Apollonian networks*, arXiv:cond-mat/0411364v1, 2004: closest same-network antiferromagnet, but with two Ising states.
- N. A. M. Araújo, R. F. S. Andrade and H. J. Herrmann, *q-state Potts model on the Apollonian network*, arXiv:1007.4494v1, 2010: same Potts framework and graph, but ferromagnetic model.
- R. Shrock, *Ground state entropy in Potts antiferromagnets*, Physica A 281 (2000): general context for antiferromagnetic residual entropy; the accessible abstract does not address the present graph and the complete text was not inspected.

The proof treats precisely the stated graph inflation, three colors, equal couplings and zero field. Historical priority remains provisional until an independent literature audit, and no independent scientific validation is asserted.

Self-review: passed. Independent audit: not yet performed.
