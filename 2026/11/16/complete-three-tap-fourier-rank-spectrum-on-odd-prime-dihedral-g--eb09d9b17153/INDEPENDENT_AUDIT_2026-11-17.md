# Independent mathematical audit

## correctness

PASS

For each odd prime p and each exact 3-element support in D_{2p}, the regular-representation Fourier fibers are 2x2 with opposite frequencies (not conjugates for complex taps). For a pure coset, prime-DFT Chebotarev full-spark minors bound a nonzero 3-term polynomial to at most two distinct roots; 0,1,2 roots are constructed with nonzero coefficients, yielding nullities 0,2,4. For a mixed coset, translation and automorphism reduce to taps e,r,s; its determinant a^2+b^2-c^2+ab(z+z^{-1}) has either j=0 singular (nullity1) or one j,+/- pair singular (nullity2), but not both, since ab,c nonzero. Explicit weights realize nullity0,1,2. Thus the claimed rank-weighted values 2p,2p-1,2p-2,2p-4 and exclusion of 2p-3 follow. Inspected exact RESULT.md blob f8f6a6ba0be6007898d51ffb7a862aec5bc17613 and full check_dihedral.py; script p=3,5,7,11 SVD corroborates only, not the infinite assertion.

## originality

PASS

Best-of-knowledge original coefficient-sensitive support-stratified spectrum; previous published arbitrary-order dihedral classification assumes all coefficients equal to one and does not imply attainable nullities at arbitrary complex weights. General uncertainty and prime full spark are acknowledged components, not the mixed-coset classification. Residual historical equivalence risk remains.

## value

PASS

An exact attainable and forbidden rank-weighted support law for every fixed three-point support is a natural noncommutative Fourier uncertainty invariant; the mixed-coset gap and every-support attainability are substantive rather than a rename of the Fourier block decomposition.

The dated certificate retains the supplied scientific assessment, sources and limitations.
