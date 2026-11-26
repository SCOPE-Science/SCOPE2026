# Exact extinction census and boundary-sensitive spectral law for three-state excitation on open ladders

## Finding
For an integer \(n\ge2\), let \(L_n=P_n\square K_2\) be the open two-rail ladder with \(2n\) labelled vertices. In the deterministic three-state Greenberg–Hastings model defined below, write \(E_n\) for the number of initial configurations whose trajectories eventually reach the all-resting configuration. Then
\[
E_1=9,\quad E_2=57,\quad E_n=7E_{n-1}-4E_{n-2}\quad(n\ge3),
\]
where the first term is the counting seed for \(P_1\square K_2\). Hence
\[
\sum_{n\ge1}E_nz^n=\frac{9z-6z^2}{1-7z+4z^2}.
\]
Set \(\lambda_\pm=(7\pm\sqrt{33})/2\). The closed form is
\[
E_n=\frac{9+51/\sqrt{33}}2\lambda_+^{n-1}+\frac{9-51/\sqrt{33}}2\lambda_-^{n-1}.
\]
For uniformly random initial states, this gives the **sharp exponential extinction probability**
\[
\frac{E_n}{9^n}\sim\frac{9+51/\sqrt{33}}{2\lambda_+}\left(\frac{\lambda_+}{9}\right)^n.
\]
This is a boundary-sensitive count of *initial configurations*, not an assertion about numbers or primitive periods of other attractors.

## Assumptions and scope
The vertices are \((i,j)\) with \(1\le i\le n\), \(j\in\{0,1\}\). Vertices in each rung are adjacent, as are successive vertices on each rail; there is **no edge joining the first and last rungs**. An initial configuration is any \(x:V(L_n)\to\{0,1,2\}\). Updates are simultaneous: \(1\to2\), \(2\to0\), and \(0\to1\) if and only if some adjacent vertex is \(1\), otherwise \(0\to0\). An orbit *extinguishes* if it reaches the all-zero state at some finite time. In the expressions above, \(E_1\) is defined on the one-rung graph, although the main family starts at \(n=2\).

For \(a,b\in\{0,1,2\}\), define \(\delta(a,b)\) as the unique integer in \(\{-1,0,1\}\) congruent to \(b-a\) modulo \(3\). For an oriented cycle \(C=(v_0,v_1,\ldots,v_k=v_0)\), its circulation is \(\omega_x(C)=\sum_{i=0}^{k-1}\delta(x(v_i),x(v_{i+1}))\). Reverse orientation changes its sign. The elementary squares are the \(n-1\) consecutive rung rectangles.

## Proof
**1. Exact zero-circulation criterion on connected finite graphs.** Let \(G\) be any finite connected simple graph with this update. Define \(\varepsilon_t(v)\in\{0,1\}\) to be \(1\) exactly when the site's color advances by one modulo \(3\) at the step. For adjacent \(u,v\), one has
\[
\delta(x_{t+1}(u),x_{t+1}(v))=\delta(x_t(u),x_t(v))+\varepsilon_t(v)-\varepsilon_t(u).
\]
Indeed both sides are congruent modulo \(3\), so it suffices that the right side lies in \(\{-1,0,1\}\). If the old difference is \(+1\), the possible ordered colors are \((0,1),(1,2),(2,0)\). In each case \(\varepsilon_t(v)\le\varepsilon_t(u)\): for the first pair the resting site has an excited neighbour, for the second both advance, and for the third the first site advances. The \(-1\) case is its reversal; the zero case is automatic. Summing around any cycle telescopes the last two terms. Thus all cycle circulations are time-invariant. Extinction forces them all to be zero.

Conversely suppose all initial cycle circulations are zero. Choose a root and integrate the edge differences \(\delta\) along paths to construct an integer-valued height \(h_0\) satisfying \(h_0(v)\equiv x_0(v)\pmod3\) and \(|h_0(u)-h_0(v)|\le1\) on edges. Path independence follows from zero circulation on all cycles. The displayed edge identity permits heights to evolve by \(h_{t+1}(v)=h_t(v)+\varepsilon_t(v)\), preserving both the residues and the edge-Lipschitz bound. Set \(H\) to the least multiple of \(3\) not smaller than \(\max_v h_0(v)\). Inductively, all heights remain at most \(H\): a vertex already at height \(H\) has state \(0\) and can have no excited neighbour, because each neighbour has height at least \(H-1\), whose residues are \(2\) or \(0\); vertices below \(H\) advance by at most one. Heights are nondecreasing bounded integers, hence eventually constant. In a stationary height vector no vertex has state \(1\) or \(2\), as either would advance unconditionally. The color vector is therefore all zero. This proves the criterion for every connected finite graph, independently of numerical experiments.

**2. Square basis of the open ladder.** The oriented boundaries of its \(n-1\) elementary squares are an integral cycle basis: every cycle circulation is an integer combination of square circulations, as may be seen by successively removing the rightmost enclosed face (or by the planar cycle-space basis). Thus the global zero condition is equivalent to zero circulation on each square, with no additional longitudinal winding constraint.

**3. Two-type transfer.** Represent a rung by its ordered color pair \((a,b)\). A consecutive pair of rungs \((a,b)\) and \((c,d)\) is compatible exactly when
\[
\delta(a,c)+\delta(c,d)+\delta(d,b)+\delta(b,a)=0.
\]
Classify the old rung as *equal* if \(a=b\) and *unequal* otherwise. Direct enumeration of the nine possibilities for the next rung yields the following **exact transition counts**, independent of its particular colors:
\[
\begin{array}{c|cc}&\text{next equal}&\text{next unequal}\\\hline
\text{old equal}&3&4\\
\text{old unequal}&2&4\end{array}.
\]
For a direct verification, when the old colors agree the new three-color boundary cannot contain all three distinct values, excluding precisely two of nine ordered new rungs. For unequal old colors, the condition allows two of the three equal next rungs and four of the six unequal next rungs; evaluating the displayed four-edge sum for any representative old pair, and applying a common color translation and an exchange of the two rail labels, proves all cases.

Let \(f_e(k)\) and \(f_u(k)\) count compatible choices of the following \(k-1\) rungs when the first rung is prescribed to be equal or unequal, respectively. Then
\[
\binom{f_e(k+1)}{f_u(k+1)}=\begin{pmatrix}3&4\\2&4\end{pmatrix}\binom{f_e(k)}{f_u(k)},\qquad f_e(1)=f_u(1)=1.
\]
There are three possible initial equal rungs and six unequal rungs, so \(E_k=3f_e(k)+6f_u(k)\). The transfer matrix has characteristic polynomial \(z^2-7z+4\), yielding the recurrence. At length one, \(E_1=9\); at length two, \(E_2=3(3+4)+6(2+4)=57\). Solving the second-order recurrence yields the rational generating function, closed form and asymptotics stated above. As \(\lambda_+\in(0,9)\) and \(|\lambda_-|<\lambda_+\), the leading term is strictly positive and the extinction probability decreases exponentially.

## Verification
An independent, dependency-free program `VERIFY_LADDER.py` constructs graph neighbours, iterates the local rule, detects finite orbits and directly counts extinguishing states for each \(n\in\{2,3,4,5\}\). It independently computes local square circulations, cross-checks membership of every one of the \(81+729+6561+59049=66420\) initial configurations, verifies each of the nine transfer rows and checks the formula. Recorded output is in `VERIFY_OUTPUT.txt`. This finite check supports the algebraic proof; it is not used as a proof for arbitrary \(n\).

## Relationship to prior work
Durrett and Griffeath, *Asymptotic Behavior of Excitable Cellular Automata* (first posted March 22, 1993), studies classical excitable models and spiral behaviour. Doba (2018), Theorem 1 in Section 6, establishes on **arbitrary finite connected graphs** the zero-circulation extinction criterion that we also prove directly above; this criterion is **known**, not a novel part of the finding. The present specialization determines the exact count of all extinction-producing **initial configurations** on every open ladder and the unexpectedly small two-type transfer, recurrence and leading exponential constant. Doba's inspected full text (Sections 2–7, including its theorem and conclusion) does not contain an open-ladder initial-state enumeration. A previously recorded result for **circular** ladders \(C_n\square K_2\) uses a nine-state Laurent transfer with an extra noncontractible winding constraint and a Gaussian correction; its statement neither gives nor implies the present open-boundary recurrence without a separate boundary transfer analysis. Finite ladders and circular ladders have different cycle spaces and different asymptotic polynomial factors.

## Limitations
No theorem about extinction **times**, full recurrent orbit counts or the dynamics on wider strips is claimed. The graph-wide winding criterion is previously established, and only the new exact open-ladder census and derived asymptotic are presented as the candidate contribution. The literature comparison is bounded; a past enumeration of equivalent ladder zero-circulation colorings outside the inspected sources could subsume this formula. The proof concerns deterministic threshold-one updates only, not stochastic excitation or larger refractory alphabets.

## References
1. R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, arXiv:patt-sol/9303002v1, first submitted 1993-03-22, https://arxiv.org/abs/patt-sol/9303002 .
2. N. Doba, *The Time Evolution of a Greenberg–Hastings Cellular Automaton on a Finite Graph*, *Complex Systems* **27** (2018), 101–126, DOI:10.25088/ComplexSystems.27.2.101, https://content.wolfram.com/sites/13/2018/09/27-2-1.pdf .
3. M. Kesseböhmer, J. D. M. Rademacher and D. Ulbrich, *Dynamics and topological entropy of 1D Greenberg–Hastings cellular automata*, *Ergodic Theory and Dynamical Systems* **41** (2021), 1397–1430, DOI:10.1017/etds.2020.18 .
