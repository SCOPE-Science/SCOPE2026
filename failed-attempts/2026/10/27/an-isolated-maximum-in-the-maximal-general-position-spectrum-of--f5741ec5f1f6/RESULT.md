# An isolated maximum in the maximal general-position spectrum of sunlet graphs

## Finding
For every integer \(n\geq4\), form the sunlet \(S_n=C_n\circ K_1\), with cycle vertices \(c_i\) and their distinct private leaves \(\ell_i\), indexed by \(i\in\mathbb Z/n\mathbb Z\). A vertex set is in *general position* if no three of its distinct vertices lie on a common shortest path. A general-position set is *maximal* if no further vertex can be added while retaining the property (not necessarily largest by cardinality).

**Theorem.** The only maximum-cardinality general-position set of \(S_n\) is the full leaf set \(L=\{\ell_i:i\in\mathbb Z/n\mathbb Z\}\), of size \(n\). Among all other inclusion-maximal general-position sets, the largest cardinality is exactly
\[
\left\lceil\frac n2\right\rceil+1.
\]
In particular, no inclusion-maximal general-position set has cardinality \(k\) with
\[
\left\lceil\frac n2\right\rceil+2\le k\le n-1.
\]
For \(n\ge6\) this is an interval of exactly \(\lfloor n/2\rfloor-2\) missing cardinalities, unbounded in a family of connected, subcubic, unicyclic graphs. **This is a statement about maximal sets, not a vanishing-coefficient assertion for the ordinary general-position polynomial**: proper subsets of \(L\) remain general-position sets.

## Assumptions and scope
All graphs are finite, simple and undirected. The graph \(C_n\) is the ordinary cycle, and the corona attaches **exactly one** leaf to every cycle vertex. The graph distance \(d_G(u,v)\) is the length of a shortest path. A vertex \(v\) lies on some geodesic between \(u,w\) exactly when \(d_G(u,w)=d_G(u,v)+d_G(v,w)\). The terms maximal and maximum are not interchangeable. We assume \(n\ge4\) throughout the theorem; \(n=3\) is excluded because additional maximum sets besides the three leaves exist.

## Proof
**1. The leaf-only case and the fiber constraint.** Every subset of the leaves is in general position: a leaf cannot be an internal vertex of a path. Therefore the only maximal set containing no cycle vertex is \(L\). If a general-position set \(M\) has at least three vertices, it cannot contain both \(c_i\) and \(\ell_i\), since a shortest path from \(\ell_i\) to any third selected vertex passes through \(c_i\). Hence such a set uses at most one vertex from every pair \(\{c_i,\ell_i\}\).

**2. Geodesic obstruction at a chosen core vertex.** Suppose a general-position set \(M\) contains a cycle vertex; after rotating indices, take \(c_0\in M\). If \(|M|=2\), its size is already below the asserted bound. Otherwise, let \(I\subseteq\mathbb Z/n\mathbb Z\setminus\{0\}\) consist of indices of the other occupied core–leaf pairs. There is at most one selected vertex per such pair. Construct a graph \(B_0\) on \(\mathbb Z/n\mathbb Z\setminus\{0\}\), joining distinct \(a,b\) if and only if
\[
d_{C_n}(a,b)=d_{C_n}(a,0)+d_{C_n}(0,b).
\]
If \(a,b\in I\) were adjacent in \(B_0\), a shortest path between the chosen vertices in fibers \(a,b\) would pass through \(c_0\): adjoining pendant endpoints changes both path lengths by the same fixed endpoint contributions. This would contradict general position. Therefore \(I\) is independent in \(B_0\).

**3. An explicit matching bounds \(I\).** Write \(m=\lfloor n/2\rfloor\), with residues interpreted modulo \(n\). For each \(s\in\{1,\ldots,m-1\}\), the pair of residues \(-s\) and \(m-s\) is an edge of \(B_0\): its route through zero has length \(s+(m-s)=m\), which is shortest (possibly tied with the opposite route when \(n\) is even). These \(m-1\) edges are pairwise vertex-disjoint. Since \(B_0\) has \(n-1\) vertices, any independent set meets each matched pair at most once, so
\[
|I|\le (n-1)-(m-1)=n-m=\left\lceil\frac n2\right\rceil.
\]
Thus every general-position set containing a core vertex has size at most \(\lceil n/2\rceil+1\) (with the two-vertex exception automatically covered).

**4. Exact attainment and maximality.** The previous bound is attained by the following explicit independent sets of \(B_0\):
\[
I=\begin{cases}
\{1,2,\ldots,m\},&n=2m,\\
\{1,2,\ldots,m\}\cup\{-m\},&n=2m+1.
\end{cases}
\]
For two positive residues on these lists, the short subpath between them avoids zero; in the odd case, every route from \(-m\) to a positive listed residue through zero has length greater than \(m\), hence is not shortest. Thus no two distinct elements of \(I\) are adjacent in \(B_0\), and \(|I|=\lceil n/2\rceil\).

Put \(M_0=\{c_0\}\cup\{\ell_i:i\in I\}\). Since selected leaves cannot be geodesic interior vertices and zero is not between any two chosen leaf indices, \(M_0\) is in general position. It has \(\lceil n/2\rceil+1\) members. To verify inclusion-maximality, adding \(\ell_0\) creates a geodesic triple through \(c_0\), while adding \(c_i\) for \(i\in I\) creates a geodesic triple through \(c_i\) with \(\ell_i\) and \(c_0\). For \(j\notin I\cup\{0\}\), adding either \(c_j\) or \(\ell_j\) would enlarge the independent set \(I\) in \(B_0\) beyond the bound in Step 3; hence it creates a geodesic triple through \(c_0\). Therefore \(M_0\) is maximal.

**5. Unique maximum and the gap.** Because \(\lceil n/2\rceil+1<n\) for \(n\ge4\), all general-position sets containing a core vertex are strictly smaller than \(L\). Therefore \(L\) is the unique maximum set. Step 3 rules out every cardinality strictly between \(\lceil n/2\rceil+1\) and \(n\) among maximal sets; Step 4 attains the lower endpoint. The count of missing integers for \(n\ge6\) is \(n-\lceil n/2\rceil-2=\lfloor n/2\rfloor-2\), as claimed. \(\square\)

## Verification
The standalone \(\texttt{verify.py}\) constructs the sunlets and their distances by breadth-first search, tests triples against the defining distance equality, exhaustively enumerates all subsets for \(3\le n\le9\), and determines maximality by trying every one-vertex extension. It checks uniqueness of the top maximal set and the sharp next-largest size. It also tests the matching lower bound and the constructed witnesses for \(4\le n\le40\). Run with \(\texttt{python3 verify.py}\); the recorded result is in \(\texttt{verification-output.txt}\). These finite checks supplement, but do not replace, the proof for all \(n\).

## Relationship to prior work
Di Stefano, Klavžar, Krishnakumar, Tuite, and Yero introduced systematic study of the smallest maximal general-position sets and established links with universal geodesic lines. Iršič, Klavžar, Rus, and Tuite introduced the general-position polynomial and studied its relation to maximal general-position sets; their graph-product results do not determine the second-largest maximal cardinality for the sunlet family. Ghorbani and coauthors previously determined the general-position number of corona graphs in their Theorem 4.3, covering the already known maximum \(n\) for sunlets. Neither this number nor the leaf construction is claimed as new. That extremal value does not imply the sharp next-largest inclusion-maximal size. Rather subsequently considered general-position polynomial coefficients for the six-sunlet, but the ordinary polynomial counts nonmaximal leaf subsets as well and does not imply the all-\(n\) maximal-cardinality gap. The present result is the sharp *next-to-largest maximal-set size* and the resulting unbounded hole in the maximal-cardinality spectrum, not a result about a zero coefficient of the ordinary polynomial.

## Limitations
No assertion is made that every size at most \(\lceil n/2\rceil+1\) occurs, nor is the number of maximal sets of each allowed size determined. The theorem is specific to a one-leaf corona of a cycle and does not extend automatically to arbitrary corona bases. Computational enumeration is finite and cannot independently establish the statement for arbitrarily large \(n\). The bibliographic search may miss unindexed results or alternate terminology; independent mathematical review is not included.

## References
1. M. Ghorbani and coauthors, *The general position problem on Kneser graphs and on some graph operations*, first posted 11 March 2019, arXiv:1903.04286, https://arxiv.org/abs/1903.04286 ; Section 4.1, Theorem 4.3 (corona general-position number).
2. G. Di Stefano, S. Klavžar, A. Krishnakumar, J. Tuite, I. G. Yero, *Lower General Position Sets in Graphs*, first posted 16 June 2023, arXiv:2306.09965, https://arxiv.org/abs/2306.09965 .
3. V. Iršič, S. Klavžar, G. Rus, J. Tuite, *General Position Polynomials*, Results in Mathematics 79 (2024), article 110, DOI:10.1007/s00025-024-02133-3, https://link.springer.com/article/10.1007/s00025-024-02133-3 .
4. B. A. Rather, *Explicit Formulas and Unimodality Phenomena for General Position Polynomials*, arXiv:2603.06930, https://arxiv.org/abs/2603.06930 ; see the discussion of the six-sunlet in the log-concavity section.
