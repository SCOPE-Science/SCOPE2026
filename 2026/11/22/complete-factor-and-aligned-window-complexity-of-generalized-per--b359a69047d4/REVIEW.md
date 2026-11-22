# Scientific review: generalized period-doubling factor and window complexity

## Correctness (C): PASS

The defining valuation sequence satisfies the length-two substitution exactly. For every factor of length at least four, its parity of occurrence is unique because every global position congruent to one modulo four contains a `1`, and no even global position does. This gives disjoint injective decompositions and exact even/odd factor recurrences. Initial lengths one through three are evaluated directly, with the potential `000` intersection explicitly ruled out by adjacent-letter parity. The proposed piecewise deficit has exactly the same initial values and recurrences. The odd-window equality follows from the Chinese remainder theorem, and the doubling-invariance of aligned windows follows by injectivity of the substitution. This is a complete all-length proof. Exact finite residue-class enumeration and separate substitution-prefix checks test the mathematics through different representations; neither is substituted for proof.

## Originality (O): PASS, with specific priority risk

The June 2026 primary work on modulo recurrence and window complexity establishes a Thue–Morse window relationship, not the generalized period-doubling formula. The November 2025 generalized-period-doubling article develops kernel words and gap factorizations, not the stated all-length complexity and aligned-window laws. The binary factor-complexity formula is already known, and a November 2026 indexed result covers the nonbinary dyadic factor count; both are excluded from claims of novelty. Comparison by implication matters: dyadic special cases cannot determine arbitrary odd-length windows or non-dyadic factor complexity merely by logical restriction. The most relevant dyadic full text was not inspectable, so a stronger theorem or an independently derived equivalent is an unresolved historical-priority possibility; no search is treated as proof of uniqueness.

## Value (V): PASS

For an established, natural multi-alphabet automatic sequence, the exact full-length factor spectrum closes the non-dyadic gap in previously indexed enumeration, and the aligned-window spectrum provides a second distinct invariant. Its CRT-based odd-length saturation and dyadic collapse, from unbounded factor complexity to a constant number of aligned windows, explain a qualitative difference between ordinary and positioned factor sampling. This is an infinite classification across all alphabet sizes and lengths, not a routine finite test or an arbitrary isolated parameter value.

## Checks and limitations

The elementary even/odd recurrence, collision analysis at length three, two-branch deficit recurrence, Chinese remainder argument and window-doubling injection were reconstructed before acceptance. The separate exact-residue and morphic-prefix tests gave their stated finite passes. The main prior-work risk is incomplete material access to the full text of the indexed November 2026 dyadic article; independent expert review and independent validation remain unperformed.

Self-review: passed. Independent audit: not yet performed.
