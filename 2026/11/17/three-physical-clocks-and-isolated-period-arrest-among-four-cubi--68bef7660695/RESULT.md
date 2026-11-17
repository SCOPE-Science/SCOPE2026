# Three physical clocks and isolated period arrest among four cubic torus cycles

## Finding
Consider, for real \(a>1\), \(c>0\), \(\kappa>0\), and \(0<\lambda<\kappa/\sqrt{a^2+1}\), the cubic polynomial differential equations
\[
\begin{aligned}
\dot x&=\tfrac14(\kappa+\lambda x)xz+cxy^2,\\
\dot y&=\tfrac14(\kappa+\lambda x)yz-cx^2y,\\
\dot z&=\tfrac12(\kappa+\lambda x)[-a^2(x^2+y^2)+z^2+a^4-1].
\end{aligned}
\tag{1}
\]
The smooth algebraic torus \(\mathcal T_a=\{(x,y,z):(x^2+y^2-a^2)^2+z^2=1\}\) is invariant. As covered in more generality by the meridian theorem of Jana [1], it has exactly four periodic orbits: the meridians at polar angles \(0,\pi/2,\pi,3\pi/2\). The meridians at \(0\) and \(\pi\) are attracting *relative to the torus*, and the other two are repelling. Every non-meridian trajectory on the torus runs between an unstable meridian in backward time and a stable meridian in forward time.

The new quantitative conclusions concern the **original physical-time periods**, their precise stability multipliers, and a critical one-orbit slowdown. Put \(r(\varphi)=\sqrt{a^2+\cos\varphi}\), and write \(T_+\), \(T_-\), and \(T_0\) for the respective minimal periods on \(\theta=0\), \(\theta=\pi\), and either \(y\)-axis meridian. Then the four cycles have exactly **three distinct physical clocks**:
\[
\boxed{T_+=2\int_0^{2\pi}\frac{d\varphi}{r(\varphi)^2(\kappa+\lambda r(\varphi))}
\;<\;T_0=\frac{4\pi}{\kappa\sqrt{a^4-1}}
\;<\;T_-=2\int_0^{2\pi}\frac{d\varphi}{r(\varphi)^2(\kappa-\lambda r(\varphi))}.}
\tag{2}
\]
Their nontrivial torus-transverse Floquet multipliers satisfy
\[
\boxed{\mu_\pm=\exp\left[-2c\int_0^{2\pi}\frac{d\varphi}{\kappa\pm\lambda r(\varphi)}\right],
\qquad \mu_0=\exp(4\pi c/\kappa),}
\tag{3}
\]
where \(0<\mu_-<\exp(-4\pi c/\kappa)<\mu_+<1<\mu_0\). In particular, the **product of the two attracting multipliers** admits the exact closed form
\[
\boxed{\log(\mu_+\mu_-)=-\frac{8\pi c\kappa}{\sqrt{(\kappa^2-\lambda^2a^2)^2-\lambda^4}}.}
\tag{4}
\]

There is a sharp *single-meridian* slowdown at \(\lambda_c=\kappa/\sqrt{a^2+1}\). Set \(R=\sqrt{a^2+1}\) and \(\varepsilon=\kappa-\lambda R\). Holding \(a,c,\kappa\) fixed and letting \(\varepsilon\downarrow0\),
\[
\boxed{\sqrt\varepsilon T_-\longrightarrow\frac{4\pi}{R\sqrt\kappa},\qquad
\sqrt\varepsilon(-\log\mu_-)\longrightarrow\frac{4\pi cR}{\sqrt\kappa},\qquad
\frac{\log\mu_-}{T_-}\longrightarrow-cR^2.}
\tag{5}
\]
The other three cycles retain finite positive periods and finite nonzero multipliers in this limit. At the endpoint \(\lambda=\lambda_c\), the formerly periodic \(\theta=\pi\) meridian consists of a single equilibrium and a nonstationary homoclinic trajectory, while the other three meridians remain periodic. **Thus angular variation of the affine cofactor breaks the common-clock degeneracy and arrests just one of four cycles.**

## Assumptions and scope
All times and multipliers refer to the physical-time restriction of the three-dimensional flow (1) to the invariant smooth torus \(\mathcal T_a\); no ambient three-dimensional normal Floquet multiplier is claimed. The open-parameter theorem assumes exactly \(a>1\), \(c,\kappa>0\), \(0<\lambda<\kappa/R\). The endpoint description is a limit from below for fixed \(a,c,\kappa\); the critical field at equality is included only in the explicitly stated meridian claims. The four meridians are distinct embedded closed curves. No conclusion is asserted about all ambient trajectories away from \(\mathcal T_a\).

## Proof
Write \(s=x^2+y^2\), \(F=(s-a^2)^2+z^2-1\), and \(K'=\kappa+\lambda x\). Direct differentiation using (1) gives the polynomial identity \(\dot F=K'zF\), establishing invariance of \(\mathcal T_a\). Since \(a>1\), cylindrical angle is globally defined on the torus. Take coordinates modulo \(2\pi\):
\[
s=a^2+\cos\varphi,\quad z=\sin\varphi,\quad x=r(\varphi)\cos\theta,\quad y=r(\varphi)\sin\theta.
\]
From \(\dot s=\tfrac12K'z s\) and \(x\dot y-y\dot x=-cxy s\), the equations become exactly
\[
\dot\varphi=-\tfrac12 r(\varphi)^2[\kappa+\lambda r(\varphi)\cos\theta],\qquad
\dot\theta=-\tfrac c2r(\varphi)^2\sin(2\theta).
\tag{6}
\]
The first expression initially obtained at nonzero \(z\) extends continuously over \(z=0\). The strict parameter bound gives \(\kappa+\lambda r\cos\theta\ge\kappa-\lambda R>0\); hence \(\varphi\) winds strictly and monotonically. The four angular axes are invariant, and the second equation has a fixed nonzero sign in each open quadrant. No other closed trajectory can occur, while all four invariant meridians are periodic. More strongly, for each open quadrant,
\[
\frac{d}{dt}\log|\tan\theta|=-cr(\varphi)^2\le-c(a^2-1)<0.
\tag{7}
\]
The same formula integrated backwards implies \(\theta\) approaches the appropriate repelling axis, and forwards the appropriate attracting axis. Monotonic winding with a positive lower speed implies the full corresponding meridian is the forward/backward limit set. These general qualitative conclusions are consistent with, and already covered by, Jana's Theorem 2.4 [1].

On \(\theta=0,\pi\), the angular speed in (6) becomes \(-\tfrac12r^2(\kappa\pm\lambda r)\); on the other two meridians it becomes \(-\tfrac12\kappa r^2\). Integrating one full negative circuit of \(\varphi\) gives precisely (2). Positivity ensures minimality. The inequalities follow pointwise from \(\kappa-\lambda r<\kappa<\kappa+\lambda r\). The elementary identity \(\int_0^{2\pi} (a^2+\cos\varphi)^{-1}d\varphi=2\pi/\sqrt{a^4-1}\) gives the closed middle clock.

Linearizing the second equation of (6) about the stable axes \(0\) and \(\pi\) yields \(\dot u=-cr^2u\); around either unstable axis \(\dot u=+cr^2u\). Using the corresponding positive physical-time element \(dt=2|d\varphi|/[r^2(\kappa\pm\lambda r)]\) establishes (3). For their product,
\[
\begin{aligned}
\int_0^{2\pi}\left(\frac1{\kappa+\lambda r}+\frac1{\kappa-\lambda r}\right)d\varphi
&=2\kappa\int_0^{2\pi}\frac{d\varphi}{\kappa^2-\lambda^2(a^2+\cos\varphi)}\\
&=\frac{4\pi\kappa}{\sqrt{(\kappa^2-\lambda^2 a^2)^2-\lambda^4}}.
\end{aligned}
\]
Here \(\kappa^2-\lambda^2a^2>\lambda^2>0\). Multiplication by \(-2c\) proves (4); strict inequalities among stable multipliers follow by positive integrand ordering.

For the boundary in (5), fix \(a,c,\kappa\) and set \(R=\sqrt{a^2+1}\). The only vanishing of \(\kappa-\lambda r(\varphi)\) at criticality occurs at \(\varphi=0\bmod2\pi\). Uniformly as \(\varepsilon\downarrow0\) and \(\varphi\to0\),
\[
\kappa-\lambda r(\varphi)
=\varepsilon+\frac{\kappa}{4R^2}\varphi^2+O(\varepsilon\varphi^2+\varphi^4),\qquad r(\varphi)^2=R^2+O(\varphi^2).
\tag{8}
\]
Split the full-circle integrals at any fixed small neighborhood of this point. On its complement, the integrals are bounded uniformly in \(\varepsilon\). On the neighborhood, put \(\varphi=\sqrt\varepsilon v\). The rescaled denominator tends to \(1+\kappa v^2/(4R^2)\), and is bounded from below by a positive multiple of \(1+v^2\) after scaling. Dominated convergence, followed by \(\int_{-\infty}^{\infty}(1+\kappa v^2/(4R^2))^{-1}dv=2\pi R/\sqrt\kappa\), gives
\[
\sqrt\varepsilon\int_0^{2\pi}\frac{d\varphi}{\kappa-\lambda r(\varphi)}\to\frac{2\pi R}{\sqrt\kappa},\qquad
\sqrt\varepsilon\int_0^{2\pi}\frac{d\varphi}{r(\varphi)^2(\kappa-\lambda r(\varphi))}\to\frac{2\pi}{R\sqrt\kappa}.
\]
Substitution into (2)–(3) gives (5). For \(\theta=0,\pi/2,3\pi/2\), all speed denominators remain uniformly positive at \(\lambda=\lambda_c\), so periods and multipliers converge to finite nonzero limits. At equality, on \(\theta=\pi\), equation (6) has one zero at \(\varphi=0\), is strictly negative elsewhere, and uniqueness on the periodic angular circle gives one equilibrium and one orbit homoclinic to it. This completes every claimed boundary statement.

## Verification
The standalone `checker.py` uses exact rational arithmetic to check the polynomial cofactor identity at multiple sample points, and standard-library Simpson quadrature to check (2)–(4) and the approaches to the constants in (5) at representative parameters. Run `python3 checker.py`. It prints `ANISOTROPIC_TORUS_CHECK_OK` on successful checks. The finite quadratures do not prove the asymptotic statements; their proofs are the algebraic reduction, exact trigonometric integral and dominated-convergence argument above. The checker uses the original time variable without numerical time rescaling.

## Relationship to prior work
Jana [1], Theorems 2.1 and 2.4, proves the complete cubic torus-tangency parameterization and the classification of the four invariant meridians as alternating stable/unstable limit cycles. Example 5.5 specifically uses constant affine factor \(K'=1\) and \(f=xy\). Thus the existence of four cycles and their alternating stability are **prior results** rather than a novelty claim here. The present result concerns the distinct physical periods, ordered multipliers, their exact product and the isolated critical arrest under the natural anisotropic affine perturbation \(K'=\kappa+\lambda x\). The inspected source does not provide those formulas.

An existing exact study [4] treats instead \(K'=\lambda+\eta z\), whose four meridians all share the same original-time period and undergo a *simultaneous* slowdown when its coefficient reaches a zero. Its exact common-clock law cannot imply the anisotropic three-clock ordering or the *single-cycle* slowdown; the cofactor in the current theorem depends on the meridian through \(x=r\cos\theta\), while its cofactor depends only on the winding variable \(z=\sin\varphi\).

Earlier studies [2,3] address counts, existence and configurations of invariant meridians and parallels. They are acknowledged; the accessible portions do not establish the present quantitative statements. A complete full-text comparison with [2] was not possible, so an equivalent prior derivation cannot be excluded.

## Limitations
The entire theorem is restricted to the embedded torus; the second, ambient-normal Floquet multiplier is not computed. The critical endpoint is not included in the four-cycle regime; only three cycles survive there. The exact global critical dynamics off the singled-out meridian at equality, perturbation persistence beyond this polynomial family, and all ambient off-torus dynamics are outside scope. The novelty comparison is limited by incomplete access to some older sources, and general singular-integral methods already predict the square-root *exponent*, though not these family-specific coefficients, multiplier product, or one-meridian selection.

## References
1. S. Jana, *Characterization and dynamics of certain classes of polynomial vector fields on the torus*, arXiv:2401.07843v3 (first public version 2024-01-15), *J. Math. Anal. Appl.* **542** (2025), 128875. https://arxiv.org/abs/2401.07843 ; https://arxiv.org/html/2401.07843v3
2. J. Llibre and J. C. Medrado, *Limit cycles, invariant meridians and parallels for polynomial vector fields on the torus*, *Bull. Sci. Math.* **135** (2011), 1–9. https://doi.org/10.1016/j.bulsci.2010.06.005
3. J. Llibre and S. Rebollo-Perdomo, *Invariant parallels, invariant meridians and limit cycles of polynomial vector fields on some 2-dimensional algebraic tori in* \(\mathbb R^3\), *J. Dyn. Differ. Equ.* **25** (2013), 777–793. https://doi.org/10.1007/s10884-013-9315-4
4. *Two inequivalent infinite-period degenerations of four cubic torus cycles*, published mathematical research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-two-inequivalent-infinite-period-degenerations-of-four-cubic-tor--90d0f82e44b0
