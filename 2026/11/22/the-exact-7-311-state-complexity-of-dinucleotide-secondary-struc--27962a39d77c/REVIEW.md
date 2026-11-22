# Scientific review

## Correctness — PASS

The streaming state invariant records the most recent dinucleotide and the mature set of earlier pairs eligible to be disjoint from the next pair. The transition rejection rule is equivalent by induction to the defining secondary-structure obstruction. The included standalone program exhausts the finite reachable graph (22,985 nonrejecting states plus sink), computes the suffix-refinement sequence \(2,17,2715,6807,7295,7311,7311\), and independently obtains 7,311 equivalence classes with Hopcroft refinement. Its direct comparison against the pair-of-disjoint-factors definition on every DNA word through length nine is supplemental validation. Full reachability and right-congruence stabilization, rather than a bounded sample, prove the all-length state count.

## Originality — PASS (best-knowledge, qualified)

The closest primary studies are Nguyen et al., arXiv:2302.13714 (2023), and Chu, Wang, and Zhang, arXiv:2304.11403 (2023), whose full arXiv presentations were inspected, including their definitions and construction/capacity sections. Zhang and Wu (2023), PMC10749251, was also inspected in its open-access full text and focuses on the different minimum-loop variant. The first develops avoidance codes; the second develops generating sets and spectral-radius capacity bounds. The latter's small transition digraph recognizes a restricted generated family, not the entire avoidance language. Neither inspected source states or logically implies the exact minimal one-way complete DFA size 7,311 without new state-space construction and minimization. Searches on secondary-structure avoidance, automata, Myhill–Nerode state complexity, and complementary dinucleotides did not reveal an exact earlier statement; absence from searches is not a proof of historical priority. A pre-existing unindexed automaton result remains possible.

## Value — PASS

Stem-length-two avoidance is the smallest nontrivial natural constraint in the DNA secondary-structure code literature. The exact number of deterministic online recognition states is a canonical memory-complexity invariant of the **entire** allowed language, not an arbitrarily chosen subset or computational toy. It determines the sharp 13-bit fixed-state memory requirement, makes a minimum one-pass recognizer constructible, and can support exact finite-length automaton-based enumeration independently of asymptotic capacity results. Its strength is an exact natural finite classification, not a new rate improvement.

## Remaining scientific limitations

The claim is confined to linear words, four DNA bases, length-two stems, and complete deterministic one-way automata. No extra loop separation is imposed. The integer certificate is exact but no independent audit has been performed. Equivalent unindexed earlier work could affect priority.

Self-review: passed. Independent audit: not yet performed.
