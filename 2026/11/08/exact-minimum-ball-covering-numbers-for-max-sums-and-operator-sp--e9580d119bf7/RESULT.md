# Exact minimum ball-covering numbers for max-sums and operator spaces

## Finding
For a nonzero finite-dimensional real normed space \(E\), let \(\kappa(E)\) be the smallest number of closed norm balls \(\overline B_E(c,r)\) covering the entire unit sphere \(S_E\), subject to \(0\notin\overline B_E(c,r)\), equivalently \(0\le r<\|c\|\). For any integer \(m\ge2\) and any nonzero finite-dimensional real normed spaces \(E_1,\ldots,E_m\),

\[
\boxed{\kappa\bigl(E_1\oplus_\infty\cdots\oplus_\infty E_m\bigr)
=\sum_{j=1}^{m}\kappa(E_j).}
\]

Every covering attaining this number has a sharp localization property: each covering ball meets exactly one of the embedded coordinate unit spheres; for each \(j\), precisely \(\kappa(E_j)\) balls meet the \(j\)-th sphere, and their coordinate restrictions constitute a minimal ball covering of \(S_{E_j}\). In particular, all these centers possess a uniquely dominant coordinate.

Consequently, for any nonzero finite-dimensional real normed \(Y\),

\[
\boxed{\kappa\bigl(\mathcal L(\ell_1^m(\mathbb R),Y)\bigr)=m\,\kappa(Y),}
\]

since the operator norm identifies this space isometrically with \(\ell_\infty^m(Y)\). For Euclidean \(Y=\ell_2^n(\mathbb R)\), \(n\ge1\),
\[
\boxed{\kappa\bigl(\mathcal L(\ell_1^m,\ell_2^n)\bigr)=m(n+1).}
\]
This exceeds the dimension-only lower bound \(mn+1\) by exactly \(m-1\). The formula also implies that every such operator-space covering number is divisible by \(m\).

## Assumptions and scope
All spaces and operators are over the **real** scalar field. Each \(E_j\) is nonzero and finite-dimensional, and \(m\) is a finite integer. The max-sum has norm \(\|(x_1,\ldots,x_m)\|=\max_j\|x_j\|\). The balls may be taken open instead of closed without changing \(\kappa\): inflate each of the finitely many closed radii slightly without touching the origin; conversely shrink the radii of a finite open cover slightly using compactness of the unit sphere. Infinite products, infinite covering cardinalities, and complex-space analogues are not asserted.

## Proof
**1. Existence of finite component coverings and radius inflation.** In any finite-dimensional \(E\), for each \(u\in S_E\) take \(c=2u\) and radius \(r=3/2\). The open ball contains \(u\), excludes the origin, and the resulting open cover of the compact sphere has a finite subcover. Thus \(\kappa(E)\) exists and is finite. Any minimal closed covering can be inflated by replacing each radius \(r\) by some \(r_0\) with \(r<r_0<\|c\|\), yielding an open covering with unchanged cardinality.

For any center \(c\ne0\) and radius \(r_0<\|c\|\), define, for \(t>1\), \(c_t=tc\) and
\[
 r_t=r_0+(t-1)\|c\|=t\|c\|-(\|c\|-r_0).
\]
The triangle inequality shows \(B_E(c,r_0)\subset B_E(c_t,r_t)\), while \(r_t<t\|c\|\). By taking \(t\) sufficiently large we also obtain \(r_t>1\). Thus any finite component covering can be replaced by one with the same number of balls, all of radius strictly greater than one, still excluding the origin.

**2. Upper bound.** Fix such a covering \(\{B_{E_j}(c_{j,k},r_{j,k})\}_{k=1}^{\kappa(E_j)}\) of \(S_{E_j}\) with \(r_{j,k}>1\) and \(r_{j,k}<\|c_{j,k}\|\). In the max-sum, place a ball centered at \(\iota_j(c_{j,k})\), the vector supported only in coordinate \(j\), with the same radius \(r_{j,k}\). It misses the origin because \(r_{j,k}<\|c_{j,k}\|\). Given any \(x=(x_1,\ldots,x_m)\) in the max-sum unit sphere, some coordinate \(j\) satisfies \(\|x_j\|=1\), and some component ball satisfies \(\|x_j-c_{j,k}\|<r_{j,k}\). For all \(i\ne j\), \(\|x_i\|\le1<r_{j,k}\). Hence the corresponding max-sum ball contains \(x\), establishing
\[\kappa(\oplus_\infty E_j)\le\sum_j\kappa(E_j).\]

**3. Axis exclusivity and lower bound.** Consider *any* ball \(\overline B(c,r)\) in the max-sum with \(r<\|c\|_\infty\). If it meets the embedded unit sphere \(\iota_j(S_{E_j})\), then for some unit \(u\in E_j\),
\[
\max\bigl\{\|u-c_j\|,\max_{i\ne j}\|c_i\|\bigr\}\le r.
\]
It follows that \(\|c_i\|\le r\) for every \(i\ne j\). Since \(\|c\|_\infty>r\), necessarily \(\|c_j\|>r\). This is impossible for two distinct indices \(j\). Thus a ball excluding the origin meets **at most one** embedded unit sphere, and if it meets the \(j\)-th sphere then the restricted ball \(\overline B_{E_j}(c_j,r)\) misses zero and contains the corresponding unit points.

If \(\mathscr B\) is a finite ball covering of the whole max-sum sphere, let \(\mathscr B_j\) be its subfamily meeting axis \(j\). Those subfamilies are disjoint, and their restrictions cover \(S_{E_j}\), so \(|\mathscr B_j|\ge\kappa(E_j)\). Therefore
\[
|\mathscr B|\ge\sum_j|\mathscr B_j|\ge\sum_j\kappa(E_j).
\]
This matches the upper bound. When equality holds, every ball belongs to exactly one \(\mathscr B_j\), every \(|\mathscr B_j|=\kappa(E_j)\), and each restricted family is minimal. The inequalities above show that its center satisfies \(\|c_j\|>r\ge\max_{i\ne j}\|c_i\|\), proving the unique dominant-coordinate assertion.

**4. Operator-space application.** Every \(T\in\mathcal L(\ell_1^m,Y)\) satisfies
\[
\|T\|=\max_{1\le j\le m}\|Te_j\|_Y.
\]
The inequality \(\le\) follows from \(\|Tx\|\le\sum_j|x_j|\|Te_j\|\); equality follows by evaluating on a maximizing basis vector. Thus \(T\mapsto(Te_1,\ldots,Te_m)\) is an onto linear isometry from the operator space to \(\ell_\infty^m(Y)\), and the covering formula applies.

**5. Euclidean component value.** For \(E=\ell_2^n(\mathbb R)\), the established value \(\kappa(E)=n+1\) also has an elementary argument. For the lower bound, with at most \(n\) candidate ball centers, choose a unit vector \(u\) whose inner product with every center is nonpositive (perpendicular to their span if it is proper, otherwise solve the independent \(n\)-by-\(n\) system of negative unit inner products and normalize). Then \(\|u-c_i\|^2\ge1+\|c_i\|^2>r_i^2\), so all balls miss \(u\). For the upper bound, choose the \(n+1\) unit vertices \(v_i\) of a centered regular simplex. They span \(\mathbb R^n\) and sum to zero, so \(\delta:=\min_{\|u\|=1}\max_i\langle u,v_i\rangle>0\). For any \(t>1/(2\delta)\), choose \(r\) satisfying \(\sqrt{1+t^2-2t\delta}<r<t\). Then \(\|u-tv_i\|<r\) for some \(i\), and all \(n+1\) balls exclude the origin. Hence \(\kappa(\ell_2^n)=n+1\), completing the operator-space formula.

## Verification
The upper-bound construction is explicit and works uniformly in the shapes of the component unit spheres, after finite radius inflation. The lower bound is not a countability argument: each actual ball is assigned to at most one coordinate axis, giving a sharp integer inequality and the optimal-covering rigidity. The operator-space norm identity is proved above, without assumptions about smoothness or strict convexity of \(Y\). A standalone finite-grid checker in `CHECK.py` tests coordinate-ball constructions on small max-norm examples; these tests are diagnostic, not substitutes for the general proof.

## Relationship to prior work
Mishra, Paul, Sain and Sohel (2026), arXiv:2607.10353, prove qualitative stability of the ball-covering property under \(\ell_p\)-sums (Theorem 3.19) and determine \(mn+1\) for certain operator spaces when the **domain is strictly convex** and the range is smooth (Theorem 3.31). Their stated results do not determine the finite minimum cardinality for max-sums or operators with \(\ell_1^m\) domain. The latter domain is not strictly convex for \(m\ge2\), and the answer is instead \(m\kappa(Y)\).

Luo, Liu and Wang (2017), DOI:10.2298/FIL1712905L, establish qualitative ball-covering stability under finite product norms. Their max-sum axis argument (proof of Theorem 1, Case I) anticipates the lower-bound mechanism above; their countable construction is not the exact finite-cardinality upper bound, nor does it establish minimal-cover localization. Luo and Zheng (2019/2020), DOI:10.4064/sm180607-6-10, prove corresponding countable stability for sequences of summands. The classical Euclidean value \(n+1\) and the dimension lower bound are credited to Cheng's earlier ball-covering work. The claimed contribution is precisely the **exact finite-cardinality additivity and its optimal-covering localization**, and its operator-space consequences, not qualitative BCP inheritance.

## Limitations
Only finite max-sums of nonzero finite-dimensional **real** normed spaces are asserted. No claim is made for other \(p\)-sum norms, arbitrary operator domains, infinite products, uniform radius constraints, or complex-space geometry. The elementary proof does not establish that its identities were unpublished in all earlier ball-covering literature; a broader previously unnoticed exact cardinality theorem remains a publication-priority risk.

## References
1. A. Mishra, K. Paul, D. Sain, S. Sohel, *On the Ball Covering Property of \(\mathcal L(X,Y)\)*, arXiv:2607.10353, first submitted 11 July 2026; especially Theorems 3.19 and 3.31. https://arxiv.org/abs/2607.10353
2. Z. Luo, J. Liu, B. Wang, *A Remark on the Ball-Covering Property of Product Spaces*, Filomat 31:12 (2017), 3905–3908, DOI:10.2298/FIL1712905L. https://www.pmf.ni.ac.rs/filomat-content/2017/31-12/31-12-24-3778.pdf
3. Z. Luo, B. Zheng, *Stability of the ball-covering property*, Studia Mathematica 250 (2020), 19–34, DOI:10.4064/sm180607-6-10. https://www.impan.pl/en/publishing-house/journals-and-series/studia-mathematica/all/250/1/112671/stability-of-ball-covering-property
4. L. Cheng, *Ball-covering property of Banach spaces*, Israel Journal of Mathematics 156 (2006), 111–123.
