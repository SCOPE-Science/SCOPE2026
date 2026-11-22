# Three leading clique-rarity levels of Henson types over independent parameters

## Finding
Fix integers \(q\ge3\), \(r\ge q+1\), and \(m\ge0\). In the countable homogeneous universal \(K_{q+1}\)-free graph, individually name an induced independent set \(A_m\) of \(m\) vertices. Let \(T_{q,r}(m)\) be the number of complete types over \(A_m\) of ordered \(r\)-tuples of distinct vertices outside \(A_m\).

For each labelled graph \(H\) on the new coordinates \([r]\), let \(\mathcal K_q(H)\) be its set of \(q\)-vertex cliques, and define
\[
 b_q(H)=\#\bigl\{S\subseteq[r]:\text{no member of }\mathcal K_q(H)\text{ is contained in }S\bigr\}.
\]
Then the complete type count has the finite transfer identity
\[
 T_{q,r}(m)=\sum_{\substack{H\text{ on }[r]\\K_{q+1}\not\subseteq H}}b_q(H)^m.
\]
Define the three disjoint, nonempty graph classes \(\mathcal C_0,\mathcal C_1,\mathcal C_2\) among these labelled graphs, where \(\mathcal C_0\) consists of graphs with no \(q\)-clique, \(\mathcal C_1\) of graphs with exactly one \(q\)-clique, and \(\mathcal C_2\) of graphs with exactly two \(q\)-cliques sharing precisely \(q-1\) vertices. Write \(N_j=|\mathcal C_j|\). Set
\[
 B_0=2^r,\qquad B_1=2^r-2^{r-q},\qquad B_2=2^r-3\cdot2^{r-q-1}.
\]
These are the three strictly largest possible distinct positive values of \(b_q(H)\), attained precisely on \(\mathcal C_0,\mathcal C_1,\mathcal C_2\), respectively. Consequently, for fixed \(q,r\),
\[
 \boxed{T_{q,r}(m)=N_0B_0^m+N_1B_1^m+N_2B_2^m+O_{q,r}((B_2-1)^m).}
\]
Uniformly choosing one complete type, its induced graph \(H\) tends to the **uniform distribution on labelled \(K_q\)-free graphs on \([r]\)**, with total-variation error \(O_{q,r}((B_1/B_0)^m)\). Conditional on having at least one \(q\)-clique, \(H\) tends to the uniform distribution on \(\mathcal C_1\); conditional on having at least two \(q\)-cliques, it tends to the uniform distribution on \(\mathcal C_2\). In particular the two rare cliques asymptotically overlap in exactly \(q-1\) vertices, and the first two rare-event exponential bases are sharply \(B_1/B_0\) and \(B_2/B_0\). Their exact leading rare-event laws are
\[
 \Pr_m(|\mathcal K_q(H)|\ge1)\sim\frac{N_1}{N_0}\left(\frac{B_1}{B_0}\right)^m,\qquad
 \Pr_m(|\mathcal K_q(H)|\ge2)\sim\frac{N_2}{N_0}\left(\frac{B_2}{B_0}\right)^m.
\]

At the **critical arity \(r=q+1\)**, the expansion is an exact three-term identity with no remainder. Put
\[
 N_2=\binom{q+1}{2},\quad N_1=(q+1)(2^q-q-1),\quad
 N_0=2^{\binom{q+1}{2}}-1-N_1-N_2.
\]
Then for every \(m\ge0\),
\[
 \boxed{T_{q,q+1}(m)=N_0(2^{q+1})^m+N_1(2^{q+1}-2)^m+N_2(2^{q+1}-3)^m.}
\]
For example, the homogeneous \(K_4\)-free graph has exactly \(41\cdot16^m+16\cdot14^m+6\cdot13^m\) ordered injective four-types over \(m\) named independent vertices.

## Assumptions and scope
All graphs are finite, simple, irreflexive and undirected, except for the fixed countably infinite homogeneous host. Parameter vertices are pointwise named, pairwise nonadjacent, and disjoint from the new tuple; all new coordinates are ordered and pairwise distinct. Every adjacency bit to a named vertex and among tuple coordinates is part of the type. The distribution is uniform over **complete types**, not over vertex samples or a random graph on the host. The integers \(q,r\) are fixed in all asymptotic statements, while \(m\to\infty\). No assertion about growing \(r\) is made.

## Proof
**Finite types and the transfer identity.** The age of the homogeneous \(K_{q+1}\)-free graph is precisely the finite \(K_{q+1}\)-free graphs; ultrahomogeneity identifies complete types of distinct new points over a named finite base with finite induced extension diagrams. Fix an internal labelled graph \(H\) on the \(r\) coordinates. If it has a \(K_{q+1}\), there are no types. Otherwise each independently named, pairwise nonadjacent old vertex \(a\) chooses a new-coordinate neighborhood \(S_a\subseteq[r]\). Since the old vertices have no edges among themselves, a forbidden \(K_{q+1}\) in the complete diagram can use **at most one** old vertex. It occurs precisely when some \(S_a\) contains a \(q\)-clique of \(H\). Thus there are exactly \(b_q(H)\) allowed neighborhood choices per old vertex, independently, giving \(b_q(H)^m\) types with internal graph \(H\) and the displayed sum.

**Sharp first three bases.** For every \(q\)-clique \(Q\subseteq[r]\), the forbidden neighborhood event \(\{S:Q\subseteq S\}\) has cardinality \(2^{r-q}\). No \(q\)-clique yields \(B_0\) allowed neighborhoods, and exactly one yields \(B_1\). For distinct \(q\)-cliques \(Q_1,Q_2\), inclusion–exclusion gives a forbidden-neighborhood union of size
\[
 2^{r-q+1}-2^{r-|Q_1\cup Q_2|}\ge 2^{r-q+1}-2^{r-q-1}=3\cdot2^{r-q-1},
\]
with equality if and only if \(|Q_1\cap Q_2|=q-1\). Any **third** distinct \(q\)-clique \(Q_3\) makes this union strictly larger: the neighborhood \(S=Q_3\) contains neither of the other equal-sized distinct \(q\)-cliques, and hence is a new forbidden neighborhood. Therefore every graph with at least two \(q\)-cliques has at most \(B_2\) allowed neighborhoods, with equality precisely when it has exactly two \(q\)-cliques sharing \(q-1\) vertices. The classes are nonempty: use an edgeless graph, one isolated \(K_q\), or \(K_{q+1}\) with one edge removed, respectively, with extra isolated vertices where necessary. Their defining graphs are \(K_{q+1}\)-free. Since \(r\ge q+1\), the integers obey \(B_0>B_1>B_2\ge13\). Every other admissible graph has integer base at most \(B_2-1\), establishing the three leading exponential terms and an absolute remainder bound \(2^{\binom r2}(B_2-1)^m\).

**Conditional limits.** For every internal graph in one \(\mathcal C_j\), its weight is exactly \(B_j^m\); hence the conditional distribution within that class is uniform. The total weight of the classes below the leading allowed class decays exponentially relative to that leading base. First, all graphs with a \(q\)-clique have weight at most \(B_1^m\), so the full law converges to uniform on \(\mathcal C_0\). Restricted to graphs with at least one \(q\)-clique, \(\mathcal C_1\) is dominant; restricted to those with at least two, \(\mathcal C_2\) is dominant. All coefficients are positive for fixed \(q,r\), proving the limits and the sharp decay ratios.

**The exact critical-arity census.** If \(r=q+1\), every internal graph is either \(K_{q+1}\)-free or the unique complete graph \(K_{q+1}\). A graph with one fixed \(q\)-clique \(Q\) has only one remaining vertex \(v\); it has **exactly one** \(q\)-clique if and only if \(v\) has at most \(q-2\) neighbors in \(Q\). This provides \((q+1)\sum_{d=0}^{q-2}\binom qd=(q+1)(2^q-q-1)\) labelled graphs, with no double count. A graph with two distinct \(q\)-cliques is necessarily the complete graph with the edge between their two omitted vertices deleted; it has exactly two such cliques, and there are \(\binom{q+1}{2}\) choices of the absent edge. Three distinct \(q\)-cliques would force the full \(K_{q+1}\). Subtraction from all \(2^{\binom{q+1}{2}}\) labelled graphs leaves the stated \(N_0\), after also removing the single forbidden complete graph. Thus only the three bases are possible and the critical-arity formula is exact.

## Verification
The standard-library program `verify.py` enumerates every labelled \(K_{q+1}\)-free internal graph in five test regimes \((q,r)=(3,4),(3,5),(3,6),(4,5),(5,6)\). It independently counts the allowed old-to-new adjacency bit patterns in small cases, checks the leading-base equality cases, and compares the critical-arity closed formula with brute-force totals at several positive parameter sizes. The recorded output in `verification_output.txt` ends in `ALL_FINITE_DIAGRAM_TESTS_PASS`. For example, it gives \(T_{3,4}(0)=63\), \(T_{3,4}(1)=958\), \(T_{3,4}(2)=14646\) and the class coefficients \((41,16,6)\). These finite checks are corroboration only; the unrestricted theorem follows from the preceding proof.

## Relationship to prior work
Henson's homogeneity and universality theorem (Theorem 2.3, 1971) and Conant's graph-type consistency criterion (Proposition 3.4, 2014) establish the logical framework; these are prior and are not claimed as new. Existing exact one-point counting in Henson graphs deals with \(r=1\), not the present higher-arity rarity hierarchy. An indexed higher-arity result for the **triangle-free Henson graph** already obtains an independent-base finite transfer and the first two exponential terms; in particular its two-edge effect is not claimed here. The present theorem has \(q\ge3\), a nontrivial \(K_q\)-free limiting graph ensemble, a complete three-leading-base classification and two rare-clique conditional laws, as well as an exact \(r=q+1\) census. Another indexed result for \(K_{q+1}\)-free Henson graphs treats repeated **maximal parameter cliques** and rare **internal edges**: its named base is a disjoint union of cliques, whereas the present named base is independent and most internal graph types remain nonempty; the statements do not imply one another by restriction. A current independent-base biclique type-recovery result concerns small arities and distinct reconstruction questions. There can nevertheless be unindexed general enumerations or later derivations with stronger coverage; historical priority requires external review.

## Limitations
The result does not give closed forms for the numbers \(N_j\) at arbitrary larger arities, does not describe fourth or lower exponential levels, does not apply to non-independent named bases, and gives no quantitative bound uniform as \(r\) grows with \(m\). The derivation uses standard finite-extension counting and elementary inclusion–exclusion; the claimed new content is the precise all-arity leading three-level hierarchy, conditional clique-overlap concentration, and the closed critical-arity enumeration. The finite checker is not an infinite proof and no independent audit has been performed.

## References
1. C. W. Henson, “A family of countable homogeneous graphs,” *Pacific Journal of Mathematics* 38 (1971), 69–83, especially Section 2 and Theorem 2.3. https://msp.org/pjm/1971/38-1/pjm-v38-n1-p09-p.pdf
2. G. Conant, “Forking and dividing in Henson graphs,” arXiv:1401.1570v1, first posted 2014-01-08, Section 3 and Proposition 3.4. https://arxiv.org/pdf/1401.1570
3. “Exact finite-parameter 1-type counting in Henson graphs is #P-complete,” published mathematical research record, 2026-10-04. https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-finite-parameter-1-type-counting-in-henson-graphs-is-p-com--7c84dde7c650
4. “Higher-arity Henson type enumeration and exact-counting hardness,” published mathematical research record, 2026-10-25. https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-higher-arity-henson-type-enumeration-and-exact-counting-hardness--141a441755d6
5. “Exact triple-type spectrum and rare-edge clustering over disjoint maximal cliques in Henson graphs,” published mathematical research record, 2026-10-26. https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-exact-triple-type-spectrum-and-rare-edge-clustering-over-disjoin--85936f11eaf8
