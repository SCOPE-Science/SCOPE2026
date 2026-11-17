# Higher tuplings of stacked odd-dimensional spheres are connected circle bouquets

## Finding
For integers \(r\ge3\) and \(N\ge2r+1\), let \(X\) be any stacked simplicial \((2r-1)\)-sphere with \(N\) vertices. Its \(r\)-tupling is a **connected graph** and admits the integral homotopy classification
\[
|D^r(X)|\simeq\bigvee^{\,1+(N-2r)\frac{r-1}{2}\binom{2r+1}{r}}S^1.
\]
Each stacking step contributes exactly \(\frac{r-1}{2}\binom{2r+1}{r}\) additional independent integral circles. The result depends only on \(r,N\), not on stacking history. At \(r=3\) the initial seven-vertex sphere gives \(36\) circles; each subsequent stacking adds \(35\).

## Assumptions and scope
Let \(r\ge3\) and let \(X_0=\partial\Delta^{2r}\), the boundary of a simplex with \(2r+1\) labeled vertices. Repeatedly choose a top-dimensional face \(F\) of cardinality \(2r\), introduce a new vertex \(w\), remove \(F\), and replace it by the \(2r\) faces \((F\setminus\{x\})\cup\{w\}\), where \(x\in F\). The resulting simplicial complex is \(X\). The integer \(N\) is its total number of vertices, so the number of operations is \(k=N-(2r+1)\).

For any finite simplicial complex \(Y\), define \(D^r(Y)\) to have as vertices the \(r\)-element faces of \(Y\). A set of distinct such vertices spans a simplex exactly when they are pairwise disjoint and their union is a face of \(Y\). Here each facet of \(X\) has cardinality \(2r\), so the tupling is at most one-dimensional. It has an edge precisely for an unordered complementary pair of \(r\)-sets spanning one top facet.

## Proof
**1. Base graph.** Every \(r\)-subset of the \(2r+1\) starting vertices belongs to a top facet of \(X_0\). Two disjoint \(r\)-subsets have union of size \(2r\), a top facet. Hence \(D^r(X_0)\) is the Kneser graph \(\operatorname{KG}(2r+1,r)\), with
\[
V_0=\binom{2r+1}{r},\qquad E_0=\frac{r+1}{2}\binom{2r+1}{r}.
\]
It is connected: any two \(r\)-subsets differing in one element have a common neighbor, namely the \(r\)-element complement of their union. Any pair of \(r\)-sets can be joined by a sequence of one-element exchanges. Thus its integral first Betti number is
\[
\beta_1(D^r(X_0))=E_0-V_0+1=1+\frac{r-1}{2}\binom{2r+1}{r}.
\]

**2. Local stacking operation.** Fix a top facet \(F\) of cardinality \(2r\) and introduce \(w\). Exactly \(\frac12\binom{2r}{r}\) old edges of \(D^r(X)\) have union \(F\), namely the complementary pairs \(\{A,F\setminus A\}\). They are deleted. The new tupling vertices are exactly \(\{w\}\cup B\) for \(B\subset F\) of cardinality \(r-1\), so the number of vertices added is
\[
\Delta V=\binom{2r}{r-1}.
\]
Every new tupling edge joins an old \(r\)-subset \(A\subset F\) to a new vertex \(\{w\}\cup B\) with \(|B|=r-1\) and \(A\cap B=\varnothing\). Conversely, every such pair forms the union of one of the new top facets: precisely the one missing the unique element in \(F\setminus(A\cup B)\). Therefore
\[
E_{\mathrm{new}}=\binom{2r}{r}\binom r{r-1}=r\binom{2r}{r},\qquad
\Delta E=\left(r-\frac12\right)\binom{2r}{r}.
\]
No other edges change, because the union of the two \(r\)-sets determines its top facet uniquely.

**3. Connectivity of the replacement.** The local replacement is a bipartite graph on old vertices \(\binom Fr\) and new vertices \(\{\{w\}\cup B:B\in\binom F{r-1}\}\), joining \(A\) to \(B\) exactly when \(A\cap B=\varnothing\). If two old \(r\)-sets \(A,A'\) differ by one element, their union has \(r+1\) elements, so \(F\setminus(A\cup A')\) has \(r-1\) elements and supplies a common new neighbor. Since the Johnson graph of \(r\)-subsets of \(F\) is connected, this entire bipartite replacement is connected. In particular the endpoints of every removed complementary-pair edge remain linked by a new path. Replacing these old edges therefore cannot disconnect the full graph, and every added vertex is attached. Connectivity is preserved at every stacking.

**4. Rank and integral homotopy.** Since the updated graph stays connected, its first Betti number increases by
\[
\Delta\beta_1=\Delta E-\Delta V
=\frac{r-1}{2}\binom{2r+1}{r},
\]
using \(\binom{2r}{r-1}=\frac r{r+1}\binom{2r}{r}\). With \(k=N-2r-1\) operations, the formula in the Finding follows. Every connected finite graph has the integral homotopy type of a bouquet of \(E-V+1\) circles, with torsion-free first homology and no higher homotopy contributions. This concludes the proof for all stated parameters.

## Verification
The independent finite enumerator `check_higher_tuple_stacked.py` constructs each tupling directly from the top facets and checks exact graph vertex/edge counts, connectedness and cycle rank, including every distinct labeled stacking complex through \(N=10\) at \(r=3\), through \(N=11\) at \(r=4\), and through \(N=12\) at \(r=5\). Its recorded output is `CHECK_OUTPUT.txt`. These checks confirm examples but are not used as a proof of the infinite theorem; Steps 1–4 provide that proof.

## Relationship to prior work
Lesh, Schreiner and Wahl introduced the general \(r\)-tupling operation and established a weak Cohen–Macaulay connectivity bound. At the boundary-sphere dimension here, their general theorem guarantees only the weakest nonemptiness-level bound, not the claimed connectedness or circle rank. A previously established calculation for the double of stacked three-spheres handles only \(r=2\); the present classification covers every \(r\ge3\), with a new uniform hypergraph-complement incidence argument. Previously published multipartite tuple-graph characters also do not address replacing top simplices of stacked spheres or the rank increment under such replacements.

## Limitations
Only stacked odd-dimensional spheres with the specified matching tupling threshold are covered. The result is nonequivariant. No formula for arbitrary triangulated spheres, arbitrary dimensions or other tupling indices is asserted. The literature comparison cannot exclude unindexed broader results. Independent mathematical review has not been performed.

## References
- Kathryn Lesh, Bridget Schreiner and Nathalie Wahl, *The double of a simplicial complex*, arXiv:2506.10436, first publicly submitted 2025-06-12, version 2 of 2026-10-27, https://arxiv.org/abs/2506.10436.
- The previously recorded stacked three-sphere double theorem and the multipartite tuple-graph homology classification are considered solely as mathematical prior-art comparators; no claims from them are needed in the proof.
