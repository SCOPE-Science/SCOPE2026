# Connected-forcing polynomials of cycle bouquets: log-concavity and a sharp real-zero boundary

## Finding

For integers \(r\ge2\) and \(\ell_1,\ldots,\ell_r\ge3\), let \(B=B(\ell_1,\ldots,\ell_r)\) be the graph formed from \(r\) vertex-disjoint cycles by identifying one distinguished vertex of every cycle into a single hub \(h\). The other vertices remain distinct; the order is \(N=1+\sum_i(\ell_i-1)\). All vertices are labelled. A *connected forcing set* is a subset inducing a connected subgraph from which the ordinary zero-forcing rule colors every vertex, and the connected-forcing polynomial counts such subsets by size:
\[
 Z_c(B;z)=\sum_{S:\,B[S]\text{ connected and }S\text{ forces }B}z^{|S|}.
\]

Define the petal polynomial
\[
 P_{\ell}(z)=\sum_{s=1}^{\ell-2}(s+1)z^s+z^{\ell-1}.
\]
**Theorem.** Every such bouquet satisfies
\[
\boxed{Z_c(B;z)=z\prod_{i=1}^r P_{\ell_i}(z).}
\]
Its connected forcing number is \(r+1\), exactly \(2^r\) sets attain this minimum, and the number of connected forcing sets of any size is given by the displayed coefficient product. In total there are
\[
\boxed{Z_c(B;1)=\prod_{i=1}^r\binom{\ell_i}{2}.}
\]
All coefficients from degree \(r+1\) to degree \(N\) are strictly positive and log-concave (hence unimodal). There is also an exact real-zero threshold:
\[
\boxed{Z_c(B;z)\text{ has only real zeros}\quad\Longleftrightarrow\quad \ell_i\in\{3,4\}\text{ for every }i.}
\]

## Assumptions and scope

The graphs are finite, undirected, simple and labelled. The connectedness requirement applies to the *initial* blue set, not necessarily to each subsequently forced intermediate set. The hub is a cut vertex because \(r\ge2\). A petal's peripheral path is the path obtained by deleting \(h\) from that cycle; its endpoints are the two neighbours of \(h\) in that petal. Standard zero forcing permits a blue vertex to force its unique white neighbour, with any legal sequence of forces allowed. A polynomial is real-rooted when all its complex zeros are real, counted with multiplicity. Log-concavity is stated for the contiguous nonzero coefficient sequence, excluding leading zero coefficients.

## Proof

**Hub necessity.** Suppose a connected forcing set \(S\) omits \(h\). Because all petals meet only at \(h\), its selected vertices must lie in one peripheral path (or \(S\) is empty, which is not forcing). At least one other petal is wholly white. Initially both neighbours of \(h\) on that white petal are white. Neither can acquire color from a peripheral neighbour, because every vertex of the petal is white; the only possible external force enters through \(h\). Even if \(h\) becomes blue, it has those two white neighbours and cannot force either. The same observation remains true at every forcing step, so \(S\) fails. Thus \(h\in S\).

**Every petal must meet the initial set.** If \(h\in S\) but some peripheral path initially has no selected vertex, its two endpoints remain white by the identical two-neighbour obstruction. Thus each petal contains a nonempty selected set.

**Connectedness forces a prefix/suffix shape.** Once \(h\in S\), every selected peripheral vertex must be connected to \(h\) along its own cycle using selected vertices. On the path \(u_1,\ldots,u_{\ell-1}\), whose ends attach to \(h\), this means the selected vertices form a prefix \(u_1,\ldots,u_a\) and a suffix \(u_{\ell-b},\ldots,u_{\ell-1}\), with nonnegative integers \(a,b\) and \(a+b\le\ell-1\). Indeed, any selected component of the path that meets neither endpoint would be disconnected from \(h\). If both selected runs meet, all peripheral vertices are selected. Hence every connected forcing set belongs to the stated prefix/suffix family.

**Sufficiency.** If the peripheral path is fully selected, there is nothing to force in that petal. Otherwise the nonempty selected prefix/suffix supplies at least one blue peripheral endpoint of a maximal selected run adjacent to the missing (consecutive) interior interval; that vertex has exactly one white neighbour, namely the next vertex in the missing interval, since its other neighbour is blue. It forces that neighbour, and the argument propagates through the entire omitted interval. This propagation uses only degree-two peripheral vertices, so it is unaffected by the number of other petals and never needs the high-degree hub to force. Thus every nonempty prefix/suffix pattern in every petal forces all of \(B\).

**Exact petal count.** A proper peripheral selection of size \(s\), where \(1\le s\le\ell-2\), is determined by the two nonnegative run lengths \(a,b\) summing to \(s\). There are exactly \(s+1\) such pairs, all producing distinct labelled subsets. When \(s=\ell-1\), the entire peripheral path is selected, counted only once even though many pairs of descriptions would coincide. This proves the formula for \(P_{\ell}\), and independence across petals gives \(z\prod_iP_{\ell_i}\). Each petal contributes at least one vertex, yielding minimum \(r+1\), and each has two possible singleton endpoints, giving \(2^r\) optimal sets. Since \(P_\ell(1)=\sum_{s=1}^{\ell-2}(s+1)+1=\binom\ell2\), evaluation at one gives the total.

**Log-concavity.** After removing a factor \(z\), the coefficient sequence of \(P_{\ell}\) is \(2,3,4,\ldots,\ell-1,1\) for \(\ell\ge4\), and \(2,1\) for \(\ell=3\). These sequences have no internal zeros and are log-concave: between linear consecutive terms, \((s+1)^2>s(s+2)\), and at the final turn \((\ell-1)^2\ge(\ell-2)\cdot1\). The convolution of two nonnegative log-concave sequences without internal zeros is log-concave; this is the standard convolution-preservation theorem, with one proof using total positivity of the associated Toeplitz matrices. Iterating over all petals proves that the coefficients of the product, after discarding the leading zeros, are log-concave. Because each petal sequence is strictly positive, every coefficient in the supported interval is positive.

**Sharp real-zero boundary.** For small petals,
\[
P_3(z)=z(z+2),\qquad P_4(z)=z(z+1)(z+2),
\]
so a bouquet entirely of triangles and squares has only real nonpositive roots. Conversely, let \(\ell\ge5\) and set \(Q_\ell(z)=P_\ell(z)/z\), of degree \(d=\ell-2\ge3\). Its first three coefficients are exactly \(a_0=2\), \(a_1=3\), and \(a_2=4\). If all roots of \(Q_\ell\) were real, then as its coefficients are positive all roots would be negative. Newton's inequalities would make the binomial-normalized coefficients log-concave, in particular
\[
\left(\frac{3}{d}\right)^2\ge \frac{2\cdot4}{\binom d2},
\]
which simplifies to \(9(d-1)\ge16d\), impossible for \(d\ge3\). Thus each petal of length at least five contributes a nonreal pair of zeros. The roots of a finite product are the union of the roots of its factors, so real-rootedness of the bouquet polynomial is equivalent to every petal length being three or four.

## Verification

The accompanying standalone file `CODE/bouquet_verify.py` constructs labelled cycle bouquets, independently enumerates all vertex subsets in the tested cases, checks connectivity directly by a graph search, and checks ordinary zero forcing by an iterative closure algorithm. It compares every cardinality coefficient with the factorization from independent petal polynomial convolutions. It additionally checks the predicted minimum and total counts and log-concavity in larger arithmetic cases. A small arithmetic certificate tests the two explicitly factored petal polynomials and the strict Newton obstruction for the first three coefficients of every larger petal. On successful execution it prints `VERIFY_OK` and its finite test totals. Exhaustive checks concern finite graph orders only; the displayed structural and Newton arguments prove the all-parameter statements.

## Relationship to prior work

Mukherjee and Ray, *On the connected zero forcing polynomial of finite trees*, arXiv:2611.10985 (first public 2026-11-07), develop full cardinality enumeration for trees. Cycle bouquets have multiple cycles and are outside that theorem. Newton and Brimkov, *Zero forcing is not unimodal*, arXiv:2611.11352 (first public 2026-11-08), disprove universal unimodality, including for connected forcing; their nonunimodal join construction does not imply log-concavity for bouquets. Brimkov, Davila and Schuerger, *Connected forcing density and related problems*, arXiv:2507.11194 (first public 2025-07-15), introduce cardinality counts and give general extremal coefficients, minimum-set results and tree enumerators, but no all-cardinality polynomial of a shared-hub cycle bouquet. Brimkov and Davila's 2016 work on connected forcing numbers concerns scalar and structural parameters, not this enumerator.

Closely related independently published mathematical records include a complete fort and minimal-fort polynomial for the **same cycle-bouquet graphs** (published-finding corpus, record `47aae2192937`, November 2, 2026). That result describes zero-forcing obstructions via forts; it does not enumerate connected successful initial sets, characterize their hub-selected prefix/suffix shapes, or prove log-concavity and the real-zero boundary. Other records determine connected-forcing polynomials for sunlet and wheel graphs. A sunlet is a cycle with leaves, and a wheel adds all hub-to-rim edges; neither is the cycle bouquet used here. The convolution log-concavity fact and Newton inequalities are classical and are not claimed as new. The claimed advance is the exact bouquet-class characterization and its sharp coefficient and real-zero consequences.

## Limitations

The graph class requires at least two cycles attached at precisely one hub and no additional bridges or edges. The result does not address arbitrary cactus graphs or count forcing chronologies and propagation times. The real-zero conclusion concerns *only* the listed connected-forcing polynomial, not ordinary or total forcing polynomials. The log-concavity proof invokes a standard classical theorem, not a new preservation law. Historical priority remains subject to unindexed or unpublished general cut-vertex enumerations; a complete mathematical independent audit has not been performed.

## References

1. S. Mukherjee and P. Ray, *On the connected zero forcing polynomial of finite trees*, arXiv:2611.10985, first public 2026-11-07, https://arxiv.org/abs/2611.10985.
2. T. Newton and B. Brimkov, *Zero forcing is not unimodal*, arXiv:2611.11352, first public 2026-11-08, https://arxiv.org/abs/2611.11352.
3. B. Brimkov, R. Davila and H. Schuerger, *Connected forcing density and related problems*, arXiv:2507.11194, first public 2025-07-15, https://arxiv.org/html/2507.11194v1.
4. B. Brimkov and R. Davila, *Characterizations of the Connected Forcing Number of a Graph*, arXiv:1604.00740, 2016, https://arxiv.org/abs/1604.00740.
5. O. Johnson and C. Goldschmidt, *Preservation of log-concavity on summation*, ESAIM Probability and Statistics 10 (2006), 206–215, DOI:10.1051/ps:2006008.
6. *All forts and inclusion-minimal forts of bouquets of cycles: exact cardinality polynomials*, published-finding corpus record `47aae2192937` (2026-11-02), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-all-forts-and-inclusion-minimal-forts-of-bouquets-of-cycles-exac--47aae2192937.
7. *Cardinality enumerator of connected forcing sets of sunlet graphs*, published-finding corpus record `a54ae5ebc761` (2026-10-13), https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-cardinality-enumerator-of-connected-forcing-sets-of-sunlet-graph--a54ae5ebc761.
8. *Connected-forcing polynomial of wheel graphs*, published-finding corpus record `b392706736de` (2026-10-13), https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-connected-forcing-polynomial-of-wheel-graphs--b392706736de.
