# Scientific review

## Correctness — PASS
For all positive lengths and every admissible index, the proof reduces a greedy binary subsequence-universal arch decomposition to disjoint adjacent transitions. Rotations then convert path matchings to cycle matchings; the even-transition parity condition is necessary and sufficient, with two labelled binary realizations each. The three-state cyclic transfer counts all proper marked-edge sets uniquely and removes exactly one surplus state assignment in the all-marked even-length case. The characteristic polynomial and coefficient extraction give the stated formula, including lengths one and two, zero index and the maximal index. The bundled verifier reproduces every word for lengths 1–12 and identities to 500. Residual correctness risk is an unrecognized subtlety in the cyclic trace proof; no finite check can exclude that, but the proof explicitly treats it.

## Originality — PASS, with residual bibliographic risk
The 2020 circular universality paper defines the index and develops greedy arches, but its reviewed circular section does not provide the complete fixed-length distribution across all binary lengths. The 2023 ranking/unranking and regular-language papers address linear-word counting and algorithms rather than this evaluated cyclic-index formula. The closest recovered existing minimum-length binary result, \(2^{k+1}-2\) at length \(2k\), is implied by the new distribution and is expressly not itself claimed new. Searches for the cyclic transition matching/Lucas-polynomial census, equivalences and broader covering theorems found no stronger direct result. A different indexing convention or unindexed equivalent could still exist.

## Mathematical value — PASS
The count determines a natural two-parameter language invariant at every length and every admissible circular universality index, rather than a one-off finite cell. The cyclic-parity and all-transition correction reveal a structural difference between linear and circular counting, and the formula directly supports distributional analysis and efficient exact counts. The known minimum-length value is a boundary check, not the sole contribution.

## Closest literature and limits
Barker et al. (2020), arXiv:2003.04629; Adamson (2023), arXiv:2304.04583; Adamson et al. (2023), arXiv:2311.10658. The theorem is binary and counts labelled words rather than necklace classes. The full-word literature cannot be declared completely searched. The same verifier performs finite consistency tests, not independent scientific evaluation.

Self-review: passed. Independent audit: not yet performed.
