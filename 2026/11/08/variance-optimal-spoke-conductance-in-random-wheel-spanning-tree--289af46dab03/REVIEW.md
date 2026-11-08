# Review of the asymptotic wheel variance optimization

## Correctness
PASS. The spanning-tree determinant is the hub-deleted weighted Laplacian determinant. Its cycle eigenvalues yield the exact variance. The Chebyshev/hyperbolic representation yields an exact positive derivative at conductance \(2\). Compact second-derivative convergence and quantitative tail localization force eventual global uniqueness; the mean-value argument yields the sharp \(12\) displacement constant and the peak deficit. An executable, independent finite counting route checks the polynomial identities (188 passed checks). The theorem deliberately makes no all-sizes uniqueness assertion.

## Originality
PASS, with residual priority risk. The full prior source [1] explicitly gives the general hub-degree variance spectral sum in Example 4.1: the moment formula is **covered** and is not presented as new. The inspected general unweighted degree-law theory [2] does not optimize a continuously variable wheel spoke conductance. Searches for wheel conductance optimization, spoke variance, and the exponential correction found no statement implying the sharp displacement/peak claim. A publicly indexed wheel optimization result for a Löwner ellipsoid concerns a different shape functional and an exponentially different correction, not the variance of stochastic spanning-tree spoke counts.

## Value
PASS. In the natural single-parameter weighted wheel model, the variance-maximizing design is not exactly the thermodynamic-optimal value \(2\) at finite size; its bias is positive and exponentially small with a sharp leading coefficient. Simultaneously identifying eventual uniqueness and the exponentially small deficit resolves a qualitative and quantitative tuning question not determined merely by a general variance formula.

## Closest literature and limitations
[1] E. Fita Sanmartín, C. Schnörr and F. A. Hamprecht, arXiv:2409.13472, Example 4.1; covers the underlying spectral variance formula, not the optimizer theorem. [2] A. Rapoport, arXiv:2312.14992, unweighted UST correlation formulas. No explicit finite cutoff for eventual uniqueness is established. Historical priority remains subject to independent expert review.

Self-review: passed. Independent audit: not yet performed.
