# Sharp split-graph threshold and uniqueness for two-token maximum cuts

## Finding
For integers \(r\ge2\) and \(n\ge1\), let \(G_{r,n}=K_r\vee\overline K_n\): a clique \(C\) of \(r\) vertices joined to an independent set \(I\) of \(n\) vertices. Its simple, unweighted two-token graph \(F_2(G_{r,n})\) has the two-element subsets of \(V(G_{r,n})\) as vertices, with two states adjacent exactly when their symmetric difference is an edge of \(G_{r,n}\). Let \(m(H)\) denote the maximum number of edges crossing a two-part vertex cut of \(H\).

**Theorem.** For all \(r\ge2\) and \(n\ge r-1\),
\[
m(F_2(G_{r,n}))=rn(n+r-2).
\]
For \(n\ge r\), its only maximum cut up to interchange of the sides puts every mixed token state \(\{u,i\}\), with \(u\in C\) and \(i\in I\), on one side and every pure state on the other. At the boundary \(n=r-1\) the same maximum-cut value holds, but at least \(r+1\) distinct unordered maximum cuts exist. For all \(1\le n\le r-2\), the displayed formula is strictly smaller than the true maximum cut. Thus \(n=r-1\) is the exact threshold for the value formula, and \(n=r\) is the exact threshold for uniqueness within its range.

## Assumptions and scope
All graphs are finite, simple and unweighted. Clique vertices are pairwise adjacent; independent vertices are adjacent only to clique vertices. Token configurations are *unlabelled*, have no repeated vertex, and are distinct graph vertices even when automorphically equivalent. Two cut sides are unordered: cuts differing only by interchanging the sides count as one. The formula treats \(r\ge2,n\ge r-1\); only the strict failure of that formula, rather than an exact alternative value, is asserted below threshold.

## Proof
Write the token states as \(A_{uv}=\{u,v\}\) for \(u,v\in C\), \(B_{ui}=\{u,i\}\) for \(u\in C,i\in I\), and \(D_{ij}=\{i,j\}\) for \(i,j\in I\). The nonempty edge classes are \(AA\), \(BB\), \(AB\), and \(BD\). Their respective cardinalities are
\[
|E_{AA}|=r\binom{r-1}{2},\quad |E_{BB}|=n\binom r2,
\quad |E_{AB}|=2n\binom r2,\quad |E_{BD}|=2r\binom n2.
\]
The mixed-versus-pure cut crosses exactly the \(AB\) and \(BD\) classes. Consequently its size is
\[
2n\binom r2+2r\binom n2=rn(n+r-2).
\]
It remains to upper-bound every cut by this value.

We use a **weighted fractional packing of triangles**. If nonnegative weights \(w(T)\) are placed on graph triangles so that \(\sum_{T\ni e}w(T)\le1\) for every graph edge \(e\), then the number of uncut graph edges in *any* vertex bipartition is at least \(\sum_Tw(T)\). Indeed every triangle has at least one uncut edge, and summing weighted contributions cannot exceed the number of uncut edges because all edge loads are at most one.

The first triangle family consists, for every distinct \(v,w\in C\setminus\{u\}\) and \(i\in I\), of
\[
(A_{uv},A_{uw},B_{ui}), \qquad \text{weight }\gamma=1/n.
\]
Every \(AA\) edge occurs in precisely \(n\) triangles of this family and so has total load one. The second and third families are, for each \(u\ne v\in C\) and \(i\in I\),
\[
(B_{ui},B_{vi},A_{uv}),\qquad \text{weight }\alpha,
\]
and, for every \(j\in I\setminus\{i\}\),
\[
(B_{ui},B_{vi},D_{ij}),\qquad \text{weight }\beta.
\]
Every \(BB\) edge receives total load \(\alpha+(n-1)\beta\). In addition, each \(AB\) edge has load \((r-2)\gamma+\alpha\) and each \(BD\) edge has load \((r-1)\beta\). The latter two formulas exhaust all remaining edge capacities.

If \(n\ge r\), choose
\[
\alpha=0,\qquad\beta=1/(n-1),\qquad\gamma=1/n.
\]
Here \(n\ge2\); every \(AA\) and \(BB\) load is one, while the \(AB\) load \((r-2)/n\) is strictly below one and the \(BD\) load \((r-1)/(n-1)\) is at most one.

If \(n=r-1\) and \(r\ge3\), instead choose
\[
\alpha=\beta=1/(r-1),\qquad \gamma=1/n.
\]
Again the \(AA\) and \(BB\) loads are one, and the \(AB\) and \(BD\) loads are both at most one (in fact, equal to one). For the remaining boundary case \((r,n)=(2,1)\), take \(\alpha=1\), \(\beta=0\), \(\gamma=1\); all required loads are at most one.

In every allowed case the total weight of triangles equals the number of \(AA\) plus \(BB\) edges, because each weighted triangle is assigned to exactly one such edge and these edges all have load one. Hence every cut leaves at least
\[
r\binom{r-1}{2}+n\binom r2
\]
uncut edges. Subtracting from the total number of edges gives the stated upper bound and proves equality with the displayed cut.

To establish uniqueness for \(n\ge r\), observe that the \(AB\) edges have **strictly less than unit** fractional-triangle load. Equality in the uncut-edge bound forces every \(AB\) edge to be cut: otherwise the weighted inequality would have strict slack. Every \(A_{uv}\) is adjacent to both \(B_{ui}\) and \(B_{vi}\); as \(C\) is complete and \(r\ge2\), these relations force all \(B\) states onto one cut side and all \(A\) states onto the other. The target cut value then forces all \(BD\) edges also to cross; every \(D\) state has an incident \(BD\) edge because \(r\ge2\), so each \(D\) state joins the \(A\) side. This is exactly the mixed-versus-pure bipartition, up to swapping sides.

For sharpness and the boundary multiplicity, let \(N=r+n\). Any cut \(V(G_{r,n})=X\sqcup Y\) induces a *parity cut* on two-token states: the side of \(\{x,y\}\) is determined by whether \(|\{x,y\}\cap X|\) is odd. Each base-graph cut edge \(xy\) lifts to exactly \(N-2\) crossing two-token edges, one for every remaining vertex; noncut base edges lift to no crossing edges. Hence this induced cut has size \((N-2)|E_G(X,Y)|\).

Separating all \(r\) clique vertices from all \(n\) independent vertices cuts \(rn\) base edges. Moving one selected clique vertex to the independent side instead cuts \((r-1)(n+1)\) base edges. At \(n=r-1\) these are equal, producing the standard cut and \(r\) further, pairwise distinct unordered parity cuts of the same proven maximum size. These lifted cuts are distinct because different base bipartitions modulo complement induce different two-token parity partitions when \(N\ge3\). For \(1\le n\le r-2\), the latter base cut is strictly larger since
\[
(r-1)(n+1)-rn=r-1-n>0.
\]
Its parity lift is a cut of \(F_2(G_{r,n})\) strictly larger than \(rn(n+r-2)\). This proves the sharp failure below the boundary and completes the theorem.

## Verification
The standard-library verifier `verify.py` constructs the literal base graph and token graph independently, enumerates every weighted triangle, and sums its incident edge loads as exact rational numbers. It validates the capacity certificate for \(2\le r\le8\) and all \(\max\{1,r-1\}\le n\le r+3\), and independently enumerates all unordered cuts for seven small parameter pairs, including just-below and at-threshold instances. It also checks the explicit parity-lift obstruction for \(3\le r\le9\). Run using `python3 verify.py`; the output in `verification_log.txt` concludes `VERIFY_OK`. These finite computations corroborate rather than replace the preceding all-parameter proof.

## Relationship to prior work
Cai, Dalfó, Fernández and Fiol (first publicly posted November 4, 2026) study distinguishable-capacity generalizations of token graphs, with structural and metric invariants rather than maximum-cut thresholds of two-token graphs of complete split graphs. Classical token-graph and symmetric-square references are recorded in their bibliography.

Alejandro-Soto and collaborators' November 18, 2026 preprint, published after the November 4, 2026 paper, gives general token-graph maximum-cut lower and projection upper bounds, and treats complete, triangular, Kagome and random parent graphs. Its parity-lift lower bound and projection upper bound actually imply the **value formula in the easier regime \(n\ge r\)** after evaluating the base split-graph cuts; that part alone is not claimed as a new consequence. Crucially, those bounds leave a gap of \(r-1\) uncut edges at \(n=r-1\) and do not establish the exact boundary value, a matching fractional-packing certificate there, or the optimizer rigidity statement. These later results are cited to distinguish the exact new boundary statement from already established general bounds. This later work is cited for scientific comparison, not as the qualifying dated source. Claims of absolute priority cannot be made from database searches alone.

## Limitations
No exact formula is claimed for \(1\le n\le r-2\), only a strict improvement over the displayed expression. At \(n=r-1\) at least \(r+1\) optimal cuts exist, but their complete enumeration is not established here. The result is for two indistinguishable tokens, complete split parent graphs and unweighted edges; no conclusion about arbitrary parent graphs, distinguishable tokens, larger token counts, weighted variants or independent external validation follows. Historical publication priority remains provisional.

## References
1. Y. Cai, C. Dalfó, B. Fernández, M. À. Fiol, *On generalized \(k\)-token graphs with distinguishable tokens and a maximum capacity of \(s\) tokens per vertex*, arXiv:2611.06275v1, first posted 2026-11-04. https://arxiv.org/abs/2611.06275
2. J. A. Alejandro-Soto, P. T. Araujo, R. Fabila-Monroy, S. G. Gómez-Galicia, M. Hibat-Allah, M. M. R. Raj, M. A. Shamim, A. L. Trujillo-Negrete, *Max-Cut on Token Graphs*, arXiv:2611.25153v1, first posted 2026-11-18 (later comparison). https://arxiv.org/html/2611.25153v1
3. K. Audenaert, C. Godsil, G. Royle, T. Rudolph, *Symmetric squares of graphs*, Journal of Combinatorial Theory, Series B 97 (2007), 74–90.
4. R. Fabila-Monroy et al., *Token graphs*, Graphs and Combinatorics 28 (2012), 365–380.
