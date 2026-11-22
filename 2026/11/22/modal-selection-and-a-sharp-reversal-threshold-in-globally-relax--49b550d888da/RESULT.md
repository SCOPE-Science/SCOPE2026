# Modal selection and a sharp reversal threshold in globally relaxed classical RK4

## Finding

A **single global quadratic-energy relaxation** of classical fourth-order Runge–Kutta (RK4) can transfer essentially *all* of the conserved energy of independent oscillators to one subset of modes, although the differential equation preserves every modal energy separately. The phenomenon admits a dimension-free selection law and an explicit sharp two-frequency reversal threshold.

For independent nonzero-frequency planar oscillators, let \(E_{j,n}\) denote each squared modal amplitude after the \(n\)-th globally relaxed step, and let \(x_j=h\omega_j\), where the common base step \(h>0\) obeys \(0<x_j^2<12\) on every initially excited mode. Define
\[
D(t)=t^3-8t^2-48t+576,\quad q(t)=\frac{tD(t)}{576},\quad g(t)=\frac{48(12-t)}{D(t)}.
\]
Write \(g_j=g(x_j^2)\). Among the initially excited modes let \(g_*\) be the smallest \(g_j\). Then, for **every** finite number of oscillators and any nonzero initial energy distribution, the sum of energies of the modes with \(g_j=g_*\) tends to the total initial energy; all other modal energies tend to zero. If the winner is unique, it collects the entire conserved energy. For a losing mode \(j\) that remains nonzero, its asymptotic one-step energy ratio exists and equals
\[
\rho_j=1+g_*q(x_j^2)(g_*-g_j)\in[0,1).
\]
These are statements about exact infinite discrete orbits, not finite experiments.

For **two** initially excited oscillators with \(0<\omega_1<\omega_2\), put \(r=(\omega_2/\omega_1)^2>1\) and \(t=(\omega_1h)^2\in(0,12/r)\). The *unique* threshold \(t_*\) is the smaller positive root of
\[
P_r(t)=r(r+1)t^2-(12r^2+20r+12)t+96(r+1)=0.
\]
For \(t<t_*\), energy flows asymptotically to the slower mode. At \(t=t_*\), the global relaxation preserves **each** modal energy separately. For \(t>t_*\), energy flows asymptotically to the faster mode. The threshold is thus necessary and sufficient throughout the specified \(0<t<12/r\) interval.

For the frequency ratio \((\omega_1,\omega_2)=(1,2)\),
\[
t_*=\frac{71-\sqrt{2641}}{10},\qquad t_{\mathrm{radial}}=\frac{168}{85},\qquad t_*<\frac{197}{100}<t_{\mathrm{radial}}<2.
\]
At the **same** stable RK4 base step \(h^2=197/100\), global *increment relaxation* selects the **fast** oscillator whereas ordinary *radial projection of the RK4 endpoint* selects the **slow** oscillator. These genuinely different total-energy conserving corrections can therefore have opposite infinite-time modal selection inside the standard RK4 imaginary-axis stability interval.

## Assumptions and scope

Fix any integer \(m\ge2\). Let \(J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}\) and consider \(\dot z_j=\omega_jJz_j\) on \(\mathbb R^{2m}\), with fixed \(\omega_j>0\). Work in exact real arithmetic with a constant RK4 base step \(h>0\). Define \(E_{j,n}=\|z_{j,n}\|_2^2\). At least one \(E_{j,0}\) must be positive; a mode of zero initial energy stays zero. The condition \(0<(h\omega_j)^2<12\) is imposed on all initially excited modes, and no assumption is needed for modes that are identically zero. Consider classical four-stage RK4 with stability polynomial
\[
R(s)=1+s+\frac{s^2}{2}+\frac{s^3}{6}+\frac{s^4}{24}.
\]
At each step compute its full predictor \(y=R(hA)z\) and increment \(d=y-z\), then select the **nonzero** scalar \(\gamma_n\) satisfying \(\|z+\gamma_nd\|_2^2=\|z\|_2^2\), and update \(z^+=z+\gamma_nd\). The trivial root \(\gamma_n=0\) is excluded. This is a *single global scalar* for all modes, not an independent scalar per mode; it acts along the RK increment, not along the RK endpoint. The numerical time associated with a relaxed update may be taken as the accumulated \(\gamma_nh\); our conclusions concern discrete step indices.

## Proof

**1. RK4 oscillatory reduction and nonzero positive relaxation.** With \(t=x^2\), the real and imaginary parts of \(R(ix)\) are \(a(t)=1-t/2+t^2/24\) and \(b(x)=x(1-t/6)\). Direct expansion gives
\[
|R(ix)-1|^2=q(t)=\frac{t(t^3-8t^2-48t+576)}{576}.
\]
The denominator polynomial is strictly positive for \(0<t<12\), because \(q(t)=|R(ix)-1|^2\), and the imaginary part could vanish only at \(t=6\), where \(a(6)-1=-3/2\ne0\). Also
\[
-\frac{2\operatorname{Re}(R(ix)-1)}{|R(ix)-1|^2}=g(t)=\frac{48(12-t)}{D(t)}>0\quad(0<t<12).
\]
The quadratic relaxation equation is
\[
0=2\gamma_n\langle z,d\rangle+\gamma_n^2\|d\|^2.
\]
Since \(\sum_jE_{j,n}q_j>0\), its unique nonzero root is strictly positive and equals
\[
\boxed{\quad\gamma_n=\frac{\sum_j E_{j,n}q_jg_j}{\sum_j E_{j,n}q_j},\qquad q_j=q(x_j^2)>0.\quad}
\]
It is a weighted mean of the active \(g_j\), so lies between their extreme values. The exact individual energy map is
\[
\boxed{\quad E_{j,n+1}=E_{j,n}\left(1+q_j\gamma_n(\gamma_n-g_j)\right).\quad}
\]
Each energy is a squared norm and hence nonnegative. Summing the identity and using the formula for \(\gamma_n\) proves exact conservation \(\sum_jE_{j,n}=E_{\mathrm{tot}}\).

**2. Strict global Lyapunov law and mode selection.** Define \(\Phi_n=\sum_jg_jE_{j,n}\). The energy map yields the exact nonpositive increment
\[
\boxed{\quad\Phi_{n+1}-\Phi_n=-\gamma_n\sum_j E_{j,n}q_j(g_j-\gamma_n)^2\le0.\quad}
\]
Equality holds exactly when every excited mode has the same \(g_j\). More constructively, let \(M=\{j:E_{j,0}>0,\ g_j=g_*\}\) and \(L=\{j:E_{j,0}>0,\ g_j>g_*\}\). Since \(\gamma_n\ge g_*\), the total winning energy \(E_{M,n}=\sum_{j\in M}E_{j,n}\) is nondecreasing, and its increment is
\[
E_{M,n+1}-E_{M,n}=\gamma_n(\gamma_n-g_*)\sum_{j\in M}q_jE_{j,n}.
\]
The right side is at least \(g_*q_{M,\min}E_{M,0}(\gamma_n-g_*)\), with strictly positive constant \(g_*q_{M,\min}E_{M,0}\). The left side tends to zero, because a bounded nondecreasing sequence has increments tending to zero. Thus \(\gamma_n\to g_*\). But the weighted-mean identity also gives
\[
\gamma_n-g_*=\frac{\sum_{j\in L}E_{j,n}q_j(g_j-g_*)}{\sum_jE_{j,n}q_j}.
\]
The denominator is bounded above by \(E_{\mathrm{tot}}\max_jq_j\), whereas every factor \(q_j(g_j-g_*)\) on \(L\) is strictly positive. Therefore \(E_{j,n}\to0\) for every \(j\in L\), and \(E_{M,n}\to E_{\mathrm{tot}}\). Within \(M\), the individual amplification factors may differ when the \(q_j\) differ, so their transient relative energies need not be fixed. The argument determines only the total winning energy, and makes no claim about fixed relative weights in a tied winning set. The losing-mode ratio is the displayed \(\rho_j\), obtained by substituting \(\gamma_n\to g_*\) into the exact factor. As that factor is a squared complex modulus it lies in \([0,1)\). If \(\rho_j>0\) the decay is asymptotically geometric; if \(\rho_j=0\), the ratio tends to zero. (A mode that becomes exactly zero stays zero; ratios are then read on positive-energy steps.)

**3. Sharp two-frequency switch.** On \(0<t<12\), the derivative is
\[
\frac{d}{dt}g(t)=\frac{96t(t-6)(t-16)}{D(t)^2}.
\]
Thus \(g\) rises until \(t=6\) then falls until \(t=12\), so distinct modal frequencies can cross in selection. Clearing positive denominators in \(g(t)=g(rt)\), after removing \((r-1)t>0\), gives precisely \(P_r(t)=0\). Since \(P_r(0)=96(r+1)>0\), \(P_r(12/r)=-48r<0\), and its leading coefficient is positive, its two roots are positive and exactly one lies in \((0,12/r)\). Continuity and the endpoint signs show \(g(t)<g(rt)\) below that root and \(g(t)>g(rt)\) above it. The selection law of step 2 therefore yields the stated three regimes. If \(g_1=g_2\), \(\gamma_n=g_1=g_2\) at every step and each modal multiplier has squared norm one, giving individual energy conservation. The smaller root has the explicit formula
\[
t_*=\frac{12r^2+20r+12-\sqrt{(12r^2+20r+12)^2-384r(r+1)^2}}{2r(r+1)}.
\]

**4. Comparison with a different correction.** For classical RK4, \(Q(t)=|R(i\sqrt t)|^2=1+t^3(t-8)/576\). Radial normalization of the full RK4 endpoint multiplies both modal energies by the same scalar and has ratio growth \(Q(rt)/Q(t)\); its switch at \(r=4\) is \(t_{\mathrm{radial}}=168/85\), as separately established in the cited projected-RK4 result. Our incremental relaxation, instead, follows the \(g\)-selection switch \((71-\sqrt{2641})/10\) at \(r=4\). One checks exactly
\[
\frac{71-\sqrt{2641}}{10}<\frac{197}{100}<\frac{168}{85}<2.
\]
At \(t=197/100\), \(P_4(t)=-931/500<0\), so \(g(t)>g(4t)\): the *higher* frequency receives all energy under increment relaxation. In contrast \(Q(t)>Q(4t)\), so the *lower* frequency receives all energy under radial projection. The larger squared frequency-step is \(4t=197/25<8\), hence both underlying RK4 modal factors lie strictly inside the standard stability disk. This comparison establishes different mathematical implications despite both methods conserving the same total norm.

## Verification

Execute `python verify.py` in the extracted package using only Python 3 standard-library modules. The script performs 127 passing checks: exact rational expressions for \(g,q,P_r\) and the contrasting thresholds, 16 exact-rational energy-map iterations, 15 direct four-stage RK4 versus modal-map cross-checks, and four long-time selection simulations. Successful output is exactly `VERIFY_OK 127 checks`. The all-step selection proof uses analytic identities and the bounded-monotone argument, not these finite checks.

## Relationship to prior work

Doehring, Ranocha and Torrilhon, *Paired Explicit Relaxation Runge–Kutta Methods* (arXiv:2507.04991v1, 2025-07-07), use common scalar relaxation on Runge–Kutta updates to control global mathematical entropy. The generic quadratic-invariant correction and positivity of a small-step nonzero root are therefore **not** claimed as new. The present theorem instead isolates classical RK4 and derives a new complete finite-dimensional long-time mode-selection law, its explicit Lyapunov function, and a unique two-mode switch throughout a non-infinitesimal admissible interval. The source is a paired multirate construction; the present RK4 specialization is not represented as an analysis of those optimized multirate coefficients.

Ranocha et al., *Relaxation Runge–Kutta Methods: Fully Discrete Explicit Entropy-Stable Schemes for the Compressible Euler and Navier–Stokes Equations* (2020), equations (2.2)–(2.6), and Ketcheson (2019) already describe relaxation along a Runge–Kutta increment. Most pertinently, Ketcheson (2019), §4.1, studies exactly classical relaxation RK4 on a Fourier spectral semi-discretization of transport, explicitly observes that some frequencies lose energy and others gain it, and plots finite-time modal amplitudes. The *existence* of artificial modal transfer and its association with global energy conservation are therefore known. Its discussion does not establish which modes collect all energy asymptotically for general data, an exact strict mode-selection Lyapunov law, or the two-frequency step threshold here. Our contribution is the complete asymptotic classification and sharp comparison with a different correction, not the observation of mode amplification itself.

A directly relevant published study, *A unique symplectic timestep and sharp modal-energy reversal in projected RK4* (published-finding corpus, October 18, 2026), solves the related **radial endpoint projection** problem; it implies the radial threshold \(168/85\) at \((\omega_1,\omega_2)=(1,2)\). Radial projection is different from scalar relaxation **along the increment**: their energy-ratio recursions are respectively fixed-ratio \(Q_2/Q_1\) and dynamically weighted \(1+q_j\gamma(\gamma-g_j)\). The explicit stable-step opposite-winner example here proves their conclusions do not substitute for one another. Results on stage-span quasi-orthogonal projections (arXiv:2409.18328) and fixed-step relaxation-free corrections (arXiv:2401.14508) likewise use different corrections.

## Limitations

The theorem requires a finite collection of independent harmonic modes, exact arithmetic, classical RK4, a single global quadratic invariant, and \(0<(h\omega_j)^2<12\) for excited modes; it is not an error theorem for arbitrary nonlinear systems, nor a theorem about paired multirate RK tableaux. A mode with zero initial energy never becomes excited. Ties for minimum \(g\) can occur for distinct frequencies, so the full limit distribution within a tied winning set is not classified. Although total energy is exactly conserved, individual modal energies can have gross long-time errors. Exceptional zero numerical multipliers can extinguish losing modes finitely. Floating-point rounding, nonnormal operators, noncommuting dynamics and adaptive base steps are outside the proof. Historical-priority searches cannot rule out every older equivalent statement, especially under different terminology.

## References

1. D. Doehring, H. Ranocha, and M. Torrilhon, *Paired Explicit Relaxation Runge–Kutta Methods: Entropy-Conservative and Entropy-Stable High-Order Optimized Multirate Time Integration*, arXiv:2507.04991v1, 2025-07-07; https://arxiv.org/abs/2507.04991; full text https://link.springer.com/article/10.1007/s42967-026-00587-6, §§2.4–3.
2. H. Ranocha et al., *Relaxation Runge–Kutta Methods: Fully Discrete Explicit Entropy-Stable Schemes for the Compressible Euler and Navier–Stokes Equations*, SIAM J. Sci. Comput. 42 (2020), pp. A612–A638, equations (2.2)–(2.6); https://math.umd.edu/~tadmor/references/files/Ranocha%20et%20al%20RRK%20and%20ES%20SISC2020.pdf.
3. D. I. Ketcheson, *Relaxation Runge–Kutta Methods: Conservation and Stability for Inner-Product Norms*, SIAM J. Numer. Anal. 57 (2019), 2850–2870, §§2, 4.1, https://arxiv.org/pdf/1905.09847, https://doi.org/10.1137/19M1263662.
4. M. R. Najafian and B. C. Vermeire, *Quasi-Orthogonal Runge-Kutta Projection Methods*, arXiv:2409.18328v1 (2024), https://arxiv.org/abs/2409.18328.
5. *A unique symplectic timestep and sharp modal-energy reversal in projected RK4*, published finding (2026-10-18), https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-a-unique-symplectic-timestep-and-sharp-modal-energy-reversal-in--3016d962c708.
