# Exact capacity-limited domination profile of crown graphs

## Finding

Let \(n\ge3\), \(1\le k\le n-2\), and \(r=n-1-k\). The **crown graph** \(\operatorname{Cr}_n\) has named vertices \(a_1,\ldots,a_n,b_1,\ldots,b_n\) and edges \(a_i b_j\) exactly when \(i\ne j\). A subset \(D\) is **\(k\)-limited dominating** if each vertex outside \(D\) has a neighbour in \(D\), and each vertex in \(D\) has at most \(k\) neighbours outside \(D\). Put \(I=\{i:a_i\in D\}\), \(J=\{j:b_j\in D\}\), \(x=|I|\), and \(y=|J|\).

**Exact structural classification.** Such a \(D\) is \(k\)-limited dominating if and only if \(x,y\ge2\) and one of the following two, disjoint alternatives holds:

1. \(I\cap J=\varnothing\) and \(x,y\ge r\).
2. \(I\cap J\ne\varnothing\) and \(x,y\ge r+1\).

Consequently the full bivariate cardinality enumerator is
\[
\mathcal L_{n,k}(u,v)
=\sum_{x=2}^{n}\sum_{y=2}^{n}
\binom nx\left[
\mathbf 1_{\{x,y\ge r\}}\binom{n-x}{y}
+\mathbf 1_{\{x,y\ge r+1\}}\left(\binom ny-\binom{n-x}{y}\right)
\right]u^xv^y.
\]
Here a binomial coefficient is zero if its lower index is outside its usual range. The coefficient of \(u^xv^y\) is the number of actual vertex-labelled feasible sets containing exactly \(x\) vertices from the first shore and \(y\) from the second. In particular, \(\mathcal L_{n,k}(z,z)\) counts feasible sets of every size.

Writing \(\gamma_k^{\mathrm L}\) for minimum \(k\)-limited domination cardinality and \(N_{n,k}\) for the number of minimum sets, one has
\[
(\gamma_k^{\mathrm L}(\operatorname{Cr}_n),N_{n,k})=
\begin{cases}
\left(4,\binom n2^2\right),&r=1,\\[2pt]
\left(2r,\binom nr\binom{n-r}{r}\right),&r\ge2,\ n\ge2r,\\[2pt]
\left(2r+2,\binom n{r+1}^{2}\right),&r\ge2,\ n<2r.
\end{cases}
\]
The minimum sets in the three cases are exactly: any \(x=y=2\) shore selections; disjoint \(r\)-subsets \(I,J\); and arbitrary \((r+1)\)-subsets \(I,J\), respectively. In the third case intersection is forced by \(n<2r\).

For comparison, the complete bipartite graph satisfies \(\gamma_k^{\mathrm L}(K_{n,n})=2(n-k)=2(r+1)\) in this domain. Hence deleting the entire perfect matching lowers this minimum by **exactly two** if and only if \(r\ge2\) and \(n\ge2r\); otherwise the minimum does not change. For every \(n\ge4\), the gain disappears at the upper boundary \(k=n-2\). For each fixed \(n\ge5\), the gain is non-monotone as \(k\) varies over its admissible range.

## Assumptions and scope

All graphs are finite, simple and undirected. Vertices and matching indices are distinguished; no quotient by permutations or graph automorphisms is taken. The theorem covers every integer \(n\ge3\) and every integer \(1\le k\le n-2\), which is precisely the nontrivial positive capacity range below \(\Delta(\operatorname{Cr}_n)=n-1\). The enumerator concerns all feasible sets, not only inclusion-minimal sets. The minimum multiplicities count distinct vertex subsets.

## Proof

**1. Both shores contain at least two selected vertices.** If \(I=\varnothing\), then no selected vertex in the second shore can satisfy the capacity constraint: each has all \(n-1>k\) neighbours outside the set. The empty set itself is not dominating. Suppose \(I=\{i\}\). If \(i\notin J\), the unselected vertex \(b_i\) has no selected neighbour (its only possible selected neighbour would be \(a_i\), but \(a_ib_i\) is a missing edge). If \(i\in J\), the selected vertex \(b_i\) has all \(n-1>k\) of its neighbours outside the set, again impossible. By symmetry, \(|I|,|J|\ge2\).

**2. Domination becomes automatic; capacity depends only on intersection.** With \(x,y\ge2\), any unselected \(a_i\) sees at least \(y-1\ge1\) selected vertices \(b_j\), and similarly every unselected \(b_j\) sees a selected \(a_i\). For a selected \(a_i\), exactly
\[
|N(a_i)\setminus D|=n-1-y+\mathbf 1_{\{i\in J\}},
\]
and for selected \(b_j\), exactly
\[
|N(b_j)\setminus D|=n-1-x+\mathbf 1_{\{j\in I\}}.
\]
If \(I\cap J=\varnothing\), every indicator is zero on the selected vertices; both capacity conditions reduce to \(x,y\ge r\). If \(I\cap J\ne\varnothing\), there is at least one selected vertex on each shore whose indicator is one, and then both conditions are equivalent to \(x,y\ge r+1\). These conditions are sufficient for every selected vertex since its indicator never exceeds one. This proves the classification without reliance on an experiment.

**3. Count all feasible sets.** For fixed \(x,y\), the number of ordered choices of index subsets \((I,J)\) with \(I\cap J=\varnothing\) is \(\binom nx\binom{n-x}{y}\). The number with nonempty intersection is \(\binom nx\binom ny-\binom nx\binom{n-x}{y}\). Multiplication by the two sharp feasibility indicators and summation gives the polynomial. The two classes are disjoint and exhaust all feasible sets, so no multiplicity correction is needed.

**4. Determine the minimum and every equality case.** When \(r=1\), both alternatives together admit precisely all \(x,y\ge2\). The minimum is \(4\), attained by all pairs of two-element shore subsets. Suppose \(r\ge2\). If \(n\ge2r\), disjoint \(r\)-subsets exist and give size \(2r\). Every feasible set has size at least \(2r\), with equality only for \(x=y=r\), which forces disjointness. Thus their number is \(\binom nr\binom{n-r}{r}\). If \(n<2r\), no feasible disjoint pair exists because it would have \(x+y\ge2r>n\). Every feasible set therefore meets both shores in at least \(r+1\) selected vertices, and any two \((r+1)\)-subsets of the \(n\)-element index set intersect because \(2(r+1)>n\). This proves the lower bound \(2r+2\), its attainability and its multiplicity \(\binom n{r+1}^2\).

**5. Matching deletion contrast.** In \(K_{n,n}\), any selected vertex on the first shore sees all \(n-y\) unselected second-shore vertices, and vice versa. Since \(k\le n-2\), each shore must contain selected vertices; the capacity inequalities give \(x,y\ge n-k=r+1\), which also ensure domination. Therefore the minimum equals \(2(r+1)\). Subtracting the three cases above gives the claimed exact difference.

## Verification

Run `python3 artifacts/verify.py` after extracting the file from this package. The program independently constructs the adjacency masks of \(\operatorname{Cr}_n\), inspects every subset of its \(2n\) vertices for \(3\le n\le8\) and every \(1\le k\le n-2\), and compares its bivariate counts and minima against the closed formulas. It then checks the coefficient-derived minimum/multiplicity and matching-deletion gap through \(n=60\). Expected concluding lines: `ALL_COEFFICIENT_MINIMA_AND_MATCHING_DELETION_GAP_OK n=3..60` and `VERIFY_OK`. This finite replay supports but does not replace the general proof in the preceding section.

Representative values are \(\gamma_1^{\mathrm L}(\operatorname{Cr}_4)=4\) with \(6\) minimum sets, \(\gamma_1^{\mathrm L}(\operatorname{Cr}_5)=8\) with \(25\) minimum sets, and \(\gamma_2^{\mathrm L}(\operatorname{Cr}_5)=4\) with \(30\) minimum sets.

## Relationship to prior work

Božović, Radić, Kovijanić-Vukićević and Tepeh introduced systematic \(k\)-limited domination and explicitly determined \(\gamma_k^{\mathrm L}(K_{m,n})\) (Proposition 2(iv)), as well as the general equivalence to \((1,d-k)\)-domination in \(d\)-regular graphs. Those results provide the complete-bipartite baseline and an equivalent vocabulary, but do not enumerate the feasible sets of matching-deleted \(K_{n,n}\) or establish the crown-graph threshold. Their accessible arXiv manuscript and open-access journal text were compared at the level of definitions and results, including sections on exact families, regular graphs and packing. The earlier pitchfork terminology also includes the \((0,k)\) constraint, but the located records did not establish the stated crown-graph distribution.

Relevant prior exact studies of crown graphs concern different domination predicates (restrained, Roman, weakly connected two-domination, or singleton rainbow). None of those predicates implies the enumerator above. The distinguishing novelty is the complete bivariate classification and the sharp matching-deletion phase boundary, not the general \(k\)-limited definition or the complete-bipartite baseline.

## Limitations

No formula is claimed here for arbitrary deleted matchings, unequal shore sizes, \(k=0\), or \(k\ge n-1\). The theorem does not classify inclusion-minimal feasible sets. Historical priority is provisional: searchable records are not an exhaustive mathematical bibliography, and some related material (linked mathematical records and adjoining 2026 manuscripts) was available only through abstracts, indices or secondary descriptions. No independent mathematical audit or external certification has been performed.

## References

1. D. Božović, G. Radić, Ž. Kovijanić-Vukićević, A. Tepeh, *On \(k\)-limited domination in graphs*, arXiv:2606.22422, first submitted 2026-06-21, https://arxiv.org/abs/2606.22422 ; open-access publication, *Computational and Applied Mathematics*, https://doi.org/10.1007/s40314-026-03902-2 (published 2026-09-11). Proposition 2(iv), regular-graph relation, and conclusions were compared.
2. A. Tepeh, *On \(k\)-limited domination: complexity and Cartesian products*, arXiv:2606.22428, https://arxiv.org/abs/2606.22428 . Its product emphasis is distinct from crown-graph enumeration.
3. M. N. Al-Harere, M. A. Abdlhusein, *Pitchfork domination in graphs*, *Discrete Mathematics, Algorithms and Applications* 12 (2020), 2050025. The general \(j,k\)-pitchfork formulation predates the 2026 source. This 13-page 2020 paper explicitly studies positive-lower-load \(j=1,k=2\) domination and gives a complete-bipartite result (Theorem 2.4), not the all-\(k\) crown enumerator. The full PDF text was inspected at https://des.utq.edu.iq/wp-content/uploads/sites/22/2022/11/pitchfork-domination-in-graphs.pdf ; further historical coverage is not exhaustive.
