# Rank-two matrix sandwiches: three square-zero components and a rectangular balance transition

## Finding
Fix any field \(k\), integers \(a,b\geq0\), and a rank-two matrix \(J\in M_{(b+2)\times(a+2)}(k)\). Equip \(M_{(a+2)\times(b+2)}(k)\) with the associative sandwich multiplication \(X\star Y=XJY\). Let \(\mathcal Z_{a,b}(J)\) be the **reduced affine algebraic variety** of matrices with \(X\star X=0\), considered geometrically after extending scalars to an algebraic closure. The following statements hold in every characteristic.

**Component classification.** The reduced variety has exactly
\[
1+\mathbf 1_{a\ge2}+\mathbf 1_{b\ge2}
\]
geometrically irreducible components. One is a canonical line-incidence component of dimension \(ab+a+b+2\). When \(a\ge2\), an additional linear component has dimension \(ab+2a\); when \(b\ge2\), another linear component has dimension \(ab+2b\). For \(a,b\ge2\), the incidence component is the unique largest-dimensional component if \(|a-b|<2\), ties with a linear component when \(|a-b|=2\), and is overtaken by one linear component when \(|a-b|>2\). More precisely, the excess linear component is on the side with the larger of \(a,b\).

**Complete rational point count.** If \(k=\mathbb F_q\) for any prime power \(q\), the exact number of matrices with \(X\star X=0\) is
\[
\boxed{N_{a,b}(q)=q^{ab}\left[q\big((q+1)q^{a+b}-1\big)+(q^a-1)(q^a-q)+(q^b-1)(q^b-q)\right].}
\]
The summand \(q^{ab+1}((q+1)q^{a+b}-1)\) counts precisely the points of the incidence component. The two remaining nonnegative summands count the disjoint rank-two escape strata in the linear components. In particular, all boundary cases \(a=0,1\) or \(b=0,1\) are covered without exceptions.

**Component intersections.** If \(a,b\ge2\), the pairwise intersection of the incidence component with the linear component at \(Q=0\) is the rank-at-most-one determinantal cone in an \(a\)-by-two matrix, times the free \(a\)-by-\(b\) block, of dimension \(ab+a+1\). The corresponding intersection on the \(R=0\) side has dimension \(ab+b+1\). The two linear components intersect, as do all three, precisely along the common affine space of dimension \(ab\) where \(P=Q=R=0\).

## Assumptions and scope
The dimensions \(a,b\) may be zero. The ambient matrices are labeled, and the count is not divided by automorphisms. Square-zero means \(XJX=0\) in the **sandwich algebra**; it does not mean the ordinary rectangular matrix square, which may not even be defined. For geometric assertions, components are those of the reduced zero set; nothing here asserts that the possibly nonreduced defining quadratic equation scheme is reduced. Under invertible changes of row and column bases, every rank-two sandwich matrix is equivalent to the one with a leading \(I_2\) block and zeros elsewhere; the transformation preserves both the product and the zero-square condition.

Write a matrix in the normal form
\[
X=\begin{pmatrix}P&Q\\R&S\end{pmatrix},\qquad
P\in M_2(k),\quad Q\in M_{2\times b}(k),\quad R\in M_{a\times2}(k),\quad S\in M_{a\times b}(k).
\]
The block \(S\) is always unconstrained. All ranks below are ordinary matrix ranks over the indicated field.

## Proof
**1. Reduction to four equations.** In the stated normal form, direct block multiplication gives
\[
XJX=\begin{pmatrix}P^2&PQ\\RP&RQ\end{pmatrix}.
\]
Thus square-zero is equivalent to \(P^2=PQ=RP=RQ=0\). If \(P\ne0\), the \(2\)-dimensional square-zero operator \(P\) has rank one and \(\operatorname{im}P=\ker P=W\), a unique line. Then \(PQ=0\) means \(\operatorname{im}Q\subseteq W\), while \(RP=0\) means \(R(W)=0\); these two conditions already imply \(RQ=0\). Conversely, every such triple is a solution. A nonzero square-zero \(P\) is a nonzero element of the one-dimensional \(\operatorname{Hom}(k^2/W,W)\).

**2. A closed geometrically irreducible incidence component.** Let \(\mathcal I\) consist of pairs \((X,W)\) with \(W\in\mathbf P(k^2)\) and
\[
P(k^2)\subseteq W,\quad P(W)=0,\quad Q(k^b)\subseteq W,\quad R(W)=0,
\]
with \(S\) arbitrary. This is the total space of a vector bundle of rank \(1+b+a+ab\) over \(\mathbf P^1\): over a fixed line the allowed spaces for \(P,Q,R,S\) have the stated dimensions. Hence \(\mathcal I\) is geometrically irreducible of dimension \(ab+a+b+2\). The projection to the affine matrix space is closed because \(\mathbf P^1\) is proper. Call its image \(\mathcal C_{\mathrm{inc}}\). Whenever \(P\ne0\), its line \(W\) is uniquely recovered from \(P\), and these points form a dense open subset of \(\mathcal I\). Thus the image is geometrically irreducible and has the asserted dimension.

**3. The only other components.** At \(P=0\), the remaining equation is \(RQ=0\). If both \(Q\) and \(R\) have rank at most one, there exists a line \(W\) containing \(\operatorname{im}Q\) and contained in \(\ker R\): if \(Q\) has rank one use its image, if \(R\) has rank one and \(Q=0\) use its kernel, and if both vanish use any line. Thus the point lies in \(\mathcal C_{\mathrm{inc}}\). If \(Q\) has rank two, \(RQ=0\) forces \(R=0\); if \(R\) has rank two, it forces \(Q=0\). Consequently the full reduced zero locus is the union of the incidence component and the linear spaces
\[
\mathcal C_Q=\{P=R=0\},\qquad \mathcal C_R=\{P=Q=0\}.
\]
Their dimensions are \(ab+2b\) and \(ab+2a\). If \(b\le1\), every point of \(\mathcal C_Q\) is in the incidence component; if \(b\ge2\), its rank-two \(Q\) points prevent inclusion. The analogous equivalence holds for \(\mathcal C_R\) with \(a\). No remaining component can occur because the union exhausts the set. This proves the component count and dimensions. When \(a,b\ge2\), comparing \(ab+a+b+2\), \(ab+2a\), and \(ab+2b\) gives the stated balance transition.

**4. Intersections.** The condition \(\mathcal C_{\mathrm{inc}}\cap\mathcal C_Q\) forces \(P=R=0\) and \(\operatorname{rank}Q\le1\); its rank-one determinantal variety has dimension \(b+1\). The other incidence/linear intersection is obtained by reversing \(Q,R\) and has dimension \(a+1\). Their free \(S\) block contributes \(ab\) dimensions. The two linear spaces impose \(P=Q=R=0\), giving precisely the stated common intersection.

**5. Count over finite fields.** The projective line has \(q+1\) rational lines. For each line \(W\), the incidence fiber of \(X\) has \(q^{ab+a+b+1}\) points. Distinct-line fibers intersect only where \(P=Q=R=0\), which contributes exactly \(q^{ab}\) choices of \(S\). Every rational point of the incidence image has a rational witnessing line, as follows from the rank cases in Step 3. Therefore
\[
|\mathcal C_{\mathrm{inc}}(\mathbb F_q)|=(q+1)q^{ab+a+b+1}-q\,q^{ab}
=q^{ab}q\big((q+1)q^{a+b}-1\big).
\]
The points not in the incidence component are exactly: \(P=Q=0\) with \(R\) of rank two, or \(P=R=0\) with \(Q\) of rank two. These cases are disjoint. The numbers of full-column-rank \(a\)-by-two and full-row-rank two-by-\(b\) matrices are \((q^a-1)(q^a-q)\) and \((q^b-1)(q^b-q)\), respectively, each independently times \(q^{ab}\) choices of \(S\). Their sum with the incidence count proves the boxed formula. The rank-two counts vanish automatically for \(a,b<2\). This completes the proof.

## Verification
The standalone source `check_rank2.py` independently computes \(XJX\) by two actual matrix multiplications, exhaustively enumerates all \(X\) for eight small finite-field parameter triples, and verifies the original rank-stratified counting formula equivalent to the boxed symmetric expression. Tested examples include \((q,a,b)=(2,2,2)\), with exactly \(1696\) solutions among \(2^{16}\) matrices; \((3,1,1)\), with \(315\) solutions; and \((4,0,1)\), with \(76\) solutions, using explicit arithmetic in \(\mathbb F_4\). Its captured output `check-rank2-output.txt` ends in `ALL RANK-TWO CHECKS PASSED`. An independent integer evaluation checked the equivalence of the two closed expressions for \(q\in\{2,3,4,5,7\}\) and \(0\le a,b\le6\). Finite checks corroborate but do not replace the all-fields component proof or the exact counting derivation.

## Relationship to prior work
Dolinka and East, *Semigroups of rectangular matrices under a sandwich operation* (arXiv:1503.03139, first public 2015-03-11), establish this precise sandwich-semigroup setting and analyze its regular elements, Green relations, idempotents, and generators. Their full accessible manuscript was inspected, in particular its structural and idempotent sections. Neither the present rank-two square-zero fiber classification nor this three-component balance transition is stated in the inspected treatment. The rank and product normal forms are standard and are not claimed as discoveries.

De Concini and Strickland, *On the variety of complexes* (1981), study loci of composable maps with zero composition. The slice \(P=0\) of the present equations is exactly one such two-map zero-product variety, \(RQ=0\); this established connection is acknowledged. However, the incidence component incorporating **nonzero square-zero \(P\)** and its competition with two rank-two edge components is additional. The full 1981 primary article was not available for material inspection; a possible implicit treatment of this enlargement is a residual priority risk.

The published *Joint matrix-rank spectrum of commuting idempotents in rectangular sandwich semigroups* (published-finding corpus, 2026-10-13) concerns pairs satisfying \(XJX=X\) and their mutual commutation, not the set \(XJX=0\) or its geometry. The published *Commutator-rank census of finite rectangular-band semigroup algebras* (published-finding corpus, 2026-11-02) gives a rank-one sandwich model's commutators, not this rank-two single-element zero-square locus. The published *Thirteen-periodic maximal-component counts for square-zero sandwich representations* (published-finding corpus, 2026-11-08) concerns variable pairs \((P,N)\) with \(P^2=P\), \(N^2=0\) and \(PNP=0\); its parameter space and equations differ substantially from a fixed rank-two sandwich matrix. Their inspected full statements do not imply the present three-component classification or point-count identity without separate new arguments. These comparisons do not certify global historical uniqueness.

## Limitations
The assertions concern rank-two sandwich matrices. They do not determine higher-rank sandwiches, nonzero prescribed square fibers \(XJX=Y\), finer scheme nilpotents, or automorphism-orbit counts. Intersections are described only for the reduced geometric varieties. No claim of independence, exhaustive historical priority, or formal-machine proof is made. Uninspected historical treatments of varieties of complexes or Munn rings could contain equivalent consequences.

## References
1. I. Dolinka and J. East, *Semigroups of rectangular matrices under a sandwich operation*, arXiv:1503.03139v1 (2015-03-11), https://arxiv.org/abs/1503.03139.
2. C. De Concini and E. Strickland, *On the variety of complexes*, Advances in Mathematics 41 (1981), 57–77, https://doi.org/10.1016/S0001-8708(81)80004-7.
3. *Joint matrix-rank spectrum of commuting idempotents in rectangular sandwich semigroups*, 2026-10-13, https://github.com/published-finding corpus/2026/blob/main/2026/10/13/SCOPE-joint-matrix-rank-spectrum-of-commuting-idempotents-in-rectangul--85aa4c5711c9/RESULT.md.
4. *Commutator-rank census of finite rectangular-band semigroup algebras*, 2026-11-02, https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-commutator-rank-census-of-finite-rectangular-band-semigroup-alge--6f0f9b3726a9/RESULT.md.
5. *Thirteen-periodic maximal-component counts for square-zero sandwich representations*, 2026-11-08, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-thirteen-periodic-maximal-component-counts-for-square-zero-sandw--c3993cce10c6/RESULT.md.
