# Sharp configurational heating under alternating fully refreshed BAOAB steps

## Finding
Consider unit-mass, unit-temperature harmonic Langevin dynamics with potential \(U(q)=q^2/2\), integrated with standard BAOAB splitting (half kick, half drift, full Ornstein–Uhlenbeck refresh, half drift, half kick). Fix two alternating positive dimensionless step lengths \(0<s,t<2\). In the full-momentum-refresh limit, the process has a unique stationary Gaussian law for each step phase. Write \(V_s\) and \(V_t\) for the position variances immediately after steps of length \(s\) and \(t\), respectively, and define
\[
D(s,t)=32-(4-st)(s+t)^2.
\]
Then \(D(s,t)>0\) and the exact variances are
\[
V_s=1+\frac{(s-t)[st(s+t)+4(s-t)]}{D(s,t)},\qquad
V_t=1-\frac{(s-t)[st(s+t)-4(s-t)]}{D(s,t)}.
\]
The equally phase-averaged configurational variance obeys the sharp law
\[
\boxed{\frac{V_s+V_t}{2}=1+\frac{4(s-t)^2}{D(s,t)}.}
\]
Consequently it equals the unit-temperature Gibbs variance \(1\) **if and only if** \(s=t\); for every unequal pair it is strictly greater than \(1\) and strictly less than \(2\). The supremum \(2\) is sharp but unattained in the open step domain, approached as \((s,t)\to(2,0)\) or its reversal. For fixed sum \(s+t\), equal splitting is the unique variance-minimizing pair.

More finely, if \(s>t\), the long-step phase always has \(V_s>1\), whereas the short-step phase is cooler than equilibrium, at equilibrium, or hotter than equilibrium according as \(st(s+t)\) is greater than, equal to, or less than \(4(s-t)\). In particular, unequal stepping can heat both phases, or heat one phase while cooling the other, even though its phase mean always heats.

If a stationary observation phase is selected uniformly at random, its position law is the equal mixture of the two centered phase Gaussians. This mixture is non-Gaussian whenever \(s\ne t\), with exact positive fourth cumulant
\[
\kappa_4=\frac{3}{4}(V_s-V_t)^2
=\frac{3s^2t^2(s+t)^2(s-t)^2}{D(s,t)^2}.
\]

## Assumptions and scope
The underlying continuous-time SDE is \(dq=p\,dt\), \(dp=-q\,dt-\gamma p\,dt+\sqrt{2\gamma}\,dW\). Each numerical step uses the conventional BAOAB ordering with the same step length in all its substeps. At the thermostat stage the exact update is \(p\mapsto e^{-\gamma h}p+\sqrt{1-e^{-2\gamma h}}\,\xi\), with independent standard-normal \(\xi\). The theorem concerns the full-refresh limit \(\gamma\to\infty\) with each of the two positive step lengths fixed, in which the thermostat stage is exactly \(p\mapsto\xi\). The step order is deterministic and periodic, \(s,t,s,t,\ldots\); there is no independent random selection of step sizes. Both \(s\) and \(t\) lie strictly inside the harmonic Verlet interval \((0,2)\). The equal phase average weights the two post-step observations equally, not by physical elapsed time. No claim is made for finite friction, nonharmonic potentials, or general nonperiodic step sequences.

## Proof
**Full-refresh reduction.** Let \((q_n,p_n)\) be the state immediately after the \(n\)-th BAOAB step of length \(h_n\), and let \(\xi_n\) denote its fresh thermostat normal. The final half-kick gives \(p_n=\xi_n-\frac{h_n}{2}q_n\). The preceding half-kick, half-drifts, and refresh therefore give the exact recursion
\[
q_n=A_nq_{n-1}+\frac{h_n}{2}(\xi_{n-1}+\xi_n),
\qquad A_n=1-\frac{h_n(h_n+h_{n-1})}{4}.
\]
For alternating lengths, set \(A_s=1-s(s+t)/4\) and \(A_t=1-t(s+t)/4\). Because \(0<s,t<2\), both \(A_s\) and \(A_t\) lie in \((-1,1)\). Differences between trajectories driven by the same normals shrink by \(|A_sA_t|<1\) per two steps. This proves existence and uniqueness of a stationary two-phase joint Gaussian law, including the stored thermostat normal.

**Moment equations.** The fresh thermostat variable enters \(q_n\) with coefficient \(h_n/2\), independently of the previous state, so \(\operatorname{Cov}(q_n,\xi_n)=h_n/2\) in either phase. Expanding the square of the exact position recursion and retaining the shared preceding noise gives
\[
V_t=A_t^2V_s+\frac{t^2}{2}+\frac{A_tst}{2},\qquad
V_s=A_s^2V_t+\frac{s^2}{2}+\frac{A_sst}{2}.
\]
Their determinant is \(1-A_s^2A_t^2\), and direct factorization yields
\[
1-A_s^2A_t^2=\frac{(s+t)^2(4-st)D(s,t)}{256}>0.
\]
Solving the two equations and simplifying gives exactly the two rational expressions in the Finding. Summation and subtraction give
\[
\frac{V_s+V_t}{2}-1=\frac{4(s-t)^2}{D(s,t)},
\qquad V_s-V_t=\frac{2st(s+t)(s-t)}{D(s,t)}.
\]
Thus \(V_s=V_t\) exactly when \(s=t\), and the sign classification follows by inspecting the displayed numerators of \(V_s-1\) and \(V_t-1\).

**Sharp global ceiling.** Put \(u=s+t\), \(v=st\). The positive excess in the phase mean is
\[
R(u,v)=\frac{4(u^2-4v)}{32-(4-v)u^2}.
\]
At fixed \(u\), its derivative in \(v\) equals
\[
\partial_vR=-\frac{4[(u^2-8)^2+64]}{[32-(4-v)u^2]^2}<0.
\]
If \(0<u\le2\), the admissible lower bound \(v>0\) implies
\[
R<\frac{u^2}{8-u^2}\le1.
\]
If \(2<u<4\), the step caps \(s,t<2\) force \(v>2(u-2)\). At the lower boundary the denominator of \(R\) exceeds its numerator by
\[
2(u-2)(u^2-4u+8)>0,
\]
so \(R<1\) again. In both cases the supremum \(1\) is approached only in the boundary limit \((s,t)\to(2,0)\) or reversed. Since \(R\ge0\), the exact phase-average variance lies in \([1,2)\) with equality at its lower end only for \(s=t\). The formula also proves the fixed-sum unique minimum.

**Non-Gaussian phase mixture.** Each phase has a centered Gaussian distribution with variance \(V_s\) or \(V_t\). Selecting phases with equal probability produces the mixture with variance \((V_s+V_t)/2\) and fourth moment \(3(V_s^2+V_t^2)/2\). Subtracting three times its squared variance gives \(\kappa_4=3(V_s-V_t)^2/4\), and substitution gives the claimed strict formula.

## Verification
A standalone symbolic-and-numeric script is provided as `verify.py` with `requirements.txt`. It checks the two exact moment recursions, the determinant factorization, phase-average and fourth-cumulant identities, rational examples, and supplementary direct two-period Gaussian covariance computations. The proofs of global inequalities and uniqueness are analytical; numerical checks are not exhaustive proofs. For example, the exact pair \((s,t)=(1,4/5)\) gives \(V_s=345/338>1\), \(V_t=168/169<1\), and mean variance \(681/676>1\). At \((s,t)=(1,1/2)\), both phase variances are hotter: \(V_s=204/193\), \(V_t=198/193\), mean \(201/193\).

## Relationship to prior work
Leimkuhler and Matthews (2013) derived exact harmonic configurational sampling by BAOAB at **one constant** step length. Fass and collaborators (first public preprint 2018-02-16) investigated error in configurational sampling for fixed-step Langevin splitting methods, including BAOAB and its high-friction motivation. The new statement concerns **two unequal deterministic step lengths** with a full momentum refresh and gives exact phase-resolved invariant laws, a strict averaged-heating identity, a sharp universal factor-two ceiling, and a mixture-kurtosis identity. The fixed-step exactness statement is recovered on the diagonal \(s=t\), but it alone does not imply any of these off-diagonal formulas. Other relevant work investigates alternating deterministic Verlet stability and alternative Langevin splittings rather than this invariant configurational law. Searches and available source inspections did not reveal a prior theorem implying the full result; publication-priority uncertainty remains.

## Limitations
The full-refresh assumption is essential to the displayed scalar Gaussian recursion. The factor-two ceiling is proved only for two alternating positive steps inside \((0,2)\), and the equal-phase mixture is not an equal-physical-time sampling law. The two-phase periodic invariant measure need not be invariant under a one-step nonautonomous process without retaining the phase label. No claim is made about finite-friction universality, long-run autocorrelation time, weak/strong trajectory accuracy, multi-frequency potentials, or arbitrary timestep schedules. The originality comparison is not an independent historical certification.

## References
1. J. Fass, D. A. Sivak, G. E. Crooks, K. A. Beauchamp, B. Leimkuhler, J. D. Chodera, *Quantifying Configuration-Sampling Error in Langevin Simulations of Complex Molecular Systems*, bioRxiv v1 (2018-02-16), DOI: https://doi.org/10.1101/266619; published *Entropy* **20** (2018), 318, https://doi.org/10.3390/e20050318.
2. B. Leimkuhler and C. Matthews, *Robust and efficient configurational molecular sampling via Langevin dynamics*, *J. Chem. Phys.* **138** (2013), 174102, https://doi.org/10.1063/1.4802990; lawful open manuscript: https://www.pure.ed.ac.uk/ws/portalfiles/portal/11336040/Robust_and_efficient_configurational_molecular_sampling_via_Langevin_Dynamics.pdf.
3. S. Kieninger and B. G. Keller, *GROMACS Stochastic Dynamics and BAOAB Are Equivalent Configurational Sampling Algorithms*, *J. Chem. Theory Comput.* **18** (2022), 5792–5798, https://doi.org/10.1021/acs.jctc.2c00585.
