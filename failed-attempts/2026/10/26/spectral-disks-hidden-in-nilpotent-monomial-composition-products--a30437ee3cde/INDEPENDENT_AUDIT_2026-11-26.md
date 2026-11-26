# Independent mathematical audit

## correctness

PASS

The frozen Finding for C_m C_n^* is correct. The fixed ratios at m and n give bounded composition operators and positive edge weights w_k=c_k^2/(c_mk c_nk) tending to rho; the fixed ratio at 1/2 bounds c_k above and below by powers of k by iterating k -> floor(k/2), sufficient for the claimed analytic realization. Coprimality gives n^q | j after q forward edges starting at j and m^q | j for q possible backward edges, hence every positive-index reducing path is finite. All eigenvalues on these blocks are zero, for both the operator and its adjoint; the constant block accounts for 1, with one-dimensional eigenspace. Verified the singular sequence on the disjoint paths m^h n^(L-h): the adjoint geometric vector has one constant-weight endpoint error tending to zero even on the circle (rho/sqrt(L+1)), and the weight errors are uniformly o(1). The singular sequence is weakly null, excluding Fredholmness; at zero use infinitely many start vertices. Outside the disk remove the finite union of blocks containing a fixed low-index cutoff, then invert on the tail by a norm bound. If 1 is outside the disk, it remains Fredholm with a finite-dimensional kernel and cokernel on the constant summand. Nonzero points other than 1 inside the disk have zero kernels on both sides, dense range, and nonclosed range because they are not invertible. The essential norm is the limiting norm of the orthogonal tail columns, and testing the weakly null source monomials gives the reverse inequality. The aside at line 32 should not be read as a further theorem: C_n C_m^* is the adjoint and in this case has the same spectral types; the literal reversed product C_n^* C_m is not the adjoint in general. No such reversal assertion is needed for the Finding.

## originality

FAIL

The stronger predated Hardy block classification in Resultary 71d831748432 makes the general weighted classification a routine compact-perturbation consequence. After identifying orthonormal monomial bases, the nonconstant part of the frozen operator differs from rho times the known unweighted partial shift by a compact weighted partial permutation. Its essential disk and exact essential norm follow in the Calkin algebra. The already classified finite path components remain finite nilpotent blocks when weighted; both kernels at nonzero lambda on that part vanish, so Fredholmness outside the disk gives invertibility there and the remaining nonzero points have dense nonclosed range. The constant summand restores 1. Thus this is more than an overlap at beta=0: the short implication covers the asserted general classification. The unresolved Blaschke-product source is not the basis of failure.

## value

FAIL

The finite-nilpotent-block disk is mathematically useful, but that mechanism is already available in the stronger Hardy model. The remaining change is an asymptotically scalar rescaling plus a compact tail error, with no new invariant of nonconstant weight profiles or new block geometry. The phase comparison against the fixed constant eigenvalue is routine once the disk scales by rho. No genuinely distinct valuable remainder was established for repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
