# Payoff-uniform finite-time sorting of edge environments in evolutionary games

## Finding

A three-class edge environment can be initially disordered, even with depleted-environment probabilities in the reverse order. In the regularized mean-field model of Betz, Fu and Masuda, all trajectories nevertheless attain the strict ordering
\[
\boxed{c_{CC}(t)<c_{CD}(t)<c_{DD}(t)}
\]
within an **explicit uniform finite time** independent of all payoffs, finite Fermi selection strengths, and initial states. The ordered gaps then remain bounded away from zero, even on an oscillatory cooperation trajectory.

Define
\[
\delta=\min\{q_1-q_0,p_0-p_1,q_2-q_1,p_1-p_2\}>0,
\]
\[
\mu=2\omega\min\{p_1+q_1,p_2+q_2\},\qquad
L=2\omega\max\{p_1+q_1,p_2+q_2\}+1-\omega,
\]
\[
T=\max\left\{\frac{\log2}{L},\frac1\mu\log\left(\frac{2L}{\omega\delta}\right)\right\}.
\]
Then for every admissible initial condition and every \(t\ge T\),
\[
\boxed{c_2(t)-c_1(t)\ge\frac{\omega\delta}{2L},\qquad c_3(t)-c_2(t)\ge\frac{\omega\delta}{2L}.}
\]
In particular, the same lower gap holds at **every time** of any complete trajectory contained in the unit state cube, including periodic and equilibrium trajectories.

## Assumptions and scope

Use the regularized four-dimensional well-mixed game equations (47)--(50) of Betz–Fu–Masuda (2026). Here \(x\in[0,1]\) is the fraction of cooperators, \(c_1,c_2,c_3\in[0,1]\) are the probabilities that a \(CC\), \(CD\), and \(DD\) edge, respectively, is in environmental state 0 (depleted). Environmental switching probabilities satisfy
\[
0<q_0<q_1<q_2<1,\qquad 1>p_0>p_1>p_2>0.
\]
Assume \(0<\omega<1\). The Fermi imitation probability \(\rho(t)\) is determined by the game and lies in \([0,1]\); no further assumption on it is used. In particular, no small-selection, no quasi-static environmental, and no convergence-of-cooperation assumption is imposed. Since each conditional equation is an inward-pointing affine vector field at \(c_j=0,1\) with nonnegative inter-class coupling, \([0,1]^3\) is positively invariant. The interval \([0,1]\) for \(x\) is invariant because \(\dot x\) has factor \(x(1-x)\).

## Proof

Put \(m(t)=(1-\omega)x(t)[1-\rho(t)]\) and \(n(t)=(1-\omega)[1-x(t)]\rho(t)\), so \(m,n\ge0\) and \(m+n\le1-\omega\). The source's equations (48)--(50) become
\[
\begin{aligned}
\dot c_1&=2\omega[q_0-(p_0+q_0)c_1]+2n(c_2-c_1),\\
\dot c_2&=2\omega[q_1-(p_1+q_1)c_2]+m(c_1-c_2)+n(c_3-c_2),\\
\dot c_3&=2\omega[q_2-(p_2+q_2)c_3]+2m(c_2-c_3).
\end{aligned}
\]
Define differences \(u=c_2-c_1\) and \(v=c_3-c_2\). Exact subtraction gives the affine cooperative system
\[
\binom{\dot u}{\dot v}=
\underbrace{\begin{pmatrix}
-2\omega(p_1+q_1)-m-2n & n\\
m & -2\omega(p_2+q_2)-2m-n
\end{pmatrix}}_{B(t)}\binom{u}{v}+
2\omega\binom{(q_1-q_0)(1-c_1)+(p_0-p_1)c_1}{(q_2-q_1)(1-c_2)+(p_1-p_2)c_2}.
\]
Both forcing coordinates are at least \(2\omega\delta\) because \(c_1,c_2\in[0,1]\). The matrix \(B(t)\) has nonnegative off-diagonal entries and its row sums lie between \(-L\) and \(-\mu\). Let \(\Phi(t,s)\) be its (nonnegative) state-transition matrix. Comparison of the solutions starting from the all-one vector gives
\[
 e^{-L(t-s)}\mathbf1\le\Phi(t,s)\mathbf1\le e^{-\mu(t-s)}\mathbf1\qquad (t\ge s).
\]
Since \(u(0),v(0)\ge-1\), the variation-of-constants formula, positivity of \(\Phi\), and the two bounds yield, componentwise,
\[
\binom{u(t)}{v(t)}\ge
\left[-e^{-\mu t}+\frac{2\omega\delta}{L}(1-e^{-Lt})\right]\mathbf1.
\]
For \(t\ge(\log2)/L\), the positive term is at least \(\omega\delta/L\). For \(t\ge\mu^{-1}\log[2L/(\omega\delta)]\), the negative term is at most \(\omega\delta/(2L)\). Combining the two proves the displayed positive gap. The logarithm is positive because \(2L/(\omega\delta)>1\) under the stated probability inequalities.

For any **complete** trajectory lying in the cube for all real times, apply this result at time \(t-T\) and evaluate at \(t\). Its starting state is admissible for each \(t\), so the gap applies at every real time. Thus even a nonconstant periodic cooperation oscillation cannot reverse the environment ranking once represented by a complete invariant trajectory.

## Verification

Run `python3 checker.py` with SymPy available. It symbolically subtracts the three source equations and verifies the exact cooperative difference system, including the factors 2 attached to the outer edge types. With SciPy available it additionally stress-tests the quantitative lower bound for strongly time-varying, externally imposed imitation and cooperation histories and four initially disordered edge states. Those finite simulations are corroboration only: the proof applies to arbitrary measurable histories with \(0\le x,\rho\le1\), and to all times, by positivity of the transition matrix and comparison.

## Relationship to prior work

Betz, Fu and Masuda (2026) derive the four-dimensional regularized mean-field system and study its boundary equilibria and possible oscillations. The inspected model, equilibrium, and discussion sections do not assert a payoff-independent **finite sorting horizon with a uniform strictly positive inter-class gap**, nor do the oscillation results prohibit persistent reversal of the ordering. The same authors' 2024 two-community work assigns its three environments by community-edge types, not by \(CC\), \(CD\), and \(DD\) strategy pairs. Classical monotone linear-system comparison is the proof technique, not the novelty claim. The specific quantitative environmental-order constraint on all model trajectories is the contribution.

## Limitations

The explicit \(T\) and gap are sufficient and may not be optimal. The time bound becomes large as environmental updates become rare or switching-rate inequalities become weak. The proof concerns deterministic regularized mean-field conditional fractions, including auxiliary conditional fractions at the pure-strategy boundary; it does not prove the same sorting property for realized finite-network edge counts or pair-approximation equations. Historical priority beyond inspected primary references requires independent assessment.

## References

1. K. Betz, F. Fu, N. Masuda, *Evolutionary games on networks with negative edge-based environmental feedback*, arXiv:2611.11029v1, first publicly posted November 8, 2026, https://arxiv.org/html/2611.11029v1.
2. K. Betz, F. Fu, N. Masuda, *Evolutionary Game Dynamics with Environmental Feedback in a Network with Two Communities*, *Bulletin of Mathematical Biology* 86, 84 (2024), https://doi.org/10.1007/s11538-024-01310-3.
