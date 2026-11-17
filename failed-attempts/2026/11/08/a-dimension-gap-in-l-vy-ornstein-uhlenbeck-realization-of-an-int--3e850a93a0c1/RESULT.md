# A dimension gap in Lévy–Ornstein–Uhlenbeck realization of an intermittently trapped Brownian particle

## Finding

For a common two-state switching harmonic trap in every integer spatial dimension \(d\ge2\), let \(\mu_{\alpha,d}\) be the stationary vector-position law at switching rate \(\alpha>0\), with the trap and diffusivity normalized as below. Its characteristic function is the previously known isotropic transform
\[
 \phi_{\alpha,d}(q)=e^{-|q|^2/2}
 \left(1+\frac{|q|^2}{2\alpha}\right)
 \left(1+\frac{|q|^2}{\alpha}\right)^{-1-\alpha/2}.
\]
The vector law is infinitely divisible for every \(\alpha>0\), but it is **self-decomposable as a probability law on \(\mathbb R^d\) if and only if \(\alpha\ge2\)**. Equivalently, exactly in this range it is the stationary one-time marginal of an isotropic scalar-reversion Lévy-driven Ornstein–Uhlenbeck equation \(dY_t=-Y_t\,dt+dL_t\).

The distinction is invisible to scalar observations: every one-dimensional projection of \(\mu_{\alpha,d}\) is self-decomposable whenever \(\alpha\ge2(\sqrt2-1)\). Thus throughout the **nonempty sharp interval**
\[
 \boxed{2(\sqrt2-1)\le\alpha<2}
\]
all scalar projections belong to class \(L\), yet the full joint vector law does not. The one-dimensional cutoff and the original stationary transform are prior results, not claimed here as discoveries. The new assertion is the exact all-dimensional vector cutoff and this strict joint-versus-projection separation for the physical model.

When \(\alpha\ge2\), the explicit stationary-equivalent bath consists of independent standard Brownian driving with covariance rate \(2I_d\) and a symmetric, isotropic compound-Poisson driver of **total jump rate exactly \(\alpha\)**. Its fully determined jump Lévy density is displayed in the proof. The equality is only of stationary one-time distributions: neither temporal correlations nor sample paths of the switched-trap model are reproduced in general.

## Assumptions and scope

Fix an integer \(d\ge2\) and \(\alpha>0\). Let \(S_t\in\{0,1\}\) be a stationary continuous-time Markov chain that flips between its two states at rate \(\alpha\) in either direction. Let \(W\) be a standard \(d\)-dimensional Brownian motion independent of \(S\). The switched-trap diffusion is
\[
 dX_t=-S_tX_t\,dt+\sqrt2\,dW_t,
\]
where **the same** switch \(S_t\) acts on all coordinates. The trap-on relaxation rate and diffusion generator have been normalized to one and \(\Delta\), respectively. The original dimensional switching-to-relaxation ratio is \(\alpha=(\mu K\tau)^{-1}\), with the notation of Frydel's 2024 model. The process has a unique stationary position marginal: its stationary stochastic-convolution construction converges because the ergodic trap spends asymptotically half of the time on, and coupling gives uniqueness.

For the scalar-drift OU comparison, the mean-reversion matrix is fixed to \(I_d\), and \(L\) is a genuine \(\mathbb R^d\)-valued Lévy process with stationary independent increments. No characterization of OU processes with an arbitrary nonscalar drift matrix, non-Lévy bath, or nonstationary forcing is implied.

Set \(k=\alpha/2\), \(\nu=d/2\), \(a=\sqrt\alpha\), \(b=\sqrt{2\alpha}\). Write \(K_\nu\) for the standard modified Bessel function of the second kind. For \(c>0\), define the radial density function
\[
 F_{c,d}(r)=\frac{2}{(2\pi)^\nu}
 \left(\frac{\sqrt c}{r}\right)^\nu K_\nu(\sqrt c\,r),\qquad r>0.
\]

## Proof

**1. The known stationary transform and a direct normalization check.** Let \(s=|q|^2\) and let \(\phi_+(s),\phi_-(s)\) be the joint stationary characteristic transforms of position and trap-on/off state. Their Markov-generator equations are
\[
 0=-2s\phi_+'(s)-s\phi_+(s)+\alpha(\phi_-(s)-\phi_+(s)),
\]
\[
 0=-s\phi_-(s)+\alpha(\phi_+(s)-\phi_-(s)),
\]
with \(\phi_+(0)=\phi_-(0)=1/2\). Solving the second equation and then the first gives
\[
 \phi_+(s)=\tfrac12e^{-s/2}(1+s/\alpha)^{-k},\quad
 \phi_-(s)=\tfrac12e^{-s/2}(1+s/\alpha)^{-k-1}.
\]
Their sum is the transform in the Finding. This also follows from the source's Gaussian-mixture result, which remains valid in all dimensions. For example, conditionally on a nonnegative mixture variable \(U\) that is an equal-weight mixture of Gamma distributions of shapes \(k\) and \(k+1\), both of rate one, the position vector has covariance \((1+2U/\alpha)I_d\). Hence the Gaussian mixture is a genuine probability law and its characteristic transform is as claimed.

**2. An explicit infinitely divisible vector Lévy measure.** The logarithmic characteristic exponent is
\[
 -\log\phi_{\alpha,d}(q)=\tfrac12|q|^2+
 (k+1)\log(1+|q|^2/\alpha)-\log(1+|q|^2/(2\alpha)).
\]
For \(s\ge0\), use
\[
 \log(1+s/c)=\int_0^\infty(1-e^{-st})\frac{e^{-ct}}t\,dt.
\]
The non-Gaussian part is obtained by Brownian subordination with **positive** subordinator Lévy density
\[
 \frac{(k+1)e^{-\alpha t}-e^{-2\alpha t}}t
 =\frac{ke^{-\alpha t}+e^{-\alpha t}(1-e^{-\alpha t})}t>0.
\]
Thus the vector law is infinitely divisible for every positive \(\alpha\). Evaluating the heat-kernel integral
\[
 \int_0^\infty(4\pi t)^{-d/2}e^{-r^2/(4t)}\frac{e^{-ct}}t\,dt
 =F_{c,d}(r)
\]
gives its canonical radial Lévy density with respect to Lebesgue measure \(dx\):
\[
 \boxed{\ell_{\alpha,d}(r)=(k+1)F_{\alpha,d}(r)-F_{2\alpha,d}(r)>0.}\tag{1}
\]
The Gaussian covariance of the infinitely divisible law is \(I_d\). The Lévy density is unique.

**3. A sharp multivariate class-\(L\) test.** For an isotropic infinitely divisible distribution on \(\mathbb R^d\) with Lebesgue Lévy density \(\ell(|x|)\), the classical polar criterion for self-decomposability is exactly that
\[
 r\longmapsto r^d\ell(r)\quad\text{be nonincreasing on }(0,\infty).
\]
This is the usual condition that the Lévy radial measure has density \(h(r)\,dr/r\) along every direction, with \(h\) nonincreasing. It is dimension-sensitive: the Jacobian is \(r^{d-1}\), not the one-dimensional \(r^0\).

The standard Bessel identity \(\frac d{dz}[z^\nu K_\nu(z)]=-z^\nu K_{\nu-1}(z)\) applied to (1) yields
\[
 \frac d{dr}\bigl[r^d\ell_{\alpha,d}(r)\bigr]
 =-\frac2{(2\pi)^\nu}\left[(k+1)a(ar)^\nu K_{\nu-1}(ar)
       -b(br)^\nu K_{\nu-1}(br)\right].\tag{2}
\]
For \(d\ge2\), set \(\beta=\nu-1\ge0\) and \(H_\beta(z)=z^\beta K_\beta(z)\). This is positive and strictly decreasing on \((0,\infty)\), since
\[
 H_\beta'(z)=-z^\beta K_{\beta-1}(z)<0.
\]
The ratio of the positive second and first Bessel terms in square brackets in (2), *before* multiplying the first by \(k+1\), is
\[
 R_d(r)=\frac{b(br)^\nu K_{\nu-1}(br)}{a(ar)^\nu K_{\nu-1}(ar)}
 =2\frac{H_\beta(br)}{H_\beta(ar)}<2.\tag{3}
\]
Moreover, \(\lim_{r\downarrow0}R_d(r)=2\): for \(\beta>0\), \(H_\beta(z)\to2^{\beta-1}\Gamma(\beta)\); for \(\beta=0\), \(K_0(z)\sim-\log z\) and the ratio also tends to one. Thus (2) is nonpositive at every radius **if and only if** \(k+1\ge2\), namely \(\alpha\ge2\). For \(\alpha<2\), the derivative is strictly positive at sufficiently small radii, precluding class \(L\). For \(\alpha\ge2\), it is strictly negative at every positive radius; the critical value is included. This proves the exact vector threshold in every finite integer dimension \(d\ge2\).

**4. Constructive independent-increment OU bath.** In the attainable range define the nonnegative radial Lévy density
\[
 \boxed{j_{\alpha,d}(x)=
 \frac{2|x|^{1-\nu}}{(2\pi)^\nu}
 \left[(k+1)a^{\nu+1}K_{\nu-1}(a|x|)
         -b^{\nu+1}K_{\nu-1}(b|x|)\right],\quad x\ne0.}\tag{4}
\]
By (2) this equals \(-r^{1-d}\frac d{dr}[r^d\ell_{\alpha,d}(r)]\) for \(r=|x|\); positivity follows from (3). The exact normalization is obtained without numerics. The surface area of the unit sphere is \(\omega_{d-1}=2\pi^\nu/\Gamma(\nu)\), and
\[
 \lim_{r\downarrow0}r^d\ell_{\alpha,d}(r)
 =\frac{\alpha\Gamma(\nu)}{2\pi^\nu},\qquad
 \lim_{r\to\infty}r^d\ell_{\alpha,d}(r)=0.
\]
Hence radial integration and the derivative representation give
\[
 \int_{\mathbb R^d}j_{\alpha,d}(x)\,dx
 =\omega_{d-1}\int_0^\infty j_{\alpha,d}(r)r^{d-1}\,dr
 =\alpha.
\]
Take \(L\) to be independent Brownian motion of covariance rate \(2I_d\) plus a centered, isotropic compound-Poisson process with Lévy density (4) and total jump intensity \(\alpha\). The unique stationary OU solution of \(dY_t=-Y_t\,dt+dL_t\) has Gaussian covariance \(I_d\). Its jump Lévy density equals
\[
 \int_0^\infty e^{ds}j_{\alpha,d}(e^sx)\,ds
 =|x|^{-d}\int_{|x|}^\infty u^{d-1}j_{\alpha,d}(u)\,du
 =\ell_{\alpha,d}(|x|).
\]
Its full stationary Lévy triplet therefore equals that of \(\mu_{\alpha,d}\). Conversely, any stationary law of a scalar-drift Lévy OU is self-decomposable, and so none exists below \(\alpha=2\).

**5. Strict projection–vector separation.** For every unit vector \(u\), the projection \(u\cdot X\) has the same characteristic transform as the one-dimensional switched-trap law, regardless of ambient dimension. That law's known one-dimensional class-\(L\) threshold is \(\alpha\ge2(\sqrt2-1)\), by the same canonical-density criterion with the one-dimensional polar Jacobian. (Indeed, its monotonicity ratio is \(\sqrt2\exp[-(\sqrt2-1)\sqrt\alpha\,r]\).) This threshold is smaller than two, so (3) proves the claimed strict interval in which all one-dimensional linear projections are self-decomposable but the full spatial vector is not.

## Verification

The standalone script `verify.py` reconstructs the stationary Gaussian-mixture transform, the positive-subordinator exponent, second/fourth moments, the Bessel-profile derivative, its sign across dimensions one through six, the dimension-two logarithmic small-radius limit at high precision, and the jump intensity by radial numerical quadrature. It produced `PASS: 393 computational diagnostic assertions` with NumPy, SciPy and mpmath. The exact all-dimensional and all-parameter claims above are established by the displayed algebra and Bessel monotonicity, **not** by these finite diagnostics.

For a concrete strict example, take \(d=2\) and \(\alpha=1\). Both coordinate marginals and every scalar projection are self-decomposable because \(1>2(\sqrt2-1)\), while the joint two-dimensional distribution fails the necessary polar monotonicity near the origin because \(1<2\). This is a statement about the shared-switch two-coordinate joint law, not two independently switched traps.

## Relationship to prior work

Frydel (2024), arXiv:2407.12213v1 (July 16, 2024), already obtains the Gaussian-mixture stationary position law, its one-dimensional characteristic function and its all-dimensional extension. Those are the input, not new claims. Earlier one-dimensional analyses of the switched harmonic trap already establish infinite divisibility and the exact scalar self-decomposability/OU threshold, even for some unequal switching rates; the scalar cutoff is used only for comparison. The present contribution is the previously unaccounted **full-vector radial Lévy measure**, its different exact cutoff \(\alpha=2\) for every \(d\ge2\), and the resulting interval of scalar self-decomposability without joint self-decomposability.

The general polar class-\(L\) criterion and the Bessel heat-kernel identity are classical and are used as tools. Sato (2001) proves the sufficient inheritance of self-decomposability under stable Brownian subordination; here the positive subordinator itself is self-decomposable exactly when \(\alpha\ge2\) because \(t\) times its Lévy density is \(q(t)=(1+\alpha/2)e^{-\alpha t}-e^{-2\alpha t}\), and \(q\) is nonincreasing exactly in that range. This inherited sufficiency does not on its own establish the converse for the specific vector law or the strict scalar-versus-joint gap. Buchmann, Lu and Madan analyze multivariate variance-generalized-gamma-convolution laws subordinated by Thorin subordinators; that framework is not an automatic coverage of this law, since the relevant subordinator density has a difference of exponentials and its \(t\)-multiplier fails complete monotonicity. Literature on Lévy copulas contains other examples where marginal self-decomposability does not lift to the joint law; those examples do not give this physical distribution or its cutoff. Work on Gaussian compound-Poisson shocks added to symmetric variance-gamma laws addresses another Lévy family and does not yield (1)–(4). Work on Markov-modulated OU processes is related, but the comparison is confined to *stationary one-time* laws and scalar-reversion Lévy forcing.

## Limitations

The claim concerns the common-switch, isotropic two-state on/off trap in finite integer dimensions, with equal on/off switching rates and positive rates. Anisotropic stiffness or independent switches per coordinate can change the cutoff. The exact bath reproduces only the one-time stationary distribution, not the Markov modulation or its time correlations. The obstruction does not rule out all conceivable non-scalar-drift OU realizations. No distributional-tail ordering, estimation theorem or statement about pathwise equivalence is claimed. Publication priority remains subject to independent literature scrutiny, particularly broader Markov-modulated OU and convolution-factor results that could contain an equivalent vector-Lévy statement under different language.

## References

1. D. Frydel, *Statistical mechanics of passive Brownian particles in a fluctuating harmonic trap*, arXiv:2407.12213v1 (July 16, 2024), https://arxiv.org/abs/2407.12213 ; *Physical Review E* **110**, 024613 (2024), https://doi.org/10.1103/PhysRevE.110.024613 . Stationary mixture/transform and extension to arbitrary dimension.
2. K.-I. Sato, *Lévy Processes and Infinitely Divisible Distributions*, Cambridge University Press (1999), Chapter 3. Classical multivariate self-decomposability/polar Lévy measure and OU integral representations.
3. B. Buchmann, K. W. Lu and D. B. Madan, *Selfdecomposability of Weak Variance Generalised Gamma Convolutions*, arXiv:1712.03640 (2017), https://arxiv.org/abs/1712.03640 . Closely related multivariate subordination framework.
4. O. E. Barndorff-Nielsen et al., *Lévy Copulas: Dynamics and Transforms of Upsilon Type*, *Scandinavian Journal of Statistics* (2007), https://doi.org/10.1111/j.1467-9469.2006.00527.x . General marginal-versus-joint class-L counterexamples.
5. N. Ratanov, *First-passage probabilities and invariant distributions of Kac-Ornstein-Uhlenbeck processes*, arXiv:2102.13308 (2021), https://arxiv.org/abs/2102.13308 . Related two-state modulation and stationary laws.
6. D. Frydel, *Semi-Markovian switching in a fluctuating harmonic trap: An age-structured formulation*, arXiv:2607.05173v1 (2026), https://arxiv.org/abs/2607.05173 . Later extension to nonexponential waiting times, not an input to this proof.
7. K.-I. Sato, *Subordination and self-decomposability*, *Statistics & Probability Letters* **54** (2001), 317–324, https://doi.org/10.1016/S0167-7152(01)00110-9 . Classical sufficient subordination inheritance.
