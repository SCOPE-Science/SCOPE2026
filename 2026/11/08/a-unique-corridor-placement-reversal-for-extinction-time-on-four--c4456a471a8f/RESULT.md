# A unique corridor-placement reversal for extinction time on four habitat patches

## Finding

Consider four suitable habitat patches connected initially in a path \(1-2-3-4\). Exactly one undirected colonization corridor may be added, with the same positive per-edge colonization rate \(c\) as the existing corridors. Up to path reflection there are exactly two options: the endpoint link \(\{1,4\}\), producing the four-cycle \(C_4\), and the short link \(\{1,3\}\), producing a triangle with one pendant patch, denoted \(P\). In the continuous-time occupied/empty patch process defined below, all four patches start occupied. Let \(T_C(c)\) and \(T_P(c)\) be the respective mean times to global extinction.

**Theorem.** There is exactly one threshold \(c_*>0\), with \(1.079524<c_*<1.079525\), such that

\[
T_P(c)>T_C(c)\quad(0<c<c_*),\qquad
T_P(c)=T_C(c)\quad(c=c_*),\qquad
T_C(c)>T_P(c)\quad(c>c_*).
\]

The threshold is the unique positive root of

\[
\begin{aligned}
P_9(c)={}&648c^9+3504c^8+8486c^7+10624c^6+4144c^5\\
&-7529c^4-13801c^3-10608c^2-4176c-684.
\end{aligned}
\]

The adjacency spectral radius of the triangle-with-tail graph is strictly larger than that of the four-cycle for all choices of the colonization rate. Thus its larger spectral radius does not give a uniform ranking of finite-population mean persistence. The theorem completely resolves the choice of one additional corridor on the four-patch path, but does not assert an optimum for larger graphs.

## Assumptions and scope

The patches are labeled \(V=\{1,2,3,4\}\). A configuration is the occupied subset \(A\subseteq V\). Every occupied patch independently becomes empty at rate \(1\). For each edge joining an occupied patch to an empty patch, the empty patch is colonized at rate \(c>0\), with contributions from distinct occupied neighbors added. Empty-all is absorbing; there is no external immigration or catastrophe. Time is measured in units of inverse local-extinction rate. Initially \(A=V\). The object is the **unconditional mean time until the first all-empty configuration**, not a quasistationary lifetime or a deterministic mean-field threshold. Because the chain is finite and from every nonempty state an uninterrupted sequence of local extinctions can reach the absorbing state, absorption is almost sure and the mean is finite.

Write \(G_C=(V,\{12,23,34,14\})\) and \(G_P=(V,\{12,23,34,13\})\), with unordered edge notation. Each contains four vertices and four edges, so costs and individual corridor strengths are matched. The remaining missing edge \(\{2,4\}\) produces a graph isomorphic to \(G_P\) by path reflection. This is therefore an exhaustive discrete choice for one added edge.

## Proof

For any nonempty \(A\), write \(t_A(G,c)\) for the expected absorption time and set \(t_\varnothing=0\). Let \(m_v(A)=|\{u\in A:\{u,v\}\in E(G)\}|\) for \(v\notin A\). First-step conditioning gives the exact backward system

\[
\Big(|A|+c\sum_{v\notin A}m_v(A)\Big)t_A
-\sum_{v\in A}t_{A\setminus\{v\}}
-c\sum_{v\notin A}m_v(A)t_{A\cup\{v\}}=1.
\]

This is a system of \(15\) linear equations for the \(15\) nonempty states, with a unique solution because the killed chain has finite mean absorption time. Reducing states by the automorphism group of \(G_C\) yields \(5\) equations; for \(G_P\), reflection about the two equivalent degree-two triangle vertices yields \(11\). Exact rational elimination (reconstructed by `checker.py`) gives

\[
T_C(c)=\frac{8c^4+24c^3+42c^2+61c+25}{4(5c+3)}
\]

and

\[
T_P(c)=\frac{J_{10}(c)}{6H_7(c)},
\]

where

\[
\begin{aligned}
H_7(c)={}&162c^7+806c^6+1857c^5+2618c^4\\
&+2412c^3+1416c^2+480c+72,\\[3pt]
J_{10}(c)={}&324c^{10}+2556c^9+9919c^8+25760c^7\\
&+48131c^6+65654c^5+65563c^4+46968c^3\\
&+22806c^2+6696c+900.
\end{aligned}
\]

The exact subtraction simplifies to

\[
T_C(c)-T_P(c)=\frac{c^2P_9(c)}{12(5c+3)H_7(c)}.
\]

Every denominator factor is strictly positive for \(c>0\). Reading the nonzero coefficients of \(P_9\) in descending order gives five positive coefficients followed by five negative coefficients, hence exactly one sign change. Descartes' rule permits at most one positive root, counted with multiplicity. Because \(P_9(0)=-684<0\) and \(P_9(c)\to+\infty\) as \(c\to+\infty\), continuity supplies a positive root and makes it unique. Its sign is negative before that root and positive afterward. Exact rational bisection brackets it between \(1.079524\) and \(1.079525\). This proves all three optimization cases.

For comparison with a common network proxy, the four-cycle is regular of degree two and has adjacency spectral radius \(2\). The triangle with a pendant site contains a triangle as a proper connected subgraph; extending a positive Perron eigenvector from that triangle to the pendant vertex and applying strict Perron monotonicity gives spectral radius strictly greater than \(2\). Alternatively its characteristic polynomial is \((z+1)(z^3-z^2-3z+1)\), whose largest root is about \(2.170086\). This eigenvalue ordering is independent of \(c\) and cannot reproduce the proven switch. The exact low/high-rate behavior also follows from the rational difference:

\[
T_C(c)-T_P(c)=-\frac{19}{72}c^2+O(c^3)\quad(c\downarrow0),
\qquad T_C(c)-T_P(c)\sim\frac{c^3}{15}\quad(c\to\infty).
\]

## Verification

Run `python checker.py` with Python 3 and SymPy. The script constructs the \(15\)-state transient generator directly from the graph edge lists, calculates both automorphism-orbit reductions, verifies all \(15\) symbolic backward equations after lifting the orbit solutions, checks the two rational formulas and their difference identically, and verifies the Descartes coefficient signs, rational root bracket, and asymptotics. It separately solves both full \(15\)-state systems using exact rational arithmetic at six nonzero colonization rates. It also checks the two adjacency characteristic polynomials. Every asserted equality is exact; decimal values illustrate rather than prove the theorem.

For example, at \(c=1\), \(T_C=5\) and \(T_P=295277/58938\), so the triangle-and-tail is better. At \(c=2\), \(T_C=635/52\) and \(T_P=1182381/99812\), so completing the four-cycle is better. At \(c=0\) (outside the positive-rate theorem) both arrangements reduce to the four independent local-extinction clocks with mean \(25/12\).

## Relationship to prior work

Finite contact processes and stochastic patch-occupancy metapopulations use the same occupied-to-empty and neighbor-induced recolonization generator; this equivalence must be considered when testing priority. Mountford et al. (2012 preprint, later 2016 journal article) establish asymptotic extinction-time results for growing graph families, not an ordering of the two fixed four-vertex unicyclic graphs. Shtilerman and Stone (2015) investigate network symmetry and spectral-radius persistence criteria for metapopulations; such criteria do not yield the exact finite mean-absorption ranking here, especially since the spectral ranking stays fixed while the mean ranking reverses. Van de Bovenkamp and Van Mieghem (2015) derive exact survival-time expressions for complete graphs and stars; neither of the two graphs here belongs to those families. Ross and Pollett (2010) study metapopulation persistence management under cost constraints, motivating the corridor-budget question, but an exact comparison for this pair was not established in the material accessible for inspection. The comparison of prior statements and possible implicit coverage remains subject to independent historical review.

## Limitations

The result applies to one symmetric extra corridor, equal positive transmission/colonization rates on all edges, homogeneous unit extinction, full initial occupancy, and a four-patch network only. It is not an assertion about stochastic dominance of all survival distributions, quasi-stationarity, larger networks, unequal costs, one initially occupied patch, empirical landscape management, or spatially correlated disturbances. No claim is made that an adjacency spectral radius criterion is wrong in its own large-network or near-linearized domain. Historical originality is assessed only against inspected accessible literature and searches; some potentially relevant full texts were unavailable, and independent scholarly review has not been performed.

## References

- T. Mountford, J.-C. Mourrat, D. Valesin and Q. Yao, *Exponential extinction time of the contact process on finite graphs*, arXiv:1203.2972, first public preprint 13 March 2012, https://arxiv.org/abs/1203.2972.
- E. Shtilerman and L. Stone, *The effects of connectivity on metapopulation persistence: network symmetry and degree correlations*, Proc. R. Soc. B 282 (2015), 20150203, https://doi.org/10.1098/rspb.2015.0203.
- R. van de Bovenkamp and P. Van Mieghem, *Survival time of the susceptible-infected-susceptible infection process on a graph*, Phys. Rev. E 92 (2015), 032806, https://doi.org/10.1103/PhysRevE.92.032806.
- J. V. Ross and P. K. Pollett, *Simple rules for ranking and optimally managing metapopulations*, Ecological Modelling 221 (2010), 2515–2520, https://doi.org/10.1016/j.ecolmodel.2010.02.016.
- K. Frank, *Metapopulation Persistence in Heterogeneous Landscapes: Lessons about the Effect of Stochasticity*, American Naturalist 165 (2005), 374–388, https://doi.org/10.1086/428293.
