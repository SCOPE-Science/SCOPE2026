# Independent mathematical audit

## correctness

PASS

The one-dimensional exact consistent mass divided by its row-sum lump is the symmetric matrix with diagonal 2/3 and off-diagonal 1/3. Its symmetric and antisymmetric eigenvalues are 1 and 1/3. Tensorization and the strictly positive physical scale give positive definite blends at both endpoints and throughout. The opposite-corner products of normalized tensor eigenvectors are (−1)^k/2^d for antisymmetric degree k. For t=(1−α)/α the resulting sum F(t) has d+1 linear factors in the denominator and cancels its t⁻¹ term; its t⁻² coefficient is −(1−1/3)^d, so the numerator degree is exactly d−1. Also F(t)=−S(log t)/t for S the d-th forward difference with the stated binomial sign of f(x)=1/(1+exp x). Its integral representation by f^(d) over the fixed box of side log 3 is exact. Integration by parts in each x-moment through degree d−2 leaves no boundary terms, since every derivative used there has order at least one and decays exponentially. A polynomial with roots at all sign changes would have nonzero integral against S after matching signs, contradicting those moments if the number of sign changes were at most d−2. The degree bound proves exactness and simplicity. Reflecting x to −x−d log 3 gives parity (−1)^(d+1), yielding the stated α involution and the even-dimensional fixed root. In d=3 the numerator in the given denominator is −8+192t−216t² (the constant and linear coefficients follow at t=0, the leading one from infinity); this independently gives the stated roots and the negative–positive–negative signs. The α=0 entry is trivially zero because the inverse is diagonal, not an extra interior zero. The supplied exact finite checker was read for scope; the review does not infer the all-d theorem from it.

## originality

PASS

The d=3 case follows from Hanukah's exact formula and is not credited as distinct. The targeted comparison supports only the arbitrary-dimensional exact sign-count and pairing theorem as distinct; related local inverse and mode-switching results do not give that theorem. A separately published equivalent logistic finite-difference theorem remains a priority risk.

## value

PASS

This isolates how large the number of sign changes of an inverse coupling can be while positive definiteness persists for a canonical scalar element model. The exact dimension dependence, simplicity, and root pairing are the significant structural data. The familiar d=3 example is illustrative, not an independent contribution or evidence of numerical instability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
