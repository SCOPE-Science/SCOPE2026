# Sharp ridge-skeleton lower bound for all Euclidean products of simplices containing the unit ball

## Finding
For every integer \(n\ge3\), every orthogonal Cartesian product \(P=S_1\times\cdots\times S_r\subset\mathbb R^n\) of positive-dimensional nondegenerate Euclidean simplices that contains a Euclidean ball of radius one satisfies
\[
\Phi_{n-2}(P)=\sum_{F:\,\dim F=n-2}\mathcal H^{n-2}(F)\ge 2^n\binom{n}{2}.
\]
Equality holds precisely for translates of \([-1,1]^n\) with an orthonormal coordinate frame. In particular, if at least one simplex factor has dimension at least two, the inequality is strict. The hypothesis is simply containment of a unit ball; no higher-codimension face-distance hypothesis is needed.

## Assumptions and scope
The factors \(S_i\) have positive dimensions \(d_i\) with \(\sum_i d_i=n\). The product uses the standard orthogonal product Euclidean metric; each factor is a compact full-dimensional simplex in its affine span. Denote by \(\Phi_k(Q)\) the sum of \(k\)-dimensional Hausdorff measures of the distinct \(k\)-faces of \(Q\), and put \(\Phi_0(Q)\) equal to its vertex count. The top coefficient \(\Phi_{\dim Q}(Q)\) means the volume of \(Q\). A unit ball inside \(P\) projects onto a unit ball inside every factor. Each factor may be translated to its own incenter without changing any face measures.

## Proof
**1. Factorwise comparison.** For \(d\ge2\), the fixed-inradius simplex theorem of Basit and Lángi [2, Theorem 8] says that, for each \(1\le k\le d-1\), the total \(k\)-face content of any \(d\)-simplex of inradius one is no smaller than that of the regular such simplex \(T_d\). Its vertex count is always \(d+1\). Its volume is also minimized by \(T_d\): every simplex is tangential, so \(d\operatorname{vol}(S)=r(S)\Phi_{d-1}(S)\). A factor of inradius at least one can be rescaled down to inradius one, making all positive-dimensional face measures no larger; for \(d=1\), a segment containing a unit ball has length at least two. Consequently all face coefficients of each factor dominate those of \(T_{d_i}\), with \(T_1=[-1,1]\). A face of an orthogonal product is a product of factor faces, and its Euclidean face volume is the product of their volumes. Thus the face polynomials
\[
F_Q(z)=\sum_{k=0}^{\dim Q}\Phi_k(Q)z^k
\]
satisfy \(F_{P}(z)=\prod_iF_{S_i}(z)\), and their coefficientwise positivity reduces the claim to products of regular inradius-one simplices.

**2. Regular-simplex face measures.** The side length of \(T_d\) is \(\sqrt{2d(d+1)}\), so its \(k\)-face total is
\[
\Phi_k(T_d)=\binom{d+1}{k+1}\frac{[d(d+1)]^{k/2}\sqrt{k+1}}{k!},\quad 0\le k\le d.
\]
Let \(V_d=\operatorname{vol}(T_d)\), \(A_d=V_d/2^d\), \(c_1=0\), and for \(d\ge2\) put
\[
 c_d=\frac{\Phi_{d-2}(T_d)}{V_d}=\binom d2\sqrt{\frac{d-1}{d+1}},\qquad
 \delta_d=\binom d2-c_d.
\]
For all \(d\ge1\), \(\Phi_{d-1}(T_d)=dV_d\). Therefore, separating codimension two into (i) two missing dimensions in one factor and (ii) one missing dimension in each of two distinct factors, we obtain the exact identity
\[
\frac{\Phi_{n-2}(\prod_iT_{d_i})}{2^n\binom n2}
 =\left(\prod_iA_{d_i}\right)\left(1-\frac{\sum_i\delta_{d_i}}{\binom n2}\right).
\tag{1}
\]

**3. Numerical inequalities valid for all dimensions.** Put \(\alpha=1-1/\sqrt2\), \(\beta=1-1/\sqrt3\), and let \(t\) denote the number of factors having dimension two. For \(d\ge3\), \(0\le\delta_d\le\alpha\binom d2\); also \(\delta_2=\beta\), \(\delta_1=0\), and \(\beta<3\alpha\). This last strict inequality follows, for instance, from \(\alpha>1/4\) and \(\beta<1/2\).

Suppose some factor has dimension at least three. Its volume ratio satisfies \(A_d>\sqrt2\). Indeed \(A_3=\sqrt3\), \(A_4=25\sqrt5/24\), and for \(d\ge5\), the arithmetic-geometric mean estimate \(d!\le((d+1)/2)^d\) gives
\[
A_d\ge\sqrt{d+1}\left(\frac d{d+1}\right)^{d/2}
\ge\sqrt{(d+1)/e}\ge\sqrt{6/e}>\sqrt2.
\]
All other volume ratios \(A_j\) are at least one: directly for \(j=1,2,3,4\), and from this same bound for \(j\ge5\). Write \(C=\binom n2\) and \(H=\sum_{i<j}d_id_j\), so \(C=\sum_i\binom{d_i}2+H\). If \(t>0\), the assumption \(n\ge3\) implies \(H\ge2t\) (each two-dimensional factor has at least two units of dimensional interaction with other factors); for \(t=0\) this estimate is vacuous. Thus
\[
\sum_i\delta_{d_i}
 \le\alpha\sum_i\binom{d_i}2+(\beta-\alpha)t
 \le\alpha C
\]
by \(\beta<3\alpha\). Identity (1) now gives a strict lower bound \(\sqrt2(1-\alpha)=1\) for the normalized ridge content; strictness follows from \(A_d>\sqrt2\).

It remains to consider factors of dimensions one and two, with at least one two-dimensional factor. Then \(n\ge3\), \(\prod_iA_{d_i}\ge A_2=3\sqrt3/4\), and \(C\ge3t\): if \(t=1\), this is \(C\ge3\); if \(t\ge2\), it follows from \(n\ge2t\) and \(\binom{2t}2\ge3t\). Therefore (1) yields
\[
\frac{\Phi_{n-2}(\prod_iT_{d_i})}{2^n C}
\ge\frac{3\sqrt3}{4}\left(1-\frac\beta3\right)
=\frac{2\sqrt3+1}{4}>1.
\]
Finally, if every factor has dimension one, \(P\) is an orthogonal box with side lengths at least two. Each ridge face volume is a product of \(n-2\) side lengths; the ridge sum is minimized by taking every length to be two, giving \(2^n\binom n2\), with strict inequality if any side is longer because \(n\ge3\). This proves both the inequality and the equality characterization. \(\square\)

## Verification
The standard-library program `verify.py` independently computes \(\Phi_k(T_d)\) from the regular-simplex face formula and convolves the face-polynomials, then compares the codimension-two coefficient against identity (1). For every ordered composition of each dimension \(3\le n\le13\), it checks the identity, the sharp lower bound, and equality only for one-dimensional factors. It also evaluates the elementary strict constants above. It passed 24,567 supplementary assertions over 8,188 ordered compositions. These finite checks are not a proof for unbounded dimensions; the proof above is analytic.

## Relationship to prior work
Zwierzyński [1, Conjecture 5.2] asks for this exact ridge bound for general convex polytopes satisfying stronger affine-face-distance requirements. Theorem 1.1 concerns *surface area*, not ridges; Proposition 5.3 proves the ridge bound for centered orthotopes and centrally symmetric admissible tangential polytopes, and Proposition 5.4 gives a nonsharp ridge bound. Products containing a factor of dimension at least two are not centrally symmetric, so these cases are not supplied by those results. Basit and Lángi [2, Theorem 8] supply the single-simplex isoperimetric input, but neither study Cartesian-product ridge bounds nor infer inequality (1). Joós and Lángi [3] study intrinsic-volume isoperimetry of zonotopes and parallelotopes, a different class and functional; their parallelotope conclusions cover the all-segment endpoint but not products with a simplex factor of dimension at least two. Moreover, a regular \(d\)-simplex of inradius one has squared distance \(cd/(d-c+1)\ge c\) from its center to each codimension-\(c\) face span; orthogonal products add these squared distances. Hence the minimizing regular products themselves obey all the conjecture's stronger face-distance conditions, giving genuinely new noncentrally symmetric instances of the conjecture. The new content is the product reduction, the exact codimension-two deficit identity, and the sharp dimension-uniform strict inequality under only the inball condition.

## Limitations
This result does not prove the general ridge-skeleton conjecture for arbitrary polytopes. No assertion is made for non-orthogonal affine products, general projective images, or products of nonsimplicial factors. Historical priority is assessed against inspected source material and targeted searches but is not independently certified. The supplementary computations test only bounded dimensions.

## References
[1] Michał Zwierzyński, *A Sharp Surface-Area Extension of Vaaler's Theorem* (2026), arXiv:2609.27798, especially §5, Conjecture 5.2 and Propositions 5.3–5.4. https://arxiv.org/abs/2609.27798

[2] Bushra Basit and Zsolt Lángi, *Discrete isoperimetric problems in spaces of constant curvature* (2022), arXiv:2206.04323, Theorem 8. https://arxiv.org/abs/2206.04323

[3] Antal Joós and Zsolt Lángi, *Isoperimetric problems for zonotopes* (2022), arXiv:2206.03204. https://arxiv.org/abs/2206.03204
