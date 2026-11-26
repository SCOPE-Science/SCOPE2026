# Independent mathematical audit

## correctness

PASS

Conditioning the first edge gives B_(k+1)=E[Q B_k Q] on the mean-zero space. Shore permutations force B_k to be scalar on each of the three sectors; projected edge-vector squared lengths are w_i and E[zz^T] has eigenvalues d_i there. Expansion of Q=I−zz^T/2 gives row i of M. Projection contraction gives B_(k+1) <= B_k and hence nonincreasing forcing s_k/4 <= 1/2. The common-uniform last-reset coupling orders the responses in reverse order of d. Strictness holds on the event of no reset at the smaller d in any step and a final reset only at the larger d; this event has positive probability and compares the unchanged 1 with at most 1/2. Thus k>0 gives precisely the stated worst sectors, including their direct sum at equal shores, while k=0 is tied on all sectors. All M entries are positive, and row sums are at most ν with the third strictly smaller; positivity makes all entries of M²1 strictly below ν² and implies the higher-power bound and Perron rate <ν. The Perron eigenvector puts the root above max_i(1−d_i); the secular sum then decreases from infinity to 1/2 at 1. In proportional growth, the upper 2x2 limiting block of q(I−M) has the stated smaller eigenvalue and the third eigenvalue is 1+1/r. M is diagonally similar to a real symmetric diagonal-plus-rank-one matrix (rank-one entries sqrt(d_i w_i d_j w_j)/4), so the Perron mode tracks the smallest of the scaled losses. The smaller branch satisfies (3−2rR)(3−2R)=1, with negative derivative and endpoints 1 and 4/3. For fixed p, at ε=1/q=0 the two modes off the simple unit mode have eigenvalues 1−1/p and 1−3/(4p). Pairing the middle-row derivative with the left and right unit modes e_B and (1/3,1,1/3) gives −2/3, proving the separate fixed-p limit. An independent exact rational check for (p,q)=(2,3) compared the full 5x5 projection recursion to the three-mode reconstruction entrywise at horizons 0–4; e.g. at k=2 the three coefficients were (53/96,97/144,113/288).

## originality

PASS

The general lifted second-moment method and the one-step bound are not new. The supported specific result combines the sharp all-horizon shore extremizers for two nontrivial shores with the continuous aspect-ratio gain and a separate fixed-p asymptotic. The strongest distinct Resultary comparator already has the analogous star extremizer and 4/3 limit but its one-dimensional shore eliminates a sector and does not imply this theorem.

## value

PASS

This is a natural graph family for comparing one-step spectral contraction with worst-case expected squared error. The exact optimizer across all positive horizons and the strict comparison show when a standard power estimate overstates disagreement. The limiting ratio quantifies the effect of imbalance (up to a factor 4/3 in logarithmic mean-square decay rate) rather than merely giving a tractable recurrence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
