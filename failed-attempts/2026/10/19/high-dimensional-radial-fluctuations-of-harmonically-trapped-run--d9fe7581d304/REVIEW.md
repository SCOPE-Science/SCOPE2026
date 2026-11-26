# Independent mathematical audit

## correctness

PASS

At a stationary observation time the backward Poisson inter-event gaps, including the age, are independent exponentials; weighting them by the exponential trap kernel gives the stated Beta(1,alpha) breaks and independent directions. Under the nested Gaussian coupling each fixed pair of directions becomes orthogonal almost surely, and the sum of discarded weights bounds the positional truncation error uniformly in dimension. For fixed masses, all distinct pairwise dot products are uncorrelated (condition on all directions except one occurring in just one of the two pairs) and each has variance 1/d. This gives Var(Q_d|P)=2(H^2-K)/d. The Beta recursion gives E H=1/(alpha+1), E K=6/D, and E H^2=(alpha+6)/D, with D=(alpha+1)(alpha+2)(alpha+3), yielding both finite-dimensional moment formulas. For a finite set of pairs, the coordinate products satisfy the multivariate CLT with identity covariance; the Gaussian direction normalizers tend to 1 after division by sqrt(d). After multiplying by sqrt(d), omitted pairs have conditional squared error at most 4H times the sum of omitted squared weights, uniformly in d, so finite truncation passes to the full conditional limit. H>0 permits the stated delta method. A first break near 1 forces the mixing variance near 0, whereas first two breaks in (1/3,1/2) give a positive lower bound; both events have positive probability. The normal mixture is consequently non-Gaussian.

## originality

FAIL

A distinct indexed theorem in the same physical model gives exactly the conditional radial law, exact finite-dimensional conditional and averaged errors, and a stronger joint coordinate/radius limit. The non-Gaussian mixture assertion for the radial component, radial delta method, and unconditional moments are immediate consequences. The additional almost-sure coupling uses the known finite Pearson-walk orthogonality limit and the elementary summable-mass tail, so it does not leave a distinct substantive finding. This is material coverage, not a chronological priority claim: the closest matching indexed record is dated later in its path, and the inspected original RTP paper does not state the conditional CLT.

## value

PASS

The statement addresses a natural physical limit: it separates persistent renewal-history randomness from shrinking angular noise and identifies the angular correction as a mixture. This is informative for high-dimensional approximations and is not simply a low-dimensional moment recomputation, although the indexed coverage prevents crediting a distinct contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
