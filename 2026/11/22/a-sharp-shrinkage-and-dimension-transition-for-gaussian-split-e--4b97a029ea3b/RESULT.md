# A sharp shrinkage and dimension transition for Gaussian split e-values

## Finding

Fix integers \(m,k,d\ge1\). Let \(X_1,\ldots,X_m\) (training) and \(Y_1,\ldots,Y_k\) (testing) be independent observations from \(N_d(0,I_d)\), and put \(\bar X=m^{-1}\sum_iX_i\). For a deterministic shrinkage \(0\le\lambda\le1\), the split Gaussian likelihood-ratio e-value is
\[
E_{\lambda}=\exp\left\{\lambda\bar X\cdot\sum_{j=1}^{k}Y_j-\frac{k\lambda^2}{2}\|\bar X\|^2\right\}.
\]
Then \(\mathbb E_0E_{\lambda}=1\), and for every real \(q>1\),
\[
\mathbb E_0E_{\lambda}^{q}=
\begin{cases}
\left(1-\frac{k}{m}q(q-1)\lambda^2\right)^{-d/2},&\frac{k}{m}q(q-1)\lambda^2<1,\\
+\infty,&\frac{k}{m}q(q-1)\lambda^2\ge1.
\end{cases}\tag{1}
\]

In the balanced two-way split \(m=k\), let \(E_1\) be this e-value with the first half as training and the second as testing, and let \(E_2\) interchange the halves, using the same \(\lambda\). Denote their average \(F_{\lambda,d}=(E_1+E_2)/2\). For \(0<\lambda<1/\sqrt2\),
\[
\begin{aligned}
\mathbb E_0(E_1E_2)&=(1-\lambda^2)^{-d},\\
\operatorname{Var}_0(F_{\lambda,d})
&=\frac12\left[(1-2\lambda^2)^{-d/2}+(1-\lambda^2)^{-d}\right]-1,\\
\mathbb E_0(E_1-E_2)^2
&=2\left[(1-2\lambda^2)^{-d/2}-(1-\lambda^2)^{-d}\right].
\end{aligned}\tag{2}
\]
For \(1/\sqrt2\le\lambda\le1\), \(\mathbb E_0F_{\lambda,d}^2=+\infty\). In particular, nonnegative averaging of the two split statistics does not repair their infinite second moments without shrinkage.

For any fixed \(c>0\), take \(\lambda_d=c/\sqrt d\), with \(d\) large enough that \(\lambda_d\le1\). As \(d\to\infty\), with the balanced half-size arbitrary, one has the joint limit
\[
(E_1,E_2,F_{\lambda_d,d})\ \Rightarrow\ (Z,Z,Z),
\quad Z=\exp\{cG-c^2/2\},\quad G\sim N(0,1).
\tag{3}
\]
Moreover, the sharp mean-square distinction between the two directions is
\[
\boxed{\lim_{d\to\infty}d\,\mathbb E_0(E_1-E_2)^2=e^{c^2}c^4.}\tag{4}
\]
In this only nontrivial fixed-\(c\) finite-variance scale, their correlation tends to one, and the variance reduction due to averaging is asymptotically only \(e^{c^2}c^4/(4d)\).

Finally, under a common alternative \(N_d(\mu,I_d)\) and still with independent training and testing halves of sizes \(m,k\),
\[
\mathbb E_\mu\log E_\lambda=k\left[\lambda\|\mu\|^2-\frac{\lambda^2}{2}\left(\|\mu\|^2+\frac dm\right)\right].\tag{5}
\]
For \(r=m\|\mu\|^2/d\), its unrestricted maximizer on \([0,1]\) is \(\lambda_*(r)=r/(1+r)\). In the balanced case \(m=k\), this growth-optimal deterministic shrinkage has finite null variance precisely when \(r<1+\sqrt2\); at and above that boundary the growth-optimal point is not variance-safe. A maximizer of expected log evidence subject to strict finite-variance admissibility exists for \(r<1+\sqrt2\), while for \(r\ge1+\sqrt2\) the supremum on the safe class is approached as \(\lambda\uparrow1/\sqrt2\) but is not attained.

## Assumptions and scope

The Gaussian variance is known and is the identity; the tested mean is exactly zero. The two sample halves are independent and all coordinates are independent standard normal under the null. The tuning \(\lambda\) is **deterministic and prespecified**, not chosen using the testing sample. The growth-optimal \(\lambda_*(r)\) is an oracle comparison depending on the unknown alternative, not a proposed data-adaptive valid tuning rule. The balanced model comprises two disjoint equally sized halves; the result does not cover overlapping random splits, unknown covariance, non-Gaussian observations, or composite-null likelihood denominators.

## Proof

**Moment boundary.** Conditional on \(\bar X\) under the null, \(\sum_jY_j\sim N_d(0,kI_d)\). Its exponential moment gives
\[
\mathbb E_0(E_\lambda^q\mid\bar X)
=\exp\{q(q-1)k\lambda^2\|\bar X\|^2/2\}.
\]
Since \(\sqrt m\,\bar X\sim N_d(0,I_d)\), the chi-square moment-generating function is \((1-2t)^{-d/2}\) for \(t<1/2\), and infinite for \(t\ge1/2\) by direct Gaussian integration. This proves (1), including the strict equality boundary. For \(q=1\), conditioning gives \(\mathbb E_0E_\lambda=1\).

**Two-way dependence.** Write \(U=\sqrt m\,\bar X\), \(V=\sqrt m\,\bar Y\) with independent \(N_d(0,I_d)\) vectors and balanced halves. Then
\[
E_1=\exp\{\lambda U\cdot V-\lambda^2\|U\|^2/2\},\qquad
E_2=\exp\{\lambda U\cdot V-\lambda^2\|V\|^2/2\}.
\]
The joint Gaussian precision matrix for one coordinate pair in \(\mathbb E_0(E_1E_2)\) is
\[
B_\lambda=\begin{pmatrix}1+\lambda^2&-2\lambda\\-2\lambda&1+\lambda^2\end{pmatrix}.
\]
Its eigenvalues are \((1-\lambda)^2\) and \((1+\lambda)^2\), and its determinant is \((1-\lambda^2)^2\). Hence \(\mathbb E_0(E_1E_2)=(1-\lambda^2)^{-d}\) when \(0\le\lambda<1\); the integral diverges at \(\lambda=1\). By (1), \(\mathbb E_0E_j^2=(1-2\lambda^2)^{-d/2}\) when \(\lambda<1/\sqrt2\) and is infinite otherwise. Expanding the square of the sum and difference proves (2). Since both terms are nonnegative and \(F_{\lambda,d}\ge E_1/2\), variance is infinite whenever \(E_1\) has infinite second moment. This proves the sharp common threshold without relying on a cancellation of infinities.

**Dimension transition and sharp rate.** Under \(\lambda=c/\sqrt d\), the multivariate central limit theorem for the independent products \(U_jV_j\), together with the strong law for \(d^{-1}\|U\|^2\) and \(d^{-1}\|V\|^2\), shows jointly that
\[
\log E_1,\log E_2\ \Rightarrow\ cG-c^2/2
\]
with the **same** \(G\). The continuous mapping theorem proves (3). Set \(z=c^2/d\). The exact mean-square difference is \(2[(1-2z)^{-d/2}-(1-z)^{-d}]\). Taylor expansion gives
\[
\begin{aligned}
-\frac d2\log(1-2z)&=c^2+\frac{c^4}{d}+O_c(d^{-2}),\\
-d\log(1-z)&=c^2+\frac{c^4}{2d}+O_c(d^{-2}).
\end{aligned}
\]
Thus the mean-square difference is \(e^{c^2}c^4/d+O_c(d^{-2})\), proving (4). Both second moments converge to \(e^{c^2}\), while both means are one, so the two e-values become perfectly correlated for \(c>0\). The difference between one-direction variance and average variance equals one quarter of the above mean-square difference, giving the stated exact rate of variance gain.

**Growth frontier.** Under \(N_d(\mu,I_d)\), independence gives \(\mathbb E(\bar X\cdot\sum_jY_j)=k\|\mu\|^2\), while \(\mathbb E\|\bar X\|^2=\|\mu\|^2+d/m\). Equation (5) follows directly. It is a strictly concave quadratic (since \(d\ge1\)), whose stationary point is \(\|\mu\|^2/(\|\mu\|^2+d/m)=r/(1+r)\), lying in \([0,1)\). In the balanced case, (1) at \(q=2\) demands \(\lambda<1/\sqrt2\). Solving \(r/(1+r)<1/\sqrt2\) gives exactly \(r<1+\sqrt2\). Strict concavity and the open admissible boundary complete the maximizer-versus-supremum distinction.

## Verification

Run \(\texttt{python checker.py}\) with Python and NumPy. It checks the one-dimensional Gaussian integrals independently by tensor Gauss-Hermite quadrature; the mixed two-direction integral; the sharp high-dimensional mean-square constant; the oracle-growth threshold; and alternative mean log growth by an independently seeded Gaussian simulation. The checker reports 89 passed assertions. The analytical proof above covers all integer dimensions, all positive sample sizes, and all allowed tuning parameters; the numerical calculations do not substitute for it.

## Relationship to prior work

Wasserman, Ramdas and Balakrishnan introduce universal split likelihood ratios and their e-value validity. Dunn, Ramdas, Balakrishnan and Wasserman analyze split and repeated-split Gaussian universal likelihood tests, including high-dimensional testing. Tse and Davison derive the infinite-variance phenomenon for *unshrunk* balanced cross-fitting and exact variance of unshrunk \(K\)-fold averaging. These facts are prerequisites and **are not claimed as new**. The contribution here is the deterministic training-mean shrinkage boundary, its exact two-direction covariance and safe-averaging formula, the sharp dimension-dependent collapse of averaging, and the oracle log-growth obstruction at \(1+\sqrt2\). The result does not imply a more powerful test than existing alternatives.

## Limitations

The formula is exact only for a known identity Gaussian covariance, a point null and deterministic scalar shrinkage. No adaptive tuning guarantee, improved test power, nontrivial high-dimensional alternatives, or coverage optimization is claimed. The threshold is one way to stabilize moments; it is not a universal optimal regularization rule. Earlier equivalent computations via general Gaussian quadratic-form moment formulas may exist; the cited work establishes the shared fundamentals, and a separate independent priority review is needed for publication.

## References

1. L. Wasserman, A. Ramdas, S. Balakrishnan, *Universal Inference*, arXiv:1912.11436 (first posted 2019-12-24); https://arxiv.org/abs/1912.11436.
2. R. Dunn, A. Ramdas, S. Balakrishnan, L. Wasserman, *Gaussian universal likelihood ratio testing*, arXiv:2104.14676 (first posted 2021-04-29); https://arxiv.org/abs/2104.14676.
3. T. Tse, A. C. Davison, *A note on universal inference*, *Stat* 11 (2022), e501; https://doi.org/10.1002/sta4.501.
4. L. Wasserman, A. Ramdas, S. Balakrishnan, *A Discussion of “A Note on Universal Inference”*, *Stat* 12 (2023), e573; https://doi.org/10.1002/sta4.573.
5. Y. Hao, P. Grünwald, T. Lardy, L. Long, R. Adams, *E-values for k-Sample Tests with Exponential Families*, *Sankhya A* 86 (2024), 596–636; https://doi.org/10.1007/s13171-024-00339-9.
