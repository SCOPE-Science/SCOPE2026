# The seven-vertex extremal transition for Mahler products of type-B tree-root polytopes

## Finding
For every tree \(T\) on \(n\ge2\) vertices, let
\[
\mathcal B_T=\operatorname{conv}\bigl(\{0,\pm e_i:i\in V(T)\}\cup\{\pm e_i\pm e_j:ij\in E(T)\}\bigr)\subset\mathbb R^n.
\]
Let \(M(T)\) denote the total number of matchings of \(T\), including the empty matching. Choose one of the two bipartition classes \(U,V\), and define the height-two poset \(Q_T\) by putting \(u\prec v\) for every edge \(uv\) with \(u\in U\) and \(v\in V\). Let \(L(T)\) be the number of linear extensions of \(Q_T\); reversing the two classes dualizes the poset without changing this count. The normalized Mahler product is exactly
\[
\boxed{\mathscr R(T):=\frac{n!}{4^n}\operatorname{vol}_n(\mathcal B_T)\operatorname{vol}_n(\mathcal B_T^\circ)=\frac{M(T)L(T)}{n!}.}
\]
Among all isomorphism classes of trees with \(2\le n\le6\) vertices, the path is the unique maximizer. For seven vertices the unique maximizer is the subdivided claw \(S_{2,2,2}\), obtained by subdividing each edge of a three-leaf star exactly once. Explicitly,
\[
(M(S_{2,2,2}),L(S_{2,2,2}))=(20,288),\qquad(M(P_7),L(P_7))=(21,272),
\]
so
\[
\boxed{\mathscr R(S_{2,2,2})=\tfrac87>\tfrac{17}{15}=\mathscr R(P_7),\quad\mathscr R(S_{2,2,2})-\mathscr R(P_7)=\tfrac1{105}.}
\]
Thus seven vertices is the first size at which the path loses its maximality among tree-root polytopes.

## Assumptions and scope
The graph is finite, simple, connected, and acyclic; volumes are ordinary Euclidean volumes in the ambient \(n\)-space, with the standard inner-product polar. The origin lies in the interior because \(\mathcal B_T\) contains the coordinate cross-polytope, so the polar is bounded. The empty matching is included. The order on \(Q_T\) has no relations except those forced by the edges and transitivity; all comparabilities go from \(U\) to \(V\). The theorem is an exact formula for every tree, and a sharp, exhaustive finite classification only for sizes two through seven; there is no extrapolation to larger-tree maximizers.

## Proof
**Primal volume.** Ohsugi and Tsuchiya [1] establish for type-B graph-root polytopes of a forest the palindromic Ehrhart \(h^*\)-identity
\[
 h^*(\mathcal B_T,z)=\sum_{k\ge0}m_k(T)(4z)^k(1+z)^{n-2k},
\]
where \(m_k(T)\) counts matchings with exactly \(k\) edges. Evaluating at \(z=1\), and using that the sum of Ehrhart \(h^*\)-coefficients is normalized lattice volume, gives
\[
 n!\operatorname{vol}_n(\mathcal B_T)
 =2^n\sum_{k\ge0}m_k(T)=2^nM(T).
\]
This primal-volume identity is **previously published mathematics** and is not claimed as a new lemma.

**Polar volume.** Since \(\mathcal B_T\) is unconditional, its polar is exactly
\[
 \mathcal B_T^\circ=\{y\in\mathbb R^n: |y_i|\le1\ (i\in V(T)),\ |y_i|+|y_j|\le1\ (ij\in E(T))\}.
\]
Fix one coordinate orthant, put \(x_i=|y_i|\), and use a bipartition \(U\sqcup V\) of the tree. Within that orthant, the inequalities become \(0\le x_i\le1\) and \(x_u+x_v\le1\). The volume-preserving affine involution \(x_v\mapsto1-x_v\) for \(v\in V\), leaving the \(U\) coordinates unchanged, converts each edge inequality to \(x_u\le x_v\). This is Stanley's order polytope of \(Q_T\). Its standard sorting-chamber triangulation has one simplex of Euclidean volume \(1/n!\) for every linear extension, so the volume of each of the \(2^n\) orthants is \(L(T)/n!\). Orthants overlap only on null sets. Consequently,
\[
 \operatorname{vol}_n(\mathcal B_T^\circ)=\frac{2^nL(T)}{n!}.
\]
Combining the two equalities proves the exact formula; no unknown analytic normalizing constants remain.

**Complete finite extremality verification.** Every labeled tree on \(n\ge2\) vertices has a unique Prüfer sequence of length \(n-2\); enumerating all \(n^{n-2}\) sequences is therefore exhaustive. Two subset recurrences count its matchings and its poset linear extensions. For any nonempty vertex subset \(S\), select its least vertex \(i\), and let \(f(S)\) count matchings of its induced subgraph. Then
\[
 f(S)=f(S\setminus\{i\})+\sum_{j\in N(i)\cap S}f(S\setminus\{i,j\}),\qquad f(\varnothing)=1.
\]
For the poset, let \(g(S)\) count ways to extend an already placed ideal \(S\). Then \(g(V(T))=1\), and \(g(S)\) is the sum of \(g(S\cup\{i\})\) over vertices \(i\notin S\) whose predecessors all belong to \(S\). Both are exact integer recurrences. To avoid overcounting isomorphic trees, canonically encode an unrooted tree as the lexicographically least rooted-parentheses encoding over all possible roots, sorting child encodings at every vertex. A simple inductive reconstruction shows that two trees have the same code precisely when they are isomorphic.

The resulting isomorphism-class counts for sizes \(2,3,4,5,6,7\) are \(1,1,2,3,6,11\), respectively. The maximal products \(M(T)L(T)\) are \(2,6,25,128,793,5760\). In the first five sizes the unique maximizer is a path; in the last size it is \(S_{2,2,2}\). The seven-vertex census, descending by exact product, is as follows (codes are canonical rooted-parentheses strings, and represent every one of the eleven isomorphism types):

| Canonical tree code | Matchings | Extensions | Product |
| --- | ---: | ---: | ---: |
| `((((())(()))))` | 20 | 288 | 5760 |
| `((((((()))))))` | 21 | 272 | 5712 |
| `(((((())()))))` | 19 | 298 | 5662 |
| `(((((()())))))` | 18 | 310 | 5580 |
| `((((()())())))` | 17 | 328 | 5576 |
| `((((())()())))` | 16 | 348 | 5568 |
| `((((()()))()))` | 15 | 360 | 5400 |
| `((((()()()))))` | 14 | 384 | 5376 |
| `(((()()())()))` | 13 | 408 | 5304 |
| `(((()()()())))` | 11 | 480 | 5280 |
| `((()()()()()))` | 7 | 720 | 5040 |

The supplied independently executable exact enumeration script implements these recurrences and includes explicit assertions of the unique maximizers and every class count. This exhausts the finite claim; it is not statistical sampling.

## Verification
Run `python check_tree_mahler.py` with the stated dependencies. The script enumerates all \(18{,}248\) labeled trees on two through seven vertices and checks their complete unlabeled-class census and optimizing classes by exact integer arithmetic. It additionally reconstructs the primal and dual convex hulls for four representative trees in dimensions four through seven using floating-point computational geometry, and checks the volumes against the two theoretical formulas. The latter four checks corroborate the formulas but are not substituted for the analytic proof. Reported success markers are `EXACT_TREE_CENSUS_PASSED 18248` and `INDEPENDENT_HULL_CHECKS_PASSED 4`.

## Relationship to prior work
The type-B polytope and the forest matching-polynomial Ehrhart identity belong to Ohsugi–Tsuchiya [1], with further matching-polynomial context [2]. Stanley's classical order-polytope volume theorem [3] supplies the standard linear-extension volume once the polar orthant is identified. Kohl–Olsen–Sanyal [4] study unconditional reflexive polytopes, prove broader Mahler lower bounds, and explicitly investigate maximum volume products across perfect graphs through nine vertices. Their study includes the broader extremal context, but the inspected statements do not specify the tree-only seven-vertex transition proved here. The contribution asserted here is the **joint exact primal–polar factorization for tree-root polytopes and its first sharp tree-extremal crossover**, not the preexisting primal or order-polytope identities. Earlier equivalent calculations or an unpublished enumeration behind a published global experiment may exist; the originality conclusion is provisional.

## Limitations
The seven-vertex statement is an exhaustive finite theorem, not a general extremal classification for all tree orders. The displayed polarity and linear-extension formula actually apply to bipartite graphs, but the matching interpretation of the primal volume used here specifically assumes a forest. No priority, independence, or formal machine certification is claimed. The numerical hull computations have floating-point tolerances and do not replace exact combinatorial enumeration or proofs. Whether a prior source lists the same seven-vertex tree maximum under different graph-polytope nomenclature remains a bibliographic risk.

## References
[1] H. Ohsugi and A. Tsuchiya, *Reflexive polytopes arising from bipartite graphs with gamma-positivity associated to interior polynomials*, arXiv:1810.12258 (first submitted 2018-10-29), especially Proposition 3.4. https://arxiv.org/abs/1810.12258

[2] H. Ohsugi and A. Tsuchiya, *Symmetric edge polytopes and matching generating polynomials*, arXiv:2008.08621 (2020). https://arxiv.org/abs/2008.08621

[3] R. P. Stanley, *Two poset polytopes*, Discrete & Computational Geometry **1** (1986), 9–23. https://doi.org/10.1007/BF02187680

[4] F. Kohl, M. Olsen, and R. Sanyal, *Unconditional Reflexive Polytopes*, Discrete & Computational Geometry **64** (2020), 427–452, especially Sections 3 and 8.1. https://doi.org/10.1007/s00454-020-00199-8
