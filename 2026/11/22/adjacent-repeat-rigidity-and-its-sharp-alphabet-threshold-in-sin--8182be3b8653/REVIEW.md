# Scientific review: adjacent-repeat rigidity and alphabet threshold

## Correctness (C): PASS

The definition counts distinct length-three subsequence *parents* of a length-four received word. The universal adjacent-repeat construction is verified against all fifteen equality patterns of four-position words, so the two-list bound is independent of alphabet size. Its cardinality is \(2q^2-q\). The finite optimality/uniqueness certificate checks all \(\binom{8}{7}\), \(\binom{8}{6}\), \(\binom{27}{16}\), and \(\binom{27}{15}\) source-code subsets, without omission, giving feasible counts \(0,1,0,1\). The unique feasible optimum in each small alphabet equals the adjacent-repeat construction. The 29-word four-letter replacement is validated against all 256 received words. The disjoint-block lifting lemma proves the construction for every \(q\ge4\), not merely the tested alphabets through twelve. Source and captured output are included in the package.

The proof is computer-assisted for the exact finite maxima. An integer-programming calculation using a separately generated incidence matrix agreed on both ternary maxima and uniqueness, but correctness does not depend on an optimizer status. Neither exhaustive enumeration nor the blockwise lift establishes an exact optimum for \(q\ge4\).

## Originality (O): PASS, with residual risks

The closest inspected primary full text, Con–Doron–Ribeiro (2026), concerns the asymptotic binary insertion list-decoding capacity rather than exact length-three ternary packing or uniqueness. Hayashi–Yasunaga (2020) develops Johnson/Plotkin-style bounds for general list decoding, not this precise unconditional small-block incidence optimum. Published two-symbol insertion–deletion separation results treat **source length two**, whereas the present theorem treats source length three. The published fractional four-supersequence/three-subsequence **covering** record minimizes a covering objective, not the integral two-list packing objective. These do not imply the exact \(15\)-word unique optimum or the all-alphabet four-letter exchange threshold. The accessible abstract of Kiah–Wei–Zeng (2026) describes broad asymptotic bounds; its complete text could not be inspected.

Equivalent formulations involving fixed-weight hypergraph packings, code-word incidence inequalities, alphabet relabeling, and complement/run-pattern descriptions were searched. Search negatives alone are not novelty certificates. Residual risks are unindexed tables of short-list insertion codes and an implicit specialization in inaccessible broader coding-theory literature.

## Value (V): PASS

The theorem answers a natural structural question about the smallest nontrivial run-based synchronization code: exactly when does the universally valid adjacent-repeat construction stop being best? It proves literal optimizer rigidity at two and three symbols, locates the **sharp threshold** at alphabet size four, and uses a reusable four-symbol exchange to obtain an improvement for every larger alphabet. The improvement grows as \(\lfloor q/4\rfloor\), rather than being an isolated one-codeword numerical anomaly. The answer is not implied by asymptotic insertion list-decoding capacity, and the all-alphabet lift is independent of any numerical optimizer. It does not claim an unknown exact capacity outside the two small alphabets.

## Closest literature and limitations

- R. Con, D. Doron, J. Ribeiro, *The Insertion List-Decoding Capacity and an Improved Bound on the Deletion List-Decoding Capacity*, arXiv:2607.03989v1 (2026): full-text Sections 1–3 and related work inspected; binary asymptotics only.
- T. Hayashi and K. Yasunaga, *On the List Decodability of Insertions and Deletions* (2020): full-text setup and bounding framework inspected; no three-symbol ternary enumeration.
- H. M. Kiah, H. Wei, R. Zeng, *Constant-List Insertion--Deletion Codes* (2026): abstract inspected, full text inaccessible; residual priority risk.
- *A sharp two-symbol list-two insertion–deletion separation* (2026): published summary compared; source length differs.
- *Exact fractional covering of four-symbol supersequences by three-symbol subsequences* (2026): published summary compared; optimization direction differs.

The upper bound is proved only for \(q=2,3\); the result gives a constructive lower bound for \(q\ge4\). Finite exhaustive search is used as a fully inspectable certificate, not as an infinite proof. No independence or external certification is asserted.

Self-review: passed. Independent audit: not yet performed.
