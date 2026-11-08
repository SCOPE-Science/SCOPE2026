# Scientific review

## Correctness — PASS

The cyclic trigram counts partition exactly into statistics of the zero-run and one-run length vectors: singleton-run counts, longer-run counts, and their excess over length two. This statement is verified for all length regimes including the wraparound cases. Choosing the singleton positions and a weak composition of the excess gives \(\binom rs\binom{T+r-s-1}{r-s-1}\), and the only possibilities with at most \(r\) vectors are the U and D classes. The common cyclic shift on the Cartesian product of the two vector sets proves the necessity and sufficiency of the classification. The generating function is then a sum of explicit rational geometric series. Exhaustive cyclic-spectrum grouping through length \(19\) and 120 coefficient comparisons provide an independent computational check, not the proof.

## Originality — PASS (with residual bibliographic risk)

The most relevant work is Ota–Manada (2023/2024): a general automaton-based binary circular reconstruction condition, under an aperiodicity assumption, rather than a closed U/D/X classification and all-length singleton count for fixed trigram read length. Acosta–Tomescu (2022) studies uniqueness of edge-distinguishable Euler tours, whose treatment of parallel edges is strictly different from indistinguishable identical trigrams. Gabrys–Milenkovic (2018) focuses on linear spectra and constructive codebooks, not this unrestricted cyclic singleton enumeration. A search of relevant published mathematical findings and related mathematical claims found adjacent pair-spectrum and all-trigram-spectrum enumerations but no direct singleton-trigram classification. However, the nonexistence of unindexed equivalents cannot be established.

## Mathematical value — PASS

Unique recovery from exact short-fragment frequency data is a basic structural question in sequence assembly. At fixed read length three, the theorem completely identifies which **unrestricted** binary circles are reconstructible and gives the exact number at every length, including periodic circles that some general algorithms exclude. The linear asymptotic singleton count reveals how exceptionally rare rigidity is in this model. The disjoint U/D/X boundary also supplies explicit ambiguity witnesses whenever the criterion fails, rather than just an algorithmic yes/no decision.

## Sources and limits

- Gabrys–Milenkovic (2018), arXiv:1804.04548, sections I–III: coded reconstruction from linear multiset spectra.
- Acosta–Tomescu (2022), arXiv:2208.08522, introduction, uniqueness corollary, graph-edge identity discussion and proof: distinguishable Euler tours.
- Ota–Manada (2023), DOI:10.1587/transfun.2023TAP0015, journal pages 409–416, sections 2–5: circular frequency reconstruction via weighted automata and minimal absent words.
- Primary computation: `verify.py`, standard-library exhaustive spectra through length \(19\) and generating-series coefficients through degree \(120\).

No claim is made about larger alphabets, longer windows, noisy data, or external independent validation. Residual originality uncertainty is restricted to unindexed prior specializations or possible equivalence under a different encoding.

Self-review: passed. Independent audit: not yet performed.
