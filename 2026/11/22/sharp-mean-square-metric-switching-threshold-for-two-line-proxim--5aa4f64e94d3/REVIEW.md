# Independent mathematical audit

## correctness

PASS

Taking the Euclidean projections for a scalar metric in the stated update keeps z on V and u on its orthogonal line. In orthonormal line coordinates the map is T(m)=[[p,cs/m],[−mcs,p]] with p=c². For fixed m it is similar to T(1) by diag(1,m), with eigenvalue modulus c. In T(m)^T T(m) the off-diagonal is proportional to 1/m−m, and its diagonal terms differ only by swapping m² and m^-2. Reciprocity and the second-moment assumption cancel the off-diagonal and equalize the diagonal to lambda=p²+p(1−p)v. Independence from the past makes this a conditional norm identity at every step, including k=0 by initialization, hence the exact geometric moment for each starting vector. Since lambda−1=−(1−p)[1−(v−1)p], the strict, neutral and expansive regimes and the uniform reciprocal two-point boundary follow, with random equality at r²=2+sqrt(3) still contractive at every 0<p<1. Orthogonal lines, though excluded in the theorem's proof setup, give T=0 and do not affect the all-noncoincident-lines threshold. For the periodic product the trace is 2p²−p(1−p)q, q=r²+r^-2, and determinant p²<1. Of the two remaining Schur tests only 1+3p²−p(1−p)q>0 restricts q. The ratio (1+3p²)/[p(1−p)] is 6+(3p−1)²/[p(1−p)], so strict all-angle stability needs q<6 (at equality p=1/3 gives eigenvalue −1). At p=9/10,r=2 the random factor is 801/800 and the periodic trace/determinant are 99/80 and 81/100, yielding nonreal roots of modulus 9/10. Neither the periodic nor the random result overstates the pathwise conclusion.

## originality

PASS

Best-of-knowledge pass for the independent reciprocal-metric second-moment law, its sharp stability boundary, and the explicit separation from deterministic alternation. The earlier deterministic threshold is covered and receives no originality credit; generic covariance propagation is also a standard ingredient.

## value

PASS

The case isolates a meaningful risk in dropping a metric safeguard: two individually stable metrics, even contractive in strict alternation, are not interchangeable with independent switching for expected joint squared error. The exact thresholds, equality regime and all-starting-state law make this a usable stability test and give a counterexample without numerical ambiguity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
