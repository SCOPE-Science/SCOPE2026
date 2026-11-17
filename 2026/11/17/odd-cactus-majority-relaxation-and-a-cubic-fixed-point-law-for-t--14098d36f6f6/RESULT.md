# Odd-cactus majority relaxation and a cubic fixed-point law for triangular chains

## Finding
Let \(F_G\) be synchronous, tie-retaining **open-neighbor binary strict-majority dynamics** on a finite, simple, undirected graph \(G\). If every vertex has even degree and \(G\) contains **no even cycle**, then \(F_G\) has no genuine temporal two-cycle. By the finite symmetric-threshold period theorem [1], every trajectory therefore eventually becomes fixed. In particular this applies to any disjoint union of connected cacti built solely from odd-cycle blocks and isolated vertices.

For each integer \(n\ge1\), let \(T_n\) be the labelled triangular cactus chain with vertices \(v_0,\ldots,v_n,w_1,\ldots,w_n\) and precisely the three edges of each triangle \(\{v_{i-1},v_i,w_i\}\), \(1\leq i\leq n\). The total number \(Q_n\) of one-step fixed binary configurations is exactly
\[
\sum_{n\ge1}Q_n z^n=\frac{2z(1+z)^2}{1-z-2z^2-z^3}.
\]
Hence \(Q_1=2\), \(Q_2=6\), \(Q_3=12\), and for every \(n\ge4\),
\[
Q_n=Q_{n-1}+2Q_{n-2}+Q_{n-3}.
\]
The first eight counts are \(2,6,12,26,56,120,258,554\). Writing \(\lambda=2.147899035704787\ldots\) for the largest real root of \(t^3-t^2-2t-1=0\),
\[
Q_n\sim C\lambda^n,\qquad C=1.222983983901625\ldots.
\]
Thus the initially fixed fraction among all \(2^{2n+1}\) configurations is asymptotically \((C/2)(\lambda/4)^n\), and every initial state, though generally not initially fixed, eventually reaches one of these fixed configurations.

## Assumptions and scope
All vertices are labelled, with no quotient by automorphisms. At each integer time \(t\), every vertex compares the number of 1-valued neighbors with half its degree and simultaneously takes the strict neighbor-majority bit; if these numbers tie, the vertex preserves its incumbent bit. A two-cycle means a distinct pair \(x\neq y=F_G(x)\) with \(F_G(y)=x\). The graph-theoretic prohibition covers disconnected graphs too, including isolated vertices. A cactus has each edge in at most one cycle; the specified odd-cycle-only cactus class excludes bridges between blocks, because such bridges could produce odd degrees. For \(T_n\), all vertices have even degree (two at free and ear vertices, four at interior cut vertices), and all cycles are triangles.

## Proof
**1. An even-cycle obstruction to two-step majority oscillations.** Assume \(x\mapsto y\mapsto x\) is a genuine two-cycle, and let \(S=\{v:x_v\neq y_v\}\). At each flipping vertex \(v\), write \(p_v\) for the number of neighbors in \(S\) whose bit at time zero is opposite to \(x_v\), and \(q_v\) for flipping neighbors whose time-zero bit agrees with \(x_v\). Let \(h_0,h_1\) be the numbers of nonflipping neighbors, respectively, agreeing and disagreeing with \(x_v\). As \(\deg(v)=p_v+q_v+h_0+h_1\) is even, switching at both time zero and time one requires strictly more than half the neighbors to disagree with the current vertex in both phases:
\[
p_v+h_1\ge\deg(v)/2+1,\qquad p_v+h_0\ge\deg(v)/2+1.
\]
Adding gives \(p_v-q_v\ge2\), in particular \(p_v\ge2\). Construct the subgraph \(H\) on all flipping vertices, keeping exactly those graph edges whose endpoints have opposite time-zero bits. Every vertex of \(H\) has at least two incident edges, so \(H\) contains a cycle. But all retained edges join opposite time-zero colors: \(H\) is bipartite and its cycle has even length. This contradicts the absence of even cycles in \(G\). Therefore genuine two-cycles cannot occur. The classical period-at-most-two theorem [1] for symmetric finite threshold dynamics now forces every trajectory to eventually reach a fixed state. A vertex of degree zero is itself always fixed and causes no exception.

**2. Encode fixed chain configurations by cut disagreements.** For fixed \(n\), put \(b_i=1\) when the bits at \(v_{i-1}\) and \(v_i\) differ, and zero otherwise. The bit at \(v_0\) has two choices, and once the \(n\)-bit word \(b_1\ldots b_n\) is fixed, every other cut-vertex bit is determined. Each degree-two ear \(w_i\) must agree with both adjacent cut vertices when \(b_i=0\); when \(b_i=1\), its bit is provisionally free. The degree-two endpoint vertices force \(w_1=v_0\) if \(b_1=1\) and \(w_n=v_n\) if \(b_n=1\). Every interior cut vertex has four neighbors and is fixed precisely when at most two neighbors disagree. If \(b_i=b_{i+1}=1\), its two adjacent cut vertices already disagree, so \(w_i=w_{i+1}=v_i\) is forced. Consequently three consecutive ones are impossible, and a run of two ones cannot touch either boundary. Conversely, these restrictions are sufficient: all remaining vertices have at most half disagreeing neighbors. A run of ones of length one has exactly two ear assignments if strictly internal, and exactly one if it touches an endpoint; a run of length two has one assignment, and is allowed only strictly internally. Zeros carry weight one. All choices described are independent across separated runs.

**3. Evaluate the weighted word language.** For a suffix of length \(m\ge0\) that begins just after a zero, define states \(Z,U,V\) recording whether the current run of ones has length zero, one, or two. A zero following \(U\) closes an internal singleton and contributes weight two; a zero following \(V\) closes a doubleton and contributes weight one. Introducing a new singleton from \(Z\) has weight one, and extending \(U\) to \(V\) has weight one. With row-state convention,
\[
M=\begin{pmatrix}1&1&0\\2&0&1\\1&0&0\end{pmatrix},\quad
T_m=(1,0,0)M^m(1,1,0)^{\mathsf T}.
\]
The terminal functional assigns weight one to an ending singleton (because it touches the right boundary), zero to a terminal doubleton, and one to the zero state. Direct inversion, or the companion recurrence, gives
\[
\sum_{m\ge0}T_m z^m=\frac{1+z}{1-z-2z^2-z^3}.
\]
Every admissible word either begins with zero, followed by an unrestricted suffix counted by \(T_{n-1}\), or begins with the pair one-zero, followed by a suffix counted by \(T_{n-2}\). In the second case the first singleton touches the left boundary and has multiplicity one. With \(T_{-1}=0\), the two possible initial cut bits give
\[
Q_n=2(T_{n-1}+T_{n-2}).
\]
Substituting the generating series yields the claimed rational function for every \(n\ge1\), and the cubic recurrence follows by coefficient comparison.

**4. Growth and rarity.** The characteristic polynomial \(t^3-t^2-2t-1\) has one positive root \(\lambda\) exceeding two; its other two roots are nonreal of modulus less than one (numerically, \(0.682\ldots\)). Equivalently, the nonnegative matrix \(M\) is primitive, so its simple Perron root \(\lambda\) strictly dominates the remaining eigenvalues. Let \(D(z)=1-z-2z^2-z^3\) and \(\rho=1/\lambda\). The residue of the generating function at its unique dominant pole gives
\[
C=-\frac{2\rho(1+\rho)^2}{\rho D'(\rho)}=1.222983983901625\ldots.
\]
Since \(T_n\) has \(2n+1\) vertices, division by \(2^{2n+1}\) proves the fixed-fraction asymptotic.

## Verification
The standalone `verify_majority.py` independently constructs every edge of the triangular cactus chain and implements the full synchronous local majority update, rather than using the word grammar. For each \(n=1,\ldots,8\) it enumerates all \(2^{2n+1}\) labelled states, counts fixed and two-step-return states, and compares both with the recurrence: the totals match \(2,6,12,26,56,120,258,554\). Across those sizes, \(174{,}760\) labelled states were examined. The separate `verify_transfer.py` implements weighted run enumeration independently of matrix powers and matches the \(3\times3\) transfer and recurrence through \(n=80\); it also checks absence of genuine two-cycles by complete state enumeration on six other odd-cycle bouquets. Reproducibility commands: `python verify_majority.py` and `python verify_transfer.py` from the package directory. The finite checks corroborate the proofs, not replace infinite quantifiers.

## Relationship to prior work
Goles and Olivos [1] establish the general eventual period-one-or-two restriction for symmetric finite threshold networks; this does not exclude primitive two-cycles specifically on graphs whose degree parity and cycle parity have the stated conjunction, nor give the chain equilibrium count. The full accessible expositions of Benjamini, Chan, O'Donnell, Tamuz, and Tan [2] and Kaaser, Mallmann-Trenn, and Natale [3] concern finite majority convergence and its bounds rather than the present graph-specific obstruction and exact polynomial. Turau [4] characterizes fixed states and two-cycles on trees; the triangular cactus chains here contain cycles.

Two particularly close archived results were examined by full `RESULT.md` text: one applies **three-state Greenberg–Hastings excitation to the exact same labelled triangular cactus chains** and counts primitive three-waves rather than binary majority equilibria [5]; the other treats binary majority on a graph consisting of triangles in a **single-hub clique windmill**, rather than consecutive triangles joined along a chain [6]. Neither prior statement entails the present no-two-cycle argument and cubic fixed-state law. Additional related exact counts for majority on cylindrical triangular strips and bouquets of four-cycles address different graph topologies. Search nonmatches do not establish unique historical priority.

## Limitations
The graphwide absence-of-two-cycles assertion requires **every** vertex to have even degree and the graph to contain no even cycle. It does not extend as stated to odd-degree graphs or even-cycle cacti; bridges have not been allowed in the odd-cactus corollary. The exact fixed-state formula applies to the specified open triangular chain only and makes no claim for all branched odd cacti, time-to-absorption distributions, basin sizes, stochastic updates, asynchronous updates, or closed-neighborhood majority. Historical priority is not independently established; possible equivalent formulations in unindexed statistical-mechanics enumeration and majority-network literature remain a residual risk. Independent external mathematical validation has not been performed.

## References
1. E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics **30** (1980), 187–189, DOI:10.1016/0012-365X(80)90121-1, https://doi.org/10.1016/0012-365X(80)90121-1 .
2. I. Benjamini et al., *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs*, first arXiv version 2014-05-11, https://arxiv.org/abs/1405.2486v1 .
3. M. Kaaser, K. Mallmann-Trenn and E. Natale, *On the Voting Time of the Deterministic Majority Process*, first arXiv version 2015-08-14, https://arxiv.org/abs/1508.03519v1 .
4. V. Turau, *Fixed Points and 2-Cycles of Synchronous Dynamic Coloring Processes on Trees*, 2022, https://arxiv.org/abs/2202.01580 .
5. *A two-state recurrence for three-periodic excitation on triangular cactus chains*, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-two-state-recurrence-for-three-periodic-excitation-on-triangul--6e5034274f28 .
6. *Four-step majority dynamics and exact oscillation basins on triangular clique windmills*, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-four-step-majority-dynamics-and-exact-oscillation-basins-on-tria--bfe9315b1ab6 .
