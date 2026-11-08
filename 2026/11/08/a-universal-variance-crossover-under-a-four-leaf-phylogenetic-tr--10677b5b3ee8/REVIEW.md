# Scientific assessment: rooted-phylogenetic-diversity variance crossover

## Correctness — PASS

The final claim is an infinite, fully quantified statement on rooted full-binary nonplane trees with unit edges, independent survival probability \(1-q\), and \(0<q<1\). Its central covariance formula follows from nested/disjoint descendant sets and is independently reconstructed in the proof. The local four-leaf expressions, the grafting covariance correction, and strictly increasing crossover polynomial yield the claim for every \(n\ge4\). The empty-tree endpoint is not silently treated as a surviving taxon. The exact standard-library checker passes 61 comparisons, including independent survivor-state enumeration for six orders and tree-shape counting. The infinite result does not depend on the finite tests. No extension to nonunit/ultrametric/correlated models is asserted.

## Originality — PASS within inspected evidence

The exact general covariance formula is *known* from Faller, Pardi and Steel (arXiv:0708.0425, Section 1 and Lemma 1.1). That source was inspected beyond the introduction through the algorithm, unrooted extension and conclusion. It supplies a formula for any given tree, but does not state, prove, or classify these topology-dependent variance crossings, the sharp four-leaf starting order, or the monotone infinite sequence of crossover probabilities. Faith (2008) discusses risk-sensitive use of future phylogenetic diversity, but not this exact tree-variance topology switch. Nipperess and Matsen (2013) address fixed-sample rarefaction rather than independent extinctions. Fischer, Francis and Wicke (2022/2023) address Fair Proportion rankings of species after deletion; their concept is not the variance of total rooted PD. Searches for variance/tree-shape/caterpillar/balanced/field-of-bullets formulations found no directly dominating theorem. Historical priority outside inspected material remains unverified; this is not an independent novelty certificate.

## Value — PASS

The question is whether the topology with greater expected preserved evolutionary history also has greater uncertainty across extinction risks. An explicit sharp four-taxon boundary and a uniform all-size construction answer it negatively. The nontrivial structural feature is cancellation of shared backbone contributions and a strictly monotone crossover polynomial with a nonzero limiting threshold, rather than only a small numerical counterexample. It demonstrates why variance-sensitive biodiversity comparisons cannot be inferred from expected future PD, while remaining explicitly limited to this stylized model.

## Closest literature and limitations

The main technical ancestor is the Faller–Pardi–Steel formula. Faith motivates risk aversion; Nipperess–Matsen uses a different sampling design; Fischer–Francis–Wicke uses a distinct priority index. Existing private prior claims on full-tree mean identification, fixed-budget deletion variance, and bimodality of variance for two-block trees do not imply this exact independent-extinction comparison. The tree pair is not ultrametric, and all edges have unit length; no universality for arbitrary branch lengths or extinction dependencies is claimed. No independent expert audit has been performed.

Self-review: passed. Independent audit: not yet performed.
