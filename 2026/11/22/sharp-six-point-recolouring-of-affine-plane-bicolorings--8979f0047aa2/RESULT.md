# Sharp six-point recolouring of affine-plane bicolorings

## Finding

Let \(\mathcal A\) be the line hypergraph of \(\operatorname{AG}(2,4)\), with sixteen points and twenty four-point lines. A *proper named bicoloring* is a map \(c:V(\mathcal A)\to\{0,1\}\) with neither color constant on any line. The known set of 120 bicolorings admits the following more detailed classification.

Each coloring has a unique direction whose four parallel lines are all split \(2+2\). Each of the five directions labels exactly 24 colorings. Any two distinct colorings have Hamming distance \(6\), \(8\), \(10\), or \(16\), with precisely \(2880\), \(1320\), \(2880\), and \(60\) unordered pairs, respectively. Distance eight occurs exactly within one balanced-direction class, except that a coloring and its complement have distance sixteen; distance six and ten occur exactly between different classes.

Define \(G_6\) to join two proper bicolorings when exactly six point colors change simultaneously. Then \(G_6\) is connected, 48-regular, with 120 vertices, 2880 edges, radius and diameter three. Every vertex has distance-sphere cardinalities \((1,48,70,1)\); its unique vertex at graph distance three is the global color complement. The number of common \(G_6\)-neighbors of a distinct pair at Hamming distance \(6,8,10,16\) is respectively \(22,24,14,0\). This gives the complete metric:

\[
 d_{G_6}(c,d)=\begin{cases}
 0,& c=d,\\
 1,& |\{v:c(v)\ne d(v)\}|=6,\\
 2,& |\{v:c(v)\ne d(v)\}|\in\{8,10\},\\
 3,& d=1-c.
 \end{cases}
\]

No two distinct proper bicolorings can be transformed by changing fewer than six points, so six is the sharp batch-flip connectivity threshold. In contrast, the graph \(G_8\) of *exactly eight*-point flips has five components, one for each parallel direction, and each is \(K_{24}\) with twelve disjoint edges removed (the missing edges pair complementary colorings).

## Assumptions and scope

Points are the ordered pairs \((x,y)\in\mathbb F_4^2\) and lines are the fibers \(x=b\), and the sets \(y=mx+b\), for \(m,b\in\mathbb F_4\). In the computational representation \(\mathbb F_4=\mathbb F_2[z]/(z^2+z+1)\), field elements are represented as integers 0 through 3 and one point \((x,y)\) is bit position \(4x+y\). There are five parallel directions. A color complement exchanges the two *named* colors; it is a distinct configuration. A batch flip changes precisely the indicated number of distinct points in one move and must end at a proper bicoloring; intermediate single flips are not required to remain proper.

## Proof

**Previously known static premise.** Glynn (1988, the affine-plane blocking-set calculation in section 4) established exactly 120 blocking point sets in \(\operatorname{AG}(2,4)\), each of size eight, and no other blocking set sizes. Innamorati and Tondini (2013, pp. 194–196) give a direct geometric proof that each such set is an eight-point Möbius–Kantor configuration and its complement is another one. A proper named bicoloring corresponds exactly to one of those 120 blocking sets by taking its color-one class. An exhaustive independent check over all \(2^{16}\) bitstrings is provided below, so the count is also verified without relying solely on that literature.

**Unique balanced direction.** In a proper bicoloring every line contains one, two or three color-one points. With eight color-one points, double counting lines, point-line incidences and collinear color-one pairs yields \(t_1+t_2+t_3=20\), \(t_1+2t_2+3t_3=40\) and \(t_2+3t_3=28\), hence \((t_1,t_2,t_3)=(8,4,8)\). Two 3-secants cannot meet at a color-zero point: the three other lines through that point would need three additional color-one points, giving at least nine. At most three 3-secants pass through any color-one point, since four would require at least nine color-one points. As eight 3-secants carry 24 color-one incidences in total, precisely three pass through every color-one point. Hence each 3-secant meets six of the other seven 3-secants at its three color-one points and is parallel to the remaining one. The eight 3-secants form four parallel pairs in four different directions, because three parallel 3-secants would require nine color-one points. The fifth parallel direction has no 3-secant, and its four lines must each contain two color-one points (their counts sum to eight). No other direction can be balanced. This also proves the same direction is uniquely defined by the coloring itself.

**Constructive parametrization.** Fix a direction \(U\), a two-dimensional subspace of \(\mathbb F_2^4\). Choose \(\mathbb F_2\)-linear coordinates \((s_1,s_2,t_1,t_2)\) on \(\mathbb F_2^4\) such that the affine lines parallel to \(U\) are exactly the sets with \((s_1,s_2)\) fixed. For every nonzero \(\mathbb F_2\)-linear functional \(\ell\) of \((t_1,t_2)\) and each affine function \(h\) of \((s_1,s_2)\), set

\[
 c(s,t)=s_1s_2+\ell(t)+h(s)\pmod 2.
\]

On every line parallel to \(U\), \(c\) takes both values twice. On every other affine line, the quotient coordinate \(s\) runs through all four values, and \(\ell(t)+h(s)\) is affine in \(s\). The quadratic function \(s_1s_2\) plus an affine function has odd parity on its four inputs, hence takes values in a \(1+3\) split rather than becoming constant. Thus all these colorings are proper with unique balanced direction \(U\). There are \(3\cdot8=24\) such maps for each \(U\), making 120 distinct proper colorings over five directions. The previously proved total count, independently confirmed by exhaustive enumeration, shows that these comprise the complete set.

**Distances and reconfiguration.** Within one direction class, two distinct maps in the displayed parametrization differ by a nonconstant affine Boolean function, hence differ on eight points, except global complements, which differ on sixteen points. For distinct directions, the sum of their displayed quadratic functions has nondegenerate quadratic polar form over \(\mathbb F_2\) (this is a check of the ten unordered pairs of the five two-dimensional direction subspaces). Every nondegenerate quadratic Boolean function in four variables has weight six or ten even after adding any affine term. Consequently these and only these cross-direction Hamming distances occur. Complementation is a fixed-point-free involution inside each direction class, and forces exactly half of each other class to be at distance six and half at distance ten, giving 12 six-flip neighbors per other direction and degree 48. The total pair counts follow.

The remaining common-neighbor counts \((22,24,14,0)\) are certified by exhaustive finite tests over the 120 states in the included source files. Thus every Hamming-eight or Hamming-ten pair has a common six-flip neighbor, whereas Hamming-six pairs are adjacent. A complementary pair has no common neighbor and is at Hamming distance sixteen, so it cannot be connected in fewer than three six-point flips. It admits three flips: choose any six-flip neighbor \(e\) of \(c\); then \(e\) is Hamming-ten from \(1-c\) and thus has a two-flip route there. The metric formula and unique antipodes follow. Finally, all Hamming-eight pairs are precisely the noncomplementary pairs within the same direction class, giving the stated five copies of \(K_{24}\) minus a perfect matching.

## Verification

The file `verify.py` enumerates all 65,536 named assignments with explicit field multiplication, independently reconstructs all 120 via the quadratic parametrization, verifies line incidences, the unique direction, all Hamming and common-neighbor counts, and all-source shortest paths. The file `verify.cpp` builds the same affine plane by independently enumerating cosets of five two-dimensional binary subspaces with the opposite point-bit encoding, then checks the complete state census, pairing histogram, full shortest-path profile, and eight-flip component structure. Both scripts were executed successfully from their packaged source files. To repeat, run `python3 verify.py` and compile `verify.cpp` with a C++17 compiler then execute the resulting binary. The successful outputs are also recorded in `CHECKS.txt`. Enumeration is exhaustive because every binary assignment is scanned and every possible pair of accepted assignments is inspected; no sampling or unproved extension to larger planes is used.

## Relationship to prior work

The static count of 120 and the Möbius–Kantor structure are credited explicitly to Glynn (1988) and Innamorati–Tondini (2013); neither is a novelty claim. The new statement is the complete six-flip and eight-flip reconfiguration geometry and metric on these 120 objects. The relevant complete 2013 paper was inspected, especially its theorem, proof and conclusion, and does not classify flips, pairwise intersections or the associated graphs. Glynn's relevant section counts blocking sets rather than their exchange distances. A related classification of 168 hyperovals in the different plane \(\operatorname{PG}(2,4)\) concerns six-point arcs and cannot directly imply a classification of 120 eight-point affine blocking sets; the published summary was compared, but its complete artifact was inaccessible. Searches found no direct statement of the reconfiguration metric. Absence from searched sources is not a proof of priority.

## Limitations

This is a complete theorem about the unique affine plane of order four only; it does not assert an analogous result for higher-order affine planes or all symmetric designs. The exact common-neighbor counts use an explicitly reproducible finite verification of 120 states; no closed symbolic formula for other orders is claimed. The published 1988 census and 2013 geometric characterization are prior knowledge. Some unindexed literature or unavailable results may contain equivalent intersection information. No independent external audit has been performed.

## References

- D. G. Glynn, *Rings of Geometries II*, Journal of Combinatorial Theory, Series A **49** (1988), 26–66; DOI: 10.1016/0097-3165(88)90027-1. Relevant affine-plane blocking-set census on pp. 58–59.
- S. Innamorati and D. Tondini, *The Yin–Yang Structure of the Affine Plane of Order Four*, Ars Combinatoria **110** (2013), 193–197; https://combinatorialpress.com/article/ars/Volume%20110/volume-110-paper-19.pdf. First verified article publication date: 2013-07-31.
