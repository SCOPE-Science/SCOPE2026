# Complete mutual-visibility and maximal-set polynomials of the Pappus graph

## Finding

Let \(P\) be the 18-vertex Pappus graph (the cubic Levi graph of the \((9_3)\) Pappus configuration), and let a vertex subset \(S\) be *mutually visible* when, for each distinct \(u,v\in S\), there exists a shortest \(u\)-to-\(v\) path in \(P\) with no internal vertex in \(S\). Define the full cardinality polynomial \(\mathcal V_P(z)=\sum_{S\text{ mutually visible}}z^{|S|}\), and define \(\mathcal F_P(z)=\sum_{S\text{ inclusion-maximal mutually visible}}z^{|S|}\). All vertices are distinguished (labeled); these are not automorphism-orbit enumerators.

The following complete finite identities hold:

\[
\boxed{\mathcal V_P(z)=1+18z+153z^2+762z^3+2340z^4+4374z^5+4605z^6+1998z^7+36z^8.}
\]

\[
\boxed{\mathcal F_P(z)=63z^6+1710z^7+36z^8.}
\]

In particular, the ordinary mutual-visibility number is \(\mu(P)=8\); the *lower* mutual-visibility number, meaning the minimum cardinality of an inclusion-maximal mutually visible set, is \(\mu^{-}(P)=6\). There are exactly \(14\,287\) mutually visible subsets, including the empty set, and \(1\,809\) inclusion-maximal ones. Under the full 216-element automorphism group, the inclusion-maximal sets split into **15 orbits**: two of size six, twelve of size seven, and one of size eight. The 36 maximum sets constitute a *single orbit*.

The exact orbit-size census is:

| Cardinality | Number of orbits of each size | Number of labeled facets |
|---|---|---:|
| \(6\) | one orbit of size \(9\); one of size \(54\) | \(63\) |
| \(7\) | two of size \(18\); one of size \(54\); three of size \(108\); six of size \(216\) | \(1710\) |
| \(8\) | one orbit of size \(36\) | \(36\) |

Consequently the simplicial complex of mutually visible subsets is **nonpure**, with maximal faces of three different sizes. A greedy inclusion-maximal placement can use six locations even though eight mutually visible locations are possible.

## Assumptions and scope

Identify the ground field with \(\mathbb F_3=\{0,1,2\}\). The point vertices are \(p_{x,y}\), where \(x,y\in\mathbb F_3\), and the line vertices are \(\ell_{m,b}\), where \(m,b\in\mathbb F_3\). Edges are exactly the \(27\) incidences

\[
 p_{x,y}\sim\ell_{m,b}\quad\Longleftrightarrow\quad y=mx+b\pmod 3.
\]

This is the affine plane of order three with the vertical parallel class deleted, yielding the standard 18-vertex Pappus graph. It is bipartite, cubic, of girth six and diameter four. It is **not** the different, sometimes similarly named, nine-vertex point-collinearity graph. The vertex indexing used by all checkers is: \(p_{x,y}\leftrightarrow3x+y\), and \(\ell_{m,b}\leftrightarrow 9+3m+b\), with zero-based indices \(0,\ldots,17\). Every selected set is represented by an 18-bit integer mask.

The distance in the visibility condition is always the original graph distance in \(P\), not the distance after deleting selected vertices. Unlike *total* mutual visibility, only pairs with both endpoints selected must be witnessed.

## Proof

**Finite exact enumeration lemma.** For distinct vertices \(i,j\), compute \(d(i,j)\) in the original graph by breadth-first search. Let \(\mathscr P_{ij}\) be the collection of bitmasks of internal vertices of all paths \(i=v_0,\ldots,v_d=j\) that are shortest in the original graph. They are enumerated with the strictly increasing-distance rule

\[
 d(i,v_{t+1})=d(i,v_t)+1,\qquad d(i,v_{t+1})+d(v_{t+1},j)=d(i,j).
\]

Any original shortest path obeys both equalities at every step; conversely, such a path reaches \(j\) in \(d(i,j)\) steps, so this enumerates **all and only** original geodesics. The path algorithm finds at most six shortest paths for any unordered pair of Pappus vertices. For a bitmask \(s\) encoding \(S\), define

\[
 \operatorname{good}(s)\Longleftrightarrow
 \forall\,i<j\text{ in }S\ \exists\,Q\in\mathscr P_{ij}:\ Q\mathbin{\&}s=0.
\]

Here \(\&\) denotes bitwise intersection. The equivalence to mutual visibility is immediate because \(Q\) consists exactly of the internal vertices of a shortest witness path. Thus a complete loop over the \(2^{18}=262\,144\) possible masks proves the coefficient at \(z^k\) by summing \(\operatorname{good}(s)\) over masks with \(k\) one-bits. The exhaustive checker `verification/visibility_paths.cpp` evaluates all masks and obtains the exact nine nonzero coefficient counts

\[
 (1,18,153,762,2340,4374,4605,1998,36).
\]

The family is **downward closed**: deleting selected vertices never removes a geodesic witness for any pair remaining selected. Hence a good mask is inclusion-maximal exactly when **every** one-vertex extension is not good; no larger extension can then be good. Counting these masks by size yields exactly \(63,1710,36\) facets of sizes \(6,7,8\), with none of any other size. This proves both polynomials and the extremal numbers.

**Independent acceptance test.** The source `verification/visibility_bfs.cpp` constructs the same incidence graph using a separately written adjacency representation and never enumerates geodesic paths. For each candidate pair \(i,j\), it recomputes a breadth-first-search distance with the vertices \(S\setminus\{i,j\}\) forbidden, and compares that distance with \(d(i,j)\). These distances are equal if and only if a geodesic with unselected interior exists. The program constructs all valid subsets by one-element extensions. This is exhaustive by downward closure and increasing integer-mask order. It independently gives **the same full binary state vector** (checked by a fixed-order 64-bit FNV fingerprint \(\mathtt{035086ad4bd0f946}\), displayed without the leading zero in the logs) and the same polynomial and facet counts. The fingerprint is corroboration, not a substitute for the exhaustive algorithms.

**Automorphism-orbit certificate.** For \(a,c\in\mathbb F_3^{\times}\) and \(b,d,e\in\mathbb F_3\), the following 108 vertex permutations preserve incidence:

\[
\begin{aligned}
 p_{x,y}&\mapsto p_{ax+b,\,cy+dx+e},\\
 \ell_{m,t}&\mapsto\ell_{(cm+d)/a,\,ct+e-b(cm+d)/a}.
\end{aligned}
\]

Together with the incidence-reversing involution \(p_{x,y}\leftrightarrow\ell_{x,-y}\), they give 216 distinct automorphisms. A second exhaustive algorithm in `verification/count_automorphisms.py` counts **every** distance-preserving vertex bijection of the graph by backtracking with all pairwise distance constraints, independently obtaining exactly 216, so these explicit maps form the full automorphism group. The embedded program `verification/symmetry_orbits.py` verifies that every permutation preserves all 27 edges, forms all 216 images of every facet, and partitions the entire list of 1,809 maximal masks into the displayed 15 orbits. The orbit sizes sum separately to \(63\), \(1710\), and \(36\), furnishing an independently checkable structural refinement.

The proof is a **finite exhaustive proof on a fixed graph**, with complete source and all branch conditions supplied. The calculations do not assert an unproved theorem for larger affine planes or a family of Pappus generalizations.

## Verification

Compile and run from the directory containing the embedded `verification/` subdirectory (or change to that subdirectory):

```sh
cd verification
g++ -O3 -std=c++17 visibility_paths.cpp -o visibility_paths
./visibility_paths
g++ -O3 -std=c++17 visibility_bfs.cpp -o visibility_bfs
./visibility_bfs
python3 symmetry_orbits.py
python3 count_automorphisms.py
```

The path-based checker writes `maximal_sets.txt` (the full list of 1,809 maximal masks) and `visibility_states.bin` (exactly 262,144 bytes of Boolean membership states); these reproducible outputs need not be pre-supplied. Run `symmetry_orbits.py` **after** the first checker, since it reads the generated maximal-mask list. The four expected standard-output transcripts appear in `verification/path_output.txt`, `verification/bfs_output.txt`, `verification/orbit_output.txt`, and `verification/automorphism_count_output.txt`.

Both C++ approaches return the polynomial coefficients above and the full-state fingerprint \(\mathtt{35086ad4bd0f946}\). The symmetry program returns orbit totals \((2,12,1)\) by facet size and a single 36-element orbit of optimal sets. Every required computation was rerun from the supplied source paths before the final scientific assessment.

## Relationship to prior work

Brešar and Yero (2023), *Lower (total) mutual visibility in graphs*, introduced \(\mu^{-}\), investigated its interpretation as a worst-case maximal (greedy) outcome, and developed general methods. Their inspected results concern other graph classes, not the fixed 18-vertex Pappus incidence graph or its 1,809 maximal sets. This work adds a complete instance to that motivated lower-invariant problem, including a nonpure case with explicit symmetry refinement. Boruzanlı Ekinci and Bujtás (2024), *Mutual-visibility problems in Kneser and Johnson graphs*, investigated related graph-family visibility parameters, but their bipartite Kneser family is not this Pappus graph; their theorem on **total** visibility has a different universal-pair requirement. Cicerone, Di Stefano and Klavžar's 2021 preprint on Cartesian products and triangle-free graphs studies general triangle-free visibility but does not supply this Pappus all-subsets census.

The graph's construction and standard properties are independently described in MathWorld's *Pappus Graph* entry, which lists its incidence realization and other invariants, not this polynomial. Public research-record searches for Pappus/visibility, incidence-graph aliases, exact coefficients, and stronger statements uncovered no result implying the full two-polynomial and orbit classification. This is a best-knowledge literature comparison, **not a guarantee of worldwide priority**.

## Limitations

Only the standard 18-vertex Pappus graph with the stated incidence relation is covered. An exhaustive finite census is not an infinite-family structural theorem. No results are asserted for other \((9_3)\) incidence configurations, for total, outer, dual, or one-tolerant visibility, or for the topology of the resulting simplicial complex beyond its nonpurity. Some computational databases can calculate general graph visibility invariants; an unindexed or dynamically generated Pappus table remains a residual literature risk. Mathematical validation by a separate independent auditor has not been performed.

## References

1. B. Brešar and I. G. Yero, *Lower (total) mutual visibility in graphs*, first arXiv version 6 July 2023, https://arxiv.org/abs/2307.02951.
2. G. Boruzanlı Ekinci and C. Bujtás, *Mutual-visibility problems in Kneser and Johnson graphs*, first arXiv version 22 March 2024, https://arxiv.org/abs/2403.15645.
3. S. Cicerone, G. Di Stefano, and S. Klavžar, *On the mutual-visibility in Cartesian products and in triangle-free graphs*, https://arxiv.org/abs/2112.13024.
4. E. W. Weisstein, *Pappus Graph*, MathWorld, https://mathworld.wolfram.com/PappusGraph.html.
