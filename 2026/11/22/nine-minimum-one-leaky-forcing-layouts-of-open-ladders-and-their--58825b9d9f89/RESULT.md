# Nine minimum one-leaky forcing layouts of open ladders and their exchange–slide gap

## Finding
For every integer \(n\ge5\), the labelled open ladder \(L_n=P_n\square K_2\) has one-leaky zero-forcing number \(Z_{(1)}(L_n)=4\) and **exactly nine** minimum one-leaky forcing sets. Among these optima the unrestricted single-token exchange graph is \(P_3\square P_3\), whereas the adjacency-restricted token-slide graph is \(9K_1\). Consequently a fixed four-vertex placement budget admits global relocation by successive replacements but forbids even one locally adjacent relocation.

## Assumptions and scope
The simple graph has vertices \(t_i,b_i\), \(1\le i\le n\), with edges \(t_it_{i+1}\), \(b_ib_{i+1}\), and \(t_ib_i\) for valid indices. Starting from an initial blue set \(B\), a blue vertex can turn its only white neighbor blue. A *leak* is a graph vertex that is never allowed to perform a force, whether blue initially or colored later. One-leaky forcing means completion is possible for **every choice of one leak**.

Define the three left end pairs
\[
A_T=\{t_1,t_2\},\qquad A_B=\{b_1,b_2\},\qquad A_V=\{t_1,b_1\},
\]
and the corresponding right end pairs
\[
D_T=\{t_{n-1},t_n\},\qquad D_B=\{b_{n-1},b_n\},\qquad D_V=\{t_n,b_n\}.
\]
The nine minimum sets are precisely \(A_i\cup D_j\) for \(i,j\in\{T,B,V\}\). A token exchange replaces exactly one selected vertex with exactly one unselected vertex and must finish in another minimum one-leaky forcing set. A token slide is an exchange for which the removed and added vertices are adjacent in the original ladder; there is no requirement to consider nonoptimal intermediate sets.

## Proof
**1. Two seeds are required at each end.** Let the left two-column window be \(C_L=\{t_1,b_1,t_2,b_2\}\). Suppose \(B\) includes at most one of these four vertices. Because adding initial blue vertices cannot make forcing harder, it suffices to color every vertex outside \(C_L\) blue and show a surviving white obstruction with a suitable leak. For each possible selected singleton (or no singleton), take the following leak and nonempty white trap:

| Initially blue in \(C_L\) | Leaked vertex | White trap \(W\) |
|---|---|---|
| none | \(t_3\) | \(\{t_1,t_2,b_1\}\) |
| \(\{t_1\}\) | \(t_3\) | \(\{t_2,b_1\}\) |
| \(\{b_1\}\) | \(b_3\) | \(\{t_1,b_2\}\) |
| \(\{t_2\}\) | \(b_3\) | \(\{t_1,b_1,b_2\}\) |
| \(\{b_2\}\) | \(t_3\) | \(\{t_1,t_2,b_1\}\) |

In every row, each nonleaked vertex outside \(W\) has either zero or at least two neighbors in \(W\). Thus no permitted forcing step enters \(W\), irrespective of what other vertices become blue. The symmetric right window \(C_R=\{t_{n-1},b_{n-1},t_n,b_n\}\) also needs two initially blue vertices. For \(n\ge5\) the windows are disjoint, hence every one-leaky set has size at least four.

**2. Exactly three pairs survive at either end of an optimum.** A four-vertex optimum must contain exactly two vertices in each window and none elsewhere. The diagonal choice \(\{t_1,b_2\}\) is impossible: with leak \(t_3\) the white trap \(\{t_2,b_1\}\) persists even if all vertices outside it start blue. The other diagonal \(\{b_1,t_2\}\) is excluded by the symmetric trap \(\{t_1,b_2\}\) and leak \(b_3\). The remaining left pairs are \(A_T,A_B,A_V\) and the inner rung \(\{t_2,b_2\}\); there are analogous right pairs.

The left inner rung cannot occur. If both ends use their inner rungs, all four initially blue vertices have two white horizontal neighbors and no force is possible. If the right pair is \(D_T\), declare \(b_n\) leaked. The right top pair can only color \(b_n\), whose leak prevents further movement, and the left inner rung cannot start. For right pair \(D_B\), use the symmetric leak \(t_n\). With right pair \(D_V\), declare \(t_n\) leaked: at most \(b_{n-1}\) can be colored from \(b_n\), after which no further force is possible. These cases exhaust right choices. Symmetry excludes the right inner rung. Thus every four-vertex one-leaky set, if any, belongs to the nine specified pairs.

**3. All nine sets are one-leaky.** Each of \(A_T,A_B,A_V\) is an ordinary zero-forcing set: for \(A_V\), both rails start propagating to the right; for \(A_T\), first force \(t_1\to b_1\), then propagate from the two-vertex starting strip, and use reflection for \(A_B\). Hence the union \(A_i\cup D_j\) supports an ordinary left-to-right forcing process and a right-to-left forcing process. Extra initially blue vertices never invalidate a process once forces into already-blue targets are skipped. For every target outside the union, its possible left-to-right forcer and possible right-to-left forcer are different: in interior columns they are the two horizontal neighbors; in the first or last two columns one is the local rung or nearer-end predecessor and the other is the farther-end horizontal neighbor. By the two-distinct-possible-forcers criterion of Alameda, Kritschgau, Warnberg and Young (2020, Theorem 2.3), each union is one-leaky. Therefore precisely nine minimum sets exist.

**4. Reconfiguration graphs.** The three allowed choices on one end form a path under one-token replacement: \(A_T\) and \(A_B\) each differ from \(A_V\) in one selected vertex, but differ from one another in two selected vertices. The same holds at the right end. The disjoint-end product structure gives exactly \(P_3\square P_3\), with \(3\cdot2+3\cdot2=12\) edges. Every one-token replacement between these end pairs moves a token between opposite corners of an end square, which are diagonally separated, never adjacent in \(L_n\); hence the token-slide graph is \(9K_1\). This completes the all-order proof.

## Verification
The standalone file `verify.cpp` constructs \(P_n\square K_2\) from its adjacency lists, tests every possible single leaked vertex, and exhaustively examines all initial subsets of sizes up to four for \(2\le n\le16\). For each \(5\le n\le16\), it finds forcing number four, exactly the nine stated sets, 12 one-token exchanges, and zero valid token slides. It separately reports the boundary cases \(n=2,3,4\) (minimum sizes \(2,3,4\), counts \(4,6,16\)). The program prints `VERIFY_OK` on success. Compile with `g++ -std=c++17 -O3 -Wall -Wextra -pedantic verify.cpp -o verify` and execute `./verify`. Exhaustive finite checks are independent corroboration, not a substitute for the infinite proof.

## Relationship to prior work
Dillman and Kenter (2019, arXiv:1910.00168v1, Section 4.2) introduced leaky forcing and established general bounds for grid graphs, including the upper bound \(Z_{(1)}(P_a\square P_b)\le2a\) when \(a\le b\). Alameda, Kritschgau, Warnberg and Young (2020, arXiv:2008.06552v1, Theorem 2.3 and Section 4) characterize one-leaky sets using alternative possible forcers and sharpen grid bounds; **their Theorem 4.11 already proves the scalar equality \(Z_{(1)}(P_2\square P_n)=4\) for \(n\ge8\)**. These results supply the definition, the useful sufficiency criterion, and the existing large-length optimum size. The new contribution is the complete nine-placement classification at all lengths at least five and the exchange/slide geometry. The specific classification of all minimum one-leaky placements on the open two-row strip and both resulting reconfiguration graphs are not stated in the examined portions of those works. Ordinary zero forcing of circular ladders, complete-clique prisms, and ordinary forts of open ladders concern different graph classes or forcing conditions.

## Limitations
The theorem concerns labelled open two-row ladders of length at least five, the standard one-vertex-leak forcing rule, and reconfiguration restricted to minimum solutions. It does not classify larger one-leaky sets, two-leak forcing, closed circular ladders or wider grids. Publication-priority searches and primary-text comparisons can miss unindexed or differently named results; independent mathematical review is not claimed.

## References
1. S. Dillman and F. Kenter, *Leaky Forcing: A New Variation of Zero Forcing*, arXiv:1910.00168v1, first public 2019-10-01, https://arxiv.org/abs/1910.00168.
2. J. S. Alameda, J. Kritschgau, N. Warnberg and M. Young, *On leaky forcing and resilience*, arXiv:2008.06552v1, first public 2020-08-14, https://arxiv.org/abs/2008.06552.
