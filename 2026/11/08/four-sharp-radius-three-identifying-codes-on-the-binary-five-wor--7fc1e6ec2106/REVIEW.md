# Scientific review of the binary five-word radius-three identification classification

## Correctness — PASS

The object and orientation are explicit: the directed binary de Bruijn graph on all length-five words, and closed **incoming** directed balls of radius three. The elementary one-per-prefix argument forces at least one selected vertex in each of sixteen disjoint pairs, so the lower bound of sixteen has no computational premise. Under equality, sixteen listed symmetric-difference constraints force fourteen specified codewords, leaving only the final bits at the prefixes `0001` and `1110`. Each of the four surviving codebooks is independently verified to have thirty-two nonempty, pairwise distinct identifying sets. The exact signature certificate and two independent graph implementations prove the finite upper bound and exhaustiveness.

The symbolic in-ball generator and the separate directed-edge/reverse-BFS generator agree. Replaying `python3 verify.py` gives `VERIFY_OK`; replaying the C++17 verifier gives `CROSSCHECK_OK 4`, and the 128-row exact signature certificate passes its own reconstruction check. No conclusion about infinitely many graph orders is drawn from finite enumeration. A limitation of the result is that only the specified binary graph and radius are treated.

## Originality — PASS, with historical-priority qualification

The most relevant primary paper is Boutin–Horan Goliber–Pelto, *Identifying Codes on Directed De Bruijn Graphs*, originally public on December 18, 2014 (arXiv:1412.5842; full revised text and author-hosted manuscript inspected). Theorem 3.5 gives the existing general lower bound, here sixteen. Their Theorem 3.9 gives a valid critical-length code with twenty-four vertices and expressly says that determining the minimum at the critical length is open. Theorem 3.6 addresses lengths at least twice the radius and thus excludes the pair of parameters in this result. Neither the minimum of sixteen nor the complete four-code classification follows from those statements. Search comparisons also checked equivalent notation such as \(\vec B(2,5)\), binary critical length, radius-three identifying sets, and one-per-prefix selector codes.

The nearest accessible prior local mathematical result concerns radius two on the three-letter-word graph with nonbinary alphabets. Its hypotheses and ball sets differ, and it neither implies nor contains this five-letter-word radius-three case. Related research on undirected de Bruijn graphs uses different neighborhoods and does not supply the asserted directed classification.

Residual risk: a later unindexed census or a different terminology could already contain the same enumeration. Searches and the available primary texts are evidence for originality, not a proof of global historical uniqueness. Independent priority assessment has not been performed.

## Value — PASS

This is the first genuinely higher-radius critical-length binary case in the exact boundary family \(\(n=2t-1\)\), which the foundational paper isolates as unresolved in general. For this natural instance, the known general bounds were sixteen and twenty-four. The result closes that gap, proves the strongest possible lower bound is attained, and classifies **all** optimal solutions rather than only exhibiting one. A short finite forcing certificate explains why the optimum is highly rigid: fourteen decisions are compulsory and only two independent choices remain. This is a natural and reusable case study for identifying-sensor placement and constrained Boolean graph-search problems, not an arbitrary numerical slice.

## Sources and limitations

- D. Boutin, V. Horan Goliber, M. Pelto, *Identifying Codes on Directed De Bruijn Graphs*, https://arxiv.org/abs/1412.5842 ; full text https://arxiv.org/pdf/1412.5842 . The original public record dates to December 18, 2014; Theorems 3.5, 3.6 and 3.9 establish the relevant prior bounds and boundary gap.
- Author-hosted full manuscript, https://people.hamilton.edu/dboutin/publicationpdfs/boutingoliberpelto , particularly Section 3 and the critical-length remark.

Only labeled binary length-five words and radius-three incoming balls are settled. The four optimal codes are counted separately, and the three natural complement classes identify only global alphabet interchange. No independent historical-priority validation has been conducted.

Self-review: passed. Independent audit: not yet performed.
