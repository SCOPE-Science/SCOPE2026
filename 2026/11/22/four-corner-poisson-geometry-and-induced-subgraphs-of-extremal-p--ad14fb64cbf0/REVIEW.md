# Scientific review: four-corner extremal induced graph

## Correctness
**PASS.** The proof uses the exact conditional hypergeometric degree formula and the all-four-corner factorial moment argument. Hoeffding localization excludes low/high degree extremes away from the corners, while a tight corner count controls every local degree-to-score discrepancy uniformly. Because inversion edges are exactly disagreements between coordinate orders, the marked graph limit follows by continuous mapping. The two induced edge expectations follow from a direct triangle integral. The standard-library verifier exhaustively checks finite identities; it does not establish the limit.

## Originality
**PASS, qualified.** Bhattacharya and Mukherjee (arXiv:1503.03582; revised version at https://sites.stat.columbia.edu/sumitm/perm_deg.pdf) establish the one-sided marginal minimum-degree Rayleigh law, which is not claimed new. The published result at https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-independent-corner-poisson-clouds-and-gaussian-inversion-fluctua--14fa62567e42 proves two anti-diagonal corner Poisson clouds jointly with Gaussian inversion fluctuations but does not state the full four-corner low/high-degree induced graph. The full primary documents and this published comparison were inspected. A general earlier marked corner-process result might supply some steps; no equivalent induced graph law was identified, and publication priority warrants independent scholarly review.

## Value
**PASS.** The result classifies the entire graph among fixed-threshold extreme low/high degree vertices and the joint degree-order statistics, rather than merely recomputing a marginal. Despite equal Poisson vertex-count laws, the two induced extremal graph classes have different limiting expected edge counts, \(t^4/6\) and \(t^4/3\). This is a concrete structural distinction relevant to extreme-degree subgraph statistics.

## Limitations
The theorem assumes a uniform permutation and fixed threshold and finite ranks. No quantitative convergence rate, extension to biased permutations, or independent validation is asserted.

Self-review: passed. Independent audit: not yet performed.
