# Extremal forests and enumeration of weak two-metric bases in near-square rook graphs

## Finding

Let \(8\le n\le m\le 2n-5\) be integers and \(G=K_n\square K_m\). Write \(N=n+m=3q+r\), where \(r\in\{0,1,2\}\). A landmark set \(S\subseteq V(G)\) is *weak two-resolving* when, for every distinct \(x,y\in V(G)\),
\[
\Delta_S(x,y)=\sum_{w\in S}|d_G(x,w)-d_G(y,w)|\ge2.
\]
Represent \(S\) by the simple bipartite incidence graph \(H_S\) on the \(n\) labelled row vertices and \(m\) labelled column vertices; a selected landmark is one row-column edge.

**Theorem.** Every smallest weak two-resolving set has \(|S|=N-q=\lceil2N/3\rceil\). More strongly, the complete collection of minimum sets consists precisely of the bipartite forests \(H_S\) with \(q\) components of the following orders:

* If \(r=0\), all \(q\) components are trees of order \(3\).
* If \(r=1\), exactly one component is a tree of order \(4\) and the other \(q-1\) have order \(3\).
* If \(r=2\), either one component has order \(5\) and the other \(q-1\) have order \(3\), or two components have order \(4\) and the other \(q-2\) have order \(3\).

All forests on the specified labelled row and column vertex classes with these component orders are permitted, with no further condition on tree shapes or which part contains their vertices.

Define the following bivariate exponential component polynomials:
\[
\begin{aligned}
T_3(u,v)&=\frac{u^2v+uv^2}{2},\\
T_4(u,v)&=\frac{u^3v+uv^3}{6}+u^2v^2,\\
T_5(u,v)&=\frac{u^4v+uv^4}{24}+u^3v^2+u^2v^3.
\end{aligned}
\]
The exact number \(B_{n,m}\) of distinct minimum landmark sets (row and column labels fixed) is \(n!m!\) times the coefficient \([u^nv^m]\) in
\[
F_{q,r}(u,v)=
\begin{cases}
T_3(u,v)^q/q!,&r=0,\\
T_3(u,v)^{q-1}T_4(u,v)/(q-1)!,&r=1,\\
T_3(u,v)^{q-1}T_5(u,v)/(q-1)!+T_3(u,v)^{q-2}T_4(u,v)^2/(2(q-2)!),&r=2.
\end{cases}
\]
For example, \(B_{8,8}=31{,}046{,}400\), \(B_{8,9}=1{,}079{,}038{,}800\), and \(B_{8,10}=47{,}628{,}000\).

## Assumptions and scope

Graphs are finite, undirected, simple and labelled, and \(\square\) denotes the Cartesian graph product. Different choices of a landmark vertex count separately; no quotient by graph automorphisms is taken. All statements are uniform over the integer range \(8\le n\le m\le2n-5\). The minimum cardinality alone is **not** a new claim: a previously released complete numerical formula covers it. The contribution here is the *complete shape classification* and *labelled extremal enumerator*.

## Proof

**1. Exact distance constraints.** For row \(i\) and column \(j\) let \(g_i\) and \(h_j\) denote degrees in \(H_S\), and let \(A_{ij}\in\{0,1\}\) be the incidence indicator. From \(d((i,j),(a,b))=[i\ne a]+[j\ne b]\), same-row pairs have \(\Delta_S=h_j+h_{j'}\), same-column pairs have \(\Delta_S=g_i+g_{i'}\), and nonaligned pairs satisfy
\[
\Delta_S((i,j),(i',j'))=g_i+g_{i'}+h_j+h_{j'}-2A_{ij'}-2A_{i'j}.
\]
Thus if all row and column degrees are positive and no connected component of \(H_S\) is an isolated single edge, then \(S\) is weak two-resolving. Indeed, the same-row and same-column tests are automatic; a nonaligned pair with at most one occupied cross-corner has separation at least \(4-2=2\); if both cross-corners are occupied, they are vertex-disjoint edges with endpoint-degree sum at least \(3+3=6\), since neither is a one-edge component, and separation is at least \(6-4=2\). Conversely, any weak two-resolving set must satisfy these exact distance constraints, including the endpoint-degree inequality at least six for disjoint selected edges.

**2. No empty class, no isolated edge at optimum.** Put \(s=\lceil2N/3\rceil\). The parameter range implies \(N\le3n-5\) and therefore \(s\le2n-3\). An empty row forces the other \(n-1\) row degrees to be at least two by the same-column tests, hence \(|S|\ge2n-2>s\). An empty column similarly implies \(|S|\ge2m-2\ge2n-2\). Now suppose that a weak two-resolving set with no empty row or column has a one-edge component \(e\). The disjoint-edge condition forces every other edge to have endpoint-degree sum at least four, so every other connected component has at least four vertices. For a connected component on \(v\ge4\) vertices, its edge count is at least \(v-1\ge3v/4\). Consequently
\[
|S|\ge 1+\frac{3}{4}(N-2)=\frac{3N-2}{4}>\left\lceil\frac{2N}{3}\right\rceil=s
\]
for \(N\ge16\), which holds here. Hence no set of size at most \(s\) has an empty class or one-edge component.

**3. Forest rigidity.** If \(H_S\) has no isolated vertices and no one-edge component, each component has order \(v\ge3\) and at least \(v-1\ge2v/3\) edges. Therefore \(|S|\ge\lceil2N/3\rceil=s\). Equality implies, writing \(c\) for the number of components, \(c\le q=\lfloor N/3\rfloor\) and \(|S|\ge N-c\), so necessarily \(c=q\), each component is a tree, and the excess orders satisfy \(\sum_C(|V(C)|-3)=r\). Since \(r=0,1,2\), precisely the three component-order alternatives in the statement occur.

**4. Attainment and sufficiency.** To realize every admissible pair of part sizes, construct disjoint bipartite trees as follows. When \(r=0\), take \(a=(2m-n)/3\) three-vertex stars centered on a row, and \(b=(2n-m)/3\) centered on a column. When \(r=1\), use one four-vertex path with two row and two column vertices, together with \(a=2q-n\) row-centered three-vertex stars and \(b=n-q-1\) column-centered ones. When \(r=2\), replace the four-vertex path by a five-vertex tree with two row and three column vertices, and use the same values of \(a,b\). The displayed integer parameters are nonnegative throughout the stated range and sum to the required row/column counts. Every constructed component is a tree on at least three vertices, so Step 1 proves weak two-resolution. Each has exactly \(s=N-q\) edges. More generally, Step 1 shows that **every** bipartite forest of the prescribed component sizes gives a minimum weak two-resolving set.

**5. Labelled enumeration.** On \(a\) labelled rows and \(b\) labelled columns, the number of spanning trees of the complete bipartite graph \(K_{a,b}\) is \(a^{b-1}b^{a-1}\) for \(a,b\ge1\). Enumerating tree components of total order three, four, and five, and dividing respectively by \(a!b!\), gives exactly \(T_3,T_4,T_5\) above. The two-colour exponential formula for unordered connected components gives \(F_{q,r}\). Multiplication by \(n!m!\) restores the labels. This exhausts all minimum sets by Steps 3 and 4.

## Verification

The accompanying standalone `artifacts/verify.py` performs exact rational polynomial coefficient extraction for six parameter pairs in the theorem and constructs a valid minimum set for every pair \(8\le n\le16\), \(n\le m\le2n-5\), independently checking every pair of graph vertices against the distance-sum definition. The accompanying `artifacts/verify_six.cpp` enumerates every \(8\)-edge subset of the \(6\times6\) row-column grid with positive degrees and no one-edge component, verifies all pair distances directly, and finds exactly \(8100\); this smaller case is a supporting check of the combinatorial method and lies outside the stated parameter range. These finite checks are not an unrestricted proof; Steps 1–5 supply that proof.

## Relationship to prior work

Fernández, Klavžar, Kuziak, Muñoz-Márquez and Yero introduced the Hamming-graph weak-metric problem and calculated the square case, with incidence-matrix distance identities, small rectangular computations, and a square-case proof that minimum incidence graphs have no isolated edge component. Their square-case component lower bound already contains the main rigidity mechanism. Kumar proved the sharp rectangular equality threshold for \(k=2\) and other parameter regimes. A separately released formal mathematical resolution provides the **complete scalar formula** \(\operatorname{wdim}_2(K_n\square K_m)=\min\{\lceil2(n+m)/3\rceil,2n-2\}\) in the rectangular range. Its distance identities, degree-counting bounds and incidence-forest constructions therefore cover the numerical part of the present result and are acknowledged as prior work. The present contribution is the explicit necessary-and-sufficient **classification of every optimal landmark incidence graph** at the near-square endpoint, including all allowed component shapes, and the corresponding exact bivariate exponential enumerator of labelled optimum sets. These refinements are not implied by knowing only the minimum cardinality; they are nevertheless structurally related to the existing lower-bound proof, and equivalently phrased enumerations in other literature remain possible.

## Limitations

The classification is restricted to \(8\le n\le m\le2n-5\); it does not treat the transition strip where a minimum set may have an empty row, or higher weak-resolution parameters. The scalar minimum and the foundational distance identities are not claimed as new. Exact count formulas do not classify symmetry orbits. The available literature search did not exhaust every index or all unpublished combinatorial notes, so historical priority is provisional. No independent mathematical audit has been performed.

## References

1. E. Fernández, S. Klavžar, D. Kuziak, M. Muñoz-Márquez, I. G. Yero, *On the weak \(k\)-metric dimension of Hamming graphs*, arXiv:2505.19642, first posted 2025-05-26, https://arxiv.org/abs/2505.19642.
2. A. Kumar, *Weak \(k\)-metric dimension of Hamming graphs: rectangular products and near-maximum parameters*, arXiv:2609.32161, first posted 2026-09-26, https://arxiv.org/abs/2609.32161.
3. *Kumar's remaining rectangular weak two-metric dimensions*, publicly accessible resolution and argument, https://www.trureturing.org/research/kumar-2026-rectangular-weak-two-metric-dimension/, inspected 2026-11-06; posting date not independently established.
