# Half-degree rigidity and a sharp contact-threshold collapse on squared cycles

## Finding

Let \(G\) be a finite, connected, simple, \(2r\)-regular graph with \(r\ge1\). In synchronous three-state Greenberg–Hastings dynamics with excitation threshold \(\theta\), an unexcited site at state \(0\) changes to \(1\) if at least \(\theta\) neighbors have state \(1\), while \(1\to2\to0\) is unconditional. Let \(U_\theta\) denote the simultaneous update. A configuration is *initially primitive-three* if \(U_\theta^3x=x\) and \(U_\theta x\ne x\).

**General half-degree rigidity.** For \(\theta>r\), there are no initially primitive-three configurations. For \(\theta=r\), the initially primitive-three configurations are **exactly** the proper colorings \(c:V(G)\to\mathbb Z/3\mathbb Z\) in which every vertex has exactly \(r\) neighbors of each of the two other colors. Such colorings have three equally sized color classes, so \(3\mid |V(G)|\). They can equivalently be characterized by the adjacency eigenvector equation
\[
A_Gu=-r u,\qquad u_v=\exp(2\pi i c(v)/3).
\]
The eigenvector equation with cube-root coordinates is necessary *and sufficient*; the mere occurrence of the eigenvalue \(-r\) is not sufficient.

**Exact cycle-square transition.** Let \(G_n=C_n^2\), \(n\ge5\), be the labelled cycle-square with edges joining offsets \(\pm1,\pm2\) modulo \(n\). Its degree is four. Writing \(P_\theta(n)\) for the number of initially primitive-three configurations,
\[
P_2(n)=\begin{cases}6,&3\mid n,\\0,&3\nmid n,\end{cases}\qquad
P_\theta(n)=0\quad(\theta\ge3).
\]
For every \(n=3m\ge6\), the smaller threshold has the independently proved lower bound
\[
P_1(3m)\ge3\cdot 2^m.
\]
Thus raising the contact threshold from one to two destroys an exponentially growing explicit family of immediately periodic waves, leaving precisely two three-phase temporal orbits (six configurations) whenever \(3\mid n\); raising it again to three destroys even those. The periodic-point growth along the divisible-by-three subsequence changes from a rate at least \(\log 2/3\) to zero.

## Assumptions and scope

The graph is finite, simple, undirected, and connected, with every vertex of degree \(2r\ge2\); in the cycle-square specialization \(n\ge5\) guarantees four distinct neighbors per site. The threshold \(\theta\) is an integer at least one. Distinct vertex labels and three literal colors \(0,1,2\) are counted; spatial automorphisms and global cyclic color shifts are *not* quotiented. An orbit has least temporal period three only if the initial configuration is already periodic, not merely eventually periodic. The all-zero configuration is the unique fixed configuration.

For the general theorem, “proper” means that endpoints of each edge have different colors. “Balanced” means \(r\) neighbors of color \(c(v)+1\) and \(r\) of color \(c(v)-1\), modulo three. The spectral characterization concerns an eigenvector with every coordinate a third root of unity, **not** arbitrary vectors in the \(-r\) eigenspace.

## Proof

**1. Sitewise temporal dichotomy.** Assume \(U_\theta^3 x=x\). A vertex initially in state \(1\) must follow \(1,2,0,1\), and one initially in state \(2\) must follow \(2,0,1,2\). A vertex initially in state \(0\) either remains \(0\) for all four observations, or follows \(0,1,2,0\). Indeed, if it stays \(0\) at the first update, becoming \(1\) at the second would force state \(2\) at the third, contradicting return to \(0\). Hence vertices partition into an inactive set (permanently \(0\)) and an active set \(S\) (each rotating through all three colors). If \(S\) is empty, \(x\) is all-zero; otherwise the global orbit has least period three.

**2. Directed successor budget.** For an active vertex \(v\), consider the instant during its three-step rotation when its color is \(0\). The excitation threshold can be met only by *active* neighbors, since inactive neighbors are always \(0\). At that instant, a neighbor in initial active color \(c(v)+1\pmod3\) is excited; the number of these neighbors is constant across the three phase comparisons. Therefore
\[
d^+(v)=|\{w\in S:w\sim v,\ c(w)=c(v)+1\pmod3\}|\ge\theta.
\]
Every edge in the subgraph induced by \(S\) contributes to at most one such directed-successor count. Consequently, with \(e(S)\) the number of induced edges,
\[
\theta |S|\le\sum_{v\in S}d^+(v)\le e(S)\le r|S|.
\]
The last inequality follows by summing degrees in the \(2r\)-regular graph. If \(\theta>r\), these inequalities rule out nonempty \(S\). If \(\theta=r\), equality holds everywhere. In particular \(e(S)=r|S|\), so **no edge has exactly one endpoint in \(S\)**. Connectivity forces \(S=V(G)\). Equality \(\sum_v d^+(v)=e(G)\) forces every edge to have differently colored endpoints, and equality \(d^+(v)=r\) at every vertex forces exactly \(r\) successor neighbors and, by degree \(2r\), exactly \(r\) predecessor neighbors.

Conversely, any such balanced proper three-coloring rotates every site through \(c(v),c(v)+1,c(v)+2\) (modulo three), since whenever a site is in state zero it has \(r\) excited successor neighbors. It therefore supplies an initially primitive-three orbit. For each pair of colors \(a\ne b\), counting edges joining the two classes gives \(r|V_a|=r|V_b|\). Thus all class sizes are \(|V(G)|/3\).

**3. Spectral reformulation.** Write \(\omega=\exp(2\pi i/3)\) and \(u_v=\omega^{c(v)}\). A balanced proper coloring has \(r\) neighbors of each other color, hence
\[
(A_Gu)_v=r(\omega+\omega^2)u_v=-r u_v.
\]
Conversely, if \(u_v\in\{1,\omega,\omega^2\}\) and \(A_Gu=-r u\), let \(a,b,d\) count neighbors respectively with the same, successor and predecessor colors as \(v\). Then \(a+b+d=2r\) and \(a+b\omega+d\omega^2=-r\). Comparing imaginary parts gives \(b=d\), and real parts give \(a-b=-r\). Hence \(a=0\) and \(b=d=r\); the coloring is balanced and proper. (This also proves the eigenvalue obstruction, without asserting its converse absent cube-root coordinates.)

**4. Squared-cycle classification.** In \(C_n^2\), every three consecutive vertices form a triangle. Any proper three-coloring therefore uses all three colors on every consecutive triple. The next triple shares two vertices, forcing \(c(i+3)=c(i)\) for all indices modulo \(n\). Such a coloring exists only when \(3\mid n\), and then there are exactly six choices of the three ordered colors. Every one is balanced: among offsets \(\pm1,\pm2\), precisely two neighbors are successors and two are predecessors. With \(r=2\), the general result yields the claimed exact formula at threshold two and nonexistence at thresholds three and above. For \(n=5\), the graph is \(K_5\), and the same argument gives no proper three-coloring.

**5. Constructive lower bound at threshold one.** For \(m\ge2\), concatenate \(m\) blocks independently chosen from the two length-three words \(012\) and \(021\), then optionally add the same constant \(0,1,2\) modulo three to every color. Every vertex has a successor-colored vertex **within its own block** at distance at most two: in \(012\), distances to the required successor are \(1,1,2\), and in \(021\), they are \(2,1,1\). These vertices rotate unconditionally from \(1\) or \(2\), and meet threshold one whenever at zero. Every concatenation is therefore initially primitive-three, including across cyclic block boundaries. The \(3\cdot2^m\) configurations are pairwise distinct, because the first color identifies the global shift and each block identifies its binary choice. This proves the exponential lower bound without relying on a previously reported exact threshold-one census.

## Verification

The included script `verification/direct_update.py` independently applies the actual three-state update three times to every \(3^n\) initial configuration, for \(5\le n\le11\) and thresholds one, two and three. It checked \(796797\) initial states in total. Its threshold-two counts are \(0,6,0,0,6,0,0\), and every threshold-three count is zero. Threshold-one counts are \(150,270,588,1548,4092,10710,26400\).

The separate script `verification/phase_patterns.py` enumerates the augmented alphabet consisting of three rotating phases and an inactive marker, verifies the complete local period-three conditions for \(5\le n\le10\), and checks all binary block constructions through \(n=27\). It examined \(2795520\) augmented assignments, returning the same threshold-two and threshold-three populations. The logs `verification/direct_update.out` and `verification/phase_patterns.out` were generated by executing these exact source files. These finite checks corroborate the all-size proof but are not offered as an exhaustive proof for unbounded graph size.

## Relationship to prior work

The 1993 public preprint by Durrett and Griffeath introduces contact threshold and interaction range as organizing parameters of excitable dynamics; its accessible abstract emphasizes phase regions rather than finite ring period-three populations [1]. Fisch and Gravner [2, pp. 329–340, especially §§1–4] study one-dimensional threshold/range dynamics and stable periodic objects on the infinite line. Their periodic-boundary experiments do not provide the exact finite \(C_n^2\), threshold-two initial-period-three census, the general balanced-coloring equivalence, or the cube-root adjacency criterion. Their discussion of stable periodic objects motivates the distinction between local wave generators on an infinite lattice and global rotating modes on a finite ring.

Gravner, Lyu, and Sivakoff [3, §§1–2] analyze arbitrary finite graphs using the threshold-one three-color dynamics and an activity/circulation characterization. Those results do not imply the threshold-two classification. The new result is specifically a *contact-threshold comparison* and an exact finite population law, not an assertion about random initial data, long transients, or all temporal periods.

## Limitations

No classification of transient basins or of primitive periods other than three is asserted. For general even-regular graphs the result reduces the population to a balanced-coloring census, which may remain difficult; only the cycle-square family is counted explicitly. The spectral obstruction \(-r\in\operatorname{spec}(A_G)\) alone is not sufficient to produce a cube-root eigenvector. The exact threshold-one population outside the explicit constructive family is not reproved here. Historical priority is qualified: some older related works have not been compared in complete full text, and alternative equivalent formulations could exist.

## References

[1] R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, public preprint submitted **1993-03-22**, arXiv:patt-sol/9303002, https://arxiv.org/abs/patt-sol/9303002 (abstract consulted; full text unavailable in this inspection).

[2] R. Fisch and J. Gravner, *One-dimensional Deterministic Greenberg–Hastings Models*, Complex Systems **9** (1995), 329–348, https://content.wolfram.com/uploads/sites/13/2018/02/09-5-1.pdf (full primary source available; relevant §§1–4 examined).

[3] J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320, first public preprint **2016-10-24**, https://arxiv.org/abs/1610.07320; later Annals of Applied Probability **28** (2018), 3324–3357, https://www.math.ucdavis.edu/~gravner/hidden/clanki/AAP_2018.pdf (full accessible edition, especially §§1–2 examined).
