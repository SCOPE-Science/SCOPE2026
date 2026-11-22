# Exact average-flow spectral separation of the Shrikhande and four-by-four rook graphs

## Finding

The two nonisomorphic strongly regular graphs with parameters \(16,6,2,2\) have **different average-flow spectra**, although their adjacency spectra and distance spectra agree. For the four-by-four rook graph \(R\) and the Shrikhande graph \(S\), the common vertex average flows are exactly

\[
 c_R=\frac{29551748}{2331947},\qquad
 c_S=\frac{29620706}{2338221},\qquad
 c_R-c_S=\frac{24601265726}{5452607446287}>0.
\]

In the definition of Waheed and Azam, the average-flow matrix \(F(G)\) has diagonal entries \(\operatorname{fl}_G(v)\), the average length of all nonempty simple paths beginning at \(v\), and off-diagonal entries equal to minus the ordinary graph distances. Both graphs have distance spectrum \(\{24,(-4)^{[6]},0^{[9]}\}\). Therefore their average-flow spectra are respectively

\[
 \operatorname{spec}F(R)=\{(c_R-24)^{[1]},(c_R+4)^{[6]},c_R^{[9]}\},
 \quad
 \operatorname{spec}F(S)=\{(c_S-24)^{[1]},(c_S+4)^{[6]},c_S^{[9]}\}.
\]

The first difference between the rooted simple-path counts occurs at length seven: \(34452\) versus \(34320\). The exact total numbers of nonempty paths from a fixed root are \(13991682\) and \(14029326\), and their total lengths are \(177310488\) and \(177724236\), respectively.

## Assumptions and scope

Both graphs are finite, simple, undirected, connected, and have vertex set \(\mathbb{Z}_4^2\). In \(R\), distinct vertices are adjacent precisely when their first or second coordinates agree. In \(S\), vertices are adjacent precisely when their difference is one of \(\pm(1,0),\pm(0,1),\pm(1,1)\), with all coordinates modulo four. Every path is an ordered sequence of pairwise distinct vertices; its length is the number of edges. For each \(v\), let \(p_k(v)\) be the number of such paths of exactly \(k\) edges starting at \(v\). The average flow is

\[
\operatorname{fl}_G(v)=
\frac{\sum_{k=1}^{15} k p_k(v)}{\sum_{k=1}^{15} p_k(v)}.
\]

The claim concerns exactly these two graphs, the two known isomorphism types with parameters \(16,6,2,2\); no statement is made about every pair of distance-cospectral graphs.

## Proof

**1. Graph identities.** Each coordinate translation acts as an automorphism of each of \(R\) and \(S\); hence both graphs are vertex-transitive. The neighbor set at the origin induces two disjoint triangles in \(R\) and a six-cycle in \(S\). Thus they are nonisomorphic. Directly from the displayed edge rules, every vertex has six neighbors and every two distinct vertices have exactly two common neighbors. Both graphs are therefore strongly regular with parameters \(16,6,2,2\).

If \(A\) denotes either adjacency matrix, the common-neighbor conditions yield \(A^2=4I+2J\). Consequently the adjacency eigenvalues are \(6\) (multiplicity one), \(2\) (six), and \(-2\) (nine), where multiplicities follow from dimension and \(\operatorname{tr}A=0\). Every nonadjacent pair has distance two, so the distance matrix is \(D=2(J-I)-A\). Its eigenvalues are \(24\) once, \(-4\) six times, and \(0\) nine times, for both graphs.

**2. Exact simple-path census.** By vertex transitivity, \(p_k(v)\) is independent of \(v\). The following table lists all nonempty simple paths starting at the origin, classified by length:

| Path length | Rook graph | Shrikhande graph |
|---:|---:|---:|
| 1 | 6 | 6 |
| 2 | 30 | 30 |
| 3 | 138 | 138 |
| 4 | 612 | 612 |
| 5 | 2556 | 2556 |
| 6 | 9792 | 9792 |
| 7 | 34452 | 34320 |
| 8 | 110016 | 109680 |
| 9 | 313344 | 314064 |
| 10 | 779904 | 785424 |
| 11 | 1648656 | 1661712 |
| 12 | 2828880 | 2844336 |
| 13 | 3672000 | 3682176 |
| 14 | 3191616 | 3195072 |
| 15 | 1399680 | 1389408 |

These integers follow from a finite, exhaustive dynamic program. For each graph and root zero, let \(h(U,w)\) be the number of paths from zero that visit exactly the vertex subset \(U\), ending at \(w\). Initialize \(h(\{0\},0)=1\). For each neighbor \(z\) of \(w\) outside \(U\), add \(h(U,w)\) to \(h(U\cup\{z\},z)\). This defines a finite acyclic recurrence on subsets; induction on their cardinalities proves that every simple path is counted once and only once. Sum the states with \(|U|=k+1\) to obtain \(p_k(0)\). The accompanying standalone integer-arithmetic implementation implements the complete recurrence; a second implementation independently enumerates every such path by direct backtracking. They agree with every total and verify all edge rules and strong-regularity parameters.

**3. Flow and spectral separation.** Summing the table gives

\[
\begin{aligned}
\sum_k p_k^R&=13991682,& \sum_k k p_k^R&=177310488,\\
\sum_k p_k^S&=14029326,& \sum_k k p_k^S&=177724236.
\end{aligned}
\]

Reducing these integer ratios gives the displayed values of \(c_R\) and \(c_S\). Since both graphs are vertex-transitive, their average-flow matrices are \(F(R)=c_R I-D(R)\) and \(F(S)=c_S I-D(S)\). The distance-spectrum computation gives the claimed exact spectra. In particular their traces are \(16c_R\) and \(16c_S\), which are unequal because the displayed positive rational difference is nonzero. This proves spectral separation.

## Verification

Run `python3 verify.py` to evaluate the complete subset recurrence using exact Python integers and fractions, and `c++ -O2 -std=c++17 verify.cpp -o verifier && ./verifier` for the independent exhaustive depth-first traversal. The output checks all fifteen path-count coefficients, two totals, weighted totals, graph local structures, and the exact rational difference. These finite computations are exhaustive for the two explicitly defined 16-vertex graphs; no asymptotic extrapolation is involved. The supporting source files are part of this result.

## Relationship to prior work

Waheed and Azam introduced the average-flow matrix and proved that it is a scalar shift of the negative distance matrix for any flow-stable graph. They proved that vertex-transitive graphs are flow-stable, enumerated connected graphs through order ten, and expressly suggested studying highly symmetric and distance-regular graphs. Their paper does not calculate the average flow of the two strongly regular graphs on sixteen vertices. The shift identity used here is theirs, not new.

Graziani, Drucks, Bianchini, Scarselli and Gärtner studied path-based graph discrimination and explicitly observed that path multisets of length up to seven distinguish the rook and Shrikhande graphs. Therefore neither the use of this graph pair nor the existence of a seven-step path distinction is claimed as new. The additional claim here is that the **particular all-length weighted average used in the new average-flow matrix does not cancel the discrepancies**, with the complete exact rooted-path data and resulting rational spectral shift.

Cameron's account of Shrikhande's classification establishes that these are the only two isomorphism types with parameters \(16,6,2,2\). That classification is background, not new.

## Limitations

This is an exact result for a canonical finite strongly regular pair, not a classification of arbitrary strongly regular parameters, an all-orders claim, or evidence that the average-flow spectrum determines every connected graph. Historical priority of the specific all-length weighted average comparison has been checked against the listed sources but cannot be guaranteed against unindexed literature.

## References

1. U. Waheed and N. A. Azam, *Enumeration of Cospectral Graphs with Respect to the Average Flow Matrix*, arXiv:2611.18344v1, first public 2026-11-13, https://arxiv.org/html/2611.18344v1.
2. C. Graziani, T. Drucks, M. Bianchini, F. Scarselli and T. Gärtner, *No PAIN no Gain: More Expressive GNNs with Paths*, NeurIPS Graph Learning workshop (2023), https://repositum.tuwien.at/bitstream/20.500.12708/193616/1/2023-No%20PAIN%20no%20Gain%20More%20Expressive%20GNNs%20with%20Paths-vor.pdf.
3. P. J. Cameron, *Strongly regular graphs*, draft April 2001, Section 4, https://maths.qmul.ac.uk/~lsoicher/designtheory.org/library/preprints/srg.pdf.
