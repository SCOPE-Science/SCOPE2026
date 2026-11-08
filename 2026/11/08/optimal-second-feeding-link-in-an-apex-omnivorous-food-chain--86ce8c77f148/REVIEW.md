# Self-review

## Correctness — PASS

The stated domain is a forward-only extra link in an unweighted \(n\)-species path with a basal-to-apex edge. The proof partitions **all** admissible absent forward edges into those targeting an internal consumer and those targeting the apex. Direct trophic-level propagation yields the two exact rational \(q^2\) formulas, and completing the square gives the unique optimal skipped span and excludes apex additions. The strict comparison and asymptotic ratio follow without numerical assumptions. Standalone exact-rational checks directly recompute every admissible link for all \(4\le n\le32\). These finite checks supplement the infinite algebraic proof.

## Originality — PASS within investigated sources

The 2014 Johnson et al. paper defines the trophic levels and index and investigates generative food-web models and stability, but does not classify a deterministic single-edge optimization in an already shortcut-containing chain. The full main text of the 2017 Klaise–Johnson paper likewise studies motif signatures and random assembly, not the precise rule or its all-order guarantee. Search comparisons include aliases for omnivory, edge addition, repair, feeding distance and trophic incoherence, alongside semantic research records and related prior scientific claims. A later non-normality article uses another trophic-level convention, and its general objective is not the same as prey-average \(q^2\). Residual risk: unexamined special-purpose results, theses or appendices may contain an equivalent reduction; no failed search alone is a novelty certificate.

## Value — PASS

The motivating question is structural repair of a food chain already perturbed by long-range apex omnivory: can one extra trophic link make the overall hierarchy **more** coherent? The exact answer both establishes strict improvement for all lengths and identifies the globally optimal new feeding distance—roughly two-fifths of the chain—with an asymptotic 20% reduction in squared incoherence. The independence of the position of the new link is also a structural explanation, not just a decimal optimization. These statements are motivated by the original coherence–omnivory relationship, without claiming stability or conservation benefits not proved by the model.

## Closest literature and limitations

- Johnson et al. (2014), doi:10.1073/pnas.1409077111: original index and probabilistic food-web assembly, not deterministic chain repair.
- Klaise and Johnson (2017), doi:10.1038/s41598-017-15496-1: food-web motifs and stochastic prey assignment, not exact optimal one-edge augmentation.
- Drysdale and Johnson (2025), doi:10.3389/fams.2024.1512865: related but distinct trophic-level convention and non-normality framework.

Only one unweighted forward new edge and this one chain family are proved. Independent historical-priority review has not been done.

Self-review: passed. Independent audit: not yet performed.
