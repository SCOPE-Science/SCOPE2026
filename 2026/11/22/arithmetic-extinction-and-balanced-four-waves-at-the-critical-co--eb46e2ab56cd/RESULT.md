# Arithmetic extinction and balanced four-waves at the critical contact threshold

## Finding

**Theorem (period and attractor classification).** Let \(G=(V,E)\) be a finite connected simple undirected \(2r\)-regular graph, where \(r\ge1\), whose adjacency spectrum consists of integers. Suppose \(3\nmid |V|\). For synchronous three-state Greenberg–Hastings dynamics with excitation threshold exactly \(r\), every trajectory eventually reaches either the all-rest configuration or a primitive temporal four-cycle; no other recurrent orbit occurs. A four-cycle exists if and only if \(G\) is bipartite and its adjacency matrix \(A\) admits a function \(f:V\to\{-1,+1\}\) with \(Af=0\). If \(G\) is bipartite, the precise number of primitive four-cycle orbits is

\[
\frac12\#\{f\in\{-1,+1\}^{V}:Af=0\}.
\]

In particular, **every** initial state becomes all-rest on any nonbipartite graph satisfying these hypotheses.

**Infinite high-odd-girth application.** For every integer \(a\ge0\), put \(m=4\cdot3^a\), and let \(O_m=KG(2m-1,m-1)\) denote the odd graph on the \((m-1)\)-subsets of a \((2m-1)\)-element set, with adjacency by disjointness. Its degree is \(m\). At excitation threshold \(m/2\), every initial three-state configuration becomes completely resting after finitely many updates. These graphs have no triangles and possess odd cycles (indeed, their known odd girth is \(2m-1\)). Their spectra contain the threshold eigenvalue \(m/2\); thus absence of all threshold-resonant eigenvalues is **not** the explanation for extinction. The first case is the 35-vertex graph \(KG(7,3)\), with adjacency spectrum \(\{4,-3,2,-1\}\).

For comparison, when \(3\nmid r\) the complete bipartite graph \(K_{2r,2r}\) has exactly \(\binom{2r}{r}^{2}/2\) primitive four-cycle orbits under the same half-degree rule, whereas the nonbipartite odd-graph family becomes extinct.

## Assumptions and scope

A state is \(x_t:V\to\{0,1,2\}\), with \(0\) resting, \(1\) excited, and \(2\) refractory. All vertices update simultaneously by \(1\to2\), \(2\to0\), and \(0\to1\) if and only if at least \(r\) neighbors are in state \(1\); otherwise \(0\to0\). The graph is finite, simple, undirected, connected, and exactly \(2r\)-regular; adjacency integrality means **every** complex adjacency eigenvalue is an integer. The divisibility condition is \(3\nmid |V|\), not merely an assumption about graph degree or the size of a bipartition.

“Eventually” means after a finite initial transient depending on the configuration; no graph-uniform upper bound on extinction or transient length is asserted. The reported orbit count counts labelled temporal orbits, not states and not classes modulo graph automorphisms. A primitive four-cycle has four distinct configurations.

## Proof

**1. Saturated contact balance on a recurrent orbit.** Fix a periodic trajectory with least period \(p\), and write \(e_t(v)=\mathbf 1\{x_t(v)=1\}\), with time indices modulo \(p\). Two excitations at the same vertex are separated by at least three updates; therefore \(e_{t-1}(v)e_{t+1}(v)=0\). Every excited vertex at time \(t\) had at least \(r\) excited neighbors at \(t-1\). Summing these contact counts over all vertices and times gives at least \(r\sum_t |e_t|\) contacts from the preceding layer, and by undirectedness the same lower bound for contacts to the succeeding layer. These two neighbor layers are disjoint at every vertex, so their combined contact count is at most \(2r\sum_t|e_t|\). Both inequalities are equalities. Thus every excited vertex has *exactly* \(r\) neighbors excited one time earlier and exactly \(r\) one time later, with no neighbors excited in any other phase. Every neighbor of any excited vertex must therefore be excited at an adjacent time; connectivity propagates this property to all vertices of a nonzero recurrent orbit. If a vertex is excited at a time other than \(t-1\) or \(t+1\), saturation also excludes edges to the excited layer at time \(t\). Consequently, for every vertex and time, including times at which the vertex is resting or refractory, we have the exact vector identity

\[
A e_t=r(e_{t-1}+e_{t+1}). \tag{1}
\]

Let \(s=\sum_{t=0}^{p-1}e_t\). Equation (1) gives \(As=2rs\). On a connected \(2r\)-regular graph any real-valued function equal to the average of its neighbors is constant (apply a maximum principle). Hence every vertex is excited the same integer number \(k\) of times per period, with \(0\le k\le\lfloor p/3\rfloor\). A nonzero recurrent orbit has \(k\ge1\). Summing (1) over vertices shows that \(|e_t|\) is constant in \(t\), because \(2|e_t|=|e_{t-1}|+|e_{t+1}|\) and a periodic sequence with vanishing second difference is constant. Consequently

\[
p\,|e_t|=k|V|. \tag{2}
\]

**2. Integral-spectrum temporal restriction.** For a \(p\)th root of unity \(\zeta=e^{2\pi i/p}\), take the temporal Fourier coefficients \(h_j=\sum_t\zeta^{jt}e_t\). Equation (1) yields

\[
A h_j=r(\zeta^j+\zeta^{-j})h_j. \tag{3}
\]

If \(h_j\ne0\), the scalar \(r(\zeta^j+\zeta^{-j})\) is an adjacency eigenvalue, hence an integer. But \(\zeta^j+\zeta^{-j}\) is an algebraic integer; a rational algebraic integer is an integer. Its absolute value is at most two, so it belongs to \(\{-2,-1,0,1,2\}\). Such roots of unity have order only \(1,2,3,4,6\). Fourier inversion therefore makes every \(e_t\) twelve-periodic. Since the full state at time \(t\) is determined by excitation at \(t\) and \(t-1\), the original orbit period divides twelve. The only possibilities are \(p\in\{1,2,3,4,6,12\}\).

**3. The order-three obstruction.** The all-rest state is the only fixed point, and refractory separation excludes nonzero periods one and two. Suppose \(3\mid p\). Equation (2) and \(3\nmid|V|\) force \(3\mid k\). For \(p=3\) or \(p=6\), the bound \(k\le\lfloor p/3\rfloor\) then forces \(k=0\), impossible for a nonzero orbit. If \(p=12\), necessarily \(k=3\). Equation (3) at the primitive twelfth root \(\zeta=e^{\pi i/6}\) gives \(Ah_1=r\sqrt3\,h_1\). Since \(r\sqrt3\) is not an integer adjacency eigenvalue, \(h_1=0\). At each vertex exactly three time coordinates are excited, so \(\zeta^{t_1}+\zeta^{t_2}+\zeta^{t_3}=0\). Three complex numbers of modulus one sum to zero if and only if their arguments are separated by \(2\pi/3\). Accordingly, the three excitation times differ by four modulo twelve, and \(e_{t+4}(v)=e_t(v)\) at every vertex. The state itself is four-periodic, contradicting least period twelve. Thus the only nonzero recurrent period is four.

**4. Exact characterization and count of four-waves.** At period four, refractory separation and uniform firing give \(k=1\). Label every vertex by its unique excited-time phase \(\phi(v)\in\mathbb Z/4\mathbb Z\). Saturation implies that every vertex has exactly \(r\) neighbors of phase \(\phi(v)-1\) and exactly \(r\) of phase \(\phi(v)+1\), and no other neighbors. Every edge joins opposite phase parity, so \(G\) is bipartite. Choose its bipartition \(L\sqcup R\). Up to the choice of which shore has even phase, a phase labeling is obtained by a sign function \(f\in\{-1,+1\}^V\): on the even-phase shore, \(+1\) means phase zero and \(-1\) phase two; on the odd-phase shore, \(+1\) means phase one and \(-1\) phase three. Exactly \(r\) neighbors of each sign at every vertex is equivalent to \(Af=0\).

Conversely, choose either shore as the even-phase shore, choose any \(\{-1,+1\}\)-valued \(f\) with \(Af=0\), and assign phases as above. For each \(t\), put a vertex in state one if \(\phi(v)=t\), in state two if \(\phi(v)=t-1\), and otherwise in state zero. The balanced-neighbor identity ensures that these four configurations update successively under the stated threshold rule. They have least period four. This gives exactly two distinct periodic *states at a fixed time* for each sign function, one for each parity orientation; the correspondence is injective because a periodic state determines all its future excitation times. Hence the number of primitive four-cycle orbits is \(2\#\{f:Af=0\}/4\), as claimed. In particular, if the graph is nonbipartite it has no four-wave, and finiteness forces eventual all-rest.

**5. Infinite odd-graph application.** Put \(m=4\cdot3^a\). Vertices of \(O_m\) are \((m-1)\)-subsets of a \((2m-1)\)-set. Each has \(m\) disjoint neighbors; the graph is connected because the Kneser parameters satisfy \(2m-1>2(m-1)\). It is nonbipartite: with indices modulo \(2m-1\), the sets \(S_i=\{i,i+2,\ldots,i+2(m-2)\}\) satisfy \(S_i\cap S_{i+1}=\varnothing\) for every \(i\), yielding an odd closed walk of length \(2m-1\). Also no three such vertices can be pairwise disjoint, since \(3(m-1)>2m-1\). Its adjacency spectrum is integral: if \(g_T(S)=\mathbf1\{T\subseteq S\}\) for \(|T|=j\le m-1\), then

\[
(A g_T)(S)=(m-j)\mathbf1\{S\cap T=\varnothing\}
=(m-j)\sum_{R\subseteq T}(-1)^{|R|}g_R(S).
\]

The spaces spanned by \(g_T\) of size at most \(j\) form an invariant filtration, and at level \(j\) the induced map is multiplication by \((-1)^j(m-j)\). Since the highest-level incidence functions span all functions on vertices, every adjacency eigenvalue is an integer. Furthermore, the order

\[
|V(O_m)|=\binom{2m-1}{m-1}\equiv2\pmod3
\]

by Lucas's theorem: in ternary, \(2m-1\) has digits \(21\) followed by \(a\) digits \(2\), while \(m-1\) has digits \(10\) followed by the same \(a\) trailing digits \(2\), so the Lucas product is \(\binom21\binom10=2\) modulo three. The general theorem therefore gives extinction. The standard odd-graph eigenvalues \((-1)^j(m-j)\) include \(+m/2\) at \(j=m/2\) because \(m/2\) is even. This particular eigenvalue is also witnessed explicitly: select \(m/2\) disjoint pairs from the ground set and take \(h(S)\) to be the product of the pairwise membership differences. Swapping pair members shows \(Ah=(m/2)h\). Thus the extinction conclusion genuinely uses the order-three counting obstruction in addition to integrality, not merely absence of critical spectral modes.

For \(K_{2r,2r}\), a sign function has \(Af=0\) precisely when each shore has \(r\) positive signs and \(r\) negative signs. There are \(\binom{2r}{r}^2\) such functions. When \(3\nmid r\), the period restriction applies and gives the stated complete orbit census.

## Verification

The accompanying `verify.py` uses exact integer adjacency tests and an exact integer polynomial-annihilator and power-trace certificate. It checks \(O_4=KG(7,3)\): 35 vertices, degree four, connectedness, no triangles, a seven-edge odd cycle, and exact characteristic polynomial

\[
(\lambda-4)(\lambda+3)^6(\lambda-2)^{14}(\lambda+1)^{14}.
\]

It independently enumerates the \(36\) signed zero eigenvectors on \(Q_4\) and on \(K_{4,4}\), and constructs and directly updates their respective \(18\) primitive four-cycle orbits. It checks that all \(3^5=243\) configurations on \(K_5\) become resting, and checks the Lucas residue for the first seven values of \(a\). These finite checks support the definitions and boundary cases; the all-order statement is established by the proof, not by enumeration.

Run `python3 verify.py` from the extracted package directory with Python 3 (standard library only). The expected exact output is included in `CHECK_OUTPUT.txt`.

## Relationship to prior work

Fisch, Gravner and Griffeath introduce threshold Greenberg–Hastings excitable systems on lattices; Gravner, Lyu and Sivakoff and Doba analyze three-state propagation on arbitrary finite graphs under **one-neighbor** activation. Their graph-wide theorems do not cover the contact threshold equal to half an even degree. The previously available integral-spectrum period-divisibility statement allows periods three, six and twelve and does not give this cardinality-dependent exclusion or the signed-kernel orbit bijection. General perfect-coloring theory recognizes balanced neighbor classes but does not by itself give the dynamical extinction mechanism and order-three obstruction. Classical Kneser eigenvalue and Lucas results supply established graph-theoretic and arithmetic ingredients rather than the dynamical conclusion.

## Limitations

The theorem requires connectedness, even regular degree, integral adjacency spectrum and an order not divisible by three. It does not claim a uniform convergence-time bound, a count of extinction-basin sizes, a classification for nonintegral graphs, or a complete formula for signed-nullvector counts on arbitrary bipartite graphs. For example, a five-cycle under threshold one is outside the integrality hypothesis and may sustain a traveling wave. The examples and Fourier proof have been checked, but independent external scientific validation and historical-priority confirmation have not been performed. Unindexed results on equitable colorings or threshold graph dynamics may still bear on originality.

## References

- R. Fisch, J. Gravner and D. Griffeath, *Threshold-Range Scaling of Excitable Cellular Automata*, arXiv:patt-sol/9304001, original arXiv posting dated 1993-04-02. https://arxiv.org/abs/patt-sol/9304001
- J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320, first posted 2016-10-24. https://arxiv.org/pdf/1610.07320
- N. Doba, *The Time Evolution of a Greenberg–Hastings Cellular Automaton on a Finite Graph*, *Complex Systems* 27 (2018), 101–126, doi:10.25088/ComplexSystems.27.2.101. https://wpmedia.wolfram.com/sites/13/2018/09/27-2-1.pdf
- *On Forced Periodicity of Perfect Colorings*, *Theory of Computing Systems* (2023), doi:10.1007/s00224-023-10127-x. https://link.springer.com/article/10.1007/s00224-023-10127-x
- Kneser graph, classical adjacency-spectrum and connectedness formulas, reference overview: https://mathworld.wolfram.com/KneserGraph.html and https://en.wikipedia.org/wiki/Kneser_graph
