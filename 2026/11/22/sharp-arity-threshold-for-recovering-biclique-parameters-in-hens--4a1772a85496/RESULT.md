# Sharp arity threshold for recovering biclique parameters in Henson graphs

## Finding
For every integer \(m\ge4\), let \(H_m\) be the countable homogeneous universal graph omitting \(K_m\). Let \(A\subset H_m\) be an induced complete bipartite graph \(K_{a,b}\), with integers \(a,b\ge1\), and put \(n=a+b\). Every vertex of \(A\) is individually named. Let \(t_s(A)\) be the number of complete types of ordered \(s\)-tuples of pairwise distinct vertices outside \(A\). Set \(r=m-2\), \(q=2^r\), and \(h=q-1\).

For all \(0\le s<r\), the complete numerical prefix is independent of the biclique's bipartition:
\[
\boxed{t_s(A)=2^{sn+\binom{s}{2}}.}
\]
At the first potentially distinguishing arity, there is an exact correction:
\[
\boxed{t_r(A)=2^{rn+\binom r2}-(q^a-h^a)(q^b-h^b).}
\]
For fixed \(m\), the numerical pair \((t_1,t_r)\) uniquely recovers \(\{a,b\}\) as an unordered multiset, without knowing \(n\) in advance. Indeed \(n=\log_2 t_1\), and the forbidden-diagram correction is strictly monotone as a positive bipartition becomes more balanced. More precisely, for \(1\le a\le b-2\),
\[
\boxed{t_r(K_{a,b})-t_r(K_{a+1,b-1})
       =(qh)^a\big(q^{b-a-1}-h^{b-a-1}\big)>0.}
\]
Consequently \((t_1,\ldots,t_r)\) recovers the unlabelled induced base graph and determines the total numerical type count at every higher arity. For each \(n\ge4\), no shorter initial prefix can recover the unordered bipartition: every prefix through \(t_{r-1}\) is identical for the nonisomorphic graphs \(K_{1,n-1}\) and \(K_{2,n-2}\). Thus \(m-2\) is the **sharp detecting arity** for every forbidden-clique size \(m\ge4\).

Examples at \(n=4\): in \(H_4\), both \(K_{1,3}\) and \(K_{2,2}\) have \(t_1=16\), but \(t_2=475\) and \(463\), respectively. In \(H_5\), both have \(t_1=16\) and \(t_2=512\), but their \(t_3\) values are \(32599\) and \(32543\).

## Assumptions and scope
The graphs are simple, undirected and loopless. Both parts of the induced biclique are nonempty. The ambient \(H_m\) is fixed when comparing numerical spectra. Types count all labelled adjacency diagrams of new ordered, distinct coordinates disjoint from the finite named base, **not** algebraic coordinate types, repetitions, random ambient vertex frequencies, or unlabeled tuple orbits under coordinate permutations. A zero-length tuple contributes \(t_0=1\). Equality of spectra is numerical equality, not equality of types with differently named parameter vocabularies. The recovered unordered pair of part sizes describes the base up to unlabelled graph isomorphism, not a canonical correspondence between its named vertices.

## Proof
**1. Complete types and finite diagrams.** Henson's homogeneity and age theorem (1971, Theorem 2.3) says a finite labelled graph over \(A\) is realizable as an induced extension in \(H_m\) precisely when it contains no \(K_m\); two such extensions give the same complete type if and only if all their edge bits agree. Quantifier elimination in the graph presentation and the optimal-realization discussion in Conant (2014, Section 3, Proposition 3.4) justify the equivalence between finite diagrams and complete injective tuple types. Since all old vertices are individually named and tuple coordinates are ordered, no quotient by automorphisms of the biclique occurs.

**2. The invisible prefix.** The base \(K_{a,b}\) has clique number two. For \(s\le m-3\), any graph on the union of the base and \(s\) new vertices has clique number at most \(s+2\le m-1\), regardless of the edges inserted among the new vertices or between new and old ones. Thus every one of the \(\binom s2+sn\) free adjacency bits may be assigned arbitrarily. This gives \(t_s=2^{sn+\binom s2}\) for every \(s<r=m-2\).

**3. The first forbidden diagrams.** At \(s=r\), every \(K_m\) in the extension must contain exactly two old vertices, one from each side, and all \(r\) new vertices. It exists precisely when all new vertices are mutually adjacent and some old vertex in each side is adjacent to all the new vertices. For each individual old vertex there are \(q=2^r\) possible incidence vectors to the new vertices. Exactly one vector has all entries one. On a side of size \(a\), the number of assignments having at least one all-one old vertex is \(q^a-(q-1)^a=q^a-h^a\). The two sides' choices are independent; the internal edges of the \(r\) new vertices are then uniquely forced to be all present. Therefore precisely \((q^a-h^a)(q^b-h^b)\) of the \(2^{rn+\binom r2}\) diagrams are forbidden, proving the second boxed identity.

**4. Strict inverse reconstruction.** The first identity with \(s=1\) yields \(t_1=2^n\), so \(n\) is determined. Let \(F(a,b)=(q^a-h^a)(q^b-h^b)\) with \(a+b=n\). Expanding gives
\[
F(a,b)=q^n+h^n-q^ah^b-q^bh^a.
\]
A direct subtraction for \(a\le b-2\) yields
\[
F(a+1,b-1)-F(a,b)=(qh)^a(q^{b-a-1}-h^{b-a-1})>0,
\]
since \(q>h\ge1\). Hence \(F\) is strictly increasing as the smaller part grows until the balanced partition, while \(t_r=2^{rn+\binom r2}-F\) is strictly decreasing. Symmetry in \(a,b\) proves that the value of \(t_r\), once \(n\) is known, uniquely determines the unordered pair \(\{a,b\}\). Every higher tuple-count invariant is a function of the isomorphism type of the finite base and the fixed ambient \(H_m\); therefore it is determined as well.

**5. Sharpness.** For any \(n\ge4\), the unordered bipartitions \(\{1,n-1\}\) and \(\{2,n-2\}\) differ. The first formula gives identical \(t_s\) for every \(s<m-2\), whereas strict monotonicity separates them at \(s=m-2\). No smaller uniform detecting arity exists. At \(n=2,3\) there is only one unordered positive bipartition, so no distinction is needed.

## Verification
The standalone `verification/check_henson_threshold.py` exhaustively enumerates all free adjacency bit strings in 92 finite extension instances with \(m\in\{4,5,6,7\}\), tests for forbidden cliques by scanning genuine vertex subsets, and compares direct counts with both closed formulas. It separately checks 39600 arithmetic inverse-reconstruction instances for \(4\le m\le11\) and \(2\le n\le100\). The resulting output is embedded as `verification/output.txt` and was reproduced from the packaged checker. The proof above establishes the unbounded statements; finite checks do not replace it.

## Relationship to prior work
Henson (1971, Theorem 2.3) establishes the universal homogeneous \(K_m\)-free graphs. Conant (2014, Section 3) establishes finite graph-type consistency and realizability and does not present a numerical inverse threshold for bipartite named bases. An earlier one-type subset-polynomial theorem for Henson graphs already gives \(t_1=2^n\) for a triangle-free base in \(H_m\), \(m\ge4\), so that unary assertion is prior input, not claimed as new.

An existing two-point correction for **maximal** \(r\)-partite bases in \(K_{r+1}\)-free graphs (\(r\ge4\)) assumes that the base already has maximum clique number \(r\), and studies a distinct pair-compatibility obstruction. The present base has clique number two and the first forbidden mixed clique requires \(m-2\) new vertices; in particular all shorter tuple arities are free. A separate higher-arity counting result for the homogeneous triangle-free graph applies to forbidden \(K_3\), not to the \(K_m\)-free family \(m\ge4\). The new assertion is the sharp **delayed arity boundary plus recovery of the unordered bipartition at that boundary**. Those statements are neither direct special cases of the maximal-multipartite two-point correction nor stated in the inspected classical sources.

## Limitations
The recovery statement applies to induced nonempty **complete** bipartite bases, not arbitrary triangle-free graphs or bases with three or more parts. It reconstructs only the unordered part sizes. The ambient forbidden clique order must be known. The first distinguishing arity is sharp uniformly for \(n\ge4\), not a claim that two different partitions exist at smaller sizes. The enumerative method is exact, but historical priority may be obscured by unindexed literature or general finite-extension counting formulations. No independent mathematical audit or proof assistant certification is claimed.

## References
1. C. Ward Henson, *A family of countable homogeneous graphs*, Pacific Journal of Mathematics **38** (1971), 69–83, especially Theorem 2.3. https://msp.org/pjm/1971/38-1/pjm-v38-n1-p09-p.pdf ; doi:10.2140/pjm.1971.38.69.
2. Gabriel Conant, *Forking and dividing in Henson graphs*, arXiv:1401.1570v1 (first public 2014-01-08), especially Section 3, Proposition 3.4. https://arxiv.org/html/1401.1570v1 .
3. *Exact finite-parameter 1-type counting in Henson graphs is #P-complete*, publicly indexed mathematical note, 2026-10-04. https://github.com/published-finding corpus/2026/blob/main/2026/10/4/SCOPE-exact-finite-parameter-1-type-counting-in-henson-graphs-is-p-com--7c84dde7c650/RESULT.md .
4. *A collision law for two-types over maximal multipartite parameter graphs in Henson structures*, publicly indexed mathematical note, 2026-10-26. https://github.com/published-finding corpus/2026/blob/main/2026/10/26/SCOPE-a-collision-law-for-two-types-over-maximal-multipartite-paramete--8c8e5c9b100b/RESULT.md .
5. *Higher-arity Henson type enumeration and exact-counting hardness*, publicly indexed mathematical note, 2026-10-25. https://github.com/published-finding corpus/2026/blob/main/2026/10/25/SCOPE-higher-arity-henson-type-enumeration-and-exact-counting-hardness--141a441755d6/RESULT.md .
