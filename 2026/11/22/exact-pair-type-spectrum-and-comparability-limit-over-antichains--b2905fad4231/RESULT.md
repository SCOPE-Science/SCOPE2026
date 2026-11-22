# Exact pair-type spectrum and comparability limit over antichains in the generic linearly ordered poset

## Finding
Let \(\mathcal L=(L,\prec,<)\) be the countable Fraïssé limit of finite *linearly ordered posets*: \(\prec\) is a strict partial order and \(<\) is a strict linear order extending it. Let \(A_n=\{a_1<\cdots<a_n\}\), \(n\ge0\), be an individually named induced \(\prec\)-antichain. For complete types of injective **ordered** pairs \((x,y)\) with \(x,y\notin A_n\), write \(C_n\) for the number with \(x\) and \(y\) \(\prec\)-comparable, \(I_n\) for the number with \(x\parallel_\prec y\), and \(T_n=C_n+I_n\).

Then, for **every** \(n\ge0\),
\[
\boxed{C_n=8\cdot4^n+18\cdot3^n-(10n+22)2^n-2,}
\]
\[
\boxed{I_n=\frac{32\cdot4^n+54\cdot3^n-(24n+120)2^n+3n^2+21n+40}{3},}
\]
and
\[
\boxed{T_n=\frac{56\cdot4^n+108\cdot3^n-(54n+186)2^n+3n^2+21n+34}{3}.}
\]
In particular, under **uniform counting of complete pair types**, not a measure on realized pairs,
\[
\lim_{n\to\infty}\frac{C_n}{T_n}=\frac37,\qquad
\lim_{n\to\infty}\frac{I_n}{T_n}=\frac47.
\]
There are \(U_n=2^{n+2}-n-3\) nonalgebraic complete one-point types over \(A_n\), and the exact counts also imply
\[
\lim_{n\to\infty}\frac{T_n}{U_n^2}=\frac76.
\]
The first values of \((C_n,I_n,T_n)\), for \(n=0,1,2,3,4,5\), are respectively \((2,2,4)\), \((20,22,42)\), \((120,140,260)\), \((580,700,1280)\), \((2512,3094,5606)\), and \((10260,12810,23070)\).

## Assumptions and scope
The finite base is an antichain **in the partial order** but has its prescribed linear order \(a_1<\cdots<a_n\); its labels are fixed pointwise. The coordinates \(x\) and \(y\) are distinct and lie outside the base. Both the partial order and its named linear extension are part of the first-order language. The Fraïssé extension property and ultrahomogeneity identify complete finite-tuple types with precisely the finite induced linearly ordered posets extending the labelled base. The case \(n=0\) is included and gives the four possible pair types.

The linear order may have \(x<y\) or \(y<x\). Reversing variable names gives the same count in each case. Fix \(x<y\) for the proof, and let \(l,m,r\ge0\), \(l+m+r=n\), denote the numbers of old parameters left of \(x\), strictly between \(x,y\), and right of \(y\) in the linear order.

## Proof
**1. One-point patterns.** At a gap after \(i\) old parameters, a new point can lie strictly above an arbitrary subset of those \(i\) left parameters, strictly below an arbitrary subset of the \(n-i\) right parameters, or be incomparable with all. Both a nonempty lower and a nonempty upper subset would make two old antichain elements comparable by transitivity. Thus the gap contributes
\[
u_i=2^i+2^{n-i}-1.
\]
Summing \(u_i\) over \(0\le i\le n\) gives \(U_n=2^{n+2}-n-3\).

**2. Incomparable new vertices.** Put \(i=l\) and \(j=l+m\). The independently legal unary patterns for \(x\) and \(y\) number
\[
t_x=2^l+2^{m+r}-1,\qquad t_y=2^{l+m}+2^r-1.
\]
If \(x\parallel_\prec y\), the only *additional* possible transitivity violation is a parameter \(a\) with \(x\prec a\prec y\). Such a parameter must lie among the \(m\) middle parameters. To count pairs of unary patterns containing at least one such witness, choose their two potentially overlapping incidence subsets: the set of old elements strictly above \(x\) has \(m+r\) available positions, and the set strictly below \(y\) has \(l+m\). There are \(2^{l+r}4^m\) pairs of these subsets, of which \(2^{l+r}3^m\) avoid intersection on all middle positions. An intersecting pair necessarily uses two nonempty subsets, so no correction for the empty type is needed. Every other pair of legal unary patterns produces a transitive finite extension with \(x\parallel_\prec y\): paths through a single new vertex are already excluded by unary legality, and paths through both would imply one of the forbidden middle witnesses. Therefore the exact incomparable count for this placement is
\[
\boxed{J(l,m,r)=t_xt_y-2^{l+r}(4^m-3^m).}
\]

**3. Comparable new vertices.** Suppose \(x\prec y\). A left parameter has three possible statuses: unrelated, below \(y\) only, or below \(x\) (hence below both). A middle parameter has four: unrelated, below \(y\) only, above \(x\) only, or strictly between \(x\) and \(y\) in the partial order. A right parameter has three: unrelated, above \(x\) only, or above \(y\) (hence above both).

Call the last left status \(A\) and the last right status \(D\). If no \(A\) and no \(D\) occur, all assignments within the resulting two-, four-, and two-choice alphabets are legal; this gives \(2^{l+r}4^m\) assignments. If at least one \(A\) occurs, transitivity and the old antichain force every right parameter to be unrelated and each middle parameter to be either unrelated or below \(y\) only. There are \((3^l-2^l)2^m\) such assignments. Dually, at least one \(D\) forces all left parameters to be unrelated and permits only unrelated/above-\(x\) middle statuses; this gives \((3^r-2^r)2^m\) assignments. Cases containing both \(A\) and \(D\) are impossible, so the cases are disjoint and exhaustive. Hence the comparable count for this placement is
\[
\boxed{H(l,m,r)=2^{l+r}4^m+(3^l+3^r-2^l-2^r)2^m.}
\]
All surviving patterns satisfy transitivity: the enumerated forbidden mixed statuses are exactly the ways to force a relation between two distinct old antichain elements, while the required consequences of \(x\prec y\) are already incorporated into each local status. This proves sufficiency rather than just necessity.

**4. Summation and closed forms.** Each triple \((l,m,r)\) corresponds to exactly one relative linear-order placement \(x<y\). Interchanging the variable names doubles the count, giving
\[
C_n=2\sum_{l+m+r=n}H(l,m,r),\qquad
I_n=2\sum_{l+m+r=n}J(l,m,r).
\]
For a short check of the coefficient extraction, write \(h(z)=\sum_{n\ge0}C_nz^n/2\) and \(j(z)=\sum_{n\ge0}I_nz^n/2\). Independent geometric sums over \(l,m,r\) give
\[
h(z)=\frac1{(1-2z)^2(1-4z)}+
\frac2{(1-3z)(1-2z)(1-z)}-
\frac2{(1-2z)^2(1-z)},
\]
and, setting
\[
\begin{aligned}
p(z)={}&\frac2{(1-4z)(1-2z)(1-z)}+
\frac1{(1-2z)^2(1-4z)}\\
&-\frac1{(1-2z)^2(1-z)}-
\frac2{(1-2z)(1-z)^2}+\frac1{(1-z)^3},
\end{aligned}
\]
we have
\[
j(z)=p(z)-\frac1{(1-2z)^2(1-4z)}+
\frac1{(1-2z)^2(1-3z)}.
\]
Here \(p(z)\) is exactly the generating series for \(\sum_{l+m+r=n}t_xt_y\). Partial fractions of \(2h(z)\) and \(2j(z)\), or direct coefficient extraction using \((1-az)^{-2}\) and \((1-z)^{-3}\), yield all three boxed formulas. Since \(C_n=8\cdot4^n+O(n2^n+3^n)\), \(I_n=(32/3)4^n+O(n2^n+3^n)\), and \(U_n\sim4\cdot2^n\), the limits are \(8/(8+32/3)=3/7\), \(4/7\), and \((56/3)/16=7/6\). No extrapolation from finite computations is used.

## Verification
The standalone pure-Python program `verify.py` independently enumerates every subset of possible partial-order comparisons for every ordered insertion placement \((l,m,r)\) with \(0\le n\le5\), testing all transitivity consequences rather than using the local-state argument. It verifies the two placement formulas and their sum against the exact closed forms. It then checks the placement sums and the formulas through \(n=40\). The recorded run in `verification_output.txt` ends `VERIFICATION_OK`. These are finite checks only; the unrestricted result is proved by the preceding exhaustive structural classification and generating-function identities.

## Relationship to prior work
Dolinka and Mašulović's 2012 classification of homogeneous linearly ordered posets, including the Fraïssé limit of all finite linearly ordered posets, supplies the underlying structure and its uniqueness, **not** the displayed parameter-relative two-type enumeration. The earlier published *Exact two-point and fixed-arity type spectra over antichains in the random poset* determines \(4\cdot4^n+6\cdot3^n-8\cdot2^n+1\) for the **pure partial-order reduct** with no named linear extension and asymptotic comparability frequency \(1/2\). That result does not imply the new \(3/7\) fraction or the exact placement-weighted ordered expansion formula without additional enumeration. The earlier *Exact ordered-pair type spectrum over complete height-two parameter posets* likewise concerns the **pure** random poset and comparability between two antichain levels, not a second linear-order relation on the same domain. The present formulas concern a different Fraïssé age and the new obstruction due to insertions into prescribed linear-order gaps. A hidden equivalent weighted-counting identity in historical order-enumeration literature remains possible.

## Limitations
The theorem is for induced named antichains and injective ordered nonparameter pair types. It does not classify arbitrary named parameter posets, tuples of higher arity, probability of comparable **actual random elements**, or all finite ordered-poset orbit profiles. The source comparison is best-of-knowledge and does not establish absolute historical priority.

## References
1. Igor Dolinka and Dragan Mašulović, *Countable homogeneous linearly ordered posets*, European Journal of Combinatorics 33 (2012), 1965–1973, DOI: 10.1016/j.ejc.2012.06.006, available online 2012-07-15. https://doi.org/10.1016/j.ejc.2012.06.006
2. *Exact two-point and fixed-arity type spectra over antichains in the random poset*, 2026 public research record. https://github.com/published-finding corpus/2026/blob/main/2026/10/25/SCOPE-exact-two-point-and-fixed-arity-type-spectra-over-antichains-in--3d742ffe8f7d/RESULT.md
3. *Exact ordered-pair type spectrum over complete height-two parameter posets*, 2026 public research record. https://github.com/published-finding corpus/2026/blob/main/2026/10/26/SCOPE-exact-ordered-pair-type-spectrum-over-complete-height-two-parame--8b01eae861b0/RESULT.md
