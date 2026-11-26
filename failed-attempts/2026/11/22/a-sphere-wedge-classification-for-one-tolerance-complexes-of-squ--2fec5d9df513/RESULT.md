# A sphere-wedge classification for one-tolerance complexes of squared paths

## Finding

For each integer \(n\ge 4\), let \(H_n=P_n^2\) be the simple graph on \(V=\{0,1,\ldots,n-1\}\) in which \(i\) and \(j\) are adjacent exactly when \(0<|i-j|\le2\). Let \(K_n=\operatorname{Cl}(H_n)\), the **filled** clique complex, and let \(X_n=\mathcal T_1(K_n)\). Then

\[
|X_n|\simeq\bigvee^{\binom{n-4}{2}} S^2.
\]

Here the empty wedge denotes a point, so the cases \(n=4,5\) are contractible. In fact, there is an explicit sequence of exactly \((n-3)^2\) elementary simplicial collapses removing every tetrahedron. The isomorphism \(\widetilde H_2(X_n;\mathbb Z)\cong\mathbb Z^{\binom{n-4}{2}}\) is integral, and all other reduced homology groups vanish.

## Assumptions and scope

The input is a finite path **square**, not the original one-dimensional path. Every triangle \(\{i,i+1,i+2\}\) is filled in \(K_n\), and no four vertices form a clique of \(H_n\). The tolerance definition is \(\mathcal T_1(K)=\{\sigma\subseteq V:\sigma\setminus\{v\}\in K\text{ for some }v\in\sigma\}\cup K\), equivalently a union of a face of \(K\) and at most one additional vertex. For \(n\ge4\), the faces of \(X_n\) are precisely the vertices and all two-element subsets; the triples containing an edge of \(H_n\); and the four-element subsets containing a consecutive triple. There are no larger faces. Binomial coefficients with an upper index smaller than the lower index are zero.

## Proof

**1. List of three-simplices.** Every tetrahedral vertex set is written uniquely as \(a<b<c<d\). Since the only original filled triangles are consecutive triples, a four-set is a tetrahedron of \(X_n\) if and only if \(b=a+1,c=a+2\), or \(c=b+1,d=b+2\). Call the former *L-type*. Call the latter *R-type* only when it is not L-type; thus its first entry satisfies \(a\le b-2\).

**2. Collapse L-types.** Order L-type tetrahedra \(\{a,a+1,a+2,d\}\), with \(d\ge a+3\), by increasing \(a\), breaking ties arbitrarily. Pair each with the triangular face \(\{a,a+1,d\}\), removing both. At this moment the chosen face is free: any tetrahedron containing it must complete a consecutive triple, and can only be the displayed tetrahedron or \(\{a-1,a,a+1,d\}\) when \(a>0\). The latter is an L-type tetrahedron with smaller first index and has already been removed. The paired triangular faces are distinct.

**3. Collapse R-types.** The remaining tetrahedra have the form \(\{a,b,b+1,b+2\}\), where \(a\le b-2\). Process them by **decreasing** \(b\). Pair such a tetrahedron with \(\{a,b+1,b+2\}\). Any other tetrahedron originally containing this face and a consecutive triple must be \(\{a,b+1,b+2,b+3\}\), if \(b+3<n\). It is an R-type with larger middle index and has already been removed. Thus each selected face is free. These faces are distinct and were not used in the first phase: the first-phase triangles have a pair of consecutive *smallest* entries, while these R-phase triangles have \(a\le b-2<b+1\). Every three-simplex disappears. The numbers of L- and R-type tetrahedra are respectively \(\binom{n-2}{2}\) and \(\binom{n-3}{2}\), whose sum is \((n-3)^2\).

**4. Simple connectivity.** The one-skeleton of \(X_n\) is the complete graph. It contains, for every \(i<j\), all triangles \(\{i,i+1,j\}\) whenever the three vertices are distinct, since \(\{i,i+1\}\) is an edge of \(H_n\). These triangle relations identify the edge path from \(i\) to \(j\) with the path \(i,i+1,\ldots,j\). Consequently every edge loop is nullhomotopic. This proves \(\pi_1(X_n)=0\); elementary collapses preserve this property.

**5. Euler characteristic and the wedge.** The counts of vertices, edges, triangles, and tetrahedra are
\[
f_0=n,\quad f_1=\binom n2,\quad f_2=\binom n3-\binom{n-4}{3},\quad f_3=(n-3)^2.
\]
The omitted triples are exactly independent triples in the squared path, whose sorted indices have successive gaps at least three; these are counted by \(\binom{n-4}{3}\). The resulting Euler characteristic satisfies
\[
\chi(X_n)=n-\binom n2+\binom n3-\binom{n-4}{3}-(n-3)^2=1+\binom{n-4}{2}.
\]
After the collapses the complex is connected, simply connected, and two-dimensional. Such a finite CW complex is homotopy equivalent to a wedge of two-spheres: its second homology is free, Hurewicz realizes a basis by spheres, and the resulting map from their wedge induces an integral homology isomorphism, hence a homotopy equivalence by Whitehead's theorem. Its sphere multiplicity is \(\chi-1=\binom{n-4}{2}\), as claimed.

## Verification

The accompanying standalone script `checks/check_tolerance_path_square.py` constructs every face directly from the definitions, then checks in real time that each prescribed triangular face is free at the moment of its removal, for all \(4\le n\le50\). It checks all \(35,720\) collapse pairs, face counts and Euler identities. For \(4\le n\le12\), it additionally builds simplicial boundary matrices and verifies their ranks independently over \(\mathbb F_2\), finding \(\widetilde\beta_2=\binom{n-4}{2}\) and zero first and third Betti numbers. Run `python3 checks/check_tolerance_path_square.py` using Python 3. These finite tests are diagnostic only; the free-face argument and homotopy proof above establish the assertion for all integers \(n\ge4\) over the integers.

## Relationship to prior work

Kim and Lew, *Leray numbers of tolerance complexes* (2021 preprint, 2023 publication), introduced the general tolerance framework and established Leray bounds; their theorems do not provide this explicit homotopy type. Selvaraja, *Tolerance complexes of chordal graphs and squarefree symbolic powers* (first available 10 November 2026), proves collapsibility and Leray bounds for chordal graphs, in particular interval graphs, but its statements do not identify the homotopy type or rank for the present filled-triangle path-square family. The graph \(H_n\) is an interval graph, so those general bounds apply; the new content here is the complete integral homotopy type and a uniform explicit elementary-collapse certificate.

## Limitations

The result is restricted to the one-tolerance construction and the clique complexes of squared paths. It does not claim an all-parameter classification for higher powers of paths, arbitrary interval graphs or \(t\ge2\). Neither the finite checker nor an unsuccessful literature search proves priority; the proof is a direct combinatorial argument and awaits independent validation.

## References

1. S. Selvaraja, *Tolerance complexes of chordal graphs and squarefree symbolic powers*, arXiv:2611.14384, initial public version 10 November 2026, https://arxiv.org/html/2611.14384v1 .
2. M. Kim and A. Lew, *Leray numbers of tolerance complexes*, arXiv:2109.03030, initial public version 7 September 2021; *Combinatorica* 43 (2023), https://arxiv.org/html/2109.03030v1 .
