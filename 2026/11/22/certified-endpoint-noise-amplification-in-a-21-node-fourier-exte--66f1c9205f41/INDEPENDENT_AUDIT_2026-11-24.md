# Independent mathematical audit

## correctness

PASS

Liu–Zhao–Gong's n=10, m=21, T=6 and uniform samples give L=120 and the stated Gram matrix. The endpoint formula in their Eq. (4), with a zero placeholder at the missing endpoint, gives exactly the coefficient row in the finding. The Euclidean row norm is sqrt(1/|u_p|²−1), attained by an aligned perturbation; even for real data the eigenvector may be chosen real. The rational certificate's rank-one positive shift restricts to the perpendicular complement of the test vector, giving lambda_2(H)>10^−35 in increasing order by min–max and Weyl. The Rayleigh bound places lambda_1(H) below 2·10^−38; the normalized residual and gap then bound the difference of endpoint magnitudes by less than 2·10^−15. Commutation with reflection and simplicity give equal endpoint magnitudes. The strict rational coordinate inequalities imply both claimed gain bounds. For independent centered equal-variance noise, the variance is exactly A²sigma²; the strict lower variance comparison is for sigma²>0, with zero prediction variance at sigma²=0. The Bareiss and endpoint checks were inspected, not independently replayed; the submitted verification reports their successful execution. The line 81 cosine-error comment should not be used: it neglects fixed-point rounding. To recover the actual needed bound, the recurrence uses 49 floors at scale 10^90, with subsequent propagation coefficient at most 1/3 for j≥2, so term errors are at most 1.5 units of scale and contribute less than 74 units in their sum. Angle quantization adds less than two units via the Lipschitz bound for cosine, and the Taylor remainder is below 10^−125. Thus the stated coarser cosine bound 10^−85 is ample: together with the final downward entry rounding it gives entry error less than 2·10^−75 and a row-sum bound less than 10^−70. No change to the scientific bound is needed.

## originality

PASS

The predictor and the choice of Fourier block are existing work, and the row-norm and independent-noise variance identities are elementary. The distinct surviving claim is the certified size of the endpoint gain for the published 21-row block. Prior Fourier-block singular-value estimates do not estimate this coordinate; the closest vector machinery provides a way to compute it but not the bracket or an already certified substitute.

## value

PASS

The published method motivates this precise block before computation. A certified gain above 280000 identifies severe endpoint noise amplification in a method component that smooth-data accuracy and Fourier condition numbers alone do not quantify. It is useful for assessing observation precision requirements without inferring failure of the full quadrature.

The dated certificate retains the supplied scientific assessment, sources and limitations.
