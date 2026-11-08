# Exact equilibrium counting with degree-four hubs in a picky binary public-goods game

## Finding
Let \(G=(V,E)\) be a finite simple undirected graph on \(n\ge1\) labeled vertices, with maximum degree at most four. Each vertex's unique best response is action \(1\) if the number of active neighbors belongs to \(\{0,2\}\), and action \(0\) otherwise. Put \(M=I+A_G\), computed over \(\mathbb F_2\), and \(D=\{v\in V:\deg(v)=4\}\). For disjoint subsets \(B,J\subseteq D\), define \(P(B,J)=\bigcup_{v\in B\cup J}N(v)\) and let \(L(B,J)\) be the number of binary solutions to
\[
 Mx=\mathbf1+\mathbf1_B,\qquad x_v=0\ (v\in B),\qquad x_u=1\ (u\in P(B,J)).
\]
All equations are over \(\mathbb F_2\), including the pinned coordinates. Each \(L(B,J)\) equals either zero or a power of two and is exactly computable by Gaussian elimination. The number of pure Nash equilibria is
\[
 \boxed{E(G)=\sum_{B\subseteq D}\ \sum_{J\subseteq D\setminus B}(-1)^{|J|}L(B,J).}
\]
Thus equilibrium existence and exact counting take \(O(3^{|D|}\operatorname{poly}(n))\) operations. In particular, for maximum degree three, \(E(G)=2^{n-\operatorname{rank}_{\mathbb F_2}(M)}\ge1\).

Unconditional existence fails at maximum degree four: on six vertices labeled \(0,1,2,3,4,5\), the eight edges \(01,02,04,05,12,23,25,34\) give no equilibrium. No simple graph on fewer than six vertices has this property.

## Assumptions and scope
Graphs are finite, simple, loopless and undirected; disconnected graphs and isolated vertices are allowed. Vertex actions are binary, and the best-response function is deterministic and homogeneous, with exactly the active-neighbor counts zero and two mapping to action one. The degree cap four and use of open rather than closed neighbors are essential. The result concerns pure Nash equilibria, not convergence of asynchronous updates, mixed equilibria, or weighted/multigraph games.

## Proof
Write \(s_v\) for the action of vertex \(v\) and \(q_v=\sum_{u\in N(v)}s_u\) as an integer. For \(\deg(v)\le3\), the prescribed best-response condition \(s_v=\mathbf1_{q_v\in\{0,2\}}\) is equivalent to \(s_v+q_v\equiv1\pmod2\). At a degree-four vertex, the same parity condition holds when \(q_v\le3\). The sole exception is \(q_v=4\): then the prescribed action is zero whereas parity would prescribe one. Hence, in any equilibrium, the set \(B\subseteq D\) of degree-four vertices with all neighbors active satisfies \(s_v=0\) for \(v\in B\), and its profile obeys \(Ms=\mathbf1+\mathbf1_B\). Conversely, any solution to that affine system with these pins and with \(q_v\ne4\) for each \(v\in D\setminus B\) is an equilibrium whose exceptional set is exactly \(B\).

For a fixed \(B\), the requirement \(q_v=4\) for \(v\in B\) imposes \(s_u=1\) for every \(u\in\bigcup_{v\in B}N(v)\). The requirement \(q_v\ne4\) for the remaining degree-four vertices is the complement of the event that all four of their neighbors have action one. Inclusion-exclusion over a chosen set \(J\subseteq D\setminus B\) of such events gives exactly the displayed signed sum of the affine-solution counts \(L(B,J)\). The possible assignments of each degree-four vertex to \(B\), \(J\), or neither give exactly \(3^{|D|}\) elimination tasks. A consistent system with coefficient rank \(r\) in \(n\) unknowns has \(2^{n-r}\) solutions; an inconsistent system has none. All steps are finite and exact.

If \(D=\varnothing\), the expression reduces to the all-ones linear system \(Mx=\mathbf1\). This system is solvable for every graph: for any \(z\in\ker M\), symmetry and characteristic two give \(0=z^\mathsf T Mz=\sum_v z_v\), because the off-diagonal adjacency terms occur twice and the diagonal entries of \(M\) are one. Thus \(\mathbf1\) is perpendicular to \(\ker M\), hence belongs to the image of the symmetric matrix \(M\); rank-nullity gives its stated solution count. This solvability is the classical odd-domination theorem, not claimed as a new result.

For the six-vertex witness, all vertex degrees are even (four for vertices zero and two, two for the others). Therefore \(M\mathbf1=\mathbf1\). Exact elimination shows \(\operatorname{rank}_{\mathbb F_2}(M)=6\), so the unique solution to the parity equation is the all-active profile. In any actual equilibrium, a degree-four vertex with four active neighbors cannot be active. The complete search in `verify.py` evaluates the best-response equations for all \(2^6=64\) possible profiles and finds no equilibrium. This finite exhaustive check certifies the witness; parity invertibility alone would not exclude exceptional degree-four profiles. The other five-vertex boundary is analytic: any graph on at most five vertices either has maximum degree at most three (and therefore a parity equilibrium) or has a universal vertex. If it has a universal vertex, activating that vertex alone is a pure equilibrium, since its active-neighbor count is zero and every other vertex sees exactly one active neighbor.

## Verification
Run `python verify.py` with Python 3.10 or later. It compares exact inclusion-exclusion counts with direct complete profile enumeration for every labeled graph on up to five vertices, then for deterministic samples of graphs on six, seven and eight vertices of degree at most four. It separately tests the six-vertex obstruction and its affine parity rank. The theoretical proof is independent of finite experiments. The witness's nonexistence is also verified over all 64 possible profiles; this is an exhaustive certificate for that finite graph, not an extrapolation from a sample.

## Relationship to prior work
Klimm and Stahlberg (arXiv:2301.11849, initially public January 27, 2023) define the picky response pattern and prove NP-completeness of equilibrium existence for unrestricted graphs. Their six-vertex 3-sun gadget without external operands already establishes a degree-four nonexistence example; this work does **not** claim to be the first degree-four or six-vertex obstruction. Their gadget has nine edges, whereas the displayed witness has eight. The separate odd-domination literature, including Batal (arXiv:2011.10270) and Sutner's theorem, already establishes the solvability and solution count of the parity system; the parity subcase is not claimed as independently original. The new component is the exact degree-four exception decomposition and its \(3^{|D|}\)-term census for the non-parity best-response rule, together with the explicit smaller-edge witness.

Maiti and Dey (arXiv:2012.01880) analyze parameterized complexity for the broader binary networked public-goods model, but their theorems do not supply this nonmonotone pattern's exact degree-four correction formula. The distinction is between a fixed best-response pattern and general utility-based instances.

## Limitations
The algorithm is fixed-parameter tractable in the number of degree-four vertices only under the maximum-degree-four restriction; no result is asserted for vertices of degree five or more. The repeated linear-algebra calculations may be expensive when many vertices have degree four. The main parity-solvability component was previously known, and a six-vertex nonexistence gadget was already in the initiating paper. Mathematical priority of the degree-four inclusion-exclusion construction has not been independently established by exhaustive indexing of all literature.

## References
- M. Klimm and M. J. Stahlberg, *Complexity of equilibria in binary public goods games on undirected graphs*, arXiv:2301.11849, initial release 2023-01-27, https://arxiv.org/abs/2301.11849.
- A. Batal, *Parity of an odd dominating set*, arXiv:2011.10270, first public 2020-11-20, https://arxiv.org/abs/2011.10270.
- A. Maiti and P. Dey, *On Parameterized Complexity of Binary Networked Public Goods Game*, arXiv:2012.01880, first public 2020-12-03, https://arxiv.org/abs/2012.01880.
