# Fibonacci precision law for random-permutation descent indicators

## Finding

Let \(\pi\) be uniform on \(S_N\), \(N\ge2\), and put
\[
k=N-1,\qquad
D_i=\mathbf 1\{\pi(i)>\pi(i+1)\},\quad 1\le i\le k.
\]
For
\[
C=\operatorname{Cov}(D_1,\ldots,D_k),
\]
one has
\[
C_{ii}=\frac14,\qquad
C_{i,i+1}=C_{i+1,i}=-\frac1{12},\qquad
C_{ij}=0\quad(|i-j|>1).
\tag{1}
\]

Let \(F_0=0\), \(F_1=1\), and \(F_{r+1}=F_r+F_{r-1}\). Then
\[
\boxed{\det C=12^{-k}F_{2k+2}}
\tag{2}
\]
and, for all \(1\le i,j\le k\),
\[
\boxed{
(C^{-1})_{ij}
=
12\,
\frac{F_{2\min(i,j)}F_{2(k-\max(i,j)+1)}}{F_{2(k+1)}}.
}
\tag{3}
\]
In particular, every precision entry is strictly positive.

For \(i<j\), define the full-order linear partial correlation as the correlation of the least-squares residuals obtained after projecting \(D_i\) and \(D_j\) onto all other descent indicators. Then
\[
\boxed{
\rho^{\mathrm{lin}}_{ij\cdot-\{i,j\}}
=
-
\sqrt{
\frac{F_{2i}F_{2(k-j+1)}}{F_{2j}F_{2(k-i+1)}}
}
<0.
}
\tag{4}
\]

Thus a striking reversal occurs: whenever \(|i-j|>1\), the indicators are marginally independent, but their full-order linear partial correlation is strictly negative.

For a fixed separation \(d=j-i\), with both \(i\) and \(k-j+1\) tending to infinity,
\[
\boxed{
\rho^{\mathrm{lin}}_{ij\cdot-\{i,j\}}
\longrightarrow
-\varphi^{-2d},
\qquad
\varphi=\frac{1+\sqrt5}{2}.
}
\tag{5}
\]

## Assumptions and scope

The permutation law is uniform and the variables are ordinary adjacent-descent indicators.

“Linear partial correlation” means correlation after least-squares residualization. The descent vector is not Gaussian, so (4) is not claimed to be a nonlinear conditional correlation and does not imply a conditional-independence statement.

The Fibonacci formulas are exact for every finite \(N\). The golden-ratio formula is a bulk limit with the pair receding from both boundaries.

## Proof

For every \(i\),
\[
\Pr(D_i=1)=\frac12,
\]
hence
\[
\operatorname{Var}(D_i)=\frac14.
\]

For adjacent positions,
\[
\Pr(D_i=D_{i+1}=1)
=
\Pr(\pi(i)>\pi(i+1)>\pi(i+2))
=
\frac16,
\]
so
\[
\operatorname{Cov}(D_i,D_{i+1})
=
\frac16-\frac14
=
-\frac1{12}.
\]
If \(|i-j|>1\), the two comparisons use disjoint position pairs. Relative-rank symmetry makes the four ascent/descent sign combinations equiprobable, so the two indicators are independent. This proves (1).

Set
\[
A_k=12C.
\]
Then
\[
A_k=
\begin{pmatrix}
3&-1&&\\
-1&3&-1&\\
&\ddots&\ddots&\ddots\\
&&-1&3
\end{pmatrix}.
\tag{6}
\]
Let \(d_r=\det A_r\), with \(d_0=1\). Expansion along an end row gives
\[
d_r=3d_{r-1}-d_{r-2},
\qquad
d_0=1,\quad d_1=3.
\tag{7}
\]
The even Fibonacci subsequence satisfies the same recurrence and initial values, so
\[
d_r=F_{2r+2}.
\tag{8}
\]
Equation (2) follows, and positivity of all leading principal minors also proves \(C\succ0\).

For \(i\le j\), the continuant cofactor decomposition of the inverse gives
\[
(A_k^{-1})_{ij}
=
\frac{d_{i-1}d_{k-j}}{d_k}.
\tag{9}
\]
The cofactor sign is canceled by the product of the \(-1\) entries along the connecting tridiagonal chain. Substitution of (8) yields
\[
(A_k^{-1})_{ij}
=
\frac{F_{2i}F_{2(k-j+1)}}{F_{2(k+1)}}.
\]
Symmetry covers \(i>j\), and \(C^{-1}=12A_k^{-1}\), proving (3).

For a random vector with positive-definite covariance, the full-order linear partial correlation is the negative normalized off-diagonal precision entry. Substituting (3) and canceling common factors proves (4).

Finally,
\[
\frac{F_{2i}}{F_{2(i+d)}}\longrightarrow\varphi^{-2d}
\]
and the analogous right-boundary ratio has the same limit. Taking the square root proves (5).

## Verification

The accompanying checker uses exact arithmetic. It exhaustively enumerates all permutations through \(N=8\), reconstructs the full descent-indicator covariance matrix, and verifies (1).

It then checks the Fibonacci determinant recurrence and multiplies the proposed inverse by the tridiagonal matrix in every dimension through \(k=80\). It checks strict positivity of every precision entry and the exact squared identity underlying (4).

These finite checks are supplementary. The all-\(N\) theorem is established analytically above.

## Relationship to prior work

Borodin, Diaconis, and Fulman identify the descent set of a uniform random permutation as a stationary one-dependent determinantal point process. Their Theorem 5.1 gives the process-level one-dependence and determinantal kernel, and the surrounding discussion computes the mean and variance of the total descent count. It does not state the inverse of the finite descent-indicator covariance matrix or the associated all-pairs linear partial correlations.

Pike decomposes generalized descents into Bernoulli comparison indicators and explicitly computes which comparison pairs contribute nonzero covariance. The ordinary-descent case contains exactly the local ingredients behind (1), but the article studies scalar variance and normal-approximation rates rather than the precision matrix of the indicator vector.

Explicit inversion of Jacobi tridiagonal matrices is classical. The contribution here is therefore not a new matrix-inversion method: it is the exact random-permutation specialization, the Fibonacci simplification, and the statistical consequence that one-dependent marginal structure coexists with strictly negative full-order linear partial association at every distance.

Targeted searches for descent-indicator precision matrices, inverse covariance, partial correlations, and Fibonacci formulas did not locate this combined statement.

## Limitations

The result is second-order and linear; it does not classify nonlinear conditional dependence.

Uniformity of the permutation is essential to the simple tridiagonal Toeplitz covariance.

The inversion step is classical matrix theory. Older permutation or graphical-model literature may contain the same specialization under different terminology; this is the principal originality risk.

## References

1. A. Borodin, P. Diaconis, and J. Fulman, “On adding a list of numbers (and other one-dependent determinantal processes),” arXiv:0904.3740, first submitted 2009-04-23; *Bulletin of the American Mathematical Society* 47 (2010), 639–670.
2. J. Pike, “Convergence Rates for Generalized Descents,” *The Electronic Journal of Combinatorics* 18 (2011), #P236, DOI 10.37236/723.
3. R. A. Usmani, “Inversion of Jacobi’s tridiagonal matrix,” *Computers & Mathematics with Applications* 27 (1994), 59–66, DOI 10.1016/0898-1221(94)90066-3.
