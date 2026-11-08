# Scientific review — distance-first two-offer target hitting

## Correctness

**PASS.** The claim has a precise proposal-with-replacement model, a mean-first-hitting objective and explicitly unrestricted tie handling. Equation (1) follows from forced-path properness and exact Bellman optimization. The decorated-cycle rational solution satisfies the complete Bellman system, and the signs of the comparison polynomials establish the reversal for **every** integer pendant load at least two, not merely finitely many tests. The lower-order statement is a complete labeled-graph census: every edge mask at orders two through six is visited, disconnected graphs are excluded, and relabeling fixes the target without loss. The checker replays exact policy evaluation, Bellman residuals, and all pairwise offered-neighbor distance comparisons, yielding 27,475 rooted connected masks. There are no numerical tolerances in the certificate. The exhaustive lower-bound argument does depend on inspecting the standalone enumerator and trusting its exact execution, and no independent formal verification is claimed.

## Originality

**PASS, with priority limitations.** The main source, Georgakopoulos–Haslegrave–Sauerwald–Sylvester (arXiv:1911.05170, Sections 2 and 7), already establishes the general optimal-hitting-value ordering. The 1996 biased-walk paper by Azar et al. already explicitly says that going closer need not be the best bias action. Neither proposition is claimed as novel. The present result instead fixes the distinct two-offer random-neighbor mechanism and obtains the **minimum graph order seven** by an exhaustive finite classification, as well as a natural exact unicyclic pendant-load family with the threshold two and a nonzero rational gap for all loads beyond it. The inspected primary material does not state or directly imply that exact cutoff. Targeted searches and accessible prior-claim comparisons found no matching enumerative theorem. Broader literature could conceivably contain an unnoticed exact small-graph example; a search cannot establish absolute priority.

## Value

**PASS.** A common graph-distance routing heuristic is perfectly reliable for optimal two-choice mean target-hitting on all graphs through six vertices, yet fails as soon as two pendant leaves perturb a five-cycle. The exact seven-vertex cutoff and all-load preference sign give a mathematically interpretable obstruction, not just an arbitrarily chosen small numerical anomaly. The effect is small at the first instance (\(4/415\)), but the strict qualitative failure is sharp and the signed gap grows along a structural infinite family. This is useful for understanding when distance-based local choice is an optimal or unsafe surrogate for global hitting-value routing.

## Closest literature and limitations

1. Georgakopoulos et al., *The Power of Two Choices for Random Walks*, arXiv:1911.05170, original 2019-11-12. Section 7 proves value-ranking optimality and polynomial-time strategy calculation, not a seven-vertex graph-order cutoff.
2. Azar et al., *Biased Random Walks*, Combinatorica 16 (1996), DOI:10.1007/BF01300124. It supplies the qualitative warning about moving closer under a **different** biased-walk mechanism, not the exact two-neighbor model or the pendant-load classification.

The result does not establish finite-deadline stochastic optimality, a unique seven-vertex obstruction, or weighted/directed extensions. The computer-assisted part is limited to the completely enumerated finite graph-order range; the infinite-family assertion has its own exact algebraic proof.

Self-review: passed. Independent audit: not yet performed.
