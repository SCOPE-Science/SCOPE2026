# Singular facet valleys at balanced lengths in weighted metric cycles

## Finding
Let \(m\ge4\) and let \(p\) be an integer satisfying \(1<p<m\) and \(p\equiv m\pmod 2\). Form a cycle on \(m+1\) vertices with \(m\) successive edge lengths equal to one and the closing edge length \(p\). Equip its vertices with the induced shortest-path metric. Let \(B_{m,p}\) be the unit ball of the **real** Lipschitz-free (Kantorovich–Rubinstein) space over this metric, of dimension \(m\).

The exact number of facets is
\[
F_{m,p}=\sum_{\substack{0\le j\le m\\|m-2j|\le p}}\binom mj.
\]
Put \(k=(m-p)/2\) and \(C=\binom mk\). Exactly \(2C\) facets have \(m+1\) vertices and are nonsimplicial; all remaining \(F_{m,p}-2C\) facets are simplices with \(m\) vertices. Every facet of the nonsimplicial kind corresponds to one sign assignment on the unit edges with signed sum \(p\) or \(-p\).

For any sufficiently small \(\varepsilon>0\), holding the \(m\) unit edges fixed and replacing the closing length by \(p-\varepsilon\) or \(p+\varepsilon\) gives respectively
\[
F_{-}=F_{m,p}+(m+p-2)C,\qquad
F_{+}=F_{m,p}+(m-p)C.
\]
Both excesses are positive, and their difference is \(F_{-}-F_{+}=2(p-1)C>0\). Thus each nontrivial balanced length is a strict isolated local minimum of the facet count, with an asymmetric loss from the two sides.

For example, at \(m=4,p=2\), the three counts are \(F_-=30\), \(F_{4,2}=14\), and \(F_+=22\); eight facets at the wall are nonsimplicial. At \(m=5,p=3\), they are \(60\), \(30\), and \(40\), with ten nonsimplicial facets at the wall.

## Assumptions and scope
The weighted graph is a simple cycle with strictly positive edge lengths. The closing length is strictly below the length of its alternate path (\(p<m\)); hence every graph edge is a strict shortest connection between its endpoints. The result includes all integers \(m,p\) satisfying the quantified assumptions and no other edge perturbations. The metric is the shortest-path metric on vertices, not the intrinsic metric on all points of the metric graph. All spaces, polarities, and facet counts are real.

A facet means a codimension-one exposed face of the unit ball \(B_{m,p}\); its number equals the number of vertices of the polar Lipschitz unit ball. The operator word 'simplicial' refers to the face itself, not the entire ball.

## Proof
Index the cycle edges by \(1,\ldots,m+1\), with respective lengths \(1,\ldots,1,p\), and orient cyclically. A real Lipschitz potential is determined up to an additive constant by its edge differences \(s_i\). The dual Lipschitz unit ball is linearly isomorphic to
\[
L_p=\left\{s\in\mathbb R^{m+1}:\sum_{i=1}^{m+1}s_i=0,\ |s_i|\le1\ (i\le m),\ |s_{m+1}|\le p\right\}.
\]
The edge inequalities imply all pairwise shortest-path Lipschitz inequalities by summing along either connecting path. Conversely the edge inequalities are necessary, so this is the complete dual ball.

The hyperplane has dimension \(m\), and any \(m\) coordinate functionals are independent on it. Thus at a vertex of \(L_p\) at least \(m\) of its \(m+1\) coordinate inequalities are tight. There are only two possibilities: the closing coordinate is not tight and all \(m\) unit coordinates are tight, or the closing coordinate is tight and at most one unit coordinate is not.

In the latter possibility, if unit coordinate \(i\) were strictly slack, the remaining \(m-1\) unit coordinates would be signs \(\pm1\). Write their sum as \(S'\). The zero-sum equation would force \(s_i= -S'\mp p\), an integer of odd parity, since \(S'\equiv m-1\pmod2\) and \(p\equiv m\pmod2\). Thus \(|s_i|\ge1\), a contradiction to strict slackness. **Every vertex therefore has all \(m\) unit coordinates equal to \(\pm1\).** Its closing coordinate is their negative sum and it is feasible precisely when the absolute sum is at most \(p\). Conversely every such sign vector has \(m\) linearly independent active constraints, so it is a vertex. Exactly \(\binom mj\) sign vectors have sum \(m-2j\). The displayed formula for \(F_{m,p}\) follows by polarity.

A feasible sign vector has \(m\) active edge inequalities when \(|\sum_{i\le m}s_i|<p\), and \(m+1\) when equality holds. To verify that active inequalities correspond to *distinct vertices of the primal ball*, observe that each oriented edge molecule is exposed: for edge \(i\) of length \(\ell_i\), take its potential edge difference equal to \(\ell_i\), and take each other difference to be \(-\ell_i\ell_j/\sum_{h\ne i}\ell_h\). Their sum is zero and all other normalized edge differences are strictly smaller than one, because every \(\ell_i<\sum_{h\ne i}\ell_h\). Hence each of the \(2(m+1)\) signed edge molecules is a vertex. Since the primal ball is their convex hull, the primal facet exposed by a dual vertex has exactly the corresponding number of active edge molecules, namely \(m\) or \(m+1\). A facet of dimension \(m-1\) with \(m\) vertices is a simplex, while one with \(m+1\) vertices is not. The equality \(|m-2j|=p\) occurs for \(j=k\) and \(j=m-k\), giving \(2\binom mk=2C\) nonsimplicial facets.

Finally, let \(t\) replace \(p\) in the last coordinate bound. Choose \(0<\varepsilon<1\) sufficiently small. At either \(t=p-\varepsilon\) or \(t=p+\varepsilon\), no subset of edge lengths sums to half the perimeter; hence a vertex has exactly \(m\) tight coordinates. The vertices with the closing coordinate slack have all unit differences equal to signs with \(|m-2j|<t\). At \(t=p-\varepsilon\), these contribute \(A=F_{m,p}-2C\); at \(t=p+\varepsilon\) they contribute \(F_{m,p}\). Vertices with a single slack unit coordinate have the other \(m-1\) unit differences signed, the closing coordinate equal to \(\pm t\), and the slack unit coordinate uniquely determined. The condition \(|s_i|<1\) yields, just to the left, exactly \(2m\binom{m-1}{k}=(m+p)C\) such vertices; just to the right it yields exactly \(2m\binom{m-1}{k-1}=(m-p)C\). Summing these two disjoint types gives
\[
F_{-}=A+(m+p)C=F_{m,p}+(m+p-2)C
\]
and
\[
F_{+}=F_{m,p}+(m-p)C.
\]
All coefficients are strictly positive for \(1<p<m\). This completes the proof.

## Verification
A standalone exact-rational program, `cycle_wall_check.py`, enumerates signed independent active sets of the edge-difference box section rather than using the displayed binomial formula to generate vertices. It verifies the facet counts, nonsimplicial counts and both one-sided jumps for twenty balanced parameter pairs in \(4\le m+1\le11\). Its successful terminal message is `ALL_WEIGHTED_CYCLE_WALL_TESTS_PASSED 20 critical_cases`. The code includes the already known equal-edge case \(p=1\) solely as a regression test; this case is not claimed as novel. Finite checks are not the proof of the universal assertions.

## Relationship to prior work
Gordon and Petrov [1] give the general duality and generic-metric face enumeration, but not the nongeneric balanced-cycle wall counts. Jevtić, Timotijević and Živaljević [2], Theorem 1.1, identify the boundary of a **generic** weighted-cycle KR polytope with a threshold Bier sphere; their explicit assumption that no subset carries half the perimeter fails at every wall considered here. Theorem 2.3 in [2] establishes polytopality of threshold Bier spheres generally, but does not supply the present nongeneric KR facet count, facet-size stratification, or asymmetric neighboring jumps. Higashitani, Jochemko and Michałek [3], and Braun and Bruegge [4], concern unweighted symmetric edge polytopes; these do not provide a variable-edge-length wall classification. The unweighted critical case \(p=1\) is deliberately excluded from the new statement. The noncritical nearby facet numbers may be obtained using known generic weighted-cycle methods; novelty is asserted only for the explicit simultaneous wall classification and its two-sided facet collapse.

## Limitations
This theorem does not enumerate lower-dimensional faces or treat multiple exceptional edge lengths. It does not claim any extension of the generic weighted-cycle/Bier-sphere correspondence, and it does not assert originality for the equal-edge case \(p=1\). The proof and checks do not establish that no equivalent formulation exists in unindexed literature; the priority assessment is therefore qualified.

## References
[1] J. Gordon and F. Petrov, *Combinatorics of the Lipschitz Polytope*, arXiv:1608.06848 (first public posting 2016-08-24), https://arxiv.org/abs/1608.06848.

[2] F. D. Jevtić, M. Timotijević and R. T. Živaljević, *Polytopal Bier Spheres and Kantorovich–Rubinstein Polytopes of Weighted Cycles*, arXiv:1812.00397 (2018), https://arxiv.org/abs/1812.00397.

[3] A. Higashitani, K. Jochemko and M. Michałek, *Arithmetic Aspects of Symmetric Edge Polytopes*, arXiv:1807.07678 (2018), https://arxiv.org/abs/1807.07678.

[4] B. Braun and K. Bruegge, *Facets of Symmetric Edge Polytopes for Graphs with Few Edges*, arXiv:2201.13303 (2022), https://arxiv.org/abs/2201.13303.
