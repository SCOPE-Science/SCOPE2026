# Integral homotopy of induced-forest complexes under partial matching deletion

## Finding
Let \(p,q\ge 2\) and \(0\le t\le\min\{p,q\}\). Label the shores of a complete bipartite graph by \(A=\{a_1,\ldots,a_p\}\) and \(B=\{b_1,\ldots,b_q\}\), and delete the \(t\) independent edges \(a_i b_i\), \(1\le i\le t\). Write \(G_{p,q,t}\) for the resulting graph and \(\mathcal F(G)\) for the abstract simplicial complex whose faces are vertex subsets inducing **acyclic** graphs. Put
\[
\beta_{p,q,t}=(t-1)(p-1)(q-1)-(p+q-3)\binom t2+\binom t3.
\]
Then the following is a complete **integral homotopy** classification:
\[
\mathcal F(G_{p,q,t})\simeq
\begin{cases}
\displaystyle\bigvee^{(p-1)(q-1)} S^2,&t=0,\\
\displaystyle\bigvee^{\beta_{p,q,t}}S^3\ \vee\ \bigvee^{\binom t3}S^4,&1\le t\le\min\{p,q\}.
\end{cases}
\]
An empty wedge is a contractible space. In particular, the first missing cross-edge makes the complex contractible, the second yields \(\bigvee^{(p-2)(q-2)}S^3\), and the third creates the first four-dimensional sphere. For \(t=\min\{p,q\}\) with \(p=q=n\), the formula specializes to the previously established crown-graph result \(\bigvee^{\binom{n-1}3}S^3\vee\bigvee^{\binom n3}S^4\). The new content is the complete intermediate matching-defect range, including rectangular shores.

## Assumptions and scope
Graphs are finite, simple and undirected. The missing cross-edges form a matching, so no vertex is an endpoint of two deleted edges. The vertex-set forest complex is **not** the graphic-matroid complex of edge subsets, a dissociation complex, or a cut complex. Geometric realizations, reduced homology and all stated homotopy equivalences are integral. The zero-, one- and full balanced-matching stages are included to state a complete classification, but their sphere counts are previously known. There are no connectivity or regularity hypotheses beyond the displayed domain.

## Proof
**1. The reference complex.** Let \(Q=\mathcal F(K_{p,q})\). Its faces meet at most one shore in two or more vertices, since any four selected vertices with two on each shore form a four-cycle. Thus
\[
Q=(\Delta_A*B_{\mathrm{disc}})\ \cup\ (A_{\mathrm{disc}}*\Delta_B).
\]
The two pieces are contractible; their intersection is the one-dimensional simplicial graph \(K_{p,q}\). The homotopy pushout, or Mayer–Vietoris followed by Whitehead, gives \(Q\simeq\bigvee^{(p-1)(q-1)}S^2\). In particular, there is a natural integral identification
\[
H_2(Q;\mathbb Z)\cong I_p\otimes_{\mathbb Z}I_q,
\qquad I_s=\ker(\mathbb Z^s\xrightarrow{\sum}\mathbb Z),
\]
under which the boundary of the tetrahedron on \(\{a_i,a_j,b_k,b_l\}\) maps to \(\pm(e_i-e_j)\otimes(e_k-e_l)\). Here the sign is determined by the chosen orientation; this is the fundamental four-cycle in the intersection graph.

**2. Exact relative face census.** Put \(F=\mathcal F(G_{p,q,t})\). Since deleting edges cannot create graph cycles, \(Q\subseteq F\). Every additional face contains at least two vertices on each shore. If it contained at least three on each, the induced six-vertex subgraph would have at least \(9-3=6\) edges, exceeding the five-edge bound for a forest. If it contained two on one shore and at least four on the other, a six-vertex subset would have at least \(8-2=6\) edges, again forcing a cycle. Hence additional faces have shore sizes \((2,2)\), \((2,3)\) or \((3,2)\), and no others.

A \((2,2)\)-set is a face precisely when it contains at least one complete deleted matching pair \(\{a_i,b_i\}\). The number of such *relative three-simplices* is therefore
\[
c_3=t(p-1)(q-1)-\binom t2.
\]
A \((2,3)\)-set is a forest precisely when the two vertices on its smaller shore correspond to two distinct deleted matching indices and their two partners lie in the larger shore. The same holds with the shores exchanged. Consequently the number of *relative four-simplices* is
\[
c_4=\binom t2(p+q-4).
\]
There are no new simplices of dimensions zero, one or two. The relative chain complex \(C_*(F,Q;\mathbb Z)\) is thus \(0\to\mathbb Z^{c_4}\xrightarrow{\partial_4}\mathbb Z^{c_3}\to0\) in degrees four and three, with the connecting map to \(H_2(Q)\) understood separately.

**3. Primitive integral rank of the relative boundary.** Call a relative three-simplex *triple-supported* if its two left and two right label sets together contain exactly three distinct indices. Project \(C_3(F,Q;\mathbb Z)\) onto the free coordinate subgroup on triple-supported relative simplices. Every relative four-simplex uses exactly three distinct indices, of which at least two are among the missing matching indices. Projected boundary matrices therefore split as disjoint blocks indexed by those three-element label sets.

If a support triple has precisely two deleted indices, it supplies two relative four-simplices, one of each shore shape. Their projected boundaries each have two coefficients \(\pm1\) on **disjoint** pairs of relative three-simplices. Hence this block has rank two with a unit maximal minor. If all three support indices are deleted, all six five-vertex subsets of the associated six-vertex set are relative four-simplices; their projected boundaries have two nonzero coefficients each and form the signed incidence matrix of a six-cycle. It has rank five and a unit rank-five minor. The one signed relation is the boundary of the formal five-simplex on \(\{a_i,a_j,a_k,b_i,b_j,b_k\}\); its boundary vanishes in the *full* integral simplicial chain complex, not merely after projection.

There are \(\binom t2(p+q-2t)\) four-simplices in the two-deleted-index blocks and \(6\binom t3\) in the three-deleted-index blocks. All projected images are primitive sublattices, and the only full integral kernel generators are the \(\binom t3\) six-term boundaries just described. It follows that
\[
\ker(\partial_4)\cong\mathbb Z^{\binom t3},\qquad
\operatorname{rank}(\partial_4)=c_4-\binom t3,
\]
and \(\operatorname{im}(\partial_4)\) is primitive in \(C_3(F,Q;\mathbb Z)\). Primitivity follows because its projection is primitive and injective on its image; the remaining non-triple-supported coordinates only describe the graph of an integral map over that primitive sublattice. This is an integer statement, not an inference from a field-rank computation.

**4. The connecting map and the integral Betti numbers.** For \(t\ge1\), fix one deleted pair \(a_d b_d\). All \((p-1)(q-1)\) relative tetrahedra \(\{a_d,a_i,b_d,b_j\}\), with \(i\ne d\) and \(j\ne d\), are present. Their connecting images in \(H_2(Q;\mathbb Z)\) are exactly \(\pm(e_d-e_i)\otimes(e_d-e_j)\). They constitute an integral basis of \(I_p\otimes I_q\). Thus the connecting map \(C_3(F,Q)\to H_2(Q)\) is split surjective. Since \(\partial_4\) maps into its kernel, the long exact sequence of \((F,Q)\), together with Step 3, gives
\[
\widetilde H_2(F;\mathbb Z)=0,\qquad
\widetilde H_3(F;\mathbb Z)\cong\mathbb Z^{c_3-(p-1)(q-1)-c_4+\binom t3},
\qquad
\widetilde H_4(F;\mathbb Z)\cong\mathbb Z^{\binom t3}.
\]
The degree-three quotient is free: its denominator is primitive in the free relative chain group. Substituting \(c_3,c_4\) gives the displayed \(\beta_{p,q,t}\). All other reduced integral homology vanishes.

**5. From integral homology to homotopy.** All vertex triples induce forests in any bipartite graph, so \(F\) and \(Q\) have exactly the same complete two-skeleton. Consequently \(F\) is simply connected. The homology groups just calculated are free and concentrated in the two consecutive degrees three and four. The standard simply connected, consecutive-degree sphere-wedge theorem (equivalently, Hurewicz, integral cell cancellations and Whitehead) yields \(F\simeq\bigvee^{\beta_{p,q,t}}S^3\vee\bigvee^{\binom t3}S^4\). For \(t=1\), both ranks vanish and Whitehead gives contractibility. The \(t=0\) case was established in Step 1. This proves all parameters, without computational extrapolation.

## Verification
The accompanying standalone `verify.py` enumerates all vertex subsets and tests induced acyclicity using a union–find graph-cycle test, independently of the relative-face classification. It then reconstructs the simplicial boundary operators over \(\mathbb F_2\) and checks every predicted reduced Betti number. All \(65\) cases \(2\le p\le q\le6\) and \(0\le t\le p\) passed, with \(20,934\) enumerated forest faces in aggregate. Separate checks of new relative three- and four-face counts also passed. Run `python3 verify.py`; no external packages or internet access are required. The finite field checks corroborate the general theorem, while the integral primitivity and homotopy conclusions depend on the proof above.

## Relationship to prior work
Carnero Bravo's *The Forest Filtration of a Graph* introduces the unrestricted vertex-induced forest complex, establishes homotopy calculations for \(K_{p,q}\) and for complete crown graphs \(K_2\times K_n\), and supplies the simply connected consecutive-degree wedge criterion. Those intact and full-matching endpoint results are **not** claimed as novel. A subsequent published one-edge-deletion theorem establishes the contractible stage \(t=1\), again an already-covered endpoint. An existing bivariate induced-forest enumerator for matching-deleted complete bipartite graphs determines face counts, but does not establish the integral boundary ranks, primitivity, or homotopy types of intermediate stages. The new claim determines those integral homotopy types **for every partial matching size** and every rectangular choice of shore sizes. Its two- and three-deleted-edge stages make the difference especially visible: the second deletion creates a family of three-spheres, while the third creates a genuine four-sphere alongside them.

## Limitations
The theorem assumes the deleted edges form a matching and does not cover arbitrary sets of missing bipartite edges. It identifies the homotopy types of each stage, not all maps in the edge-deletion filtration or a natural equivariant splitting. All verification beyond the symbolic proof is finite and over \(\mathbb F_2\). This work has not undergone independent mathematical audit. An unindexed equivalent result or a stronger theorem not captured by the inspected sources remains a bibliographic risk.

## References
1. Andrés Carnero Bravo, *The Forest Filtration of a Graph*, first public arXiv version 2023-07-25, arXiv:2307.13271, especially the complete-bipartite and crown-graph calculations and the consecutive-degree wedge theorem. https://arxiv.org/abs/2307.13271
2. *A one-edge homotopy transition for induced-forest complexes of bipartite graphs* (2026), previously established missing-edge connectivity and one-deletion contractibility; publicly accessible result at https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-one-edge-homotopy-transition-for-induced-forest-complexes-of-b--e5b294bc3a20
3. *Integral symmetry modules of crown-graph induced-forest complexes* (2026), whose background explicitly records the earlier full-crown sphere counts. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-integral-symmetry-modules-of-crown-graph-induced-forest-complexe--254ef80c8528
4. *Bivariate induced-forest enumerator of matching-deleted bicliques* (2026), matching-defect face-count classification, without intermediate homotopy types. https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-bivariate-induced-forest-enumerator-of-matching-deleted-biclique--373532fcf326
