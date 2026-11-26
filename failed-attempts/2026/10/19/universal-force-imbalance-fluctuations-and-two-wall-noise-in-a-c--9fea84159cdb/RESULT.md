# Universal force-imbalance fluctuations and two-wall noise in a confined run-and-tumble gas

## Finding

A confined non-diffusive run-and-tumble particle presses on either of two hard walls while its propulsive orientation points outward. The stationary **mean** wall contact is a familiar part of the active-gas equation of state. The result below instead determines the joint long-time fluctuations of the two wall-contact forces and their signed large deviations.

For every box length \(\ell>0\), speed \(v>0\), and independent orientation-flip rate \(\lambda>0\), define the dimensionless confinement parameter \(z=\lambda\ell/v\). Let \(R_t\) and \(L_t\) be the indicators of the particle being stuck, respectively, at the right and left walls. If the process is started in its unique stationary law, then

\[
\lim_{T\to\infty}\frac{1}{T}
\operatorname{Cov}\!\left(
\begin{pmatrix}\int_0^T R_t\,dt\\\int_0^T L_t\,dt\end{pmatrix}
\right)
=\frac{1}{12\lambda(1+z)^3}
\begin{pmatrix}
4z^3+12z^2+9z+3 & -(2z^3+6z^2+9z+3)\\
-(2z^3+6z^2+9z+3) & 4z^3+12z^2+9z+3
\end{pmatrix}.
\]

In particular, the integrated *signed* wall-contact time \(A_T^- =\int_0^T(R_t-L_t)\,dt\) has exactly the same long-time scaled cumulant generating function as an unconfined telegraph orientation:

\[
\lim_{T\to\infty}\frac1T\log\mathbb E\exp(\theta A_T^-)
=\sqrt{\lambda^2+\theta^2}-\lambda
\quad\text{for every }\theta\in\mathbb R.
\]

This holds for **every** \(v\) and \(\ell\); equivalently, the average signed contact \(A_T^-/T\) obeys a large-deviation principle with speed \(T\) and rate function

\[
I_-(a)=
\begin{cases}
\lambda\bigl(1-\sqrt{1-a^2}\bigr),& |a|\le1,\\
+\infty,&|a|>1.
\end{cases}
\]

The complementary *total* contact time \(A_T^+=\int_0^T(R_t+L_t)\,dt\) has a confinement-dependent asymptotic variance rate:

\[
\lim_{T\to\infty}\frac{\operatorname{Var}(A_T^-)}T=\frac1\lambda,
\qquad
\lim_{T\to\infty}\frac{\operatorname{Var}(A_T^+)}T
=\frac{z^2(z+3)}{3\lambda(1+z)^3}.
\]

The second coefficient is strictly increasing with \(z\) and approaches \(1/(3\lambda)\) as \(z\to\infty\), even though the stationary total wall occupancy tends to zero. More precisely, the infinite-box and long-observation-time limits of the normalized variance **do not commute**:

\[
\lim_{\ell\to\infty}\lim_{T\to\infty}\frac{\operatorname{Var}(A_T^+)}T=\frac1{3\lambda},
\qquad
\lim_{T\to\infty}\lim_{\ell\to\infty}\frac{\operatorname{Var}(A_T^+)}T=0.
\]

The same noncommutation holds for \(A_T^-\), with the respective values \(1/\lambda\) and \(0\). All statements take the flip rate, propulsion speed, and number of particles fixed; no simultaneous thermodynamic/time limit is asserted.

## Assumptions and scope

The state consists of the position \(X_t\in[0,\ell]\) and orientation \(\sigma_t\in\{-1,+1\}\). The orientation flips at the events of an independent homogeneous Poisson process of rate \(\lambda\). In the open interval the position moves deterministically at \(\dot X_t=v\sigma_t\). At \(X_t=\ell\) with \(\sigma_t=+1\), or \(X_t=0\) with \(\sigma_t=-1\), it stays attached without moving until the next orientation flip; it then immediately travels inward. There is no translational Brownian noise, absorption, interaction, or instantaneous specular reversal. This *sticking-until-tumble* convention is essential: a different reflecting boundary rule gives a different force observable.

The boundary indicators are precisely

\[
R_t=\mathbf 1_{\{X_t=\ell,\,\sigma_t=+1\}},\qquad
L_t=\mathbf 1_{\{X_t=0,\,\sigma_t=-1\}}.
\]

The instantaneous force on a wall is the propulsion-force magnitude \(F_0>0\) times the corresponding contact indicator; the net oriented force on the pair of walls is \(F_0(R_t-L_t)\). Thus all covariance-rate formulas for physical forces are multiplied by \(F_0^2\), and the signed-force cumulant generating function is obtained by replacing \(\theta\) by \(F_0\theta\). For \(N\) independent identically prepared particles, cumulant generating functions and covariance rates are multiplied by \(N\). No interparticle forces or wall motion is included.

A stationary bulk density exists on each orientation branch and has value

\[
p=\frac{\lambda}{2(v+\lambda\ell)}.
\]

Each wall has stationary point mass

\[
q=\frac{v}{2(v+\lambda\ell)}=\frac1{2(1+z)}.
\]

Consequently \(\mathbb E R_t=\mathbb E L_t=q\), and the stationary total contact probability is \(2q=(1+z)^{-1}\). The stationary law is uniquely ergodic with exponentially integrable correlations; long-time covariance integrals below are well-defined.

## Proof

**1. Exact force-balance coboundary.** At every regular time the following identity holds, including on both stuck branches:

\[
\dot X_t=v(\sigma_t-R_t+L_t).
\]

Since \(X_t\) is continuous and piecewise linear, integration yields the **pathwise** relation

\[
A_T^- = \int_0^T\sigma_t\,dt -\frac{X_T-X_0}{v},
\qquad
\left|A_T^- -\int_0^T\sigma_t\,dt\right|\le\frac\ell v.
\]

In particular, the difference is uniformly bounded for every trajectory and observation time. If \(B_T=\int_0^T\sigma_t\,dt\), for any real \(\theta\)

\[
e^{-|\theta|\ell/v}\,\mathbb E e^{\theta B_T}
\le\mathbb E e^{\theta A_T^-}
\le e^{|\theta|\ell/v}\,\mathbb E e^{\theta B_T}.
\]

For the two-state orientation alone, the tilted generator is

\[
Q_\theta=
\begin{pmatrix}
-\lambda+\theta & \lambda\\
\lambda & -\lambda-\theta
\end{pmatrix}
\]

with eigenvalues \(-\lambda\pm\sqrt{\lambda^2+\theta^2}\). Its top eigenvalue is simple and dominates the moment generating function from either initial orientation, hence yields the claimed scaled cumulant generating function. The uniform pathwise discrepancy makes the time-averaged observables \(A_T^-/T\) and \(B_T/T\) exponentially equivalent: for any \(\epsilon>0\), their difference is surely smaller than \(\epsilon\) once \(T>\ell/(v\epsilon)\). The standard two-state tilted-generator large-deviation principle therefore transfers unchanged. The Legendre transform of the top eigenvalue is the stated \(I_-\) on \([-1,1]\), including both endpoints by continuity, and infinite off this interval.

The second derivative at the origin of the scaled cumulant generating function is \(1/\lambda\). For completeness, the variance-rate identity also follows directly from the pathwise relation and the bounded displacement, since \(\operatorname{Var}B_T=O(T)\): the variance of the displacement correction is \(O(1)\), and its covariance with \(B_T\) is \(O(\sqrt T)\). Thus \(T^{-1}[\operatorname{Var}A_T^- -\operatorname{Var}B_T]\to0\). The orientation covariance is \(\operatorname{Cov}(\sigma_0,\sigma_t)=e^{-2\lambda t}\), giving the variance rate \(2\int_0^\infty e^{-2\lambda t}dt=1/\lambda\).

**2. Stationary law and existence of covariance integrals.** Stationary current conservation in the interior gives \(v(p_+-p_-)=0\), so \(p_+=p_-\). The stationary bulk equations make them constant. Balance between the incoming bulk flux \(vp\) and flipping of outward wall orientations \(\lambda q\) gives \(vp=\lambda q\); normalization \(2\ell p+2q=1\) gives the stated \(p,q\).

Uniform ergodicity is elementary. Fix a time \(\tau>0\). Irrespective of the initial position and sign, the probability that \(\sigma_\tau=+1\) is at least \((1-e^{-2\lambda\tau})/2\). With the additional event of no flips for the next \(\ell/v\) time units, the particle is in the right-wall stuck state at the deterministic time \(\tau+\ell/v\). This supplies a uniform positive minorization by a point mass, hence exponential mixing of the state process. In particular, the stationary Green–Kubo integrals and Poisson resolvents exist.

**3. Poisson equation for right-wall contact.** For a state function \(f\), the backward generator in the open interval is

\[
(\mathcal L f)_\pm(x)=\pm v\,\partial_x f_\pm(x)
+\lambda(f_\mp(x)-f_\pm(x)).
\]

At the right stuck wall, \((\mathcal L f)_R=\lambda(f_-(\ell)-f_R)\), with \(f_R=f_+(\ell)\). At the left stuck wall, \((\mathcal L f)_L=\lambda(f_+(0)-f_L)\), with \(f_L=f_-(0)\).

Solve \(-\mathcal L\phi=R-q\). Adding an arbitrary common constant is harmless. Choosing the constant to set \(\phi_+(0)=0\), the explicit solution is

\[
\phi_+(x)=\frac{2q}{v}x+\frac{\lambda q}{v^2}x^2,
\qquad
\phi_-(x)=-\frac q\lambda+\frac{\lambda q}{v^2}x^2.
\]

Substitution into both bulk generator equations gives \(\mathcal L\phi=q\), and substitution at the walls gives \(\mathcal L\phi=q-1\) on the right and \(\mathcal L\phi=q\) on the left. Hence this is an exact Poisson solution with the appropriate glued boundary values.

Its mean under the stationary law is

\[
\overline\phi=\frac{2z^3+6z^2+3z-3}{12\lambda(1+z)^2}.
\]

The stationary Green–Kubo formula gives

\[
G_{RR}:=\int_0^\infty\!\operatorname{Cov}(R_0,R_t)\,dt
= q\bigl(\phi_+(\ell)-\overline\phi\bigr)
=\frac{4z^3+12z^2+9z+3}{24\lambda(1+z)^3}
\]

and

\[
G_{LR}:=\int_0^\infty\!\operatorname{Cov}(L_0,R_t)\,dt
=q\bigl(\phi_-(0)-\overline\phi\bigr)
=-\frac{2z^3+6z^2+9z+3}{24\lambda(1+z)^3}.
\]

Reflection of the stationary process through the box midpoint exchanges its two wall states. Therefore \(G_{LL}=G_{RR}\) and \(G_{RL}=G_{LR}\), even without assuming time reversibility. The stationary integrated covariance rate equals twice the integrated covariance, yielding the displayed matrix. Algebra gives \(4(G_{RR}-G_{LR})=1/\lambda\) and \(4(G_{RR}+G_{LR})=z^2(z+3)/[3\lambda(1+z)^3]\), agreeing with the coboundary calculation independently.

**4. Confinement dependence and order of limits.** Differentiating the dimensionless total-contact variance coefficient gives

\[
\frac{d}{dz}\frac{z^2(z+3)}{3(1+z)^3}=\frac{2z}{(1+z)^4}>0.
\]

Thus its range for finite \(z>0\) is \((0,1/3)\), so the total-contact variance rate increases from zero to \(1/(3\lambda)\) as \(z\) grows. For the reversed order of limits, at fixed \(T\), \(0\le A_T^+\le T\) and \(\mathbb E A_T^+=T/(1+z)\). Consequently \(\operatorname{Var}(A_T^+)\le\mathbb E[(A_T^+)^2]\le T^2/(1+z)\to0\) as \(\ell\to\infty\). The same domination applies to \(A_T^-\), because \(|A_T^-|\le A_T^+\). This proves both claimed failures of commuting limits, with \(T\to\infty\) taken only after each fixed-\(T\) limit in the second ordering.

**5. Independent particles.** For \(N\) independent particles sharing the same fixed walls but not interacting, their additive wall contact functionals are sums of independent copies. Exact factorization of moment generating functions and additivity of covariances multiply the single-particle scaled cumulant generating functions and variance matrices by \(N\). This does not assert the same formula for interacting systems.

## Verification

The accompanying standalone `verify.py` uses a distinct discretization of the piecewise-deterministic dynamics: inward-directed hopping at rate \(v/h\) on a finite lattice, independent orientation flips at rate \(\lambda\), and zero hopping away from the box at its two endpoints. It solves the stationary generator and the finite-state Poisson equation for wall occupation, then compares their Green–Kubo integrals with the continuous formulas. For three separate positive parameter triples and four refinements (24, 48, 96, 192 intervals), the absolute errors systematically decrease with grid spacing, with the final sums of two absolute Green–Kubo errors respectively approximately \(2.17\cdot10^{-4}\), \(6.18\cdot10^{-4}\), and \(2.16\cdot10^{-3}\). These are convergence checks rather than proof of an infinite-dimensional limit.

The script also computes leading eigenvalues of six independently tilted finite-volume generators at two parameter triples and three refinements, converging to \(\sqrt{\lambda^2+\theta^2}-\lambda\). Its largest final displayed error is approximately \(1.03\cdot10^{-3}\). Exact symbolic rational-function checks independently verify the signed and total covariance identities and the monotonicity derivative. Run `python verify.py` with NumPy, SciPy and SymPy installed.

The mathematical theorem itself is proved analytically above. The numerical computations neither substitute for that proof nor demonstrate originality.

## Relationship to prior work

Li, Eichhorn and Dabelow (arXiv:2610.01287v1, first public October 1, 2026) give a new finite-box active ideal gas law, exact for one-dimensional RTPs, motivating the examination of fluctuations beyond a mean wall pressure. The publicly indexed abstract and submission history were accessible; the full source could not be inspected in this work. Its possible additional discussion of force fluctuations is therefore an explicit coverage risk. The present theorem applies only to the precisely defined athermal sticky-hard-wall two-velocity model, not automatically to all active-gas models analyzed there.

Angelani (2017, DOI:10.1088/1751-8121/aa734c; freely available as arXiv:2206.03123) studies exactly the same sticky hard-wall boundary convention and establishes the one-time wall distribution, pressure and transient average pressure; these ingredients are explicitly prior work. Full-text comparison of its Sections II–VI (including equations for the wall-pressure transient) did not reveal a two-time wall-force covariance or an integrated signed-force large-deviation law. Bressloff (arXiv:2508.20473) thoroughly distinguishes nonsticky from sticky boundary conventions in the zero-diffusion limit and analyzes weighted boundary local times and first-passage questions; its sections 2, 3 and 5 do not state the two-wall stationary covariance matrix or the signed-force large-deviation invariance above. Mukherjee, Le Doussal and Smith (arXiv:2405.07032v1) give large deviations for the local and interval occupation time of RTPs on unbounded domains, not the **signed hard-wall force difference** under stationary compact confinement. Roberts and Pruessner (arXiv:2206.06105, DOI:10.1103/PhysRevResearch.4.033234) solve a **boundary-only** tumbling particle model with additional diffusion, so their particle generator does not coincide with the present bulk-flipping process.

The full literature of general additive-functional large deviations, reflected telegraph processes and Green–Kubo theory supplies methods capable of implying portions of the result after a suitable specialization. The contribution assessed here is their explicit, combined consequence for the two physical wall-force observables: a closed two-wall covariance matrix, exact force-imbalance large-deviation invariance, and noncommuting size/time limits. No claim of a new general large-deviation principle or a new telegraph-process formula is made.

## Limitations

The infinite-barrier convention prescribes attachment until an orientation flip. Instantaneous specular reversal, finite wall softness, boundary-dependent tumble rates, bulk translational diffusion, asymmetric self-propulsion, wall movement and particle interactions are outside the proof. Physical force requires an externally chosen propulsion-force scale. The order-of-limits statements assume fixed \(v,\lambda>0\) and stationary initialization at each finite size. The October 2026 source that motivated the calculation was accessible only through its abstract, with its detailed results unavailable for exhaustive full-text comparison. Even though the closest 2017 source was examined in full, broader general reflected-telegraph additive-functional literature may implicitly entail some conclusions. Results are mathematically demonstrated here, but independent expert validation has not been performed.

## References

- S. Li, R. Eichhorn, L. Dabelow, *Ideal gas of active particles in a box*, arXiv:2610.01287v1 (2026-10-01), https://arxiv.org/abs/2610.01287 .
- L. Angelani, *Confined run-and-tumble swimmers in one dimension*, J. Phys. A 50, 325601 (2017), https://arxiv.org/pdf/2206.03123 .
- P. C. Bressloff, *Run-and-tumble particle with diffusion: boundary local times and the zero-diffusion limit*, arXiv:2508.20473 (2025), https://arxiv.org/pdf/2508.20473 .
- S. Mukherjee, P. Le Doussal, N. R. Smith, *Large deviations in statistics of the local time and occupation time for a run and tumble particle*, arXiv:2405.07032v1 (2024), https://arxiv.org/html/2405.07032v1 .
- C. Roberts, G. Pruessner, *Exact solution of a boundary tumbling particle system in one dimension*, Phys. Rev. Research 4, 033234 (2022), https://doi.org/10.1103/PhysRevResearch.4.033234 .
