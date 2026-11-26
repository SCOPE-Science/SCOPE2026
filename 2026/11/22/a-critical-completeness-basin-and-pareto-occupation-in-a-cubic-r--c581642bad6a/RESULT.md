# A critical completeness basin and Pareto occupation in a cubic rigid flow

## Finding

Fix \(\lambda>0\), put \(h_{\mathrm c}=\sqrt{1+\lambda^2}/\lambda\), and consider the real planar cubic differential system
\[
\begin{aligned}
\dot x&=-y+x\bigl(\lambda-(x^2+y^2)+h(x^2-y^2)\bigr),\\
\dot y&=x+y\bigl(\lambda-(x^2+y^2)+h(x^2-y^2)\bigr).
\end{aligned}
\]
At either critical anisotropy \(h=\pm h_{\mathrm c}\), let \(\theta_*\) be an angle determined by
\[
\cos(2\theta_*)=\frac{h\lambda^2}{1+\lambda^2},\qquad
\sin(2\theta_*)=\frac{h\lambda}{1+\lambda^2}.
\]
Equivalently, \((\cos2\theta_*,\sin2\theta_*)=\operatorname{sgn}(h)(\lambda,1)/\sqrt{1+\lambda^2}\). Put \(c=\sqrt{\lambda/2}\), and interpret angles modulo \(\pi\). A nonzero initial state with polar coordinates \((r_0,\theta_0)\) is forward complete **if and only if**
\[
\boxed{\quad r_0^2\,\frac{2}{\lambda}\sin^2(\theta_0-\theta_*)<1.\quad}
\]
Equivalently, in the rotated Cartesian coordinate \(q=y\cos\theta_*-x\sin\theta_*\), the **entire forward-complete set is the infinite open Euclidean strip** \(\mathcal C=\{(x,y):|q|<c\}\), with \(c=\sqrt{\lambda/2}\). Its two boundary lines are invariant trajectories up to their finite-time escape. All other nonzero states blow up in finite positive *original physical time*. Every nonzero forward-complete trajectory is unbounded, with an exactly exponentially growing sequence of radii sampled at the phases \(\theta_*\bmod\pi\): defining
\[
\Delta=r_0^{-2}-\frac2\lambda\sin^2(\theta_0-\theta_*)>0,
\]
for each sufficiently large nonnegative integer \(k\), at the time \(t_k=\theta_* -\theta_0+k\pi>0\),
\[
\boxed{\quad r(t_k)=\Delta^{-1/2}e^{\lambda t_k}.\quad}
\]

Let \(\mathcal C\) be the set of forward-complete initial states, including the origin, and let \(D_R\) denote the Euclidean radius-\(R\) disk. The **exact Euclidean area** is
\[
\boxed{\quad |\mathcal C\cap D_R|=\begin{cases}
\pi R^2,&0<R\le c,\\
2R^2\arcsin(c/R)+2cR\sqrt{1-c^2/R^2},&R>c.
\end{cases}\quad}
\]
In particular, \(|\mathcal C\cap D_R|=2\sqrt{2\lambda}\,R+O(R^{-1})\). Thus this open forward-complete basin has infinite planar area but zero asymptotic planar-area density.

For **every** nonzero forward-complete solution and **every** \(R>0\), its original-time radial occupation fraction satisfies
\[
\boxed{\quad \lim_{T\to\infty}\frac1T\bigl|\{t\in[0,T]:r(t)>R\}\bigr|
=\begin{cases}
1,&0<R\le c,\\
\dfrac2\pi\arcsin(c/R),&R>c.
\end{cases}\quad}
\]
The limiting radial survival distribution has Pareto tail \(\sqrt{2\lambda}/(\pi R)+O(R^{-3})\) and infinite first moment. These assertions do **not** require any invariant finite probability measure on the noncompact orbit.

## Assumptions and scope

The vector field and solutions are real; \(\lambda>0\) is arbitrary and \(h=\pm h_{\mathrm c}\). Forward completeness means existence on every finite interval \([0,T]\) in physical time. The zero equilibrium is complete and excluded from the assertions about phase-sampled radii and occupation fractions. \(|\cdot|\) applied to sets in the area formula means planar Lebesgue measure; applied to subsets of the time interval it means one-dimensional Lebesgue measure. The inequalities describing \(\mathcal C\) are strict; points on the nonzero basin boundary are not complete. This is a sharp critical-slice statement, not a full bifurcation diagram for all parameters.

## Proof

Write \(x=r\cos\theta\), \(y=r\sin\theta\) with \(r>0\). Direct calculation gives \(\dot\theta=1\) and
\[
\dot r=\lambda r+r^3(-1+h\cos2\theta).
\]
Set \(u=r^{-2}\). As long as the solution is finite and nonzero,
\[
\dot u=-2\lambda u+2(1-h\cos2\theta),\qquad \theta(t)=\theta_0+t.
\]
A periodic particular solution is
\[
H_h(\theta)=\frac1\lambda-\frac{h(\lambda\cos2\theta+\sin2\theta)}{1+\lambda^2},
\]
so the unique solution satisfies the exact identity
\[
\boxed{u(t)=H_h(\theta_0+t)+\bigl[r_0^{-2}-H_h(\theta_0)\bigr]e^{-2\lambda t}.}\tag{1}
\]
At \(|h|=h_{\mathrm c}\), the amplitude of the oscillatory term equals \(1/\lambda\), and choosing \(\theta_*\) as above gives \(H_h(\theta)=(2/\lambda)\sin^2(\theta-\theta_*)\). Let \(\Delta=r_0^{-2}-H_h(\theta_0)\). If \(\Delta>0\), formula (1) stays strictly positive for every finite \(t\ge0\); therefore the radial solution is finite on every compact time interval, establishing forward completeness. If \(\Delta=0\), it first reaches zero at a finite positive time when \(\theta_0+t\equiv\theta_*\pmod\pi\) (unless \(r_0^{-2}=0\), impossible for finite nonzero initial radius). If \(\Delta<0\), evaluating (1) at the next strictly positive such phase gives a negative value, whereas \(u(0)=r_0^{-2}>0\); by continuity \(u\) first reaches zero earlier. When \(u\downarrow0\), \(r=u^{-1/2}\to\infty\), so continuation in the finite plane is impossible. This establishes the exact completeness criterion and the boundary convention. With \(\Delta>0\), (1) evaluated at each zero of \(H_h\) gives the exact phase-sampled values. These are not times of local maxima: \(H_h'(\theta_*+k\pi)=0\) and \(u'(t_k)=-2\lambda u(t_k)\), giving \(r'(t_k)=\lambda r(t_k)>0\). The sampled values suffice to show that no nonzero complete solution is bounded.

For the area formula, \(r_0^2\sin^2(\theta_0-\theta_*)=(y_0\cos\theta_*-x_0\sin\theta_*)^2=q_0^2\). Thus \(\Delta>0\) is exactly \(|q_0|<c\), proving that the complete region is an infinite straight strip, without exceptional boundary rays. To verify the invariant straight boundaries directly, put \(p=x\cos\theta_*+y\sin\theta_*\). At criticality \(h\cos2\theta_*=1\) and \(h\sin2\theta_*=1/\lambda\), so \(\lambda-(x^2+y^2)+h(x^2-y^2)=\lambda-2q^2-2pq/\lambda\) and consequently \(\dot q=(p+\lambda q)(1-2q^2/\lambda)\). Hence both lines \(q=\pm c\) are invariant for as long as their solutions exist, and the earlier sign argument shows their finite-time escape. Orthogonal coordinates \((q,w)\) preserve Euclidean area. Integrating horizontal chords of the radius-\(R\) disk gives, for \(R>c\),
\[
|\mathcal C\cap D_R|=\int_{-c}^c 2\sqrt{R^2-q^2}\,dq=2R^2\arcsin(c/R)+2c\sqrt{R^2-c^2}.
\]
If \(R\le c\), the entire disk is in the closed strip up to a null boundary and has area \(\pi R^2\). Taylor expansion of \(\arcsin(c/R)\) and \(\sqrt{1-c^2/R^2}\) gives
\[
|\mathcal C\cap D_R|=4cR-\frac{2c^3}{3R}+O(R^{-3}).
\]
This proves both infinite area and zero area density (the ratio to \(\pi R^2\) tends to zero).

For time occupation, (1) implies that at every angular phase except \(\theta\equiv\theta_*\pmod\pi\), the radius along successive turns converges to
\[
r_\infty(\theta)=\frac{c}{|\sin(\theta-\theta_*)|}.
\]
For each fixed \(R>0\), the set of phases satisfying \(r_\infty(\theta)=R\) is finite or empty; in particular it has measure zero. Partition the time integral into complete \(2\pi\)-turns and use bounded convergence on the angular interval for the indicators \(\mathbf1_{\{r(t)>R\}}\) (their only possible nonconvergent phases have measure zero). The Cesàro average of turn integrals converges to the fraction of phases with \(r_\infty(\theta)>R\). That fraction equals \(1\) if \(R\le c\), and \(2\arcsin(c/R)/\pi\) otherwise. The incomplete last turn contributes at most \(2\pi/T\). Finally, \(\arcsin(c/R)=c/R+O(R^{-3})\); the positive survival-tail integral diverges, proving infinite first moment of the limiting distribution. This completes the proof.

## Verification

`verify.py` is a standalone Python 3 checker using only the standard library. Run `python3 verify.py` from the same directory as this document. It checks the periodic particular-solution differential identity by exact rational coefficient comparison at several parameter samples, evaluates the critical-phase radius formula for representative parameters, and numerically compares the exact disk-area formula with independent deterministic quadrature for multiple disk radii. These finite checks are consistency tests; the statements for every parameter, every initial condition, and infinite time rest on the preceding analytic proof.

## Relationship to prior work

Llibre's 2024 preprint studies the same general class of homogeneous rigid polynomial flows (primary MSC 34C05) and supplies a Bernoulli radial solution, qualitative limit-cycle classification and an example of a connection at infinity. The earlier Gasull–Torregrosa 2004/2005 work already proves the general inverse-radial linearization, the limit-cycle criterion and disappearance in a polycycle. All those ingredients are **prior**, including integrability and existence of a critical infinity connection. The additional result here is the exact separation of finite-time blowup from forward-complete *yet unbounded* orbits on a natural sign-changing harmonic critical slice, together with the full disk-truncated completeness-area law and a physical-time Pareto occupation law. The explicit periodic inverse-radius solution by itself is not claimed as new. Published results on a different rigid cubic's finite-time survival ellipses, and on a different quartic rigid center's area-growth exponents, concern distinct initial-condition sets and do not give this critical completeness geometry.

## Limitations

This is a theorem about the critical \(|h|=h_{\mathrm c}\) family only, not a claim that all large-data trajectories remain bounded at nearby subcritical parameters. The limiting radial occupation distribution is an empirical distribution along each complete nonzero trajectory; it does not assert convergence to an invariant probability on the full plane. Earlier general solution formulas imply the critical strip by specialization, but do not state its disk-area and original-time occupation laws in the inspected passages. Additional unindexed results could supersede these measure conclusions.

## References

1. J. Llibre, *Rigid Polynomial Differential Systems with Homogeneous Nonlinearities*, preprint posted 2024-07-24, https://www.preprints.org/manuscript/202407.1946/v1 ; published in *Mathematics* 12 (2024), 2806, https://doi.org/10.3390/math12182806 .
2. A. Gasull and J. Torregrosa, *Exact number of limit cycles for a family of rigid systems*, *Proceedings of the American Mathematical Society* 133 (2005), 751–758, electronically published 2004-10-07, https://doi.org/10.1090/S0002-9939-04-07542-2 . Author-hosted accessible text: https://www.researchgate.net/publication/248816417_Exact_number_of_limit_cycles_for_a_family_of_rigid_systems .
3. A. Gasull, R. Prohens and J. Torregrosa, *Limit cycles for rigid cubic systems*, *Journal of Mathematical Analysis and Applications* 303 (2005), 391–404, https://doi.org/10.1016/j.jmaa.2004.07.030 .
