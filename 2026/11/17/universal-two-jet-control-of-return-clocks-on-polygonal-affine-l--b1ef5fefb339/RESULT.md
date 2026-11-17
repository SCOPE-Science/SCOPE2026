# Universal two-jet control of return clocks on polygonal affine limit cycles

## Finding

Consider the polygonal piecewise-affine oscillator with a prescribed counterclockwise simple star-shaped cycle. **For every admissible polygon and every choice of positive edge speeds and transverse decay rates, any two distinct tangential shear gains independently control the first two transverse Taylor coefficients of its physical first-return time**, near an explicitly calibrated gain vector. The Jacobian has every ordered two-column minor strictly positive. The cycle's geometric shape, its original-time period, and its transverse Floquet multiplier are unchanged throughout the adjustment.

Here is the exact statement. Fix an integer \(N\ge3\); nonzero vertices \(p_1,\ldots,p_N\in\mathbb R^2\) in counterclockwise order, forming a simple origin-star-shaped polygon with the origin strictly inside and consecutive polar-angle gaps in \((0,\pi)\); and arbitrary \(\omega_i>0\), \(\lambda_i>0\). Use cyclic subscripts, and set
\[
 e_i=p_{i+1}-p_i,\qquad n_i=((e_i)_2,-(e_i)_1),\qquad
 \Delta_i=\det(p_i,p_{i+1})>0,\qquad
 k_i=\lambda_i\|e_i\|^2,
\]
\[
 \alpha_i=\frac{e_i\cdot p_i}{\|e_i\|^2},\qquad
 c_i=\frac{k_i}{\omega_i},\qquad q_i=e^{-c_i},\qquad
 Q_i=\prod_{h<i}q_h,\quad Q_1=1.
\]
On the open sector bounded by the rays through \(p_i\) and \(p_{i+1}\), the affine vector field is
\[
 \dot x=(\omega_i-\mu_iV_i(x))e_i-\lambda_iV_i(x)n_i,
 \qquad V_i(x)=n_i\cdot x-\Delta_i,
\]
with the next-sector continuation at transverse ray crossings. Every tangential shear parameter \(\mu_i\in\mathbb R\) is allowed. Let \(\mathcal T_\mu(s)\) be the physical elapsed time for the first complete forward return to the ray through \(p_1\), starting at \((1+s)p_1\), for all sufficiently small \(|s|\), and write
\[
 \mathcal T_\mu(s)=T+G(\mu)s+H(\mu)s^2+O(s^3),
 \qquad T=\sum_{i=1}^N\omega_i^{-1}.
\]
Define the calibrated gains and positive factors
\[
 \mu_i^*=\frac{k_i}{\Delta_i}\left(\alpha_i-\frac{q_i}{1-q_i}\right),\qquad
 B_i=\frac{\Delta_i(1-q_i)}{k_i\omega_i},\qquad
 R_i=Q_i\frac{c_iq_i}{1-q_i}.
\]
Then \(\mathcal T_{\mu^*}(s)=T\) identically for all sufficiently small \(|s|\); hence \(G(\mu^*)=H(\mu^*)=0\). The \(2\times N\) Jacobian of \((G,H)\) at this calibration has columns
\[
 \boxed{\begin{pmatrix}\partial_{\mu_i}G\\\partial_{\mu_i}H\end{pmatrix}_{\mu^*}
       =Q_iB_i\begin{pmatrix}1\\-R_i\end{pmatrix}.}
\]
Moreover \(R_1>R_2>\cdots>R_N>0\), so for *every* \(1\le i<j\le N\),
\[
 \boxed{\det \frac{\partial(G,H)}{\partial(\mu_i,\mu_j)}\bigg|_{\mu^*}
 =Q_iB_iQ_jB_j(R_i-R_j)>0.}
\]
Holding all other gains fixed at their calibrated values, any pair \((\mu_i,\mu_j)\) consequently realizes all sufficiently small prescribed pairs \((G,H)\). This also independently prescribes the actual derivatives \((\mathcal T_\mu'(0),\mathcal T_\mu''(0))=(G,2H)\). Throughout, the polygonal periodic orbit is unchanged, its period is \(T\), and its nontrivial Floquet multiplier is \(\prod_{i=1}^Nq_i\), independent of \(\mu\).

## Assumptions and scope

All assertions concern the deterministic *forward, next-sector hybrid continuation* of affine flows through the prescribed polygonal switching rays. The local first-return map and clock are well-defined and analytic in the radial section displacement and the gains near the cycle because every edge is traversed with positive speed \(\omega_i\) at the orbit and the corresponding crossing is transverse. The switching field is not claimed to be continuous or classically differentiable across sector boundaries. The stated Jacobian uses the incoming vertex-ray displacement \(s\), not Euclidean normal distance or an asymptotic phase coordinate; those choices alter numerical coefficients. The result needs no uniformity of the positive speeds or decay rates, and it places no sign restriction on the tangential shear gains.

## Proof

**1. Integrate one affine sector.** Put \(E_i=\|e_i\|^2\) and abbreviate \(p=p_i\), \(e=e_i\), \(n=n_i\), \(\Delta=\Delta_i\), \(k=k_i\), \(\omega=\omega_i\), \(\mu=\mu_i\). The identities \(n\cdot p=\Delta\), \(n\cdot e=0\), \(\|n\|^2=E\) give \(V((1+s)p)=\Delta s\) and \(\dot V=-kV\). The affine trajectory starting at \((1+s)p\) is exactly
\[
 x(t)=(1+s)p+\omega te-\frac{\Delta s}{k}(1-e^{-kt})(\mu e+\lambda n).
\]
At the next ray the state must be \((1+s_+)p_{i+1}\). Taking the normal coordinate yields \(s_+=s e^{-kt}\). Projecting onto \(e\), using \(e\cdot p=E\alpha\), and rearranging yields the exact first-crossing equation
\[
 \boxed{\omega t-1=s\big[(b+1)e^{-kt}-b\big],\qquad
 b=\alpha-\frac{\mu\Delta}{k},\qquad s_+=se^{-kt}.} \tag{1}
\]
At \(s=0\), its root is \(t=1/\omega\) and its derivative with respect to \(t\) is \(\omega>0\). The implicit-function theorem and the orbit's positive forward crossings make this the unique local selected first-exit time.

**2. Calibrate every sector to a constant flight time.** Setting \(b=q/(1-q)\), where \(q=e^{-k/\omega}\), makes the right-hand side of (1) vanish identically at \(t=1/\omega\), for every sufficiently small \(s\). This is precisely the displayed choice of \(\mu_i^*\). Thus each sector takes exactly \(1/\omega_i\), its ray displacement is multiplied by \(q_i\), and one entire circuit takes \(T\), independently of the incoming \(s\), near the cycle. The return displacement becomes \((\prod_iq_i)s\). More generally, for arbitrary nearby gains, differentiating successive sector maps at \(s=0\) gives the same multiplier \(\prod_iq_i\), since each flight time there still equals \(1/\omega_i\). No part of this argument relies on global transversality or global attraction.

**3. Compute the two local clock jets.** For a general gain, expand the selected sector time in its incoming displacement \(u\) as
\[
 t_i(u)=\omega_i^{-1}+a_i u+d_i u^2+O(u^3).
\]
Expansion of (1) gives, with \(b_i=\alpha_i-\mu_i\Delta_i/k_i\),
\[
 a_i=\frac{(b_i+1)q_i-b_i}{\omega_i},\qquad
 d_i=-c_i(b_i+1)q_i a_i.
\]
At \(\mu^*\), both coefficients vanish. Their gain derivatives there are
\[
 \partial_{\mu_i}a_i=B_i>0,\qquad
 \partial_{\mu_i}d_i=-\frac{c_iq_i}{1-q_i}B_i.
\]
The incoming displacement of sector \(i\) is \(Q_i s+O(s^2)\), and its \(s^2\) coefficient vanishes at the common calibration. Therefore, differentiating the full sum of the sector flight times at \(\mu^*\), all cross-terms containing a calibrated \(a_i\) or a calibrated second-order displacement coefficient vanish. The coefficient variations are exactly
\[
 \partial_{\mu_i}G=Q_i B_i,\qquad
 \partial_{\mu_i}H=-Q_i^2\frac{c_iq_i}{1-q_i}B_i
  =-Q_iB_iR_i.
\]
These identities apply to any number of sectors, any geometry meeting the assumptions, and any positive \(\omega_i,\lambda_i\).

**4. Prove every ordered minor is positive.** For every \(z>0\),
\[
 \frac{z}{1-e^{-z}}>1,\qquad 0<\frac{z}{e^z-1}<1.
\]
It follows for consecutive indices that
\[
 \frac{R_i}{Q_iq_i}=\frac{c_i}{1-q_i}>1,
 \qquad
 \frac{R_{i+1}}{Q_iq_i}=\frac{c_{i+1}q_{i+1}}{1-q_{i+1}}<1.
\]
Thus \(R_i>R_{i+1}\) and hence \(R_i>R_j\) for every \(i<j\). Since all \(Q_i,B_i\) are positive, every displayed minor is strictly positive. The ordinary two-variable inverse-function theorem, applied with all other gains fixed, gives the independent local prescriptions of \(G,H\). The unperturbed polygon, its original-time period, and the section derivative \(\prod_iq_i\) depend only on the vertices, speeds, and decay rates, completing the proof.

## Verification

Run `python3 checker.py` using the Python 3 standard library. The script integrates the original two-dimensional affine vector fields analytically for each leg and checks their endpoint positions against the independently derived scalar first-crossing equation. It also checks exact calibrated times and radial multipliers near the polygon, verifies every ordered minor of the derived Jacobian, and compares finite-difference sensitivities with the analytic formulas in two independent geometries: a triangle with equal \(c_i=\log2\), and an irregular pentagon with unequal positive speeds and contractions. The triangle gives
\[
 \det\frac{\partial(G,H)}{\partial(\mu_1,\mu_2)}
 =\frac{1}{16\log2}\approx0.09016844005556.
\]
These finite checks corroborate the algebra. The analytic argument above, not a finite experiment, proves the theorem for all admissible polygons and positive parameters.

## Relationship to prior work

Kai (2026) introduces precisely the three-parameter polygonal affine vector-field family and proves the cycle's existence, period, and local attraction, including the role of tangential gain in transient motion. Those foundations are not claimed here. A closely related published open mathematical note, *Polygon-shape conjugacy and an explicit full-interior basin for calibrated affine oscillators*, establishes a **different**, globally defined calibration giving a common radial gauge and time-preserving shape conjugacy. Its tangential calibration is \(\mu_i=(a/\Delta_i)(\alpha_i+1/2)\) with common normal decay \(a\), not the constant-sector-flight calibration used here. It neither states nor implies the universal strict two-jet Jacobian for arbitrary positive and unequal per-edge decay rates and speeds. Another published note, *Exact one-sided crossing and a three-regime central startup transition in regular polygonal oscillators*, establishes a Lambert-function crossing map and central startup regimes for uniform regular polygons and nonnegative gains. That special geometry and one-sided singular-origin analysis do not yield the all-polygon, any-two-gain local rank theorem, although the shared crossing-equation technique is closely related.

General phase-response theory for piecewise-smooth oscillators studies infinitesimal phase shifts and matching conditions across switching boundaries (Park, Shaw, Chiel and Thomas, 2016), but does not directly provide this two-gain second-order return-clock design statement. The exact scalar return-time identity and first-order qualitative control are elementary consequences of the Kai model; the new structural point is their **joint, universally positive two-jet controllability over all pairs of gain coordinates**. The most plausible priority risks are unindexed local higher-order phase-sensitivity calculations and early polygonal-affine oscillator literature.

## Limitations

This is a local first-return clock and parameter-unfolding result at a prescribed hyperbolic polygonal cycle, not a statement about global basins, full-plane hybrid uniqueness, resetting phase at arbitrary pulse locations, arbitrary large timing perturbations, or global control of an entire phase response curve. The positivity uses the specified incoming vertex-ray coordinate and cyclic sector order. The earlier 2012 and 2019 polygonal oscillator papers were not completely available for full-text comparison; their identified earlier models precede the freely tunable tangential parameter introduced in 2026, but priority is not certified. Independent scientific validation has not been performed.

## References

1. T. Kai, *Piecewise affine oscillators with polygonal limit cycles*, International Journal of Dynamics and Control **14**, article 392 (first publicly available 2026-10-08), DOI: 10.1007/s40435-026-02340-6. https://link.springer.com/article/10.1007/s40435-026-02340-6
2. *Polygon-shape conjugacy and an explicit full-interior basin for calibrated affine oscillators*, openly published mathematical research record (2026-11-08), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-polygon-shape-conjugacy-and-an-explicit-full-interior-basin-for--595e7a393d3f
3. *Exact one-sided crossing and a three-regime central startup transition in regular polygonal oscillators*, openly published mathematical research record (2026-11-01), https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-exact-one-sided-crossing-and-a-three-regime-central-startup-tran--731cdfe46af3
4. Y. Park, K. M. Shaw, H. J. Chiel, and P. J. Thomas, *The Infinitesimal Phase Response Curves of Oscillators in Piecewise Smooth Dynamical Systems* (first public 2016-03-11), https://arxiv.org/abs/1603.03503
5. T. Kai and R. Masuda, *Limit cycle synthesis of multi-modal and 2-dimensional piecewise affine systems*, Mathematical and Computer Modelling **55** (2012), 505–516, DOI: 10.1016/j.mcm.2011.08.028.
6. T. Kai, S. Chiku and K. Maehara, *Derivation and mathematical analysis of piecewise affine oscillators with desired polygonal limit cycles*, European Control Conference (2019), 2632–2637, DOI: 10.23919/ECC.2019.8795666.
