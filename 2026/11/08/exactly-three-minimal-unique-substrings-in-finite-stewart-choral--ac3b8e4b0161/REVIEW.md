# Scientific review: three minimal unique factors of Stewart choral iterates

## Correctness (C) — PASS

The unique middle discrepancy between \(\varphi^j(0)\) and \(\varphi^j(1)\) gives the block decomposition and three of the four repeated intervals. The fourth repeated interval is proved by an explicit induction on substitution boundaries. The four intervals cover every position with increasing endpoints, so any factor escaping all repeated intervals must include one of three bridges. A three-residue synchronization lemma proves unique occurrences for the two trimmed-image bridges; the remaining bridge is a unique left extension of a prefix occurring exactly twice. Each bridge's prefix and suffix are independently covered by repetitions. Consequently the three bridges are precisely the three MUSs, for every integer \(k\ge2\). The extracted independent-of-ledger code computes the same list for lengths \(9\) through \(19683\), using a suffix array and a direct factor census for small instances. Finite checks corroborate, but do not replace, the universal proof.

## Originality (O) — PASS, priority risk retained

Kishi et al. (arXiv:2605.18034v1) discuss occurrence-preserving morphisms and determine MUSs for the Fibonacci and Thue–Morse families. Their full-text theorems on those families do not assert the Stewart choral result. Fici–Shallit (arXiv:2112.12125v1), which explicitly identifies the Stewart choral morphism, studies critical exponent, pattern avoidance, palindrome factors, complexity and common factors; the inspected full text does not provide a finite-iterate MUS classification. OEIS A116178 records the classical word and its morphism, not the MUS classification. Searches for Stewart/choral/Toeplitz MUSs, occurrence-preserving formulations, and existing mathematical-record findings did not show a covering result. Previously encountered complete MUS classifications for other morphisms, including the period-doubling and Mephisto–Waltz words, have different defining substitutions; their formulas do not imply this statement. The absence of a search hit is not a proof of historical priority; a hidden equivalent or unindexed table remains possible.

## Value (V) — PASS

Minimal unique substrings are canonical shortest anchors for uniquely identifying regions of a string. Recent research explicitly seeks exact MUS structure for named morphic families. The complete fixed-count phenomenon in Stewart choral iterates is not inferred from the word's known factor complexity or cubefreeness: the exact three occurrence intervals and distinct linear-in-length MUS sizes require a four-block structural cover and a synchronization argument. This is a natural infinite-family classification, not a selected finite parameter or routine relabeling.

## Scope and risks

The result applies to canonical iterates of a single substitution, not every prefix or generalized Stewart word. The use of exclusive occurrence synchronization must not be mistaken for a claim of globally occurrence-preserving untrimmed substitution. The proof handles arbitrarily large iterates; the computation is finite diagnostic evidence. Possible unindexed prior equivalences and independent mathematical verification are unresolved.

Self-review: passed. Independent audit: not yet performed.
