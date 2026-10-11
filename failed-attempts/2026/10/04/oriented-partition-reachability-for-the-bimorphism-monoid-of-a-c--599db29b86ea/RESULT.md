# Oriented-partition reachability for the bimorphism monoid of a countable union of random tournaments
## Finding
Let
\[
M=\bigsqcup_{i\in\mathbb N}T_i,
\]
where each \(T_i\) is a copy of the countable homogeneous random tournament and there are no arcs between distinct components. Coleman proved that this disconnected digraph is MB-homogeneous: every finite partial monomorphism extends to a bimorphism, meaning a bijective endomorphism.

For each \(n\), let \(\mathcal O_n\) be the set of \(\operatorname{Aut}(M)\)-orbits on injective ordered \(n\)-tuples. Define a reachability relation on orbit states by
\[
O\preceq O'\quad\Longleftrightarrow\quad
\text{some bimorphism of }M\text{ sends a representative of }O\text{ to one in }O'.
\]
Then an orbit state is exactly a set partition \(\pi\) of \([n]\), together with a labeled tournament \(\tau_B\) on every block \(B\in\pi\). Under this identification,
\[
(\pi,\tau)\preceq(\sigma,\upsilon)
\quad\Longleftrightarrow\quad
\pi\text{ refines }\sigma
\text{ and }
\upsilon|_B=\tau_B\text{ for every }B\in\pi.
\]
In particular, this is a partial order rather than merely a preorder. For \(n\ge1\), it is graded by
\[
\rho(\pi,\tau)=n-|\pi|,
\]
has height \(n-1\), and a cover relation merges exactly two blocks and chooses arbitrary orientations for all newly created cross-pairs.

Writing \(A_n=|\mathcal O_n|\),
\[
A_n=\sum_{\pi\in\Pi_n}
2^{\sum_{B\in\pi}\binom{|B|}{2}},
\]
so
\[
\sum_{n\ge0}A_n\frac{z^n}{n!}
=
\exp\!\left(
\sum_{m\ge1}2^{\binom m2}\frac{z^m}{m!}
\right).
\]
The first values are
\[
A_0,\ldots,A_7=
1,1,3,15,121,1665,43883,2437423.
\]

If \(C_n\) counts ordered comparable orbit pairs \((O,O')\) with \(O\preceq O'\), then
\[
C_n=\sum_{\sigma\in\Pi_n}
\prod_{B\in\sigma}
\left(B_{|B|}2^{\binom{|B|}2}\right),
\]
where \(B_m\) is the \(m\)-th Bell number. Equivalently,
\[
\sum_{n\ge0}C_n\frac{z^n}{n!}
=
\exp\!\left(
\sum_{m\ge1}B_m2^{\binom m2}\frac{z^m}{m!}
\right).
\]
The first values are
\[
C_0,\ldots,C_7=
1,1,5,53,1193,60329,7071533,1893360157.
\]

## Assumptions and scope
A tournament is a loopless oriented complete graph. The random tournament is the unique countable homogeneous tournament whose age is the class of all finite tournaments. A bimorphism is a bijective endomorphism, and MB-homogeneity means that every finite partial monomorphism extends to a bimorphism.

The result concerns injective ordered tuples. Repetitions can be added afterward by a Stirling transform because every bijection preserves the equality pattern. No classification of individual bimorphisms is claimed.

## Proof
Take an injective ordered tuple \(\bar a=(a_1,\ldots,a_n)\). Put indices \(i,j\) in the same block exactly when \(a_i,a_j\) lie in the same component of \(M\). Each block therefore carries the tournament induced by its coordinates. Conversely, every set partition of \([n]\) decorated by one labeled tournament on each block occurs: place different blocks in different copies of the random tournament and use universality within each copy.

Two such tuples are in the same automorphism orbit exactly when their decorated partitions agree. Indeed, an automorphism permutes the connected tournament components and, inside each target component, homogeneity of the random tournament extends the finite labeled tournament isomorphism.

Now suppose a bimorphism sends a tuple in state \((\pi,\tau)\) to one in state \((\sigma,\upsilon)\). A bimorphism is an injective homomorphism. Every pair of vertices lying in one source component has an arc between them, so their images must remain in one target component and the arc orientation must be preserved. Hence every block of \(\pi\) lies inside a block of \(\sigma\), and \(\upsilon|_B=\tau_B\) on each old block.

Conversely, assume exactly those refinement and restriction conditions. Sending the source tuple coordinatewise to a representative of the target state is then an injective homomorphism between finite induced substructures: all source arcs occur within old blocks and are preserved, while pairs from different old blocks have no source relation and impose no homomorphism constraint. Coleman's MB-homogeneity result extends this finite partial monomorphism to a bimorphism of \(M\). This proves the reachability criterion.

Antisymmetry follows immediately: mutual reachability forces mutual refinement, hence identical partitions, and then identical block tournaments. A strict step can only coarsen the partition. It is a cover exactly when it decreases the number of blocks by one, i.e. merges two blocks; all orientations between those two old blocks were absent in the source and may be chosen freely in the target. Thus \(n-|\pi|\) is a rank function.

For enumeration, a block of size \(m\) admits \(2^{\binom m2}\) labeled tournaments. The exponential formula for set partitions decorated by these block structures gives the stated formula and exponential generating function for \(A_n\).

For comparable pairs, first fix the target decorated partition \(\sigma\). Within a target block \(B\), the source can refine \(B\) according to any of its \(B_{|B|}\) set partitions; once that refinement is chosen, all source block tournaments are forced by restricting the target tournament. Different target blocks are independent. Therefore that target partition contributes
\[
\prod_{B\in\sigma}B_{|B|}2^{\binom{|B|}2},
\]
and a second application of the exponential formula yields the generating function for \(C_n\).

A useful rank refinement is
\[
R_n(q)=\sum_{\pi\in\Pi_n}
2^{\sum_{B\in\pi}\binom{|B|}{2}}
q^{n-|\pi|},
\]
with bivariate exponential generating function
\[
\sum_{n\ge0}R_n(q)\frac{z^n}{n!}
=
\exp\!\left(
\sum_{m\ge1}2^{\binom m2}q^{m-1}\frac{z^m}{m!}
\right).
\]

## Verification
The accompanying `verify.py` enumerates every set partition through seven coordinates. It independently computes the orbit totals by decorated-partition weights and the comparable-pair totals in two ways: by the Bell-product formula and by explicitly testing every refinement relation through six coordinates. It also verifies every rank row, including the unique rank-zero state and the \(2^{\binom n2}\) top-rank tournament states.

The script returns `VERIFY_OK`. Its orbit and comparable-pair rows are
\[
(1,1,3,15,121,1665,43883,2437423)
\]
and
\[
(1,1,5,53,1193,60329,7071533,1893360157).
\]

## Relationship to prior work
Coleman's Example 5.13 explicitly considers the infinite disjoint union of copies of the countable random tournament and proves that it is HE-homogeneous; he then states that adapting the argument to monomorphism extension shows it is MB-homogeneous. His paper also defines monomorphisms as injective endomorphisms and bimorphisms as bijective endomorphisms. That MB-homogeneity theorem is the extension principle used here, not part of the originality claim.

Coleman's earlier thesis develops forward orbits for monoid actions, including componentwise actions on tuples, so the use of a reachability relation is aligned with the established monoid-action viewpoint. In the inspected thesis material, however, no decorated-partition classification or Bell/tournament enumerator for this random-tournament union was located.

Targeted searches were made for the exact object, for bimorphism-orbit preorders of disjoint unions of random tournaments, for oriented set partitions, and for the displayed Bell-number generating functions. The closest located results concern automorphism-orbit profiles of other homogeneous structures, not the bimorphism transition order here. The present contribution is therefore the explicit finite transition poset and its two exact enumerators.

## Limitations
The originality search cannot exclude an equivalent formulation hidden under transformation-monoid terminology not mentioning random tournaments. The formulas are immediate once the reachability classification is known, so the strongest content is the exact identification of the finite bimorphism action order. No asymptotic analysis of \(A_n\) or \(C_n\), and no structural classification of the full bimorphism monoid, is claimed.

## References
1. T. D. H. Coleman, “Two Fraïssé-style theorems for homomorphism-homogeneous relational structures,” *Discrete Mathematics* 343 (2020), 111674. DOI 10.1016/j.disc.2019.111674; arXiv:1812.01934. The first arXiv version was submitted 5 December 2018. Primary MSC 03C15.
2. T. D. H. Coleman, D. M. Evans, and R. D. Gray, “Permutation monoids and MB-homogeneity for graphs and relational structures,” *European Journal of Combinatorics* 78 (2019), 163–189; arXiv:1802.04166.
3. T. D. H. Coleman, *Automorphisms and endomorphisms of first-order structures*, PhD thesis, University of East Anglia, 2017.
