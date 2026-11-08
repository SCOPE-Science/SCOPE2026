# Scientific review

## Correctness — PASS

The object is a numerical semigroup with exactly five minimal generators for every integer \(a\ge18\). The proof derives the exact coin-length recurrence, shows that the first ten-shift anomalies occur only at \(2,5,8\), and proves \(c(n+10)=c(n)+1\) for every \(n\ge10\) by a finite base table and a strict coin-count estimate for \(n\ge40\). A direct minimization argument proves \(W_r=r+a c(r)\) for every residue modulo \(a\); the generator-membership inequalities then classify pseudo-Frobenius elements. The ten explicit boundary sets are finite inequalities in the coin-length vector; the twelve transitional parameters \(18\le a\le29\) are checked directly. The least type period and boundary counterexample \(a=17\) follow by exact checks. The included Python verifier independently constructs Apéry sets by Dijkstra for 983 parameters and compares every pseudo-Frobenius number. Ten additional direct-reachability checks agree. Finite checks are corroboration, not a substitute for the infinite proof.

## Originality — PASS within inspected evidence

Targeted exact generator, type-vector, and pseudo-Frobenius searches located no identical classification in relevant accessible research records. Liu–Xin–Ye–Yin, arXiv:2306.03459, supply general Apéry/coin tools and exact formulas for different structured families, but not the five triangular-offset type vector. Stamate–Strazzanti, arXiv:2601.19629, prove general eventual pseudo-Frobenius transport for arbitrary shifts; that result anticipates qualitative eventual periodicity but does not state the ten particular sets or the sharp threshold \(18\). Morales–Dung, arXiv:2601.07467, treat generalized almost arithmetic generating sets, not this five-element non-arithmetic pattern. The major residual risk is that an unindexed specialization of general shift techniques could produce an equivalent exact table; the search cannot establish absolute uniqueness.

## Mathematical value — PASS

The object is the complete finite-prefix triangular-offset analogue of an actively studied shifted-generator semigroup. Its exact pseudo-Frobenius spectrum is stronger than a Frobenius or genus formula; the least-period-ten type table has unequal entries between five and ten, while the two fixed low residues persist across the family. The exact threshold \(18\) and a counterexample at \(17\) make this a complete and sharp infinite-family classification, rather than an arbitrary finite numerical observation. General eventual transfer is acknowledged as prior art rather than claimed anew.

## Limits and closest literature

The result says nothing about arbitrary triangular offsets, arbitrary shifted families, or unpublished classifications. The 2023 motivating paper's latest available PDF is a 2025 revision, but the source's first public release is 2023-06-06. The strongest comparison is the general 2026 Stamate–Strazzanti theorem: it gives PF transport but does not explicitly compute this family's earliest universal threshold or its ten boundary sets. Literature not indexed or not inspected could contain an equivalent specialization. The proof of the new exact statement is self-contained except for standard definitions.

Self-review: passed. Independent audit: not yet performed.
