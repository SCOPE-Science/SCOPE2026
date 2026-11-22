# Scientific review

## Correctness — PASS
The result is a finite exact classification. Every ternary word of the specified length is generated, every self-overlap is checked, and pair compatibility is precisely the conjunction of non-overlap and Hamming distance at least three. The compatibility cliques therefore coincide with valid codebooks. A bitset Bron–Kerbosch exhaustive maximal-clique search and a separately implemented C++ all-clique enumeration both return maximum sizes \(1,1,2,4,8\), with exact counts \(6,18,108,300,528\), and no nine-word code at length six. Both reproduce the equality tables. The 29- and 49-orbit and five-symbol distance-three claims are checked against full lists rather than sampled. The actual source programs were run and returned their success markers.

## Originality — PASS, qualified
The closest full-text published mathematical results are the Chee et al. 2012 cross-bifix-free construction and Blackburn's 2013 general non-overlap theory. Neither fixes the additional Hamming-distance-three finite optimum. Full published records for unrestricted ternary length-five non-overlap (17 words) and joint non-overlap with minimum Hamming distance two (9 words) were compared by their exact hypotheses and equality statements. Those stronger capacities under weaker constraints do not imply capacities or equality classes after enforcing distance three; they do not address length six. The 2025 Wang–Fang–Feng research on Hamming-constrained partial overlap is directly relevant but was only available as an abstract and expanded preview, leaving a residual historical-coverage risk. Semantic searches of the public finding database and accessible local claims found no equivalent or implying statement, but this does not prove global priority.

## Mathematical value — PASS
Frame synchronization and within-frame substitution correction are independent operational constraints; designing a code satisfying both is a natural finite coding objective. The exact first eight-message threshold distinguishes three-bit feasibility at six symbols from infeasibility at all shorter lengths. The complete codebook classification reveals nonuniqueness (49 six-symbol symmetry classes) and a rigid distance-three equality property at length five. These are reusable design data and a reproducible benchmark for constrained-code methods. The value does not rely on a conjectural extension beyond six symbols.

## Scope and risks
This is a finite computer-assisted theorem. It does not promise noisy-stream synchronization, give a formula for arbitrary length, or establish historical novelty against inaccessible texts. The result is not independently certified.

Self-review: passed. Independent audit: not yet performed.
