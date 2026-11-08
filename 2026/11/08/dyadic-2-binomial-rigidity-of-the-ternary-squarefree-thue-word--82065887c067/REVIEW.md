# Scientific assessment

## Correctness — PASS

The binary transition representation is independently cross-checked against the ternary substitution. For each dyadic length \(n=2^j\), \(j\ge2\), a direct block-parity calculation gives \(N_1\) odd in the first and third groups of \(n\) windows, and \(N_1\equiv2\pmod4\) in the middle. The \(M_1\) residue selects offsets uniquely in the outer groups and up to a half-turn in the middle. The outer groups swap \(0\) and \(2\), while an odd zero count prevents a middle half-turn from preserving \(M_0\). These arguments account for all \(3n\) factors and give the claimed lower bound. The matching upper bound is the published ternary Thue factor-complexity formula [3]. A self-contained verifier checks the exact signature, morphism correspondence, modular moment relations and half-turn separation for \(j=2,\ldots,10\); these checks support, but do not replace, the infinite proof.

## Originality — PASS (historical-priority qualified)

The closest source to the actual word, Shallit and Shur [3], proves ordinary rather than 2-binomial factor counts. Rigo and Salimov [1] prove bounded 2-binomial complexity for *binary* Thue-Morse, which does not imply a result for its ternary transition word. Lejeune, Rigo and Rosenfeld [4] obtain an all-length 2-binomial rigidity theorem, but for the different Tribonacci fixed point. Golafshan, Rigo and Whiteland [5] handle uniform generalized Thue-Morse words, not the nonuniform squarefree Thue morphism. Rao, Rigo and Salimov [2] address avoidance of 2-binomial repetitions. Targeted published-result and accessible historical-record searches did not recover a result with the same domain and implication. An unindexed equivalent theorem or a later paper remains a genuine priority risk; database silence is not novelty proof.

## Value — PASS

This exact formula isolates a dyadic subsequence-order rigidity phenomenon in the classical ternary squarefree Thue word. It provides a concrete four-statistic factor fingerprint and a full infinite family of exact 2-binomial complexity values, rather than a finite extension of a table. Its contrast with bounded binary Thue-Morse 2-binomial complexity suggests structural consequences for coded automatic sequences. No assertion about other lengths or downstream theorems is needed for the claimed value.

## Limitations and comparison references

The proof is dyadic only, uses the established \(p_x(n)=p_t(n+1)\) identity, and does not determine full-length 2-binomial complexity outside the stated family. The closest original papers and their applicability are documented in `AUDIT.json` and in the paper's references. Computation cannot certify all cases or historical novelty, and independent scientific assessment is not yet available.

Self-review: passed. Independent audit: not yet performed.
