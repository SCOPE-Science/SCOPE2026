# Parity reversal in Builder–Blocker general-position games on \(K_3\square K_n\)

## Finding
For every integer \(n\ge3\), the Builder-first and Blocker-first general-position game numbers on the three-row rook graph are
\[
\operatorname{gp}_{\mathrm g}(K_3\square K_n)
 = n+\begin{cases}1,&n\text{ odd},\\0,&n\text{ even},\end{cases}
\qquad
\operatorname{gp}'_{\mathrm g}(K_3\square K_n)
 = n+\begin{cases}0,&n\text{ odd},\\1,&n\text{ even}.\end{cases}
\]
This determines both adversarial game values for the infinite family and shows an exact parity reversal of the starting-player advantage. It does not claim values for wider rook graphs.

## Assumptions and scope
Let \(n\ge3\) and let \(R_n=K_3\square K_n\). Its vertices are pairs \((i,j)\) with \(i\in\{1,2,3\}\) and \(j\in\{1,\ldots,n\}\); two distinct pairs are adjacent exactly when their row or column coordinates agree. The graph has diameter two. A set is in *general position* if no three of its vertices lie on a shortest path. Builder and Blocker alternately add unused vertices, maintaining general position after each move. Play stops when no legal addition exists; Builder maximises and Blocker minimises the final cardinality. The game number with Builder opening is \(\operatorname{gp}_{\mathrm g}\), and with Blocker opening is \(\operatorname{gp}'_{\mathrm g}\), as in the cited game definition.

## Proof
**1. Forbidden patterns and terminal cardinalities.** Identify every square \((i,j)\) with the edge joining row vertex \(i\) and column vertex \(j\) in \(K_{3,n}\). Three selected squares violate general position precisely when their associated edges induce a three-edge path: the middle square lies on a two-edge shortest path between the outer squares. Thus legal square sets are exactly edge sets inducing disjoint unions of stars in \(K_{3,n}\) (the graph is bipartite, so no triangular edge-component is possible).

Every inclusion-maximal legal edge set has one of the following forms. If there is a column-star of degree three, every row vertex is already occupied by this star, and the configuration is exactly that column-star, of cardinality \(3\). If there is a column-star of degree two and the third row has a selected edge at a different column, those two star components are disjoint, and the third row must take all the other \(n-1\) columns at maximality, yielding \(2+(n-1)=n+1\). In all remaining maximal configurations, each column has at most one selected edge, and maximality requires every column to be used; the size is \(n\). These categories are exhaustive because distinct column-stars of degree at least two cannot be disjoint when only three rows exist, and a column-star of degree two without an edge at the third row is always extendible. Therefore *every* possible terminal score belongs to \(\{3,n,n+1\}\), and no play can exceed \(n+1\).

Two useful locked positions follow. A **high lock** consists of two marked squares in one column on two rows, and at least one marked square of the third row in another column; any subsequent legal square must lie in the third row at a column other than the column of the pair, so the eventual total is \(n+1\). A **middle lock** consists of at least one marked square in each of the three rows, with all their columns distinct; subsequent legal additions occur only in as-yet-unoccupied columns, so the eventual total is \(n\). A column of three squares gives a terminal **low lock** of size \(3\).

**2. The two-in-one-row phase.** Suppose the current set consists of \(k\) squares in one row, where \(2\le k<n\). A move in that row is always legal. A move outside that row is legal only in an unused column. If one player makes such an off-row move and at least two columns remain unused *before* that move, the other player may choose a square in the remaining third row in a **different** unused column, establishing a middle lock of eventual size \(n\). Alternatively, the other player may choose a square in the remaining third row in the **same** column as the off-row move, establishing a high lock of eventual size \(n+1\). Both options are legal; the off-row move has not changed any previously selected column.

Thus, a player who wants the high score may keep playing in the occupied row while at least two unused columns remain, and answer any opponent off-row move with the same-column square of the third row. If this player moves with precisely one unused column remaining, instead they can place an off-row square in that column. The opponent then has only one legal move, in its remaining row in that same column, so a high lock results. A player who wants the middle score may keep filling the occupied row, answer an opponent's off-row move made while at least two columns remained unused with a third-row move in a **different** unused column, and complete the row when offered its last unfilled square. Hence the player who acts at the state with \(n-1\) occupied-row squares controls whether the terminal size is \(n+1\) (Builder) or \(n\) (Blocker), provided the opponent has not deviated first. Any earlier deviation instead lets the player following this strategy lock their preferred outcome. This statement includes \(n=3\).

**3. Optimal response to the first move.** Either player can move second in the *same row* as the first square, obtaining exactly the two-in-one-row phase with \(k=2\). In Builder-first play, Builder can also guarantee at least the row-phase value against any other response: if Blocker's second move shares the first column but not its row, Builder picks a square in the third row at a different column, establishing a high lock. If the second move shares neither row nor column, Builder picks a square in the third row in the first square's column, again establishing a high lock. These choices are possible since \(n\ge3\). Therefore choosing a same-row reply suffices for Blocker to attain the row-phase upper bound; choosing otherwise allows Builder the larger score \(n+1\).

In Blocker-first play, choosing a same-row second square suffices for Builder to obtain the row-phase lower bound. For completeness, Blocker's response to a second square outside the first row cannot increase Builder's advantage: when it is in the first column, Blocker can choose the third square in that column to finish at \(3\); when it is in a different column, Blocker can choose a square in the third row and a third distinct column, establishing a middle lock of size \(n\). This proves that the same-row second move is optimal for the relevant minimax bound in either game.

**4. Parity.** From a same-row opening pair, the next move belongs to the original first player, and after \(n-1\) same-row moves the next player is Builder precisely when (i) Builder moved first and \(n\) is odd, or (ii) Blocker moved first and \(n\) is even. The row-phase strategies then produce exactly \(n+1\) in these two cases, and \(n\) in the others. The first-two-move analysis rules out an improved adversarial alternative, completing both minimax equalities. \(\square\)

## Verification
The accompanying standalone Python verifier `artifacts/verify.py` constructs the rook graph directly, tests the shortest-path condition on every triple of squares using the exact diameter-two graph metric, enumerates all legal game continuations by cached minimax recurrence, and tests all possible first moves and same-row second replies. It returns `VERIFY_OK` for every \(n\in\{3,4,5,6,7,8\}\), with \(185514\) cached minimax states in total. This is a finite corroboration, not the proof of the arbitrary-\(n\) theorem.

## Relationship to prior work
Klavžar, Tian and Tuite [1] define the Builder- and Blocker-first general-position minimax numbers and determine them for several other graph families. Their accessible version treats complete multipartite graphs and Kneser graphs, but not the stated rook-graph family. Di Stefano et al. [2, Theorem 5.3] prove the *non-game* lower general-position number \(\operatorname{gp}^{-}(K_3\square K_n)=3\); the known maximum is \(n+1\) by the same paper's cited results. Those extremal parameters bound but do not determine adversarial minimax. Klavžar, Neethu and Chandran [3] study which player makes the *last* move on Cartesian products, not minimisation/maximisation of the final size. The later mutual-visibility game paper [4, Section 4] studies the *existence* of a clean geodesic between each selected pair, rather than the general-position requirement forbidding **all** selected interior geodesic vertices; its rook-graph conclusions therefore do not imply these scores.

## Limitations
Only three-row rook graphs and \(n\ge3\) are covered. This does not classify optimal move sequences, all maximal general-position sets, or wider rook graphs. Finite computations do not replace the infinite strategy proof. Unindexed equivalent prior game calculations cannot be ruled out by literature search; an independent mathematical audit has not been performed.

## References
[1] S. Klavžar, J. Tian and J. Tuite, *Builder-Blocker General Position Games*, arXiv:2310.19949 (first submitted October 30, 2023). https://arxiv.org/abs/2310.19949

[2] G. Di Stefano, S. Klavžar, A. Krishnakumar, J. Tuite and I. Yero, *Lower General Position Sets in Graphs*, arXiv:2306.09965 (2023). https://arxiv.org/abs/2306.09965

[3] S. Klavžar, P. K. Neethu and S. V. Ullas Chandran, *The general position achievement game played on graphs*, arXiv:2111.07425 (2021). https://arxiv.org/abs/2111.07425

[4] V. Iršič Chenoweth et al., *Builder-Blocker Mutual-Visibility Game*, Bull. Malays. Math. Sci. Soc. 49 (2026), Article 89. https://doi.org/10.1007/s40840-026-02083-9
