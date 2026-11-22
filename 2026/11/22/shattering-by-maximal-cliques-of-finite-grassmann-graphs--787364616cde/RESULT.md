# Shattering by maximal cliques of finite Grassmann graphs

## Finding

Let \(q\ge2\) be a prime power, \(n\ge4\), and \(2\le k\le n-2\). The vertices of the Grassmann graph \(J_q(n,k)\) are the \(k\)-dimensional subspaces of \(\mathbb F_q^n\); two distinct vertices are adjacent when their intersection has dimension \(k-1\). Regard the vertex sets of **all inclusion-maximal cliques** as a Boolean concept class, with one membership query for each graph vertex.

**Complete criterion.** A query support is shattered precisely when it is empty, is a singleton, is an adjacent pair, or is a graph triangle which is **not** wholly contained in one pencil
\[
\mathcal P(A,B)=\{U: A\subset U\subset B,\ \dim A=k-1,\ \dim B=k+1,\ \dim U=k\}.
\]
Each pencil has \(q+1\) vertices. No four-point support is shattered. In particular, the VC and Littlestone dimensions are both exactly \(3\).

Define \(G_q(a,b)\) to be the number of \(b\)-dimensional subspaces of \(\mathbb F_q^a\) (a Gaussian binomial coefficient), and put
\[
L_q(r)=\frac{q^r-1}{q-1},\qquad
B_q(r)=\binom{L_q(r)}{3}-G_q(r,2)\binom{q+1}{3}.
\]
Then the **complete shattering polynomial** is
\[
\boxed{\Phi_{n,k,q}(z)=1+G_q(n,k)z+
\frac{q}{2}G_q(n,k)L_q(k)L_q(n-k)z^2+
\bigl(G_q(n,k-1)B_q(n-k+1)+G_q(n,k+1)B_q(k+1)\bigr)z^3.}
\]
The shattering complex is pure and two-dimensional: all its maximal faces are shattered triples. The number of excluded graph triangles (pencil triples) is
\[
G_q(n,k-1)G_q(n-k+1,2)\binom{q+1}{3}.
\]
For example \(\Phi_{4,2,2}(z)=1+35z+315z^2+840z^3\), while \(\Phi_{4,2,3}(z)=1+130z+3120z^2+18720z^3\).

## Assumptions and scope

All subspaces and dimensions are over the same finite field \(\mathbb F_q\), and a concept is one complete *maximal* graph clique, not a nonmaximal clique, a graph neighborhood, or a family of vertices lying in an arbitrary flat. Shattering means that for every subset \(T\) of a query support \(S\), some maximal clique \(C\) satisfies \(C\cap S=T\). The empty support is shattered because the family of maximal cliques is nonempty. The hypotheses exclude the complete-graph degeneracies \(k=1\) and \(k=n-1\).

A **star** indexed by a \((k-1)\)-subspace \(A\) is \(\mathcal S(A)=\{U:A\subset U\}\); a **top** indexed by a \((k+1)\)-subspace \(B\) is \(\mathcal T(B)=\{U:U\subset B\}\). A standard Grassmann-graph clique theorem states that these are precisely the maximal cliques. Distinct adjacent vertices \(U,V\) belong to exactly two maximal cliques: \(\mathcal S(U\cap V)\) and \(\mathcal T(U+V)\). Their intersection is the pencil \(\mathcal P(U\cap V,U+V)\). This structural theorem is used as a stated, referenced premise, not asserted as new.

## Proof

**1. Empty traces on small supports.** Fix any \((k-2)\)-subspace \(R\). Exactly \(L_q(n-k+2)\) different \((k-1)\)-subspaces contain \(R\). Each specified \(k\)-space \(U\) contains at most \(q+1\) of these: exactly that many when \(R\subset U\), and otherwise none. Since \(n-k+2\ge4\) and
\[
L_q(4)=q^3+q^2+q+1>3(q+1)\quad(q\ge2),
\]
for any support of at most three vertices one of these \((k-1)\)-subspaces \(A\) lies in none of them. The maximal clique \(\mathcal S(A)\) realizes the empty labeling.

**2. Singleton and pair supports.** Every vertex \(U\) lies in a star, so its one-positive labeling is realizable. An adjacent pair \(U,V\) has a two-positive witness, either of its common maximal cliques. For the labeling positive on \(U\) and negative on \(V\), choose a \((k-1)\)-subspace of \(U\) different from \(U\cap V\); such a choice exists because \(L_q(k)\ge q+1\ge3\). The corresponding star contains \(U\) but not \(V\). Reverse symmetrically and use step 1 for the empty trace. A nonadjacent pair cannot be simultaneously contained in any clique, and hence is not shattered.

**3. Triple supports.** A shattered triple is necessarily a graph triangle by step 2. Every graph triangle is contained in at least one maximal clique: if \(U,V,W\) are pairwise adjacent, \(W\) belongs to the star or top of the edge \(UV\). A triangle contained in a pencil cannot be shattered: for any two of its vertices, the only two maximal cliques containing that pair are exactly the corresponding star and top, and both contain the third vertex. Thus its two-positive/one-negative labeling fails.

Conversely suppose a triangle \(U,V,W\) is not contained in a pencil. It lies in a star or top, providing the all-positive trace. For the two-positive trace on \(U,V\) excluding \(W\), choose whichever of \(\mathcal S(U\cap V)\) and \(\mathcal T(U+V)\) does not contain \(W\). This is possible because otherwise all three would lie in their common pencil. The same argument gives every other two-positive trace. For a singleton-positive trace on \(U\), select a \((k-1)\)-subspace of \(U\) different from both \(U\cap V\) and \(U\cap W\). Since there are \(L_q(k)\ge3\) such subspaces in total, at least one remains. Its star contains \(U\), neither \(V\) nor \(W\). Combine with step 1 to obtain all eight traces. Therefore the stated triangle criterion is necessary and sufficient.

**4. No four-point support and exact dimensions.** Suppose a four-point support were shattered. Its all-positive trace would place all four vertices in some maximal clique \(C\). Each three-subset would be shattered and hence, by step 3, could not lie in a pencil. Choose three vertices \(U,V,W\). Their nonpencil triangle belongs to a **unique** maximal clique: any two distinct maximal cliques containing that triangle would be the star and top of an edge, forcing the triangle inside their pencil. That unique clique must be \(C\), which also contains the fourth vertex. Hence there is no concept realizing three positives on \(U,V,W\) and a negative on the fourth, a contradiction.

Noncollinear triples exist in stars since \(\dim(\mathbb F_q^n/A)=n-k+1\ge3\); thus \(\operatorname{VCdim}=3\). A shattered triple supplies a depth-three Littlestone mistake tree. To rule out depth four, consider the root query \(U\) and the next query \(V\) on the positive branch. If \(U,V\) are nonadjacent, there is no concept containing both. If adjacent, exactly two concepts contain both. In either case, the double-positive branch has fewer than four concepts and cannot support its required remaining binary tree of depth two (which would have four distinct leaves). Therefore \(\operatorname{Ldim}=3\).

**5. Enumeration and purity.** There are \(G_q(n,k)\) vertices, each with \(q L_q(k)L_q(n-k)\) adjacent vertices, giving the degree-two coefficient. A star indexed by \(A\) is a projective point set with \(L_q(n-k+1)\) elements, and a top indexed by \(B\) is dually a projective point set with \(L_q(k+1)\) elements. In a projective space with \(L_q(r)\) points, the collinear triples number \(G_q(r,2)\binom{q+1}{3}\), since each collinear triple determines a unique projective line. Subtraction gives \(B_q(r)\) noncollinear triples. Each nonpencil triangle belongs to exactly one maximal clique, proving the cubic coefficient without double counting. A pencil is uniquely indexed by its pair \((A,B)\), and there are \(G_q(n,k-1)G_q(n-k+1,2)\) pencils; each has \(\binom{q+1}{3}\) triples, again uniquely assigned to its pencil. Finally, every graph edge extends to a nonpencil triangle: choose a third vertex of its star outside the pair's pencil, possible since \(L_q(n-k+1)>q+1\). Every singleton extends to an edge. Thus all facets are triangles, as claimed.

## Verification

The standalone program `grassmann_maxclique_check.py` builds small prime-field vector spaces directly, enumerates all subspaces, constructs adjacency by intersection cardinality, independently finds graph maximal cliques using a graph algorithm, and evaluates every Boolean trace on all one-, two-, and three-query supports. For \(J_2(4,2)\) it also exhausts all four-query supports; for \(J_3(4,2)\) it checks 10,000 reproducibly sampled four-supports. Its outputs match the two face vectors above. An additional check on \(J_2(5,2)\) directly reconstructed 186 maximal cliques among 155 vertices, and verified 2,000 reproducibly sampled supports at each of sizes two, three, and four, yielding the predicted coefficients \((1,155,3255,17360)\). Finite tests corroborate but do not prove the unrestricted theorem: the preceding arguments provide that proof.

## Relationship to prior work

Kwiatkowski and Pankov (2023) explicitly state the star/top classification for ordinary Grassmann graphs, in an article studying a different induced graph of simplex codes. Shuldiner and Oldford (2022) classify maximal cliques of ordinary set-valued Johnson graphs; this provides a natural combinatorial comparison, but not the finite-field pencil obstruction. Benediktsson, Macpherson and Adler (2020) study VC dimensions of **open adjacency neighborhoods** in Johnson/Hamming graphs, not incidence with maximal cliques. A published result on maximal cliques of **line graphs** gives an online-dimension-three upper bound, while another determines the complete-graph edge-family shattering polynomial. The unrestricted line-graph result does not apply here: in a simple line graph, if an adjacent pair belongs to two maximal cliques, one is a triangle of size three, whereas every adjacent pair of the Grassmann graph belongs to two maximal cliques each containing at least seven vertices. Hence the Grassmann graphs in scope cannot be line graphs of simple graphs; moreover the finite-field pencil exclusion and Gaussian coefficients are not consequences of the complete-graph edge case.

The contribution here is the complete, all-rank finite-field *maximal-clique incidence* shattering criterion, its exact Gaussian-binomial polynomial, the sharp projective-pencil obstruction and its static/online dimensions. These exact implications were not found among the inspected results; absence from a search is not proof of universal historical priority.

## Limitations

The theorem is stated only for prime-power finite fields, nondegenerate Grassmann ranks, and maximal-clique membership concepts. Nothing is asserted for arbitrary induced subgraphs of Grassmann graphs, nonmaximal cliques, neighborhood concepts, or the degenerate complete-graph ranks. The computational checker only implements prime fields \(2\) and \(3\), not general prime-power arithmetic. Unindexed publications or unavailable broader results could affect attribution; the work has not undergone an independent mathematical audit.

## References

1. M. Kwiatkowski and M. Pankov, *On maximal cliques in the graph of simplex codes*, first public 2023-08-11, https://arxiv.org/abs/2308.06109 (particularly the introductory star/top statement).
2. P. Shuldiner and R. W. Oldford, *The Clique Structure of Johnson Graphs*, first public 2022-08-26, https://arxiv.org/abs/2208.12710.
3. B. G. Benediktsson, D. Macpherson and I. Adler, *Vapnik-Chervonenkis Dimension and Density on Johnson and Hamming Graphs*, first public 2020-07-31, https://arxiv.org/abs/2007.16042.
4. *Uniform online dimension three for maximal cliques of line graphs and their complete-graph shattering polynomial*, publicly indexed 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-uniform-online-dimension-three-for-maximal-cliques-of-line-graph--6f453c3402bf.
5. *Exact shattering and online learning for maximal intersecting edge families*, publicly indexed 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-shattering-and-online-learning-for-maximal-intersecting-ed--636288308791.
