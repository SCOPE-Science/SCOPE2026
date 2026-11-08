# Scientific review — Joint leaf–cherry fluctuations in uniform labelled trees

## Correctness: PASS

The random object and the cherry convention are fixed precisely. Cayley's Prüfer bijection gives the leaf moments. A cherry-deletion bijection gives its expectation and conditional leaf mean. Two distinct cherries have six disjoint labels at all orders covered by the complete moment theorem; counting ordered disjoint pairs and diagonal pairs separately yields the exact second moment. The elementary exponential bounds give strictly positive covariance for every size \(n\ge5\). Expansion of exact moments gives a positive-definite limiting covariance matrix. For every nontrivial linear combination of the two local pattern counts, the bounded-rewiring central limit criterion of Isaev–Southwell–Zhukovskii applies, and Cramér–Wold gives the joint limit. The standalone checker exhaustively enumerates Prüfer words for orders five through eight and passes 282379 assertions and diagnostic checks. Finite checks do not replace the uniform proofs.

## Originality: PASS, qualified

Junk–Schmidt–Weber (2019 preprint; 2020 journal) use the same degree-three cherry indicator to study marginal cherry moments and abundance, not the leaf–cherry mixed moment or explicit limiting cross-correlation. Isaev–Southwell–Zhukovskii (2019/2022) provide the general local-pattern Gaussian criterion and enumeration framework; the new claim is not that criterion but the independently derived, exact mixed covariance and its explicit two-dimensional Gaussian covariance matrix. Ekhad–Zeilberger (2022) concern joint degree counts rather than a local pair-of-leaves configuration. Choi–Kaur–Wu (2021) treat different random binary phylogenetic trees and the cherry–pitchfork pair. Actual mathematical database, literature, alias and parameter searches did not produce a dominating same-model formula. An earlier mixed-moment identity obtained by specializing generic forest enumerators remains a historical-priority risk; no search can prove uniqueness.

## Value: PASS

This identifies the explicit fluctuation dependence of a natural global tree-shape statistic (leaves) with a local structure that generates tree automorphisms (degree-three cherries). Their positive limiting correlation, \(\sqrt{2(e-2)/(e^3-3)}\approx0.289967\), is a precise feature not captured by the known asymptotic independence of degree-one and degree-three vertex counts. The theorem is all-order, gives a strict finite-size covariance sign and a nondegenerate joint central limit law, and is not just another finite table or a marginal recomputation. Its significance is confined to the uniform labelled-tree model.

## Closest sources and limitations

Primary full texts inspected include Junk–Schmidt–Weber, *Almost all trees have quantum symmetry* (2019 arXiv preprint; 2020 journal), Sections 3–4; Isaev–Southwell–Zhukovskii, *Distribution of tree parameters by martingale approach* (first public version 2019), Theorem 1.1 and Section 2; and Choi–Kaur–Wu, *On asymptotic joint distributions of cherries and pitchforks for random phylogenetic trees* (2021), model definitions and joint limits. The Ekhad–Zeilberger (2022) preprint abstract was also checked for degree-count coverage. Independent expert audit and historical-priority certification remain unperformed.

Self-review: passed. Independent audit: not yet performed.
