# A sharp cumulative heat-error law and horizon-dependent jump migration

## Finding
Let \(P_t=e^{t\Delta_N}\) be the Neumann heat semigroup on \((0,1)\), with diffusivity one, and \(V(f)=|Df|((0,1))\) for real \(f\in BV(0,1)\). Define the *cumulative* squared residual over an observation horizon \(T>0\) by
\[
\mathcal J_T(f)=\int_0^T\|(I-P_t)f\|_{L^2(0,1)}^2\,dt,
\qquad K(T)=\sup_{V(f)>0}\frac{\mathcal J_T(f)}{V(f)^2}.
\]
For every \(T>0\), the **exact attained** sharp constant is
\[
K(T)=\max_{0<s<1}J_T(s),\quad
J_T(s)=\frac2{\pi^2}\sum_{n=1}^\infty\frac{\sin^2(n\pi s)}{n^2}\left[T-\frac{2(1-e^{-\pi^2n^2T})}{\pi^2n^2}+\frac{1-e^{-2\pi^2n^2T}}{2\pi^2n^2}\right].
\]
Every nonconstant equality function is a single jump \(a+b\mathbf1_{(0,s)}\), with \(b\ne0\) and \(s\) maximizing \(J_T\). In particular, for **every \(T\ge1/2\)** the unique maximizing jump is at \(s=1/2\).

The genuinely different short-horizon behavior is governed by
\[
A(z)=(1+2z^2)\operatorname{erfc}(z)-\frac{2z}{\sqrt\pi}e^{-z^2},\qquad
G(z)=\int_0^z\left[2A(u)-A(u/\sqrt2)\right]du.
\]
The equation \(2A(\zeta)=A(\zeta/\sqrt2)\) has a **unique** positive root, \(\zeta=0.772397284434\ldots\), and \(G\) has its unique global maximum there. Put \(\kappa=G(\zeta)=0.257188139594\ldots\). Then
\[
\boxed{\lim_{T\downarrow0}\frac{K(T)}{T^{3/2}}=\kappa.}
\]
There is \(T_0>0\) such that, for every \(0<T<T_0\), the complete maximizing set consists of precisely two jumps at \(s_T\) and \(1-s_T\), where
\[
\boxed{\frac{s_T}{\sqrt T}\longrightarrow\zeta.}
\]
The bulk single-jump cumulative coefficient is only \(2(2-\sqrt2)/(3\sqrt\pi)=0.220329737528\ldots\), so allowing a boundary-scale jump gives a \(16.72874596\ldots\%\) gain. This **cumulative** optimal position differs from the single-time Gaussian optimum \(0.992269655382\ldots\); integrating the single-time sharp constants is therefore not a sharp cumulative estimate.

## Assumptions and scope
The interval is the unit open interval and \(\Delta_N\) has homogeneous Neumann conditions on both ends. \(BV(0,1)\) denotes real-valued equivalence classes of functions with finite distributional variation on the open interval; endpoint trace jumps are not separately counted. The heat diffusivity is one. \(\operatorname{erfc}(z)=(2/\sqrt\pi)\int_z^\infty e^{-v^2}dv\). Observations are integrated with respect to ordinary unweighted Lebesgue time measure from zero to a finite horizon \(T\), and the spatial squared error uses unweighted Lebesgue measure. The threshold \(T_0\) is positive but not specified numerically. The sufficient large-horizon condition \(T\ge1/2\) is not asserted sharp.

## Proof
**1. Exact global reduction to a single jump.** Every real \(f\in BV(0,1)\) is, up to a constant, a signed derivative-measure superposition \(f(x)=c+\int_{(0,1)}\mathbf1_{(0,s)}(x)\,d\mu(s)\) almost everywhere, with \(|\mu|((0,1))=V(f)\). Regard \(R_sf\) here as the single-jump space-time residual \(R_s(t,x)=(I-P_t)\mathbf1_{(0,s)}(x)\) in \(\mathcal H_T=L^2((0,T)\times(0,1))\). Bochner integration and Minkowski yield
\[
\mathcal J_T(f)^{1/2}\le\int\|R_s\|_{\mathcal H_T}d|\mu|(s)\le V(f)\max_sJ_T(s)^{1/2}.
\]
Each jump has \(V=1\), giving the exact supremum. Equality in the Hilbert triangle inequality requires all nonzero \(R_s\) on one positive ray. For distinct \(s,u\), proportionality of these space-time vectors would imply proportionality at almost every positive time. For such a time, \(I-P_t\) annihilates only constants by the Neumann spectral gap, and a nontrivial linear combination of distinct step indicators cannot be constant. Thus a nonconstant equality function has exactly one derivative atom. The stated spectral formula follows from the normalized Neumann cosine coefficients \(\sqrt2\sin(n\pi s)/(n\pi)\) and termwise integration of their squared heat-residual multipliers.

**2. A rigorously unique cumulant-profile maximizer.** For \(z\ge0\) write \(E(z)=\operatorname{erfc}(z)\). Its hazard \(m_E(z)=-E'(z)/E(z)\) increases strictly: its reciprocal equals \(\int_0^\infty e^{-v^2-2zv}dv\), which strictly decreases. Hence \(E\) is strictly log-concave. We use the following elementary tail lemma, with proof: if \(g\) is positive, integrable, strictly log-concave on \([0,\infty)\), then \(\widehat g(z)=\int_z^\infty g(u)du\) is strictly log-concave. Indeed for fixed \(v>0\), the ratio \(g(z+v)/g(z)\) strictly decreases in \(z\); therefore \(\widehat g(z)/g(z)=\int_0^\infty[g(z+v)/g(z)]dv\) strictly decreases, and \(-\widehat g'(z)/\widehat g(z)=g(z)/\widehat g(z)\) strictly increases. Apply the lemma twice to \(E\). Direct differentiation of the displayed expression for \(A\) gives \(A''(z)=4E(z)\), \(A(\infty)=A'(\infty)=0\); therefore \(A(z)=4\int_z^\infty\int_v^\infty E(w)dw\,dv\), which is strictly log-concave, positive and decreasing.

Consequently \(A(z)/A(z/\sqrt2)\) strictly decreases, because its logarithmic derivative is \(-m_A(z)+m_A(z/\sqrt2)/\sqrt2<0\) with strictly increasing positive hazard \(m_A=-A'/A\). The ratio starts at one and tends to zero by the Gaussian tail asymptotics. Thus \(G'(z)=2A(z)-A(z/\sqrt2)\) changes sign exactly once, positively to negatively, at \(\zeta\), proving uniqueness and nondegeneracy (\(G''(\zeta)<0\)). Moreover \(G(0)=0\) and \(G(\infty)=2(2-\sqrt2)/(3\sqrt\pi)<G(\zeta)\).

**3. Gaussian boundary-layer limit uniform across all knots.** Define \(h(z)=2\operatorname{erfc}(z)-\operatorname{erfc}(z/\sqrt2)\), and let \(\widetilde h\) denote its odd extension. Fourier coefficients of the Neumann heat-filtered single step (equivalently Gaussian image reflection) give the exact derivative identity for \(0<s<1\):
\[
\frac{d}{ds}\|(I-P_t)\mathbf1_{(0,s)}\|_2^2
=\sum_{k\in\mathbb Z}\widetilde h\left(\frac{s-k}{\sqrt t}\right).
\]
On \(0<s\le1/2\), all nonzero images lie at distance at least \(1/2\), and Gaussian complementary-error-function bounds give a uniform remainder \(O(e^{-c/t})\) for small \(t\), with corresponding scaled derivatives on compact positive distance ratios. Integrating from \(0\) to \(T\) therefore yields, uniformly in \(0\le s\le1/2\),
\[
J_T'(s)=T\left[2A\!\left(\frac{s}{\sqrt T}\right)-A\!\left(\frac{s}{\sqrt{2T}}\right)\right]+O(Te^{-c/T}),
\]
\[
J_T(s)=T^{3/2}G(s/\sqrt T)+O(Te^{-c/T}).
\]
The identity \(\int_0^1\operatorname{erfc}(z/\sqrt u)du=A(z)\) follows from a substitution and one integration by parts, giving the displayed derivative and the specific \(G\). The error bounds follow from summing Gaussian images and integrating \(\int_0^T e^{-c/t}dt\le Te^{-c/T}\).

**4. Global short-time rigidity.** Because \(G\) has a strict isolated maximum above both \(G(0)\) and \(G(\infty)\), the uniform approximation forces every maximizing \(s\in[0,1/2]\) to lie in a \(\sqrt T\)-scale compact neighborhood of \(\zeta\) for sufficiently small \(T\). On that compact neighborhood the rescaled first and second derivatives converge uniformly to \(G'\) and \(G''\). By \(G''(\zeta)<0\), \(J_T'\) is strictly decreasing through its unique zero there, so exactly one half-interval maximizer \(s_T\) exists and \(s_T/\sqrt T\to\zeta\). Neumann reflection \(J_T(1-s)=J_T(s)\) supplies exactly the two indicated knots. Substitution into the uniform expansion proves the sharp limit and all short-time equality cases.

**5. An exact midpoint theorem at long horizons.** Write \(\lambda_n=\pi^2n^2\) and \(b_n(T)=[3/2-2e^{-\lambda_nT}+e^{-2\lambda_nT}/2]/\lambda_n\). Then \(0<b_n(T)<3/(2\lambda_n)\) and
\[
J_T(s)=T s(1-s)-\frac2{\pi^2}\sum_{n\ge1}\frac{b_n(T)\sin^2(n\pi s)}{n^2}.
\]
The correction has absolutely convergent second derivative, and
\[
J_T''(s)=-2T-4\sum_{n\ge1}b_n(T)\cos(2\pi ns)
<-2T+4\sum_{n\ge1}\frac3{2\pi^2n^2}=-2T+1.
\]
For \(T\ge1/2\), strict concavity follows. Symmetry forces the unique maximizing knot to be exactly \(s=1/2\). This establishes a genuine shift from two near-wall optimal jumps at short horizons to one central optimum at all sufficiently long horizons, without asserting a sharp transition time.

## Verification
The accompanying executable \(check.py\) reproduces the unique \(A\)-ratio crossing and numerical cumulative coefficient, verifies numerical derivative and tail identities, compares independent quadrature and spectral finite-horizon calculations, checks the short-horizon optimizer scaling, and tests the uniform \(J_T\) concavity at long horizons. Finite computations are supplementary; the analytical argument above proves the infinite-dimensional bound, uniqueness, global localization and horizon-dependent midpoint theorem.

## Relationship to prior work
Miranda, Pallara, Paronetto and Preunkert (public manuscript inserted 2005-02-19) established heat-semigroup characterizations of Euclidean \(BV\) and short-time perimeter laws. Choulli, Kayser and Ouhabaz (public manuscript 2015-02-24) established Gaussian Neumann heat-kernel upper bounds. Neither supplies the present **time-integrated sharp variation-to-spacetime-\(L^2\) norm**, its new profile root, or the large-horizon exact midpoint theorem.

A previously established periodic *single-time* squared heat-residual norm has a Gaussian near-jump optimizer at \(0.992269655382\ldots\), and a reflecting-interval *single-time* \(L^1\) residual norm selects the midpoint. The first does **not** imply the cumulative sharp norm by integrating its separately optimized values; the cumulative maximizer here is \(0.772397284434\ldots\), hence the two optimizations do not commute. The second concerns a different output norm. Our contribution is the genuinely time-integrated objective and its complete short-/long-horizon optimizer regimes, not a reassertion of an instantaneous heat result.

## Limitations
The small-horizon threshold \(T_0\) is existential. The exact intermediate-horizon switching time and complete intermediate maximizer diagram are not determined. The result concerns real \(BV(0,1)\), interior distributional variation, Neumann heat diffusion, ordinary time integration and spatial \(L^2\); no Dirichlet, drifted, fractional or higher-dimensional analogue is asserted. Residual historical-priority risk remains, especially for unindexed parabolic functional inequalities. The self-review is not independent validation.

## References
1. M. Miranda Jr., D. Pallara, F. Paronetto, M. Preunkert, *Short-time Heat Flow and Functions of Bounded Variation in \(\mathbb R^N\)*. Public manuscript dated 2005-02-19: https://cvgmt.sns.it/paper/801/ ; accessible article https://cvgmt.sns.it/document/686/ ; *Ann. Fac. Sci. Toulouse Math.* 16 (2007), 125–145, https://doi.org/10.5802/afst.1142 .
2. M. Choulli, L. Kayser, E. M. Ouhabaz, *Observations on Gaussian Upper Bounds for Neumann Heat Kernels*. Public manuscript dated 2015-02-24: https://arxiv.org/abs/1502.06740 .
3. M. Miranda Jr., D. Pallara, F. Paronetto, M. Preunkert, *Heat Semigroup and Functions of Bounded Variation on Riemannian Manifolds*, https://cvgmt.sns.it/paper/376/ ; *J. Reine Angew. Math.* 613 (2007), 99–119.
