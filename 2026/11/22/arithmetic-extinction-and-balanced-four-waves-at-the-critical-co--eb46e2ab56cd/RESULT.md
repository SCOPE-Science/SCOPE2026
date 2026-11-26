# Arithmetic extinction and balanced four-waves at the critical contact threshold

## Finding

Let \(G=(V,E)\) be a finite connected simple undirected \(2r\)-regular graph, \(r\ge1\), with integral adjacency spectrum and \(3\nmid |V|\). For synchronous three-state Greenberg–Hastings dynamics with threshold \(r\), every trajectory eventually reaches the all-rest state or a primitive temporal four-cycle. A four-cycle exists exactly when \(G\) is bipartite and its adjacency matrix \(A\) has a signed nullvector \(f:V\to\{-1,1\}\), \(Af=0\). The number of primitive four-cycle orbits in the bipartite case is
\[
\frac12\#\{f\in\{-1,+1\}^{V}:Af=0\}.
\]
Thus every initial state on a nonbipartite graph satisfying the hypotheses eventually rests.

For every integer \(a\ge0\), put \(m=4\cdot3^a\). On the odd graph \(O_m=KG(2m-1,m-1)\), at threshold \(m/2\), all initial states eventually rest. These graphs have odd girth \(2m-1\) and have the threshold eigenvalue \(+m/2\), so spectral exclusion of all threshold-resonant eigenvalues is not the cause. The first case is the 35-vertex graph \(KG(7,3)\), with spectrum consisting of \(4,-3,2,-1\). By contrast, when \(3\nmid r\), the complete bipartite graph \(K_{2r,2r}\) has \(\binom{2r}{r}^2/2\) primitive four-cycle orbits at threshold \(r\).

## Assumptions and scope

A state is \(x_t:V\to\{0,1,2\}\), with \(0\) resting, \(1\) excited, and \(2\) refractory. Simultaneously at each update, \(1\to2\), \(2\to0\), and \(0\to1\) if and only if at least \(r\) neighbors are excited; otherwise \(0\to0\). The count is of temporal orbits on the labelled vertex set, not states or classes modulo graph automorphisms. Grouping by time translation identifies precisely the four states in each primitive four-cycle. No uniform transient bound is claimed.

## Proof

**Saturated contact balance.** On a periodic orbit of least period \(p\), let \(e_t(v)=\mathbf1\{x_t(v)=1\}\) with time indices modulo \(p\). At any vertex distinct excitations are separated by at least three updates. In particular the layers \(e_{t-1}\) and \(e_{t+1}\) are disjoint, also when regarded as subsets of vertices. For each excited pair \((v,t)\), let \(d_-(v,t)\) and \(d_+(v,t)\) count neighbors excited at \(t-1\) and \(t+1\). The update rule gives \(d_-\ge r\). By undirectedness and cyclicity, the two counts sum to the same total over all excited pairs. On each pair, disjointness of the two layers gives \(d_-+d_+\le2r\). Hence both totals are exactly \(r\sum_t|e_t|\), and equality forces \(d_-=d_+=r\) at *each* excited pair. In particular every neighbor of a vertex excited at \(t\) is excited at one of \(t-1,t+1\). This assertion concerns the two adjacent times; it imposes no further restriction on a neighbor's possible excitations elsewhere in the period.

For any vertex \(v\) and time \(t\), if \(e_{t-1}(v)+e_{t+1}(v)=1\), applying the pointwise balance at that excitation of \(v\) gives exactly \(r\) neighbors excited at \(t\). If the sum is zero, there can be no neighbor excited at \(t\), since applying saturation to such a neighbor would force \(v\) to be excited at \(t-1\) or \(t+1\). This proves
\[
Ae_t=r(e_{t-1}+e_{t+1}). \tag{1}
\]
Let \(s=\sum_{t=0}^{p-1} e_t\); then \(As=2rs\) and the maximum principle on the connected regular graph makes \(s\) constant. Thus every vertex fires \(k\) times per period, \(0\le k\le\lfloor p/3\rfloor\), with \(k>0\) on a nonzero orbit. Summing (1) over vertices gives zero second difference of \(|e_t|\) in time, so periodicity makes it constant. Therefore
\[
p|e_t|=k|V|. \tag{2}
\]

**Integral-spectrum temporal restriction.** For \(\zeta=e^{2\pi i/p}\) put \(h_j=\sum_t\zeta^{jt}e_t\). Equation (1) gives
\[
Ah_j=r(\zeta^j+\zeta^{-j})h_j. \tag{3}
\]
If \(h_j\ne0\), integrality of the adjacency eigenvalues makes \(\zeta^j+\zeta^{-j}\) rational. Being an algebraic integer of absolute value at most two, it lies in \(\{-2,-1,0,1,2\}\). Accordingly \(\zeta^j\) has order \(1,2,3,4\) or \(6\). Fourier inversion gives twelve-periodicity of \(e_t\), and of the full state since \(x_t\) is determined by \(e_t,e_{t-1}\). Hence \(p\mid12\).

**The order-three obstruction.** The all-rest state is the only fixed point and refractory separation excludes period two with any excitation. If \(3\mid p\), (2) and \(3\nmid |V|\) force \(3\mid k\). For \(p=3,6\) this is impossible on a nonzero orbit since \(k\le p/3\). For \(p=12\) it forces \(k=3\). Now the primitive twelfth-root coefficient is zero by (3), because \(r\sqrt3\) is not an integer. Thus at each vertex the three twelfth roots corresponding to its excitation times sum to zero. Three unit complex numbers sum to zero only when they form a rotated equilateral triple: for two of them \(u,v\) the third forces \(|u+v|=1\), so \(\operatorname{Re}(u\bar v)=-1/2\). The three times therefore differ by four modulo twelve, and the whole state is four-periodic, contrary to least period twelve. Finiteness of the state space now yields the eventual period restriction.

**Four-waves and their census.** At period four, \(k=1\). Give each vertex its unique excitation phase \(\phi(v)\in\mathbb Z/4\mathbb Z\). Pointwise saturation requires exactly \(r\) neighbors in each phase \(\phi(v)\pm1\), and every edge goes between opposite phase parity. On a connected bipartite graph there are two choices for the even shore. Once it is chosen, encode phases \(0,2\) by signs \(+1,-1\) there, and phases \(1,3\) by the same two signs on the other shore. Exactly \(r\) neighbors of each sign is precisely \(Af=0\).

Conversely, a choice of even shore and a signed nullvector gives a phase assignment. At time \(t\), phase \(t\) is excited, \(t-1\) refractory, and all others resting. The phase \(t+1\) has exactly \(r\) neighbors excited at \(t\) and activates, whereas phase \(t+2\) has none by bipartiteness and remains resting. This is a four-cycle of least period four since each vertex fires once. Distinct assignments define distinct states at time zero: the state determines the future trajectory and hence the excitation phases. The two choices of even shore therefore give twice the signed-nullvector count as a state count; divide by four for the orbit count. A nonbipartite graph has no such orbit, and hence every state eventually rests.

**Odd graphs and complete bipartite graphs.** The vertices of \(O_m\) are \((m-1)\)-subsets of a \((2m-1)\)-element set, with adjacency by disjointness. Each has \(m\) disjoint neighbors. Two vertices differing by one element have a common neighbor (the complement of their union), so \(O_m\) is connected. With indices modulo \(2m-1\), the sets \(S_i=\{i,i+2,\ldots,i+2(m-2)\}\) have consecutive sets disjoint and give an odd closed walk of length \(2m-1\). In any two steps on \(O_m\) at most one element of the initial set is replaced: both endpoints are \((m-1)\)-subsets of the middle vertex's size-\(m\) complement. In a closed walk of odd length \(2d+1\) the endpoints after \(2d\) steps are disjoint, so \(d\ge m-1\). This proves odd girth \(2m-1\) and triangle-freeness for the stated family.

For a subset \(T\) of size \(j\le m-1\), write \(g_T(S)=\mathbf1\{T\subseteq S\}\). Then
\[
(Ag_T)(S)=(m-j)\mathbf1\{S\cap T=\varnothing\}=(m-j)\sum_{R\subseteq T}(-1)^{|R|}g_R(S).
\]
The spaces spanned by \(g_T\) of size at most \(j\) give an invariant filtration, on whose successive quotients \(A\) acts by \((-1)^j(m-j)\). The largest space is the full function space, proving integrality. For \(j=m/2\), choose \(j\) disjoint pairs and let \(h(S)\) be the product of the differences of their two membership indicators. If a pair is entirely in \(S\), there are no disjoint sets contributing nonzero values. If both its members are outside \(S\), swapping them cancels the sum over disjoint sets. Otherwise, when exactly one member of every pair belongs to \(S\), exactly \(m-j\) neighbors have nonzero \(h\), all with value \((-1)^j h(S)\). Since \(j\) is even and \(h\) is not identically zero, \(+m/2\) is an eigenvalue. Lucas's theorem gives \(\binom{2m-1}{m-1}\equiv2\pmod3\): the ternary expansions begin with \(21\) and \(10\) respectively, followed in each by \(a\) copies of \(2\). The general theorem now applies. For \(m=4\), the eigenvalue multiplicities are \(1,6,14,14\) in the order given in the Finding, as certified by the exact annihilator and power traces in the accompanying verification.

For \(K_{2r,2r}\), the spectrum is integral (eigenvalues \(2r,-2r,0\)), and \(3\nmid r\) ensures \(3\nmid|V|\). The signed-kernel condition is that each shore carries exactly \(r\) positive signs. This gives \(\binom{2r}{r}^2\) signed nullvectors and the stated orbit count.

## Verification and limitations

The accompanying standard-library `verify.py` checks the exact spectrum, connectivity, triangle-freeness and seven-cycle of \(KG(7,3)\), the 36 signed nullvectors and 18 primitive four-cycles on each of \(Q_4\) and \(K_{4,4}\), extinction on all 243 states of \(K_5\), and the first seven Lucas residues. `CHECK_OUTPUT.txt` gives the expected output. These finite checks do not establish the general theorem or enumerate initial configurations on the odd-graph family. The analysis is specific to the hypotheses, does not classify basin sizes or transient lengths, and does not address nonintegral graphs, for example threshold-one traveling waves on \(C_5\).

## Relationship to prior work

The distinct twelve-step spectral-ceiling result [1] proves the period-divisibility input in wider graph scope and an extinction test when \(\{-r,0,r\}\) are all absent. Its conclusion alone does not exclude periods 6 and 12 under the order condition or count four-cycles. The half-degree period-three classification [2] gives balanced three-colorings and already provides the period-three size obstruction. The addition here is the order-three obstruction for the full recurrent classification, the signed-kernel census, and extinction on an infinite triangle-free nonbipartite family with a threshold eigenvalue. The colour balance, Kneser eigenvalues, and Lucas's theorem are not themselves new. Bounded comparisons do not establish historical priority.

## References

1. Twelve-step spectral-ceiling result, record `3ebebc11989a`, https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-a-twelve-step-spectral-ceiling-for-critical-excitation-on-integr--3ebebc11989a.
2. Half-degree rigidity result, record `7c3fe196f42d`, https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-half-degree-rigidity-and-a-sharp-contact-threshold-collapse-on-s--7c3fe196f42d.
3. R. Fisch, J. Gravner and D. Griffeath, *Threshold-Range Scaling of Excitable Cellular Automata*, https://arxiv.org/abs/patt-sol/9304001.
4. J. Gravner, H. Lyu and S. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, https://arxiv.org/abs/1610.07320; and N. Doba, *The Time Evolution of a Greenberg–Hastings Cellular Automaton on a Finite Graph*, Complex Systems 27 (2018), 101–126, doi:10.25088/ComplexSystems.27.2.101. These finite-graph works use one-neighbor rather than general half-degree activation.
5. *On Forced Periodicity of Perfect Colorings*, Theory of Computing Systems (2023), doi:10.1007/s00224-023-10127-x; and *Kneser Graph*, https://mathworld.wolfram.com/KneserGraph.html.
