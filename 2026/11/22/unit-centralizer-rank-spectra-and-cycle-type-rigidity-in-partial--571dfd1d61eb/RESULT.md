# Unit-centralizer rank spectra and cycle-type rigidity in partial Brauer monoids

## Finding
Let \(n\ge 1\), and let \(\mathcal{PB}_n\) be the partial Brauer monoid of partitions of a top and bottom copy of \([n]\), with blocks of cardinality at most two. Its rank \(\operatorname{rk}(\alpha)\) is the number of blocks joining a top vertex to a bottom vertex. For a unit \(\sigma\in S_n\subseteq\mathcal{PB}_n\), put
\[
C_\sigma(u)=\sum_{\substack{\alpha\in\mathcal{PB}_n\\\alpha\sigma=\sigma\alpha}}u^{\operatorname{rk}(\alpha)}.
\]
If \(m_\ell\) denotes the number of cycles of length \(\ell\) of \(\sigma\), define \(s_\ell=1+\mathbf1_{2\mid\ell}\). Then **the complete rank polynomial** is
\[
\boxed{C_\sigma(u)=\prod_{\ell\ge1}(m_\ell!)^2[x^{m_\ell}y^{m_\ell}]
\exp\!\left(s_\ell(x+y)+\frac{\ell}{2}(x^2+y^2)+\ell u^\ell xy\right).}
\tag{1}
\]
This factorization determines the precise ranks that occur:
\[
[u^r]C_\sigma(u)>0\iff r=\sum_{\ell\ge1}\ell k_\ell\quad(0\le k_\ell\le m_\ell).
\tag{2}
\]
The leading coefficient is \(z_\sigma=\prod_{\ell\ge1}\ell^{m_\ell}m_\ell!\), the order of the ordinary permutation centralizer. **Rigidity:** the one polynomial \(C_\sigma(u)\) determines every \(m_\ell\). In particular,
\[
C_\sigma(u)=C_\tau(u)\quad\Longleftrightarrow\quad\sigma,\tau\text{ have the same cycle type}.
\tag{3}
\]
Also, the number of unit-conjugacy orbits of rank \(r\) in \(\mathcal{PB}_n\) is
\[
\boxed{\sum_{\lambda\vdash n}\frac{[u^r]C_\lambda(u)}{z_\lambda}},
\qquad z_\lambda=\prod_{\ell\ge1}\ell^{m_\ell(\lambda)}m_\ell(\lambda)!.
\tag{4}
\]
Here \(C_\lambda\) is formula (1) for any permutation of cycle type \(\lambda\).

## Assumptions and scope
The two vertex rows are distinct. Singleton blocks and two-element blocks are allowed, and multiplication is ordinary partition-diagram concatenation, discarding components wholly inside the middle row. There are no planarity restrictions or weights from closed components. The units are the permutation diagrams \(S_n\). Equations (1)--(4) concern centralizers of **units** in the full partial Brauer monoid, not arbitrary diagram centralizers, and are valid for every positive integer \(n\) without reference to a coefficient field. Formal power series and coefficient extraction are over \(\mathbb Q[x,y,u]\) (with the displayed coefficient in fact integral).

## Proof
**1. Conjugation is diagonal relabeling.** Multiplication by permutation diagrams permutes the corresponding top or bottom labels. Thus \(\alpha\sigma=\sigma\alpha\) is equivalent to invariance of the matching represented by \(\alpha\) under simultaneous action of \(\sigma\) on both vertex rows. The equivalence can also be seen by conjugating with the inverse permutation diagram.

**2. Classification of invariant matching edges.** On the doubled vertex set, every two-element block is an edge of a partial matching. Invariance makes the partner map (where defined) an equivariant partial involution under \(\langle\sigma\rangle\). Hence an entire \(\sigma\)-cycle of vertices is either left entirely as singleton blocks, paired internally, or paired bijectively with a different vertex cycle of the **same length**. If two distinct cycles each have length \(\ell\), there are exactly \(\ell\) equivariant pairings, specified by the image of one vertex. Within a single cycle, a fixed-point-free equivariant involution must be translation by an offset \(h\) satisfying \(2h\equiv0\pmod\ell\) and \(h\not\equiv0\); it exists uniquely when \(\ell\) is even, then pairs opposite vertices. Therefore each unpaired orbit has \(s_\ell\) internal choices: all singleton or, for even \(\ell\), antipodal pairs.

**3. Counting by length and rank.** Fix \(\ell\) and write \(m=m_\ell\). There are \(m\) distinguishable top cycles and \(m\) distinguishable bottom cycles. An isolated cycle contributes \(s_\ell x\) or \(s_\ell y\); joining two top cycles contributes \(\ell x^2/2\), joining two bottom cycles contributes \(\ell y^2/2\), and joining one top and one bottom cycle contributes \(\ell u^\ell xy\), since that pair forms \(\ell\) transversal edges. The labeled-set exponential formula, with \(m!\) for each color, gives the \(\ell\)-factor of (1). Distinct lengths cannot pair, so factors multiply. Every transversal pair consumes one top and one bottom \(\ell\)-cycle. Therefore \(k_\ell\) can be any integer from \(0\) to \(m_\ell\), proving (2). Taking all cycles transversal produces \(m_\ell!\ell^{m_\ell}\) matchings for length \(\ell\), giving \(z_\sigma\).

**4. Recovering all cycle multiplicities.** Let \(P_{\ell,m}(u)\) be the \(\ell\)-factor in (1), with \(P_{\ell,0}=1\), and define
\[
Q_{\ell,m}(t)=\frac{t^{\ell m}P_{\ell,m}(t^{-1})}{\ell^m m!}.
\]
Its constant term is one. To lower the rank by exactly \(\ell\) while using only length-\(\ell\) cycles, exactly one top and one bottom cycle must be excluded from transversals; each has \(s_\ell\) internal choices. There are \(m^2(m-1)!\ell^{m-1}s_\ell^2\) such matchings. Consequently
\[
Q_{\ell,m}(t)=1+\frac{ms_\ell^2}{\ell}t^\ell+O(t^{2\ell}).
\tag{5}
\]
The normalized reversed polynomial
\[
R_\sigma(t)=\frac{t^nC_\sigma(t^{-1})}{z_\sigma}=\prod_{\ell\ge1}Q_{\ell,m_\ell}(t)
\]
has constant term one. At stage \(\ell\), divide \(R_\sigma\) formally by the already recovered factors \(Q_{d,m_d}\) for \(d<\ell\), and take the coefficient of \(t^\ell\). Terms from \(d>\ell\) have no such coefficient, and (5) recovers \(m_\ell\) as \(\ell/s_\ell^2\) times that coefficient. Induction gives all cycle multiplicities and proves (3), including zero multiplicities.

**5. Unit-conjugacy orbits.** The unit group \(S_n\) acts on \(\mathcal{PB}_n\) by conjugation, preserving diagram rank. Its fixed rank-\(r\) diagrams at \(\sigma\) are counted by \([u^r]C_\sigma\). Burnside's lemma gives the average over \(S_n\). Grouping permutations by partitions of \(n\), with class size \(n!/z_\lambda\), gives (4).

## Verification
The standalone Python checker `verify.py` independently constructs all partial matchings on \(2n\) vertices, implements diagram multiplication, computes the predicted polynomials through an integer recursion on unmatched cycles, and compares results. For \(1\le n\le4\), it checks **every diagram against every permutation** with direct multiplication as well as diagonal relabeling; for \(n=5\) it checks one representative of each cycle type by explicit matching enumeration. The cycle-recovery formula is checked through \(n=6\), and identity-permutation rank counts are also checked against an independent elementary product count through \(n=6\). Details and captured output appear in `verification_output.txt`. These finite computations are consistency tests, not the proof of an infinite theorem.

Examples: for a single \(\ell\)-cycle, \(C_\sigma(u)=s_\ell^2+\ell u^\ell\). For cycle type \((2,1)\), \(C_\sigma(u)=4+4u+2u^2+2u^3\). The unit-orbit rank polynomial for \(n=3\) is \(5+8u+4u^2+3u^3\).

## Relationship to prior work
Dolinka, East, and Gray describe the partial Brauer monoid and its Green structure, rank ideals, and idempotent generation in arXiv:1512.02279; their diagram definition and rank convention are the archival starting point. Halverson and Jacobson, arXiv:1808.08118, §5.3, give fixed-diagram formulas for **vertically symmetric** diagrams in irreducible-module character calculations for rook-Brauer algebras. Those fixed sets are not the full matching sets considered in (1), and no reconstruction of the unit cycle type from the all-diagram rank-centralizer polynomial is supplied there. Araújo et al., arXiv:2301.04252, §5, study natural semigroup conjugacy and normal forms; this is a different relation from the unit action and does not enumerate rank-wise fixed diagrams. There is also related work on rank spectra of centralizers of nilpotent partial injections in the symmetric inverse monoid; it involves neither the partial Brauer hooks nor permutation-unit centralizers. The present claim is the combined complete formula (1), rank support and cycle-type rigidity (3), with (4) as an orbit enumeration consequence. Standard labeled matching enumeration and Burnside's lemma are not themselves claimed as new.

## Limitations
The result applies only to commuting with a permutation unit, not arbitrary elements of \(\mathcal{PB}_n\), and does not classify natural semigroup-conjugacy classes. It gives polynomial-time coefficient recurrences for a fixed cycle type via generating functions but makes no optimal complexity claim. Priority may be affected by an unidentified equivalent cycle-index formula for diagonally invariant matchings; no claim of independent priority certification is made.

## References
1. I. Dolinka, J. East, R. D. Gray, *Motzkin monoids and partial Brauer monoids*, arXiv:1512.02279, first version 7 December 2015, https://arxiv.org/abs/1512.02279 .
2. T. Halverson, T. N. Jacobson, *Set-partition tableaux and representations of diagram algebras*, arXiv:1808.08118, §5.3, https://arxiv.org/abs/1808.08118 .
3. J. Araújo et al., *Conjugacy in Abstract Semigroups, Transformation and Diagram Monoids, and Conjugacy Growth*, arXiv:2301.04252, §5, https://arxiv.org/abs/2301.04252 .
