# Convergent all-order graphon response for analytic expanding circle maps

## Finding

Consider a family of self-consistent Perron–Frobenius operators for integer-expanding circles with an arbitrary bounded graphon and real trigonometric-polynomial interactions. Near zero coupling, the normalized fixed density is a **genuine holomorphic Banach-valued function of coupling**. Its full Taylor series converges in a common analytic Fourier norm, for every bounded graphon including discontinuous block graphons. Each coefficient equals the formally defined susceptibility of Maquera (2026), so the rooted-tree decomposition there is an actual convergent response series in this analytic subclass, rather than only a formal identity. Quantitative geometric remainder estimates hold uniformly across all graphon fibres.

Precisely, for every integer \(d\geq2\), every measurable symmetric graphon \(W:[0,1]^2\to[0,1]\), and every real trigonometric polynomial \(h:\mathbb T^2\to\mathbb R\), there are \(\sigma>0\), \(\epsilon>0\), and \(\eta>0\) and a unique solution \(\varphi^*(\alpha)\) in the \(\eta\)-ball about the constant density \(1\) in the normalized analytic space below whenever \(|\alpha|<\epsilon\). The map \(\alpha\mapsto\varphi^*(\alpha)\) is holomorphic for complex \(\alpha\) there, and real positive for real \(\alpha\). If
\[
\varphi^*(\alpha)=1+\sum_{m\ge1}\alpha^m\varphi_m,
\]
then for every finite \(m\), \(\varphi_m\) is Maquera's formal susceptibility of order \(m\), and hence has its rooted-graphon-tree expansion. For \(0<r<\epsilon\), \(M_r=\max_{|\alpha|=r}\|\varphi^*(\alpha)-1\|_X\), and \(|\alpha|<r\),
\[
\left\|\varphi^*(\alpha)-1-\sum_{m=1}^{n}\alpha^m\varphi_m\right\|_X
\leq \frac{M_r(|\alpha|/r)^{n+1}}{1-|\alpha|/r},\qquad n\ge0.
\]
The constants can depend on \(d,h,W\); no optimal coupling radius is claimed.

## Assumptions and scope

Write \(\mathbb T=\mathbb R/\mathbb Z\). Let \(W\) be an essentially bounded, measurable, symmetric, real graphon (the conventional range \([0,1]\) suffices) and let \(h\) be any fixed real trigonometric polynomial in two periodic variables. Define the analytic Wiener algebra
\[
 A_\sigma=\left\{u(x)=\sum_{k\in\mathbb Z}\widehat u(k)e^{2\pi i kx}:\ \|u\|_\sigma=\sum_k|\widehat u(k)|e^{2\pi\sigma|k|}<\infty\right\},
\]
with \(X=L^\infty([0,1];A_\sigma)\) as a Bochner-measurable Banach space, and \(X_0=\{u\in X:\int_\mathbb T u_z=0\text{ for a.e. }z\}\). The normalized affine space is \(1+X_0\). For \(\varphi\in X\), set
\[
 Q_{\varphi,z}(x)=\int_0^1W(z,z')\int_\mathbb T h(x,y)\varphi_{z'}(y)\,dy\,dz',\qquad
 F_{\alpha,\varphi,z}(x)=dx+\alpha Q_{\varphi,z}(x)\pmod1.
\]
The operator \(\mathcal F_\alpha\varphi\) has fibre \((F_{\alpha,\varphi,z})_*\varphi_z\), defined by pushforward against test functions, and by analytic inverse branches for complex parameters near zero. We solve \(\varphi=\mathcal F_\alpha\varphi\) within an explicitly local neighborhood in \(X\), not over arbitrary invariant measures. Graphon dependence in \(z\) is merely measurable; smoothness in the fibre variable \(x\) is analytic.

## Proof

**1. A resolvent with a uniform analytic-fibre bound.** At \(\alpha=0\), the fibre transfer map is the doubling-style map of degree \(d\), whose Perron operator is
\[
 (P_du)(x)=\frac1d\sum_{j=0}^{d-1}u((x+j)/d),\qquad \widehat{P_du}(k)=\widehat u(dk).
\]
For any \(u\in A_\sigma\) of zero average, \(\widehat u(0)=0\), whence for every integer \(n\ge1\),
\[
 \|P_d^nu\|_\sigma\le e^{-2\pi\sigma(d^n-1)}\|u\|_\sigma.
\]
Indeed, the weight ratio between the input frequency \(d^nk\) and output frequency \(k\), for nonzero \(k\), is at most the displayed exponential. Consequently
\[
 (I-P_d)^{-1}\big|_{X_0}=\sum_{n=0}^\infty P_d^n,
 \qquad \left\|(I-P_d)^{-1}\right\|_{X_0}\le 1+\sum_{n\ge1}e^{-2\pi\sigma(d^n-1)}<\infty.
\]
This estimate is pointwise uniform in the graphon coordinate and requires no regularity in \(z\).

**2. Analyticity of the nonlinear transfer operator in a fixed Banach space.** Fix any sufficiently small \(\sigma>0\), then choose a strict intermediate strip \(\sigma<\tau<d\sigma\), for example \(\tau=(d+1)\sigma/2\). The map \(\varphi\mapsto Q_{\varphi,z}\) is bounded and complex linear from \(X\) to a finite-dimensional space of trigonometric polynomials in \(x\), uniformly in almost all \(z\): each Fourier coefficient is an integral of a bounded kernel against a bounded linear functional of \(\varphi\). The polynomial \(Q\) and every \(x\)-derivative are therefore uniformly bounded on any fixed complex strip, for \(\varphi\) in a bounded \(X\)-ball.

For sufficiently small complex \(\alpha\), uniformly throughout that ball and almost all \(z\), the equations
\[
 d b_j(x)+\alpha Q_{\varphi,z}(b_j(x))=x+j,\qquad j=0,\ldots,d-1,
\]
have inverse branches holomorphic on the closed strip \(|\operatorname{Im}x|\le\tau\), taking values in the interior of \(|\operatorname{Im}b_j|<\sigma\), with \(|d+\alpha Q'_{\varphi,z}(b_j)|\) bounded below by a positive constant. This follows from the uniform contraction principle applied near \((x+j)/d\): the strict margin \(\tau/d<\sigma\) absorbs the perturbation. Contraction and implicit differentiation also show joint Banach holomorphy in \((\alpha,\varphi)\).

Thus the inverse-branch formula
\[
 (\mathcal F_\alpha\varphi)_z(x)=\sum_{j=0}^{d-1}
 \frac{\varphi_z(b_j(x))}{d+\alpha Q'_{\varphi,z}(b_j(x))}
\]
defines a bounded holomorphic function on the \(\tau\)-strip, uniformly in the graphon variable. A function bounded by \(B\) on a strip \(|\operatorname{Im}x|<\tau\) has Fourier coefficients bounded by \(B e^{-2\pi\tau|k|}\), so its \(A_\sigma\)-norm is at most \(B\sum_k e^{-2\pi(\tau-\sigma)|k|}\). Consequently \((\alpha,\varphi)\mapsto\mathcal F_\alpha\varphi\) is a jointly Fréchet-holomorphic map into the **same** Banach space \(X\), with no loss of analytic width. Its fibre integrals equal the fibre integrals of \(\varphi\), initially by real change of variables and then by the identity theorem for the complex parameter and complex densities. Hence \(\mathcal F_\alpha\) preserves \(1+X_0\).

**3. Implicit-function argument.** Put \(G(\alpha,u)=1+u-\mathcal F_\alpha(1+u)\), a holomorphic function with values in \(X_0\). We have \(G(0,0)=0\), and because the dependence of the maps on \(u\) is multiplied by \(\alpha\),
\[
 D_uG(0,0)=I-P_d\big|_{X_0}.
\]
Step 1 makes this derivative an isomorphism. The complex Banach-space analytic implicit-function theorem supplies \(\epsilon,\eta>0\) and a unique local holomorphic solution \(u(\alpha)\in X_0\) for \(|\alpha|<\epsilon\). Shrinking \(\epsilon\) if necessary makes \(\|u(\alpha)\|_X<1/2\). Since the defining equations respect complex conjugation for real \(\alpha\), local uniqueness forces \(u(\alpha)\) to be real for real \(\alpha\); the sup-norm bound makes \(1+u(\alpha)>0\), with unit fibre mass. The conventional Perron operator then agrees with the holomorphic expression.

**4. Formal coefficients become genuine and convergent.** By Banach holomorphy, \(\varphi^*(\alpha)=1+\sum_{m\ge1}\alpha^m\varphi_m\) converges absolutely in \(X\) on smaller disks. Differentiating the pushforward identity \(m\) times against smooth tests and integrating by parts gives, for every \(m\ge1\),
\[
 (I-P_d)\varphi_{m,z}=
 \sum_{\substack{p\ge1,\ \ell,j_1,\ldots,j_p\ge0\\p+\ell+j_1+\cdots+j_p=m}}
 \frac{(-1)^p}{p!}\partial_x^p P_d\!
 \left[\biggl(\prod_{a=1}^p Q_{\varphi_{j_a},z}\biggr)\varphi_{\ell,z}\right],
 \qquad \varphi_{0,z}=1.
\]
Every right-hand term has zero mean and uses only lower-order coefficients. Invertibility from Step 1 identifies this recursion uniquely with the formal susceptibilities of Maquera, Proposition 3.9, for every finite order (choose the smoothness index in that paper arbitrarily large because the present local dynamics and coupling are analytic). Its Theorem 3.10 then gives the rooted-tree representation at each order. The theorem there supplies the **formal** tree identity; the present analytic argument supplies the missing proof that these coefficients are the actual Taylor coefficients and converge. Cauchy's Banach-valued estimate \(\|\varphi_m\|_X\le M_r r^{-m}\) followed by a geometric sum proves the remainder bound in the finding.

## Verification

A reproducible exact check uses \(d=2\),
\[
 h(x,y)=\cos(4\pi x)(1+\sin(2\pi y)),\qquad
 W=\begin{pmatrix}1&1/4\\1/4&1/2\end{pmatrix}
\]
on two graphon blocks of equal measure. Put \(D(z)=\int W(z,z')\,dz'\), \(E(z)=\int W(z,z')D(z')\,dz'\), so block values are \(D=(5/8,3/8)\) and \(E=(23/64,11/64)\). The first two coefficients, **already within the known two-order theory**, are
\[
 \varphi_{1,z}(x)=2\pi D(z)\sin(2\pi x),
 \qquad \varphi_{2,z}(x)=2\pi^2 E(z)\sin(2\pi x)
 -4\pi^2D(z)^2\bigl[\cos(4\pi x)+\cos(2\pi x)\bigr].
\]
The standalone checker `verify.py` evaluates both cohomological equations in exact symbolic Fourier arithmetic for each block, including the nonlinear first-order mean-field correction. Run `python verify.py` with SymPy installed; its expected final line begins `VERIFY_OK`. These checks test definitions, signs, and normalizations for a nonconstant graphon; they neither establish nor substitute for the infinite-order analytic proof.

## Relationship to prior work

Maquera (2026), arXiv:2611.10167v1, Proposition 3.9 and Theorem 3.10, **already** defines all formal susceptibility coefficients and proves their rooted-tree representation for each finite smoothness order. Proposition 3.11 establishes genuine coefficients through order two; the paper explicitly leaves both higher genuine response and convergence open. The present result proves precisely those two properties **only in the stated integer-affine analytic subclass**. It makes no originality claim to the recurrence, rooted-tree identity, first two coefficients, graphon framework, or standard analytic implicit-function theorem. Earlier self-consistent transfer-operator response theory by Sélley and Tanzi (2020), Galatolo (2021), and Castorrini–Galatolo–Tanzi (2025, 2026) concerns first-order response, differentiability or stability in related homogeneous/strong-coupling settings, not this all-order graphon statement. Analytic-transfer-operator theory for ordinary expanding maps supplies relevant background but does not by itself settle nonlinear graphon self-consistency.

## Limitations

The theorem is local at zero coupling, requires an integer affine expanding base map and a trigonometric-polynomial interaction, and does not provide an explicit or optimal radius \(\epsilon\). It establishes uniqueness only in a small analytic-density neighborhood, not among all invariant probability families. It does not prove global attraction, finite-network convergence, nonanalytic-coupling response, or all-order behavior for arbitrary nonlinear expanding base maps. It does not establish historical priority beyond the sources inspected. The full text of every potentially relevant older source was not available, and independent mathematical audit has not been performed.

## References

1. H. M. C. Maquera, *Linear Response for Self-Consistent Transfer Operators on Graphons*, arXiv:2611.10167v1 (first public version, 6 November 2026), especially §§3.3, 7 and Proposition 7.2. https://arxiv.org/html/2611.10167v1
2. F. M. Sélley and M. Tanzi, *Linear Response for a Family of Self-Consistent Transfer Operators*, arXiv:2001.01317 (2020). https://arxiv.org/abs/2001.01317
3. S. Galatolo, *Self consistent transfer operators: invariant measures, convergence to equilibrium, linear response and control of the statistical properties*, arXiv:2105.12388 (2021). https://arxiv.org/abs/2105.12388
4. R. Castorrini, S. Galatolo and M. Tanzi, *The Differential of Self-Consistent Transfer Operators and the Local Convergence to Equilibrium of Mean Field Strongly Coupled Dynamical Systems*, Journal of Nonlinear Science (2025). https://doi.org/10.1007/s00332-025-10177-0
5. O. F. Bandtlow and O. Jenkinson, *Invariant measures for real analytic expanding maps*, Journal of the London Mathematical Society 75 (2007). https://doi.org/10.1112/jlms/jdm001
