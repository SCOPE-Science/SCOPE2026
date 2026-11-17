# Peripheral trapping on a dephased quantum star has an exact \(m^{3/2}\) optimum

## Finding
For an excitation initially localized on an untrapped leaf of a uniformly coupled star with one *different leaf* acting as an irreversible sink, the exact unconditional mean capture time is
\[
T_m(\gamma,\kappa)=\frac{m+2}{\kappa}+\frac{m-1}{\gamma}
+\frac{m(m-1)}{2(\gamma+\kappa/2)}
+\frac{(m+2)\gamma+(m+1)\kappa/2}{2J^2}.
\]
For every integer \(m\ge 2\), every nonzero real hopping \(J\), and every fixed \(\kappa>0\), the unique dephasing-rate minimizer \(\gamma_m^*>0\) is characterized by
\[
\frac{m+2}{2J^2}=\frac{m-1}{\gamma_m^{*2}}+
\frac{m(m-1)}{2(\gamma_m^*+\kappa/2)^2}.
\]
For fixed \(J,\kappa\) and \(m\to\infty\),
\[
\frac{\gamma_m^*}{|J|\sqrt m}\to1,\qquad
\frac{\min_{\gamma>0}T_m(\gamma,\kappa)}{m^{3/2}/|J|}\to1.
\]
The function is also strictly convex and coercive on the full positive \((\gamma,\kappa)\)-quadrant, so the jointly optimized pair is unique, and
\[
\lim_{m\to\infty}\frac{\min_{\gamma,\kappa>0}T_m(\gamma,\kappa)}{m^{3/2}/|J|}=1.
\]
The exponent \(3/2\) is a peripheral-trap penalty not captured by a single localized two-site approximation.

## Assumptions and scope
The star has vertex set \(\{h,t,o_1,\ldots,o_m\}\), hub \(h\), trapping leaf \(t\), and \(m\ge2\) equivalent ordinary leaves. In the one-excitation site basis, \(H=J\sum_{v\ne h}(|h\rangle\langle v|+|v\rangle\langle h|)\), with \(J\in\mathbb R\setminus\{0\}\). Projectors are \(P_v=|v\rangle\langle v|\). The trace-decreasing master equation on the nonabsorbed sector is
\[
\dot\rho=-i[H,\rho]+\gamma\sum_v\bigl(P_v\rho P_v-\tfrac12\{P_v,\rho\}\bigr)-\tfrac\kappa2\{P_t,\rho\}.
\]
The dephasing convention is *offdiagonal decay rate exactly \(\gamma\)*. All claims require \(\gamma,\kappa>0\) except the limiting statements. The initial density is \(\rho(0)=|o_1\rangle\langle o_1|\). The unconditional mean first-capture time is \(T=\int_0^\infty\operatorname{tr}\rho(s)\,ds\); loss to the distinguished sink is the only population loss.

## Proof
**Step 1: complete absorption.** The finite-dimensional evolution is positive and trace-nonincreasing; its trace derivative equals \(-\kappa\rho_{tt}\). If a nonzero positive invariant state existed, its trap diagonal and hence entire trap row would vanish. The \((t,h)\) entry of the stationary master equation then forces \(\rho_{hh}=0\) and, by positivity, all hub coherences vanish. At stationarity every ordinary-leaf offdiagonal then solves \(0=-\gamma\rho_{o_i o_j}\), and the \((h,o_j)\) entry forces each ordinary-leaf diagonal to vanish. This is impossible for a nonzero state. A nonvanishing survival limit would have a nonzero positive invariant Cesàro limit, so survival tends to zero and the generator has no zero eigenvalue on the physical Hermitian operator space. The same stationary argument excludes any nondecaying oscillatory sector; more concretely, the bounded finite-dimensional positive semigroup has no nonzero invariant positive element, hence its integrals are finite by the standard finite-dimensional spectral/positivity argument.

**Step 2: permutation reduction.** Since the generator and the capture-time functional are invariant under permutations of the \(m\) untrapped leaves, the localized initial density has the same mean as the uniform incoherent mixture \(m^{-1}\sum_iP_{o_i}\). Fix the labels, and introduce real quantities \(a=\rho_{tt}\), \(b=\rho_{hh}\), \(c=\rho_{o_i o_i}\), \(d=\rho_{o_i o_j}\) for \(i\ne j\), \(e=\operatorname{Im}\rho_{th}\), \(f=\operatorname{Im}\rho_{ho_i}\), \(g=\rho_{to_i}\). In this invariant real sector the complete equations are
\[
\begin{aligned}
\dot a&=-2Je-\kappa a, & \dot b&=2J(e-mf), & \dot c&=2Jf,\\
\dot d&=2Jf-\gamma d, & \dot e&=-J(b-a-mg)-(\gamma+\kappa/2)e,\\
\dot f&=-J(g+c+(m-1)d-b)-\gamma f, &
\dot g&=J(f-e)-(\gamma+\kappa/2)g.
\end{aligned}
\]
Initially \(c(0)=1/m\) and the other variables vanish. No other matrix entries are generated.

**Step 3: integrate the equations.** Write \(A,B,C,D,E,F,G\) for the integrals of \(a,b,c,d,e,f,g\), respectively. The first four equations and complete absorption give
\[
F=-\frac1{2Jm},\quad E=-\frac1{2J},\quad
A=\frac1\kappa,\quad D=-\frac1{m\gamma}.
\]
The last three give
\[
G=\frac{m-1}{2m(\gamma+\kappa/2)},\qquad
B=A+mG+\frac{\gamma+\kappa/2}{2J^2},\qquad
C=B-G-(m-1)D+\frac{\gamma}{2J^2m}.
\]
Thus \(T=A+B+mC\), which simplifies exactly to the stated formula. This derivation is valid for every integer \(m\ge2\) and every \(J\ne0\), \(\gamma,\kappa>0\).

**Step 4: optimization and asymptotics.** Differentiation at fixed \(\kappa\) gives
\[
\partial_\gamma T=\frac{m+2}{2J^2}-\frac{m-1}{\gamma^2}-\frac{m(m-1)}{2(\gamma+\kappa/2)^2}.
\]
It is strictly increasing from \(-\infty\) to a positive limit and hence has one root, the unique global minimum. Setting \(\gamma=c|J|\sqrt m\) in this equation shows that the root has \(c\to1\); direct substitution gives the minimum-time limit. For simultaneous optimization, the reciprocal terms \(1/\kappa\), \(1/\gamma\), and \(1/(\gamma+\kappa/2)\) are convex; the first two give a positive-definite Hessian, whereas the positive linear terms give coercivity at infinity. The unique positive global minimizer therefore exists. Put \(z=\gamma+\kappa/2\). The exact formula implies
\[
T\ge\frac{m(m-1)}{2z}+\frac{(m+1)z}{2J^2}
\ge\frac{\sqrt{m(m-1)(m+1)}}{|J|}.
\]
Taking \(\gamma=\kappa=2|J|\sqrt m/3\), so \(z=|J|\sqrt m\), gives \(T=m^{3/2}/|J|+O(\sqrt m/|J|)\) for fixed nonzero \(J\), proving the joint optimum asymptotic.

## Verification
The standalone `verify_leaftrap.py` constructs the full \((m+2)^2\)-dimensional Lindblad superoperator, rather than the seven-coordinate reduction, and solves the full complex linear system for the integrated density matrix. It compares that trace with the symbolic formula for 90 combinations of \(m\), \(J\), \(\gamma\), and \(\kappa\). Execute with `python verify_leaftrap.py` (requires Python and NumPy). These are finite consistency tests; the uniform all-\(m\) assertion rests on the complete analytical reduction and convexity argument, not finite sampling.

## Relationship to prior work
Plenio and Huelga's 2008 work introduced dephasing-assisted quantum transport in finite networks. Caruso and collaborators (2009) analyzed invariant dark spaces and pure dephasing on fully connected networks, not a leaf-absorbing star and its mean capture-time minimizer. Wu, Cao and Silbey (2012) formulated general weak/strong-noise mean-passage scaling, not this exact finite-\(m\) law. Novo and collaborators (2014) treated star geometry and quantum transport via unitary invariant-subspace reductions, without site dephasing in the displayed star trapping formula. An earlier result for trapping at the *hub* of a star is not equivalent under any graph automorphism to trapping at a leaf, and does not determine the additional mixed-rate term and the peripheral large-star asymptotic.

## Limitations
This is a theoretical trace-decreasing Markovian single-excitation Lindblad model with uniform on-site energies, uniform hopping and uniform dephasing. The time is the unconditional first-capture mean, not the median, a finite-horizon efficiency, or a conditional mean in a noncapturing model. No claim is made for non-Markovian baths, nonidentical arm couplings, disorder, multi-excitation interactions, or experimental realization. The numerical checks do not establish the infinite-family theorem independently. Literature priority beyond the examined sources is not certified by this manuscript.

## References
- M. B. Plenio and S. F. Huelga, *Dephasing assisted transport: Quantum networks and biomolecules*, arXiv:0807.4902v1 (public 2008-07-30), https://arxiv.org/html/0807.4902v1.
- F. Caruso, A. W. Chin, A. Datta, S. F. Huelga, M. B. Plenio, *Highly efficient energy excitation transfer in light-harvesting complexes: The fundamental role of noise-assisted transport*, arXiv:0901.4454v1 (public 2009-01-28), https://arxiv.org/html/0901.4454v2.
- J. Wu, J. Cao, R. J. Silbey, *Generic Mechanism of Optimal Energy Transfer Efficiency: A Scaling Theory of the Mean First Passage Time in Exciton Systems*, arXiv:1207.6197 (public 2012-07-26), https://arxiv.org/abs/1207.6197.
- L. Novo et al., *Systematic Dimensionality Reduction for Quantum Walks: Optimal Spatial Search and Transport on Non-Regular Graphs*, arXiv:1412.7209 (public 2014-12-22), https://arxiv.org/abs/1412.7209.
