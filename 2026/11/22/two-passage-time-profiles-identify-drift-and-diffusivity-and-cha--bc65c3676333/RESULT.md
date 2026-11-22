# Two passage-time profiles identify drift and diffusivity and characterize realizable data

## Finding

Consider an Itô diffusion on a finite interval with an absorbing left endpoint and a reflecting right endpoint. Its mean absorption-time profile and its variance profile, observed as functions of the starting position, uniquely determine **both** the spatial drift and the spatial diffusivity, even when both are initially unknown. There is an exact necessary-and-sufficient compatibility test for smooth proposed profiles.

Let \(\tau(x)=\mathbb E_x T\), \(v(x)=\operatorname{Var}_x T\), and
\[
W(x)=\tau'(x)v''(x)-v'(x)\tau''(x)+2\tau'(x)^3.
\]
For \(0\le x<L\), the only possible coefficients are
\[
\boxed{D(x)=\frac{v'(x)}{W(x)},\qquad b(x)=\frac{-1-D(x)\tau''(x)}{\tau'(x)}.}
\]
Every regular diffusion has \(\tau'(x)>0\), \(v'(x)>0\), and \(W(x)>0\) there. Conversely, smooth profiles satisfying the four mixed boundary conditions, these strict inequalities, and regular extendibility of the reconstructed coefficients uniquely arise from such a diffusion.

At a reflecting endpoint there is a universal fourth-order variance law:
\[
\lim_{x\uparrow L}\frac{v(L)-v(x)}{(L-x)^4}=\frac{1}{6D(L)^2}.
\]
A nontrivial family shares **exactly the same mean profile** while having strictly ordered variances, proving that the variance measurement is genuinely informative and not simply an alternative parametrization of the mean.

## Assumptions and scope

Fix \(L>0\). On \([0,L]\), consider
\[
dX_t=b(X_t)\,dt+\sqrt{2D(X_t)}\,dB_t+dK_t,
\]
where the reflection regulator \(K_t\) acts only at \(L\), inward, and the path is killed on first reaching \(0\). Assume \(D,b\in C^1([0,L])\) and \(D(x)\ge d_*>0\). The infinitesimal generator on the interior is \(\mathcal Lf=D f''+bf'\). All moments of the absorption time \(T\) are finite on this compact uniformly elliptic domain.

For the converse, suppose \(\tau,v\in C^3([0,L])\), satisfying \(\tau(0)=v(0)=0\) and \(\tau'(L)=v'(L)=0\). Require \(\tau'(x)>0\), \(v'(x)>0\), and \(W(x)>0\) for every \(0\le x<L\). Calculate \(D\) and \(b\) from the displayed formulas for \(x<L\), and **also require** they possess extensions to \([0,L]\) with \(D,b\in C^1\) and \(\inf D>0\). These explicit boundary-regularity conditions are essential; positivity of \(W\) alone is not sufficient without them.

The assertion concerns exact full spatial profiles, not two scalar moments measured at a single starting point. It is a structural identifiability and realization theorem, not a statistical stability guarantee.

## Proof

**1. Backward moment identities.** The mean solves the unique Dirichlet–Neumann boundary problem
\[
\mathcal L\tau=-1,\quad\tau(0)=0,\quad\tau'(L)=0.
\]
The second raw moment \(m_2=\mathbb E_xT^2\) solves \(\mathcal Lm_2=-2\tau\) with the same homogeneous boundary conditions. Because \(v=m_2-\tau^2\) and \(\mathcal L(\tau^2)=2\tau\mathcal L\tau+2D(\tau')^2\), subtraction gives the exact *variance* equation
\[
D(x)v''(x)+b(x)v'(x)=-2D(x)\tau'(x)^2.
\]
The factor on the right is the variable diffusivity, not a constant.

**2. Positive derivatives.** Define \(I(x)=\exp(\int_0^x b(u)/D(u)\,du)>0\). Integrating the mean and variance ODEs backward from their right Neumann conditions yields
\[
\tau'(x)=I(x)^{-1}\int_x^L\frac{I(y)}{D(y)}\,dy,
\qquad
v'(x)=2I(x)^{-1}\int_x^LI(y)\tau'(y)^2\,dy.
\]
Both derivatives are strictly positive for \(x<L\), including \(x=0\).

**3. Unique reconstruction and compatibility.** Multiply the variance ODE by \(\tau'\), subtract \(v'\) times the mean ODE, and rearrange. The drift cancels and gives
\[
D\{\tau'v''-v'\tau''+2(\tau')^3\}=v'.
\]
Thus \(W=v'/D>0\) and the claimed formulas for both coefficients follow. Any two regular coefficients with the same two profiles must coincide on \([0,L)\), and hence by continuity at \(L\). In the reverse direction, the assumed extension conditions make these formulas regular; direct substitution verifies the two backward equations and their mixed boundary conditions. The two boundary-value problems have unique solutions (e.g. by the integrating-factor formula), so the reconstructed diffusion realizes the prescribed mean and variance. This proves necessity and sufficiency without any statistical or numerical assumption.

**4. Boundary signature.** Write \(s=L-x\). The mean ODE at the reflecting wall gives \(\tau''(L)=-1/D(L)\); hence \(\tau'(L-s)=s/D(L)+O(s^2)\). The preceding positive integral for the variance implies
\[
v'(L-s)=\frac{2s^3}{3D(L)^2}+O(s^4),
\qquad
v(L)-v(L-s)=\frac{s^4}{6D(L)^2}+O(s^5).
\]
It also follows that \(W(L-s)=2s^3/[3D(L)^3]+O(s^4)\). This specifies the common vanishing order of numerator and denominator in the reconstruction formula and explains why direct inversion becomes poorly conditioned near reflection.

**5. A mean-blind, variance-distinguishable family.** Set \(L=1\). For every \(\eta>-1\), define
\[
D_\eta(x)=1+\eta(1-x)^2,\quad b_\eta(x)=\eta(1-x),
\quad\tau_\eta(x)=x-\frac{x^2}{2}.
\]
These coefficients are regular and positive where needed. Direct substitution gives \(D_\eta\tau_\eta''+b_\eta\tau_\eta'=-1\) with the required boundary conditions, so the *entire* mean profile is independent of \(\eta\). Writing \(s=1-x\), the variance integral is
\[
v_\eta'(x)=2\sqrt{1+\eta s^2}\int_0^s\frac{u^2}{\sqrt{1+\eta u^2}}\,du.
\]
For fixed \(0<u<s\), the ratio \(\sqrt{(1+\eta s^2)/(1+\eta u^2)}\) increases strictly with \(\eta>-1\), because \(z/(1+\eta z)\) increases strictly with \(z\ge0\). Therefore \(v_\eta'(x)\) increases strictly in \(\eta\) for all \(x<1\). Integrating \(v_\eta(0)=0\) proves that for \(\eta_2>\eta_1>-1\), \(v_{\eta_2}(x)>v_{\eta_1}(x)\) at every \(0<x\le1\). At \(\eta=0\), the explicit profile is \(v_0(x)=[1-(1-x)^4]/6\). Thus, first-moment ambiguity persists throughout a smooth, physical one-parameter family, and the second profile resolves it.

## Verification

The standalone `checker.py` uses only standard-library Python. It independently evaluates the explicit integral formula for the example family by composite Simpson quadrature, differentiates the integral analytically, and checks recovery of \(D_\eta\) and \(b_\eta\), the two backward equations, the constant-diffusivity closed form, strict variance ordering at five starting positions, and the reflecting-wall fourth-order limit. It passed **183** deterministic assertions. These checks concern a finite test family and do **not** replace the general proof in the preceding section.

Reproduce with `python3 checker.py`. No external paper, inaccessible table, downloaded data, or other artifact is required to run it.

## Relationship to prior work

Keidar, Reuveni, and Sokolov (2026) treat the inverse mean first-passage profile for a conservative force with a **known constant diffusion coefficient** on a half-line. Its admissibility condition and trapping/sliding results address a different inverse problem, and are not claimed here. Xiang, Zhou, and Xiang (2026) recover **scalar parameters** for arithmetic and geometric Brownian motion from first two hitting-time moments; this does not treat two freely varying coefficient functions or an exact class of realizable spatial profiles. Bal and Chou (2004) study reconstruction from the *entire* exit-time distribution at selected initial positions with additional a priori coefficient information; they also reference classical identification using mean exit time plus an exit-side probability on a two-exit interval. Neither is the exact first-two-moment, single-absorber spatial-profile reconstruction established here. The backward moment hierarchy itself is classical.

## Limitations

The theorem assumes exact, sufficiently smooth profiles for every starting position, uniform ellipticity, a finite one-dimensional interval, and a reflecting endpoint opposite absorption. The compatibility criterion includes explicit endpoint regularity of the reconstructed coefficients. No recovery rate under noise or from finitely many starting positions is proved; derivative-based inversion may be ill-conditioned near reflection. An equivalent result may be implicit in older inverse diffusion or passage-moment literature, so publication priority has not been independently established. No multidimensional extension is claimed.

## References

1. T. D. Keidar, S. Reuveni and I. M. Sokolov, *The Inverse Mean First-Passage Time Problem*, arXiv:2611.03831v1, first submitted 2026-11-02. https://arxiv.org/html/2611.03831v1
2. X. Xiang, J. Zhou and B. Xiang, *Moment-Based Identification of Diffusion Generators via First Hitting Times*, Mathematics 14 (2026), 2586, DOI:10.3390/math14142586. https://www.mdpi.com/2227-7390/14/14/2586
3. G. Bal and T. Chou, *On the reconstruction of diffusions from first-exit time distributions*, Inverse Problems 20 (2004), 1053–1065, DOI:10.1088/0266-5611/20/4/004. https://www.stat.uchicago.edu/~guillaumebal/PAPERS/FirstExit.pdf
4. M. Cristofol and L. Roques, *Simultaneous determination of the drift and diffusion coefficients in stochastic differential equations*, arXiv:1702.06859, 2017. https://arxiv.org/abs/1702.06859
