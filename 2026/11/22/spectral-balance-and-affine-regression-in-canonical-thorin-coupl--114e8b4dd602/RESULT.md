# Spectral balance and affine regression in canonical Thorin couplings

## Finding

Let \(X\) belong to the real Thorin class with signed-rate Thorin measure \(U\). The unique hyperbolic Bochner–Bernstein (HBB) coupling \((Z,Y)\), specified by
\[
\mathbb E e^{\mathrm i(u-w)Z-uwY}=\varphi_X(u)\varphi_X(-w),\qquad u,w>0,
\]
is infinitely divisible on \(\mathbb R\times[0,\infty)\). Its entire two-coordinate Lévy measure is the explicit gamma-ray transform
\[
\boxed{\displaystyle
\Pi(B)=\int_{\mathbb R\setminus\{0\}}U(d\lambda)
\int_0^\infty\frac{e^{-r}}r\,
\mathbf 1_B\!\left(\frac r\lambda,\frac r{\lambda^2}\right)dr,\quad
 B\in\mathcal B(\mathbb R^2\setminus\{(0,0)\}).}
\]
In particular, every jump has both coordinates nonzero and positive second coordinate. The law has Gaussian covariance matrix \(\operatorname{diag}(\sigma^2,0)\) in the coordinate order \((Z,Y)\). The Thorin measure is recovered *exactly*, for every Borel \(A\subseteq\mathbb R\setminus\{0\}\), from the joint jump measure by
\[
\boxed{\displaystyle
U(A)=\frac{\Pi\bigl\{(z,y):y>0,\ z\ne0,\ z/y\in A,\ 1\le z^2/y\le2\bigr\}}
{\int_1^2 e^{-r}r^{-1}\,dr}.}
\]
Both sides may be infinite. Hence the jump geometry retains the *sign* of the original Thorin spectrum, even though the second marginal \(Y\) only records the pushforward of \(U\) by \(\lambda\mapsto\lambda^2\).

**Exact affine-regression classification.** Suppose additionally that
\[
\int_{\lambda\ne0}\bigl(|\lambda|^{-1}+\lambda^{-2}\bigr)U(d\lambda)<\infty,
\qquad d=\beta-\int\frac{\lambda}{1+\lambda^2}\,U(d\lambda).
\]
For any real slope \(b\), the conditional mean is affine **if and only if** the signed and unsigned spectral masses satisfy an exact measure identity:
\[
\boxed{\displaystyle
\mathbb E[Z\mid Y]=d+b(Y-\sigma^2)\ \text{almost surely}
\quad\Longleftrightarrow\quad
r\bigl(U_+(dr)-U_-(dr)\bigr)
=b\bigl(U_+(dr)+U_-(dr)\bigr),\quad r>0.}
\]
Here \(U_+(A)=U(A)\) and \(U_-(A)=U(-A)\) for Borel \(A\subset(0,\infty)\). For \(U\ne0\), a slope satisfying this condition is unique. In particular, **constant regression occurs exactly for sign-symmetric spectra**, \(U_+=U_-\); a nonzero spectrum confined to one sign has affine regression **exactly when it is supported at one rate magnitude**. Conversely, all admissible affine-regression spectra are given by
\[
U_+(dr)=\frac{1+b/r}{2}H(dr),\qquad
U_-(dr)=\frac{1-b/r}{2}H(dr),
\quad |b|\le r\ \text{for }H\text{-almost every }r,
\]
where \(H\) is any positive measure satisfying the same integrability requirements. For example, taking \(H\) to be uniform measure on \([1,2]\) and \(b=1/2\) produces a genuinely two-sided, non-atomic and asymmetric spectrum with nonzero affine regression; generic one-sided multi-rate spectra instead give nonlinear regression.

The components \(Z\) and \(Y\) are independent **if and only if \(U=0\)**, equivalently, if and only if \(X\) is Gaussian, possibly degenerate. If \(U\) is supported on positive rates, \((Z,Y)\) is associated; if it is supported on negative rates, \((-Z,Y)\) is associated. No finite-moment hypothesis is needed for the jump geometry, independence, or association statements; the affine-regression characterization uses the stated absolute first-moment integrability.

For additional geometric specificity, when \(U(d\lambda)=v(\lambda)d\lambda\), the joint jump measure has density
\[
\Pi(dz,dy)=\mathbf 1_{\{z\ne0,y>0\}}\,y^{-2}e^{-z^2/y}v(z/y)\,dz\,dy.
\]
For any \(x,y>0\), the simultaneous upward-jump tail is
\[
\Pi\bigl((x,\infty)\times(y,\infty)\bigr)
=\int_{\lambda>0}E_1\bigl(\max\{\lambda x,\lambda^2y\}\bigr)U(d\lambda),
\quad E_1(a)=\int_a^\infty e^{-r}r^{-1}dr.
\]
The corresponding negative-first-coordinate tail replaces \(\lambda>0\) by \(\lambda<0\) and \(\lambda x\) by \(|\lambda|x\).

## Assumptions and scope

The characteristic function of \(X\) is, with the principal logarithm,
\[
\varphi_X(t)=\exp\left\{\mathrm i\beta t-\frac{\sigma^2t^2}{2}+
\int_{\lambda\ne0}\left[-\log(1-\mathrm it/\lambda)-\frac{\mathrm it\lambda}{1+\lambda^2}\right]U(d\lambda)\right\}.
\]
Here \(\beta\in\mathbb R\), \(\sigma^2\ge0\), and \(U\) is a positive Borel measure on \(\mathbb R\setminus\{0\}\) satisfying
\[
\int(1+\lambda^2)^{-1}U(d\lambda)<\infty,
\qquad\int_{0<|\lambda|\le1}|\log(\lambda^2)|\,U(d\lambda)<\infty.
\]
The coupling is the unique probability measure on \(\mathbb R\times[0,\infty)\) with the Fourier–Laplace identity above, as provided by Kloster's HBB characterization. Neither absolute continuity nor finite Thorin mass, variance, or any other moment is assumed. The jump measure \(\Pi\) is a measure on \(\mathbb R^2\setminus\{0\}\); it is not itself a probability law. Association means nonnegative covariance of every pair of bounded coordinatewise nondecreasing measurable functions evaluated on the vector. The affine-regression condition is a signed-measure equality, not merely an equality of finitely many moments.

## Proof

**1. The gamma atom.** For \(\lambda\ne0\), \(a>0\), and \(G\sim\operatorname{Gamma}(a,1)\), the vector \((G/\lambda,G/\lambda^2)\) has joint Fourier–Laplace transform
\[
\mathbb E e^{\mathrm itG/\lambda-qG/\lambda^2}
=(1-\mathrm it/\lambda+q/\lambda^2)^{-a}.
\]
The elementary Frullani identity
\[
-\log(1+h)=\int_0^\infty(e^{-hr}-1)e^{-r}r^{-1}dr,
\quad \Re h>-1,
\]
shows that the atom contributes jumps \((r/\lambda,r/\lambda^2)\) with intensity \(a e^{-r}dr/r\). Moreover, if \(t=u-w\) and \(q=uw\), then
\[
(1-\mathrm iu/\lambda)(1+\mathrm iw/\lambda)
=1-\mathrm it/\lambda+q/\lambda^2.
\]
Thus this bivariate gamma vector is exactly the canonical coupling for a signed-rate gamma law. Independent convolution of gamma atoms adds these jump measures. The normal component contributes \((N,\sigma^2)\), where \(N\sim N(0,\sigma^2)\), and the drift contributes only a deterministic first-coordinate translation.

**2. Integrability for arbitrary \(U\).** Write \(v(\lambda,r)=(r/\lambda,r/\lambda^2)\). Its proposed jump kernel is a genuine Lévy measure because
\[
\int_{\lambda\ne0}\int_0^\infty (1\wedge\|v(\lambda,r)\|^2)e^{-r}r^{-1}dr\,U(d\lambda)<\infty.
\]
For \(|\lambda|\ge1\), the inner integral is at most \(2\lambda^{-2}\int_0^\infty re^{-r}dr=2\lambda^{-2}\). For \(0<|\lambda|<1\), split \(r\) at \(r=\lambda^2\) and \(r=1\) to bound it by \(1+2|\log|\lambda||+\int_1^\infty e^{-r}r^{-1}dr\). The stated Thorin conditions make both bounds integrable. This also rules out hidden axis jump masses.

**3. Arbitrary Thorin measures and the canonical limit.** Restrict \(U\) to \(A_n=\{1/n\le|\lambda|\le n\}\), a finite measure. Let \(N_n\) be a Poisson random measure on \(A_n\times(0,\infty)\) with intensity \(U|_{A_n}(d\lambda)e^{-r}dr/r\). Its absolutely convergent gamma-point sums yield
\[
Z_n=\beta-\int_{A_n}\frac{\lambda}{1+\lambda^2}U(d\lambda)
+N_\sigma+\int\frac r\lambda\,N_n(d\lambda,dr),
\qquad
Y_n=\sigma^2+\int\frac r{\lambda^2}\,N_n(d\lambda,dr),
\]
where \(N_\sigma\sim N(0,\sigma^2)\) is independent of the Poisson measure. Their joint transform is
\[
\mathbb E e^{\mathrm itZ_n-qY_n}
=\exp\left\{\mathrm i\beta t-\frac{\sigma^2t^2}2-\sigma^2q+
\int_{A_n}\left[-\log(1-\mathrm it/\lambda+q/\lambda^2)
-\frac{\mathrm it\lambda}{1+\lambda^2}\right]U(d\lambda)\right\}.
\]
For \(q=uw\), \(t=u-w\), the exponent equals the sum of the two truncated Thorin characteristic exponents at \(u\) and \(-w\). Thorin integrability gives pointwise convergence of their characteristic functions. Each first marginal \(Z_n\) therefore converges weakly to \(X\), and the Laplace transforms \(\mathbb Ee^{-qY_n}=|\varphi_{X_n}(\sqrt q)|^2\) converge to the valid second-marginal transform of the HBB coupling. Marginal tightness and uniqueness of the joint Fourier–Laplace transform show that \((Z_n,Y_n)\) converges weakly to the canonical pair \((Z,Y)\).

Every finite-truncation law is infinitely divisible with jump measure \(\Pi_n\) given by the boxed formula with \(U\) replaced by \(U|_{A_n}\). The class of infinitely divisible laws is closed under weak limits. For a nonnegative continuous test function supported away from the origin, the integral against \(\Pi_n\) increases to its integral against \(\Pi\), finite by Step 2. The Lévy-triplet continuity theorem therefore identifies \(\Pi\) as the jump measure of the limit. The small-jump covariance contributed by omitted rates tends to zero under the same integrable bound in Step 2, so the Gaussian covariance remains \(\operatorname{diag}(\sigma^2,0)\). This establishes the result even with infinite Thorin mass and without finite moments.

**4. Explicit spectral inversion, density, and tails.** On the support of \(\Pi\), the change of variables
\[
(z,y)=\left(r/\lambda,r/\lambda^2\right)
\quad\Longleftrightarrow\quad
(\lambda,r)=\left(z/y,z^2/y\right)
\]
is one-to-one. Selecting \(1\le r\le2\) gives precisely the stated reconstruction identity, including sets of infinite measure. If \(U\) has density \(v\), the absolute Jacobian \(|\partial(r,\lambda)/\partial(z,y)|=z^2/y^3\), multiplied by \(r^{-1}=y/z^2\), produces the density \(y^{-2}e^{-z^2/y}v(z/y)\). Positive simultaneous jump inequalities are equivalent to \(r>\max(\lambda x,\lambda^2y)\), yielding the \(E_1\) formula and its reflected analogue.

**5. Necessity and sufficiency of spectral balance for affine regression.** Under the extra absolute integrability condition, the Poisson sum in Step 3 converges in \(L^1\) after removing the rate truncation, so
\[
Z=d+N_\sigma+\int\frac r\lambda N(d\lambda,dr),\qquad
Y=\sigma^2+\int\frac r{\lambda^2}N(d\lambda,dr).
\]
The Poisson exponential formula, or differentiation of the joint Fourier–Laplace transform, gives, for \(q>0\),
\[
\frac{\mathbb E[Z e^{-qY}]}{\mathbb E[e^{-qY}]}=d+
\int\frac{\lambda}{\lambda^2+q}\,U(d\lambda),\qquad
\frac{\mathbb E[(Y-\sigma^2)e^{-qY}]}{\mathbb E[e^{-qY}]}=
\int\frac{1}{\lambda^2+q}\,U(d\lambda).
\]
The two integrals tend to zero as \(q\to\infty\) by dominated convergence and the displayed absolute integrability assumption. Thus, if the conditional expectation is affine in \(Y\), its intercept in the shifted parametrization must be \(d\). The conditional mean identity with slope \(b\) is therefore equivalent to
\[
\int_{\lambda\ne0}\frac{\lambda-b}{\lambda^2+q}\,U(d\lambda)=0
\qquad\text{for every }q>0.
\]
Push the signed measure \((\lambda-b)U(d\lambda)\) forward under \(\lambda\mapsto\lambda^2\). The resulting signed measure \(M_b\) satisfies \(\int(1+t)^{-1}|M_b|(dt)<\infty\). Its Stieltjes transform vanishes at every positive \(q\) precisely when \(M_b=0\): write \((t+q)^{-1}=\int_0^\infty e^{-s(t+q)}ds\) and apply Laplace-transform uniqueness twice, justified by the weighted integrability. Writing \(M_b=0\) in the positive and negative rate variables is exactly the boxed spectral-balance condition.

Conversely, spectral balance makes the preceding joint-transform identity hold for every \(q>0\). The finite signed measure \(A\mapsto\mathbb E[(Z-d-b(Y-\sigma^2))\mathbf 1_{\{Y\in A\}}]\) then has zero Laplace transform and hence vanishes, establishing the conditional expectation almost surely. If \(U\ne0\), the positive measure \(H=U_++U_-\) makes the slope unique. Since \(|U_+-U_-|\le H\), the equality \(r(U_+-U_-)=bH\) is equivalent to the stated parametrization and its constraint \(|b|\le r\), \(H\)-almost everywhere. If \(b=0\) it forces \(U_+=U_-\); if one sign is absent, it forces all rate magnitudes to equal \(|b|\). This proves all regression assertions.

**6. Independence and association.** If \(U\ne0\), then \(\Pi\) charges some compact subset of \(\{(z,y):z\ne0,y>0\}\). An infinitely divisible vector with independent coordinates has its Lévy measure supported on the coordinate axes (uniqueness of the Lévy–Khintchine triplet). Thus \(Z\) and \(Y\) cannot be independent. If \(U=0\), the pair is \((N(\beta,\sigma^2),\sigma^2)\) and is independent. Finally, for a Thorin measure supported on positive rates every Poisson jump simultaneously increases both coordinates. Independent Poisson increments are associated, and adding independent normal noise in the first coordinate preserves association. Truncating small jumps and passing to the weak limit proves the bounded-monotone association inequality. For negative rates apply the same argument to \((-Z,Y)\).

## Verification

The accompanying `checker.py` is standalone Python with no nonstandard dependencies. Its exact-rational tests verify the inverse gamma-ray map and Jacobian over positive/negative rates, the shell reconstruction, the affine-regression spectral-balance examples, and the mixed-cumulant identities for finite signed gamma sums. Complex-transform tests check the HBB factorization in nontrivial mixed-sign examples. These are finite diagnostic checks, *not* substitutes for Steps 2–6 of the proof. Execute from the package directory using `python checker.py`.

## Relationship to prior work

Kloster's arXiv:2611.01058v1 (2026-10-31), in its Example 3.1, establishes the canonical coupling for a **single gamma law**, and its Proposition 3.1 shows uniqueness and closure under convolution and weak convergence. Its Proposition 3.2 identifies the **second marginal** as a generalized gamma convolution and Proposition 3.3 provides mixed cumulants assuming moments. The present theorem instead identifies the **entire joint jump measure**, gives invertible signed-rate spectral recovery, and establishes a necessary-and-sufficient spectral balance criterion for **affine conditional regression**, including non-atomic asymmetric examples. The independence criterion is moment-free.

The general multivariate Thorin radial Lévy representation was developed by Barndorff-Nielsen, Maejima, and Sato (2006); Torricelli (2025) proves a Thorin–Bondesson representation in several dimensions, and later simulation work by Grabchak and Zhang (2026) gives a general multivariate gamma jump framework. The new theorem does not claim general multivariate gamma Lévy representations; its claimed gap is the exact rate-to-ray identification and especially the affine-regression spectral classification for the *specific canonical HBB coupling*. Standard Lévy–Khintchine uniqueness and independent-Poisson association are used, not claimed as new. Older gamma-regression characterizations (such as Wesołowski’s constant-regression result) concern different observable ratios or independent positive variables; the present criterion is for the canonical HBB pair and applies to arbitrary continuous signed-rate Thorin measures. Neither the inspected Kloster coupling propositions nor the inspected multivariate Thorin representation sections give this conditional-mean classification.

## Limitations

The result gives structural and regression classifications, not an explicit closed-form density for the full joint probability distribution. The affine-regression equivalence needs absolute first-moment integrability of the signed gamma jumps and their squared-rate partners; it is not asserted for all infinite-mean Thorin laws. No statement asserts that the two coordinates are negatively associated for mixed signs, nor that opposite one-sided support is a necessary condition for all association properties. The gamma-ray reconstruction is from the joint **Lévy measure**, not directly from a finite observed sample. The predecessor's single-gamma formula and general multivariate Lévy theory make parts of the argument natural; unlocated equivalent spectral reconstructions are a genuine historical-priority risk. Independent validation has not been performed.

## References

1. T. K. Kloster, *A characterization and closure property of Thorin's class*, arXiv:2611.01058v1, first available 2026-10-31, https://arxiv.org/html/2611.01058v1 (especially Sections 2–3 and Proposition 3.1–3.3).
2. O. E. Barndorff-Nielsen, M. Maejima, K.-I. Sato, *Some classes of multivariate infinitely divisible distributions admitting stochastic integral representations*, Bernoulli 12 (2006), 1–33, https://ksato.jp/pdf/bnms2b.pdf (general multivariate Thorin Lévy framework).
3. M. Grabchak and X. Zhang, *On the simulation of general multivariate gamma distributions using Dickman approximations*, Computational Statistics 41 (2026), article 62, https://link.springer.com/article/10.1007/s00180-026-01725-7 (general multivariate gamma jump measures).
4. L. Torricelli, *Thorin processes and their subordination*, arXiv:2503.09574v2, 2025, https://arxiv.org/pdf/2503.09574 (Theorem 2 on multivariate Thorin–Bondesson representations; not a conditional-regression theorem).
5. K.-I. Sato, *Lévy Processes and Infinitely Divisible Distributions*, Cambridge University Press, 1999 (Lévy–Khintchine triplets, independence, and convergence).
