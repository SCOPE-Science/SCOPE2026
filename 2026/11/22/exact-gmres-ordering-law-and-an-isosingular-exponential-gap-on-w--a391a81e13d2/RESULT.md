# Exact GMRES ordering law and an isosingular exponential gap on weighted triangular chains

## Finding

Let \(n\ge2\), let \(w_1,\ldots,w_{n-1}>0\), and define the nonsingular lower-bidiagonal matrix \(B(w)\in\mathbb R^{n\times n}\) by \(B(w)_{jj}=1\), \(B(w)_{j+1,j}=-w_j\), with all other entries zero. Solve \(B(w)x=e_1\) by unrestarted, exact-arithmetic Euclidean GMRES with \(x_0=0\). For every \(0\le k<n\), its residual norm \(R_k(w)\) satisfies the identity

\[
R_k(w)^2=\left[\sum_{j=0}^k\prod_{i=1}^j w_i^{-2}\right]^{-1},
\]

where the empty product equals one. At step \(k=n\), the residual is zero. Fix any multiset of \(n-1\) positive weights. Among all arrangements, nondecreasing order minimizes \(R_k\) simultaneously for *every* \(k<n\), and nonincreasing order maximizes it simultaneously. For \(k<n-1\), only the first \(k\) weights affect \(R_k\); strict uniqueness is asserted only for the arrangement of those first \(k\) weights when the weights are pairwise distinct.

In the explicit family \(n=2m+1\), \(m\ge1\), compare \(w^{\uparrow}\), with \(m\) weights \(1/2\) followed by \(m\) weights \(2\), to its reversal \(w^{\downarrow}\). They have *identical eigenvalues and singular values*, and the same initial right-hand side, but at the penultimate GMRES iteration \(k=2m\),

\[
R_{2m}(w^{\uparrow})^2=\frac{3}{5\cdot4^m-2},\qquad
R_{2m}(w^{\downarrow})^2=\frac{3}{8-5\cdot4^{-m}},
\]

so the exactly sharp ordering ratio is

\[
\frac{R_{2m}(w^{\downarrow})}{R_{2m}(w^{\uparrow})}
=\sqrt{\frac{5\cdot4^m-2}{8-5\cdot4^{-m}}}
\sim \sqrt{\frac58}\,2^m.
\]

No sorting procedure is asserted to transform one factor into the other by simultaneous permutation of a fixed system. Rather, this is a comparison within a precisely specified family of factors having an identical multiset of edge weights.

## Assumptions and scope

All results are over \(\mathbb R\) in exact arithmetic. The fixed starting vector is \(e_1\), the first coordinate vector. Every subdiagonal coupling is strictly positive; no bounds relative to one are required. The minimization is standard unrestarted GMRES in the Euclidean norm on \(\mathcal K_k(B,e_1)\), with no preconditioning, restart or numerical rounding. In the ordering comparison, the multiset of couplings is fixed and only their positions along the directed path vary.

## Proof

Set \(N=I-B\); then \(Ne_j=w_je_{j+1}\) for \(j<n\). Since every \(w_j\) is nonzero, the Krylov vectors \(e_1,Be_1,\ldots,B^{k-1}e_1\) span \(e_1,\ldots,e_k\) for each \(1\le k\le n\): the binomial expansion of \((I-N)^j e_1\) has a nonzero coefficient on \(e_{j+1}\), producing a triangular change of basis. Thus, for \(k<n\), the GMRES residual is the orthogonal projection of \(e_1\) onto the orthogonal complement of \(\operatorname{span}\{Be_1,\ldots,Be_k\}\).

Within \(\operatorname{span}\{e_1,\ldots,e_{k+1}\}\), this complement is one-dimensional. Indeed, the equations \(\langle v,Be_j\rangle=v_j-w_jv_{j+1}=0\) for \(1\le j\le k\) yield, on normalizing \(v_1=1\),

\[
v_{j+1}=\prod_{i=1}^j w_i^{-1}\quad (1\le j\le k).
\]

Projecting \(e_1\) onto the line spanned by this vector gives \(R_k^2=|\langle e_1,v\rangle|^2/\|v\|^2=1/\|v\|^2\), which is the stated formula. The remaining coordinates beyond \(k+1\) contribute neither to the residual projection nor the minimum. Since the full Krylov space is all of \(\mathbb R^n\), GMRES reaches zero at iteration \(n\).

Write \(S_k(w)=R_k(w)^{-2}\). For fixed positive weights, the product of the \(j\) smallest weights is the smallest possible product of any \(j\) distinct weights from the multiset, and the product of the \(j\) largest is the largest. Consequently, term by term in \(S_k\), ascending weights maximize each reciprocal prefix product and descending weights minimize each, simultaneously for all \(j\le k\). This proves the global bounds for each horizon. If all weights are distinct, any nonextremal selection or order in the first \(k\) produces a strict inequality in at least one prefix term, giving the stated uniqueness qualification.

For the reciprocal two-block family, direct geometric summation gives

\[
S_{2m}(w^{\uparrow})=\sum_{j=0}^{m}4^j+\sum_{j=0}^{m-1}4^j=\frac{5\cdot4^m-2}{3},
\]

and

\[
S_{2m}(w^{\downarrow})=\sum_{j=0}^{m}4^{-j}+\sum_{j=0}^{m-1}4^{-j}=\frac{8-5\cdot4^{-m}}{3}.
\]

Their ratio follows by taking square roots and the limit \(m\to\infty\). Let \(J\) denote the coordinate-reversal permutation matrix. If \(w^{\mathrm{rev}}\) reverses the sequence of couplings, inspection of the bidiagonal positions yields \(B(w^{\mathrm{rev}})=J B(w)^{\mathsf T}J\). Transposition and orthogonal permutations preserve all singular values. Both matrices are unit triangular, hence have all eigenvalues equal to one. This establishes exact isospectrality and isosingularity for the two arrangements.

## Verification

A self-contained standard-library Python script, `verify.py`, checks the residual formula by independent exact-rational normal-equation minimization, compares the sharp sorted envelopes over finite exhaustive test sets, checks the two-block rational sums and verifies the reversal-transpose identity. Running `python3 verify.py` produces `VERIFY_OK 39018`. This finite computation is supplementary: the proof above covers all positive real weights, dimensions and iteration horizons stated.

## Relationship to prior work

Dargaville and Pain, *A comparison of parallel iterative methods for ILU triangular solves*, arXiv:2611.00552v1 (2026), compare Jacobi/Neumann and GMRES polynomial approximations to unit-diagonal triangular factors and show strong practical dependence on the ordering of ILU factors. Their article does not state the all-horizon weighted-chain extremizer law or the isosingular two-block exponential ratio in its inspected technical analysis. It is a motivation, not a claim that the formula directly analyzes their recycled random-right-hand-side polynomial implementation.

Liesen and Strakoš, *Convergence of GMRES for Tridiagonal Toeplitz Matrices* (2004), and earlier work of Ipsen (2000), already derive residual formulas for constant-coupling Jordan blocks. Those homogeneous formulas, as well as the generic GMRES projection identity, are not claimed as new. Chen and Soodhalter, *Constraints on admissible behavior of GMRES applied to tridiagonal Toeplitz systems*, arXiv:2609.24751 (2026), analyze residual behavior for **constant-coefficient** Toeplitz matrices and discuss Jordan blocks. Their setting includes homogeneous bidiagonal examples but not arbitrary reordered couplings. Greenbaum, Pták and Strakoš, *Any Nonincreasing Convergence Curve is Possible for GMRES* (1996), already show that eigenvalues alone do not determine a GMRES convergence curve. Our stronger restriction is a fixed positive bidiagonal chain, a fixed right-hand side, a fixed multiset of couplings, and—specifically for the reversal pair—exactly identical singular values. The latter is not implied by merely fixing eigenvalues.

## Limitations

The ordering law concerns one prescribed right-hand side and a simple chain, not arbitrary ILU factors or optimal reordering of a fixed sparse system. The two-block gap is measured at the penultimate step; both systems terminate exactly after the next step. It is an exact-arithmetic, not a floating-point, assertion. Related Jordan-block formulas, GMRES Gram-determinant identities and known qualitative convergence-curve examples may have historical precedence; the precise unrestricted-weight sorting/isosingular comparison has not been independently priority-certified. No claims are made about runtime, parallel speedups or all right-hand sides.

## References

1. S. Dargaville and C. C. Pain, *A comparison of parallel iterative methods for ILU triangular solves*, arXiv:2611.00552v1, 2026. https://arxiv.org/abs/2611.00552
2. F. Chen and K. M. Soodhalter, *Constraints on admissible behavior of GMRES applied to tridiagonal Toeplitz systems*, arXiv:2609.24751, 2026. https://arxiv.org/abs/2609.24751
3. A. Greenbaum, V. Pták and Z. Strakoš, *Any Nonincreasing Convergence Curve is Possible for GMRES*, SIAM Journal on Matrix Analysis and Applications 17 (1996), 465–469. https://doi.org/10.1137/S0895479894275030
4. J. Liesen and Z. Strakoš, *Convergence of GMRES for Tridiagonal Toeplitz Matrices*, SIAM Journal on Matrix Analysis and Applications 26 (2004), 233–251. https://doi.org/10.1137/S0895479803424967
5. A. Greenbaum and L. N. Trefethen, *GMRES/CR and Arnoldi/Lanczos as Matrix Approximation Problems*, SIAM Journal on Scientific Computing 15 (1994), 359–368. https://doi.org/10.1137/0915025
