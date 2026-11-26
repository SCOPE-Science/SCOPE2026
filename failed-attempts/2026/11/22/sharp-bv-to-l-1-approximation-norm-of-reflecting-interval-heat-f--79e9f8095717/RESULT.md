# Sharp \(BV\)-to-\(L^1\) approximation norm of reflecting interval heat flow

## Finding
Let \(H_t=\exp(t\Delta_N)\), \(t>0\), be the heat semigroup on \((0,1)\) with reflecting (homogeneous Neumann) boundary conditions and generator \(\Delta_N=\partial_x^2\). On real distributional \(BV(0,1)\), modulo additive constants, its **exact** approximation-error operator seminorm is
\[
\boxed{\sup_{|Df|(0,1)>0}\frac{\|H_tf-f\|_{L^1(0,1)}}{|Df|(0,1)}
=C(t):=\frac12-\frac4{\pi^2}\sum_{j=0}^{\infty}\frac{\exp(-(2j+1)^2\pi^2t)}{(2j+1)^2}.}
\]
For every finite \(t>0\), equality holds for a nonconstant real \(f\in BV(0,1)\) **if and only if**, up to almost-everywhere equality, \(f(x)=a+b\mathbf 1_{(1/2,1)}(x)\) with \(a\in\mathbb R\) and \(b\in\mathbb R\setminus\{0\}\). The coefficient has the additional exact properties
\[
C'(t)=4\sum_{j=0}^{\infty}e^{-(2j+1)^2\pi^2t}>0,\qquad
C''(t)=-4\pi^2\sum_{j=0}^{\infty}(2j+1)^2e^{-(2j+1)^2\pi^2t}<0.
\]
In particular, the sharp error increases strictly and concavely from zero toward \(1/2\), with both endpoint asymptotics
\[
C(t)=\frac{2\sqrt t}{\sqrt\pi}+O\!\left(t^{3/2}e^{-1/(4t)}\right)\quad(t\downarrow0),\qquad
C(t)=\frac12-\frac4{\pi^2}e^{-\pi^2t}+O(e^{-9\pi^2t})\quad(t\to\infty).
\]

## Assumptions and scope
The interval is open and has unit length. \(BV(0,1)\) means real \(L^1\)-classes whose distributional derivative is a finite signed Radon measure on \((0,1)\); \(|Df|(0,1)\) is the **interior** variation and does not charge endpoint traces. The Neumann operator acts on \(L^2(0,1)\) with domain \(\{u\in H^2(0,1):u'(0)=u'(1)=0\}\), and \(H_t\) extends consistently to \(L^1\). The diffusion convention is \(\partial_tu=\partial_x^2u\), not the generator \(\tfrac12\partial_x^2\). The factor for an interval of length \(L\) follows by spatial rescaling: \(C_L(t)=L C(t/L^2)\). No claim is made for nonreflecting conditions, higher-dimensional sets, or drift.

For \(0<s<1\) write \(J_s(x)=\mathbf1_{(s,1)}(x)\). Denote the positive symmetric Neumann heat kernel by \(p_t(x,y)\), so that \(H_tf(x)=\int_0^1p_t(x,y)f(y)\,dy\). The spectral and image representations used below are
\[
p_t(x,y)=1+2\sum_{k=1}^{\infty}e^{-k^2\pi^2t}\cos(k\pi x)\cos(k\pi y),
\]
\[
p_t(x,y)=N_t(x-y)+N_t(x+y),\quad
N_t(z)=\sum_{m\in\mathbb Z}\frac{e^{-(z+2m)^2/(4t)}}{\sqrt{4\pi t}}
=\frac12\left(1+2\sum_{k=1}^{\infty}e^{-k^2\pi^2t}\cos(k\pi z)\right).
\]
All differentiations of these series for strictly positive time are justified by uniform exponential convergence. The wrapped Gaussian \(N_t\) is even and two-periodic.

## Proof
**1. Signed-jump reduction.** Every \(f\in BV(0,1)\) has a representative, modulo a constant, of the form \(f(x)=\int_{(0,1)}J_s(x)\,d\mu(s)\) for almost every \(x\), where \(\mu=Df\). This follows from the distributional fundamental theorem for one-dimensional \(BV\); Fubini is legitimate since \(\mu\) is finite. Because \(H_t\) preserves constants and is an \(L^1\)-contraction, Minkowski's integral inequality gives
\[
\|H_tf-f\|_1\le\int_{(0,1)}\|H_tJ_s-J_s\|_1\,d|\mu|(s)
\le\left(\sup_{0<s<1}E_t(s)\right)|Df|(0,1),
\]
where \(E_t(s)=\|H_tJ_s-J_s\|_1\). Conversely, \(|DJ_s|(0,1)=1\), so the operator norm equals \(\max_sE_t(s)\) once the maximum is found.

**2. Heat crossing and differentiation.** Positivity and mass preservation imply
\[
E_t(s)=\int_0^sH_tJ_s(x)\,dx+\int_s^1(1-H_tJ_s(x))\,dx.
\]
Symmetry \(p_t(x,y)=p_t(y,x)\) makes the two integrals equal. Consequently
\[
E_t(s)=2\int_0^s\int_s^1p_t(x,y)\,dy\,dx.
\]
Differentiating the moving limits and using \(\int_0^1p_t(s,y)\,dy=1\) yields
\[
E_t'(s)=2\left(1-2F_t(s)\right),\qquad
F_t(s)=\int_0^sp_t(s,y)\,dy.
\]
For fixed \(0<s<1\), regard the first argument \(s\) in \(F_t(s)\) as the fixed starting point while differentiating **time**. The heat equation in its integration variable and the Neumann boundary condition give
\[
\partial_tF_t(s)=\partial_yp_t(s,y)|_{y=s}-\partial_yp_t(s,y)|_{y=0}=N_t'(2s).
\]
Because the heat kernel converges to an interior point mass, \(\lim_{t\downarrow0}F_t(s)=1/2\), hence
\[
E_t'(s)=-4\int_0^tN_\tau'(2s)\,d\tau.
\]

**3. Critical strict wrapped-Gaussian monotonicity.** For \(\tau>0\), put \(q=e^{-\pi^2\tau}\). The classical Jacobi triple-product identity gives the convergent positive product
\[
N_\tau(z)=\frac12\prod_{j=1}^{\infty}(1-q^{2j})
\left(1+2q^{2j-1}\cos(\pi z)+q^{4j-2}\right).
\]
For every \(0<z<1\), each variable-dependent factor is strictly positive and has strictly negative derivative. More explicitly,
\[
\frac{d}{dz}\log N_\tau(z)
=-2\pi\sin(\pi z)\sum_{j=1}^{\infty}
\frac{q^{2j-1}}{1+2q^{2j-1}\cos(\pi z)+q^{4j-2}}<0.
\]
For \(0<s<1/2\), one has \(0<2s<1\); therefore \(E_t'(s)>0\). The reflection identity \(p_t(1-x,1-y)=p_t(x,y)\) gives \(E_t(1-s)=E_t(s)\). Hence \(E_t\) increases strictly on \((0,1/2)\), decreases strictly on \((1/2,1)\), and has the **unique** maximizing jump at \(s=1/2\). This argument proves the crucial global inequality without relying on sampled numerics.

**4. Exact center value.** Integrating the cosine kernel across the midpoint gives, for every \(t>0\),
\[
E_t(s)=2s(1-s)-4\sum_{k=1}^{\infty}
\frac{e^{-k^2\pi^2t}\sin^2(k\pi s)}{k^2\pi^2}.
\]
Putting \(s=1/2\), the even terms disappear and the odd terms have squared sine equal to one; this produces the boxed formula for \(C(t)\). The single jump \(J_{1/2}\) attains it. If equality holds for a general \(f\), the second inequality in Step 1 forces \(|Df|\) to be supported by the unique maximizer \(\{1/2\}\). Thus \(Df=b\delta_{1/2}\) and the only nonconstant equality cases are precisely the claimed centered jumps.

**5. Time behavior.** Termwise differentiation gives the formulas for \(C'\) and \(C''\), showing strict increase and concavity. Summing odd inverse squares gives \(C(0+)=1/2-(4/\pi^2)(\pi^2/8)=0\); exponential decay gives \(C(\infty)=1/2\). Poisson summation for the odd Gaussian series yields the exact identity
\[
C'(t)=\frac1{\sqrt{\pi t}}\sum_{m\in\mathbb Z}(-1)^m e^{-m^2/(4t)}.
\]
The central term dominates as \(t\downarrow0\); integrating from zero proves \(C(t)=2\sqrt{t/\pi}+O(t^{3/2}e^{-1/(4t)})\). Keeping the first odd eigenmode proves the large-time expansion. The proof is complete.

## Verification
Execute `python3 check.py` with standard Python 3. The checker independently evaluates the heat kernel by its cosine expansion, midpoint quadrature of the crossing integral, centered-jump sharp coefficients, sample monotonicity and reflection, signed multijump inequalities, derivatives and endpoint asymptotics. Its exact terminal message is `ALL_NEUMANN_BV_L1_CHECKS_PASS`. All these are numerical finite checks; the strict global maximizer, equality classification, and all-time assertions are proved in Steps 1–5 and **not inferred from computation**. The Jacobi triple product, normalization of the generator and treatment of interior rather than trace variation are critical proof premises.

## Relationship to prior work
Angiuli–Miranda–Pallara–Paronetto (2008) prove variation recovery and heat-semigroup BV estimates for general Neumann-type parabolic problems, including variation diminution on convex domains. Their estimates concern \(|D(H_tf)|\) and its small-time convergence to \(|Df|\), rather than the exact finite-time \(BV/\mathbb R\to L^1\) approximation norm of \(I-H_t\). Choulli–Kayser–Ouhabaz (2015) establish heat-kernel bounds and analyticity for Neumann semigroups, without the interval midpoint extremizer and exact odd-mode error constant. Angeloni–Vinti (2016) review convolution/integral approximations in variation; those variation-convergence estimates do not give this all-time reflected-boundary norm. Later work of Alonso Ruiz–Baudoin on heat-semigroup BV characterizations studies asymptotic perimeter recovery rather than this finite-time sharp coefficient. The present proof exploits strict unimodality of the wrapped Gaussian to identify a unique interior norming jump.

## Limitations
The exact law is proved only for real one-dimensional distributional BV on an interval, reflecting boundary conditions, the classical unweighted Lebesgue \(L^1\) norm and the heat generator specified above. The spectrum and unique-extremizer argument use interval symmetry and should not be transferred to drifted, Robin, Dirichlet, nonlinear or multidimensional semigroups without further proof. The first term \(2\sqrt{t/\pi}\) is consistent with classical heat-content asymptotics and is **not** itself claimed novel. Historical originality is assessed against accessible cited sources and public search results, not established independently for every unindexed work.

## References
- L. Angiuli, M. Miranda Jr, D. Pallara, F. Paronetto, *BV functions and parabolic initial boundary value problems on domains*, Annali di Matematica Pura ed Applicata 188 (2009), 297–331; first published online 25 April 2008. https://doi.org/10.1007/s10231-008-0076-3
- M. Choulli, L. Kayser, E. M. Ouhabaz, *Observations on Gaussian upper bounds for Neumann heat kernels*, first posted 24 February 2015. https://arxiv.org/abs/1502.06740
- L. Angeloni, G. Vinti, *A Review on Approximation Results for Integral Operators in the Space of Functions of Bounded Variation*, Journal of Function Spaces (2016), article 3843921, first published 26 September 2016. https://doi.org/10.1155/2016/3843921
- P. Alonso Ruiz, F. Baudoin, *Yet another heat semigroup characterization of BV functions on Riemannian manifolds*, first posted 23 October 2020; Ann. Fac. Sci. Toulouse 32 (2023), 577–606. https://arxiv.org/abs/2010.12131
