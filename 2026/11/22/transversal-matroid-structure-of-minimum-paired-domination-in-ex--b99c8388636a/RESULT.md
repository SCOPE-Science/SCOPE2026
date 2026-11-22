# Transversal-matroid structure of minimum paired domination in extremal five-cycle blowups

## Finding

Let \(a,b\ge1\) be integers. Let \(G_{a,b}\) be the clique blowup \(C_5(1,1,1,a,b)\) with consecutive classes \(\{x_0\},\{x_1\},\{x_2\},A,B\), where \(|A|=a\), \(|B|=b\). Each class is a clique; two classes are completely joined precisely when consecutive on the five-cycle. A paired-dominating set is a dominating vertex set inducing a perfect matching.

**Theorem.** The minimum paired-domination number of \(G_{a,b}\) equals four. All its minimum paired-dominating sets are exactly the bases of a rank-four **transversal matroid** on \(V(G_{a,b})\), whose four auxiliary roles are \(\{1,2,3,4\}\), with allowed role sets

\[
\begin{array}{c|ccccc}
\text{vertex class}&x_0&x_1&x_2&A&B\\\hline
\text{allowed roles}&\{1\}&\{2,3\}&\{1,4\}&\{2,4\}&\{3,4\}
\end{array}.
\]

Precisely, a four-set is minimum paired dominating if and only if its vertices can be assigned **distinct** allowed roles covering all four roles. There are exactly

\[
N(a,b)=a^2b+ab^2+a^2+ab+b^2
\]

such sets. Join two minima by an edge if they differ by one vertex. The exchange graph is connected and, for every pair \(S,T\) of minima,

\[
d(S,T)=4-|S\cap T|.
\]

Its exact diameter is

\[
\operatorname{diam}\mathcal R(G_{a,b})=\min\{4,a+b-1\}.
\]

For arbitrary real vertex costs, minimizing the total cost over all minimum paired-dominating sets is consequently a minimum-weight matroid-basis problem and is solvable by the ordinary greedy matroid algorithm with a bipartite-matching independence test.

## Assumptions and scope

All graphs are finite, undirected and simple. The five classes are nonempty, with the first three singleton. An induced perfect matching is **not** required: only a perfect matching within the induced subgraph on selected vertices. A vertex dominates itself and its graph neighbours. The exchange move removes one selected vertex and inserts one currently unselected vertex, preserving minimum paired domination. The result is for every labelled \(G_{a,b}\) with \(a,b\) positive, including \(a=b=1\); it does not assert the matroid property for arbitrary paired-domination problems or arbitrary clique blowups of five-cycles.

## Proof

**1. The minimum is four.** Every two-vertex paired-dominating set would be an adjacent pair, hence would occupy either one clique class or two consecutive classes. Their closed neighbourhoods cover at most three, respectively four, of the five nonempty classes. In either case a class is undominated. The cardinality of a paired-dominating set is even, so no smaller such set exists. The four-set \(\{x_0,x_1,x_2,u\}\), for any \(u\in A\cup B\), dominates the graph and has a perfect matching: use \(x_0x_1,x_2u\) if \(u\in A\), and \(x_1x_2,x_0u\) if \(u\in B\).

**2. Characterize every four-set.** Let \(C=S\cap\{x_0,x_1,x_2\}\), and let \(r=|S\cap A|\), \(s=|S\cap B|\). The following table is exhaustive; the last column lists exactly the allowed \((r,s)\) at total size four.

| \(C\) | Allowed \((r,s)\) |
|---|---|
| \(\{x_0,x_1,x_2\}\) | \((1,0),(0,1)\) |
| \(\{x_0,x_1\}\) or \(\{x_1,x_2\}\) | \((2,0),(1,1),(0,2)\) |
| \(\{x_0,x_2\}\) | \((1,1)\) |
| \(\{x_0\}\) or \(\{x_2\}\) | \((2,1),(1,2)\) |
| \(\varnothing\) or \(\{x_1\}\) | none |

Here is a direct derivation. If \(C\) is empty, \(x_1\) is undominated. If \(C=\{x_1\}\), then \(x_1\) is isolated in \(G[S]\), preventing a perfect matching. If \(C=\{x_0\}\) or \(\{x_2\}\), both \(A\) and \(B\) must be selected: the side adjacent to the selected singleton provides its matching partner and the other side is needed to dominate the opposite endpoint. With three further vertices, the only possibilities are \((2,1)\) and \((1,2)\), and both have perfect matchings. If \(C=\{x_0,x_2\}\), these nonadjacent selected singletons require a partner from \(B\) and from \(A\), respectively, so \((1,1)\) is necessary and sufficient. If \(C\) is either adjacent core pair, that pair can be matched together while any two additional vertices from the adjacent cliques \(A\cup B\) can be matched together; all vertices are dominated. If all three core vertices are chosen, one additional vertex in either \(A\) or \(B\) completes a perfect matching. This proves both necessity and sufficiency throughout the table.

**3. Identify the transversal matroid.** Connect every vertex in a class to exactly the auxiliary roles shown in the theorem. The following elementary four-role matching analysis reproduces the table: no selected vertex in \(\{x_0,x_2\}\) makes role 1 unavailable; with only \(x_0\) or only \(x_2\) in the core, both \(A,B\) are needed to fill roles 2 and 3, and this condition is sufficient; with core pair \(\{x_0,x_2\}\), these two vertices occupy roles 1 and 4, requiring one \(A\) and one \(B\); with core pair \(\{x_0,x_1\}\) or \(\{x_1,x_2\}\), any two from \(A\cup B\) can occupy the remaining roles, with the core vertices adjusted accordingly; with all three core vertices, either kind of fourth vertex completes the assignment. Thus the matchable four-subsets are **exactly** the four-vertex paired-dominating sets classified in Step 2.

Partial transversals of a finite family of sets form a transversal matroid (the standard matching/alternating-path theorem). Since a four-role matching exists, its rank is exactly four. The four-sets identified above are therefore precisely its bases. This also proves the basis-exchange axiom for every graph size, not just a tested range.

**4. Count bases.** The five nonempty table rows contribute, respectively,

\[
(a+b),\qquad 2\left(\binom a2+ab+\binom b2\right),\qquad ab,\qquad 2\left(\binom a2b+a\binom b2\right).
\]

The sum simplifies to \(a^2b+ab^2+a^2+ab+b^2\).

**5. Distances and diameter.** Matroid basis exchange repeatedly replaces an element of \(S\setminus T\) with an element of \(T\setminus S\), never leaving the basis family. It reaches \(T\) in \(4-|S\cap T|\) exchanges, while no shorter path is possible. Since the graph has \(a+b+3\) vertices, two four-sets have intersection at least \(\max\{0,5-a-b\}\). Therefore the diameter is at most \(\min\{4,a+b-1\}\).

The bound is attained. For \(a=b=1\), every four-set is a base and distinct bases differ by one element. For \((a,b)=(1,2)\), the bases \(\{x_0,x_1,b_1,b_2\}\) and \(\{x_2,a_1,b_1,b_2\}\) intersect in two elements. For \((a,b)=(1,3)\), use \(\{x_0,x_1,b_1,b_2\}\) and \(\{x_2,a_1,b_2,b_3\}\), intersecting in one; the case \((3,1)\) is symmetric. For \((2,2)\), use \(\{x_0,x_1,a_1,a_2\}\) and \(\{x_2,a_1,b_1,b_2\}\), also intersecting in one. For \(a+b\ge5\), disjoint bases exist: when \(a\ge2,b\ge3\), take \(\{x_0,x_1,b_1,b_2\}\) and \(\{x_2,a_1,a_2,b_3\}\); when \(a\ge3,b\ge2\), take \(\{x_1,x_2,a_1,a_2\}\) and \(\{x_0,a_3,b_1,b_2\}\); and for \(a=1,b\ge4\) use \(\{x_0,x_1,b_1,b_2\}\) and \(\{x_2,a_1,b_3,b_4\}\), with the symmetric construction when \(b=1,a\ge4\). These constructions cover all integer parameters and complete the diameter proof.

## Verification

The standalone programs `verify_patterns.py` and `verify_direct.cpp` use two independent implementations. The Python program tests the full 28-pattern occupancy certificate, compares graph-paired-domination and bipartite role matchability for 50,832 four-subset instances with \(1\le a,b\le8\), and verifies the counting formula. The C++17 program independently compares the two predicates for 94,941 instances with \(1\le a,b\le9\), checks all counts, and enumerates the entire ordered strong basis-exchange condition at \(a=b=5\). Both passed when executed. These finite checks test the implementation and detect boundary mistakes; the theorem for unbounded \(a,b\) follows from the table and transversal-matroid argument, **not** from finite enumeration.

To reproduce, execute `python3 verify_patterns.py`; then compile with `g++ -std=c++17 -O2 verify_direct.cpp -o verify_direct` and run `./verify_direct`. No third-party packages are required.

## Relationship to prior work

Henning, McCoy and Southey (2014) define the family \(C_5(1,1,1,a,b)\) as part of their extremal classification of graphs with given paired-domination number four and maximum edge count. That published classification supplies the natural object and establishes the scalar parameter; it does not, by its stated theorem, imply that **every optimal set** is a transversal-matroid basis, its exact number, or its exchange distance. The present proof is self-contained and does not rely on an unverified inference from the scalar theorem. Haynes and Slater (1998) introduced paired domination, while classical transversal-matroid theory supplies the basis-exchange consequences once the new four-role presentation has been established.

This matroid property is **not automatic** for paired domination: on the seven-cycle, the optimal sets \(S=\{0,1,3,4\}\) and \(T=\{0,2,3,6\}\), with indices modulo seven, violate the basis-exchange axiom for removal of vertex \(4\): neither replacement by \(2\) nor by \(6\) preserves paired domination. This contrast is why the extremal blowup family's matroid structure is a substantive configuration-space feature.

## Limitations

The theorem is restricted to the clique-blowup family with three singleton classes, not the other extremal family from the 2014 paper. The mathematical proof of the matroid representation is complete, but the research-priority assessment remains limited by the availability of full text of some related papers and by possible unindexed earlier results. The externally hosted rendering of the closest 2014 paper exposed the definitions and exact extremal theorem, but no independently downloaded full PDF was available; therefore the absence of an equivalent result elsewhere in that paper is not claimed as a whole-document exclusion. This is self-reviewed research, not independently audited or externally certified.

## References

1. M. A. Henning, J. McCoy, and J. Southey, "Graphs with maximum size and given paired-domination number," *Discrete Applied Mathematics* 170 (2014), 72–82, doi:10.1016/j.dam.2014.01.019. https://doi.org/10.1016/j.dam.2014.01.019
2. T. W. Haynes and P. J. Slater, "Paired-domination in graphs," *Networks* 32 (1998), 199–206, doi:10.1002/(SICI)1097-0037(199810)32:3<199::AID-NET4>3.0.CO;2-F.
3. R. A. Brualdi and G. W. Dinolt, "Characterizations of transversal matroids and their presentations," *Journal of Combinatorial Theory, Series B* 12 (1972), 268–286, doi:10.1016/0095-8956(72)90041-X.
4. SageMath documentation, "Transversal matroids," https://doc.sagemath.org/html/en/reference/matroids/sage/matroids/transversal_matroid.html (definition and standard matching interpretation).
