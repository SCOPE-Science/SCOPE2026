# Review of the Franel character correlation spectrum

## Correctness — PASS

For \(F_n=\sum_{j=0}^n\binom nj^3\) the binomial Lucas congruence yields the exact modulo-five digit product with digit values \((1,2,0,1,1)\). Taking quadratic characters gives \((1,-1,0,1,1)\). Enumerating five possible outgoing digit carries produces the ordered correlation coefficients \((4,0),(0,1),(-1,0),(0,-1),(1,0)\), and hence the exact unwrapped recurrence. Induction on the nonnegative shift proves \(S_r(h)=4^r C(h)+b_h\), with integer \(b_h\), once the block is sufficiently long. The signed two-state transition is the identity and the unsigned transition is \(\bigl(\begin{smallmatrix}1+2t&2t\\2t&1+2t\end{smallmatrix}\bigr)\), proving the finite all-shift binomial spectrum. The zero predecessor is unique, yielding the sharp extremal equality cases. The standalone program checks 450 original sums, direct correlations, a complete finite spectrum and stabilized error constants. It is not used as an infinite proof.

## Originality — PASS, qualified

The central comparison is Z.-W. Sun, *Congruences for Franel Numbers* (arXiv:1112.1034), which proves congruences for weighted sums of Franel terms rather than a shifted joint quadratic-character spectrum. V. J. W. Guo's *Proof of two conjectures of Z.-W. Sun on congruences for Franel numbers* (arXiv:1201.0617) likewise studies weighted congruences. E. Rowland and R. Yassawi's *Automatic congruences for diagonals of rational functions* (arXiv:1310.8635) gives a more general automatic-congruence mechanism, which accommodates the *pointwise* digit factorization but does not state the evaluated signed shift spectrum, its exact multiplicity table or the extremal families. A related published result on all-lag central-trinomial residues modulo five concerns a different sequence and does not imply this digit-character law; a result on dyadic Pascal-row shift correlations has different digit weights. A recorded Franel modulo-nine joint-residue result also does not imply the modulo-five quadratic-character spectrum. Neither semantic searches nor text comparisons demonstrate absolute priority: earlier general digit-multiplicative correlation theorems may hide an equivalent specialization. This is an explicit residual risk.

## Mathematical value — PASS

The Franel quadratic character is supported on a thin fractal set of \(4^r\) indices within \(5^r\) and is therefore not addressed by an ordinary positive-density correlation limit. Normalizing by the natural active count reveals a complete, previously unresolved two-point statistic, including exact cancellation for half of all shifts, equal positive/negative multiplicities at every scale, and uniquely extremal shift families. The complete signed spectrum, rather than isolated sample values or a restatement of Lucas's theorem, is the motivating invariant. This provides a structural benchmark for correlations on digit-defined sparse arithmetic supports.

## Evidence and limitations

Relevant opening, theorem, selected proof and closing pages of the three primary arXiv PDFs were inspected; entire documents were not read exhaustively. The supplied verifier was executed successfully, and the proof has separately been reconstructed from its defining recurrences. Finite tests do not establish the result for every index or shift; those conclusions require, and follow from, the exact induction and two-state polynomial identities. General automatic-sequence literature remains a historical-priority risk. No independent validation has been performed.

Self-review: passed. Independent audit: not yet performed.
