# The endpoint \(\lambda=2/3\) in a Fermat–Torricelli characterization of Hilbert norms

## Finding

**Endpoint characterization.** Let \(X\) be any real normed linear space of dimension at least three, without any completeness or smoothness assumption. For \(a,b,c\in X\), let
\[
\mathcal Z_X(a,b,c)=\operatorname*{argmin}_{z\in X}\bigl(\|a-z\|+\|b-z\|+\|c-z\|\bigr).
\]
Then \(X\) is an inner-product space if and only if **every** pair \(x,y\in X\) satisfying
\[
\|x+y\|=\tfrac23\|x-y\|
\]
has
\[
\mathcal Z_X(0,x,y)\cap\operatorname{co}\{0,x,y\}\ne\varnothing.
\]
Thus the fixed-ratio characterization established for \(\lambda>2/3\) also holds at its excluded endpoint. No claim is made about any smaller fixed ratio.

A geometric lemma supplies the missing endpoint: if \(u_1,u_2,u_3\) are nonzero, noncollinear vectors with \(0\in\operatorname{co}\{u_1,u_2,u_3\}\), then for some permutation and positive scalars \(a_i\), the vectors \(b_i=a_i u_i\) satisfy
\[
\|b_1+b_2-2b_3\|=\tfrac23\|b_1-b_2\|.
\]
This lemma holds in any real normed plane and involves no median assumption. The positive third scaling in its exceptional equality case is essential.

## Assumptions and scope

The points are considered in the ambient real normed space \(X\), not only in the affine plane containing their triangle. The convex hull is the ordinary finite convex hull. The hypothesis on pairs includes degenerate pairs, but the argument proving the nontrivial implication uses only noncollinear triples. Standard dual norming functionals are available by Hahn–Banach. Two established ingredients are used: (i) any finite configuration in a normed plane admits a Fermat–Torricelli median in its convex hull, and (ii) for real normed spaces of dimension at least three, the ambient convex-hull median property for all equilateral triangles characterizes inner-product norms (Pakhrou's Corollary 5.6).

## Proof

**1. Radial invariance of medianhood at the origin.** For nonzero vectors \(u_1,u_2,u_3\) in any normed space and positive scalars \(a_1,a_2,a_3\),
\[
0\in\mathcal Z_X(u_1,u_2,u_3)\quad\Longleftrightarrow\quad 0\in\mathcal Z_X(a_1u_1,a_2u_2,a_3u_3).
\]
Indeed, if the first condition holds, take \(\delta>0\) with \(\delta a_i\le1\) and write
\[
u_i-\delta z=(1-\delta a_i)u_i+\delta(a_i u_i-z).
\]
Then \(\sum_i\|u_i\|\le\sum_i\|u_i-\delta z\|\le\sum_i(1-\delta a_i)\|u_i\|+\delta\sum_i\|a_i u_i-z\|\). Cancellation yields \(\sum_i a_i\|u_i\|\le\sum_i\|a_i u_i-z\|\) for every \(z\). Apply the same argument with reciprocal factors for the converse.

**2. Endpoint rescaling: interior case.** Suppose \(u_1,u_2,u_3\) are noncollinear, nonzero and their triangle contains \(0\) in its relative interior. Choose \(\alpha_i>0\) with \(v_i=\alpha_i u_i\) and \(v_1+v_2+v_3=0\). Set \(h_i=\|v_i\|>0\), \(d_i=\|v_j-v_k\|\), where \(\{i,j,k\}=\{1,2,3\}\). From
\[
3v_i=(v_i-v_j)+(v_i-v_k)
\]
and the triangle inequality, \(3\sum_i h_i\le2\sum_i d_i\). Hence at least one \(d_i\ge\tfrac32h_i\).

If for some \(i\) the inequality is strict, relabel so that \(i=3\). Taking \(b_1=v_1\), \(b_2=v_2\) and \(b_3=t v_3\), where
\[
t=\tfrac12\bigl(\tfrac23\,d_3/h_3-1\bigr)>0,
\]
gives \(\|b_1+b_2-2b_3\|=(1+2t)h_3=\tfrac23 d_3\). This is the nonexceptional construction.

It remains to handle the case when no inequality \(d_i>\tfrac32h_i\) holds. The summed inequality forces \(d_i=\tfrac32h_i\) for all \(i\), and forces equality individually in each of the three triangle inequalities. Consequently
\[
3h_i=d_j+d_k=\tfrac32(h_j+h_k),
\]
so \(h_1=h_2=h_3=:h\) and \(d_1=d_2=d_3=\tfrac32h\). Choose a norm-one real linear functional \(\varphi\) with \(\varphi(v_1)=h\). Equality in
\[
3v_1=(v_1-v_2)+(v_1-v_3)
\]
forces \(\varphi(v_1-v_2)=\tfrac32h\), hence \(\varphi(v_2)=-\tfrac12h\). Therefore
\[
\|2v_1-v_2\|\ge\varphi(2v_1-v_2)=\tfrac52h,
\qquad
\|2v_1+v_2\|=\|v_1-v_3\|=\tfrac32h.
\]
For \(t\ge0\) define
\[
R(t)=\frac{\|2v_1+v_2-2t v_3\|}{\|2v_1-v_2\|}.
\]
The denominator is positive. At \(t=0\), \(R(0)\le\tfrac35<\tfrac23\), whereas \(R(t)\to\infty\) as \(t\to\infty\). By continuity there is \(t>0\) with \(R(t)=\tfrac23\). Then \(b_1=2v_1\), \(b_2=v_2\), \(b_3=t v_3\) give the endpoint equation with **all scaling factors positive**. The extra \(\tfrac35\) buffer is used only to resolve the equality case; no characterization is asserted for \(\lambda=3/5\).

**3. Endpoint rescaling: boundary case.** If \(0\) lies on an edge of the noncollinear triangle but is not a vertex, relabel and positively rescale the first two vectors to \(b_1=v\), \(b_2=-v\), \(v\ne0\). Choose \(b_3=\bigl((2/3)\|v\|/\|u_3\|\bigr)u_3\). Then \(\|b_1+b_2-2b_3\|=2\|b_3\|=\tfrac23\|b_1-b_2\|\). All factors are positive. This completes the geometric lemma.

**4. From the restricted endpoint property to equilateral triangles.** Assume the stated fixed-ratio convex-hull property in \(X\). Let \(A_1,A_2,A_3\) form any noncollinear equilateral triangle and \(P\) its affine plane. By the normed-plane convex-hull theorem there is a planar Fermat–Torricelli median \(m\) in the triangle. It can be chosen different from all three vertices: if the planar minimum is less than twice the common side length then no vertex minimizes, and if it equals twice that length then all vertices minimize and convexity makes the centroid a nonvertex median.

Translate \(m\) to \(0\); put \(u_i=A_i-m\), and let \(E=P-m\). We have \(u_i\ne0\), \(0\in\operatorname{co}\{u_i\}\) and \(0\in\mathcal Z_E(u_1,u_2,u_3)\). Apply the endpoint geometric lemma and obtain positive \(a_i\) with \(b_i=a_i u_i\) obeying \(\|b_1+b_2-2b_3\|=\tfrac23\|b_1-b_2\|\). Radial invariance says \(0\in\mathcal Z_E(b_1,b_2,b_3)\). Translating the restricted hypothesis to the triangle \(\{b_1,b_2,b_3\}\) gives an **ambient** median \(q\) in its convex hull, hence in \(E\). Comparing minima gives
\[
\sum_i\|b_i\|\le\sum_i\|b_i-q\|\le\sum_i\|b_i\|,
\]
so \(0\) itself is also an ambient median. By inverse radial invariance, \(0\in\mathcal Z_X(u_1,u_2,u_3)\), hence \(m\in\mathcal Z_X(A_1,A_2,A_3)\). Every equilateral triangle therefore has an ambient median in its convex hull, and Pakhrou's equilateral characterization implies \(X\) is an inner-product space.

**5. Converse.** If the norm of \(X\) comes from an inner product, metric projection of any point onto the compact convex triangle \(C=\operatorname{co}\{a,b,c\}\) does not increase its distance to any vertex. The sum-of-distances minimum over \(C\) therefore also minimizes over \(X\). This applies regardless of whether \(X\) is complete. In particular the endpoint test is satisfied.

## Verification

The only new critical argument is Step 2's exact treatment of the exceptional equality case. Its equal-length conclusion follows from the three individually saturated triangle inequalities, not from a smoothness or strict-convexity assumption; the norming functional exists by Hahn–Banach. No finite computation is used to prove the universal statement.

The standalone `CHECK.py` uses exact rational arithmetic in three polygonal norms and checked \(6{,}336\) noncollinear integer vector pairs: \(6{,}300\) strict-case and \(36\) saturated-case checks. In the rational hexagonal norm
\[
N(s,t)=\tfrac12\max\{|2s-t|,|2t-s|,|s+t|\},
\]
with \(v_1=(1,0)\), \(v_2=(0,1)\), \(v_3=(-1,-1)\), all three norms are \(1\) and all opposing differences have norm \(3/2\). The new construction \(b_1=2v_1\), \(b_2=v_2\), \(b_3=v_3/12\) satisfies the endpoint equality exactly. Run `python CHECK.py` to reproduce the supplementary checks.

## Relationship to prior work

Fang, Qi, and Liu, arXiv:2611.09226v1 (6 November 2026), characterize Hilbertian norms by the Fermat–Torricelli convex-hull test on one-sided Birkhoff–James-orthogonal pairs. This earlier orthogonality restriction motivates asking how far a fixed, metric median-to-side ratio can be restricted. Its Birkhoff–James hypothesis is not the endpoint metric equation proved here; neither criterion is a mere change of notation for the other.

Fang and Liu, arXiv:2611.13648v1 (10 November 2026), prove the restricted Fermat–Torricelli characterization for **each fixed** \(\lambda>2/3\) and explicitly note that their radial scaling can become zero at \(\lambda=2/3\) (their Lemmas 3–4 and Theorem 1). Their argument does not assert this endpoint. The present contribution addresses precisely that equality case and extends the fixed-ratio characterization to the missing boundary value. It uses their radial-invariance/planar-transfer route but supplies the positive endpoint construction above.

Pakhrou (2023, Corollary 5.6) proves the broader equilateral-triangle characterization used here as an established implication. The earlier Martini–Swanepoel–Weiß survey records the normed-plane convex-hull theorem (Theorem 3.23). Neither of those general results by itself implies that checking only triangles with the prescribed ratio \(2/3\) is sufficient: that is exactly the endpoint reduction proved here.

## Limitations

The theorem is confined to the fixed ratio \(2/3\) and real spaces of dimension at least three. It does not establish the optimal lower limit of allowable ratios, nor any quantitative stability under approximate medianhood. The normed-plane median theorem and Pakhrou's characterization are used as published results. A separate independent mathematical audit has not been performed; an earlier equivalent endpoint lemma under other terminology remains a bibliographic possibility.

## References

1. Z. Fang, J. Qi and Q. Liu, *A Fermat–Torricelli convex-hull characterization of inner-product spaces via Birkhoff–James orthogonality*, arXiv:2611.09226v1, first submitted 6 November 2026. https://arxiv.org/abs/2611.09226
2. Z. Fang and Q. Liu, *The Fermat–Torricelli problem under isosceles orthogonality-type conditions*, arXiv:2611.13648v1, submitted 10 November 2026. https://arxiv.org/html/2611.13648
3. T. Pakhrou, *Location problem and inner product spaces*, Journal of Functional Analysis **285** (2023), 110078, Corollary 5.6. https://doi.org/10.1016/j.jfa.2023.110078
4. H. Martini, K. J. Swanepoel, and G. Weiß, *The Fermat–Torricelli problem in normed planes and spaces*, Journal of Optimization Theory and Applications **115** (2002), 283–314; arXiv:0707.2592v2, Theorem 3.23. https://arxiv.org/abs/0707.2592
