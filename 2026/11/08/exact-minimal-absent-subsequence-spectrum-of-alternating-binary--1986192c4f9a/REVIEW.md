# Self-review

## Correctness — PASS

For each nonempty candidate the earliest alternating-prefix embedding ends at \(v_{|v|}+2D(v)\), so scattered-subsequence containment is exactly \(D\le k-1\). Each one-letter deletion decreases the weak-descent statistic by either zero or one. Interior zero-loss deletions correspond exactly to \(010\) and \(101\); first and last deletions have zero loss exactly when their adjacent end pairs ascend. These facts prove the complete minimal-absence characterization, including boundaries. Weighted transitions on the four binary pair states yield the displayed exact rational bivariate series. Denominator multiplication establishes the recurrence, and its simple dominant positive pole establishes exponential growth. The finite verifier tests the predicted classification against direct greedy matching/deletion (not the same classification algorithm), and the length counts against an independent transfer dynamic program. The proof is valid for every integer \(k\ge1\).

## Originality — PASS (qualified)

The most relevant prior work is Kosche, Koß, Manea and Siemer, *Absent Subsequences in Words*, arXiv:2108.13968, especially Proposition 3.6: it studies the same \(B_k\) family but expressly assumes even alphabet size at least four in the exponential-MAS construction. The full binary case, the forbidden-triple characterization, and the bivariate spectrum are not implied. Adamson et al., arXiv:2407.18599, count all absent words of fixed length under universality constraints, while Manea et al., arXiv:2504.21471, design general MAS enumeration algorithms; neither states this exact periodic binary spectrum in inspected material. Targeted literature and semantic-index searches did not identify an equivalent. A full global novelty certification has not been performed, and differently presented exact formulas may exist.

## Mathematical value — PASS

The source literature specifically distinguishes polynomially many shortest absent subsequences from exponentially many minimal absent subsequences for higher even alphabets, without establishing the analogous binary behavior. This theorem resolves the smallest nontrivial alphabet with an exact size-and-length spectrum, a simple local characterization and a sharp exponential constant. It quantifies the output size of MAS enumeration on the canonical shortest binary complete-alphabet word family, and shows a linear number of shortest witnesses coexisting with exponentially many minimal witnesses. The exact count is a motivated invariant across all lengths, not a special-case numeral or routine rescaling.

## Remaining risks and scope

The theorem is restricted to alternating finite binary words and concerns *scattered* subsequences. The later algorithms and fixed-length all-absent counting papers were inspected for relevant scope but not exhaustively across every appendix. Unindexed equivalences or a table entry with the same sequence could exist. Finite verification is not an infinite proof; the proof appears in RESULT.md.

Self-review: passed. Independent audit: not yet performed.
