# A unique stationary frequency-sensing reset rate for a dephased qubit

## Finding

An equatorial qubit with coherent angular frequency \(\omega\), Markovian pure-dephasing rate \(\gamma>0\), and independent perfect Poisson resets to \(|+\rangle\) at rate \(r>0\), has a **unique positive reset rate** maximizing the quantum Fisher information \(F_\omega\) of its stationary *unconditioned* state for the unknown frequency \(\omega\). The optimization is over the reset rate alone, with \(\gamma\) known and fixed. The result holds for every \(\omega\in\mathbb R\), including zero detuning.

Write \(u=r/\gamma\), \(v=|\omega|/\gamma\), and \(t=v^2\). Then

\[
\gamma^2 F_\omega(r)= f(u,t)
=\frac{u^2(1+u+t)(1+3u+2u^2+t)}{(1+2u+t)((1+u)^2+t)^3}.
\]

The unique optimum is \(r_*=\gamma u_*(t)\), where \(u_*(t)\) is the unique positive zero of the explicit degree-six polynomial

\[
\begin{aligned}
P(u,t)={}&(1+t)^4+(6+18t+18t^2+6t^3)u\\
&+(12+26t+16t^2+2t^3)u^2\\
&+(6+8t+2t^2)u^3-(9+11t+2t^2)u^4\\
&-(12+7t)u^5-4u^6.
\end{aligned}
\]

In particular, \(r_*(0)=\gamma\) and \(F_0(r_*)=1/(16\gamma^2)\). For \(\omega\ne0\), a strict physically scaled bound holds:

\[
\boxed{r_*(\omega)>\sqrt{\gamma^2+\omega^2}.}
\]

The weak-detuning and strong-detuning laws are

\[
\frac{r_*}{\gamma}=1+\frac{19}{36}\frac{\omega^2}{\gamma^2}
+O\!\left(\frac{\omega^4}{\gamma^4}\right)
\quad (|\omega|/\gamma\to0),
\]
\[
\boxed{\frac{r_*}{|\omega|}\longrightarrow \sqrt{\frac{1+\sqrt3}{2}},\qquad
\omega^2\max_{r>0}F_\omega(r)\longrightarrow\frac{2\sqrt3}{9}}
\quad (|\omega|/\gamma\to\infty).
\]

## Assumptions and scope

Use units \(\hbar=1\). The two-level system has Pauli matrices \(\sigma_x,\sigma_y,\sigma_z\), and \(|+\rangle\) is the \(+1\) eigenvector of \(\sigma_x\). Its averaged density operator satisfies the trace-preserving generator

\[
\frac{d\rho}{ds}=-i\left[\frac{\omega}{2}\sigma_z,\rho\right]
+\frac{\gamma}{2}(\sigma_z\rho\sigma_z-\rho)
+r\bigl(|+\rangle\langle+|-\rho\bigr).
\]

Here \(r,\gamma\in(0,\infty)\), \(\omega\in\mathbb R\). Reset events occur independently of the dephasing bath and set the entire qubit state to \(|+\rangle\langle+|\). The quantity optimized is *single-copy stationary-state* symmetric-logarithmic-derivative quantum Fisher information with respect to the locally estimated frequency, without conditioning on reset-event times or using their record. The reset rate, dephasing rate, and energy basis are assumed known when the locally optimal measurement is chosen.

## Proof

**(1) Unique stationary full-rank qubit.** Write \(\rho=(I+x\sigma_x+y\sigma_y+z\sigma_z)/2\). The Bloch equations are

\[
\dot x=-(\gamma+r)x-\omega y+r,\qquad
\dot y=\omega x-(\gamma+r)y,\qquad
\dot z=-rz.
\]

All relaxation eigenvalues have strictly negative real parts because \(r,\gamma>0\), so the stationary state is unique, with

\[
x=\frac{r(r+\gamma)}{(r+\gamma)^2+\omega^2},\quad
y=\frac{r\omega}{(r+\gamma)^2+\omega^2},\quad z=0.
\]

The squared Bloch radius is \(r^2/((r+\gamma)^2+\omega^2)<1\); consequently, this state has full rank for every permitted parameter and the standard qubit QFI formula applies without rank-limit ambiguities:

\[
F_\omega=|\partial_\omega\boldsymbol s|^2+
\frac{(\boldsymbol s\cdot\partial_\omega\boldsymbol s)^2}{1-|\boldsymbol s|^2}.
\]

**(2) Exact QFI.** Direct differentiation, with \(\gamma,r\) fixed during the frequency derivative, gives

\[
F_\omega(r)=\frac{r^2(\gamma^2+\gamma r+\omega^2)
(\gamma^2+3\gamma r+2r^2+\omega^2)}
{(\gamma^2+2\gamma r+\omega^2)((\gamma+r)^2+\omega^2)^3}.
\]

Division by \(\gamma\) converts this into \(f(u,t)\) above. All denominators are positive for \(u>0,t\ge0\). Both boundary limits \(f(u,t)\to0\) as \(u\downarrow0\) and as \(u\to\infty\) follow directly from the rational expression.

**(3) Global uniqueness.** Exact polynomial differentiation gives

\[
\frac{\partial f}{\partial u}
=\frac{2uP(u,t)}{(1+2u+t)^2((1+u)^2+t)^4}.
\]

For any \(t\ge0\), the coefficient sequence of \(P\), in ascending degree order, comprises four strictly positive coefficients (degrees zero through three) followed by three strictly negative coefficients (degrees four through six). By Descartes' rule of signs, \(P(\cdot,t)\) has at most one positive real root, counted with multiplicity. As \(P(0,t)=(1+t)^4>0\) and \(P(u,t)\to-\infty\) as \(u\to\infty\), such a root exists, crosses sign, and is simple. Thus \(f\) strictly increases to precisely one positive root and strictly decreases thereafter. Its unique global maximum lies at that root.

**(4) Exact boundary and lower bound.** At \(t=0\), factorization gives

\[
P(u,0)=-(u-1)(u+1)^3(2u+1)^2,
\]

so \(u_*(0)=1\) and \(f(1,0)=1/16\). For \(t>0\) take \(b=\sqrt{1+t}>1\). A second exact factorization is

\[
P(b,b^2-1)=b^5(b-1)(b+1)^2>0.
\]

Since \(P\) changes sign only at \(u_*(t)\), this forces \(u_*(t)>b\), equivalently \(r_*>\sqrt{\gamma^2+\omega^2}\).

**(5) Local and large-frequency limits.** At \((u,t)=(1,0)\), the derivatives of \(P\) are \(\partial_u P=-72\) and \(\partial_t P=38\). The implicit function theorem gives \(u_*(t)=1+19t/36+O(t^2)\). For \(v=\sqrt t\to\infty\), for each fixed \(c>0\) the leading polynomial balance is

\[
\frac{P(cv,v^2)}{v^8}\longrightarrow 1+2c^2-2c^4.
\]

The limiting polynomial has exactly one positive root \(c_*=\sqrt{(1+\sqrt3)/2}\). For fixed \(c_-<c_*<c_+\), the finite-\(v\) polynomial has opposite signs at \(c_-v,c_+v\) for all sufficiently large \(v\); uniqueness traps \(u_*/v\) between them, and hence \(u_*/v\to c_*\). Evaluating the leading scaled QFI yields

\[
\lim_{v\to\infty}v^2 f(u_*(v^2),v^2)
=\frac{c_*^2(1+2c_*^2)}{(1+c_*^2)^3}=\frac{2\sqrt3}{9}.
\]

Restoring \(r,\gamma,\omega\) proves the stated asymptotics.

## Verification

The accompanying executable `verify_qfi.py` verifies the Bloch-formula reduction, exact rate derivative, the two decisive polynomial factorizations, local expansion coefficients and strong-detuning coefficient in symbolic arithmetic. It independently integrates the stationary reset-age mixture and solves the two-by-two density-matrix symmetric-logarithmic-derivative equation for 45 combinations of parameters (three dephasing strengths, five frequencies including negative and zero, three reset rates); it compares these numerical QFIs to the rational formula. It also checks the positive stationary root and local optimality in eight frequency cases. Run with `python verify_qfi.py` using Python 3.10+, SymPy, NumPy and SciPy. These finite checks supplement rather than prove the global uniqueness or asymptotic limits.

## Relationship to prior work

Magoni, Carollo, Perfetto and Lesanovsky (2022), arXiv:2202.12655, give quantum stochastic-reset stationary ensembles and many-spin correlations, including possible applications to sensing; their inspected Hamiltonian/reset protocols have no competing continuous pure-dephasing channel and do not establish this all-frequency single-qubit QFI rate optimizer. Wald et al. (2024), arXiv:2410.11497, analyze geometric discrete-time gates and stationary correlations; discrete-phase resonances do not yield the stated continuous-time dephasing optimum.

Li, Tong and Bao (2026), arXiv:2610.31249, derive a general reset-rate QFI response identity and analyze exact steady-state thermometry and **transient amplitude-damped** frequency sensing. Their general formula can be applied to this model, but the inspected results do not supply the exact positive pure-dephasing **stationary frequency** QFI or its global one-root optimization theorem. A closely related published discrete-time result, "Unique optimal reset probability for stationary qubit phase information" (2026), has been compared through its full available theorem and proof. Its exact stationary gate coherence is \(z=p/[1-(1-p)e^{i\theta}]\) and the optimal Bernoulli probability solves a degree-five equation; its coherent dynamics has no independent positive dephasing channel. The result cannot by straightforward parameter specialization provide the present stationary continuously dephased generator, degree-six root, or strict bound; it does supply the same universal strong-frequency limiting constant through a distinct singular discrete-gate limit. The qubit Bloch QFI identity is standard and is not new.

## Limitations

This is single-copy **local** frequency sensitivity of the stationary unconditioned density matrix, not quantum Fisher information per elapsed time, an adaptive whole-trajectory protocol, a frequency-global optimal measurement, a clock-precision claim, or a noise-tolerant implementation with finite reset overhead. The strict statements assume \(\gamma>0\), ideal state preparation, strictly positive reset rate, and a fixed calibrated dephasing rate. The undamped limit \(\gamma=0\) is not included. Although checked close publications do not state the theorem, a broader prior optimization obtained by specialization remains possible and independent priority review is outstanding.

## References

- M. Magoni, F. Carollo, G. Perfetto, I. Lesanovsky, *Emergent quantum correlations and collective behavior in non-interacting quantum systems subject to stochastic resetting*, arXiv:2202.12655, first public 2022-02-25, https://arxiv.org/abs/2202.12655.
- S. Wald, L. H. Yao, T. Platini, C. Hooley, F. Carollo, *Stochastic resetting in discrete-time quantum dynamics: steady states and correlations in few-qubit systems*, arXiv:2410.11497, first public 2024-10-15, https://arxiv.org/abs/2410.11497.
- S. Li, Q. Tong, R. Bao, *Reset-Enhanced Dissipative Quantum Metrology*, arXiv:2610.31249, first public 2026-10-22, https://arxiv.org/abs/2610.31249 (comparison only, outside the selected anchor period).
- Y. Zhong, Z. Sun, J. Ma, X. Wang, F. Nori, *Fisher information under decoherence in Bloch representation*, Phys. Rev. A **87** (2013), 022337, https://doi.org/10.1103/PhysRevA.87.022337 (standard QFI identity).
- *Unique optimal reset probability for stationary qubit phase information*, public 2026 mathematical research record, full result inspected, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-unique-optimal-reset-probability-for-stationary-qubit-phase-info--15941b8265f8 (only the accessible published summary was inspected).
