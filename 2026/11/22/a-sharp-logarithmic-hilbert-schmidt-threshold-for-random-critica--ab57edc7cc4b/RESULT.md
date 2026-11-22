# A sharp logarithmic Hilbert–Schmidt threshold for random critical Dirichlet Gram matrices

## Finding
Let \(\mathcal H\) be the analytic reproducing-kernel Hilbert space on the unit disk \(\mathbb D\) with norm
\[
\left\|\sum_{n\ge0} a_nz^n\right\|_{\mathcal H}^2=\sum_{n\ge0}\sqrt{n+1}\,|a_n|^2,
\qquad K(z,w)=\sum_{n\ge0}\frac{(z\overline w)^n}{\sqrt{n+1}}.
\]
For \(b\in\mathbb R\), let \(\Lambda_b\) be a Poisson process of intensity
\[
d\mu_b(z)=\frac{dA(z)/\pi}{(1-|z|^2)^{3/2}\,[\log(e/(1-|z|^2))]^b}.
\]
For its distinct points \(z_i\), let \(G_b\) denote the normalized-kernel Gram matrix, with entries
\[
(G_b)_{ij}=\frac{K(z_i,z_j)}{\sqrt{K(z_i,z_i)K(z_j,z_j)}},
\qquad T_b=\sum_{i\ne j}|(G_b)_{ij}|^2.
\]
Then the exact expected off-diagonal Hilbert–Schmidt threshold and its sharp critical coefficient are
\[
\boxed{\ \mathbb ET_b<\infty\ \Longleftrightarrow\ b>\tfrac32,\qquad
\lim_{b\downarrow3/2}(b-\tfrac32)\mathbb ET_b=\frac2\pi.\ }
\]
In particular, if \(b>3/2\), then almost surely \(G_b-I\) is Hilbert–Schmidt and \(\Lambda_b\) is an interpolating sequence both for \(\mathcal H\) and for its multiplier algebra. Because \(\mathcal H\) has an equivalent norm to the weighted Dirichlet space \(\mathcal D_{1/2}\), it is also interpolating for that Dirichlet space.

## Assumptions and scope
The intensity is exactly the specified radial density with respect to normalized disk area; logarithms are natural. The process is simple and locally finite almost surely, and its total intensity is infinite, so its points can be enumerated countably without repetition. The Gram entries use the full kernel norm, not a truncated kernel. \(T_b\) is an extended nonnegative random variable, and \(\mathbb E T_b\) is an extended expectation. The assertion of interpolation is a sufficient almost-sure result in the range \(b>3/2\); no noninterpolation assertion is made for the complementary values of \(b\).

## Proof
**1. Exact second moment.** By the factorial moment identity for a diffuse Poisson process, Tonelli's theorem gives the equality of extended nonnegative integrals
\[
\mathbb ET_b=\iint_{\mathbb D^2}
\frac{|K(z,w)|^2}{K(z,z)K(w,w)}\,d\mu_b(z)d\mu_b(w).
\tag{1}
\]
There is no diagonal contribution because the intensity is nonatomic. Writing \(t=1-|z|^2\), \(s=1-|w|^2\), and \(\ell(t)=\log(e/t)\), normalized polar area gives \(dA(z)/\pi=dt\,d\theta/(2\pi)\). Hence (1) is an ordinary positive double integral over \(0<t,s<1\), with an angular average over \(\theta=\arg z-\arg w\).

**2. Kernel boundary profile and its angular average.** Put \(F(q)=\sum_{n\ge0}q^n/\sqrt{n+1}\). The standard polylogarithm expansion near \(q=1\), uniform from within the unit disk, yields
\[
F(q)=\sqrt\pi\,(1-q)^{-1/2}+O(1),\qquad
F(1-t)=\sqrt\pi\,t^{-1/2}(1+O(\sqrt t)).
\tag{2}
\]
For \(a\uparrow1\), elementary comparison near \(\theta=0\) gives
\[
\frac1{2\pi}\int_{-\pi}^{\pi}|1-ae^{i\theta}|^{-1}\,d\theta
=\frac1\pi\log\frac1{1-a}+O(1).
\tag{3}
\]
The term \(O(|1-q|^{-1/2})\) in \(|F(q)|^2=\pi|1-q|^{-1}+O(|1-q|^{-1/2})+O(1)\) has a uniformly bounded angular average, since \(|\theta|^{-1/2}\) is integrable. Thus (2) and (3), with \(a=\sqrt{(1-t)(1-s)}\), show that in a fixed sufficiently small boundary square \(0<t,s<t_0\), the angle-averaged normalized squared correlation equals
\[
\frac{\sqrt{ts}}\pi\log\frac1{t+s}
+O(\sqrt{ts})
+O\!\left(\sqrt{ts}(\sqrt t+\sqrt s)\log\frac1{t+s}\right).
\tag{4}
\]
Here changing \(1-a\) to \(t+s\) contributes only \(O(1)\) inside the logarithm. The bound (4) is uniform as \(t,s\downarrow0\).

**3. Exact integrability threshold.** Multiply (4) by the two intensity factors \(t^{-3/2}s^{-3/2}\ell(t)^{-b}\ell(s)^{-b}\,dt\,ds\). With \(u=\log(1/t)\), \(v=\log(1/s)\), the leading integral becomes
\[
\frac1\pi\int_U^\infty\!\int_U^\infty
\frac{\min(u,v)}{(1+u)^b(1+v)^b}\,du\,dv,
\tag{5}
\]
up to an additive remainder finite uniformly for \(b\) in every compact subinterval of \((1,\infty)\) containing \(3/2\). Indeed \(\log(1/(e^{-u}+e^{-v}))=\min(u,v)+O(1)\), and the other error terms in (4) carry either a bounded angle integral or an exponentially decaying factor in \(u\) or \(v\). Regions with either \(t\ge t_0\) or \(s\ge t_0\) contribute finitely for \(b>1\), by boundedness of the kernel against the compact variable.

The difference between the integrand in (5) and \(\min(u,v)u^{-b}v^{-b}\) also has a bounded integral uniformly for \(b\) near \(3/2\), since \((1+u)^{-b}=u^{-b}(1+O(u^{-1}))\). For \(b>3/2\), splitting into \(v\ge u\) and \(u\ge v\) gives the exact model integral
\[
J_b(U)=\int_U^\infty\!\int_U^\infty
\min(u,v)u^{-b}v^{-b}\,du\,dv
=\frac{2U^{3-2b}}{(b-1)(2b-3)}.
\tag{6}
\]
For \(b\le3/2\), restricting both logarithmic variables to successive comparable dyadic blocks yields divergent lower sums, proving divergence of (1), including \(b\le1\). For \(b>3/2\), (4)–(6) prove finiteness of (1). Finally, \((b-3/2)J_b(U)\to2\) as \(b\downarrow3/2\), and the uniformly bounded remainder in (5) disappears upon multiplication by \(b-3/2\). This proves both asserted exact formulas, including the coefficient \(2/\pi\).

**4. Almost-sure interpolation.** If \(b>3/2\), finite expectation implies \(T_b<\infty\) almost surely. Therefore \(G_b=I+H_b\) with \(H_b\) Hilbert–Schmidt, hence \(G_b\) is bounded and the normalized kernels form a Bessel family (the corresponding discrete normalized evaluation measure is Carleson). Moreover, finiteness of \(T_b\) implies only finitely many distinct pairs can have squared normalized correlation at least \(1/2\). Since all the finitely many exceptional pairs are distinct, and \(|(G_b)_{ij}|<1\) for \(i\ne j\), the complete sequence is separated in the reproducing-kernel metric.

The coefficients \((n+1)^{-1/2}\) are positive and log-convex with constant term \(1\). The Kaluza criterion therefore makes \(K\) a normalized irreducible complete Pick kernel. The separated-plus-Carleson characterization of Aleman, Hartz, McCarthy and Richter applies: the sequence is multiplier interpolating, and also Hilbert-space interpolating. Finally \(\sqrt{n+1}\) is equivalent to the usual coefficient weight of \(\mathcal D_{1/2}\), so Hilbert-space interpolation is invariant under this norm equivalence. This completes the proof.

## Verification
The accompanying `check.py` runs 24 finite arithmetic checks of the polylogarithmic boundary coefficient, elliptic-integral angular coefficient, exact model double integral, critical simple-pole constant, and kernel coefficient monotonicity. Execute `python check.py` with Python 3 and `mpmath`. The infinite-dimensional conclusions are proved by (1)–(6) and the cited complete Pick interpolation theorem; numerical checks do not certify those arguments.

## Relationship to prior work
Hartmann and Massaneda (arXiv:2207.10319, first posted 2022-07-21) develop the underlying inhomogeneous disk Poisson model and study separation and interpolation. Their Theorem 4.5 treats weighted Dirichlet exponents on either side of \(1/2\), and their discussion expressly asks about the borderline exponent. The present result supplies a sharp *expected Gram Hilbert–Schmidt* threshold and an almost-sure interpolation sufficient range at that borderline, without claiming a complete characterization of interpolation. Aleman–Hartz–McCarthy–Richter (arXiv:1701.04885) provide the general complete Pick interpolation criterion used in the last step; it does not supply the Poisson second-moment calculation. Chalmoukis–Dayan–Hartz (arXiv:2306.13602) distinguish simple from multiplier interpolation for complete Pick spaces; the stronger multiplier claim here is supported by Carleson plus separation.

## Limitations
An infinite expectation for \(b\le3/2\) does **not** imply \(T_b=\infty\) almost surely, and it does not imply noninterpolation. The theorem supplies no full phase diagram for almost-sure interpolation in the remaining logarithmic regimes, and it does not address other radial exponents, general intensity measures, or almost-sure asymptotics of the divergent cutoff sum. The novelty comparison is literature-based, not an independent historical-priority certification.

## References
1. A. Hartmann and X. Massaneda, *Inhomogeneous Poisson processes in the disk and interpolation*, arXiv:2207.10319 (2022 preprint; 2024 published article), https://arxiv.org/abs/2207.10319.
2. A. Aleman, M. Hartz, J. E. McCarthy and S. Richter, *Interpolating sequences in spaces with the complete Pick property*, arXiv:1701.04885 (2017 preprint), https://arxiv.org/abs/1701.04885.
3. N. Chalmoukis, A. Dayan and M. Hartz, *Simply interpolating sequences in complete Pick spaces*, arXiv:2306.13602 (2023 preprint), https://arxiv.org/abs/2306.13602.
