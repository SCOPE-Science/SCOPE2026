# Scientific review

## Correctness: PASS

The full classification follows by testing the first and last positions of a shortest symbol run, which force one shift into the short forward range and the other into the short backward range. A third position, exactly one short shift before the right endpoint, forces the sum of their lengths not to exceed the minimum run length. Conversely, this inequality ensures that the forward short shift or backward short shift remains in the same run at every position. The binomial count is an exhaustive parameter count of those admissible shifts, not an empirical extrapolation. The proof holds for every alphabet size of at least two and every positive run-length vector. A direct brute-force checker exhaustively compared actual and predicted pair sets for 19,525 parameter profiles.

## Originality: PASS (best-knowledge)

The main prior literature is Meleshko–Ochem–Shallit–Shan, *Pseudoperiodic Words and a Question of Shevelev* (2022 preprint; 2023 journal), especially Definition 1, Propositions 2–4 and Theorem 5, together with its larger-alphabet and complexity sections. These treat the same pseudoperiod definition, but do not give an exact classification or triangular enumeration of nontrivial pairs for run-cycle periodic words. Its decidability and run-bound results do not directly imply the new precise answer. The earlier Desmeules–Blondin Massé–Hallé–Gaboury *Multipseudoperiodic Words* (2013) uses a different permutation-twisted notion. Topically relevant indexed records and the accessible prior claims were compared for exact statement coverage, dual formulations and parameter specializations. None inspected subsumes this theorem. The remaining priority risk is an unindexed or inaccessible equivalent characterization; absence from an index is not a novelty proof.

## Mathematical value: PASS

Ordinary periods make the raw existence of pseudoperiods of a periodic word vacuous, so the first genuinely interesting question is the classification of shift pairs strictly below its period. The theorem answers this *completely* for a natural unbounded family, with no restriction on alphabet size or on individual run lengths beyond positivity. The normalized pair spectrum in forward/backward coordinates depends only on the smallest run, even though the period and every other run may change; absolute long-shift values depend on the period. This is a structural invariance. The exact count and sharp disappearance when one run is a singleton offer useful comparison cases for work on automatic and morphic pseudoperiods. It does not rely on a downstream general theorem or an arbitrary finite slice.

## Literature and limits

- J. Meleshko, P. Ochem, J. Shallit and S. L. Shan, arXiv:2207.10171 (first public July 20, 2022), https://arxiv.org/html/2207.10171v3.
- S. Desmeules, A. Blondin Massé, S. Hallé and S. Gaboury, *Multipseudoperiodic Words* (2013), https://doi.org/10.1142/S0129054113400364.

The theorem does not cover repeated separated occurrences of a run symbol, arbitrary nonperiodic words, or triples of shifts. The earliest public date is the arXiv first version date, not its later journal date. The verification enumeration is finite; it is not the infinite proof.

Self-review: passed. Independent audit: not yet performed.
