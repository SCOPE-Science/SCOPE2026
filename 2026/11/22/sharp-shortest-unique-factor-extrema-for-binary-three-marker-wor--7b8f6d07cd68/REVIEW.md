# Scientific assessment: sharp shortest-unique-factor extrema for binary three-marker words

## Correctness — PASS

The claim quantifies over all linear binary words of weight exactly three at every integer length \(n\ge5\). Its four zero gaps are nonnegative. The proof first establishes the exact equal-interior-gap lemma by exhaustively partitioning factors according to their number of ones, including all boundary cases with zero-length runs. The global upper bound then treats unequal interior gaps, equal interior gaps with an exterior gap larger than the common interior gap, and the remaining equal-interior case. The equality constraints follow from the *strict* inequalities in the first two cases and the exact lemma in the third. The finite checker independently counts literal occurrences for 7,315 complete words at lengths 3–21 and checks predicted equality cases and random instances through length 300. The proof, rather than finite enumeration, establishes all-length quantifiers.

## Originality — PASS against checked evidence

The closest primary 2026 paper, Charalampopoulos et al., *Faster Algorithms for Shortest Unique or Absent Substrings* (arXiv:2605.04826v1), defines the same global invariant but its main result is a packed-word-RAM algorithm. The inspected sections and statements do not provide a sharp maximum restricted to words with exactly three ones or its equality characterization. Mieno et al.'s full open 2021 sliding-window article concerns minimal unique substring updates and point/interval shortest-unique-substring queries. Indexed work on binary two-marker minimal unique factors and on four-run minimal unique factor counts has different objects/invariants; neither supplies the present bound. Exact formula and extremizers were searched using parameter, alias, and implication queries, with no equal or dominating claim found. Search nonappearance is not a proof of novelty, and an unindexed fixed-weight extremum remains a genuine residual risk.

## Value — PASS

Global shortest unique factors measure the length of a local distinguishing signature for an occurrence in a source word. Restricting the source to three marked positions keeps a meaningful sparse code design problem while still permitting nontrivial contiguous collisions. The sharp maximum \(n-2\lfloor n/4\rfloor\) and the *complete extremizer family* explain a rigidity phenomenon: maximum difficulty forces equal interior spacings, with only a bounded number of admissible exterior configurations (eventually four, three, two, or one according to length modulo four). This is an exact natural extremal classification, not a claim of improved global SUS algorithms, and the existing general algorithms do not logically imply it without separate analysis.

## Limitations and priority risks

The theorem does not classify the length distribution of all weight-three words, solve point-constrained queries, or extend to other weights. General tools can evaluate the invariant but give no closed equality criterion. Independent mathematical audit remains unperformed; the computational checks are finite. Older or unindexed papers may contain equivalent special-case extrema, and the 2020 point/interval SUS paper was compared mainly through its abstract and bibliographic record rather than its complete text; this was not treated as decisive proof of noncoverage.

Self-review: passed. Independent audit: not yet performed.
