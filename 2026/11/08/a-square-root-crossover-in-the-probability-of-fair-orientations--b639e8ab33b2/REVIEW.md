# Scientific review — A square-root crossover in the probability of fair orientations of multistars

## Correctness: PASS
The result is proved by reducing literal all-agent, all-good EFX (including deletion of zero-valued goods) to independent leaf binomial counts. In the dominant-spoke regime, the center must retain more goods on the dominant spoke than the entire subsidiary inventory, forcing the other leaves to meet exact half-quota thresholds. This gives the finite central-binomial slice with an explicit odd-parity correction. Binomial concentration, normal convergence, and a uniform local limit theorem prove the Gaussian transition and sharp subcritical equivalent. The standalone exact checker exercises labeled-good deletions on 85 small multistars and exact dominant-spoke formulas. Computer checks corroborate but do not replace the analytic proof.

## Originality: PASS, qualified
The closest available full text is Afshinmehr et al., *EFX allocations and orientations on bipartite multi-graphs: a complete picture* (2026), DOI:10.1007/s10458-026-09754-8, particularly its EFX definition and existence result for multistars. Its existential/algorithmic results do not give a distribution of the uniform orientation's success probability. Afshinmehr et al., *EFX Allocations Exist on Multi-Graphs*, arXiv:2606.18665v1, gives far more general allocation existence, but the accessible abstract does not establish the random-orientation result; its full text was inaccessible, which remains an originality risk. Neoh and Teh, *Understanding EFX Allocations: Counting and Variants* (AAAI 2025), studies general counting but the available abstract does not cover this exact independent-binomial crossover; its full text was likewise not accessible. The actual published-finding corpus semantic searches and closest IDs appear in AUDIT.json. No equivalent was identified, but this is not a uniqueness certificate.

## Value: PASS
The work answers a natural success-probability question distinct from mere existence, in a star domain already singled out by modern EFX orientation theory. The exact event handles the convention-sensitive zero-valued deletion; the nontrivial square-root transition determines when subsidiary relationships become numerous enough to permit a positive chance of fairness. The sharp subcritical constant provides additional quantitative information. The model is deliberately limited to unit-valued endpoint goods, independent orientations and a fixed number of leaves with divergent subsidiary multiplicities.

## Scientific and verification limits
The asymptotics are analytic; the finite verifier cannot independently certify an infinite limit. Full text for two plausible counting/existence sources could not be inspected. No independent scientific review has been performed.

Self-review: passed. Independent audit: not yet performed.
