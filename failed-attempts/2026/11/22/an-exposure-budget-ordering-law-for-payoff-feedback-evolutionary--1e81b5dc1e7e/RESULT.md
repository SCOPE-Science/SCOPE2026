# An exposure-budget ordering law for payoff-feedback evolutionary games

## Finding
For the scalar strategy–payoff feedback replicator model of Chen, Zhang and Li [1], interventions with distinct positive payoff contrasts have a **universal strict order** for maximizing their final cooperative share. Write
\[
 g(x)=x(1-x)(2x-1),\qquad f_i(x)=g(x)(A_i+B_i x),
 \qquad A_i=S_i-P_i>0,\quad B_i=R_i-T_i-S_i+P_i.
\]
Fix any finite collection of regimes, each held for a prescribed positive total time, and define the dimensionless index \(\kappa_i=B_i/A_i\). Among all finite switching sequences using exactly these total times, applying the regimes in **increasing order of \(\kappa_i\)** maximizes the terminal cooperation fraction for every initial \(x_0\in(0,1)\setminus\{1/2\}\). Decreasing order minimizes it. Every adjacent inversion with strictly different indices strictly worsens the result, independently of the duration of the other blocks and the initial fraction; tied-index regimes commute.

The order has a sharp long-term consequence. Two positive-payoff interventions with fixed equal exposure times can send the same initial population to opposite basins of a fixed, subsequently unaltered game: one order leads to full cooperation while the reverse leads to the interior fraction \(1/2\).

## Assumptions and scope
Take the reduced, well-mixed, deterministic replicator model with a two-strategy state \(x\in[0,1]\). In each constant-payoff regime \(i\), the environmental-feedback payoff matrix is
\[
 U_i(x)=(1-x)\begin{pmatrix}T_i&P_i\\R_i&S_i\end{pmatrix}
          +x\begin{pmatrix}R_i&S_i\\T_i&P_i\end{pmatrix}.
\]
Payoffs \(R_i,S_i,T_i,P_i\) are strictly positive real numbers, and \(A_i=S_i-P_i>0\). A schedule is a finite, piecewise-constant sequence of regimes with prescribed total exposure times \(t_i>0\) (total horizon \(T=\sum_i t_i\)). Splitting a regime across multiple intervals is allowed. At switching instants the state is continuous; each flow is solved exactly between switches. Every initial \(x_0\in(0,1)\setminus\{1/2\}\) remains within its connected invariant half-interval. Boundaries and \(x_0=1/2\) are fixed for every regime, hence do not give strict ordering.

The underlying model, and not an arbitrary extension involving a second independent resource state, is the setting of this result. The resulting monotonicity concerns **terminal cooperation**, not discounted cumulative welfare or ecological outcomes under additional differential equations.

## Proof
The standard replicator payoff difference calculated directly from the matrix above is
\[
 (U_i(x)(x,1-x)^\mathsf T)_1-(U_i(x)(x,1-x)^\mathsf T)_2
 =(2x-1)[A_i+B_i x].
\]
Consequently \(\dot x=f_i(x)=g(x)(A_i+B_i x)\). Every \(f_i\) is a smooth polynomial, so it defines an increasing order-preserving flow \(\phi_i^s\) on \((0,1)\). The points \(0,1/2,1\) are shared equilibria and cannot be crossed in finite time.

For any two regimes \(i,j\), the scalar Lie bracket in the convention used here satisfies the exact identity
\[
 W_{ij}(x):=f_i(x)f_j'(x)-f_j(x)f_i'(x)
 =A_i A_j(\kappa_j-\kappa_i)g(x)^2.
\]
In particular \(W_{ij}>0\) at all nonfixed interior states whenever \(\kappa_i<\kappa_j\). Put
\[
 H(t,u)=(\partial_u\phi_j^t(u))f_i(u)-f_i(\phi_j^t(u)).
\]
Since \(H(0,u)=0\), differentiation with respect to \(t\) gives the **exact variational equation**
\[
 \partial_tH=f_j'(\phi_j^t(u))H+W_{ij}(\phi_j^t(u)).
\]
The integrating-factor formula implies \(H(t,u)>0\) for every \(t>0\) and \(u\in(0,1)\setminus\{1/2\}\). For fixed \(t>0\) and initial state \(u\), the curve \(z(s)=\phi_j^t(\phi_i^s(u))\) therefore satisfies
\[
 z'(s)=f_i(z(s))+H(t,\phi_i^s(u))>f_i(z(s)),
 \qquad z(0)=\phi_j^t(u).
\]
Scalar ODE comparison with \(w(s)=\phi_i^s(\phi_j^t(u))\) yields, for every \(s,t>0\),
\[
 \boxed{\phi_j^t\circ\phi_i^s(u)>\phi_i^s\circ\phi_j^t(u)
 \quad\text{if}\quad\kappa_i<\kappa_j.}
\]
Thus the lower-index block must occur first for a larger final share. Swapping any adjacent inversion strictly improves the end state, because every remaining subsequent flow is strictly increasing. A finite inversion-sort sends every schedule to increasing index order, while preserving the total time of each regime. Consecutive blocks of a given regime merge by the semigroup law. If two indices agree, the respective vector fields are positive multiples of the common polynomial \(g(x)(1+\kappa_i x)\), and their flows commute. This proves the global optimum, strictness apart from ties, and the minimum by reversing all comparisons.

For an exact, positive-payoff basin-switching witness set \(x_0=3/4\), with each intervention applied for exactly eight time units, and use the following ordered payoff quadruples \((R,S,T,P)\):
\[
 \begin{array}{c|c|c|c}
 \text{regime}&(R,S,T,P)&(A,B)&\kappa\\\hline
 E&(1,10,4,1)&(9,-12)&-4/3\\
 B&(2,2,1,1)&(1,0)&0\\
 G&(9/8,1/8,1,1)&(-7/8,1)&\text{not applicable}
 \end{array}
\]
Here \(E\) and \(B\) are interventions; \(G\) is a common fixed baseline to which the system switches **after** the two intervention blocks, not part of the ordering theorem. The three vector fields simplify to
\[
 f_E=12g(x)(3/4-x),\qquad f_B=g(x),\qquad f_G=g(x)(x-7/8).
\]
Because \(x_0=3/4\) is an equilibrium of \(E\), application of \(E\) first leaves the state unchanged. During the following \(B\) block, while \(3/4\le x\le7/8\), one has \(\dot x=g(x)\ge(3/4)(1/8)(1/2)=3/64\). Traversing the distance \(1/8\) must therefore take at most \(8/3\) time units, strictly less than eight. Hence the terminal state \(z_{EB}=\phi_B^8\circ\phi_E^8(3/4)\) is strictly above \(7/8\).

For the reversed order, let \(z_B=\phi_B^8(3/4)\). With \(y=1-x\), the \(B\) equation implies \(y'= -x(2x-1)y\ge-y\), hence \(1-z_B\ge e^{-8}/4\). In the subsequent \(E\) block the state decreases toward \(3/4\) but never reaches it. If it remained at least \(7/8\) for all eight units, then with \(y=1-x\) it would satisfy
\[
 y'=12x(2x-1)(x-3/4)y\ge\frac{63}{64}y,
\]
so that \(y(8)\ge (e^{-8}/4)e^{63/8}=e^{-1/8}/4>1/8\), contradicting \(x(8)\ge7/8\). Therefore \(3/4<z_{BE}=\phi_E^8\circ\phi_B^8(3/4)<7/8\). In regime \(G\), the interior point \(7/8\) is a separating repeller: all states in \((1/2,7/8)\) converge to \(1/2\), and all states in \((7/8,1)\) converge to \(1\). Thus identical exposure budgets and positive payoff matrices yield respectively \(1\) and \(1/2\) as asymptotic cooperation fractions solely through their temporal order.

## Verification
The standalone `checker.py` recomputes the payoff-to-vector-field reduction, the exact bracket identity, all three rational witness vector fields, and the rational inequalities bounding the two eight-unit trajectories. Its numerical ODE integration is explicitly illustrative; the rigorous inequalities and scalar comparison above establish the statement for all permitted starting states and positive durations, and establish the asymptotic basin result without numerical extrapolation.

Run with `python checker.py` in an environment with SymPy and SciPy. It reports whether the exact symbolic and rational checks pass, and prints two illustrative endpoints. The derivation above is self-contained independently of software.

## Relationship to prior work
Chen, Zhang and Li [1] derive the feedback payoff matrix and autonomous scalar replicator reduction, then analyze equilibria, phase transitions, and game parameter effects. Those are inputs here, not claimed as new. The new statement compares **all fixed-budget finite schedules** of different payoff regimes and yields the explicit opposite-basin witness. Stuckey and colleagues [2] study optimal incentive scheduling in a Hawk–Dove evolutionary game under a different time-optimal control formulation, rather than a universal fixed-exposure permutation rule for the feedback game here. Standard scalar-flow Lie brackets are known control tools; the bracket manipulation itself is not claimed novel, but its strict fixed-budget ordering consequence and basin-switching example are the tested mathematical additions. Broader scalar switched-system rearrangement theorems may encompass the comparison principle; historical priority has not been independently established.

## Limitations
Only finitely many switching intervals are treated, each switching regime has \(S_i>P_i\), and the optimization criterion is the terminal scalar cooperation fraction. No conclusion is made for arbitrary signed contrasts, independent environment state dynamics, dynamic welfare, stochastic or spatial populations, or genuinely different objectives. The source's autonomous analysis alone does not imply this scheduling result; conversely, the standard positive-bracket comparison may have precedents outside evolutionary game theory. The result has undergone a self-review but no independent scientific audit.

## References
[1] Y. Chen, J.-Q. Zhang and B.-Q. Li, *Cooperation Dynamics with Environmental Feedback: Steady States and Transitions*, arXiv:2610.21575 (first public version 2026-10-15), https://arxiv.org/abs/2610.21575 .

[2] K. Stuckey, D. Dua, C. Ma, M. Parker and J. Newton, *Optimal dynamic incentive scheduling for Hawk-Dove evolutionary games*, Physical Review E **105**, 014412 (2022), https://doi.org/10.1103/PhysRevE.105.014412 .
