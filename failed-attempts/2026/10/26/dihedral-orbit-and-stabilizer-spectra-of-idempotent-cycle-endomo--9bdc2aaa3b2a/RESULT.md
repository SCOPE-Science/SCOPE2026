# Dihedral orbit and stabilizer spectra of idempotent cycle endomorphisms

## Finding

Let \(C_n\) be the loopless undirected cycle on \(\mathbb Z/n\mathbb Z\), where \(n\ge3\). Let \(E_n=\operatorname{End}(C_n)\) be the monoid of total graph endomorphisms (each edge must map to an edge, without collapsing its endpoints). Its unit group \(D_{2n}=\operatorname{Aut}(C_n)\) has order \(2n\) and acts by \(g\cdot e=g e g^{-1}\).

**Theorem (complete rank-and-symmetry classification).** When \(n\) is odd, the identity is the only idempotent of \(E_n\). When \(n\) is even, put \(h=n/2\) and let \(A_k\) be the adjacency matrix of the simple path on the ordered vertices \(0,1,\ldots,k-1\). For every integer \(2\le k\le h+1\), define

\[
L=n-k+1,\qquad W_{n,k}=(A_k^L)_{k-1,0}
\]

and

\[
F_{n,k}=\begin{cases}
(A_k^{L/2})_{k-1,(k-1)/2},&k\text{ odd},\\
(A_k^{(L-1)/2})_{k-1,k/2-1}+(A_k^{(L-1)/2})_{k-1,k/2},&k\text{ even}.
\end{cases}
\]

Here the exponents are integers because \(L\equiv k-1\pmod2\) when \(n\) is even. The entire idempotent rank and dihedral-conjugacy distribution is

\[
\#\{e\in E_n:e^2=e,\ \operatorname{rank}(e)=k\}=nW_{n,k},
\]

\[
\begin{aligned}
\#\{\text{rank-}k\text{ orbits of size }n\}&=F_{n,k},\\
\#\{\text{rank-}k\text{ orbits of size }2n\}&=\frac{W_{n,k}-F_{n,k}}2.
\end{aligned}
\]

The identity is a single further orbit of rank \(n\) and size one. Every rank \(2,\ldots,h+1\) occurs, and no other proper rank occurs. Hence

\[
\#(\{e:e^2=e\}/D_{2n})=1+\frac12\sum_{k=2}^{h+1}(W_{n,k}+F_{n,k}).
\]

This classifies stabilizer sizes as well: every proper idempotent has either trivial stabilizer or a stabilizer of order two, with the latter occurring exactly at reflection-symmetric retractions.

For even cycle sizes \(n=4,6,8,10,12,14\), the total numbers of idempotents are respectively \(9,25,73,221,685,2157\), and the numbers of dihedral conjugacy orbits are \(3,4,8,14,36,83\).

## Assumptions and scope

The term graph endomorphism is **strict**: an edge must map to an edge, so adjacent vertices cannot have identical images. Neither weak endomorphisms (which may collapse edges) nor partial graph isometries are included. The theorem covers all integers \(n\ge3\), with a simple three-cycle at \(n=3\). Rank is the cardinality of the image. Conjugacy is only under the actual unit group of \(E_n\), equivalently its dihedral graph automorphisms, not arbitrary semigroup conjugacy or a two-sided unit action.

## Proof

**1. Retraction structure and parity.** An idempotent transformation \(e\) fixes every point of its image: for \(y=e(x)\), \(e(y)=e(e(x))=e(x)=y\). Thus \(e\) retracts the cycle onto its image. Because \(C_n\) is connected and adjacency is preserved, the image is connected. A proper connected induced subgraph of a simple cycle, with at least two vertices, is a path consisting of a cyclic interval (arc) of \(k\) consecutive vertices. A one-vertex image is impossible in a loopless graph. The full-image idempotent must be the identity.

Choose an arc \(I=(v_0,v_1,\ldots,v_{k-1})\) as the image. The restriction of \(e\) to \(I\) is the identity. The remaining edges form the complementary path with \(L=n-k+1\) edges from \(v_{k-1}\) to \(v_0\), including both endpoints. Its images give a walk

\[
w_0=k-1,\quad w_L=0,\quad 0\le w_i\le k-1,\quad |w_i-w_{i-1}|=1.
\]

Conversely every such walk gives exactly one graph-endomorphism retraction onto \(I\), because it specifies the map on every non-image vertex and respects every edge. A path is bipartite, so the two endpoints of the walk force \(L\equiv k-1\pmod2\), or \(n\) even. For even \(n\), existence is equivalent to \(L\ge k-1\), i.e. \(k\le n/2+1\); a direct geodesic followed by two-edge backtracks provides a walk for every permitted \(k\). As there are exactly \(n\) distinct proper arcs of each such length, and the adjacency-matrix power counts these walks, the claimed \(nW_{n,k}\) formula follows. If \(n\) is odd, no proper idempotent exists.

**2. The action of the arc stabilizer.** The dihedral group acts transitively on all length-\(k\) arcs. For each proper arc \(I\), its setwise stabilizer has exactly two elements: the identity and the reflection \(s\) interchanging the arc endpoints. No nonidentity rotation preserves a nonempty proper arc. The reflection reverses both the arc and its complementary path. In coordinates, the induced involution on complementary walks is

\[
(\tau w)_i=k-1-w_{L-i}\qquad(0\le i\le L).
\]

Thus the \(D_{2n}\)-orbits of rank-\(k\) idempotents are exactly the orbits of \(\tau\) on the \(W_{n,k}\) complementary walks.

**3. Fixed walks and stabilizers.** If \(k\) is odd then \(L\) is even, and \(\tau w=w\) is equivalent to prescribing the midpoint \(w_{L/2}=(k-1)/2\) and choosing an arbitrary first half-walk from \(k-1\) to this midpoint; the second half is then uniquely forced by reflection. This gives \(F_{n,k}=(A_k^{L/2})_{k-1,(k-1)/2}\). If \(k\) is even then \(L\) is odd, and the two central values of a fixed walk must sum to \(k-1\) and differ by one. Therefore the first central value is either \(k/2-1\) or \(k/2\). Again the second half is uniquely forced, giving the stated two-entry expression for \(F_{n,k}\).

Each of the \(F_{n,k}\) reflection-fixed walks has a dihedral stabilizer of order two and hence an orbit of size \(n\). The remaining \(W_{n,k}-F_{n,k}\) walks form pairs under \(\tau\), yielding \((W_{n,k}-F_{n,k})/2\) orbits of size \(2n\). The identity is fixed by the full dihedral group. This also proves all integrality and nonnegativity claims and completes the orbit formula. \(\square\)

## Verification

The accompanying `cycle_retraction_orbit_checker.py` enumerates all strict endomorphisms of \(C_n\) by adjacent-image walks, tests \(e(e(i))=e(i)\) directly, constructs conjugation under all \(2n\) automorphisms, and computes the actual orbit sizes without assuming the theorem. Separately it computes the predicted \(W_{n,k}\) and \(F_{n,k}\) using dynamic programming on path adjacency. All ranks and orbit sizes agree for every \(3\le n\le14\), representing \(3176\) idempotents across the twelve cycles. Run `python3 cycle_retraction_orbit_checker.py` beside the packaged script to reproduce the recorded output. These finite checks corroborate, but do not establish, the general theorem.

## Relationship to prior work

Dimitrova, Fernandes, Koppitz, and Quinteiro [1] characterize cycle-graph endomorphisms, their cardinalities, Green relations, regularity, and generating ranks. In particular, their Proposition 1.7 gives rigidity for odd cycles, and Proposition 1.9 counts all endomorphisms. Their paper defines a two-sided unit equivalence used for generators; it does not provide the **unit-conjugation orbit/stabilizer profile of idempotents** here. Our proof includes the needed retraction and parity argument, so it does not assume an unproved characterization from [1].

The bounded-path walk counts used in \(W_{n,k}\) are classical and are not claimed as new: Lin and Zeng [2] discuss path homomorphism enumeration and a reflection-principle formula. The additional result here is the canonical retraction-to-complementary-walk correspondence together with the reversal-and-complement involution that supplies all **dihedral orbit sizes**. Michels and Knauer [3] study cycle endomorphism counts and induced congruence classes; their publicly available abstract does not establish the stated conjugacy refinement. Fernandes and Paulista [4] study partial **isometries** of cycles, a different monoid.

## Limitations

Only conjugation by invertible cycle automorphisms is classified, not natural conjugacy for arbitrary nonunits or Green-equivalence classes. The matrices \(A_k\) give exact finite integer formulas but not a single elementary closed form for all \(n,k\). The originality comparison is based on the inspected full texts of [1] and [2], together with targeted bibliographic and indexed-record searches; the full 2009 source [3] was not accessible, so an implicit equivalent enumeration there remains a priority risk. No independent mathematical audit is claimed.

## References

[1] I. Dimitrova, V. H. Fernandes, J. Koppitz, and T. M. Quinteiro, *On monoids of endomorphisms of a cycle graph*, arXiv:2310.04149v1 (first posted 2023-10-06), https://arxiv.org/html/2310.04149v1.

[2] Z. Lin and J. Zeng, *On the number of congruence classes of paths*, arXiv:1112.4026 (first posted 2011-12-17), https://arxiv.org/abs/1112.4026.

[3] M. A. Michels and U. Knauer, *The congruence classes of paths and cycles*, Discrete Mathematics 309 (2009), 5352–5359, DOI:10.1016/j.disc.2008.11.022 (abstract accessible; full text not inspected).

[4] V. H. Fernandes and T. Paulista, *On the monoid of partial isometries of a cycle graph*, Turkish Journal of Mathematics 47 (2023), 1746–1760, DOI:10.55730/1300-0098.3460 (abstract and description inspected).
