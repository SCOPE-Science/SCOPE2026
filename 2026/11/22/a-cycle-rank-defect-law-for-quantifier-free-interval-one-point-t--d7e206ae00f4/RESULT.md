# A cycle-rank defect law for quantifier-free interval one-point types

## Finding

Let \(m\ge1\), and fix a family \(I_1,\ldots,I_m\) of nondegenerate closed real intervals, with pairwise distinct endpoints and with no interval containing another. Number them by increasing left endpoint, so their right endpoints also increase. Let \(H\) be their intersection graph, let \(e=|E(H)|\), and let \(c\) be its number of connected components. For every additional nondegenerate closed interval \(J\), define its **nonalgebraic adjacency type** over these named parameters by
\[
 S_J=\{i\in\{1,\ldots,m\}:J\cap I_i\ne\varnothing\}.
\]
The new interval is unrestricted: the enlarged representation is only required to be an interval graph, not another proper-interval representation. Distinct sets \(S_J\) are precisely the quantifier-free adjacency patterns of a new point in interval-graph extensions of this fixed representation (equality to a parameter is excluded).

**Exact characterization.** Every nonempty \(S_J\) is a consecutive block \([i,j]=\{i,i+1,\ldots,j\}\), and that block is attainable if and only if
\[
 i=1\quad\text{or}\quad j=m\quad\text{or}\quad \{i-1,j+1\}\notin E(H).
\]
The empty pattern is always attainable.

**Graded one-point spectrum.** Put \(T_I(z)=\sum_{S_J\text{ distinct}} z^{|S_J|}\). Then
\[
 T_I(z)=1+\sum_{t=1}^{m}(m-t+1)z^t
 -\sum_{\substack{1\le a<b\le m\\ b\ge a+2,\ \{a,b\}\in E(H)}} z^{b-a-1}.
\]
Consequently the total number \(N(I)=T_I(1)\) is an invariant of the base graph, not merely its chosen representation, and satisfies
\[
 \boxed{N(I)=1+\binom{m+1}{2}-(e-m+c).}
\]
Thus the exact defect from the full interval-block bound is the graph's cycle-space dimension \(e-m+c\). The full bound is achieved exactly when \(H\) is a disjoint union of paths.

## Assumptions and scope

All base intervals are closed, have positive length, have distinct endpoints, and form a **proper** family (no proper containments). These hypotheses ensure both endpoint lists are strictly increasing in the same order. The domain of one-point types consists of **new vertices**, rather than the existing named parameters; each new vertex is an arbitrary interval, including intervals containing several parameter intervals. New vertices can be introduced independently, and the theorem does not require their mutual disjointness, that all such types coexist in a proper-interval extension, or any logical equivalence at positive quantifier rank.

The empty neighborhood and all realizable nonempty neighborhoods are counted once each. The trace variable \(z\) grades by the number of parameters adjacent to the new vertex. The formula does not count possible interval representations or labeled extensions; it counts distinct quantifier-free patterns of the adjacency relation with the named parameters.

## Proof

Write \(I_i=[\ell_i,r_i]\). Properness and the distinct-endpoints assumption give
\[
 \ell_1<\cdots<\ell_m,\qquad r_1<\cdots<r_m.
\]
Let \(J=[u,v]\). The intersection condition is exactly \(u\le r_i\) and \(v\ge\ell_i\). Each of these two inequalities defines respectively a suffix and a prefix in the common index order, so their intersection is an interval of indices, possibly empty. This proves the consecutive-block assertion.

Suppose the nonempty block \([i,j]\) occurs. If \(i>1\), exclusion of the preceding interval forces \(u>r_{i-1}\); if \(j<m\), exclusion of the following interval forces \(v<\ell_{j+1}\). Since \(u\le v\), interior blocks require \(r_{i-1}<\ell_{j+1}\), which is precisely nonadjacency of their two flanking vertices.

Conversely, for an interior block with \(r_{i-1}<\ell_{j+1}\), choose \(u,v\) such that
\[
 r_{i-1}<u<r_i,\qquad \ell_j<v<\ell_{j+1},\qquad u<v.
\]
Such a choice exists because \(r_{i-1}<\min\{r_i,\ell_{j+1}\}\), \(\ell_j<\ell_{j+1}\), and \(\ell_j<r_j\) with \(r_i\le r_j\). More directly, pick \(u\) immediately to the right of \(r_{i-1}\), \(v\) immediately to the left of \(\ell_{j+1}\), and enlarge their overlap where necessary until they both intersect \(I_i\) and \(I_j\); the strict inequalities allow this. By monotonicity, their intersection set is exactly \([i,j]\). For a boundary block, omit the corresponding flank constraint and extend the free endpoint far outside all base intervals. A distant interval realizes the empty block.

Among the \(m-t+1\) blocks of size \(t\), an interior block \([i,j]\) is absent exactly when its flanking pair \((a,b)=(i-1,j+1)\) is an edge. The map is a bijection from missing nonempty blocks to edges of \(H\) whose endpoint indices differ by at least two; it also gives \(t=b-a-1\). Removing their monomials from the all-block polynomial gives the graded identity.

It remains to count the short edges. In a proper interval graph, consecutive indexed vertices belong to the same connected component exactly when their intervals intersect: if \(r_i<\ell_{i+1}\), every earlier interval ends no later than \(r_i\), and every later interval begins no earlier than \(\ell_{i+1}\), so no edge crosses this cut. Therefore each component is an interval of indices, and its adjacent index pairs are all edges. There are exactly \(m-c\) such short edges. The number of nonconsecutive edges is \(e-(m-c)=e-m+c\), proving the total-count identity.

Finally, this defect vanishes exactly when \(H\) is a forest. A proper interval graph cannot contain an induced claw: the three pairwise-disjoint leaf intervals could not all meet their common central interval without one leaf being contained in another or violating the endpoint ordering. Every interval graph is chordal (a cycle of length at least four has a chord). Hence a proper interval graph that is a forest is claw-free and has maximum degree at most two, so each component is a path. Conversely, disjoint unions of paths clearly have zero cycle rank. This proves the equality characterization.

## Verification

The bundled `verify.py` independently enumerates all intervals on a doubled integer-endpoint grid, aggregates their actual adjacency patterns, and compares the complete graded polynomial with the theorem. It checks every proper perfect-matching interval configuration with up to five base intervals, plus deterministic pseudorandom proper configurations with six through nine base intervals. Running `python verify.py` prints `VERIFY_OK 544`. These finite computations test the formula but do not establish it for unbounded \(m\); the proof above supplies the universal argument.

For instance, on a three-vertex path \(T_I(z)=1+3z+2z^2+z^3\) (seven types), while on a three-vertex clique \(T_I(z)=1+2z+2z^2+z^3\) (six types): the missing singleton corresponds to the nonconsecutive edge.

## Relationship to prior work

Dreier, Mählmann and Toruńczyk (2026) motivate controlling finite quantifier-rank type spectra in structural model theory and establish broad polynomial type bounds for monadically dependent classes; their theorem does not give the present fixed-base exact adjacency-type polynomial. Berthe, Foucaud, Lehtilä and Parreau (2026) derive tight neighborhood-complexity bounds for bounded treewidth/pathwidth classes, rather than this representation-independent cycle-space defect for proper interval bases.

Foucaud, Mertzios, Naserasr, Parreau and Valicov (2015, Section 2, Theorem 5) already prove the consecutive-block bound for interval-graph neighborhoods and show its sharpness. Bousquet, Lagoutte, Li, Parreau and Thomassé (2015) give interval-graph VC-dimension bounds, which also imply polynomial trace growth. **Neither generic quadratic growth nor consecutiveness is claimed as new.** The distinct contribution asserted here is the exact *base-graph-dependent missing-flank-edge bijection*, its full graded spectrum, and the resulting identity with cycle rank for arbitrary proper base families. An earlier equivalent formula in the interval-neighborhood literature remains a genuine priority risk.

## Limitations

The one-point extension permits intervals of arbitrary length; it is **not** a theorem about extensions required to remain proper/unit interval graphs. It is an extension-type count, **not** the count of neighborhoods already represented by vertices of the base graph. The graded formula uses a selected proper ordering; only the ungraded count is asserted to be graph-intrinsic here. The relation between this identity and earlier interval identifying-code literature should receive independent historical verification. Endpoints are assumed distinct; perturbations can address many degenerate representations but are not part of the stated theorem.

## References

1. J. Dreier, N. Mählmann and S. Toruńczyk, *First-Order Model Checking on Monadically Dependent Graph Classes*, arXiv:2611.08143v1, first submitted 2026-11-05. https://arxiv.org/abs/2611.08143
2. G. Berthe, F. Foucaud, T. Lehtilä and A. Parreau, *Neighbourhood complexity and identification problems for graphs of bounded treewidth and pathwidth*, arXiv:2607.16889v1, first submitted 2026-07-18. https://arxiv.org/abs/2607.16889
3. F. Foucaud, G. B. Mertzios, R. Naserasr, A. Parreau and P. Valicov, *Identification, location-domination and metric dimension on interval and permutation graphs. I. Bounds*, arXiv:1507.08164v1, first submitted 2015-07-29, especially Section 2, Theorem 5 and Proposition 6. https://arxiv.org/abs/1507.08164
4. N. Bousquet, A. Lagoutte, Z. Li, A. Parreau and S. Thomassé, *Identifying codes in hereditary classes of graphs and VC-dimension*, arXiv:1407.5833v1, first submitted 2014-07-22. https://arxiv.org/abs/1407.5833
