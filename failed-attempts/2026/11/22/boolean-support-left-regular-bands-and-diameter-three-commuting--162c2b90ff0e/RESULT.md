# Boolean-support left-regular bands and diameter-three commuting graphs of affine-group retractions

## Finding

Let \(q=p^f\ge3\) be any prime power and write \(n=q-1\). Set \(G=\operatorname{AGL}(1,\mathbb F_q)=\mathbb F_q\rtimes\mathbb F_q^\times\), with multiplication \((b,a)(c,d)=(b+ac,ad)\). Put \(k=\omega(n)\), and factor \(n=\prod_{i=1}^{k} \ell_i^{e_i}\). For every nonempty set \(S\subseteq[k]\), let \(r_S\in\mathbb Z/n\mathbb Z\) be uniquely determined by
\[
r_S\equiv1\pmod{\ell_i^{e_i}}\quad(i\in S),\qquad r_S\equiv0\pmod{\ell_i^{e_i}}\quad(i\notin S).
\]
Then the complete set of retractions (composition-idempotent group endomorphisms) consists of the trivial homomorphism \(\mathbf0\), the identity \(\mathbf1\), and the distinct maps
\[
P_{S,u}(b,a)=\bigl((1-a^{r_S})u,a^{r_S}\bigr),\qquad \varnothing\ne S\subseteq[k],\quad u\in\mathbb F_q.
\]
Composition, with the left factor applied last, has the **left-regular-band** law
\[
P_{S,u}P_{T,v}=\begin{cases}P_{S\cap T,u},&S\cap T\ne\varnothing,\\\mathbf0,&S\cap T=\varnothing.\end{cases}
\]
The two exceptional maps are the identity and a zero for this multiplication. In particular every product remains a retraction, and \(XYX=XY\) for all retractions \(X,Y\). There are exactly
\[
2+q(2^k-1)
\]
retractions. Their proper nonzero images are the conjugates of cyclic subgroups of orders \(\prod_{i\in S}\ell_i^{e_i}\), the nontrivial unitary divisors of \(n\).

**Commuting graph.** Remove the universally commuting vertices \(\mathbf0\) and \(\mathbf1\). Join two distinct proper retractions when they commute under composition. The criterion is
\[
P_{S,u}P_{T,v}=P_{T,v}P_{S,u}\quad\Longleftrightarrow\quad u=v\ \text{or}\ S\cap T=\varnothing.
\]
For \(1\le s\le k\), the graph has the degree
\[
d_s=2^k-2+(q-1)(2^{k-s}-1)
\]
with multiplicity \(q\binom{k}{s}\). If \(k=1\), the graph consists of \(q\) isolated vertices (this is the previously covered prime-power-complement boundary). If \(k\ge2\), it is connected with **diameter exactly three**. Its clique number and chromatic number are each \(2^k-1\); exactly \(q\) cliques have that maximum size, namely all subsets at each fixed \(u\). Its independence number is \(q\).

The number of **ordered** commuting pairs of retractions, including diagonal pairs and the two universal vertices, is
\[
C_q=4+4q(2^k-1)+q(4^k-3^k)+q^2(3^k-2^{k+1}+1).
\]
For example, \(q=7\) and \(k=2\) give 23 retractions, 235 ordered commuting pairs, and a reduced graph on 21 vertices of diameter three, with degree 8 on 14 vertices and degree 2 on 7 vertices.

## Assumptions and scope

All homomorphisms and automorphisms are **abstract group homomorphisms**, not \(\mathbb F_q\)-linear maps and not transformations of the underlying affine set. The affine parameter \(a\) is nonzero. The graph above excludes the two commuting-universal idempotents, while the count \(C_q\) includes them. We distinguish the zero homomorphism \(\mathbf0\) from the maps with trivial multiplicative component: the latter coincide with \(\mathbf0\). No assertion of a diameter for a disconnected graph is made. The primary new claim concerns the compatible-retraction structure and graph in the case \(k\ge2\); the \(k=1\) boundary is identified for completeness. The degenerate field \(q=2\) yields the cyclic group of order two and exactly its zero and identity retractions; it is excluded from the stated uniform count.

## Proof

**1. Endomorphism dichotomy.** The additive subgroup \(V=\{(b,1):b\in\mathbb F_q\}\) is the unique Sylow \(p\)-subgroup and is characteristic. Any homomorphism \(F:G\to G\) induces an additive map \(T:V\to V\) and a multiplicative homomorphism \(h:\mathbb F_q^\times\to\mathbb F_q^\times\), hence \(h(a)=a^r\) for a unique residue \(r\pmod n\). The conjugation relation \((0,a)(b,1)(0,a)^{-1}=(ab,1)\) forces \(T(ab)=h(a)T(b)\) for all \(a\ne0\). If \(T\ne0\), then \(T(1)\ne0\), and \(a\mapsto h(a)=T(a)/T(1)\) extends at 0 to an additive and multiplicative map \(\mathbb F_q\to\mathbb F_q\). Such a finite-field map is an automorphism, so \(h(a)=a^{p^j}\) for some \(0\le j<f\), and \(F\) is an affine semilinear group automorphism. If \(T=0\), the image of the complement defines a 1-cocycle \(c(a)\) satisfying \(c(ab)=c(a)+a^rc(b)\). Because the complement is abelian, \((1-a^r)c(b)=(1-b^r)c(a)\). When \(r\ne0\pmod n\), choose \(a\) with \(a^r\ne1\); this proves \(c(b)=(1-b^r)u\) for a unique \(u\in\mathbb F_q\). For \(r=0\), the image of the order-\(n\) complement lies in the additive \(p\)-group, hence is zero, and \(F=\mathbf0\). Conversely every displayed \(P_{r,u}\) is a homomorphism. This standard structural reduction is not itself claimed new.

**2. Idempotence.** A group automorphism satisfying \(F^2=F\) is necessarily the identity. For any two nonautomorphic maps as in step 1, direct substitution yields \(P_{r,u}P_{s,v}=P_{rs,u}\), with the understanding that exponent zero means the trivial map. Therefore \(P_{r,u}^2=P_{r,u}\) exactly when \(r^2\equiv r\pmod n\). Since \(n=\prod_i\ell_i^{e_i}\), each local factor requires \(r\equiv0\) or 1, proving the CRT support form. The residue zero produces only \(\mathbf0\); all other support/residual-translation pairs are distinct because the action on the quotient detects the residue, and when the quotient action is nontrivial a suitable \(a\) recovers \(u\). The CRT also gives \(r_Sr_T=r_{S\cap T}\). This proves the classification, composition law, count, unitary-divisor images, and left-regular-band identity.

**3. Commutation and degrees.** If the supports intersect, the products in opposite orders are \(P_{S\cap T,u}\) and \(P_{S\cap T,v}\); their equality is equivalent to \(u=v\). If supports are disjoint both products are zero. Thus at a vertex labeled by a size-\(s\) support \(S\), there are \(2^k-2\) distinct neighbors with the same \(u\), and for each other value of \(u\), exactly \(2^{k-s}-1\) nonempty disjoint supports. The stated degrees and multiplicities follow.

**4. Geometry of the commuting graph.** For fixed \(u\), the entire layer of \(2^k-1\) vertices forms a clique. When \(k\ge2\), for arbitrary vertices \((S,u)\) and \((T,v)\) with \(u\ne v\), choose distinct singleton supports \(\{i\}\), \(\{j\}\). The path \((S,u)\)--\((\{i\},u)\)--\((\{j\},v)\)--\((T,v)\) (with repetitions omitted as needed) has length at most three. For the full supports \(([k],u)\), \(([k],v)\) with distinct \(u,v\), neither an edge nor a common neighbor exists, proving diameter at least three. A clique cannot use the same support with distinct \(u\), since such vertices do not commute. Hence its size is at most \(2^k-1\). Attaining the bound requires all nonempty supports, in particular \([k]\), whose vertex has no cross-layer neighbors, forcing a single parameter \(u\). Therefore there are exactly \(q\) maximum cliques. Coloring each vertex by its support gives \(2^k-1\) colors, proving chromatic equality. Every independent set meets each same-parameter clique in at most one vertex, so has at most \(q\) vertices; picking any fixed support with all \(q\) different parameters attains it.

**5. Ordered commuting-pair count.** The number of ordered pairs of nonempty supports that are disjoint is \(D=3^k-2^{k+1}+1\), because each prime index is assigned to the first support, second support, or neither, with both empty cases excluded. The number of intersecting pairs is \(I=(2^k-1)^2-D=4^k-3^k\). Each intersecting pair commutes for exactly \(q\) equal-parameter choices; each disjoint pair commutes for all \(q^2\) parameter pairs. There are additionally 4 ordered pairs involving only \(\mathbf0,\mathbf1\), and \(4q(2^k-1)\) ordered pairs with exactly one universal vertex. Summing gives the stated expression.

## Verification

The stand-alone `affine_retracts_verify.py` uses only the Python standard library. Execute `python3 affine_retracts_verify.py` from a directory containing the file. It constructs finite-field arithmetic for \(q=3,4,5,7,8,9\), enumerates actual group homomorphisms using two generators and tests their action on every group element, isolates all idempotent group maps, then recomputes from the actual functions their composition law, left-regular-band property, pairwise commuting count, degree multiset, and graph diameter when connected. Its final expected line is `AFFINE_RETRACTION_GRAPH_VERIFIED`. For \(q=7\), it independently finds 23 retractions and 235 ordered commuting pairs. These experiments test bounded instances; the general proof is in Steps 1–5.

## Relationship to prior work

The reduction of general affine-group endomorphisms to automorphisms or maps killing translations was explicitly described in a 2013 discussion by Derek Holt; the present classification uses that established idea rather than asserting it as new. Arvasi, Odabaş and Wensley classify the idempotent endomorphisms of the ordinary dihedral group of order \(2p\); their dimension-one case overlaps the \(k=1\) boundary when \(q=3\). A full published theorem on commuting retractions of **elementary generalized dihedral groups** treats a complement of order two and additive dimension at least two, with linear-projection and translation parameters. Its hypotheses do not cover \(\operatorname{AGL}(1,\mathbb F_q)\) when \(q-1\) has multiple prime divisors. A separate result on scalar affine Frobenius groups studies multiplicities of character codegrees rather than retraction compatibility; a result on two-round logical theories of the very same one-dimensional affine groups also has a different invariant. Classical CRT idempotents and elementary group-endomorphism theory are used as inputs, not claimed novel. The contribution is their exact **joint retraction-band and graph** structure, with the arithmetic \(\omega(q-1)\)-controlled degree law and sharp diameter transition, for the cyclic-complement family.

## Limitations

The theorem is for the full multiplicative complement \(\mathbb F_q^\times\) acting on the additive group of a finite field, not arbitrary cyclic Frobenius complements or higher-dimensional affine groups. The graph excludes two central vertices so that its diameter is not trivially two. The results do not claim a complete classification of arbitrary pairs of *nonidempotent* endomorphisms. Finite checks do not replace the proof. Prior coverage was compared by full-text inspection where available and by indexed summaries elsewhere; a mathematically equivalent unindexed theorem remains a residual literature risk. The work has not undergone independent mathematical audit.

## References

1. A. Bors, *Worst-case approximability of functions on finite groups by endomorphisms and affine maps*, arXiv:1709.00734, first public version 2017-09-03, https://arxiv.org/abs/1709.00734. General motivation for endomorphism monoids of finite groups.
2. D. Holt, answer to *What are the endomorphisms of the group of affine transformations of a field?*, MathOverflow, 2013, https://mathoverflow.net/questions/149447/what-are-the-endomorphisms-of-the-group-of-affine-transformations-of-a-field. Direct prior endomorphism dichotomy.
3. Z. Arvasi, A. Odabaş and C. D. Wensley, *Computing 3-Dimensional Groups: Crossed Squares and Cat²-Groups*, arXiv:1911.12799 (2019), https://arxiv.org/abs/1911.12799. Prior retractions of dihedral groups of prime index.
4. *Commuting retractions of elementary generalized dihedral groups*, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-commuting-retractions-of-elementary-generalized-dihedral-groups--0ef9efc1c172. Distinct complement and dimension; relevant full text inspected.
5. *Scalar affine Frobenius groups are rigid under the group pseudo-algebra*, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-scalar-affine-frobenius-groups-are-rigid-under-the-group-pseudo--7f6e8dc6f972. Same family, different invariant; relevant full text inspected.
6. *Fifteen two-round theories of one-dimensional affine groups over finite fields*, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-fifteen-two-round-theories-of-one-dimensional-affine-groups-over--fe56c12aaef1. Same family, different logical invariant; relevant full text inspected.
7. J. Hemelaer and M. Rogers, *Solution to a problem of FitzGerald*, https://doi.org/10.1007/s00233-021-10170-5. General commuting-idempotent context.
8. J. Kumar et al., *On commuting graphs of Brandt semigroups*, arXiv:2010.05000, https://arxiv.org/abs/2010.05000. Graph-theoretic context on a different semigroup.
