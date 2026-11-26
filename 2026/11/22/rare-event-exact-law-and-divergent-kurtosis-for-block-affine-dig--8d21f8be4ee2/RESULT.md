# Exponential logarithmic scale for a block-affine quadrature error

## Finding

Let \(N=2^{em}\), with fixed block width \(e\ge2\) and \(m\to\infty\). Apply one infinite binary block-affine scramble with an independent fair binary shift to all points of the complete grid \(\{a/N:0\le a<N\}\). For the integrand \(f(x)=x\), write \(E_N\) for the quadrature error (sample mean minus \(1/2\)). Then \(\Pr(E_N=0)=0\) and
\[
\frac{-\log_2(2N|E_N|)}{N}\ \Longrightarrow\ \mathrm{Exp}(1).
\]
In particular, the median of the absolute error is \((2N)^{-1}2^{-N(\log 2+o(1))}\), where \(\log\) denotes natural logarithm. Thus the typical absolute error is exponentially small in the number of points, even though its root mean square is exactly \(1/\sqrt{12N^3}\). The same logarithmic law holds for the ordinary binary affine-matrix scramble. It does not hold for fully nested uniform binary scrambling of the grid, for which the standardized error is asymptotically normal at the same root mean square.

## Assumptions and scope

The input binary expansions terminate after \(em\) digits. The scramble is Suzuki's block-affine construction [1, Definition 2.14]: diagonal blocks are independently uniform in \(\mathrm{GL}(e,2)\), blocks below the diagonal are independently uniform binary matrices, and the shift consists of independent fair bits, independent of the matrix. The output has infinitely many randomized digits; the logarithmic statement does not describe a truncation to finitely many digits.

## Proof

Put \(s=em\). The invertible prefix transformation visits each \(s\)-bit prefix once. The prefix average is \((N-1)/(2N)\). For suffix digit \(s+j\), the restriction of its matrix row to the first \(s\) input bits is uniform on \(\mathbb F_2^s\), independently for all \(j\): all of these entries are in unrestricted blocks. Any nonzero row averages to a bit value of \(1/2\) across the input cube; a zero row makes the bit constant at the independent shift bit. Centering the suffix bits cancels the deterministic prefix deficit and gives the supporting representation
\[
2NE_N=\sum_{j\ge1}2^{-j}B_jR_j,
\]
with mutually independent Bernoulli\((1/N)\) activations \(B_j\) and fair signs \(R_j\). The same reasoning is valid at block width one. This is the singleton-frequency specialization of the ordinary affine error expansion in Pan and Owen [2, Theorem 3.1 and Eq. (3.2)], transferred to the block scheme by prefix balance and suffix row independence; it is not claimed as a new error representation.

Let \(J=\inf\{j\ge1:B_j=1\}\). It is almost surely finite, with \(\Pr(J>k)=(1-1/N)^k\), so \(J/N\) converges to a unit-rate exponential. Cancellation to zero would require every bit after \(J\) to be activated with sign opposite to \(R_J\), since the maximum total possible tail magnitude is exactly \(2^{-J}\). This has probability zero. With probability \((1-1/N)^2\), both positions \(J+1,J+2\) are inactive. On this event the tail magnitude is at most \(2^{-J}/4\), so \(2N|E_N|/2^{-J}\) lies in \([3/4,5/4]\). Consequently \(-\log_2(2N|E_N|)/N-J/N\) tends to zero in probability. The strictly increasing continuous limiting CDF implies that any median of this scaled logarithm tends to \(\log 2\), giving the absolute-error median stated above.

For scale comparison, independence in the series gives \(\operatorname{Var}(E_N)=(4N^3)^{-1}\sum_{j\ge1}4^{-j}=1/(12N^3)\). In the fully nested uniform binary scramble, conditioning on the scrambled grid prefixes leaves independent uniform random continuations because the inputs have distinct length-\(s\) prefixes and hence use disjoint subtrees beyond them. The error is \(N^{-2}\sum_{a=0}^{N-1}(U_a-1/2)\) for independent uniform \(U_a\) on \([0,1]\). It has the same exact variance and an ordinary central limit theorem. In particular its scaled logarithm tends to zero in probability: \(2N|E_N^{\rm nested}|=|Z_N|/\sqrt{3N}\), where \(Z_N\) converges to a standard normal, and the probability of \(|Z_N|\) lying below a threshold tending to zero or above one tending to infinity goes to zero.

## Verification and limitations

The accompanying `verify.py` provides finite exact-rational corroboration of the supporting digit law and moment arithmetic; the logarithmic limit follows from the geometric first-activation time and the explicit cancellation bound, not from these finite checks. The result concerns the linear integrand and complete one-dimensional grids, not general smooth integrands, higher dimensions, or finite-precision implementations.

## Relationship to prior work

Suzuki [1, Definition 2.14 and Theorem 2.17] gives the block-affine construction and gain-coefficient variance theory. Pan and Owen [2, Sections 2–3 and Theorem 3.1] give the exact analytic-integrand expansion for ordinary shifted binary linear scrambling; its specialization yields the signed series above. Their single-replication probability bounds and median-of-means results in Section 5 give superpolynomial accuracy, not the two-sided limit for the logarithm at scale \(N\) proved here. In particular, the exact variance, rare-outlier mechanism, series representation, and its direct moment consequences are not claimed as new. Historical priority beyond the compared statements is not certified.

## References

1. K. Suzuki, *Coarse scrambling for Sobol' and Niederreiter sequences*, arXiv:2510.02111v1, https://arxiv.org/abs/2510.02111v1.
2. Z. Pan and A. B. Owen, *Super-polynomial accuracy of one dimensional randomized nets using the median of means*, Mathematics of Computation 92 (2023), 805–837, https://doi.org/10.1090/mcom/3791; arXiv:2111.12676.
