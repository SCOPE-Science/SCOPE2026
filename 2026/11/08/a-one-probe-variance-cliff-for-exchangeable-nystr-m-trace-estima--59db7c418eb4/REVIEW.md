# Scientific assessment

## Correctness — PASS

The complete statement is specialized to \(A=\lambda P\), an exact rank-\(k\) orthogonal projector, independent unnormalized real Gaussian probes, and \(f(0)=0\). The Nyström pseudoinverse reduces to a projected-column-space projector. Conditional single-column residuals are \(\chi^2_1\), and conditioning two columns on the other \(k-2\) proves the joint moment from a two-dimensional Gaussian angle. This yields the exact variance and expected error-proxy ratio; a further full-rank leave-one-out sketch proves exactness for \(k+1\) probes. The two-probe law follows by beta–gamma integration. The independently coded finite checks agree with all formulas, without being used as proof of universal statements.

## Originality — PASS, subject to historical priority

The main 2026 FlexTrace paper supplies the estimator and general statistical bounds but does not report the exact rank-critical pairwise covariance, \(3/(k+3)\) calibration ratio, or one-probe variance cliff. The earlier XNysTrace paper already proves a general error-proxy-to-error identity in terms of an unspecified correlation (Proposition 3.1); this is expressly acknowledged. Its general bound does not itself compute that correlation for the flat-spectrum Gaussian projector model. Searches for exchangeable Nyström trace estimators, leave-one-out Gaussian projection residuals, inverse-Wishart diagonal identities, and the exact numerical ratios did not locate a covering theorem. Unindexed classical projection-statistic equivalences remain a genuine priority risk.

## Value — PASS

The finding puts a sharp boundary on the practical interpretation of internal error bars for an exchangeable randomized matrix-function estimator. In the rank-matched regime its nominal squared-error scale tends to zero although its actual absolute mean squared error stays bounded away from zero; with one additional Gaussian probe both errors vanish. This is a motivated calibration and sampling-budget benchmark rather than a generic low-rank observation. It does not establish broad real-world failure rates or invalidate empirical performance outside the stated model.

## Closest literature and limits

- Madhavan, Alexanderian, and Saibaba, arXiv:2603.05721v1, Sections 3.1–3.2: FlexTrace construction, bias and MSE bounds.
- Epperly, Tropp, and Webber, arXiv:2301.07825v2, Sections 1.2.2, 3.1, 5.3: XNysTrace construction, exact covariance-dependent proxy identity, and general variance bounds.
- Exact finite-rank flat positive spectra, exact arithmetic, real Gaussian probes and the expected squared-error proxy only. The full historical literature on Gaussian projection statistics has not been exhaustively indexed.

Self-review: passed. Independent audit: not yet performed.
