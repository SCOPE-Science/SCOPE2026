# Self-review

**Claim.** Exact \(01\)-occurrence discrepancy along \(N_r=(3^r-1)/2\) in the ternary base-three digit-sum word, with sharp \(2\)-letter balance and failure of factor balance.

## Correctness — PASS
The carry relation \(t(n+1)-t(n)\equiv1+c(n)\pmod3\) reduces the statement to an exhaustive digit partition indexed by the highest digit differing from the all-ones bound. Contributions for trailing-two lengths smaller than, equal to one below, and equal to the free-digit count yield the three residue classes. The primitive morphism establishes \(01\) frequency \(3/13\) and sharp letter balance. Standalone enumeration confirms all exact formulas through \(r=12\), but infinite truth depends on the written proof.

## Originality — PASS (best knowledge)
The closest same-object reference is Balková's generalized Thue–Morse factor-frequency theorem (arXiv:1107.5033); it establishes limiting frequencies, not the finite all-one-prefix law. Espinoza–Popoli–Stipulanti (arXiv:2602.03746, first public February 3, 2026) establishes broader factor-balancedness criteria and the discrepancy/balance equivalence, but not this explicit counterexample computation. Spiegelhofer (arXiv:2102.01018) treats adjacent \(01\) discrepancy in the **binary base-two**, not ternary base-three, word. Relevant published exact dyadic single-letter and base-three Parikh results in published-finding corpus have different bases, invariants and quantifiers. No exact duplicate was identified. A broader unindexed digit-sum summation law remains an important priority risk.

## Mathematical value — PASS
This is an exact infinite family of naturally indexed factor-count discrepancies in a canonical automatic word. Its carry-layer derivation explains persistent oscillation and proves that the word is sharply letter-balanced while a fixed two-letter factor has unbounded discrepancy. The separate arithmetic formulas quantify the failure, rather than merely exhibiting one unbalanced factor.

## Scope and limitations
The factor frequency and the general balance/discrepancy equivalence are inherited. No universal statement for other generalized Thue–Morse parameters, nor a global sharp discrepancy envelope, is claimed. Finite computation is supplemental. Full external priority assessment and independent mathematical validation have not occurred.

Self-review: passed. Independent audit: not yet performed.
