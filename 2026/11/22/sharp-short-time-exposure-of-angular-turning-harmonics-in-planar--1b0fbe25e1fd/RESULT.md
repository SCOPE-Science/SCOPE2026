# Sharp short-time exposure of angular turning harmonics in planar active motion

## Finding

**Theorem (first unmatched angular harmonic; finite-time quantitative bound).** Consider an isotropically initialized planar run-and-tumble particle with fixed propulsion speed \(v>0\), Poisson turning rate \(\alpha>0\), and optional independent translational diffusivity \(D\geq0\). A turn adds an independent angle of an arbitrary **reflection-symmetric Borel probability law** \(\mu\) on the circle. Let \(M_{2m}^{\mu}(t)=\mathbb E_{\mu}|X_t|^{2m}\) be its radial displacement moment and \(c_j(\mu)=\int\cos(j\psi)\,\mu(d\psi)\).

For every integer \(n\geq1\), suppose two such laws \(\mu,\nu\) have \(c_j(\mu)=c_j(\nu)\) for \(1\leq j<n\). Then for **every** \(t\geq0\) and \(m<n\),
\[
M_{2m}^{\mu}(t)=M_{2m}^{\nu}(t),
\]
while the first possible difference has the **explicit universal coefficient**
\[
\boxed{\quad
M_{2n}^{\mu}(t)-M_{2n}^{\nu}(t)
=2\alpha v^{2n}\frac{(n!)^2}{(2n+1)!}\bigl(c_n(\mu)-c_n(\nu)\bigr)t^{2n+1}+R_n(t),\quad}
\]
with the *law-independent, globally valid* error guarantee
\[
\boxed{\quad |R_n(t)|\leq3\alpha^2v^{2n}t^{2n+2}\quad(t\geq0).\quad}
\]
Both the exact difference of moments and these bounds are independent of \(D\). In particular, if \(\delta=|c_n(\mu)-c_n(\nu)|>0\), the moment difference is nonzero and has the sign of \(c_n(\mu)-c_n(\nu)\) whenever
\[
0<\alpha t<\frac{2(n!)^2}{3(2n+1)!}\,\delta.
\]

**Sharp exposure and minimal moment order.** For each \(n\geq1\), the coefficient \(|c_n(\mu)-c_n(\nu)|\) is at most \(2\), and this upper bound is attained by the two reflection-symmetric, uniform, \(n\)-point turning laws
\[
\mu_n=\frac1n\sum_{k=0}^{n-1}\delta_{2\pi k/n},\qquad
\nu_n=\frac1n\sum_{k=0}^{n-1}\delta_{(2k+1)\pi/n}.
\]
They agree at every lower positive Fourier harmonic, so all radial moments of orders below \(2n\) are *identical for all time*, but
\[
\boxed{\quad
\lim_{t\downarrow0}\frac{M_{2n}^{\mu_n}(t)-M_{2n}^{\nu_n}(t)}{\alpha v^{2n}t^{2n+1}}
=\frac{4(n!)^2}{(2n+1)!}.\quad}
\]
This is the largest absolute first-exposure coefficient among any two symmetric turning laws matching their lower harmonics. Its large-order decay is explicit,\[\frac{4(n!)^2}{(2n+1)!}\sim\frac{2\sqrt{\pi}}{4^n\sqrt n}\qquad(n\to\infty),\]making the high-harmonic signal intrinsically small even before observational noise is considered. The full collection of radial moment curves therefore distinguishes all reflection-symmetric Borel turning laws, whereas a single moment of order \(2m\) cannot in general detect modes above \(m\).

## Assumptions and scope

Let \(N_t\) be a rate-\(\alpha\) Poisson process, \(\Psi_1,\Psi_2,\ldots\) independent draws from \(\mu\), and \(\Theta_0\) independent and uniform on \([0,2\pi)\). Set
\[
\Theta_t=\Theta_0+\sum_{j=1}^{N_t}\Psi_j\pmod{2\pi},\qquad
X_t=v\int_0^t(\cos\Theta_s,\sin\Theta_s)\,ds+\sqrt{2D}\,B_t,
\]
where \(B_t\) is standard two-dimensional Brownian motion independent of all other randomness, and \(X_0=0\). All angles are increments of the preceding heading; absolute-angle redraws and finite-duration tumbles are different models. An atomic law, including a null turn, is allowed. Reflection symmetry means \(\mu(E)=\mu(-E)\); therefore its Fourier coefficients \(\widehat\mu_j=\int e^{ij\psi}\mu(d\psi)\) are the real numbers \(c_j(\mu)\).

The physical parameters \(v,\alpha,D\) are held equal between the two compared laws. No ergodicity or positive angular density is required. The sharp contrast is for *two laws with matched lower Fourier coefficients*, not for the general difference of two unrelated turning distributions. The sign guarantee applies to ideal exact expectations, not finite noisy samples.

## Proof

**1. Exact lower-harmonic dependence at all times.** Work first without the Gaussian part and identify the plane with \(\mathbb C\). Given \(N_t=k\), the \(k\) turn instants are uniformly ordered in \([0,t]\); the normalized durations \((S_0,\ldots,S_k)\) between consecutive turns have the Dirichlet \((1,\ldots,1)\) law. Up to an irrelevant common unit rotation, the active displacement is
\[
A_t=vt\sum_{j=0}^k S_j\exp\!\left(i\sum_{h=1}^{j}\Psi_h\right).
\]
For any integer \(m\geq0\), expand \(|A_t|^{2m}=(A_t)^m(\overline A_t)^m\). The resulting monomials have nonnegative multiplicities \(a_j,b_j\) with \(\sum a_j=\sum b_j=m\). Their angular expectation is a product of terms
\[
\prod_{h=1}^k\widehat\mu_{\ell_h},\qquad
\ell_h=\sum_{j=h}^k(a_j-b_j),\qquad |\ell_h|\leq m.
\]
Consequently \(\mathbb E|A_t|^{2m}\) depends on \(\mu\) only through Fourier modes of index at most \(m\) in absolute value, for any number of turns and any \(t\geq0\). This is independent of any formal power-series truncation or ergodicity assertion.

For independent isotropic planar Brownian displacement \(G_t=\sqrt{2D}\,B_t\), Gaussian contraction gives the exact finite identity
\[
\mathbb E\bigl[|A_t+G_t|^{2m}\mid A_t\bigr]
=\sum_{j=0}^{m}\binom{m}{j}^2j!(4Dt)^j|A_t|^{2(m-j)}.
\]
Thus each full radial moment has the same lower-harmonic dependence. In particular all \(m<n\) moments agree for the two stated laws at all times.

**2. The higher-harmonic difference is thermal-noise-free.** In the Gaussian formula for order \(2n\), each term with \(j\geq1\) contains an active radial moment of order at most \(2n-2\), which is exactly equal between \(\mu\) and \(\nu\). Therefore
\[
M_{2n}^{\mu}(t)-M_{2n}^{\nu}(t)
=\mathbb E_{\mu}|A_t|^{2n}-\mathbb E_{\nu}|A_t|^{2n},
\]
for **every** value \(D\geq0\), not merely asymptotically.

**3. Exactly one turn exposes the first unmatched mode.** Put \(\lambda=\alpha t\). On \(N_t=0\), the active displacement has magnitude \(vt\), independently of the turning law. On \(N_t=1\), the turn time divided by \(t\) is uniform on \([0,1]\), and
\[
\frac{|A_t|^{2n}}{(vt)^{2n}}=
\left|(1-u)+u e^{i\psi}\right|^{2n}
=\bigl((1-u)+ue^{i\psi}\bigr)^n
 \bigl((1-u)+ue^{-i\psi}\bigr)^n.
\]
The terms containing the highest harmonics \(e^{\pm in\psi}\) have coefficient exactly \([u(1-u)]^n\), and every remaining nonconstant Fourier mode has absolute index below \(n\). Using the matching lower modes and reflection symmetry, the conditional difference of the normalized moments is
\[
2\bigl(c_n(\mu)-c_n(\nu)\bigr)
\int_0^1[u(1-u)]^n\,du
=2\frac{(n!)^2}{(2n+1)!}\bigl(c_n(\mu)-c_n(\nu)\bigr).
\]
Multiplication by \(\Pr(N_t=1)=\lambda e^{-\lambda}\) supplies the claimed leading term.

**4. An explicit uniform remainder.** Since the active path has length at most \(vt\), its normalized even radial moment lies in \([0,1]\), so the difference of the two conditional expectations is bounded by \(2\). Replacing \(\lambda e^{-\lambda}\) by \(\lambda\) changes the one-turn contribution by at most \(2(vt)^{2n}\lambda(1-e^{-\lambda})\). All events with at least two turns contribute in absolute value at most \(2(vt)^{2n}\Pr(N_t\geq2)\). Use
\[
\lambda(1-e^{-\lambda})\leq\lambda^2,
\qquad\Pr(N_t\geq2)=1-e^{-\lambda}(1+\lambda)\leq\frac{\lambda^2}{2}.
\]
The sum is bounded by \(3(vt)^{2n}\lambda^2\), proving the uniform error assertion at every \(t\geq0\). The strict sign window follows by comparison with the nonzero leading term.

**5. Sharp constant and minimality.** Always \(|c_n(\mu)|\leq1\), hence \(|c_n(\mu)-c_n(\nu)|\leq2\). The stated root and rotated-root laws have \(c_j=0\) for \(1\leq j<n\) and respectively \(c_n=1\) and \(c_n=-1\); both are reflection symmetric. They attain the maximal coefficient, while Step 1 proves that no lower radial moment can distinguish them at any time. Finally, two distinct symmetric Borel measures differ in some cosine Fourier coefficient by uniqueness of Fourier coefficients (density of trigonometric polynomials in continuous functions); taking its first differing index and using the nonzero limit distinguishes them by one finite-order radial moment curve.

## Verification

The independent standard-library program `checker.py` computes exact Dirichlet-multinomial expansions for paths with prescribed small numbers of turns, under uniform circular turning and uniform discrete root turning. It verifies the universal Beta coefficient through order \(14\), exact lower-moment agreement for finite turn counts, and finite-rate truncated Poisson controls. Execute `python3 checker.py` from the package root; the observed output is `PASS: 128 deterministic exact and finite-rate checks`. The general continuum and arbitrary-measure statements are proved above, not inferred from the finite checks. The program does not simulate translational Brownian noise; the exact Gaussian polynomial identity handles it for all \(D\geq0\).

## Relationship to prior work

Britton, Zhang, Han and Bertrand (arXiv:2608.23519v1, publicly submitted 24 August 2026), Sections 3.5 and 5, established the angular Fourier hierarchy for preferred reorientation in the same free-space model: order-\(2n\) moments can involve modes through \(n\). They supply the underlying framework and leading ballistic moments, not the arbitrary-order **first-sensitive time coefficient**, a global **uniform finite-time remainder**, or a sharp extremal separation pair for each \(n\). Their generic mode-ceiling statement is not claimed as new. Sevilla (arXiv:1905.07090) previously provided full exact second- and fourth-order moment transforms, from which isolated small-order coefficients can in principle be extracted; Olsen and Löwen (arXiv:2405.14326) derived angular correlations and low-order diffusion laws. Jung (arXiv:2308.00554) also reports the general finite-harmonic dependence of displacement moments. None is credited to the present result as a new Fourier-mode hierarchy.

The contribution assessed here is restricted to the **all-order exact first-exposure coefficient**, the **law-uniform finite-time error bound independent of Gaussian thermal diffusion**, and the **sharp maximum contrast and matching-moment witness**. The existence of a stronger general moment-transform representation does not by itself give the numerical coefficient and uniform quantitative guarantee without the present one-turn and bounded-multiple-turn argument. Similar all-order short-time coefficient statements in older active-matter literature remain possible, and independent publication-priority verification has not been performed.

## Limitations

The theorem requires a constant speed, independent Poisson instantaneous turning, independent angular increments, and a spatially isotropic initial heading. The new injectivity corollary is confined to **reflection-symmetric** turning laws; radial observations cannot generally recover the handedness of an asymmetric turning law. This theorem does not address finite-duration turns, rotation diffusion, measurement noise, numerical conditioning, or statistically optimal sampling. The coefficient \((n!)^2/(2n+1)!\) shrinks rapidly with harmonic order, so exact identifiability does not imply practical high-harmonic recoverability. The all-time lower-mode dependence is already known and included solely to state the sharp obstruction accurately.

## References

1. C. Britton, Z. Zhang, S. Han, T. Bertrand, *Run-and-tumble particles with preferred reorientation*, arXiv:2608.23519v1, first public 2026-08-24, https://arxiv.org/abs/2608.23519 . Primary full text, Section 3.5 and discussion.
2. F. J. Sevilla, *Two-dimensional active motion*, arXiv:1905.07090, first public 2019-05-17, https://arxiv.org/abs/1905.07090 . Exact fourth-moment transform, Eq. (48).
3. K. S. Olsen, H. Löwen, *Optimal diffusion of chiral active particles with strategic reorientations*, arXiv:2405.14326, https://arxiv.org/abs/2405.14326 ; Phys. Rev. E 110, 064606 (2024).
4. Y. Jung, *Hyperdiffusion of Poissonian run-and-tumble particles in two dimensions*, arXiv:2308.00554, first public 2023-08-01, https://arxiv.org/abs/2308.00554 . Abstract reports finite-harmonic dependence.
