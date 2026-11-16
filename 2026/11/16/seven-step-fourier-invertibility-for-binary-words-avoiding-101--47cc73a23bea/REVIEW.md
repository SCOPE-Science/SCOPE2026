# Scientific assessment

## Correctness
**PASS.** The three-state automaton encodes exactly the forbidden factor \(101\). Its length-generating transfer matrix gives an order-seven parity period modulo two. The three exact eigenvector identities for seven-step signed blocks give an explicit zero coefficient for every singular residue and a coefficient of one for every nonsingular residue. Matrix products in the proof have the stated lengths and signs, including lengths one, two, and three. Counting convolution is diagonal in the Walsh character basis, so the minimum coefficient magnitude gives the claimed Hilbert-space inverse norm. The standalone checker confirms the defining matrix identities, the witness products to length 120, and every frequency through length 17. Finite tests are supporting checks; the identities prove all lengths.

## Originality
**PASS under bounded literature comparison.** The closest papers are Bilotta–Grazzini–Pergola–Pinzani (2012, arXiv:1210.7620), on generating alternating-pattern-avoiding **balance-constrained** words, and Bilotta–Grazzini–Pergola (2013, Journal of Integer Sequences 16, 13.4.8), on their generating functions. Their counting questions are not full coordinatewise signed Fourier sums. A related published Fourier result for graph-exclusion sampling concerns a restriction matrix, not counting convolution by this avoidance indicator. Existing Fourier work on other forbidden-word and independent-set families is not an implication: the present word counts and forbidden local rule differ. Full historical coverage cannot be guaranteed; the possible existence of an earlier equivalent signed-automaton theorem remains a residual risk.

## Value
**PASS.** The zero-free condition is an infinite and exact, natural spectral classification for a simple regular language, with a sharp inverse-stability constant in every invertible dimension. The period seven is not a cosmetic relabeling: two nontrivial invariant-vector relations create explicit resonant sign patterns at exactly the three remaining residues. Ordinary word counts detect only the safe odd-cardinality classes; the proof supplies the converse singularity and exact frequency witnesses, which the unsigned enumeration alone cannot establish.

## Scope of validation
All algebraic steps have exact integer proofs and direct finite spot checks. Exact singular nullities, endpoint projection constants and other forbidden factors are not determined. Historical-priority verification was bounded. Independent mathematical validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
