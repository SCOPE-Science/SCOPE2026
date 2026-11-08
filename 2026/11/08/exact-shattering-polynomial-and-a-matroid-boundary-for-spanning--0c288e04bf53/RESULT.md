# Exact shattering polynomial and a matroid boundary for spanning trees of \(K_{3,n}\)

## Finding
For an integer \(n\ge1\), let \(G_n=K_{3,n}\) have a named left side \(L=\{0,1,2\}\) and right vertices \(v_1,\ldots,v_n\). Let \(\mathcal T_{3,n}\subseteq 2^{E(G_n)}\) be the edge sets of all spanning trees. A query asks whether a given edge belongs to the unknown tree. A query support \(S\subseteq E(G_n)\) is **shattered** when every Boolean pattern on \(S\) is the trace of at least one spanning tree.

Write \(S_j=\{i\in L: iv_j\in S\}\). The complete **column criterion** is:

* \(|S_j|\le2\) for every \(j\);
* at most two columns have \(|S_j|=2\), and if two do, their two-element subsets of \(L\) differ;
* either at least one column is empty, or among columns with \(|S_j|=1\), the selected left vertices take at least two distinct values.

These conditions are **necessary and sufficient** for shattering. Define \(b_0=1\), \(b_k=3\) for every positive integer \(k\), and \((3)_{\underline 0}=1\), \((3)_{\underline 1}=3\), \((3)_{\underline 2}=6\). The exact all-cardinality polynomial is
\[
\boxed{\Phi_{3,n}(z)=\sum_{d=0}^{\min(2,n)}\binom nd(3)_{\underline d}z^{2d}\left((1+3z)^{n-d}-b_{n-d}z^{n-d}\right).}
\]
Its degree is
\[
\boxed{\operatorname{VCdim}(\mathcal T_{3,n})=\min\{n+2,\,2n-2\}.}
\]
The initial polynomials are \(\Phi_{3,1}(z)=1\), \(\Phi_{3,2}(z)=1+6z+12z^2\), \(\Phi_{3,3}(z)=1+9z+36z^2+78z^3+72z^4\), and \(\Phi_{3,4}(z)=1+12z+66z^2+216z^3+438z^4+504z^5+216z^6\).

There is also a **sharp structural boundary**: the shattered-support complex of the spanning-tree concept class on \(K_{2,n}\) is the rank-\((n-1)\) truncation of a partition matroid (one element at most per right column). For \(K_{3,n}\), the shattered-support complex is a matroid exactly for \(n\in\{1,2\}\); for each \(n\ge3\), it fails basis exchange. These statements concern finite labeled graphs, with no asymptotic qualifications.

## Assumptions and scope
The two sides of \(K_{3,n}\) are labeled; every graph is simple, finite, undirected and connected. Isolated components are never allowed in a spanning tree. The empty support counts as shattered. The polynomial counts individual **edge subsets**, not isomorphism types or different Boolean traces. The assertion about \(K_{2,n}\) concerns its analogous spanning-tree incidence class. No assertion is made for general \(K_{m,n}\) with \(m>3\).

## Proof
**Lemma 1 (general, not claimed as new).** For any connected finite graph \(G\), its spanning-tree edge-incidence concept class shatters \(S\subseteq E(G)\) if and only if \(S\) is a forest and \(G-S\) is connected. Necessity follows from the all-positive and all-negative patterns, respectively. For sufficiency fix an arbitrary positive edge subset \(P\subseteq S\). Since \(G-S\) is connected, \(G-(S\setminus P)\) is connected; since \(P\) is a forest, it extends to a spanning tree of that connected graph. This gives exactly the desired trace \(P\). The lemma is also the graphic-matroid specialization of the familiar independent/coindependent criterion for a matroid's bases.

**Lemma 2 (forest criterion).** If any column contains all three edges, \(G_n-S\) isolates its right vertex and cannot be connected. Under the necessary bound \(|S_j|\le2\), singleton columns contribute pendant selected edges and no selected cycles; each double column contributes a two-edge path joining the two selected left vertices. A selected cycle therefore corresponds exactly to a cycle of the multigraph of these double-column connections on the three left vertices. Such a multigraph is acyclic if and only if it has at most two edges and any two connect different left-vertex pairs. This proves the second condition.

**Lemma 3 (complement connectivity).** Under \(|S_j|\le2\), the right vertex \(v_j\) has at least one complementary incident edge. If some \(S_j\) is empty, that right vertex links all three left vertices, so the complement is connected. Otherwise every singleton \(S_j=\{i\}\) links the two left vertices other than \(i\) through \(v_j\), while every double column leaves only a pendant complementary edge. The graph on the left three vertices is connected precisely when at least two different singleton labels occur. This proves the third condition and completes the all-support characterization by Lemma 1.

**Exact enumeration.** Suppose precisely \(d\) columns are double. Lemma 2 restricts \(d\) to \(0,1,2\), and the corresponding selected left pairs must be distinct. There are \(\binom nd (3)_{\underline d}\) choices of these columns and their pairs, with weight \(z^{2d}\). Each remaining column is empty (weight \(1\)) or contains one of three singleton edges (weight \(3z\)). Without the connectivity condition this gives \((1+3z)^{n-d}\). By Lemma 3 the rejected configurations have no empty columns and either zero singleton columns (one case when \(n-d=0\)) or all their singleton labels equal (three cases when \(n-d>0\)). Their contribution is \(b_{n-d}z^{n-d}\). Subtracting proves the polynomial formula without any unstated independence assumption.

**VC dimension.** A shattered set is a forest on \(n+3\) vertices and therefore has at most \(n+2\) edges; its complement must remain connected and therefore have at least \(n+2\) edges, so \(|S|\le3n-(n+2)=2n-2\). The bound is sharp in every range. For \(n=1\), the empty support attains zero; for \(n=2\), take singleton edges in the two columns with different selected left vertices, obtaining two edges. For \(n=3\), use two different double columns and a third empty column, obtaining four edges. For \(n\ge4\), choose two double columns with different selected pairs and select one edge in each remaining column, with at least two distinct singleton labels. Lemmas 2 and 3 certify these \(n+2\) edges. Thus the formula for the VC dimension holds for all \(n\).

**Matroidality boundary.** On \(K_{2,n}\), the general criterion gives exactly the supports selecting at most one edge in any right column and omitting at least one column. These are the independent sets of the rank-\((n-1)\) truncation of a partition matroid. For \(K_{3,1}\), only the empty support is shattered. For \(K_{3,2}\), the supports select at most two edges with no repeated left label across the two columns; this is a rank-two partition matroid whose three groups are the two edges incident to each left vertex.

For \(n=3\), write a support as the list of its three column subsets. Consider \(A=(\{0,2\},\{0,1\},\varnothing)\) and \(B=(\{0,1\},\{0,2\},\varnothing)\). Both are shattered and have maximal cardinality four. The edge \(e=(2,v_1)\) belongs to \(A\setminus B\), while \(B\setminus A=\{(1,v_1),(2,v_2)\}\). Replacing \(e\) by \((1,v_1)\) creates two identical double-column pairs and hence a selected four-cycle; replacing it by \((2,v_2)\) makes the second column full and isolates that right vertex in the complement. Thus no basis exchange is possible. For every \(n\ge4\), use the same first two double columns in \(A,B\), choose singleton column \(3\) with selected left label \(1\), column \(4\) with selected left label \(0\), and all remaining columns with selected left label \(0\). Both supports have the maximum possible cardinality \(n+2\), and the same two attempted exchanges fail for the same reasons. Hence matroidality fails for all \(n\ge3\).

## Verification
Running `python3 verify_k3n_spanning_shattering.py` requires only the Python standard library. It independently enumerates all spanning trees of \(K_{3,n}\) for \(1\le n\le5\) by edge-subset union-find checks, compares every support's realized binary traces with the column criterion, counts the coefficients, verifies small matroid boundary conditions, and tests explicit exchange obstructions through \(n=8\). The final deterministic output contains `K3N_SPANNING_TREE_SHATTER_PASS 37448 supports 2551 trees`. These computations are independent finite corroboration, **not** the basis of the proofs for unrestricted \(n\).

## Relationship to prior work
Dong and Ge's publicly available 2021 preprint and its 2022 journal form count spanning trees of complete bipartite graphs containing a fixed spanning forest. Their problem concerns positive containment counts and does not provide this complete shattered-support polynomial or the exact matroidality transition. More broadly, the general matroid-basis fact that shattered sets are independent in both the matroid and its dual already gives the universal forest/complement-connected test; it is **not** claimed here as novel. The new all-parameter evaluation requires the three-left-vertex column classification, subtraction of exactly the complement-disconnection patterns, and a uniform exchange obstruction. This is not a claim of a new general-purpose matroid intersection theorem.

## Limitations
No classification for left sides of size greater than three is established. The finite checker stops at five right vertices for exhaustive trace comparisons and at eight for the displayed symbolic exchange witness. No independent mathematical audit has been performed; identification of all historical publications using alternate terminology remains incomplete. The polynomial enumerates shattered supports, not all trace sets, teaching dimensions, or sample-compression schemes.

## References
1. F. Dong and J. Ge, *Counting spanning trees in a complete bipartite graph which contain a given spanning forest*, arXiv:2103.05294, first public 2021-03-09, later *Journal of Graph Theory* 101 (2022), 79–94, DOI:10.1002/jgt.22812.
2. J. Edmonds, classical matroid-intersection theorem (used only for context: this proof needs no nontrivial matroid-intersection result).
