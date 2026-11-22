# Review of finite principal-angle tomography

## Correctness: PASS
The canonical two-projection block formula reduces each trace-norm pencil datum to an equal-weight finite sum of square roots. If two spectra agree, their signed cumulative distribution has at most \(k-1\) sign changes because its jumps consist of at most \(k\) positive and \(k\) negative unit atoms. Integration by parts yields orthogonality to a strict Chebyshev system with an explicit positive Wronskian. A sign-matching linear combination yields the contradiction needed for global injectivity, including repeated and endpoint angles. Full-row-rank Chebyshev Jacobians and the implicit function theorem give nonuniqueness with fewer than \(k\) samples. Direct eigenvalue/Wronskian diagnostic: 950 checks passed. The proof does not depend on the test count.

## Originality: PASS, qualified
The motivating Grassmann Schatten-isometry paper treats \(\|P-Q\|_p\), not injectivity from finitely many asymmetric \(\|P-tQ\|_1\) samples. Loring's projection-angle decomposition and classical Chebyshev interpolation are acknowledged as prior tools. General Gaussian quadrature with variable weights is a different inverse problem. No matching fixed-scale, equal-weight, *sharp* projection-pair theorem was found in the documented literature and published-results comparisons. The precise residual risk is that older equal-weight generalized-quadrature or nonlinear Chebyshev moment theory might imply the same injectivity result in greater generality; a failure to locate such a theorem is not proof of novelty.

## Mathematical value: PASS
The datum count is exactly the dimension of the natural unordered angle parameter space and is optimal for *every prescribed choice* of sampling scales, not just generic scales. A complete projection-pair invariant can therefore be recovered from a minimal finite set of Schatten-one observations, whereas arbitrarily many Schatten-two observations collapse to one trace. This is a natural exact classification of identifiability, not merely a numerical calculation.

## Scope and remaining risks
Only complex Hilbert spaces, equal finite ranks and strictly interior positive sampling scales are covered. No noise-stability or robust inversion rate is claimed. The generalized equal-weight Chebyshev quadrature literature remains a bibliographic uncertainty. No independent mathematical validation has occurred.

Self-review: passed. Independent audit: not yet performed.
