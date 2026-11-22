# Self-review

## Correctness — PASS

The five exact moment formulas are independently reconstructed from the cardinal polynomials, hold symbolically for arbitrary nonnegative integer moment index, and force the required one-sided coefficient signs. The monotonicity of \(W_0\) and \(W_2/\lambda^2\), together with their asymptotic negative endpoint contributions, proves unique positive sign crossings. The precise order and displayed root intervals are certified by rational series enclosures reconstructed by `verify.py`. Reflection handles all negative tilts and equality boundaries. There is no experiment-to-infinity inference.

## Originality — PASS, subject to historical-priority uncertainty

Generic interpolation and weighted Newton–Cotes formulas are known and not claimed. The literature compared includes Sermutlu's unweighted coefficient table, Trefethen's Newton–Cotes exactness analysis, DLMF's general weighted interpolation construction, and a 2005 paper on Chebyshev-weighted Newton–Cotes. Accessible scientific records and relevant pre-existing results did not present the complete two-transition exponential-weight sign classification. The 2005 publisher full text was not accessible; the comparison there rests on the available abstract and introduction, a residual risk requiring independent priority review.

## Value — PASS

The first nonnegative-to-negative transition determines exactly when the classical five-sample formula retains positivity for a positive exponentially varying density; the second transition identifies a distinct failure channel. Exact sign thresholds and the absence of reentrant positivity provide an operational restriction for using interpolatory fixed-node weights on boundary-layer integrals. This is a concrete stability property not available merely from positive unweighted Boole coefficients; the result makes no claim about error-optimality.

## Limits

The scheme, weight, nodes and finite class are fixed. Sign preservation does not guarantee small quadrature error. A generic weighted quadrature formula is not itself a novelty claim; the asserted contribution is the complete sharp sign phase diagram.

Self-review: passed. Independent audit: not yet performed.
