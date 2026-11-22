# Scientific assessment of the rectangular rook majority equilibrium classification

## Correctness — PASS

The open-neighbor count is \(r_i+c_j-2x_{ij}\), giving the sharp conditions \(r_i+c_j\ge(m+n)/2+1\) at ones and \(\le(m+n)/2-1\) at zeros. Alternating submatrices are impossible, giving unique Ferrers representatives. Ferrers corner checks are precisely the two-barrier path conditions. An invertible two-column insertion removes aspect-ratio dependence within parity. The final path counts follow from an explicitly derived rank-one peak-transition kernel, rather than finite extrapolation. Standalone exhaustive partition/word checks and small labelled-state enumerations agree. Boundary cases \(m=1\), \(m=n\), and opposite-parity \(n=m+1\) are included. Risk: independent proof-checking is not performed; algebra and combinatorial reasoning have only received same-model scrutiny.

## Originality — PASS, qualified

The square case \(2^n\) and Ferrers nesting are prior work, not new. This claim determines a new genuinely rectangular invariant, showing stability when the longer dimension increases by two, and an unexpected parity alternation between \(2^t\) and coefficients of \(1/(1-2z+z^2-z^3)\). The complete inspected Benjamini et al. majority paper treats period-two behavior and random graphs. The inspected Bujtás et al. Cartesian-product paper maximizes the number of colors of majority C-colorings rather than enumerating two-color equilibria. Related published records describe three-row rook transients and a general line-graph two-cycle reduction, neither implying the all-rectangle fixed-class count. OEIS A005314 already indexes the opposite-parity sequence in other combinatorial contexts, so the integer sequence is not novel. Risk: published full text of the three-row rook-transient record and older unindexed equivalent theorems could not all be examined.

## Value — PASS

The graph family is the line graph of a complete bipartite graph and a basic two-factor Hamming graph. Exact fixed-state class counts quantify the multiplicity of stable opinions and their dependence on board anisotropy. Holding the short dimension fixed while increasing the long dimension does not create additional equilibrium types, yet increasing the longer side by just one can change the growth base from \(2\) to approximately \(1.7548776662\). This is a natural complete classification with a structural proof, not a forced parameter substitution or a mere known-table recomputation. The comparison concerns quotient-class counts and should not be mistaken for labelled populations.

## Closest literature and scientific limits

Benjamini et al., arXiv:1405.2486 (2014), supply the period-two setting. Bujtás et al., arXiv:2608.27669 (2026), treat the color-maximization invariant on the same graph. The earlier square-board classification is subsumed and explicitly credited. OEIS A005314 records the recurrence and sequence but not this graph interpretation in the retrieved evidence. An accessible published summary on three-row rook relaxation does not establish the present fixed-point formula. Unindexed equivalences remain possible, and no independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
