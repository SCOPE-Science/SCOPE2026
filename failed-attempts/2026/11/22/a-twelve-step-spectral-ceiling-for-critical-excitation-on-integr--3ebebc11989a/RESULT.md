# A twelve-step spectral ceiling for critical excitation on integral regular graphs

## Finding

Let \(G\) be any finite, nonempty, simple, undirected \(2r\)-regular graph, where \(r\) is a positive integer, and suppose every eigenvalue of its adjacency matrix is an integer. For synchronous three-state Greenberg–Hastings excitation with contact threshold \(r\), every eventually periodic trajectory has a least period dividing \(12\). Thus all recurrent least periods belong to \(\{1,3,4,6,12\}\). The bound is attained: the disjoint union \(C_3\sqcup C_4\), with critical threshold one on both components, has a primitive twelve-cycle.

More strongly, if the adjacency spectrum of \(G\) avoids \(\{-r,0,r\}\), **every** initial state becomes identically resting after finitely many updates. This criterion applies, for example, to the triangle-free Gewirtz graph, with spectrum \(\{10,2,-4\}\) and threshold \(5\), and the triangle-free Higman–Sims graph, with spectrum \(\{22,2,-8\}\) and threshold \(11\). No upper bound independent of the graph size is asserted for the extinction *time*.

Both the integrality assumption and the distinction between period and transient time are essential: the nonintegral adjacency spectrum of \(C_5\) permits a primitive five-period state at threshold one.

## Assumptions and scope

Vertices have literal states \(0\) (rest), \(1\) (excited), and \(2\) (refractory). At each simultaneous update, \(1\mapsto2\), \(2\mapsto0\), and a zero becomes one if and only if at least \(r\) of its distinct graph neighbors presently have state one; otherwise it stays zero. The graph may be disconnected but has no loops and constant positive even degree \(2r\). A primitive period is the least period of a fully recurrent configuration, not an entry or relaxation time. The all-zero configuration is the only fixed point. The term *integral graph* means that the real-symmetric adjacency matrix has integer eigenvalues, not that the graph is vertex-transitive or connected.

For an arbitrary starting state, finiteness of the state space guarantees eventual periodicity. The result identifies possible eventual least periods, without asserting a uniform finite entry-time bound or the existence of every allowable period for each graph. At a vertex set \(S\), its indicator vector is in \(\{0,1\}^{V(G)}\).

## Proof

**1. Excitation sets on a recurrent orbit.** Fix a fully periodic trajectory of period \(L\), indexed at all integer times, and put \(E_t=\{v:X_t(v)=1\}\) with indicator \(u_t\). The deterministic refractory progression gives
\[
E_{t-1}\cap E_{t+1}=\varnothing,\qquad E_t\cap E_{t+2}=\varnothing.
\]
Every vertex of \(E_{t+1}\) was at rest at time \(t\), and therefore had at least \(r\) neighbors in \(E_t\); hence the number of edges between these disjoint sets is at least \(r|E_{t+1}|\). Similarly each vertex of \(E_t\) had at least \(r\) neighbors in \(E_{t-1}\), so there are at least \(r|E_t|\) edges between them. Since \(E_{t-1}\) and \(E_{t+1}\) are disjoint and each vertex in \(E_t\) has only \(2r\) neighbors, the two edge counts together are at most \(2r|E_t|\). Therefore
\[
r|E_{t+1}|+r|E_t|\le2r|E_t|,
\quad\text{so}\quad |E_{t+1}|\le|E_t|.
\]
Periodicity forces equality at every time. All inequalities used above are consequently equalities: each excited vertex has precisely \(r\) neighbors in \(E_{t-1}\) and precisely \(r\) in \(E_{t+1}\), with no neighbors outside their union; conversely every vertex in either of those disjoint sets has exactly \(r\) neighbors in \(E_t\). All remaining vertices have no neighbors in \(E_t\). Hence the following **pointwise** integer-vector identity is exact:
\[
A u_t=r(u_{t-1}+u_{t+1})\qquad(t\in\mathbb Z).
\]
The equality applies also at vertices outside all three sets; it is not merely an identity of total excitation counts.

**2. Temporal spectrum.** Fix an \(L\)-th root of unity \(\zeta\) and form the Fourier coefficient
\[
\widehat u(\zeta)=\sum_{t=0}^{L-1}\zeta^{-t}u_t.
\]
Taking the temporal transform of the exact identity yields
\[
A\widehat u(\zeta)=r(\zeta+\zeta^{-1})\widehat u(\zeta).
\]
When \(\widehat u(\zeta)\ne0\), the right-hand scalar is an integer by the integral-spectrum hypothesis, so \(\zeta+\zeta^{-1}\) is rational. It is also an algebraic integer, being a sum of roots of unity. Every rational algebraic integer is an integer. The modulus bound gives \(\zeta+\zeta^{-1}\in\{-2,-1,0,1,2\}\). In each case \(\zeta\) is a root of unity whose order belongs to \(\{1,2,3,4,6\}\), which divides \(12\). Inverting the discrete Fourier transform shows \(u_{t+12}=u_t\) for every \(t\). The state at time \(t\) is recovered exactly from \(E_t\) and \(E_{t-1}\): its excited vertices are \(E_t\), refractory vertices are \(E_{t-1}\), and all others rest. Thus \(X_{t+12}=X_t\), establishing the period divisor property. If \(L=1\) or \(2\), periodic excitation would repeat a nonempty \(E_t\) at time \(t+2\), contradicting the refractory disjointness. Only the all-rest equilibrium has such periods.

**3. The stronger extinction criterion.** Suppose \(\operatorname{spec}(A)\cap\{-r,0,r\}=\varnothing\). The only allowed Fourier modes in Step 2 now correspond to the spectral values \(\pm2r\), hence to \(\zeta=1\) or \(\zeta=-1\). Thus \(u_{t+2}=u_t\), and the refractory disjointness \(E_t\cap E_{t+2}=\varnothing\) forces \(u_t=0\) for every time on any recurrent orbit. Consequently the only recurrent orbit is the all-zero state. Every initial state must eventually enter that state, since its trajectory is finite-state.

**4. Two triangle-free consequences.** For a strongly regular graph with parameters \((v,k,\lambda,\mu)\), the standard identity
\[
A^2=(k-\mu)I+(\lambda-\mu)A+\mu J
\]
shows that, on the space orthogonal to the constants, every adjacency eigenvalue is a root of \(z^2-(\lambda-\mu)z-(k-\mu)=0\). The Gewirtz parameters \((56,10,0,2)\) give nonprincipal roots \(2,-4\); the Higman–Sims parameters \((100,22,0,6)\) give roots \(2,-8\). The other eigenvalues are respectively \(10\) and \(22\). These spectra avoid the respective forbidden sets \(\{-5,0,5\}\) and \(\{-11,0,11\}\). Their \(\lambda=0\) guarantees no triangles, so the conclusions do not rely on a triangle-covered graph classification.

**5. Sharpness and a necessary boundary.** The two-regular integral graphs \(C_3\) and \(C_4\) have recurrent configurations `012` of least period three and `0012` of least period four, respectively, under the same threshold-one rule. Their disjoint union therefore has a recurrent state `0120012` of least period \(\operatorname{lcm}(3,4)=12\). In contrast, on the two-regular graph \(C_5\), the state `00012` travels with primitive temporal period five. The eigenvalues of \(C_5\) include irrational values, so \(C_5\) does not meet the integrality hypothesis. These witnesses demonstrate both sharpness and the significance of the hypothesis.

## Verification

The standard-library-only program `verification/check_cycles.py` exhaustively enumerates all \(3^3=27\) states of \(C_3\), \(3^4=81\) of \(C_4\), \(3^7=2187\) of their disjoint union, and \(3^6=729\) of the octahedral graph \(K_{2,2,2}\). For the disjoint union, initial states grouped by eventual period are \(1197\) of period one, \(342\) of period three, \(504\) of period four, and \(144\) of period twelve. The script explicitly follows all twelve distinct steps of `0120012` and verifies the five-period witness on \(C_5\). It verifies, rather than assumes, the local three-state update and eventual periods.

A third independently coded integer-state iterator `verification/check_contact_identity.py` checks the exact pointwise contact identity for every recurrent orbit reached from all those small initial states. A separate integer-arithmetic program `verification/check_spectrum.py` derives both exceptional graphs' eigenvalues and multiplicities from their published strongly regular parameters, checks the adjacency quadratic identity's principal consistency equation, checks trace and trace-square identities, and verifies the spectral exclusion at the exact contact threshold. It returns Gewirtz eigenvalue multiplicities \(10^1,2^{35},(-4)^{20}\) and Higman–Sims multiplicities \(22^1,2^{77},(-8)^{22}\). All three programs were executed successfully from these included source files. Neither small exhaustive exploration nor the arithmetic parameter check replaces the arbitrary-size Fourier proof; the latter supplies the infinite claim.

## Relationship to prior work

Durrett and Griffeath [1] study excitation range and contact threshold in the early Greenberg–Hastings literature. Fisch and Gravner [2, §1 and subsequent sections] investigate one-dimensional infinite-lattice models and stable periodic objects, not a general finite-graph integral-spectrum period ceiling. Gravner, Lyu and Sivakoff [3, §§1–2] study threshold-one three-color excitation on arbitrary graphs, so their graph-topological activity statements do not imply a spectral bound for higher critical thresholds. A closer subsequent result [4] characterizes **initially primitive-three** critical-threshold trajectories on even-regular graphs and explicitly does not classify other recurrent periods or universal extinction. This finding instead bounds all temporal periods on **any** integral even-regular graph and provides a spectral obstruction implying extinction even in triangle-free graphs. The previously determined complete-tripartite threshold-two period spectrum [5] is restricted to that graph family and does not imply the general integral-graph statement.

Doba [8, §§2–3] develops the exact finite-graph Greenberg–Hastings model with activation after **at least one** excited neighbor; that rule does not cover the critical threshold on graphs of degree larger than two. The Gewirtz and Higman–Sims graph spectral data and strongly regular parameters are standard [6–7]. The exceptional graphs are examples rather than a claim of newly computed eigenvalues. Novelty is claimed only for the combined period ceiling and extinction application, not for the existence of the graphs or the standard spectral identities.

## Limitations

The proof establishes a divisor bound for **eventual periods**, not a uniform upper bound on transient lengths. Graph integrality is a sufficient condition and not asserted necessary for an individual graph to have only divisor-of-twelve recurrent periods. The spectral exclusion is sufficient for extinction but not an if-and-only-if criterion. Finite program outputs corroborate tiny explicit examples only. The general graph theorem is proved analytically without reliance on those exhaustive checks. Historical priority remains qualified: a mathematically equivalent statement in an unindexed or inaccessible source may exist, and no independent external audit has been performed.

## References

[1] R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, public preprint 1993-03-22, arXiv:patt-sol/9303002, https://arxiv.org/abs/patt-sol/9303002 (abstract and submission date inspected; full primary text not accessible through the examined rendering).

[2] R. Fisch and J. Gravner, *One-dimensional Deterministic Greenberg–Hastings Models*, Complex Systems **9** (1995), 329–348, https://content.wolfram.com/uploads/sites/13/2018/02/09-5-1.pdf (primary PDF introduction and modeling sections inspected).

[3] J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320v1, first public 2016-10-24, https://arxiv.org/html/1610.07320v1 (full-text introduction, update rule and results inspected).

[4] *Half-degree rigidity and a sharp contact-threshold collapse on squared cycles*, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-half-degree-rigidity-and-a-sharp-contact-threshold-collapse-on-s--7c3fe196f42d (primary full RESULT.md, its statement/proof/scope and limitations inspected).

[5] *A nonmonotone twelve-cycle window for threshold-two excitable dynamics on tripartite graphs*, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-nonmonotone-twelve-cycle-window-for-threshold-two-excitable-dy--f93d052f0961 (indexed statement compared at claim level).

[6] E. W. Weisstein, *Gewirtz Graph*, MathWorld, https://mathworld.wolfram.com/GewirtzGraph.html (strongly regular parameters and integral spectrum inspected).

[7] E. W. Weisstein, *Higman-Sims Graph*, MathWorld, https://mathworld.wolfram.com/Higman-SimsGraph.html (strongly regular parameters and integral spectrum inspected).

[8] N. Doba, *The Time Evolution of a Greenberg–Hastings Cellular Automaton on a Finite Graph*, Complex Systems **27** (2018), 101–126, https://wpmedia.wolfram.com/sites/13/2018/09/27-2-1.pdf (primary PDF pp. 101–103 inspected, including explicit one-neighbor activation rule).
