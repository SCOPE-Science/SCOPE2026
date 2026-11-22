# Scientific review

## Correctness — PASS

For every integer \(2\le q\le7\), the graph on ordered unequal symbol pairs and the ordinary outsider-only locating signature are explicit. An exact bitmask enumeration covers every relevant \((k-1)\)- and \(k\)-element subset; increasing mask order and a checked binomial trial total certify completeness. Every smaller candidate is rejected; the code prints a valid optimum. The same enumeration counts all labeled optima and closes them under the specified adjacency-preserving relabeling and reversal generators. The standalone checker passed `VERIFY_OK`; a separately coded Python neighbor-set implementation passed `ALTERNATE_OK`, and independent integer constraints corroborated the two largest minima.

## Originality — PASS, qualified

Araki's Kautz work studies directed twin domination, not injective outsider signatures. Boutin–Goliber–Pelto study directed de Bruijn identifying codes. Stronger all-vertex identifying-code calculations for the same graph offer upper bounds only and cannot imply a complete census of the weaker outsider-only code family. The most relevant research-index results considered directed Kautz identification or location-domination in other graph families. Searches did not expose exact prior coverage of the stated finite pair \((\lambda_q,F_q)\) plus symmetry classes; this is not a guarantee against earlier unindexed priority. The original article rendering for one plausible historical source was not completely accessible, although relevant definitions and theorems were inspected.

## Mathematical value — PASS

The invariant quantifies the minimum detectors needed to locate an unsensored failure in the natural undirected Kautz network, not an arbitrary imposed alphabet slice. At six symbols, one extra detector becomes necessary compared with the preceding three nontrivial alphabet orders, and at seven that deficit persists. The exact labeled and natural-symmetry census distinguishes genuinely different optimal sensor layouts. This is a finite classification, not a statement about larger alphabets or noisy physical observation.

## Verification and limits

The delivered source `checker.cpp` is a complete exact finite checker requiring C++17. Its second implementation `secondary_check.py` uses Python3 standard-library set operations. All asserted numerical results are finite and reproducible. The checker does not imply any result for \(q\ge8\). Some plausible historical priority may remain unindexed, and independent mathematical audit has not yet taken place.

Self-review: passed. Independent audit: not yet performed.
