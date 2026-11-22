# Scientific review

## Correctness
The finite degree-spectrum inequality and its cycle-rank strengthening were reconstructed with all quantifiers: selecting one left vertex for each distinct positive count gives \(|E(H)|\ge T_q+q\), hence \(\beta_1(H)\ge T_q-k+1\). This yields the finite girth converse. The published 2026 aperiodicity lower bound and cycle-to-excess implication have the required hypotheses because the supports are infinite with arbitrarily long gaps. A graph with exactly one simple cycle cannot support a witness with two independent cycles, fixing the unicyclic first defect. The specified three-weight graph has exactly one cycle, and distant additions preserve its cycle rank; an explicit tagged pattern realizes every required count.

Two independent scripts executed from the extracted candidate paths. `check_girth.py` confirmed graph rank and girth in 40 finite cases; `check_witness.py` checked 77 designated translates and additional zero/one witnesses. Both completed successfully. These checks corroborate, but do not prove, the all-parameter theorem.

## Originality
The closest primary paper is Zeng–Xue–Zeng (arXiv:2609.28059), which supplies the aperiodic lower bound, the qualitative forest criterion and the implication from a cycle to a complexity excess. The new assertion is the converse at every finite triangular cutoff and exact unicyclic first-defect index/value. The full public RESULT.md of the shifted-geometric girth classification and the three-spike cycle-rank classification was inspected; both supply graph data but neither the general finite cutoff nor the unicyclic complexity claim. The finite three-spike cycle-rank formula is credited as prior coverage.

Residual historical-priority risk: a previously unindexed reformulation of the quantitative converse may exist, and an implicit corollary of the 2026 source may have been overlooked.

## Value
The statement gives a genuine inverse relationship: a word-complexity statistic recovers the shortest cycle of an infinite additive graph. The unicyclic theorem recovers the exact first defective pattern arity and exact size of that defect; realizations at every even girth show that minimal complexity can persist for arbitrarily many pattern lengths despite a genuine cycle. The invariant and cutoff are dictated by the central forest characterization, not an arbitrary finite computation.

## Scientific limitations
The general inverse assumes infinite supports with arbitrarily long zero gaps, while exact first-defect arity requires one global simple cycle. Multi-cycle graphs may deviate at intermediate arities. The cycle-to-excess direction and aperiodic lower envelope are previously proved inputs, not new claims. No independent audit is asserted.

Self-review: passed. Independent audit: not yet performed.
