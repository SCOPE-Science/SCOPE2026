# Seven vertices are sharp for transmissibility-dependent epidemic-source ranking reversals on trees

## Finding

**Theorem (sharp order and complete minimal classification).** Let \(T\) be a finite, connected, simple, undirected tree. For \(0<p<1\), independently transmit along each edge with common probability \(p\), starting at one prescribed infectious vertex \(v\), and allow further transmission along any subsequently reached edges. Write \(M_v(p)\) for the mean final number of infected vertices, *including* the initial case.

For every tree \(T\) with at most six vertices, no two prescribed source vertices have a **strict expected-outbreak-size ranking reversal** as \(p\) varies in \((0,1)\). That is, for any distinct \(u,v\), the sign of \(M_u(p)-M_v(p)\) cannot take both positive and negative values in this interval. At seven vertices such reversals occur, and **exactly two** isomorphism classes of pairs \((T,\{u,v\})\) exhibit one. In both classes the sources are adjacent, the difference has exactly one interior zero, and representatives are as follows.

1. **Two three-valent hubs with one intervening vertex.** On vertices \(0,1,2,3,4,5,6\), take edges \(\{01,03,04,12,25,26\}\) and compare sources \(u=0,v=1\). Then
   \[
   M_0(p)=1+3p+p^2+2p^3,\quad M_1(p)=1+2p+4p^2,\quad
   M_0(p)-M_1(p)=p(1-p)(1-2p).
   \]
   The ranking reverses at \(p=1/2\).
2. **One three-valent hub and an arm of length four.** Take edges \(\{01,04,05,12,23,36\}\), compare sources \(u=0,v=1\), and obtain
   \[
   M_0(p)=1+3p+p^2+p^3+p^4,\quad M_1(p)=1+2p+3p^2+p^3,\quad
   M_0(p)-M_1(p)=p(1-p)(1-p-p^2).
   \]
   The unique reversal is at \(p=(\sqrt5-1)/2\).

Both source pairs prefer the higher-degree endpoint at sufficiently low transmissibility and the other endpoint at sufficiently high transmissibility. These are *pairwise rankings*: no claim is made that either seed maximizes mean outbreak size among all vertices of the tree.

## Assumptions and scope

Every edge independently permits a single undirected transmission, with the same parameter \(p\). Equivalently, independently retain each edge with probability \(p\) and infect the open connected component of the initial source. The count \(M_v\) includes the seed; excluding it changes all mean scores by the same constant and does not affect rankings. Each source's infection is independently counterfactually evaluated on the same fixed tree. The theorem applies to a single-source final-size model, not to time-resolved infection peaks, Markovian recovery times, directed contacts, heterogeneous edges, general graphs with cycles, or an optimal-vaccination problem.

A reversal is defined by the existence of \(0<p_1<p_2<1\) for which \((M_u(p_1)-M_v(p_1))(M_u(p_2)-M_v(p_2))<0\). An isolated tie without a sign change is not counted. Pairs are unordered, and two marked pairs are equivalent when a graph isomorphism sends one unordered source pair to the other.

## Proof

**1. Distance identity.** Let \(d_T(u,w)\) be the number of edges on the unique path between vertices \(u,w\). The probability that \(w\) is infected from \(u\) is exactly \(p^{d_T(u,w)}\), because every edge of that unique path must transmit. Linearity of expectation gives
\[
 M_u(p)=\sum_{w\in V(T)}p^{d_T(u,w)}=1+\sum_{j=1}^{n-1}a_u(j)p^j,
\]
where \(a_u(j)\) counts vertices at graph distance \(j\) from \(u\), and \(n=|V(T)|\). This is the familiar tree distance-profile formula for expected reachable population; it is not claimed as new.

**2. Polynomial reduction.** For distinct \(u,v\) put \(d_j=a_u(j)-a_v(j)\) and \(D_{uv}(p)=\sum_{j=1}^{n-1}d_jp^j\). As \(\sum_ja_u(j)=\sum_ja_v(j)=n-1\), one has \(D_{uv}(0)=D_{uv}(1)=0\). Hence
\[
 D_{uv}(p)=p(1-p)Q_{uv}(p),\qquad
 Q_{uv}(p)=\sum_{k=0}^{n-2}\left(\sum_{j=1}^{k+1}d_j\right)p^k.
\]
The displayed final coefficient is zero; \(Q_{uv}\) has degree at most \(n-3\). Since \(p(1-p)>0\) in the open unit interval, strict ranking reversals are exactly the odd-multiplicity interior roots of \(Q_{uv}\).

**3. Complete classification up to order seven.** The supplied standalone program `checker.py` enumerates all labelled trees on \(n\) vertices for each \(2\le n\le7\) using Prüfer sequences, a bijection with sequences of length \(n-2\) in \(\{0,\ldots,n-1\}\). It obtains respectively \(1,1,2,3,6,11\) tree isomorphism classes. It deduplicates via the lexicographically least recursively encoded rooted-tree string over every possible root, an exact canonical invariant for unlabelled trees. For each isomorphism representative it processes every unordered pair of distinct vertices, obtains all distances by graph search, and forms the *exact integer* coefficients of \(Q_{uv}\).

The program counts roots of \(Q_{uv}\) in \((0,1)\) using rational polynomial division, square-free reduction and a Sturm sequence. At endpoints that are roots, it takes one-sided signs by the first nonzero derivative, making the count strictly interior. This root-counting certificate is stronger than sample-point testing: it decides *every real interior zero*, not merely zeros on a grid. Up to six vertices no pair has even an interior root. At seven vertices exactly three pairs among the eleven chosen tree representatives have an interior root, each simple, and each is adjacent. Of those three, two are related by a tree automorphism in the symmetric two-hub tree. The program identifies the two marked-edge isomorphism classes by deleting the marked edge and canonically encoding the two resulting rooted components, unordered. Thus there are exactly two tree-and-unordered-source-pair isomorphism classes.

These finite claims are exhausted by the Prüfer bijection: the seven-vertex level examines all \(7^5=16807\) labelled trees and reduces them to all eleven unlabelled trees. Exact arithmetic and the explicit algorithm are necessary parts of the complete finite proof. The argument asserts no analogous census beyond seven vertices.

**4. Witness evaluation.** On the two-hub tree, the distance-layer profiles of sources \(0\) and \(1\) are \((3,1,2)\) and \((2,4,0)\). On the one-hub four-arm tree they are \((3,1,1,1)\) and \((2,3,1,0)\). Substitution into the distance identity gives the polynomials stated in the theorem. Their nontrivial factors are strictly decreasing on \((0,1)\) and vanish exactly at \(1/2\) and \((\sqrt5-1)/2\), respectively. This establishes existence and the claimed sign directions independently of the census.

## Verification

Run `python3 checker.py` in a directory containing the embedded program. It requires Python 3 standard-library modules only. A successful execution prints `EXACT_CHECK_PASS`, the labelled and unlabelled tree counts for orders two to seven, the three reversing representative pairs, and the two marked-pair classes. For each reversing witness it independently enumerates every one of the \(2^6=64\) edge-retention patterns at \(p=1/4\) and \(p=3/4\), confirming that the exact outbreak-size differences agree with the distance-polynomial computation and have opposite signs. A separate independent check using NetworkX nonisomorphic-tree generation and SymPy exact real-root isolation returned reversal counts \(0,0,0,0,0,3\) for sizes two through seven.

The finite computer-aided proof depends on the correctness of the short provided standard-library implementation, the classical Prüfer enumeration theorem, tree canonicalization, and Sturm's theorem. It is not a proof about all larger trees and does not require numerical floating-point thresholds for correctness.

## Relationship to prior work

Eisenstat, Gordon and Redlich (2008) develop the expected reachable-vertex polynomial and its tree-distance representation, with graph-theoretic reconstruction results. More directly, Gordon and Jager (published online 18 December 2009) explicitly prove that **any integer polynomial vanishing at zero and one** can be realized as the difference of expected reachable counts for adjacent vertices of *some* tree (their Lemma 2.4), and thus arbitrary finite numbers of crossovers are possible (their Proposition 2.5). Their general construction subsumes the qualitative **existence** of a ranking reversal. Accordingly, neither existence nor arbitrary-crossing freedom is a new claim here. The isolated contribution is the **minimum vertex order for one reversal** and the **complete marked-pair classification at that order**; the cited arbitrary-order existence construction supplies neither a six-vertex obstruction nor this two-class census.

Moore and Newman (2000) relate independent bond percolation to epidemic transmissibility; Bucur and Holme (2020) compare exact epidemic source importance and graph centralities but study a different dynamical model and do not supply the present sharp classification. The 2002 article by Aivaliotis, Gordon and Graveman on tree expected-rank polynomials is an additional plausible historical-priority source for which full text was not accessible in this review. Priority therefore remains provisional and requires further human examination of that paper and other specialized literature.

## Limitations

The result holds only for finite unweighted undirected trees with homogeneous independent bond transmission and exactly one source. Pairwise reversal is not the same as a change in the globally best source. It does not assert the smallest connected *cyclic* graph with the property, multiple reversals, or extensions to stochastic infection times. The finite classification was checked algorithmically with exact arithmetic and a second root-isolation implementation, but has not undergone independent scientific audit. Unavailable older full text creates residual originality risk.

## References

- D. Eisenstat, G. Gordon and A. Redlich, *Combinatorial Properties of a Rooted Graph Polynomial*, SIAM Journal on Discrete Mathematics **22** (2008), 776–785. Published online 18 April 2008. https://doi.org/10.1137/06065951X ; lawful open copy: https://www.davideisenstat.com/cv/EisenstatGR08.pdf
- G. Gordon and E. Jager, *Distinguished Vertices in Probabilistic Rooted Graphs*, Networks **55** (2010), 237–247. First online 18 December 2009. https://doi.org/10.1002/net.20363 ; author's open copy: https://webbox.lafayette.edu/~gordong/pubs/GordonJaeger.pdf
- C. Moore and M. E. J. Newman, *Exact Solution of Site and Bond Percolation on Small-world Networks*, Physical Review E **62** (2000), 7059–7064. https://doi.org/10.1103/PhysRevE.62.7059
- D. Bucur and P. Holme, *Beyond ranking nodes: Predicting epidemic outbreak sizes by network centralities*, PLoS Computational Biology **16** (2020), e1008052. https://doi.org/10.1371/journal.pcbi.1008052
- M. Aivaliotis, G. Gordon and W. Graveman, *When bad things happen to good trees*, Journal of Graph Theory (2002). https://doi.org/10.1002/jgt.1004
