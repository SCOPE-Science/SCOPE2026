# A unique three-energy sign crossover under heterogeneous global resetting

## Finding

**Theorem.** Consider any finite family of at least three independently driven Ornstein–Uhlenbeck particles in harmonic traps, all instantaneously reset to the origin at the same Poisson times. For any three *distinct* labels, their stationary quadratic energies have strictly positive pair covariances, but the connected three-energy correlation changes sign **exactly once** as the common resetting rate increases. Unequal relaxation rates strictly lower the crossover rate at fixed total relaxation strength.

For the selected labels \(i=1,2,3\), write \(\omega_i=2\lambda_i>0\), \(\vartheta_i=D_i/2>0\), and
\[
 s=\omega_1+\omega_2+\omega_3,\qquad
 p=\omega_1\omega_2+\omega_1\omega_3+\omega_2\omega_3,\qquad
 q=\omega_1\omega_2\omega_3.
\]
The connected third-order cumulant of their stationary energies \(H_i=\lambda_iX_i^2/2\) is
\[
 \boxed{\kappa(H_1,H_2,H_3)=
 \frac{\vartheta_1\vartheta_2\vartheta_3\,r q
 \bigl(2r^3+2sr^2-sp+q\bigr)}
 {(r+s)\prod_{i=1}^{3}(r+\omega_i)\prod_{1\le i<j\le3}(r+\omega_i+\omega_j)}.}
\]
Here \(\kappa(H_1,H_2,H_3)=\mathbb E[H_1H_2H_3]-\sum_{\mathrm{cyc}}\mathbb E[H_iH_j]\mathbb E[H_k]+2\prod_i\mathbb E[H_i]\). There is a unique positive rate \(r_*\) specified by
\[
 \boxed{2r_*^3+2sr_*^2=sp-q.}
\]
The connected three-energy cumulant is negative for \(0<r<r_*\), zero at \(r=r_*\), and positive for \(r>r_*\). In contrast, for each distinct pair
\[
 \boxed{\operatorname{Cov}(H_i,H_j)=
 \frac{\vartheta_i\vartheta_j\,r\omega_i\omega_j}
 {(r+\omega_i)(r+\omega_j)(r+\omega_i+\omega_j)}>0.}
\]
Indeed, the *entire finite-dimensional stationary energy field is associated*: any two coordinatewise nondecreasing square-integrable observables have nonnegative covariance.

The crossover is a strictly Schur-concave function of the three relaxation frequencies: at fixed \(s\), any nontrivial balancing of two unequal frequencies raises \(r_*\). The sharp bounds are
\[
 \min_i\omega_i<r_*<s/3
 \quad\text{if the frequencies are not all equal},
 \qquad r_*=\omega_1\quad\text{if all are equal}.
\]
For example \((\omega_1,\omega_2,\omega_3)=(1,2,3)\) gives \(r_*=1.94338091256\ldots\), strictly below the equal-frequency threshold \(2\) at the same sum. The equal-frequency slice follows from the established homogeneous common-reset beta energy law; the **heterogeneous universal cubic classification and strict anisotropy ordering**, not the homogeneous slice, are the assessed contribution.

## Assumptions and scope

Fix any integer \(N\ge3\), positive finite diffusivities \(D_i>0\), relaxation rates \(\lambda_i>0\), and global reset rate \(r>0\). Between reset events each coordinate obeys
\[
 dX_i(t)=-\lambda_i X_i(t)\,dt+\sqrt{2D_i}\,dW_i(t),
 \qquad i=1,\ldots,N,
\]
with independent standard Brownian motions. A single independent rate-\(r\) Poisson clock sends *every* coordinate to zero at each of its jumps. Observations are made in the unique stationary regime. The result concerns distinct labels, not repeated-index cumulants. The trap relaxation frequencies can differ arbitrarily. No particle interactions, shared thermal noises, nonzero reset positions, or local reset clocks are assumed. The normalized quadratic energies are \(H_i=\lambda_i X_i^2/2\); multiplication by any strictly positive coordinatewise energy scale leaves all stated signs unchanged.

## Proof

**1. Exact stationary representation.** Two copies driven by the same Brownian paths and global clock coalesce at their first common reset, so the process has one invariant law and converges to it from any initial state in total variation at least as rapidly as the no-reset probability \(e^{-rt}\). In stationary time, the age \(A\) since the latest reset is exponential of rate \(r\), independent of all post-reset Brownian increments. Solving the linear SDE from zero gives, conditionally on \(A=a\), independent centered Gaussians of variance \((D_i/\lambda_i)(1-e^{-2\lambda_i a})\). Thus the stationary energies admit the joint representation
\[
 (H_1,\ldots,H_N)\stackrel{d}{=}
 \bigl(\vartheta_i(1-e^{-\omega_iA})Z_i^2\bigr)_{i=1}^N,
\]
where \(Z_i\) are independent standard Gaussians, independent of \(A\). The conditional mean is \(m_i(a)=\vartheta_i(1-e^{-\omega_i a})\). This also proves existence and finiteness of all stationary energy moments.

**2. The cross-cumulant reduction.** Conditional on \(A\), distinct energies are independent, hence every distinct-label subset moment equals the corresponding subset moment of \((m_i(A))\). Mixed cumulants use only such subset moments, so the connected cumulant of distinct energies equals that of their conditional means. Set \(U_i=e^{-\omega_i A}\). Since cumulants of order at least two are invariant under adding constants and multilinear,
\[
 \operatorname{Cov}(H_i,H_j)=\vartheta_i\vartheta_j\operatorname{Cov}(U_i,U_j),
 \qquad\kappa(H_1,H_2,H_3)=-\vartheta_1\vartheta_2\vartheta_3\kappa(U_1,U_2,U_3).
\]
For every \(z\ge0\), \(\mathbb E[e^{-z A}]=r/(r+z)\). The pair-covariance expression is therefore \(r/(r+\omega_i+\omega_j)-r^2/((r+\omega_i)(r+\omega_j))\), whose reduction yields the strictly positive displayed formula.

**3. Closed three-body factorization.** Let \(a=\omega_1,b=\omega_2,c=\omega_3\) and \(\phi(z)=r/(r+z)\). The defining cumulant polynomial gives
\[
 \kappa(U_1,U_2,U_3)=\phi(a+b+c)
 -\phi(a+b)\phi(c)-\phi(a+c)\phi(b)-\phi(b+c)\phi(a)
 +2\phi(a)\phi(b)\phi(c).
\]
Combining these seven rational terms over their common strictly positive denominator yields the exact identity
\[
 \kappa(U_1,U_2,U_3)=
 -\frac{rabc\,[2r^3+2(a+b+c)r^2-(a+b+c)(ab+ac+bc)+abc]}
 {(r+a)(r+b)(r+c)(r+a+b)(r+a+c)(r+b+c)(r+a+b+c)}.
\]
The preceding minus sign from \(H_i=\vartheta_i(1-U_i)\) produces the boxed energy cumulant. This algebraic identity is independently checked in `symbolic_check.py`; the rational generator recursion in `check.py` independently reconstructs the subset moments.

**4. Exactly one crossover.** The polynomial \(P(r)=2r^3+2sr^2-sp+q\) has \(P'(r)=6r^2+4sr>0\) for every \(r>0\). Its initial value is negative because \(sp-q\) is the positive sum of the six mixed cubic monomials plus twice \(abc\), and \(P(r)\) tends to infinity. Therefore exactly one simple positive zero exists and controls all three signs, including the equality case. No numerical root search is used to justify uniqueness.

**5. Strict anisotropy ordering and sharp bounds.** Write \(F=sp-q\); the root is determined by the strictly increasing map \(r\mapsto2r^3+2sr^2\) when \(s\) is fixed. Holding \(c\) and \(a+b=t\) fixed, one has
\[
 F=(t+c)(ab+tc)-abc=t\,ab+t c(t+c).
\]
Any nontrivial averaging of unequal \(a,b\) increases their product \(ab\), hence strictly increases \(F\) and \(r_*\). Successive pair-averaging operations prove strict Schur concavity. Thus \(F\) is maximized at equal frequencies, where \(F=8s^3/27\) and \(r_*=s/3\); the upper bound and its equality condition follow.

For the lower bound write, after relabeling, \(a=m,b=m+x,c=m+y\), with \(m=\min_i\omega_i>0\) and \(x,y\ge0\). Direct expansion gives
\[
 F-2sm^2-2m^3
 =6m^2(x+y)+2m(x^2+3xy+y^2)+xy(x+y).
\]
This is strictly positive unless \(x=y=0\), so \(P(m)<0\) unless all rates agree; hence \(m<r_*\) for heterogeneous rates. The equal-frequency case has \(r_*=m\). These bounds are sharp: balancing gives equality at the upper edge, while the lower bound is approached as all frequencies converge to their minimum.

**6. Association despite negative third connected correlations.** Using the joint representation from step 1, the energy vector is a coordinatewise increasing function of the independent variables \(A,Z_1^2,\ldots,Z_N^2\). The elementary product-measure association inequality (proved by iterated one-dimensional covariance positivity) shows that any two bounded coordinatewise increasing functions of these independent variables have nonnegative covariance. Applying it to increasing observables of the energy vector and extending by truncation to square-integrable observables proves the assertion. Association imposes no sign restriction on a *third* connected cumulant, and is therefore consistent with its strict negative region.

## Verification

Execute `python3 check.py` (standard library only) and `python3 symbolic_check.py` (SymPy required) from the same directory. In the recorded execution, the first passed 6,082 exact-rational assertions across 550 seeded parameter combinations, using the stationary Markov generator's subset-moment recursion rather than the last-reset integral. The second passed four symbolic polynomial identities: full three-body factorization, equal-frequency formula, lower-bound expansion, and the pair-averaging identity. The analytic steps above, not finitely many assertions, establish the theorem for every allowed parameter value. No simulation, numerical quadrature, or independent external certification is used to support unrestricted universal claims.

## Relationship to prior work

Biroli, Larralde, Majumdar and Schehr (arXiv:2211.00563, first public 2022-11-01) derive the common-age joint law and a strictly positive *pair* squared-displacement covariance for simultaneously reset **unconfined** Brownian particles. Their full text establishes the renewal starting point but not the harmonic three-body sign transition.

Olsen (arXiv:2310.04840, first public 2023-10-07) gives exact **single-particle** harmonic reset moment hierarchies and discusses the sign of a scalar *third cumulant of position* when resetting to a nonzero distribution. This does not determine a three-*distinct-mode* mixed energy cumulant under one shared clock; its general renewal method is acknowledged as prior.

Bressloff (arXiv:2401.03501, first public 2024-01-07), especially Sec. IV, derives globally reset noninteracting-particle density equations and two-point correlation hierarchies; its general model and moment-generation framework are stronger background, but it does not evaluate the unequal-trap three-energy sign diagram. Its joint equations can be specialized to recover the raw moments after further calculation; the method and raw-moment representation are **not** claimed as new.

A previously published result, *A beta-law for macroscopic energy in globally reset harmonic Brownian gases* (2026), establishes the same shared-age Gaussian/chi-square energy law for **homogeneous** mode relaxation rates, from which the equal-frequency three-body case follows. That boundary case is **covered**, not separately counted as an original discovery. The new mathematical statement assessed here is the sharp arbitrary-unequal-frequency cubic sign law and its strict fixed-sum Schur ordering.

A related three-particle result for a **randomly switching common harmonic trap** also has positive pair energy correlations and a one-crossing cubic phase diagram, but it has no stochastic resets: each particle continuously experiences the shared two-state stiffness modulation. Its switching-speed crossover is neither the present full-reset clock nor a specialization of its separate-three-frequency formula. The shared qualitative sign reversal is not claimed as novel in itself. The contribution assessed here is the exact fully resetting, independently confined three-rate law and its fixed-sum Schur ordering.

Two related results, *Alternating connected-energy correlations under heterogeneous all-but-one resetting* (2026) and *Anisotropy raises the unique cross-energy correlation threshold for a trapped run-and-tumble particle* (2026), concern respectively **free** diffusion with a randomly exempt particle at each reset and an **orientation-redrawing** particle with two-axis *pair* correlations. Neither statement, nor their inspected proofs, covers the present fully resetting, harmonically confined three-body cumulant. In particular, the sign of the anisotropy effect in the latter model is opposite here, because the physical dependencies differ.

## Limitations

The theorem assumes independent Gaussian thermal drivers, harmonic confinement, simultaneous complete Poisson resetting to zero, a common constant reset rate, and distinct labeled energy observables. It does not extend automatically to partial resets, interacting particles, non-Gaussian noise, nonlinear traps, unequal reset clocks, or finite-time correlations. The crossover is a change in sign of a stationary third-order *connected statistic*, not a singular thermodynamic phase transition. The general renewal approach, homogeneous beta-law, and pair-correlation mechanism are established prior work; only the parameter-uniform heterogeneous classification and strict ordering are assessed as new. A more general unpublished or unindexed mixed-moment theorem could imply the exact sign classification and remains a publication-priority risk; the available comparison does not constitute worldwide priority certification. There has been no independent scientific audit.

## References

1. M. Biroli, H. Larralde, S. N. Majumdar and G. Schehr, *Extreme statistics and spacing distribution in a Brownian gas correlated by resetting*, arXiv:2211.00563 (first posted 2022-11-01), https://arxiv.org/abs/2211.00563.
2. K. S. Olsen, *Steady-state moments under resetting to a distribution*, arXiv:2310.04840 (first posted 2023-10-07), https://arxiv.org/abs/2310.04840.
3. P. C. Bressloff, *Global density equations for interacting particle systems with stochastic resetting: from overdamped Brownian motion to phase synchronization*, arXiv:2401.03501 (first posted 2024-01-07), https://arxiv.org/html/2401.03501v2.
4. *A beta-law for macroscopic energy in globally reset harmonic Brownian gases*, https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-a-beta-law-for-macroscopic-energy-in-globally-reset-harmonic-bro--e140ac2fc363/RESULT.md.
5. *Alternating connected-energy correlations under heterogeneous all-but-one resetting*, https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-alternating-connected-energy-correlations-under-heterogeneous-al--f771955abc35/RESULT.md.
6. *Anisotropy raises the unique cross-energy correlation threshold for a trapped run-and-tumble particle*, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-anisotropy-raises-the-unique-cross-energy-correlation-threshold--c7257b4e8112/RESULT.md.
