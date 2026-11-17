# A contractible color-orbit chamber model for complete-graph Hom complexes

## Finding

**Theorem.** For every pair of integers \(2\le m\le n\), let \(X_{m,n}=\operatorname{Hom}(K_m,K_n)\) be the standard graph-homomorphism polyhedral complex, and let \(S_n\) permute its target colors. Its **ordinary geometric orbit space** is homeomorphic to the explicitly defined polytopal space
\[
Q_{m,n}=\bigcup_{\substack{k_1,\ldots,k_m\ge1\\ k_1+\cdots+k_m\le n}}D_{k_1}\times\cdots\times D_{k_m},
\qquad
D_k=\operatorname{conv}\{v_1,\ldots,v_k\},
\]
where \(v_j=(\underbrace{1/j,\ldots,1/j}_{j},0,\ldots,0)\in\mathbb R^n\). Consequently, \(|X_{m,n}|/S_n\) **strongly deformation retracts to one point**, and its integral reduced homology and all homotopy groups vanish. The space \(Q_{m,n}\) is a pure \((n-m)\)-dimensional polytopal complex with \(\binom{n-1}{m-1}\) maximal product-of-simplex cells, \(\binom nm\) vertices, and a common vertex in every maximal chamber. For \(n=m+1\), the quotient is precisely a star with \(m\) edges.

This strengthens the previously established **rational acyclicity** of the color-orbit space to an explicit topological contraction. The nonequivariant wedge-of-spheres classification is established prior work, not a new claim.

## Assumptions and scope

All graphs are finite, simple and loopless. Fix the source vertices \(1,\ldots,m\), and let the target colors be \(1,\ldots,n\). A cell of \(X_{m,n}\) is an ordered \(m\)-tuple \((A_1,\ldots,A_m)\) of nonempty, pairwise disjoint target subsets; its realization is \(\prod_i\Delta(A_i)\). The group \(S_n\) acts *only on target colors*, not on the ordered source positions. The quotient here is an ordinary orbit space, not a Borel construction. The explicit model uses the standard realization of each simplex as probability vectors.

For \(k\ge1\), the simplex \(D_k\) lies in the probability simplex \(\Delta^{n-1}\) and is the set of vectors \(a_1\ge\cdots\ge a_k\ge0\), \(a_{k+1}=\cdots=a_n=0\), with \(\sum_i a_i=1\). A point of \(Q_{m,n}\) is an \(m\)-tuple of such sorted probability vectors whose **total** number of nonzero coordinates is at most \(n\). The hypothesis \(n\ge m\) ensures nonemptiness. If \(n<m\), the graph-Hom space is empty; that case is not described as contractible.

## Proof

**1. Exact geometric realization.** Regard a point of \(X_{m,n}\) as an \(m\)-by-\(n\) array of nonnegative reals \((x_{ic})\). Every row sums to one, and for each target color \(c\) at most one row has \(x_{ic}>0\). Conversely any such array belongs to the product-simplex cell determined by its row supports; thus this description is exactly the standard Hom realization, including its attaching maps. The group \(S_n\) simultaneously permutes the array columns.

**2. Orbit classification by sorted rows.** Sort each row's entries in weakly decreasing order and call the result \(a^{(i)}\). This operation is continuous (order statistics are continuous) and \(S_n\)-invariant. Since supports of the original rows are disjoint, the total number of positive sorted entries is at most \(n\), so the resulting tuple lies in \(Q_{m,n}\). Conversely, given any tuple in \(Q_{m,n}\), place the positive entries from row \(i\) into its own set of target columns; disjoint placements are possible because their total number is at most \(n\). Hence sorting is surjective. Two original arrays give the same sorted rows exactly when, for every source row, they have the same multiset of nonzero entries. Disjointness of row supports then allows the rowwise matching bijections to be combined into one permutation of all \(n\) columns. Thus sorting separates precisely the \(S_n\)-orbits. Both the geometric quotient and \(Q_{m,n}\) are compact Hausdorff spaces, so this continuous bijection is a homeomorphism.

**3. Chamber decomposition.** The equal-prefix vectors \(v_j\) form the vertices of the sorted simplex \(D_k\). Indeed, for any sorted probability vector \(a\), setting \(a_{k+1}=0\) gives the unique coefficients
\[
\lambda_j=j(a_j-a_{j+1})\ge0,
\qquad \sum_{j=1}^k\lambda_j=1,
\qquad a=\sum_{j=1}^k\lambda_jv_j.
\]
The sets \(D_k\) are nested simplicial faces, with \(D_k\cap D_\ell=D_{\min(k,\ell)}\). Accordingly, intersections of product chambers are common faces. Every chamber with \(\sum_i k_i<n\) belongs to one with equality; the maximal chambers are indexed by positive compositions of \(n\) into \(m\) parts. Each maximal chamber has dimension \(\sum_i(k_i-1)=n-m\). Therefore the quotient is a pure polytopal complex with \(\binom{n-1}{m-1}\) maximal product cells. A vertex is a tuple \((v_{j_1},\ldots,v_{j_m})\) with \(j_i\ge1\) and \(\sum_i j_i\le n\); the count is \(\binom nm\) by introducing the unused-color count \(n-\sum_i j_i\).

**4. Explicit strong contraction.** Let \(e=v_1=(1,0,\ldots,0)\). For \(t\in[0,1]\), define
\[
H_t(a^{(1)},\ldots,a^{(m)})
=\bigl((1-t)a^{(1)}+te,\ldots,(1-t)a^{(m)}+te\bigr).
\]
Each \(D_{k_i}\) is convex and contains \(e\), so the entire homotopy remains inside **the same** product chamber as its starting point. It is continuous, fixes \((e,\ldots,e)\) pointwise, begins at the identity and ends at that common vertex. This proves a strong deformation retraction of \(Q_{m,n}\), and hence of \(|X_{m,n}|/S_n\).

**5. The first singular family.** When \(n=m+1\), admissible tuples have either all \(k_i=1\) or exactly one \(k_i=2\), with the rest equal to one. The model is \(m\) closed intervals glued only at \((e,\ldots,e)\). For \(m\ge3\) it is a nonmanifold tripod-like star, demonstrating why contractibility does not follow from a naive assertion that all quotients are balls. When \(m=n\), only the common vertex remains. These cases are included in the theorem.

## Verification

The standalone Python 3 standard-library program `verify_hom_color_quotient.py` is included with its full output `verify_hom_color_quotient_output.txt`. For all 15 pairs \(2\le m\le n\le6\), it enumerates the ordered disjoint color-block assignments and their size signatures; checks exact multinomial orbit sizes and all possible face signatures; and compares the count with \(\binom nm\). It independently tests the equal-prefix barycentric-coordinate formula and the straight-line contraction over exact rational samples. The final check marker is `HOM_COLOR_QUOTIENT_CHAMBER_AND_CONTRACTION_PASS 15`.

These tests support the explicit model but are not used as an infinite-parameter proof: Steps 1–4 above provide that proof. The verifier is a finite sanity check, not a computation of homotopy groups in unbounded cases.

## Relationship to prior work

Babson and Kozlov's 2003 paper defines the same Hom polyhedral complex and proves its **nonequivariant** wedge-of-spheres homotopy type. Their earlier 1997 work develops related ordered-disjoint-block posets and block-permutation quotient problems. These are historical inputs, not the new assertion. The complete-graph color-action character calculations in two later mathematical records establish that the **target-color \(S_n\) quotient is rationally acyclic**; their inspected main statements and proofs do not identify its integral homology, fundamental group, or homotopy type. Rational acyclicity alone does not imply contractibility. The present theorem supplies an explicit homeomorphism and a uniform strong deformation retraction, strictly stronger than those rational results.

Pfeifle's polyhedral Cayley-trick paper concerns geometric realizations and projections of Hom complexes, a pertinent geometric comparison. The accessible abstract does not state the present target-color quotient classification; its full text was not inspected, so it is not asserted to be excluded. The 1997 source was available as an abstract and older reported theorem descriptions, but its full text could not be retrieved despite alternative source attempts. Possible equivalent statements in that paper or in unindexed literature remain an originality risk.

## Limitations

The result uses the full **target-color** symmetric group; it does not classify quotients by its proper subgroups or simultaneous source permutations, which can have different topology. It does not give a homotopy contraction upstairs in the nonequivariant Hom complex. The model depends on the source vertices being ordered and on the source and target being complete loopless graphs. The actual homotopy-type conclusion requires \(n\ge m\); for \(n<m\), the quotient is empty. Publication priority cannot be certified solely by the indexed searches and accessible texts; an older equivalent result could exist. Independent mathematical validation has not been performed.

## References

1. E. Babson and D. N. Kozlov, *Complexes of graph homomorphisms*, arXiv:math/0310056, first submitted 2003-10-05, especially Definition 1.2 and Section 4.3, https://arxiv.org/html/math/0310056v4.
2. E. Babson and D. N. Kozlov, *Diagrams of classifying spaces and k-fold Boolean algebras*, arXiv:math/9704227, first publicly submitted 1997-04-29, https://arxiv.org/abs/math/9704227; MSRI preprint 1997-043, https://library.slmath.org/preprints/online/1997-043.html.
3. J. Pfeifle, *Dissections, Hom-complexes and the Cayley trick*, arXiv:math/0512529, first submitted 2005-12-22, https://arxiv.org/abs/math/0512529.
4. *Color-permutation characters of complete-graph Hom complexes*, public mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-color-permutation-characters-of-complete-graph-hom-complexes--50c1a3944425.
5. *Full two-sided symmetry character of complete-graph Hom complexes*, public mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-full-two-sided-symmetry-character-of-complete-graph-hom-complexe--ce942485ca98.
