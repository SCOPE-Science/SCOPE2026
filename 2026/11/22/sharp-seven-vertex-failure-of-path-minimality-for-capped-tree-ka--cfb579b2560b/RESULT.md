# Sharp seven-vertex failure of path minimality for capped-tree Katětov type counts

## Finding

Let \(T\) be any finite tree on \(n\geq1\) individually named vertices. Equip these vertices with the metric \(d_T(u,v)=\min\{\operatorname{dist}_T(u,v),3\}\), and regard this as a parameter subspace of the countable universal homogeneous metric space with positive distances \(\{1,2,3\}\). Let \(N(T)\) count complete nonalgebraic singleton types over this named subspace. Write \(d_v\) for the graph degree of vertex \(v\), \(r_v=2^{-d_v}\), and, for each vertex \(c\),
\[
R_c=\prod_{v\sim c}(1+r_v)-1-\sum_{v\sim c}r_v,\qquad
Q_c=\prod_{v\sim c}(1+2r_v)-1-2\sum_{v\sim c}r_v.
\]
Then the following **local degree-neighborhood identity** holds for *every* finite tree:
\[
\boxed{\frac{N(T)}{2^n}=1+\sum_{v\in V(T)}2^{-d_v-1}
+\sum_{uv\in E(T)}2^{-d_u-d_v}
+\frac12\sum_{c\in V(T)}\bigl(R_c+2^{-d_c}Q_c\bigr).}\tag{1}
\]
In particular, the type count depends only on vertex degrees and the multisets of degrees of their respective neighbors, rather than on the complete tree geometry.

For every \(1\le n\le6\), the path \(P_n\) uniquely minimizes \(N(T)\) among all trees on \(n\) vertices, up to isomorphism (the statement is trivial for \(n\le3\)). **The first failure of path minimality is exactly at \(n=7\):** the unique minimizer there is the subdivided three-star \(E_7\) with arm lengths \((2,2,2)\), and
\[
N(E_7)=384<392=N(P_7).
\]
Moreover, for every \(n\ge8\), let \(E_n\) be the three-arm tree whose arm lengths are \((2,2,n-5)\). Then
\[
\boxed{N(P_n)=(4n+21)2^{n-4},\qquad N(E_n)=(8n+41)2^{n-5},\qquad N(P_n)-N(E_n)=2^{n-5}>0.}\tag{2}
\]
Thus the path fails to minimize this natural logical extension invariant at **every** order \(n\ge7\). The theorem does **not** claim that \(E_n\) is a global minimizer for \(n\ge8\).

## Assumptions and scope

The ambient space is the Fraïssé limit of all finite metric spaces with distances in \(\{0,1,2,3\}\). Every finite \(d_T\) embeds in it, and every Katětov distance vector to the named parameters is realized. A nonalgebraic singleton type has a strictly positive distance vector \(f:V(T)\to\{1,2,3\}\), which must satisfy
\[
|f(u)-f(v)|\le d_T(u,v)\le f(u)+f(v)\qquad(u\ne v).
\]
The count \(N(T)\) treats all vertices as separately named, and counts logical types, not random points or metric isometry orbits of the old tree. The graph distance in \(d_T\) is capped at three; it is **not** the alternative metric assigning distance two to every nonedge of a tree.

## Proof

**1. Admissible supports.** For positive old distances \(1,2,3\), the only forbidden unordered pairs of new distances are \((1,3)\) on an old distance-one pair and \((1,1)\) on an old distance-three pair. An old distance-two pair imposes no restriction. Put \(S=f^{-1}(1)\). The second prohibition says that every two distinct vertices in \(S\) have tree distance at most two. The first says that every tree neighbor of \(S\) not already in \(S\) must have new distance two. Every other parameter may independently receive new distance two or three. Hence, with \(N_T[S]\) denoting the closed tree neighborhood of \(S\),
\[
\boxed{N(T)=2^n+\sum_{\substack{\varnothing\ne S\subseteq V(T)\\ \operatorname{diam}_T(S)\le2}}2^{n-|N_T[S]|}.}\tag{3}
\]
The first term is the empty distance-one support. This also proves every counted vector satisfies all metric triangle inequalities, so none is lost or duplicated.

**2. Unique-center decomposition.** In a tree, every support \(S\) of size at least three and diameter at most two has a unique center \(c\), with \(S\subseteq\{c\}\cup N_T(c)\). A distance-two pair has its unique central vertex as well. Partition the supports into singletons, adjacent pairs, and the following two families attached to a unique center \(c\): \(S=A\) for \(A\subseteq N_T(c)\) of size at least two, and \(S=\{c\}\cup A\) for such \(A\). The latter family contains supports of size at least three, so there is no overlap with adjacent pairs.

A singleton \(\{v\}\) has closed neighborhood size \(1+d_v\); an adjacent pair \(\{u,v\}\) has closed neighborhood size \(d_u+d_v\). For the two centered families respectively, the sizes are
\[
|N_T[A]|=1+\sum_{v\in A}d_v,\qquad
|N_T[\{c\}\cup A]|=1+d_c+\sum_{v\in A}(d_v-1).
\]
These equalities follow from absence of triangles and four-cycles in a tree: the branches beyond the selected neighbors are disjoint. Summing their powers of two in (3), and using
\[
\sum_{\substack{A\subseteq N_T(c)\\|A|\ge2}}\prod_{v\in A}q_v
=\prod_{v\sim c}(1+q_v)-1-\sum_{v\sim c}q_v,
\]
proves (1) exactly.

**3. A tail-extension identity.** Define \(F(T)=N(T)/2^{|V(T)|}\). Suppose a leaf \(v_3\) is reached by a pendant path \(v_0v_1v_2v_3\), with \(d_{v_1}=d_{v_2}=2\). Form \(T'\) by attaching a fresh leaf \(v_4\) to \(v_3\). In (1), only vertex terms at \(v_3,v_4\), edge terms at \(v_2v_3,v_3v_4\), and the centered terms at \(v_2,v_3\) change. Their respective net changes are
\[
\underbrace{\frac18}_{\text{vertex terms}}
+\underbrace{\frac1{16}}_{\text{edge terms}}
+\underbrace{\left(-\frac1{16}+\frac18\right)}_{\text{centered terms}}
=\boxed{\frac14}.
\]
The calculation is independent of the geometry beyond \(v_1\). Hence \(F(T')=F(T)+\frac14\). Direct substitution into (1) gives \(N(P_4)=37\), \(N(E_8)=840\), and \(N(E_7)=384\). Repeated tail extension yields
\[
F(P_n)=\frac{n}{4}+\frac{21}{16}\quad(n\ge4),\qquad
F(E_n)=\frac{n}{4}+\frac{41}{32}\quad(n\ge8),
\]
which is exactly (2). The isolated seven-vertex value yields \(N(P_7)-N(E_7)=8\).

**4. Sharp initial threshold.** For completeness, all labeled trees through seven vertices were enumerated by Prüfer sequences. Every labeled tree on \(n\ge2\) vertices has exactly one sequence of length \(n-2\), and (1) evaluates it using only its adjacency list, with exact rational arithmetic. The smallest observed values and numbers of labeled minimizers were:

| \(n\) | Minimum \(N(T)\) | Labeled minimizers |
|---:|---:|---:|
| 1 | 3 | 1 |
| 2 | 7 | 1 |
| 3 | 17 | 3 |
| 4 | 37 | 12 |
| 5 | 82 | 60 |
| 6 | 180 | 360 |
| 7 | 384 | 840 |

The code verifies the exact structure of every minimizing labeled tree: all minimizers with \(4\le n\le6\) have path degree sequence, and every seven-vertex minimizer has a unique degree-three center with its three leaves at distance two, hence is \(E_7\). These match respectively the \(n!/2\) labelings of paths for \(n\ge3\) and the \(7!/6=840\) labelings of \(E_7\), so no competing tree was omitted. This exhaustive finite comparison establishes the sharpness of seven, not merely an empirical guess. The supplied script independently checks raw Katětov inequalities on additional instances.

## Verification

The standalone standard-library script `artifacts/verify.py` computes (a) raw distance-vector counts by all triangle inequalities, (b) the diameter-two-support formula (3), and (c) the rational neighbor-degree formula (1) via independent implementations. It compares all three for 154 instances, exhaustively evaluates the \(n^{n-2}\) labeled trees at every order \(n\le7\), checks the identity and equality structures, and tests (2) at all orders \(8\le n\le80\). The recorded run in `artifacts/verify_output.txt` ends in `VERIFY_OK`. These finite tests do not replace the all-order proof in paragraphs 1–3.

## Relationship to prior work

Sauer's 2010 paper supplies the homogeneous finite-distance metric context, the Katětov inequalities and their realization by the ambient space; none of these foundational facts is claimed as new. A prior exact calculation for capped-metric paths and cycles already establishes the path specialization \(N(P_n)=(4n+21)2^{n-4}\) for \(n\ge5\); **that path formula alone is not claimed as new**. Its hypotheses restrict components to paths and cycles, so it does not determine the three-armed tree count, the all-tree degree-neighborhood identity (1), or the first tree-order failure. The published 2026 Widom–Rowlinson/type-polynomial result specializes instead to metrics with old distances **only one or two**. Here old distance three introduces a nonlocal prohibition on two distance-one labels, and the weighted support formula (3) is different. In particular a capped-tree metric cannot be identified with that \(\{1,2\}\)-graph metric once the underlying tree has diameter at least three.

Csikvári and Lin's 2014 tree-homomorphism paper records a seven-vertex three-spider obstruction to universal *graph-homomorphism* path minimality (Remark 4.13), using a specially constructed target graph. The shape \(E_7\) is therefore **not** claimed as a new graph. Their theorem for homomorphisms into a path likewise concerns a different, edge-local functional. The contribution here is the exact **three-distance Katětov type count**, its all-tree local formula, the first sharp tree-order comparison and the infinite numerical gap (2). Existing results about homomorphisms of a tree into a fixed graph do not directly supply it, because a distance-three pair in our metric imposes a condition on nonadjacent vertices of the tree.

## Limitations

This theorem treats only nonalgebraic singleton types over pointwise-named capped *unit-edge tree* metrics and positive distance set \(\{1,2,3\}\). It does not identify the global minimizers for \(n\ge8\), address arbitrary finite metric bases or higher-arity types, or claim that the seven-vertex tree itself is newly discovered. The sharp finite threshold is certified by complete enumeration through seven; the infinite counterfamily is proved analytically. Historical novelty beyond the inspected sources remains subject to independent literature assessment and independent mathematical audit.

## References

1. N. W. Sauer, *Partitions of metric spaces with finite distance sets*, arXiv:1010.4212, first posted 2010-10-20; especially §2, Katětov function criterion and extension theorem. https://arxiv.org/abs/1010.4212
2. P. Csikvári and Z. Lin, *Graph Homomorphisms between Trees*, Electronic Journal of Combinatorics 21(4) (2014), #P4.9, arXiv:1307.6721 first posted 2013-07-25; Theorem 1.4 and Remark 4.13. https://www.combinatorics.org/ojs/index.php/eljc/article/download/v21i4p9/pdf/
3. *Widom–Rowlinson partition functions as 1-type polynomials of the generic diameter-3 metric space*, publicly accessible research result (2026), specializing to old distances one and two. https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-widom-rowlinson-partition-functions-as-1-type-polynomials-of-the--ec80747a5989
