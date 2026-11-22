# Zeta function and rational-branch spectra of the complete Hermitian tangent divisor

## Finding
For every prime power \(q\ge2\), let \(H\) be the smooth plane Hermitian curve \(X^{q+1}+Y^{q+1}+Z^{q+1}=0\) over \(\mathbb F_q\). Let \(D\) be the reduced union of the tangent lines at its \(q^3+1\) points over \(\mathbb F_{q^2}\), considered as a curve over \(\mathbb F_q\). Write \(E=q^2(q^2-q+1)\), \(A=(q^3+q+2)/2\), \(B=(q^3-q)/2\), and \(c=q^4(q-1)/2\).

The divisor \(D\) consists of \(q^3+1\) distinct lines. Its singularities are exactly \(E\) ordinary \((q+1)\)-fold crossings, all defined over \(\mathbb F_{q^2}\). Exactly \(q^2\) of these crossings are \(\mathbb F_q\)-rational; the other \((E-q^2)/2\) form degree-two closed points. There are exactly \(q+1\) rational component lines; the rest are \((q^3-q)/2\) conjugate pairs. The all-extension point-count formula is
\[
\#D(\mathbb F_{q^m})=\begin{cases}(q+1)q^m+1,&m\text{ odd},\\ (q^3+1)q^m-q^5+q^4+1,&m\text{ even}.\end{cases}
\]
Consequently the zeta function over \(\mathbb F_q\) is
\[
Z(D/\mathbb F_q,T)=\frac{(1-T)^{c-1}(1+T)^c}{(1-qT)^A(1+qT)^B}.
\]
In particular, \(D\) contains every point of \(\mathbb P^2(\mathbb F_q)\) and every point of \(\mathbb P^2(\mathbb F_{q^2})\).

The rational branch spectrum of the \(q^2\) rational crossings depends sharply on parity. For odd \(q\), precisely \(q(q+1)/2\) rational crossings have two \(\mathbb F_q\)-rational branches, and the other \(q(q-1)/2\) have none. For even \(q\), one rational crossing has \(q+1\) rational branches, while the other \(q^2-1\) rational crossings have exactly one. Here a rational branch means a point of the normalization rational over \(\mathbb F_q\).

## Assumptions and scope
The standard Hermitian equation is defined over \(\mathbb F_q\); its tangent lines at \(\mathbb F_{q^2}\)-points individually need not descend to \(\mathbb F_q\), but their reduced union does. All points and crossings refer to geometric support, with the indicated descent. The parameter \(q\) is any prime power, including powers of two. The zeta function is that of the singular reduced projective curve, not the zeta function of its normalization or the smooth Hermitian curve.

## Proof
Write \(k=\mathbb F_{q^2}\) and let \(h(a,b)=\sum_{i=0}^2a_i^q b_i\) be the nondegenerate Hermitian form on \(k^3\). Its isotropic projective points are precisely \(H(k)\). There are \(q^3+1\) such points, and the tangent at an isotropic point \(a\) is the line \(h(a,b)=0\). The nondegenerate form identifies isotropic points bijectively with tangent lines.

If \(b\) is isotropic, the plane \(b^\perp\) has radical \(kb\) and contains no other isotropic projective point; consequently exactly one tangent line passes through \([b]\). If \(b\) is nonisotropic, \(b^\perp\) is a nondegenerate Hermitian plane, with exactly \(q+1\) isotropic projective points. Consequently every external \(k\)-point lies on exactly \(q+1\) of the chosen tangents. Distinct tangent lines meet at an external \(k\)-point, and every external point is such an intersection. As \(\#\mathbb P^2(k)=q^4+q^2+1\), there are \(E=q^4+q^2-q^3=q^2(q^2-q+1)\) distinct ordinary \((q+1)\)-fold crossings and no others. The ordinary nature follows because the components are distinct lines through each crossing.

The coefficientwise \(q\)-Frobenius permutes the tangents through the bijection with \(H(k)\). Exactly the \(q+1\) points of \(H(\mathbb F_q)\) are fixed; the remaining tangent components occur in conjugate pairs. The \(\mathbb F_q\)-points of the singular locus are exactly the external \(\mathbb F_q\)-points, in number \((q^2+q+1)-(q+1)=q^2\); all other crossings are quadratic closed points.

For \(m\) odd, an \(\mathbb F_{q^m}\)-point of the normalization lies on a fixed component line; there are \((q+1)(q^m+1)\) normalization points. The rational crossings are just the \(q^2\) external \(\mathbb F_q\)-points. Each of the \(q+1\) rational tangent lines contains exactly one rational Hermitian point and \(q\) rational external points, so the total number of rational normalization branches above rational crossings is \(q(q+1)\). Identifying these branches yields \((q+1)(q^m+1)-q(q+1)+q^2=(q+1)q^m+1\) curve points. For \(m\) even, all \(q^3+1\) lines and all \(E\) crossings split; normalization has \((q^3+1)(q^m+1)\) points, and each crossing identifies \(q+1\) branches into one. Subtracting \(qE\) gives the stated even formula. The displayed zeta function follows from \(\log Z=\sum_{m\ge1}\#D(\mathbb F_{q^m})T^m/m\) and the identity \(\#D(\mathbb F_{q^m})=1-c-c(-1)^m+Aq^m+B(-q)^m\).

Finally, the rational tangent lines are the dual points of \(H(\mathbb F_q)\). If \(q\) is odd, these points form a nonsingular conic in the dual rational plane, so no three rational tangent lines are concurrent. Their \(\binom{q+1}{2}\) intersections are distinct, with two rational branches; the other external rational points have none. If \(q\) is even, \(H(\mathbb F_q)\) is the rational line \(X+Y+Z=0\), and its dual tangent lines all pass through one rational external point. At every other rational external point there is precisely one rational tangent line, since the \(q+1\) concurrent rational lines cover the entire rational projective plane. This proves both branch spectra.

## Verification
The independent finite-field incidence enumeration in `VERIFY.py` checks \(q=2\) and \(q=3\) using explicit quadratic-field arithmetic, all projective points and tangent lines, the crossing multiplicities, the full rational-branch distributions, and the rational-plane covering property. These are finite checks only; the proof above establishes the uniform result for arbitrary prime powers.

The component and crossing counts also satisfy the pairwise line-intersection identity \(E\binom{q+1}{2}=\binom{q^3+1}{2}\). The arithmetic genus is \((q^3)(q^3-1)/2\), compatible with the normalization defect formula \(p_a=E\binom{q+1}{2}-(q^3+1)+1\).

## Relationship to prior work
The classical Hermitian unital point count, tangent uniqueness, and polar incidence geometry are prior knowledge, as described by Thas (1992). Shimada (2012) studies totally tangent rational normal curves to Hermitian varieties, not the reduced union of all Hermitian-point tangent lines. Durante--Siciliano (2012) also describes the unital/tangent incidence, but not the all-extension zeta function and parity-dependent rational normalization-branch spectra. The result isolates their arithmetic consequences over the prime-power subfield and proves the complete curve-level zeta and branch classification. The input unital incidence is explicitly credited, not claimed original.

## Limitations
The conclusions concern this standard \(\mathbb F_q\)-model of the full tangent divisor, not arbitrary twists or a single chosen subarrangement. The zeta function is a formal invariant of a reducible singular curve; it is not a new assertion about the zeta function of the smooth Hermitian curve. The calculation relies on classical Hermitian incidence and does not claim that incidence itself is new. Priority among older finite-geometry sources is not exhaustively certified; an unindexed calculation of the same tangent-union zeta function remains a possibility. External independent mathematical review has not been performed.

## References
- J. A. Thas, *A Combinatorial Characterization of Hermitian Curves*, Journal of Algebraic Combinatorics **1** (1992), 97--102, https://studylib.net/doc/10958683/journal-of-algebraic-combinatorics-1--1992---97-102 (standard unital and tangent-incidence structure).
- I. Shimada, *A note on rational normal curves totally tangent to a Hermitian variety*, arXiv:1203.4047v1, posted 2012-03-19, https://arxiv.org/abs/1203.4047 (related Hermitian tangency, different subvarieties).
- N. Durante and A. Siciliano, *Unitals of PG(2,q²) Containing Conics* (2012), https://www.academia.edu/17923160/Unitals_of_PG_2_q2_Containing_Conics (classical unitals and tangent counts).
