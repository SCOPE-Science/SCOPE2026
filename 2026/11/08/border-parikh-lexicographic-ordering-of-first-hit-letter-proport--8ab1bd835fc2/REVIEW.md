# Scientific review: Border-Parikh lexicographic ordering

## Correctness (C): PASS
The claim covers every finite alphabet of size at least two, any nonempty single target, and every pair of letters. The decomposition into a unique first occurrence followed by an ending occurrence proves the fully marked first-hit generating function, including overlapping borders. Differentiation produces the exact signed integral for the **expected random ratio**, rather than a ratio of expectations. Bounded stopped fractions justify integration. If the largest nonzero border difference is positive, the shorter-border terms are bounded below by an explicit geometric-series inequality strictly positive for \(0<z<1\), \(s\ge2\); the negative case follows by swapping labels. The checker independently tests the algebra and a prefix-automaton stopping distribution. No finite enumeration is used as an infinite proof.

## Originality (O): PASS against inspected evidence
Bóna–Maga–Richey, arXiv:2606.06655, treats binary patterns and states an associated stopping-fraction problem. A historical binary border-imbalance result is already known and is **not** asserted as new here. The present multi-letter conclusion is an all-pairs ordering and tie classification on \(s\ge3\), with arbitrary target length, not a restatement of the two-letter case. The inspected Myers and Ostaszewska–Zajkowski texts provide weighted-string and waiting-time techniques without a pairwise stopped-proportion sign theorem. Actual external and research-index searches did not return a matching lexicographic result. The Guibas–Odlyzko classical source was only accessible as an abstract; implicit older coverage remains a genuine risk, and lack of a search hit is not a proof of uniqueness.

## Value (V): PASS
An expected empirical letter proportion at a random first-hit time is generally not a ratio of expectations. A finite word over an alphabet with at least three letters naturally generates a vector of such stopped proportions; determining its entire strict/weak ordering and exact tie conditions without computing the expectations is a substantive, interpretable statistic of pattern detection. In particular, balanced global composition can coexist with strictly biased stopped proportions, with the decisive bias determined by the next longest imbalanced border. The all-alphabet pairwise classification provides a natural reference for multi-symbol sequence monitoring; it is not a parameter-relabeling of a binary output.

## Literature and scientific limits
Closest directly relevant published text: Bóna–Maga–Richey, arXiv:2606.06655 (binary); Myers, arXiv:0906.3763 (weighted avoidance); Ostaszewska–Zajkowski, arXiv:1302.4859 (waiting times). Older general overlap literature and independent review may establish an equivalent result not located in this search. No assertion extends to biased sources or simultaneous stopping targets.

Self-review: passed. Independent audit: not yet performed.
