# Universal large-energy period law for two-community eco-evolutionary feedback cycles

## Finding

For the symmetric-community, equal-recovery, reversal-payoff subfamily of the Betz–Fu–Masuda edge-environment evolutionary game, every non-equilibrium interior orbit is periodic on its fixed environmental log-odds-difference leaf. Let \(E>0\) denote the excess value of the explicitly normalized conserved Hamiltonian defined below, let \(c\in\mathbb R\) denote the fixed difference of environmental logits, and let \(\mathcal T_c(E)\) be the least period **in the original model's physical time**. For all fixed \(a,b,\theta>0\), \(0<\delta<1\), and \(c\in\mathbb R\),

\[
\boxed{\lim_{E\to\infty}\frac{\mathcal T_c(E)}{E}=2\left(1+\frac1\theta\right).}
\]

The asymptotic coefficient is independent of both positive payoff gaps \(a,b\), the within/across-community interaction mixture \(\delta\), and the leaf's environmental imbalance \(c\). Periodicity for reversal-symmetric feedback games was already observed in the source literature; the new assertion is the sharp universal original-time large-energy law for this three-state, two-environment reduction.

## Assumptions and scope

The full model has two equally sized communities with cooperation fractions \(x,y\) and three edge-environment states \(n_1,n_2,n_{12}\). Impose the invariant symmetry \(x=y\), \(n_1=n_2=n\), equal positive environmental recovery parameters \(\theta_1=\theta_2=\theta_{12}=\theta\), and within/across mixing rates \(1-\delta,\delta\) with \(0<\delta<1\). Adopt the source paper's reversal-dependent payoff matrix

\[
 A(s)=(1-s)\begin{pmatrix}T&P\\R&S\end{pmatrix}
       +s\begin{pmatrix}R&S\\T&P\end{pmatrix},
 \qquad a=T-R>0,\quad b=P-S>0.
\]

Only the payoff differences \(a,b\) enter the equations. Write \(m=n_{12}\). On strictly interior initial conditions \(0<x,n,m<1\), the exact, unrescaled three-dimensional flow is

\[
\begin{aligned}
\dot x&=x(1-x)[b+(a-b)x]\{1-2[(1-\delta)n+\delta m]\},\\
\dot n&=n(1-n)[(1+\theta)x-1],\\
\dot m&=m(1-m)[(1+\theta)x-1].
\end{aligned}
\]

Let \(\sigma(z)=e^z/(1+e^z)\) and set

\[
 u=\log\frac{x}{1-x},\quad
 v=\log\frac{n}{1-n},\quad
 c=\log\frac{n}{1-n}-\log\frac{m}{1-m}.
\]

The real number \(c\) is conserved exactly, so \(m=\sigma(v-c)\). Define

\[
 w(u)=b+(a-b)\sigma(u),\qquad
 M_c(v)=(1-\delta)\sigma(v)+\delta\sigma(v-c).
\]

Then \(\dot u=w(u)[1-2M_c(v)]\) and \(\dot v=(1+\theta)\sigma(u)-1\). On each fixed \(c\), choose the following potentials (additive constants are immaterial):

\[
\begin{aligned}
F(u)&=-\frac ub+\left(\frac\theta a+\frac1b\right)\log(b+ae^u),\\
G_c(v)&=2(1-\delta)\log(1+e^v)
  +2\delta\log(1+e^{v-c})-v.
\end{aligned}
\]

The unique equilibrium on the leaf has \(u_*=-\log\theta\) and \(v_*\) uniquely determined by \(M_c(v_*)=1/2\). The **excess energy** used in the theorem is

\[
E=F(u)+G_c(v)-F(u_*)-G_c(v_*)>0.
\]

The asymptotic concerns a fixed choice of parameters and a fixed \(c\), as \(E\) tends to infinity. It makes no claim about perturbations transverse to the symmetric submanifold of the original five-dimensional system.

## Proof

**1. Exact leafwise reduction.** Equal environmental recovery rates give
\(d\log(n/(1-n))/dt=d\log(m/(1-m))/dt=(1+\theta)x-1\), proving conservation of \(c\). The payoff row difference of the reversal matrix is \([b+(a-b)x](1-2s)\); averaging at environmental level \((1-\delta)n+\delta m\) yields the displayed three-state flow. No time reparameterization is made.

**2. A proper strict-convex integral.** Direct differentiation gives

\[
 F'(u)=\frac{(1+\theta)\sigma(u)-1}{w(u)},\qquad
 G_c'(v)=2M_c(v)-1.
\]

Therefore \(\frac d{dt}[F(u)+G_c(v)]=0\) for the physical-time equations. Moreover,

\[
F''(u)=\frac{(a+\theta b)e^u}{(b+ae^u)^2}>0,\qquad
G_c''(v)=2(1-\delta)\sigma'(v)+2\delta\sigma'(v-c)>0.
\]

The slopes at infinity are

\[
 F'(-\infty)=-1/b,\quad F'(+\infty)=\theta/a,
 \quad G_c'(-\infty)=-1,\quad G_c'(+\infty)=1.
\]

Thus both potentials are coercive and strictly convex with a unique minimum. Every level \(E>0\) is a smooth compact simple closed convex oval with no equilibria, and the flow is nonzero and tangent on it. Every such trajectory therefore runs around the oval periodically, with a well-defined least physical-time period.

**3. Energy asymptotics of the turning points.** Let \(u_-(s)<u_*<u_+(s)\) solve \(F(u)-F(u_*)=s\); let \(v_-(s)<v_*<v_+(s)\) solve \(G_c(v)-G_c(v_*)=s\). From the four nonzero asymptotic slopes,

\[
\begin{aligned}
u_-(s)&=-bs+O(1),&u_+(s)&=(a/\theta)s+O(1),\\
v_-(s)&=-s+O(1),&v_+(s)&=s+O(1)
\end{aligned}\qquad (s\to\infty).
\]

Fix \(0<\varepsilon<1/2\), and split the oval at \(u=u_\pm((1-\varepsilon)E)\). In the **central strip** between these two turning abscissas, \(G_c(v)-G_c(v_*)\ge\varepsilon E\). Consequently the upper and lower branches satisfy, uniformly throughout the strip as \(E\to\infty\),

\[
1-2M_c(v)=-1+o(1)\quad\text{(upper branch)},
\qquad 1-2M_c(v)=1+o(1)\quad\text{(lower branch)}.
\]

Both branch crossings together therefore take

\[
  [2+o(1)]\int_{u_-((1-\varepsilon)E)}^{u_+((1-\varepsilon)E)}\frac{du}{w(u)}.
\]

Since \(1/w(u)\to1/b\) as \(u\to-\infty\) and \(1/w(u)\to1/a\) as \(u\to+\infty\), the turning-point estimates give

\[
 \frac1E\int_{u_-((1-\varepsilon)E)}^{u_+((1-\varepsilon)E)}\frac{du}{w(u)}
 \longrightarrow(1-\varepsilon)\left(1+\frac1\theta\right).
\]

**4. Both turning caps are negligible after \(\varepsilon\downarrow0\).** On the right cap, \(u\ge u_+((1-\varepsilon)E)\), so \(\dot v=(1+\theta)\sigma(u)-1\ge\theta/2\) for all sufficiently large \(E\); on the left cap the same expression is \(\le-1/2\). Throughout either cap, \(G_c(v)-G_c(v_*)\le\varepsilon E\), hence \(v\in[v_-(\varepsilon E),v_+(\varepsilon E)]\), an interval of length \(2\varepsilon E+O(1)\). Monotonicity of \(v\) on each cap bounds their total duration by \(C_\theta[\varepsilon E+1]\), with \(C_\theta\) independent of \(E\) and of \(\varepsilon\in(0,1/2)\). Thus, for fixed \(\varepsilon\), the central-strip calculation gives a lower asymptotic bound \(2(1-\varepsilon)(1+1/\theta)\), and the cap bound gives an upper bound differing by at most \(C_\theta\varepsilon\). Let \(\varepsilon\downarrow0\). This proves

\[
 \lim_{E\to\infty}\mathcal T_c(E)/E=2(1+1/\theta).
\]

The proof applies to every fixed finite \(c\) and every positive \(a,b,\theta\) and \(0<\delta<1\), without asserting a uniform-in-parameter error bound.

## Verification

`verify.py` checks by symbolic rational algebra the payoff reduction, the derivative identity for \(F\), positivity of its curvature, and its two limiting slopes. Numerical ODE integration checks Hamiltonian conservation and computes the original-time period for a fixed nontrivial environmental imbalance. At \((a,b,\theta,\delta,c)=(2,1,2,1/3,\log3)\), computed period-to-energy ratios for \(E=20,80,160\) are approximately \(3.425781,3.106445,3.053223\), consistent with the proved limiting slope \(3\). Run `python verify.py` using Python with SymPy, NumPy, and SciPy installed. The code is a finite diagnostic; the limit follows from the four-step proof above.

## Relationship to prior work

Betz, Fu and Masuda's 2024 two-community edge-environment model supplies the five-dimensional equations and observes interior periodic orbits for the reversal payoff matrix with equal recovery rates (their Discussion, Eq. (47)); periodic existence and the equilibrium line are **not** claimed new. The earlier Weitz et al. 2016 single-environment model uses a conserved quantity, and Gong, Gao and Cao's 2018 two-population common-environment work establishes periodic behavior using reversibility. Their state spaces and the stated claims do not supply the exact energy-normalized physical-time slope for two independently evolving edge environments. Related high-energy period laws for other Hamiltonian systems are not implications for the present physical clock. This is a best-knowledge originality assessment, not an exhaustive publication-priority certificate.

## Limitations

This is an exact theorem on the invariant symmetric three-state subsystem, not a full five-dimensional stability result. It neither proves transverse orbital attraction nor describes heterogeneity of recovery rates, noise, mutation, or switching of community symmetry. It does not assert that \(\mathcal T_c(E)\) is monotone, give a uniformly controlled next-order offset, or furnish a uniform limit when \(c\) or parameters vary with \(E\). Earlier uncatalogued equivalent formulas are a residual originality risk.

## References

1. K. Betz, F. Fu, N. Masuda, *Evolutionary game dynamics with environmental feedback in a network with two communities*, arXiv:2404.17082 (first public version 2024-04-25), 2024. https://arxiv.org/html/2404.17082v2 ; https://doi.org/10.1007/s11538-024-01310-3.
2. J. S. Weitz, C. Eksin, K. Paarporn, S. P. Brown, W. C. Ratcliff, *An oscillating tragedy of the commons in replicator dynamics with game-environment feedback*, PNAS 113 (2016), E7518–E7525. https://doi.org/10.1073/pnas.1604096113.
3. L. Gong, J. Gao, M. Cao, *Evolutionary Game Dynamics for Two Interacting Populations under Environmental Feedback*, arXiv:1806.03194 (2018). https://arxiv.org/abs/1806.03194.
4. Y. Kawano, L. Gong, B. D. O. Anderson, M. Cao, *Evolutionary dynamics of two communities under environmental feedback*, IEEE Control Systems Letters 3 (2019), 254–259. https://doi.org/10.1109/LCSYS.2018.2866775.
