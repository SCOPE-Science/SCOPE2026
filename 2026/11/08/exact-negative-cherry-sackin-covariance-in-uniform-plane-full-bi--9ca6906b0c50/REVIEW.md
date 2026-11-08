# Self-review

## Correctness (PASS)

The claim quantifies over every integer \(n\ge1\) in the uniform plane Catalan ensemble with exactly \(n\) internal vertices. It uses exact definitions of cherries and depths, the identity \(S_n=P_n+2n\), and a checked four-function root-decomposition calculation of \(\mathbb E[H_nP_n]\). The coefficient calculations, two zero boundaries, strict negativity for all larger sizes, and Stirling asymptotic are explicit in `RESULT.md`. Independent integer recurrences plus exhaustive Catalan enumeration passed 82,878 exact assertions after executing `verify_cherry_path.py`. These checks corroborate but do not replace the analytic proof.

## Originality (PASS; priority qualified)

The closest same-model primary source, Bacher–Bodini–Jacquot (arXiv:1401.1140), develops uniform Catalan samplers rather than mixed cherry/path moments. Norton's full public tree-invariant manuscript addresses the cherry and Sackin marginals separately and lists joint distributions as future work. Janson's path-length work and McKenzie–Steel's cherry distributions are important antecedents; their uninspected material could contain implicit specializations. A 2020 full open article on Sackin variation concerns other phylogenetic-tree statistics and distributions. Available mathematical claims and the inspected primary sources do not establish the exact all-size mixed formula. Different model laws and marginal statistics do not imply this claim. The evidence supports best-knowledge originality, not a proof of publication priority.

## Value (PASS)

Local cherry abundance measures small symmetric branches while the Sackin sum measures whole-tree shape depth. Their joint covariance is natural and nontrivial under a uniform Catalan law: it is exactly negative beyond the first two sizes and scales as \(-\sqrt{\pi}n^{3/2}/8\), giving a quantitative benchmark for joint tree balance diagnostics. The sign theorem and growth rate are structural, not an arbitrary small-sample census.

## Closest literature and limits

Sources and material read are recorded in `AUDIT.json`, including Bacher et al. (2014), Janson (2005 manuscript, incomplete PDF inspection), McKenzie–Steel (2000, abstract only), Coronado et al. (2020), and Norton (2025). The result does not cover nonplane or leaf-labeled laws, nor the full joint distribution. Independent bibliographic and mathematical review has not been done.

Self-review: passed. Independent audit: not yet performed.
