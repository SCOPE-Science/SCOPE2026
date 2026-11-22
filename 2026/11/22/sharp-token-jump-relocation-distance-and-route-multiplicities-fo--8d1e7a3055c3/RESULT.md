# Sharp token-jump relocation distance and route multiplicities for three-row grid separators

## Finding
Let \(L\ge0\). Attach source \(s\) to all three vertices in the leftmost column of the rectangular grid \(P_3\square P_{L+1}\), and attach sink \(t\) to all three vertices in its rightmost column. The terminal vertices \(s,t\) are distinct, not adjacent, and cannot be removed. A feasible configuration is a minimum-cardinality vertex set separating \(s\) from \(t\). A *token jump* replaces exactly one selected grid vertex by any other unselected grid vertex, provided the resulting set is still a minimum separator.

Every minimum separator has size three and has a unique coordinate representation \((a,b,c)\in\{0,\ldots,L\}^3\) satisfying
\[
|a-b|\le1,\qquad |b-c|\le1.
\]
The coordinates give the selected column in each row, from top to bottom. Consequently the jump graph has one vertex if \(L=0\), and exactly \(9L-1\) vertices and \(23L-11\) undirected edges if \(L\ge1\).

Let \(A_L=(0,0,0)\) and \(B_L=(L,L,L)\) denote the leftmost and rightmost minimum cuts. Their exact minimum number \(d_L\) of token jumps and number \(N_L\) of distinct *shortest* reconfiguration sequences are
\[
d_L=\begin{cases}0,&L=0,\\\lceil3L/2\rceil+1,&L\ge1,\end{cases}
\qquad
N_L=\begin{cases}
1,&L=0,\\
6,&L=1,\\
2^{L/2},&L\ge2\text{ even},\\
2^{(L+3)/2},&L\ge3\text{ odd}.
\end{cases}
\]
A sequence is distinguished by its successive separator states, and no token identities beyond their distinct rows are assumed.

## Assumptions and scope
The grid is the simple, undirected Cartesian product with exactly three rows and \(L+1\) columns. Grid edges join horizontal or vertical nearest neighbors. Terminals are attached only to the designated boundary-column grid vertices; there are no other edges incident with them. A separator never contains \(s\) or \(t\). The token-jumping rule allows a token to change its column within its existing row without the requirement that it follow a grid edge. All intermediate states must remain minimum separators. This theorem concerns the two specified extreme cuts, not a closed formula for every pair in the jump graph.

## Proof
**Separator representation.** There are three internally vertex-disjoint \(s\)-to-\(t\) paths, one along each row, so any separator has at least three grid vertices. Selecting an entire column disconnects the terminals, so minimum size is three. Every minimum separator contains exactly one selected vertex in each row, hence is a triple \((a,b,c)\). If, for example, \(b\ge a+2\), a route can start in the middle row, travel right until column \(a+1\), climb into the top row, and continue to \(t\), avoiding the top and middle selected vertices; this route never enters the third row. Similar routes exclude all adjacent-row column differences greater than one. Conversely, for a triple satisfying both inequalities, the integer potential \(\phi(i,j)=j-x_i\), where \(x_0=a,x_1=b,x_2=c\), changes by at most one along each grid edge. Any surviving route from \(s\) to \(t\) would pass from negative to positive potential, and would therefore hit a zero-potential grid vertex, which is selected. Thus the inequalities characterize exactly the minimum separators.

**State and edge counts.** For \(L\ge1\), there are four triples at each boundary middle coordinate \(b=0,L\), and nine for every interior \(b\), yielding \(8+9(L-1)=9L-1\). Every legal jump changes one coordinate. When the middle coordinate is fixed, outer-coordinate jumps contribute \(8+18(L-1)=18L-10\) unordered edges. For a fixed outer pair, there are respectively three, two, or one available middle coordinates when their difference has absolute value zero (interior), one, or two; boundary coincidences have only two. The number of edges changing the middle coordinate is \(3(L-1)+2+2L=5L-1\). Their sum is \(23L-11\).

**Jump lengths and a lower bound.** In a valid state, the top or bottom coordinate lies within one of the middle coordinate. A forward jump of length two at an outer coordinate is therefore possible only from \(b-1\) to \(b+1\); a forward jump of length two at the middle is possible only from \(b=a-1=c-1\) to \(b+2\). All single-coordinate jumps, including any backwards ones, have absolute length at most two. The first move from \((0,0,0)\) can advance a coordinate by at most one. By reversing the columns, the last move to \((L,L,L)\) also advances a coordinate by at most one. If a path contains \(M\ge2\) moves, its total coordinate-sum increase \(3L\) is therefore at most \(2M-2\), so \(M\ge\lceil3L/2\rceil+1\) for \(L\ge1\). For \(L=1\), all six orders of moving the three row tokens are legal and shortest. For \(L=0\), there is just the empty route.

**Sharpness and complete optimal-route classification.** Put \(L=2h\ge2\). At the lower-bound length \(3h+1\), the first and last moves must be unit moves and every intervening move must be a forward double jump. Since double jumps do not change coordinate parity and each final coordinate is even, the two unit moves must affect the same coordinate. The first must be at the middle: moving an outer coordinate by one from the origin allows no double jump next. By reversal, the last is also at the middle. Starting with \((0,1,0)\), jump each outer coordinate from zero to two, in either order, then jump the middle coordinate from one to three. Repeating these alternations leaves both outers at \(2h\) and the middle at \(2h-1\), after which a final middle unit jump completes the route. There are exactly \(h\) independently ordered pairs of outer double jumps, giving \(2^h\) shortest sequences.

Now put \(L=2h+1\ge3\). At the lower-bound length \(3h+3\), there must be precisely three forward unit moves; every other move is a forward double jump. Since the endpoint has odd coordinates, each coordinate makes exactly one unit move. If the first move is at an outer coordinate, a double jump cannot occur until the other outer coordinate also makes its unit move. Indeed, making the middle unit move first leads either to the all-equal state (with no double jump available), or after a double jump of the remaining outer to a configuration where no further double jump is available, while the outstanding single unit move cannot unlock it. From \((1,0,1)\), the middle jumps to two, the two outer coordinates jump to three in either order, the middle jumps to four, and so forth, ending with a single middle unit move. This yields \(2\cdot2^h\) shortest sequences.

If the first move is at the middle, the two outer unit moves cannot be spent before the final stage: using either one earlier blocks the necessary chain of double jumps. Starting from \((0,1,0)\), pairs of outer double jumps alternate with middle double jumps, eventually leaving the middle at \(2h+1\) and the two outers at \(2h\); the two final outer unit moves may be ordered either way. This yields another \(2\cdot2^h\) sequences. The local double-jump eligibility stated above shows these two patterns exhaust the possibilities, because before each middle double jump both outer coordinates must be one above the middle and before each outer double jump that coordinate must be one below the middle. Hence \(N_L=2^{h+2}\) for odd \(L\ge3\). The exhibited routes attain the lower bound in every case.

## Verification
Two standalone Python 3 programs accompany this result. `verify_grid.py` constructs the *original augmented grid*, exhaustively tests every three-vertex candidate using an actual terminal-connectivity search, builds all legal token-jump moves by one-vertex set exchange, and counts shortest paths by breadth-first search for \(1\le L\le6\). `verify_triples.py` independently generates the triple-inequality state graph and checks the state count, edge count, extreme distance and number of shortest sequences for \(0\le L\le30\). Both completed with assertions passing. Their actual command output is included in `CHECKS.txt`. Finite checks supplement the preceding all-\(L\) proof; they do not replace it.

## Relationship to prior work
Gomes et al. study reconfiguration of minimum vertex separators and prove that shortest sequences of token slides can be found in polynomial time, while shortest token-jump optimization is NP-complete in general [1]. In the present three-row, boundary-attached grid, the structural characterization allows an explicit formula and complete optimal-route count for extreme cuts; no assertion of a general jump algorithm is made. OEIS A227665 [2] already counts unit-coordinate lattice walks confined to the same Lipschitz triple region. Those are *slide* routes: for instance, at \(L=2\), it counts 44 monotone unit-step routes, while the present token-jump problem has exactly two shortest routes of four moves. The known lattice-walk enumeration is therefore not represented as new, nor is it used to infer the jump result.

## Limitations
The exact jump-distance formula and route multiplicities here apply to the pair of extreme separators, not arbitrary endpoints or arbitrary grid heights. The number of shortest routes is a count of distinct separator-state sequences, not the number of optimal algorithms. The general minimum-separator jump problem remains computationally difficult. The originality assessment is based on inspected primary literature and database comparisons; an unindexed older equivalent is a residual possibility. Independent mathematical validation has not been performed.

## References
[1] G. C. M. Gomes, C. Legrand-Duchesne, R. Mahmoud, A. E. Mouawad, Y. Okamoto, V. F. dos Santos, T. C. van der Zanden, *Minimum Separator Reconfiguration*, arXiv:2307.07782, publicly posted 15 July 2023, https://arxiv.org/abs/2307.07782. Journal of Computer and System Sciences 146 (2024), article 103574.

[2] A. P. Heinz, OEIS A227665, *Number of lattice paths from \((n,n,n)\) to \((0,0,0)\)* with neighboring-coordinate differences at most one, 19 July 2013, https://oeis.org/A227665.
