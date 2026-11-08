# Sharp one-fifth trace-error gap between sequential Cholesky pivots and two-point determinant sampling on correlation kernels

## Finding

Let \(A\in\mathbb R^{3\times3}\) be any real symmetric positive-definite correlation matrix (\(A_{ii}=1\)). Compare the rank-two Nyström approximations obtained by (i) two sequential randomly pivoted Cholesky (RPCholesky) selections, each proportional to the current residual diagonal, and (ii) a single size-two determinantal point process (\(2\)-DPP) selection, with probability proportional to the corresponding principal minor. Write their expected residual traces as \(E_{\mathrm R}(A)\) and \(E_{\mathrm D}(A)\). Then

\[
1\ \le\ \frac{E_{\mathrm R}(A)}{E_{\mathrm D}(A)}\ <\ \frac65.
\]

The lower equality holds exactly when the three off-diagonal correlations have equal absolute value. The upper constant is sharp as a supremum over strictly positive-definite correlation matrices. Consequently, even though RPCholesky samples adaptively, determinant sampling *never* has a larger expected trace error in this natural three-point equal-self-similarity class. For two input indices and one selected pivot, the two rules coincide, so three indices are the smallest possible nontrivial comparison.

More explicitly, define \(w_{ij}=1-A_{ij}^2>0\), \(W=w_{12}+w_{13}+w_{23}\), and \(T_i=\sum_{j\ne i}w_{ij}\). The exact formula is

\[
E_{\mathrm R}(A)=\frac{2\det A}{3}\sum_{i=1}^3\frac1{T_i},\qquad
E_{\mathrm D}(A)=\frac{3\det A}{W},\qquad
\frac{E_{\mathrm R}(A)}{E_{\mathrm D}(A)}=\frac{2W}{9}\sum_{i=1}^3\frac1{T_i}.
\]

The optimal constant \(6/5\) is attained only as a singular limit, not by a positive-definite matrix. For example, let \(u_1=(\cos\theta,-\sin\theta)\), \(u_2=(1,0)\), \(u_3=(\cos\theta,\sin\theta)\), and \(G_\theta=(u_i^\top u_j)_{i,j=1}^3\). The matrix

\[
A_\theta=\frac{G_\theta+\theta^4 I_3}{1+\theta^4},\qquad0<\theta<\tfrac14,
\]

is positive definite with unit diagonal, and \(E_{\mathrm R}(A_\theta)/E_{\mathrm D}(A_\theta)\to6/5\) as \(\theta\downarrow0\).

## Assumptions and scope

All computations use exact real arithmetic. The input is a \(3\times3\) *positive-definite* correlation matrix. Every pivot denominator and selected principal minor is therefore strictly positive. Given a selected set \(S\subseteq\{1,2,3\}\), both rules produce the same Nyström approximation \(\widehat A_S=A_{:,S}A_{S,S}^{-1}A_{S,:}\); only their distributions on sets differ. The error is the expected trace \(\mathbb E\,\mathrm{tr}(A-\widehat A_S)\), not the spectral norm, Frobenius norm, runtime, or worst-case sample error. Both rules select precisely two different indices. RPCholesky is *not* assumed to draw the size-two DPP distribution.

## Proof

**1. Exact laws.** For \(i\ne j\), selecting index \(i\) first leaves residual diagonal \(w_{ij}=1-A_{ij}^2\) at the unselected index \(j\), and residual diagonal zero at \(i\). Since all three initial diagonals equal one, the first pivot is uniform and the residual trace after selecting \(i\) is \(T_i\). Hence, for an unordered pair \(\{i,j\}\),

\[
\mathbb P_{\mathrm R}(\{i,j\})=\frac{w_{ij}}3\left(\frac1{T_i}+\frac1{T_j}\right),\qquad
\mathbb P_{\mathrm D}(\{i,j\})=\frac{w_{ij}}W.
\]

The Schur complement identity gives \(\mathrm{tr}(A-\widehat A_{\{i,j\}})=\det A/w_{ij}\), since only the remaining diagonal entry can be nonzero. Multiplying by the probabilities and summing over the three pairs proves all three expectation formulas in the Finding section.

**2. Sharp lower bound.** We have \(\sum_iT_i=2W\). The harmonic–arithmetic mean inequality yields \(\sum_i1/T_i\ge9/(2W)\), proving the ratio is at least one. Equality requires \(T_1=T_2=T_3\), equivalently \(w_{12}=w_{13}=w_{23}\), or equal absolute off-diagonal correlations.

**3. Geometry of the sharp upper bound.** Because \(A\) is a Gram matrix, there are unit vectors \(v_1,v_2,v_3\) with \(v_i^\top v_j=A_{ij}\). Let \(P_i=v_iv_i^\top\). The numbers \(a=\sqrt{w_{12}}\), \(b=\sqrt{w_{13}}\), \(c=\sqrt{w_{23}}\) satisfy

\[
a=\frac{\|P_1-P_2\|_F}{\sqrt2},\quad
b=\frac{\|P_1-P_3\|_F}{\sqrt2},\quad
c=\frac{\|P_2-P_3\|_F}{\sqrt2}.
\]

They are therefore lengths of a (possibly degenerate) triangle, by the ordinary triangle inequality in Frobenius norm. Relabel so that \(a\ge b\ge c>0\). The ratio is the symmetric homogeneous expression

\[
R(a,b,c)=\frac{2(a^2+b^2+c^2)}9
\left(\frac1{a^2+b^2}+\frac1{a^2+c^2}+\frac1{b^2+c^2}\right).
\]

Keep \(b^2\) and \(a^2+c^2\) fixed, increase \(a^2\), and decrease \(c^2\) until \(a=b+c\). This change preserves the ordering and makes \(R\) nondecreasing: if \(H=a^2+b^2+c^2\), the derivative of \(\sum_{r\in\{a,b,c\}}(H-r^2)^{-1}\) with respect to the increasing value \(a^2\) is \((H-a^2)^{-2}-(H-c^2)^{-2}\ge0\). The triangle boundary must be encountered before \(c\) reaches zero because then \(a>b\). Thus it is enough to optimize on degenerate triangles \(a=b+c\).

Scale \(c=1\) and set \(b=t\ge1\), so \(a=t+1\). Direct algebra gives

\[
R(t+1,t,1)=\frac{20(t^2+t+1)^3}{9(t^2+1)(t^2+2t+2)(2t^2+2t+1)},
\]

and the exact nonnegative certificate

\[
\frac65-R(t+1,t,1)
=\frac{2(t-1)^2(t+2)^2(2t+1)^2}{45(t^2+1)(t^2+2t+2)(2t^2+2t+1)}\ge0.
\]

Therefore \(R(a,b,c)\le6/5\) for every admissible matrix. Strict inequality holds for a positive-definite \(A\), because the three distinct rank-one projections \(P_i\) cannot be collinear in Euclidean matrix space: a nontrivial convex combination of two distinct rank-one orthogonal projections is not rank one.

**4. Sharp positive-definite family.** For \(A_\theta\) above, \(w_{12}=w_{23}=\theta^2+O(\theta^4)\) and \(w_{13}=4\theta^2+O(\theta^4)\), so \((a,b,c)\) tends after rescaling to \((1,2,1)\). Substitution into the exact ratio formula gives the limit \(6/5\), proving sharpness over the positive-definite domain.

**5. Boundary of the equal-diagonal hypothesis.** Without normalization, dominance need not hold. For the diagonal positive-definite matrix \(\mathrm{diag}(10,5,1)\), the two-step RPCholesky risk equals \(535/264\), whereas the two-point DPP risk is \(30/13\), strictly larger. Thus the present theorem is a conditional result about correlation kernels and not a statement that the DPP always dominates.

## Verification

Run `python verify.py` with the included `requirements.txt`. The script independently constructs the selection laws, checks the Schur-complement trace-error calculations on rational positive-definite inputs, verifies the exact one-dimensional sharp-bound polynomial identity, and checks a rational Gram-plus-jitter family approaching the extremal ratio. The included output records 682 exact symbolic and rational assertions passing. These finite checks support, but do not replace, the continuous-domain proof in the preceding section.

## Relationship to prior work

Chen, Epperly, Tropp, and Webber introduce and analyze RPCholesky, including the residual-diagonal pivot law, and compare it with DPP column selection [1]. Dereziński and Mahoney survey determinant-based sampling and its Nyström approximation guarantees [2]. Steinerberger analyzes alternative powers of residual-diagonal pivot weights [3], and Epperly establishes improved nonasymptotic RPCholesky trace-error guarantees [4]. These prior frameworks supply the two probability rules and general-purpose bounds; the present finding isolates the exact two-pivot, three-point *equal-diagonal* risk ordering, its equality conditions, and a sharp universal \(6/5\) ratio. This is not a claim that DPP sampling is computationally cheaper or superior on unrestricted kernels. A possible earlier derivation in the column-subset or sequential-volume-sampling literature cannot be excluded.

## Limitations

The theorem is limited to three real indices, a strictly positive-definite unit-diagonal kernel, selection of two indices, and expected *trace* residual. It does not imply any ordering for larger matrices, unequal diagonals, other ranks, samplewise errors, computational effort, or other norms. The upper bound is a supremum approached by ill-conditioned kernels; a fixed positive-definite matrix has a strictly smaller ratio. The exact symbolic verifier is a finite reproducibility aid, not a proof of the universal inequalities or of scientific precedence. Independent assessment has not been performed.

## References

1. Y. Chen, E. N. Epperly, J. A. Tropp, and R. J. Webber, *Randomly pivoted Cholesky: Practical approximation of a kernel matrix with few entry evaluations*, first arXiv posting 2022-07-13, https://arxiv.org/abs/2207.06503 .
2. M. Dereziński and M. W. Mahoney, *Determinantal Point Processes in Randomized Numerical Linear Algebra*, first arXiv posting 2020-05-07, https://arxiv.org/abs/2005.03185 .
3. S. Steinerberger, *Randomly Pivoted Partial Cholesky: Random How?*, first arXiv posting 2024-04-17, https://arxiv.org/abs/2404.11487 .
4. E. N. W. Epperly, *A new analysis of the randomly pivoted Cholesky algorithm*, first arXiv posting 2026-08-21, https://arxiv.org/abs/2608.20633 .
