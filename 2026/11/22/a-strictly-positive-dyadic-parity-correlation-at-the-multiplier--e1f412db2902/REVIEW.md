# Scientific review: dyadic digit-parity correlation at multiplier \(7\)

## Correctness — PASS

The identity is reduced to a finite seven-carry transfer calculation valid at every binary length. Each digit transition computes the low product digit and the next carry, with transition sign \((-1)^c\). The final tail digit sum is included in the terminal vector, avoiding a common truncation error. Direct multiplication gives \((M^4-M-2I)v=4(e_2-e_4)^{\mathsf T}\); the accessible rows satisfy \(w_2=w_4\) by an invariant established from the explicit row-update equations. This proves the recurrence for all nonnegative lengths. The listed first four values and the nonnegative recurrence coefficients establish strict positivity without extrapolating a finite experiment. An independent direct implementation agrees at lengths zero through fifteen, and exact transfer identities are checked by `verify_correlation.py`. Coprimality of the rational numerator and denominator gives the minimal third-order recurrence. The only domain is complete dyadic intervals, beginning at zero, for fixed multiplier seven.

## Originality — PASS with residual literature risk

The closest checked published formulas treat the pair \(n,3n\), the multipliers \(2^k+1\), or a three-way correlation of \(n,3n,5n\), rather than the pair \(n,7n\). Neither the multiplier-three claim nor the two-one multiplier family entails a formula for seven: \(7\) does not belong to the displayed parameter family, and their hypotheses do not provide a reduction. Spiegelhofer's 2023 work [1], examined in the introduction and Section 4.3, uses digit-parity correlations to treat cubes, not the exact fixed-multiplier finite-block problem. Searches for the seven-multiplier statement, its first terms and rational generating function did not identify matching published coverage; this absence is not proof of global uniqueness. Mauduit's 2002 survey [2] is plausible broad background; only its abstract and bibliography could be read, so its uninspected body remains a concrete originality risk. A complete comparison of that unavailable source is not claimed.

## Value — PASS

The digital sum along two linked arguments is a natural multiplicative correlation observable. For the first three-one positive multiplier, \(7\), the finite dyadic excess has a persistent positive sign at *every* scale, which contrasts with the documented oscillatory three-multiplier case and the initial zero values of the two-one multipliers. The seven-state signed automaton has an unexpected two-coordinate cancellation that yields a minimal order-three recurrence, plus a separate positive order-four relation that proves all-scale positivity. The specific sign law and low-order formula, not generic rationality of automatic-sequence generating functions or finite computation alone, are the motivated contribution. The fact is restricted to multiplier seven, not a classification of general multipliers.

## Sources and limitations

[1] L. Spiegelhofer, *Thue–Morse along the sequence of cubes*, arXiv:2308.09498, initially posted 2023-08-18; full text, especially pp. 2–3 and section 4.3. https://arxiv.org/abs/2308.09498

[2] C. Mauduit, *Multiplicative properties of the Thue–Morse sequence*, Periodica Mathematica Hungarica 43 (2002), 137–153; abstract and bibliography only. https://doi.org/10.1023/A:1015241900975

[3] *Exact oscillatory parity correlations at binary triples* (2026), published result summary. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-oscillatory-parity-correlations-at-binary-triples--4ded471daa94

[4] *Exact dyadic multiplicative correlations for two-one binary multipliers* (2026), published result summary. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-dyadic-multiplicative-correlations-for-two-one-binary-mult--50b8d332f4b5

The result's proof is self-contained apart from elementary binary arithmetic and rational generating-function algebra. Direct enumeration checks only finitely many lengths and is not a substitute for the invariant proof. Literature overlap risk remains for inaccessible full text and unindexed equivalent statements.

Self-review: passed. Independent audit: not yet performed.
