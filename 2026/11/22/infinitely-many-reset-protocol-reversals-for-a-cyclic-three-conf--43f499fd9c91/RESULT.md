# Infinitely many reset-protocol reversals for a cyclic three-conformation Brownian gate

## Finding

A Brownian particle searches a stochastically reactive boundary whose conformation cycles irreversibly through three states. At each Poisson reset, compare resetting only the particle's position (protocol P) with resetting its position **and** drawing a fresh stationary gate state (protocol J). Unlike the strictly ordered two-conformation case, these protocols repeatedly exchange which one has the smaller mean first-passage time as the starting/resetting distance increases.

More precisely, for all \(D,\gamma,r>0\) and \(a>0\), set
\[
\omega=e^{2\pi i/3},\quad \kappa=\gamma(1-\omega),\quad k_0=\sqrt{r/D},\quad k=\sqrt{(r+\kappa)/D},
\]
where both square roots have positive real part. Then the exact mean absorption times are
\[
T_J(a)=\frac{e^{k_0a}[1+2k_0\operatorname{Re}(1/k)]-1}{r},\qquad
T_P(a)=T_J(a)+2k_0\operatorname{Re}\left[\frac{e^{-(k-k_0)a}}{\kappa k}\right].
\]
Write \(k=u-iv\), with \(u>k_0\), \(v>0\), and \(\phi=\arg[1/(\kappa k)]\). Then \(\pi/6<\phi<\pi/4\) and
\[
T_P(a)-T_J(a)=\frac{2k_0}{|\kappa k|}\,e^{-(u-k_0)a}\cos(va+\phi).
\]
Thus the complete set of positive equality distances is
\[
a_n=\frac{\pi/2+n\pi-\phi}{v},\qquad n=0,1,2,\ldots.
\]
These roots are simple and equally spaced by \(\pi/v\). Protocol J is strictly faster for \(0<a<a_0\); thereafter the strict mean-time ordering alternates on each successive interval. These infinitely many reversals occur at every fixed positive choice of the three rates \(D,\gamma,r\), although their absolute advantage decreases exponentially at large distance.

## Assumptions and scope

The particle has continuous trajectories on \([0,\infty)\), Brownian generator \(D\partial_x^2\), and is started at \(X_0=a>0\). Independently, the gate \(G_t\in\{0,1,2\}\) follows the directed cycle \(0\to1\to2\to0\), each transition occurring at rate \(\gamma>0\). The gate starts independently from its unique uniform stationary distribution. At \(x=0\), state \(0\) is perfectly absorbing and states \(1,2\) are reflecting. The experiment terminates at the first absorption, including absorption when a gate switch opens while the reflected particle is at the boundary.

A further independent Poisson clock of rate \(r>0\) relocates the particle instantaneously to \(a\). Protocol P leaves the gate conformation unchanged at resets. Protocol J redraws the gate independently and uniformly at resets. Gate transitions between reset times are identical in both protocols. The results concern continuous-time mean first absorption times, not pointwise ordering of the complete absorption-time distributions. All rates and distance are strictly positive; the boundary starting case \(a=0\) is outside the theorem.

## Proof

**1. Finite means and uniqueness.** Let \(Q\) act on column vectors of functions of the gate, with \(Q_{01}=Q_{12}=Q_{20}=\gamma\), diagonal entries \(-\gamma\), and other entries zero. Let \(\pi=(1,1,1)/3\). On a fixed-length block, there is a uniformly positive probability, regardless of the incoming position or gate, that a reset relocates the particle to \(a\), followed by a sufficiently long reset-free interval during which the gate reaches state \(0\) and remains there, and the reflected Brownian particle reaches the origin. The strong Markov property gives a geometric tail at these block endpoints. Hence the mean absorption time is finite, and the bounded backward boundary-value solution is unique by the stopped Dynkin formula.

**2. Spectral ingredients.** Define the principal positive-real-part matrix square root \(K=\sqrt{(rI-Q)/D}\), and \(E(x)=e^{-Kx}\). The gate eigenvalues are \(0,-\kappa,-\bar\kappa\), with right eigenvectors \(\mathbf 1=(1,1,1)^T\), \(z=(1,\omega,\omega^2)^T\), and \(\bar z\). In particular,
\[
K\mathbf1=k_0\mathbf1,\quad Kz=kz,\quad K\bar z=\bar k\bar z,
\quad e_0=(\mathbf1+z+\bar z)/3.
\]
Here \(e_0=(1,0,0)^T\) is the open-gate selector.

**3. Joint resetting.** For the process *without* resets, the Laplace transform \(f_j(x)=\mathbb E_{x,j}(e^{-r\tau})\) of absorption solves \(Df''+Qf-rf=0\) with \(f_0(0)=1\), \(f'_1(0)=f'_2(0)=0\), and vanishing as \(x\to\infty\). The solution is \(f(x)=E(x)d\), where
\[
d=\frac{K^{-1}e_0}{e_0^TK^{-1}e_0},\qquad
\pi f(a)=\frac{e^{-k_0a}}{1+2k_0\operatorname{Re}(1/k)}.
\]
Since protocol J restarts both position and gate independently, the usual first-event renewal equation gives \(T_J=(1-\pi f(a))/(r\pi f(a))\), yielding the stated formula.

**4. Position-only resetting.** Write the three conditional means \(m(x)\) as a column vector. The backward problem is
\[
Dm''+Qm+r[m(a)-m(x)]=-\mathbf1,\quad
m_0(0)=0,\quad m'_1(0)=m'_2(0)=0.
\]
Boundedness permits \(m(x)=h+E(x)c\), with constant \(h\). The two reflecting boundary conditions imply \(Kc=t e_0\) for a scalar \(t\). The constant term of the differential equation reads \(Qh=-\mathbf1-rE(a)c\). Applying \(\pi\), which annihilates \(Q\), gives \(\pi E(a)c=-1/r\), hence
\[
t=-\frac{3k_0e^{k_0a}}r,\quad
c=-\frac{3k_0e^{k_0a}}rK^{-1}e_0,
\quad c_0=-\frac{e^{k_0a}}r[1+2k_0\operatorname{Re}(1/k)].
\]
For the nonconstant gate modes, the equation for \(h\) has coefficients
\[
h_z=-\frac{k_0e^{k_0a-ka}}{\kappa k},\qquad
h_{\bar z}=\overline{h_z}.
\]
The absorbing boundary condition forces \(h_0=-c_0\), so the stationary mean of the constant vector is \(\pi h=-c_0-h_z-h_{\bar z}\). Finally \(T_P(a)=\pi m(a)=\pi h-1/r\), giving
\[
T_P(a)-T_J(a)=-h_z-h_{\bar z}
=2k_0\operatorname{Re}\left[\frac{e^{-(k-k_0)a}}{\kappa k}\right].
\]
This derivation proves the formula globally, rather than extrapolating from a finite number of sign changes.

**5. Sharp phase and zero classification.** Since \(\kappa=\gamma(3-i\sqrt3)/2\), its argument is \(-\pi/6\). Because \(r>0\), \(\arg(r+\kappa)\) is strictly between \(-\pi/6\) and zero. Consequently \(\arg k\in(-\pi/12,0)\), yielding \(\pi/6<\phi<\pi/4\), \(v>0\) and \(u>k_0\). The positive prefactor cannot vanish. Its cosine factor has precisely the simple zeros stated, and its initial sign is positive. The oscillation never terminates at finite distance.

## Verification

Run `python verify.py` with Python 3, NumPy and SciPy. The standalone script checks the scalar formulas against an independently assembled real matrix-square-root boundary-value solution over a three-parameter grid; checks positivity, phase bounds, zero identities, and post-zero signs; and discretizes the original coupled absorbing/reflecting backward equations on a large finite interval with two distinct reset operators. At \(D=r=\gamma=1\), the independent discretization gives protocol P slower near \(a=1\) and faster near \(a=5\). The script reports 1,221 passing assertions. Finite-domain and finite-grid tests are corroboration, not proof of the infinite-distance theorem.

## Relationship to prior work

The two-state gate with joint position/gate refreshing is treated in Bressloff (2020); the corresponding position-only reset problem and a direct comparison are treated by Mercado-Vásquez and Boyer (2021), especially their Appendix B, equation (49). For an irreducible two-state gate that comparison gives strict advantage to refreshing both variables and contains no distance-order reversal. Thus the present directed three-conformation example is a genuinely different mechanism, not a rephrasing of the published two-state formula. The general gated first-passage framework of Scher and collaborators (2022/2024) addresses Markovian gating but does not compare both reset operators in a directed three-state gate. The more recent renewal framework of Bressloff (2026), sections 2–3, derives two-state gate identities and discusses the difference between complete and partial resetting, but does not state a three-state cyclic protocol comparison or the infinitely repeated distance ordering. Earlier general stochastic-gating theory provides methodological context; applying linear spectral methods is not claimed as new.

## Limitations

The result treats one irreversible, equal-rate, three-state directed cycle with exactly one absorbing conformation; it does not classify every three-state Markov gate. Equality distances become exponentially hard to distinguish by noisy finite-sample observations as \(a\) grows, and no finite-data identifiability guarantee is asserted. The model assumes independent Poisson resetting and stationary gate initialization, with instantaneous reflecting and absorbing boundary behavior. Related general formulas may implicitly yield the result; the literature comparison does not establish publication priority beyond the sources inspected, and independent scientific review remains outstanding.

## References

- P. C. Bressloff, “Diffusive search for a stochastically-gated target with resetting” (first public 2020-09-06), https://arxiv.org/abs/2009.02739 .
- G. Mercado-Vásquez and D. Boyer, “Search of stochastically gated targets with diffusive particles under resetting” (first public 2021-07-05), https://arxiv.org/abs/2107.02148 ; specifically section 2, section 3, and Appendix B.
- Y. Scher, A. Kumar, M. S. Santhanam and S. Reuveni, “Continuous Gated First-Passage Processes” (first public 2022-11-16), https://arxiv.org/abs/2211.09164 ; especially sections 2–4 and conclusions.
- P. C. Bressloff, “Renewal theory for Brownian motion with stochastically gated targets” (first public 2026-01-04), https://arxiv.org/abs/2601.01588 ; specifically sections 2–3.
