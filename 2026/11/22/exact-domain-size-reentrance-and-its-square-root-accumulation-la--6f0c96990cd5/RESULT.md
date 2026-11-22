# Exact domain-size reentrance and its square-root accumulation law for Gaussian nonlocal vegetation

## Finding
Consider the periodized Gaussian version of the Allee–competition vegetation equation defined below. If the upper uniform positive equilibrium is stable against spatially constant perturbations, then its complete **linear spatial stability** as a function of habitat circumference has a sharp phase diagram. Define \(q=A/C\in(0,1)\), \(t_q=-q/W_{-1}(-q/e)\), and \(D_c=\sigma Ct_q\). For \(D>D_c\), the uniform state is linearly asymptotically stable for every circumference; at \(D=D_c\), it is stable except for possible neutral resonances. For \(0<D<D_c\), define \(0<k_-<k_+\) by
\[
k_\pm^2=\frac AD+\frac1\sigma W_{\{-1,0\}}\!\left(-\frac{\sigma C}{D}e^{-\sigma A/D}\right),
\]
where the lower endpoint uses branch \(W_{-1}\), and the upper endpoint uses \(W_0\). For every \(L>0\), a spatially nonconstant exponentially growing linear mode exists **if and only if**
\[
L\in \bigcup_{j=1}^{\infty}\left(\frac{2\pi j}{k_+},\frac{2\pi j}{k_-}\right).
\]
The number of bounded *strictly stable open gaps after the first instability*, before instability becomes permanent as \(L\) increases, is exactly
\[
N(D)=\max\left\{0,\left\lceil\frac{k_-}{k_+-k_-}\right\rceil-1\right\}.
\]
If \(z_c=\sigma^{-1}\log(\sigma C/D_c)>0\), then as \(D\uparrow D_c\),
\[
N(D)=\sqrt{\frac{\sigma D_cz_c}{2(D_c-D)}}+O(1).
\]
In particular, the number of alternating instability and restabilization windows is unbounded near the Gaussian Turing threshold. Neutral boundary lengths are **not** classified as strictly stable.

An exact biologically admissible example has \(u_0=1/2\), \(r=2039/458752\), \(\alpha=r/[2(1-r)]\), \(\beta=(1-r)/2\), \(\sigma=\log2\), and \(D=127(1-r)/(2\cdot458752)\). Its unstable wavenumber interval is **exactly** \((3,4)\), and its two bounded strictly stable return windows are \((2\pi/3,\pi)\) and \((4\pi/3,3\pi/2)\).

## Assumptions and scope
On the one-dimensional circle \(\mathbb T_L=\mathbb R/(L\mathbb Z)\) with \(L>0\), consider the scalar nonlocal equation
\[
\partial_t u=D\partial_{xx}u+u\left[\frac{u(1-G_{\sigma,L}*u)}{u+\alpha}-\beta\right],\quad D,\sigma,\alpha,\beta>0,
\]
with standard periodic convolution and the normalized periodized Gaussian
\[
G_{\sigma,L}(x)=\sum_{m\in\mathbb Z}\frac{e^{-(x+mL)^2/(4\sigma)}}{\sqrt{4\pi\sigma}}.
\]
Let \(u_0=u_+>0\) be the *upper* positive uniform equilibrium, a root of \(u_0(1-u_0)=\beta(u_0+\alpha)\), satisfying the strict homogeneous stability inequality \(u_0^2>\alpha\beta\). The useful positive coefficients are \(A=\alpha\beta/(u_0+\alpha)\), \(C=u_0^2/(u_0+\alpha)\), so \(0<A<C\). All statements concern the spectrum of the linearization at this positive equilibrium; they do not assert nonlinear convergence, stable finite-amplitude spatial patterns, or field validation.

Linear asymptotic stability means all Fourier growth rates have strictly negative real parts. Because the diffusion term dominates at high frequency and the spectrum is real, the classification by Fourier eigenvalues is exhaustive; the same formulas apply to periodic Sobolev or continuous-function linearizations.

## Proof
**1. Fourier linearization.** Write \(u=u_0+v\). Using the equilibrium equation, differentiation of the local argument and the convolution argument gives
\[
\partial_t v=D\partial_{xx}v+Av-CG_{\sigma,L}*v.
\]
The Fourier basis \(e^{2\pi ijx/L}\), \(j\in\mathbb Z\), diagonalizes both operators. By periodizing the Gaussian, its Fourier multiplier is exactly \(e^{-\sigma(2\pi j/L)^2}\), so
\[
\lambda_j(L)=A-Ce^{-\sigma(2\pi j/L)^2}-D(2\pi j/L)^2.
\]
The uniform eigenvalue is \(\lambda_0=A-C<0\).

**2. Gaussian band and exact diffusion onset.** Put \(z=k^2\ge0\) and \(f_D(z)=A-Ce^{-\sigma z}-Dz\). We have \(f_D(0)=A-C<0\), \(f_D(z)\to-\infty\) as \(z\to\infty\), and \(f_D''(z)=-\sigma^2Ce^{-\sigma z}<0\). When \(D\ge\sigma C\), the function decreases from a negative starting value. For \(D<\sigma C\), its sole maximum occurs at \(z_*(D)=\sigma^{-1}\log(\sigma C/D)\) with value
\[
M(D)=A-\frac{D}{\sigma}\left[1+\log\left(\frac{\sigma C}{D}\right)\right].
\]
Writing \(t=D/(\sigma C)\) shows \(M(D)/C=q-t(1-\log t)\). The function \(t\mapsto t(1-\log t)\) strictly increases from zero to one on \((0,1)\), hence has the unique solution \(t_q\in(0,1)\) for \(q\in(0,1)\). Solving with \(W_{-1}\) yields the displayed \(t_q\). Thus exactly for \(0<D<D_c\) the maximum is positive and, by strict concavity and negative endpoint values, \(f_D\) has precisely two positive zeros \(z_-<z_+\). Solving \(A-Dz=Ce^{-\sigma z}\) with Lambert W gives their stated branches, with \(k_\pm=\sqrt{z_\pm}\), and \(f_D(k^2)>0\) exactly when \(k_-<|k|<k_+\). At \(D=D_c\), the maximum merely touches zero.

**3. Exact domain-size census.** A nonzero integer Fourier mode is growing precisely when \(k_-<2\pi j/L<k_+\), namely \(L\in I_j=(2\pi j/k_+,2\pi j/k_-)\). The starts and ends increase strictly with \(j\). Consecutive intervals have a nonempty positive-length gap exactly when
\[
\frac{2\pi j}{k_-}<\frac{2\pi(j+1)}{k_+}\quad\Longleftrightarrow\quad j<\frac{k_-}{k_+-k_-}.
\]
These are exactly the bounded strict-stability return gaps; if adjacent intervals touch, the contact length is marginal rather than strictly stable. Once intervals overlap or touch, all subsequent ones do too, because the above inequality fails for all larger indices. Counting positive integers \(j\) strictly below the ratio gives \(\max\{0,\lceil k_-/(k_+-k_-)\rceil-1\}\). No higher Fourier mode is omitted: the intervals enumerate all nonzero integers, and their union is exactly the growth set.

**4. Critical accumulation.** Let \(\varepsilon=D_c-D\downarrow0\) and \(z_c=\sigma^{-1}\log(\sigma C/D_c)\). At the double zero \((z_c,D_c)\), \(f=0\), \(f_z=0\), \(f_{zz}=-\sigma D_c\), and \(f_D=-z_c\). Taylor expansion and the strict nondegenerate maximum give
\[
z_\pm=z_c\pm\sqrt{\frac{2z_c\varepsilon}{\sigma D_c}}+O(\varepsilon),\quad
k_+-k_-=\sqrt{\frac{2\varepsilon}{\sigma D_c}}+O(\varepsilon).
\]
As \(k_-\to\sqrt{z_c}\), their ratio is \(\sqrt{\sigma D_c z_c/(2\varepsilon)}+O(1)\). Taking the integer ceiling changes the value by at most a bounded amount, completing the asymptotic.

**5. Exact three-parameter resonance example.** Put \(r=2039/458752\) and choose the biological parameters stated in the finding. The positive roots of \(u(1-u)=\beta(u+\alpha)\) are \(r/2\) and \(1/2\), with the upper root \(u_0=1/2\). Direct substitution gives \(A/C=r\), \(C=(1-r)/2\) and \(D/C=127/458752\). Consequently
\[
\frac{458752}{C}\lambda(k)=2039-458752\,2^{-k^2}-127k^2.
\]
At \(k^2=9\) and \(k^2=16\), the right-hand side is exactly zero: \(2039-896-1143=0\) and \(2039-7-2032=0\). At \(k^2=10\), it equals \(321>0\). Since the expression is strictly concave in \(k^2\), these are its **only** roots and the open unstable band is exactly \((3,4)\). The ratio of bandwidth endpoints is \(3/(4-3)=3\), giving two nonempty intervening stable gaps; the adjacent pair for indices 3 and 4 only touch at \(L=2\pi\) and does not produce another strictly stable window.

## Verification
The attached standalone standard-library script `verify.py` checks the two exact rational root identities, strictly positive test mode, biological parameter identities, illustrative finite circumferences, independent numerical solutions for five normalized Gaussian parameter cases and four subcritical offsets each, the consecutive-interval count, and the critical asymptotic. Run with `python verify.py` (Python 3; no third-party requirements). Its result is a supplementary check, **not** a substitute for Steps 1–5, which prove the infinite assertions.

## Relationship to prior work
Dimatz and Kuperman (2026, arXiv:2611.08215, sections II–III and Appendix A) derive the local Allee and nonlocal Gaussian dispersion relationship and the continuous-space Turing threshold. Their analysis emphasizes two-dimensional pattern morphology and biomass changes, not a complete one-dimensional circumference-by-circumference spectral census. The present theorem uses their Gaussian linearization but additionally resolves the integer Fourier-mode resonance problem, sharp number of stable return intervals, and critical square-root accumulation with an exact admissible numerical-free example.

Van der Voort, Martínez-García and Doelman (2025 preprint, arXiv:2512.09488, section 3 and Appendix A) give broad nonlocal-competition Turing criteria for vegetation models and examples with other competition kernels. General discrete-mode selection on bounded habitats is established spectral practice; the new claim **does not claim to discover that principle**. It is the model-specific **global count over all circumference values** and critical scaling not implied by an infinite-domain band criterion alone. Clerc, Escaff and Kenkre (2010) analyze Allee competition fronts and patterns with other kernels; no encompassing result for the displayed Gaussian ring-length count was identified in the material inspected. A definitive historical novelty determination remains subject to independent source review.

## Limitations
The result is a one-dimensional, periodized-Gaussian, positive homogeneous-equilibrium linear theorem. In the unstable windows it proves positive linear growth for some mode, not nonlinear pattern persistence; in strictly stable windows it gives local linear decay, not globally asymptotic ecological recovery. The model's extinction state may coexist with the positive equilibrium. Width and curvature are held fixed while circumference varies by periodizing the same Gaussian. A general bounded-domain Fourier-mode principle underlies the proof, and relevant uncatalogued theorems could already express the exact count or critical accumulation; no claim of independently certified novelty is made.

## References
1. F. Dimatz and M. N. Kuperman, *Pattern selection and biomass shifts in a vegetation model with nonlocal competition and Allee activation*, arXiv:2611.08215v1 (public November 5, 2026), https://arxiv.org/abs/2611.08215 , full text https://arxiv.org/html/2611.08215 .
2. J. van der Voort, R. Martínez-García and A. Doelman, *Vegetation pattern formation induced by local growth outpacing susceptibility to non-local competition*, arXiv:2512.09488v1 (December 10, 2025), https://arxiv.org/abs/2512.09488 .
3. M. G. Clerc, D. Escaff and V. M. Kenkre, *Analytical studies of fronts, colonies, and patterns: combination of the Allee effect and nonlocal competition interactions*, Phys. Rev. E 82, 036210 (2010), https://doi.org/10.1103/PhysRevE.82.036210 .
