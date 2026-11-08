# Complete fixed-point and two-cycle census for synchronous majority on prism networks

## Finding
For every integer \(n\ge3\), let \(G_n=C_n\square K_2\), with two labeled rings of \(n\) vertices and one rung between corresponding vertices. Every vertex has three distinct neighbors. At each simultaneous update, a vertex adopts the strict majority opinion among its three neighbors. There are no ties. Write \(F_n\) for the number of fixed binary opinion configurations, \(T_n\) for the number of configurations belonging to a fixed point or a temporal two-cycle, and \(P_n\) for the number of *distinct unordered strict two-cycle orbits*. Define the Lucas numbers by \(L_0=2\), \(L_1=1\), and \(L_{m+2}=L_{m+1}+L_m\).

**Theorem.** Every trajectory eventually reaches a fixed point or a strict two-cycle. The exact counts for every \(n\ge3\) are
\[
F_n=L_n+2+2\cos(n\pi/3),\qquad P_n=(T_n-F_n)/2,
\]
and
\[
T_n=\begin{cases}
L_{2n}+8L_n+18,& n\equiv0\pmod6,\\
L_{2n}+2L_n+3,& n\equiv2,4\pmod6,\\
L_{2n}+4,& n\equiv3\pmod6,\\
L_{2n}+1,& n\equiv1,5\pmod6.
\end{cases}
\]
Consequently, if \(\varphi=(1+\sqrt5)/2\), then \(T_n\sim\varphi^{2n}\), \(F_n\sim\varphi^n\), and the proportion of fixed configurations among all eventual periodic configurations is asymptotic to \(\varphi^{-n}\). The strict two-cycle states overwhelmingly dominate the exact terminal-state census, even though all periodic configurations form an exponentially vanishing fraction of the \(4^n\) possible initial configurations.

## Assumptions and scope
The graph is the simple labeled prism \(C_n\square K_2\), with \(n\ge3\); the two opinions are binary and equally weighted; every vertex updates synchronously from its *three neighbors, without including its own current opinion*. The number \(T_n\) counts labeled configurations \(x\) satisfying \(M^2(x)=x\), where \(M\) is one majority update. A strict two-cycle orbit \(\{x,M(x)\}\) is counted once in \(P_n\). The formula does not count sizes of basins of attraction or probabilities of reaching particular orbits. No claim is made for noisy, asynchronous, self-inclusive or tie-randomized updates.

## Proof
**1. No higher temporal periods.** Write current opinions as spins \(s_i(t)\in\{-1,+1\}\), let \(A\) be the symmetric adjacency matrix, and set \(H_i(t)=\sum_j A_{ij}s_j(t)\). Every degree is three, hence \(H_i(t)\ne0\) and \(s_i(t+1)=\operatorname{sgn}H_i(t)\). For \(t\ge1\) put
\[
E(t)=-\sum_{i,j}A_{ij}s_i(t)s_j(t-1).
\]
Symmetry of \(A\) gives the exact difference
\[
E(t+1)-E(t)=-\sum_i\bigl(s_i(t+1)-s_i(t-1)\bigr)H_i(t)\le0.
\]
If any spin at time \(t+1\) differs from its value at \(t-1\), the associated summand is strictly negative, because the update chooses the strict sign of \(H_i(t)\). The integer-valued energy has finitely many values, so eventually no such difference occurs. Thus \(s(t+1)=s(t-1)\) at every sufficiently late time, proving that all eventual periods divide two.

**2. Fixed-point census.** Suppose a fixed coloring has a rung whose two ends carry opposite opinions. Each endpoint already has one opposite neighbor, so both of its same-ring neighbors must agree with it. This forces the next two rungs to be opposite in the same orientation, and propagation around the cycle shows that the entire upper ring is monochromatic and opposite to the entire lower ring. There are precisely two such fixed colorings.

In any other fixed coloring the two endpoints of every rung must agree. Thus the state is a binary cyclic word of length \(n\), copied to both rings. Each vertex gets one agreeing neighbor across its rung; it remains fixed precisely if it has at least one agreeing neighbor along its ring, so the cyclic word has no isolated symbol. Mark edge \(i\) when the neighboring symbols disagree. The marked edges form an independent set of \(C_n\), and their total number must be even to permit cyclic closure. Conversely, each even independent edge set and an initial symbol specify exactly one cyclic word. The cycle independence polynomial has values \(I(C_n;1)=L_n\) and \(I(C_n;-1)=2\cos(n\pi/3)\), by the standard two-state transfer recurrence with characteristic equation \(\lambda^2=\lambda+z\). Even-cardinality extraction and the two initial-symbol choices therefore give \(L_n+2\cos(n\pi/3)\) such fixed colorings. Adding the two opposite-ring states proves the displayed formula for \(F_n\).

**3. Exact transfer representation of all period-dividing-two states.** Given any candidate pair of consecutive colorings \(x,y\), encode each ring-column \(i\) as
\[
c_i=(x_i^0,x_i^1,y_i^0,y_i^1)\in\{0,1\}^4.
\]
There are sixteen column symbols. Construct a directed graph on the \(256\) ordered symbol pairs \((a,b)\). Include the edge \((a,b)\to(b,c)\) if and only if, at column \(b\) and for both layers \(\ell\in\{0,1\}\),
\[
y_b^\ell=\operatorname{maj}(x_a^\ell,x_c^\ell,x_b^{1-\ell}),\qquad
x_b^\ell=\operatorname{maj}(y_a^\ell,y_c^\ell,y_b^{1-\ell}),
\]
where \(\operatorname{maj}(u,v,w)=1\) exactly when \(u+v+w\ge2\). If \(B\) is this directed adjacency matrix, the cyclic-trace bijection is
\[
T_n=\operatorname{tr}(B^n),\qquad n\ge3.
\]
Indeed, the two local equations are precisely \(M(x)=y\) and \(M(y)=x\); each labeled circular sequence has one and only one closed walk with its first two symbols fixed.

**4. The finite exact characteristic certificate.** Exhausting the \(16^3=4096\) possible symbol triples gives exactly \(400\) directed edges. Directed strongly connected components containing cycles have sizes \(16,8,8,2,1,1\); the remaining \(220\) vertices are acyclic singleton components. Their adjacency characteristic polynomials, in size order, are
\[
\begin{aligned}
p_{16}(z)&=(z-1)^2(z+1)^2(z^2-3z+1)(z^2+z+1)\\
&\quad\cdot(z^4-z^3+2z^2+z+1)(z^4+z^3+2z^2-z+1),\\
p_8(z)&=(z^2-z-1)(z^2-z+1)(z^2+z-1)(z^2+z+1),\\
p_2(z)&=(z-1)(z+1),\qquad p_1(z)=z-1.
\end{aligned}
\]
The \(p_8\) factor occurs twice, as does \(p_1\). For complete repeatability, the component vertex indices are specified in `verify.py`; that program independently constructs the whole directed graph and computes each characteristic polynomial exactly with integer matrix powers and Newton identities. This finite computation is exhaustive, with only \(256\) states; it is not an extrapolation from finitely many values of \(n\).

Taking the sums of \(n\)th powers of roots gives \(\operatorname{tr}(B^n)\). The quadratic factors \(z^2-3z+1\) and \(z^2-z-1\) contribute \(L_{2n}\) and \(L_n\). For the pair of quartics, their product is the polynomial \(q^4+3q^3+8q^2+3q+1\) in \(q=z^2\), whose four roots are \(\varphi^2\omega,\varphi^2\omega^2,\varphi^{-2}\omega,\varphi^{-2}\omega^2\), with \(\omega=e^{2\pi i/3}\). Thus their combined root-power sum vanishes for odd \(n\) and is \(4L_n\cos(n\pi/3)\) for even \(n\). Counting all the remaining cyclotomic and linear factors yields the explicit identity
\[
\begin{aligned}
\operatorname{tr}(B^n)=L_{2n}&+2(1+(-1)^n)(1+\cos(n\pi/3))L_n\\
&+5+3(-1)^n+4\cos(n\pi/3)+6\cos(2n\pi/3).
\end{aligned}
\]
Simplifying for the six residues of \(n\) modulo six proves the displayed formula for \(T_n\). Every nonfixed state counted by \(T_n\) belongs to exactly one strict two-cycle containing two states, proving \(P_n=(T_n-F_n)/2\).

**5. Growth laws.** From \(L_m=\varphi^m+(-\varphi)^{-m}\), the nonleading terms of \(T_n\) are \(O(\varphi^n)\) and those of \(F_n\) are bounded. Thus \(T_n/\varphi^{2n}\to1\), \(F_n/\varphi^n\to1\), and \(F_n/T_n\sim\varphi^{-n}\). Since the entire binary state space has \(4^n\) configurations, \(T_n/4^n\sim(\varphi^2/4)^n\to0\).

## Verification
Run `python3 verify.py` with Python 3 and no third-party modules. The program constructs all \(256\) transfer vertices and \(400\) transitions; identifies the six recurrent components and \(220\) acyclic vertices; reconstructs their six characteristic polynomials from exact Newton identities; checks the trace formulas for \(3\le n\le40\); and independently enumerates every labeled configuration on prisms of sizes \(3\le n\le8\), including all length-one and length-two temporal cycles. The checks pass. Small-size examples for \((F_n,T_n,P_n)\) are \((4,22,9)\), \((8,64,28)\), \((14,124,55)\), \((22,484,231)\) at \(n=3,4,5,6\), respectively.

## Relationship to prior work
Zehmakan (arXiv:2302.06760, first released February 14, 2023) analyzes synchronous and randomized majority opinion diffusion, proves stable-coloring growth on simple rings, and motivates exact counts on graph families beyond simple cycles. The present result concerns the distinct cubic prism network and gives exact fixed and full temporal-two-cycle enumerations, not just growth of fixed states. Nakar and Ron (arXiv:2205.08972) characterize temporal periodicity for one-dimensional self-inclusive radius-majority cellular automata; their neighborhood is different from the rung-coupled, self-exclusive prism rule. Turau (arXiv:2312.13769) obtains counting algorithms for fixed and pure two-cycle configurations on *trees*, whereas prisms contain cycles and the present census includes non-pure temporal two-cycles. Sánchez Muñoz and Mc Gettrick (arXiv:2101.09103) count pure Nash equilibria for anti-coordination games on ladders and circular ladders, a different one-time fixed-point constraint; their formulas do not imply the entire two-step majority dynamics spectrum. The general fact that symmetric binary majority processes have eventual period at most two is classical and is re-proved here for the odd-degree setting.

## Limitations
Novelty is a best-knowledge literature comparison, not proof of priority. An undiscovered equivalent transfer-matrix or Boolean-network result could cover this spectrum; a specialist comparison remains appropriate. The theorem makes no assertions about individual attraction-basin sizes, typical convergence times, or probabilities of reaching two-cycles from random starting opinions. The exact characteristic-polynomial reduction is a finite reproducible certificate; its mathematical validity does not imply physical realism of unweighted synchronous majority interactions.

## References
1. Ahad N. Zehmakan, *Random Majority Opinion Diffusion: Stabilization Time, Absorbing States, and Influential Nodes*, arXiv:2302.06760, first submitted 2023-02-14. https://arxiv.org/abs/2302.06760
2. Yonatan Nakar and Dana Ron, *The Structure of Configurations in One-Dimensional Majority Cellular Automata: From Cell Stability to Configuration Periodicity*, arXiv:2205.08972. https://arxiv.org/abs/2205.08972
3. Volker Turau, *Counting Problems in Trees, with Applications to Fixed Points of Cellular Automata*, arXiv:2312.13769. https://arxiv.org/abs/2312.13769
4. Victoria Sánchez Muñoz and Michael Mc Gettrick, *Nash Equilibria in Certain Two-Choice Multi-Player Games Played on the Ladder Graph*, arXiv:2101.09103. https://arxiv.org/abs/2101.09103
5. E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics 30 (1980), 187–189; period-two background as cited in the above literature.
