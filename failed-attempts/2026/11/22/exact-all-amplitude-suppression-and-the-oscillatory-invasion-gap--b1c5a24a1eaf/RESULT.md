# Exact all-amplitude suppression and the oscillatory invasion gap in a host–vector predator cycle

## Finding

**Theorem (exact ecological-cycle invasion gap).** In the uncontrolled dimensionless SIR–SI and Lotka–Volterra model [1], let \(m=\mu_h>0\), \(\gamma>0\), \(g=\gamma+m\), \(\delta=\mu_D>0\), \(B_h,B_v>0\) and \(\kappa=B_hB_v\). Fix any positive trajectory of the ecological subsystem and restrict the remaining initial conditions to the biological simplex described below.

If the ecological trajectory is a nonconstant closed orbit of period \(T\), there is exactly one \(\kappa_c(N)>g\) where the infection-free cycle changes transverse invasion stability. For the principal Floquet exponent \(\lambda(\kappa)\), the positive Floquet solution of the infection variational system gives the **nonperturbative identity**

\[
\kappa-g=\lambda(\lambda+g+1)+\operatorname{Var}_T(z),\qquad z(t)=\frac{d}{dt}\log y(t),
\]

with \(\langle z\rangle_T=\lambda\) and \(\operatorname{Var}_T(z)=\langle(z-\lambda)^2\rangle_T\). At the sharp threshold, \(\kappa_c-g=\langle z^2\rangle_T>0\).

Every biologically admissible infection solution on the orbit satisfies \(I_h(t),I_v(t)\to0\) **exponentially** whenever \(0<\kappa<\kappa_c\), including all \(0<\kappa\le g\). For \(\kappa>\kappa_c\) the infection-free cycle has a positive transverse Floquet exponent. At the constant ecological equilibrium \(N=D=1\), the threshold is exactly \(g\); infection still disappears for \(\kappa=g\), but exponential decay is not asserted there.

For the small-amplitude ecological orbit \(N(0)=1+\varepsilon\), \(D(0)=1\), \(0<\varepsilon\ll1\),

\[
\kappa_c(\varepsilon)
=g+\frac{g^2}{2\big((g+1)^2+\delta\big)}\varepsilon^2
+O(\varepsilon^3).
\]

These conclusions concern infection invasion and clearance conditional on a fixed ecological orbit. They do not imply positive endemic persistence above the threshold or give a nonlinear conclusion at \(\kappa=\kappa_c\) on a nonconstant orbit.

## Assumptions and scope

The source model's dimensionless uncontrolled equations are

\[
\begin{aligned}
S_h'&=m(1-S_h)-B_hS_hI_v,&
I_h'&=B_hS_hI_v-gI_h,\\
S_v'&=(S_v+I_v)-B_vS_vI_h-DS_v,&
I_v'&=B_vS_vI_h-DI_v,\\
D'&=\delta(S_v+I_v-1)D.
\end{aligned}
\]

The recovered-host proportion is \(R_h=1-S_h-I_h\), and the biological region is \(S_h,I_h,R_h\ge0\), \(S_v,I_v\ge0\), \(D>0\), \(S_v+I_v>0\). In this region \(R_h'=\gamma I_h-mR_h\), and the ecological subsystem is independent of infection. Set the total vector density \(N=S_v+I_v\), the infected vector fraction \(q=I_v/N\), and infected-host fraction \(i=I_h\). Its exact transformed equations are

\[
\begin{aligned}
N'&=(1-D)N,&D'&=\delta(N-1)D,\\
S_h'&=m(1-S_h)-B_hS_hNq,&i'&=B_hS_hNq-gi,\\
q'&=B_v(1-q)i-q.
\end{aligned}
\]

Thus \(0\le q\le1\), \(0\le S_h\le1\). All conclusions apply to fixed positive ecological initial conditions; the classical center has orbit-dependent, nonuniform extrema. Define \(\langle f\rangle_T=T^{-1}\int_0^T f(t)\,dt\).

## Proof

**1. Ecological geometry and exact mean.** The positive ecological system has the first integral

\[
H(N,D)=\delta(N-\log N)+D-\log D.
\]

Every nonminimum level is a compact smooth closed curve surrounding \((1,1)\) and contains no equilibrium, hence is a periodic orbit of period \(T\). Since \((\log D)'=\delta(N-1)\), integration over a period gives the exact identity \(\langle N\rangle_T=1\), without a small-amplitude assumption.

**2. Infection linearization.** At the infection-free solution \(S_h=1,i=q=0\), the transverse linear variational equation is

\[
\binom{h}{y}'=
\begin{pmatrix}-g&B_hN(t)\\B_v&-1\end{pmatrix}\binom{h}{y}.
\]

Because both off-diagonal entries are strictly positive, its period monodromy is strictly positive. Its Perron eigenvalue and positive eigenvector determine a positive Floquet solution \((h,y)\) whose components are each a positive periodic function multiplied by \(e^{\lambda t}\). In particular \(z=y'/y=B_vh/y-1>-1\) is periodic and \(\langle z\rangle_T=\lambda\).

**3. Exact Riccati variance identity.** Differentiate \(z=B_vh/y-1\) using the two equations. Pointwise,

\[
z'=\kappa N-g-(g+1)z-z^2.
\]

Averaging, and using \(\langle N\rangle_T=1\), proves

\[
\kappa-g=(g+1)\lambda+\langle z^2\rangle_T
=\lambda(\lambda+g+1)+\operatorname{Var}_T(z).
\]

Since \(z>-1\), we have \(\lambda>-1\), and \(\lambda+g+1>g>0\). If \(\kappa<g\), the identity excludes \(\lambda\ge0\). At \(\kappa=g\), equality \(\lambda=0\) forces \(\operatorname{Var}_T(z)=0\), hence constant \(z\); the Riccati equation then forces constant \(N\), impossible on a nonconstant orbit. Therefore \(\lambda(g)<0\) for every nonconstant orbit, even arbitrarily large ones.

**4. Unique sharp invasion crossing.** For fixed \(N(t)>0\), the dominant Floquet exponent depends continuously and *strictly increasingly* on \(\kappa>0\): after the constant positive change of coordinates \(u=B_vh\), the infection matrix has positive off-diagonal entries \(\kappa N(t)\) and \(1\), so strict comparison of its positive period propagators applies. As \(\kappa\downarrow0\), its growth exponent approaches \(-\min\{g,1\}<0\). As \(\kappa\to\infty\), it tends to positive infinity by comparison with the constant cooperative matrix obtained by replacing \(N(t)\) by its strictly positive minimum. Thus exactly one crossing \(\lambda(\kappa_c)=0\) exists. By step 3, \(\kappa_c>g\) and \(\kappa_c-g=\langle z^2\rangle_T>0\); the last inequality is strict because zero square mean would force \(N\) constant.

**5. Nonlinear global extinction below the crossing.** In the admissible state space, the exact equations give componentwise

\[
\binom{i}{q}'\le
\begin{pmatrix}-g&B_hN(t)\\B_v&-1\end{pmatrix}\binom{i}{q},
\]

because \(S_h\le1\) and \(1-q\le1\). Cooperative comparison with the positive periodic linear system, whose principal exponent is negative when \(\kappa<\kappa_c\), proves \(i,q=O(e^{-ct})\) for some orbit- and parameter-dependent \(c>0\). As \(I_v=Nq\), and \(N\) is bounded on the fixed orbit, both physical infection compartments decay exponentially. If \(\kappa>\kappa_c\), the positive transverse exponent gives linear instability of the infection-free ecological cycle; no nonlinear persistence statement is needed or asserted.

For the constant ecological equilibrium, the same constant linear system crosses at \(\kappa=g\). At equality \(\kappa=g\), define \(L=i+B_hq\), which satisfies

\[
L'=B_h(S_h-1)q-g i q\le0.
\]

The biological infection-host phase region is compact and positively invariant. Its largest invariant subset with \(L'=0\) lies in \(i=q=0\): any nonzero infection creates both positive components immediately and then makes the derivative strictly negative. The invariance principle therefore yields \(i,q\to0\) at \(\kappa=g\). This equality-case argument does not assert exponential decay.

**6. Small ecological amplitude.** From the ecological linearization at \((1,1)\), for \(N(0)=1+\varepsilon,D(0)=1\),

\[
N(t)=1+\varepsilon\cos(\sqrt\delta\,t)+O(\varepsilon^2),\qquad
T(\varepsilon)=2\pi/\sqrt\delta+O(\varepsilon).
\]

Smooth dependence of the periodic orbit and the simple Perron Floquet multiplier, together with the strict transverse crossing at \((\varepsilon,\kappa)=(0,g)\), gives \(\kappa_c(\varepsilon)=g+O(\varepsilon^2)\) by the exact variance identity. At the crossing \(\lambda=0\) and \(z(t)=\varepsilon z_1(t)+O(\varepsilon^2)\), where the uniquely periodic leading term solves

\[
z_1'+(g+1)z_1=g\cos(\sqrt\delta\,t).
\]

Its mean square is \(g^2/[2((g+1)^2+\delta)]\). Applying \(\kappa_c-g=\langle z^2\rangle_T\) yields the displayed quadratic threshold displacement, with an \(O(\varepsilon^3)\) remainder.

## Verification

The included `verify_vector_cycle.py` independently integrates six nonconstant ecological cycles, computes the two-by-two monodromy and principal Floquet exponent, brackets the unique threshold, and checks the Riccati mean-square identity numerically. Use `python3 verify_vector_cycle.py` with NumPy and SciPy installed. The test case \(g=3/2,\delta=2\) has the exact predicted small-amplitude shift coefficient \(3/22\). These are diagnostic numerical checks; every infinite-orbit statement is established by the preceding analytic proof, not by the finite tests.

## Relationship to prior work

Balderrama, Ceresa Dussel and Sanchez de la Vega [1], equations (3.3)–(3.8) and Propositions 3.4–3.5, give the model, the constant-equilibrium reproduction threshold and an orbit-extrema-based sufficient extinction condition. The present theorem instead supplies the sharp *per-orbit* infection invasion crossing, an exact variance representation for arbitrary oscillation amplitude, and a global comparison-based clearance statement that holds for every orbit when \(\kappa\le g\). It neither revises nor re-certifies earlier unrelated results.

Bacaër [2] and Khong, Carmona and Gandon [3] **already establish perturbative suppression of vector-borne invasion under density-only seasonality**, and [3] develops covariance characterizations. The direction of the quadratic small-amplitude effect is therefore not claimed new. The distinguishing mathematical contributions here are the all-amplitude positive-definite variance identity *on the endogenous conservative predator–vector cycles*, the sharp unique per-cycle invasion boundary, and the nonlinear subthreshold extinction result. Zhou and Yao [4] study a different predator–host–vector system, including thresholds and periodic phenomena; their model does not establish this identity for [1]. Searches of related published mathematical findings revealed periodic vector–host schedules and ecological invasion laws but no statement implying this exact theorem. This comparison is evidence of bounded originality, not a proof of priority or uniqueness.

## Limitations

The result assumes the *uncontrolled* source system, a conserved positive ecological trajectory and constant transmission and recovery coefficients. It does not cover seasonal forcing of the biting rate, predator release controls, stochastic systems, global attraction of an endemic state above invasion, or nonlinear dynamics at the sharp threshold on a nonconstant orbit. The clearance rate is orbit-dependent and need not be uniform as ecological amplitudes diverge. A separate historical-priority comparison is still warranted for general periodic cooperative-system inequalities and the full text of earlier perturbative work. There has been no independent validation.

## References

[1] R. Balderrama, I. Ceresa Dussel, C. Sanchez de la Vega, *Optimal Control Strategies for Epidemic Dynamics: Integrating SIR-SI and Lotka–Volterra Models*, arXiv:2602.06178 (first submitted 2026-02-05), https://arxiv.org/abs/2602.06178.

[2] N. Bacaër, *Approximation of the basic reproduction number R0 for vector-borne diseases with a periodic vector population*, Bulletin of Mathematical Biology (2007), doi:10.1007/s11538-006-9166-9.

[3] V. H. Khong, P. Carmona, S. Gandon, *Seasonality and the persistence of vector-borne pathogens*, Journal of the Royal Society Interface (2023), doi:10.1098/rsif.2023.0470, https://pmc.ncbi.nlm.nih.gov/articles/PMC10715918/.

[4] F. Zhou, H. Yao, *Dynamics and Biocontrol: The Indirect Effects of a Predator Population on a Host-Vector Disease Model*, Abstract and Applied Analysis (2014), doi:10.1155/2014/252718, https://onlinelibrary.wiley.com/doi/10.1155/2014/252718.
