# Anisotropic semicircle containment and the Gaussian–von Mises crossover for random enclosing disks

## Finding

Independently sample \(n\ge3\) points \(X_j=(\cos\Phi_j,\sin\Phi_j)\) on the unit Euclidean circle using the strictly positive angular density
\[
f_\eta(\theta)=\frac{1+\eta\cos\theta}{2\pi},\qquad 0\le\eta<1.
\]
Let \(B_n\) be the smallest closed Euclidean disk containing all sampled points, with center \(C_n\) and radius \(R_n\). Write \(E_n=\{R_n<1\}\). Almost surely on \(E_n\), the sample has a unique shortest occupied counterclockwise arc of length less than \(\pi\); let \(\Theta_n\) be its first point's angle and \(S_n\) the unused portion of its containing semicircle, so that the occupied arc has length \(\pi-S_n\). Define \(b=2\eta/\pi\) and \(p_*=(1+b)/2\).

**Exact probability.** For all \(n\ge3\) and \(0\le\eta<1\),
\[
\boxed{\Pr(E_n)=\frac{n}{2^{n-1}}\sum_{k=0}^{\lfloor(n-1)/2\rfloor}
\binom{n-1}{2k}\frac{\binom{2k}{k}}{4^k}\,b^{2k}.}
\]
This finite polynomial is an exact normalization, not a claim of novelty for the classical symmetric case or the previously known three-point extremality.

**Fixed anisotropy.** For any fixed \(0<\eta<1\), as \(n\to\infty\),
\[
\boxed{\Pr(E_n)\sim \sqrt{\frac{n(1+b)}{2\pi b}}\,p_*^{n-1}.}
\]
Writing \(\operatorname{wrap}(t)\in(-\pi,\pi]\) for the representative modulo \(2\pi\), the following **joint convergence in total variation** holds:
\[
\boxed{\left(\sqrt{\frac{nb}{1+b}}\,\operatorname{wrap}(\Theta_n+\pi/2),\quad
\frac{nS_n}{\pi+2\eta}\right)\ \Big|\ E_n
\ \xrightarrow{\mathrm{TV}}\ (Z,H),}
\]
where \(Z\sim N(0,1)\) and \(H\sim\operatorname{Exp}(1)\) are independent. In particular, with \(e_1=(1,0)\),
\[
 nC_n\mid E_n\ \Rightarrow\ \frac{\pi+2\eta}{2}H e_1,
 \qquad n^2(1-R_n)\mid E_n\ \Rightarrow\ \frac{(\pi+2\eta)^2}{8}H^2.
\]
The last two limits are weak, not total-variation, statements: the center limit is supported on a ray.

**Critical weak-anisotropy window.** Fix \(\lambda\ge0\), set \(\eta_n=\lambda/n\) for \(n>\lambda\), and define
\[
I_0(z)=\frac{1}{2\pi}\int_0^{2\pi}e^{z\cos u}\,du.
\]
Then
\[
\boxed{\frac{\Pr_{\eta_n}(E_n)}{n2^{1-n}}\longrightarrow
I_0(2\lambda/\pi).}
\]
Conditioned on \(E_n\), \((\Theta_n,nS_n/\pi)\) converges **in total variation** to independent \((\Theta_\lambda,H)\), where \(H\sim\operatorname{Exp}(1)\) and \(\Theta_\lambda\) has the shifted von Mises density
\[
\boxed{g_\lambda(\theta)=\frac{e^{-(2\lambda/\pi)\sin\theta}}{2\pi I_0(2\lambda/\pi)},\quad0\le\theta<2\pi.}
\]
Consequently,
\[
nC_n\mid E_n\Rightarrow\frac\pi2H(\cos(\Theta_\lambda+\pi/2),\sin(\Theta_\lambda+\pi/2)),\quad
n^2(1-R_n)\mid E_n\Rightarrow\frac{\pi^2}{8}H^2.
\]
Thus an anisotropy of order \(1/n\) is the exact orientation crossover: the conditional enclosing-disk center has an angularly distributed limit in this window, versus concentration toward the positive horizontal ray for every fixed positive \(\eta\).

## Assumptions and scope

All circle points have Euclidean radius exactly one and are sampled independently using the displayed density relative to angular Lebesgue measure. All probabilistic limits are along integers \(n\to\infty\). The fixed-anisotropy limit keeps \(\eta\in(0,1)\) constant; the critical-window limit keeps \(\lambda\ge0\) fixed as \(\eta_n=\lambda/n\). The unique circular gap longer than \(\pi\) and its complementary occupied arc exist almost surely on \(E_n\). No assertions are made for varying \(\eta_n\) outside those regimes or for other sampling densities. The symbol \(\Rightarrow\) indicates convergence in distribution, and \(\xrightarrow{\mathrm{TV}}\) convergence in total variation of the indicated absolutely continuous joint laws.

## Proof

**1. Geometric reduction and uniqueness of the anchor.** A finite subset of the unit circle has minimal enclosing radius strictly below one precisely when it lies in an open semicircle. Indeed, if it lies in an arc shorter than \(\pi\), the disk whose diameter connects the two extreme sample points contains every intermediate point by the inscribed-angle theorem, and its radius is less than one. Conversely, if it is not contained in a semicircle, its convex hull contains the origin, and any disk containing all points has radius at least one: for any center \(c\), \(\max_j|X_j-c|^2\ge1+|c|^2\) by a convex combination expressing the origin. On \(E_n\), exactly one circular gap exceeds \(\pi\), because two such gaps cannot coexist. Hence \(\Theta_n\) is the uniquely determined first sampled point of the complementary short arc. Its final point lies at \(\Theta_n+\pi-S_n\) modulo \(2\pi\).

The unique smallest enclosing disk has this endpoint chord as its diameter (the endpoints force a radius of at least half the chord length, and all other points are inside that diameter disk). Therefore, exactly,
\[
\boxed{R_n=\cos(S_n/2),\qquad
C_n=\sin(S_n/2)\bigl(\cos(\Theta_n+\pi/2-S_n/2),
\sin(\Theta_n+\pi/2-S_n/2)\bigr).}
\]

**2. Exact density and endpoint gap.** For a candidate anchor at \(\theta\), the mass of its forward semicircle is
\[
p_\eta(\theta)=\int_\theta^{\theta+\pi}f_\eta(u)\,du
=\frac12-\frac\eta\pi\sin\theta=\frac12(1-b\sin\theta).
\]
Uniqueness of the long gap makes the \(n\) possible anchor-label events disjoint. Thus
\[
\Pr(E_n)=n\int_0^{2\pi}f_\eta(\theta)p_\eta(\theta)^{n-1}\,d\theta,
\quad
\Pr(\Theta_n\in d\theta\mid E_n)=\frac{nf_\eta(\theta)p_\eta(\theta)^{n-1}}{\Pr(E_n)}\,d\theta.
\]
The term with \(\eta\cos\theta\) integrates to zero: it is a multiple of the integral of the derivative of \((1-b\sin\theta)^n\) around a full period (for \(\eta=0\) the term vanishes identically). Expanding \((1-b\sin\theta)^{n-1}\), all odd sine moments vanish and the even moments are \(\binom{2k}{k}/4^k\). This proves the exact displayed polynomial.

Conditionally on \(\Theta_n=\theta,E_n\), the other \(n-1\) angles are independent and have density \(f_\eta/p_\eta(\theta)\) restricted to the forward semicircle. Let
\[
q_\eta(\theta,s)=\int_{\theta+\pi-s}^{\theta+\pi}f_\eta(u)\,du
=\frac{s+\eta[-\sin\theta+\sin(\theta-s)]}{2\pi}.
\]
For \(0\le s\le\pi\), the exact conditional survival function is
\[
\boxed{\Pr(S_n>s\mid\Theta_n=\theta,E_n)=
\left(1-\frac{q_\eta(\theta,s)}{p_\eta(\theta)}\right)^{n-1}.}
\]
It is differentiable for \(0<s<\pi\), and its derivative yields the joint anchor–gap density used below.

**3. Fixed-anisotropy Laplace and Gaussian asymptotics.** If \(\eta>0\), \(p_\eta\) has a unique periodic maximum at \(\theta_0=-\pi/2\), equal to \(p_*=(1+b)/2\). Moreover,
\[
\log p_\eta(\theta_0+u)=\log p_*-\frac{b}{2(1+b)}u^2+O_\eta(u^4),
\qquad f_\eta(\theta_0)=\frac1{2\pi}.
\]
The standard one-dimensional Laplace method, with exponentially smaller contribution outside each fixed neighborhood of \(\theta_0\), gives the probability asymptotic, while the conditional anchor density under the stated square-root rescaling tends pointwise to the standard Gaussian density.

For a gap \(s\downarrow0\), uniformly in \(\theta\),
\[
q_\eta(\theta,s)=f_\eta(\theta+\pi)s+O_\eta(s^2).
\]
At \(\theta_0\), \(f_\eta(\theta_0+\pi)=1/(2\pi)\), so \(p_*/f_\eta(\theta_0+\pi)=\pi+2\eta\). Substituting \(s=(\pi+2\eta)t/n\) into the exact conditional survival function yields \(e^{-t}\), jointly with the concentrated anchor, and the conditional density of the scaled gap tends to \(e^{-t}\). The product of the Gaussian and exponential densities is the pointwise limit of the joint scaled density. These joint densities are normalized, and the limit density integrates to one; Scheffé's lemma upgrades convergence to \(L^1\), hence total variation. The exact disk-center formulas and Slutsky's theorem give the stated weak geometric limits.

**4. Critical-window Laplace replacement.** When \(\eta_n=\lambda/n\) and \(a=2\lambda/\pi\), uniformly in \(\theta\),
\[
f_{\eta_n}(\theta)\longrightarrow\frac1{2\pi},\qquad
(2p_{\eta_n}(\theta))^{n-1}
=\bigl(1-a\sin\theta/n\bigr)^{n-1}\longrightarrow e^{-a\sin\theta}.
\]
Dominated convergence gives the Bessel factor and the von Mises limit for the conditional anchor density. For fixed \(t\ge0\), uniformly in \(\theta\),
\[
\frac{q_{\eta_n}(\theta,\pi t/n)}{p_{\eta_n}(\theta)}=\frac{t}{n}+O_\lambda(n^{-2}),
\]
so the exact gap law yields an independent unit exponential limit. Differentiating the conditional gap survival function and applying dominated convergence gives pointwise convergence of the *joint* density to \(g_\lambda(\theta)e^{-t}\). Both densities integrate to one. Scheffé's lemma proves total-variation convergence. Applying the exact center and radius identities completes the result.

## Verification

The self-contained numerical diagnostic `check_anisotropic_mec.py` (NumPy and SciPy; install versions from `requirements.txt`) computes the finite polynomial independently of angular quadrature, compares fixed-parameter Laplace and critical-window Bessel normalizations, and uses 30,000 independently simulated conditional samples per marked-law configuration. Its successful observed terminal message was `ANISOTROPIC_MEC_WINDOW_CHECK_OK`. The tests included six polynomial/quadrature pairs, three fixed-parameter asymptotic comparisons, three critical-window comparisons, and fixed/weak/zero anisotropy conditional-mark diagnostics. These finite computations do not prove the infinite limits; the preceding analytical argument does.

## Relationship to prior work

Wendel's classical theorem determines the center-containment probability for antipodally symmetric distributions, including the uniform-circle value \(\Pr(E_n)=n/2^{n-1}\). Wagner and Welzl determine qualitative extremal containment bounds and their balanced equality cases. Prior three-point work gives an exact weighted semicircle integral and a quantitative antipodal-symmetry stability bound; the present finite-\(n\) anchor integral extends that known method and is **not** presented as an independently novel three-point inequality. Work on marked center-exclusion geometry for centrally symmetric ovals establishes a conditional exponential clearance limit under a symmetric density; it does not cover non-antipodal modulation, the minimum enclosing disk's *center*, or the \(1/n\) Gaussian–von Mises orientation crossover. Random circle-covering literature gives related spacing methods, but was not found to settle this conditional marked transition. The claimed increment is the fixed/weak-anisotropy crossover for the center and extremal-gap marks, including its explicit conditional densities and rates.

## Limitations

The model is the particular cosine-modulated positive circle density, not arbitrary anisotropic sampling. Neither the optimality of the numerical Laplace remainder nor uniform convergence across every sequence \(\eta_n\to0\) is asserted. The fixed-positive-\(\eta\) and fixed-\(\lambda\) windows do not by themselves establish a theorem for intermediate modulation rates. The exact probability integral and the baseline symmetric case have existing antecedents; the novelty is restricted to the specified transition and marked enclosing-disk geometry. The finite numerical checks are consistency tests, not independent mathematical certification. A non-indexed earlier treatment of the conditional orientation law or a general theorem subsuming it remains a historical-priority risk.

## References

1. J. G. Wendel, “A Problem in Geometric Probability,” *Mathematica Scandinavica* **11** (1962), 109–112, DOI: 10.7146/math.scand.a-10655, https://journals.msp.org/mscand/article/download/2688/2687/2719 (full text examined; first verified publication date 1962-06-01).
2. U. Wagner and E. Welzl, “A Continuous Analogue of the Upper Bound Theorem,” *Discrete & Computational Geometry* **26** (2001), 205–219, DOI: 10.1007/s00454-001-0028-9, https://people.inf.ethz.ch/emo/PublFiles/ContAnalog_DCG26_01.pdf (full author-hosted text examined).
3. “Optimal fourth-root symmetry stability for the three-point semicircle probability,” publicly indexed mathematical finding, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-optimal-fourth-root-symmetry-stability-for-the-three-point-semic--02dfcc175f2f (full mathematical result compared).
4. “Marked Wendel law and convex-order optimal sampling for random inscribed polygons,” publicly indexed mathematical finding, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-marked-wendel-law-and-convex-order-optimal-sampling-for-random-i--6fc92189d743 (full mathematical result compared).
5. L. Holst and J. Hüsler, “On the random coverage of the circle,” *Journal of Applied Probability* **21** (1984), 558–567 (abstract located; full text not inspected and retained as historical-priority risk).
