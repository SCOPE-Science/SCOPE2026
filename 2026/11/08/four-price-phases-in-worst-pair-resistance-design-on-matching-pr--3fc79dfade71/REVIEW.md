# Review of the four-phase resistance-diameter theorem

## Correctness

**PASS.** The global symmetry reduction follows from the variational representation of pairwise effective resistance as a supremum of affine functions of edge conductances. The quotient reduction is exact for a connected \(K_{m,m}\) with a priced matching. Three explicitly reconstructed resistance values arise from the Laplacian's three nonzero eigenspaces; the nonmatched cross-part resistance is strictly below the same-part resistance. The remaining two functions cross once. Both first derivatives are explicit, and their signs prove four price phases, with exact common boundary values and no additional invariant minimizer. Unrestricted optimality follows from convex orbit averaging, not from treating symmetry as an assumption. Exact grounded-Laplacian checks and independent scalar optimization tests passed. Finite computations are corroborative and do not certify arbitrary parameter ranges.

## Originality

**PASS on inspected evidence; priority remains qualified.** Ghosh, Boyd and Saberi (MTNS 2006, §VII; SIAM Review 2008, §8) explicitly formulate general minimax effective-resistance design as a convex program, but do not give the exact price thresholds on matched balanced bicliques. Earlier matching-priced *complete-graph* resistance-diameter classifications concern a different edge set and cannot be specialized by merely choosing their two prices. An earlier matching-priced \(K_{m,m}\) spectral-gap classification optimizes \(\lambda_2\), not the maximum pairwise resistance; the two matching-edge screening thresholds differ here by the proved amount \(1/(2m-3)\). Available literature and indexed mathematical result searches did not identify an equivalent all-parameter worst-pair theorem. This is not proof of exhaustive novelty; an unindexed specialist treatment could predate the result.

## Mathematical value

**PASS.** Worst-pair electrical resistance measures a robust network-design cost distinct from total resistance and spectral-gap optimization. The theorem is a natural complete classification of one matching-discount/surcharge problem on an infinite network family. Its four genuine regimes distinguish which vertex pairs constrain the optimum, when a conducting matching is economically excluded, and a nontrivial \(m^{-2}\)-wide intermediate transition. The difference from spectral-gap screening is exact, not a numerical trend.

## Limits and closest literature

The theorem classifies the invariant optimal allocation and the unrestricted optimum *value*, not every asymmetric global optimum. The focal conference version is dated July 24–28, 2006; the exact first appearance of a possible earlier working paper has not been established. Relevant prior full texts are Ghosh, Boyd and Saberi, MTNS 2006 and SIAM Review 2008; unweighted complete multipartite resistance expressions do not address priced optimization.

Self-review: passed. Independent audit: not yet performed.
