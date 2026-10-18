# A sharp girth-six transition for scale-two Rips complexes of equal-arm theta graphs

## Finding
For integers \(m\ge3\) and \(\ell\ge2\), let \(\Theta_{m,\ell}\) have two designated vertices \(u,v\) joined by \(m\) pairwise internally disjoint paths, each with exactly \(\ell\) edges. Put the unit-edge shortest-path metric on the **vertex set** (not the continuum metric graph), and define the **inclusive** Vietoris–Rips complex \(R_r(\Theta)=\mathrm{VR}_{\le}(V\Theta;r)\).

The complete scale-two homotopy classification is
\[
R_2(\Theta_{m,\ell})\simeq
\begin{cases}
*,&\ell=2,\\
\bigvee^{m-1}S^2,&\ell=3,\\
\bigvee^{m-1}S^1,&\ell\ge4.
\end{cases}
\]
Define the integral augmentation module \(A_m=\{(c_1,\ldots,c_m)\in\mathbb Z^m:\sum_i c_i=0\}\), with \(S_m\) permuting coordinates, and let \(\tau\) reverse all paths simultaneously, interchanging their two common endpoints. The commuting arm-permutation and reversal actions give \(S_m\times C_2\). At scale one, \(\widetilde H_1(R_1;\mathbb Z)\cong A_m\), with \(\tau\) acting by \(-I\). At scale two, for \(\ell=3\), \(\widetilde H_2(R_2;\mathbb Z)\cong A_m\), with \(\tau\) acting by \(+I\); for \(\ell\ge4\), \(\widetilde H_1(R_2;\mathbb Z)\cong A_m\), with \(\tau\) acting by \(-I\). These are the only nonzero reduced integral homology groups at the indicated scales, and \(R_2\) is contractible for \(\ell=2\).

For \(\ell=3\), the graph has diameter three; hence over any field the full positive-dimensional barcode has exactly \(m-1\) degree-one bars \([1,2)\) and \(m-1\) degree-two bars \([2,3)\), with no other positive-dimensional bars.

## Assumptions and scope
Paths are internally vertex-disjoint and share only \(u\) and \(v\); lengths count graph **edges**. Parameter ranges throughout are \(m\ge3\), \(\ell\ge2\). The coefficient ring for the equivariant statements is \(\mathbb Z\), and the barcode assertion is over an arbitrary field. A face of \(R_r\) is any finite set of original graph vertices with every pair at graph distance at most \(r\). No claim is made about all later thresholds when \(\ell\ge4\).

## Proof
**Scale one and symmetry.** This graph has \(m\ell\) edges and \(m(\ell-1)+2\) vertices. It is connected, so its first homology is free of rank \(m-1\). Orient each arm from \(u\) to \(v\). A cellular one-cycle is a linear combination of the entire oriented arms with total coefficient zero: its lattice is precisely \(A_m\). A permutation of the arms permutes coordinates. Reversing endpoints reverses every oriented arm and therefore acts by \(-I\).

**Length two.** In this case the graph is \(K_{2,m}\), of diameter two. Every vertex pair is adjacent in its square, so \(R_2\) is the full simplex.

**Length three.** Write the paths \(u-a_i-b_i-v\), for \(1\le i\le m\), and set \(A=\{a_i\}\), \(B=\{b_i\}\). In the distance-two graph the vertices of \(A\) form one clique and those of \(B\) another; the only edges between \(A\) and \(B\) are the matching pairs \(a_ib_i\). Every vertex in \(A\cup B\) is distance at most two from each of \(u,v\), while \(d(u,v)=3\). Thus the **entire** Rips complex is the simplicial suspension
\[
R_2=\{u,v\}*K_m,\qquad
K_m=\Delta(A)\cup\Delta(B)\cup\bigcup_{i=1}^m[a_i,b_i].
\]
Collapse separately the contractible simplices \(\Delta(A)\) and \(\Delta(B)\) to points (as subcomplex cofibrations). The resulting graph has two vertices and \(m\) parallel one-cells. Thus \(K_m\simeq\bigvee^{m-1}S^1\) and \(R_2\simeq\bigvee^{m-1}S^2\). The oriented matching edges represent the coordinate lattice \(\mathbb Z^m\) and the cycle condition is zero total coefficient; hence \(\widetilde H_1(K_m;\mathbb Z)=A_m\).

For the integral reversal sign, choose \(i\ne j\) and form the oriented one-cycle
\[
c_{ij}=[a_i,b_i]+[b_i,b_j]+[b_j,a_j]+[a_j,a_i].
\]
Its class corresponds to the difference of the \(i\)-th and \(j\)-th matching coordinates, and such differences generate \(A_m\). Reversal sends \(a_i\leftrightarrow b_i\), hence \(\tau c_{ij}=-c_{ij}\) as oriented one-chains. The suspension cycle is \(z_{ij}=[u]*c_{ij}-[v]*c_{ij}\), where the vertex-first cone notation defines oriented triangles. Since \(\tau(u)=v\) and \(\tau(v)=u\), the two minus signs cancel: \(\tau z_{ij}=z_{ij}\). Arm permutations carry \(z_{ij}\) to \(z_{\sigma(i),\sigma(j)}\). Therefore the top integral homology is the claimed augmentation representation with **trivial** endpoint-reversal action.

**Lengths at least four.** Every simple cycle in \(\Theta_{m,\ell}\) uses two full arms and has length \(2\ell\ge8\). In a graph with girth at least seven, a set of three or more vertices mutually within graph distance two lies in the closed neighborhood \(N[w]\) of some vertex \(w\): three shortest paths of length at most two that fail to share a tree-like center would form a cycle of length at most six. In this girth range each new distance-two edge has a unique common neighbor, and distinct closed-neighborhood simplices intersect only in dimension at most one. Thus, for every \(w\), pair each simplex \(\sigma\) consisting of at least two neighbors of \(w\) with \(\sigma\cup\{w\}\), processing larger \(\sigma\) first. These are elementary free-face collapses that remove precisely the new distance-two edges and their higher faces, leaving the original graph. (An independent general statement with this girth bound is Proposition 2.2 of Adamaszek [2].) In particular the inclusion \(\Theta_{m,\ell}\hookrightarrow R_2\) is a homotopy equivalence. It is naturally \(S_m\times C_2\)-equivariant as an inclusion, so it identifies the integral first-homology representation, including the \(-I\) reversal action.

**Persistence for length three.** The longest shortest path in \(\Theta_{m,3}\) has length three, so at scale three the Rips complex is a simplex. At scale one all \(m-1\) classes are in degree one. At scale two this degree-one homology vanishes and \(m-1\) new free degree-two classes appear; at scale three these vanish. Thus the stated barcode is exact over every field.

## Verification
The self-contained `verifier.py` reconstructs all graph distances, all scale-one/scale-two faces, and all simplicial boundary matrices; performs exact elimination over \(\mathbf F_2\); validates the suspension as an **equality of face sets** at length three; and checks the claimed length-at-least-four elementary collapse pairs. It independently verifies the cycle-reversal signs as integral one-chain identities. The replay output is stored in `verification_output.txt`. Its finite range is \(3\le m\le6\) and \(2\le\ell\le5\); the all-parameter result rests on the preceding symbolic proof, not those tests.

## Relationship to prior work
Adamaszek [2], Proposition 2.2, proves collapse of the square clique complex to the graph for girth at least seven, and explicitly gives the known \(C_6\) scale-two sphere, which corresponds to only **two** arms of length three. That published case and its high-girth collapse do not determine the multiple-arm exceptional homotopy type or the two contrasting endpoint-reversal representations. Parks–Marchette [3] analyze general graph-power homology persistence without this exact family and representation. Adamaszek–Adams [1] give the foundational inclusive-Rips notation and classify samples on a circle; those results do not classify a branched theta graph. General metric-gluing results [4] address other gluing conditions and do not themselves supply the exact multiple-arm calculation.

## Limitations
The result concerns shortest-path distances **only among graph vertices**, not the geodesic continuum of the realization. Full barcode information is asserted only for length three. The integral action is an ordinary homology-module calculation for the specified action, not an equivariant homotopy-type classification. This mathematical statement has not undergone independent audit. A later or unindexed equivalent theorem in the graph-power literature remains a possible originality risk.

## References
[1] M. Adamaszek and H. Adams, *The Vietoris–Rips complexes of a circle*, arXiv:1503.03669 (first posted 2015-03-12); *Pacific Journal of Mathematics* **290** (2017), 1–40, primary MSC 55U10 among its primary codes. https://arxiv.org/abs/1503.03669

[2] M. Adamaszek, *Clique complexes and graph powers*, arXiv:1104.0433 (first posted 2011-04-03), Proposition 2.2, Sections 3 and 6; *Israel Journal of Mathematics* **196** (2013), 295–319. https://arxiv.org/abs/1104.0433

[3] A. D. Parks and D. J. Marchette, *Persistent homology in graph power filtrations*, *Royal Society Open Science* **3** (2016), 160228. https://doi.org/10.1098/rsos.160228

[4] M. Adamaszek, H. Adams, E. Gasparovic, M. Gommel, E. Purvine, R. Sazdanovic, B. Wang, Y. Wang and L. Ziegelmeier, *On homotopy types of Vietoris–Rips complexes of metric gluings*, arXiv:1712.06224. https://arxiv.org/abs/1712.06224
