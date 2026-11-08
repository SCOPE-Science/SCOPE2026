# Exact Euclidean inballs and balanced-facet contacts of star PQ adjacency polytopes

## Finding

Let \(m\ge1\) be an integer and let \(G=K_{1,m}\) have hub \(0\) and leaves \(1,\ldots,m\). The standard PQ-type adjacency polytope is
\[
P_m=\operatorname{conv}\{(e_i,e_j):\ i=j\ \text{or}\ \{i,j\}\in E(G)\}\subset\mathbb R^{2(m+1)}.
\]
It has affine dimension \(2m\), measured with the Euclidean metric inherited from its affine hull. Define
\[
a_m=\sqrt{\frac{m}{m+1}},\qquad b_m=\sqrt{\frac{m+2\lfloor m^2/4\rfloor}{m+1}},\qquad
r_m=\frac{1}{ma_m+b_m},\qquad t_m=a_mr_m.
\]
**Theorem.** The intrinsic Euclidean inradius of \(P_m\) is exactly \(r_m\). Its unique incenter has coordinates
\[
x_0=y_0=1-mt_m,\qquad x_i=y_i=t_m\quad(1\le i\le m).
\]
There are exactly \(2m+2^m\) facets. Exactly the \(2m\) leaf nonnegativity facets and the upper facets with balanced leaf-selection size touch the maximal inball. The number of tangent facets is
\[
T_m=2m+\begin{cases}
\binom{m}{m/2},&m\ \text{even},\\
2\binom{m}{(m-1)/2},&m\ \text{odd}.
\end{cases}
\]
In particular, \(mr_m\to1\) as \(m\to\infty\), while the proportion of upper facets tangent to the optimal inball is of order \(m^{-1/2}\) and has an explicit parity dependence.

## Assumptions and scope

The graph is the **unweighted star** on \(m+1\) vertices; each generator is the ordered incidence pair \((e_i,e_j)\), including diagonal pairs. The polytope lies in the affine subspace \(\sum_{i=0}^m x_i=\sum_{i=0}^m y_i=1\). All balls and normal lengths use the restriction of the **standard** Euclidean inner product on \(\mathbb R^{2(m+1)}\), not the Euclidean metric on a nonorthonormal leaf-coordinate chart. The theorem is valid for each integer \(m\ge1\), including the square case \(m=1\).

## Proof

**1. An exact and irredundant facet description.** Use leaf variables \(u_i=x_i\), \(v_i=y_i\), with hub coordinates \(x_0=1-\sum_i u_i\), \(y_0=1-\sum_i v_i\). The generators become the origin and, for each leaf \(i\), the three vectors with leaf pair \((u_i,v_i)\) equal to \((1,0),(0,1),(1,1)\) and all other pairs zero.

Consequently,
\[
P_m=\left\{u_i,v_i\ge0\ (1\le i\le m),\qquad
\sum_{i=1}^m\max(u_i,v_i)\le1\right\}.
\]
The forward inclusion follows from convexity of the sum of maxima and inspection of the generators. Conversely, suppose the displayed inequalities hold and put \(\lambda_i=\max(u_i,v_i)\). If \(u_i\ge v_i\), write its contribution as \((u_i-v_i)(1,0)+v_i(1,1)\); otherwise write it as \((v_i-u_i)(0,1)+u_i(1,1)\). The coefficients sum to \(\lambda_i\). Put the remaining nonnegative coefficient \(1-\sum_i\lambda_i\) on the origin. This proves the reverse inclusion.

The equivalent linear facet description is
\[
u_i\ge0,\quad v_i\ge0,\qquad
L_S(u,v):=\sum_{i\in S}u_i+\sum_{i\notin S}v_i\le1\quad(S\subseteq[m]).
\]
Every displayed inequality is an actual facet. For a lower inequality, set its coordinate to zero and choose every other leaf coordinate equal to a sufficiently small positive number; the resulting point is strict in all other inequalities. For a chosen \(L_S\), set every one of its \(m\) selected leaf coordinates to \(1/m\) and each unselected coordinate to a common \(\delta\in(0,1/m)\). Then \(L_S=1\), all leaf coordinates are positive, and every other upper inequality is strict. Since the polytope contains a full-dimensional point with all leaf coordinates small and positive, these witnesses prove irredundancy and the count \(2m+2^m\).

**2. The intrinsic facet-normal lengths.** The translation space of the affine hull is the orthogonal direct sum of two copies of \(\mathbf1^\perp\subset\mathbb R^{m+1}\). An individual standard coordinate normal, after projection to this translation space, has norm
\[
a_m=\sqrt{1-\frac1{m+1}}.
\]
For \(L_S\), write \(s=|S|\). Its normal has \(s\) ones in the first block and \(m-s\) ones in the second. Its squared projected norm is therefore
\[
\left(s-\frac{s^2}{m+1}\right)+\left(m-s-\frac{(m-s)^2}{m+1}\right)
=\frac{m+2s(m-s)}{m+1}.
\]
The maximum occurs precisely for \(s\in\{\lfloor m/2\rfloor,\lceil m/2\rceil\}\) and equals \(b_m^2\).

**3. Global optimality and the radius.** The leaf-permutation group together with the isometry swapping the two coordinate blocks acts on \(P_m\). If any closed intrinsic ball of radius \(r\) is contained in \(P_m\), averaging its center over this finite isometry group gives a center for another contained ball of the same radius: each facet condition is affine in its center and has the same required distance margin. Thus an optimal center may be taken with \(u_i=v_i=t\) for all leaves.

At that center the distances to the lower facets are \(t/a_m\). The nearest upper facets are the balanced ones, at distance \((1-mt)/b_m\). The permitted range is \(0\le t\le1/m\), and the minimum of these two quantities is maximized at their intersection. Solving
\[
\frac{t}{a_m}=\frac{1-mt}{b_m}
\]
gives \(t=t_m\) and radius \(r=r_m\). It proves global optimality because averaging does not reduce any feasible ball radius, and the symmetric optimization has been solved exactly.

**4. Uniqueness and all contacts.** Let any other center support a ball of radius \(r_m\). Each lower facet forces \(u_i,v_i\ge a_mr_m=t_m\). For every balanced \(S\), its projected normal has norm \(b_m\), so its containment inequality forces
\[
L_S(u,v)\le1-b_mr_m=mt_m.
\]
But its \(m\) selected coordinates are individually at least \(t_m\); therefore all those selected coordinates equal \(t_m\). Every one of the \(2m\) leaf variables appears as a selected coordinate in at least one balanced subset, including when \(m=1\). Thus every variable equals \(t_m\), proving **uniqueness**. At this center every lower facet is tangent. The upper facet \(S\) is tangent exactly when its projected normal has length \(b_m\), which is equivalent to balanced \(|S|\). Counting those subsets gives the stated formula.

Finally, \(a_m\to1\) and \(b_m=O(\sqrt m)\), hence \(m/(ma_m+b_m)\to1\). Stirling's formula yields the asserted contact-fraction order, with the even and odd cases differing by a factor asymptotically two.

## Verification

The accompanying `check_pqstar.py` reconstructs the original \(3m+1\) generator vectors and the genuine orthonormal affine translation space. For each \(1\le m\le12\), it solves the full Chebyshev-center linear program, compares the optimum against the exact formula, and checks each asserted facet contact. For \(m\le4\) it also constructs the convex hull independently from the vertices and optimizes using those hull hyperplanes. An executed run returned `PQ_STAR_INTRINSIC_INBALL_LP_CHECKS_PASSED 12`. These finite numerical tests supplement, but do not prove, the all-\(m\) theorem established above; a numerical tolerance is used by the checker.

## Relationship to prior work

Davis and Chen studied PQ-type adjacency polytopes and their normalized volumes by draconian sequences (arXiv:2007.11051, first public version July 21, 2020), including families of forests. Ohsugi and Tsuchiya studied PQ-type adjacency polytopes of join graphs (arXiv:2103.15045, first public version March 28, 2021), including complete bipartite graph examples. Those papers establish the graph-polytope framework and lattice-enumerative invariants; their inspected definitions and forest/join/complete-bipartite results do not give the present intrinsic Euclidean inradius, unique incenter, or balanced-facet contact classification. Related metric statements about star **symmetric-edge** and **cosmological** polytopes use different vertex constructions and cannot be transferred by a general Euclidean isometry. The present formula is therefore an independently derived metric statement, with historical priority still subject to broader literature verification.

## Limitations

The theorem treats stars in the canonical PQ-type ordered-pair embedding, not arbitrary graphs, weighted generators, or affinely equivalent root-polytope embeddings. The unimodular equivalence between PQ-type and certain bipartite root polytopes does not in general preserve Euclidean distances. Independent mathematical audit has not been performed. Earlier work under alternative names for convex hulls of coordinate-square supports could contain a related geometric formula; a negative literature search alone does not establish priority.

## References

1. R. Davis and T. Chen, *Computing Volumes of Adjacency Polytopes via Draconian Sequences*, arXiv:2007.11051 (2020), https://arxiv.org/abs/2007.11051.
2. H. Ohsugi and A. Tsuchiya, *PQ-type Adjacency Polytopes of Join Graphs*, arXiv:2103.15045 (2021), https://arxiv.org/abs/2103.15045.
