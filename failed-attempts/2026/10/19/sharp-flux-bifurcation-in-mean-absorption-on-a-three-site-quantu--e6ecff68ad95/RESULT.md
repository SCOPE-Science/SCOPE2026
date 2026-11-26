# Sharp flux bifurcation in mean absorption on a three-site quantum ring

## Finding

There is an exact transition in the flux minimizing the unconditional mean absorption time of a three-site chiral quantum ring with a single continuously operating sink. For hopping strength \(J>0\), trap rate \(\Gamma>0\) and flux \(\phi\) defined by the matrix below, the mean time is infinite at \(\sin\phi=0\) and otherwise equals

\[
T(J,\Gamma,\phi)=\frac{3}{\Gamma}+\frac{1}{2J\sin\phi}+\frac{\Gamma}{4J^2\sin^2\phi}.
\]

When \(0<\Gamma<J\), exactly two fluxes modulo \(2\pi\) minimize this quantity: they satisfy \(\sin\phi=-\Gamma/J\) and give \(T_{\min}=11/(4\Gamma)\). When \(\Gamma\ge J\), the unique minimizing flux is \(\phi=3\pi/2\) modulo \(2\pi\), with \(T_{\min}=3/\Gamma-1/(2J)+\Gamma/(4J^2)\). Thus two nonquadrature optimizers merge at the sharp transition \(\Gamma=J\).

## Assumptions and scope

Let \(\{|0\rangle,|1\rangle,|2\rangle\}\) be an orthonormal single-excitation site basis. Take

\[
H_\phi=J\begin{pmatrix}0&1&1\\1&0&e^{i\phi}\\1&e^{-i\phi}&0\end{pmatrix},\quad P_0=|0\rangle\langle0|,\quad \rho(0)=|1\rangle\langle1|.
\]

The phase of the \(1\)-to-\(2\) edge is the gauge-fixed definition of \(\phi\); reversing the edge orientation reverses the sign of the quoted optimal flux. A perfect Markovian absorbing channel of rate \(\Gamma\) at site \(0\) acts on the unabsorbed three-dimensional sector by

\[
\dot\rho=-i[H_\phi,\rho]-\frac{\Gamma}{2}\{P_0,\rho\}.
\]

There is no on-site disorder, dephasing, pumping, reset, or re-emission from the sink. The survival probability is \(S(t)=\operatorname{tr}\rho(t)\); the unconditional absorption time is \(T=\int_0^\infty S(t)dt\), with \(T=+\infty\) if the survival distribution has positive mass at infinite time. All claims hold for every \(J,\Gamma>0\) and every real \(\phi\) modulo \(2\pi\).

## Proof

**1. Stability and dark phases.** Set \(k=\Gamma/J\), \(s=\sin\phi\), \(c=\cos\phi\), and introduce dimensionless time \(\tau=Jt\). Let

\[
A=-i\begin{pmatrix}0&1&1\\1&0&c+is\\1&c-is&0\end{pmatrix}-\frac{k}{2}P_0.
\]

For an eigenpair \(Av=\lambda v\), taking the real part of the inner product with \(v\) gives

\[
\operatorname{Re}\lambda=-\frac{k|v_0|^2}{2\|v\|^2}\le0.
\]

Equality forces \(v_0=0\); the site-zero eigenvector equation then gives \(v_2=-v_1\). The remaining two components are simultaneously an eigenvector equation only when \(e^{i\phi}=e^{-i\phi}\), equivalently \(s=0\). Thus if \(s\ne0\), every eigenvalue of \(A\) has strictly negative real part and \(e^{A\tau}\to0\) exponentially (possibly with polynomial factors), so absorption is almost sure and the time integral below converges.

If \(s=0\), the normalized vector \((0,1,-1)/\sqrt2\) is an exact dark eigenstate of \(H_\phi\). It has squared overlap \(1/2\) with \(|1\rangle\). Its orthogonal complement is invariant under both \(H_\phi\) and \(P_0\), and has no other undamped eigenvector; hence the complementary component decays and \(S(t)\to1/2\). Therefore the eventual absorption probability is \(1/2\) and \(T=+\infty\) at these phases.

**2. The exact integrated survival matrix.** For \(s\ne0\), define

\[
X=\int_0^\infty e^{A\tau}|1\rangle\langle1|e^{A^\dagger\tau}\,d\tau.
\]

It uniquely solves \(AX+XA^\dagger=-|1\rangle\langle1|\). The following explicit Hermitian matrix satisfies that equation:

\[
X=\begin{pmatrix}
\frac1k & \frac c{4s}-\frac i4 & -\frac c{4s}-\frac i4\\
\frac c{4s}+\frac i4 & \frac1k+\frac{k}{8s^2} & -\frac{kc^2}{8s^2}-\frac1{4s}-\frac{ikc}{8s}\\
-\frac c{4s}+\frac i4 & -\frac{kc^2}{8s^2}-\frac1{4s}+\frac{ikc}{8s} & \frac1k+\frac{k}{8s^2}+\frac1{2s}
\end{pmatrix}.
\]

Indeed, inserting its nine entries into \(AX+XA^\dagger+|1\rangle\langle1|\) gives zero using only \(c^2+s^2=1\) and \(k>0\), \(s\ne0\). This finite symbolic identity is independently checked entry-by-entry in the supplied executable script. Stability makes the Lyapunov solution unique and equal to the integral. Since physical time is \(t=\tau/J\),

\[
T=\frac1J\operatorname{tr}X
=\frac1J\left(\frac3k+\frac1{2s}+\frac{k}{4s^2}\right),
\]

which is the asserted formula after substituting \(k=\Gamma/J\).

**3. Global flux optimization.** Put \(x=1/s\). Excluding exactly dark fluxes, its feasible domain is \(( -\infty,-1]\cup[1,\infty)\). Up to the positive factor \(1/J\), the objective is the strictly convex quadratic

\[
\frac3k+\frac x2+\frac{kx^2}{4}
=\frac{11}{4k}+\frac k4\left(x+\frac1k\right)^2.
\]

If \(0<k<1\), the unconstrained minimizer \(x=-1/k<-1\) is feasible, so both and only the two distinct fluxes with \(\sin\phi=-k\) are optimal. If \(k\ge1\), its closest feasible point is uniquely \(x=-1\) (always strictly preferable to \(x=1\)), corresponding to \(\phi=3\pi/2\) modulo \(2\pi\). Evaluating the quadratic gives both displayed optimal values and equality cases. In particular, at \(k=1\) the two branches meet at \(x=-1\). Dark phases have infinite time and cannot minimize.

## Verification

The bundled standalone \(\texttt{triangle\_absorption\_checker.py}\) is runnable using Python 3 with SymPy, NumPy and SciPy. It first symbolically reduces all nine Hermitian Lyapunov residual components modulo \(c^2+s^2-1\), verifies the trace identity, then tests independent matrix Lyapunov solvers, direct physical-time integration, eigenvalue decay, flux minimization and dark survival probabilities. It passed **390 assertions** when executed on the source embedded in this record. Independent numerical solvers and finite experiments corroborate, but do not replace, the all-parameter proof above.

## Relationship to prior work

Wang, Ren, Yin, Ziegler, Barkai and Tornow (2024, arXiv:2402.15843) studied the same chiral three-site topology and target-detection dark states, but their detection is based on discrete stroboscopic projective measurements. Their hitting-time and phase-matching formulas do not give the continuous Markovian sink's integrated survival time or the sink-rate-dependent global flux optimization derived here.

Zimborás and collaborators (2013, arXiv:1208.4049; *Scientific Reports* 3, 2361) introduced chiral continuous-time quantum transport with open-system trapping and explored phase-dependent transport efficiency and half-arrival times on quantum switch and triangle-chain networks. The present claim concerns a different observable (complete survival integral), a single three-site ring and an exact global phase classification at every sink strength.

Bottarelli and collaborators (2023, arXiv:2302.08472) investigated a six-site chiral quantum router with a triangular core, primarily through unitary transfer probabilities; this does not yield the present dissipative lifetime formula. Established non-Hermitian rank-one trapping methods and known dark-state mechanisms are used as foundations rather than claimed as new. The resulting formula is a narrow specialization that could in principle be derivable from more general published transport frameworks; a literature search cannot certify historical uniqueness.

## Limitations

The theorem is specific to an initially occupied neighboring site, three equal hopping magnitudes, one absorbing Lindblad jump, and the stated flux orientation. It makes no claim about finite-sample flux estimation, non-Markovian detection, arbitrary graphs, incoherent dephasing, disorder, or multiple absorbers. The result's mathematical proof is complete within those assumptions, but independent literature-priority and mathematical audit have not been performed.

## References

1. Q. Wang, S. Ren, R. Yin, K. Ziegler, E. Barkai, S. Tornow, *First Hitting Times on a Quantum Computer: Tracking vs. Local Monitoring, Topological Effects, and Dark States*, arXiv:2402.15843, first publicly posted 2024-02-24. https://arxiv.org/abs/2402.15843
2. Z. Zimborás et al., *Quantum Transport Enhancement by Time-Reversal Symmetry Breaking*, *Scientific Reports* 3, 2361 (2013), arXiv:1208.4049. https://pmc.ncbi.nlm.nih.gov/articles/PMC3734483/
3. L. Bottarelli et al., *Quantum routing of information using chiral quantum walks*, arXiv:2302.08472 (2023). https://arxiv.org/abs/2302.08472
4. Mathematical Subject Classification 2020, 82C70: Transport processes.
