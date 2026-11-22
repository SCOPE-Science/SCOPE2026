# Scientific review

## Correctness (C): PASS
The finite group law follows directly from the ordered-pair concatenation identity. Its generators have order \(m\), while commutators produce every independent pair coordinate; hence all \(m^{q(q+1)/2}\) proposed states are reachable. The accepting condition is exactly zero forward-pair counts plus zero products of each pair of letter counts. The proof checks the **left** stabilizer of the accepting set, as demanded by right continuation languages: multiplication by the last letter and then by the first letter forces every stabilizing coordinate to vanish. The Markov-chain period is exactly \(m\), proving the density limits. The submitted checkers reproduce reachable and minimal state counts on seven parameter choices and directly enumerate short words; no finite sample is treated as an infinite proof.

## Originality (O): PASS against inspected sources
The closest structural predecessor is Lejeune–Rigo–Rosenfeld, *On the binomial equivalence classes of finite words* (arxiv:2001.11732), which identifies the 2-binomial quotient with a free class-two nilpotent group. That prior fact gives group coordinates but does not calculate the syntactic quotient of the specific modular Boolean language or its residue-periodic acceptance density. Fazekas–Huang–Mercaş, *Subsequence Analysis Problems for Binary Parikh Matrices* (arxiv:2610.06717), treats exact binary Parikh fibers, universality and containment, rather than modular all-directed-pair tests. Relevant published single-pattern modular state-complexity findings were compared and concern non-equivalent patterns and predicates. Targeted database, alias and general-literature searches found no stronger instance; an unindexed equivalent or unexamined broader algebraic result is a remaining priority risk.

## Value (V): PASS
This is a sharp all-parameter state-complexity theorem for a natural second-order information signature. It identifies the full syntactic group and a nontrivial arithmetic oscillation in long-word acceptance frequencies, with a complete prime-modulus formula and an exact finite arithmetic description for composite moduli. Such results measure the memory required to monitor multiple directional pair correlations simultaneously, rather than merely one designated counter.

## Limits and literature
The theorem excludes same-letter scattered pairs and does not compare with NFA or nonuniform-source complexity. The two inspected primary references are arxiv:2610.06717 (first public 2026-10-05) and arxiv:2001.11732 (first public 2020-01-31). Earlier work supplies essential group and 2-deck foundations; it is not claimed as novel.

Self-review: passed. Independent audit: not yet performed.
