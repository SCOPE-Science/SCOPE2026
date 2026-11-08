# Sharp Hilbert-target extension factor for the zero-sum plane in a real cube

## Finding

Let \(E=\ell_\infty^3(\mathbb R)\) and \(H=\{(s,t,-s-t):s,t\in\mathbb R\}\), with their inherited norms. The optimal constant \(C_2(H,E)\) in the simultaneous Hilbert-valued linear extension property is

\[
C_2(H,E):=\sup_{n\ge1}\sup_{0\ne R:H\to\ell_2^n}\frac{\inf\{\|A\|:A:E\to\ell_2^n,\ A|_H=R\}}{\|R\|}=\frac2{\sqrt3}.
\]

More precisely, put \(u=R(1,0,-1)\), \(v=R(0,1,-1)\), and \(m=\max\{\|u\|,\|v\|,\|u-v\|\}=\|R\|\). For every nonzero \(R\), its optimal extension inflation is at most \(2/\sqrt3\). Equality holds if and only if \(\|u\|=\|v\|=\|u-v\|=m\), equivalently the three target points \(0,u,v\) form a nondegenerate equilateral triangle. This is realizable already for \(n=2\); for \(n=1\), the optimal inflation is always one.

## Assumptions and scope

All vector spaces and operators are **real linear**. The target is the ordinary Euclidean space \(\ell_2^n(\mathbb R)\), and every operator norm is induced by the specified domain and target norms. No assertion is made for complex-linear operators, for other ambient norms, or for arbitrary subspaces. The extension constant is uniform in the target dimension \(n\), as in the quantitative POE-2 condition.

The plane's unit ball is the centrally symmetric hexagon with vertex pairs \(\pm(1,0,-1)\), \(\pm(0,1,-1)\), and \(\pm(1,-1,0)\). Hence the expression for \(m\) is exact.

## Proof

**1. Reduction to a three-point Euclidean problem.** Fix \(R\), its images \(u,v\), and an extension \(A\). Its values on the ambient coordinate basis have the form \(Ae_1=u+c\), \(Ae_2=v+c\), \(Ae_3=c\), for some \(c\in\ell_2^n\), and every such \(c\) defines an extension. Because the unit ball of \(E\) is a cube, checking its eight vertices and identifying opposite signs gives

\[
\|A\|=\max\{\|u+v+3c\|,\|u+v+c\|,\|u-v+c\|,\|-u+v+c\|\}.
\]

Writing \(d=u+v+c\), let \(P_0=0\), \(P_1=2u\), \(P_2=2v\) and let \(G=(P_0+P_1+P_2)/3=2(u+v)/3\). The same formula becomes

\[
\|A\|=\max\{\|d-P_0\|,\|d-P_1\|,\|d-P_2\|,3\|d-G\|\}.
\tag{1}
\]

The triangle \(P_0P_1P_2\) has diameter \(D=2m\). The problem is thus to minimize the right side of (1) over all \(d\) in a real Hilbert space.

**2. Geometry lemma (including degenerate triangles).** For any three points of diameter \(D\) in a real Hilbert space, their least-enclosing-ball center \(o\), radius \(\rho\), and arithmetic centroid \(G\) satisfy

\[
\rho\le\frac D{\sqrt3},\qquad\|o-G\|\le\frac D6.
\tag{2}
\]

Moreover, \(\rho<D/\sqrt3\) unless the points form an equilateral triangle of positive side length. For \(D=0\) the assertion is immediate. The three points span an affine plane, so Euclidean triangle geometry applies. If the triangle has a right or obtuse angle, or is collinear, take the midpoint \(o\) of a longest side \(AB\) as center; the third point \(C\) lies in the closed disk with diameter \(AB\). Therefore \(\rho=D/2\) and \(\|o-G\|=\|o-C\|/3\le D/6\). The radius statement is strict for \(D>0\).

If the triangle is acute, choose the longest side as \(AB\), normalize \(D=2\), and write \(A=(-1,0)\), \(B=(1,0)\), \(C=(x,y)\), with \(y>0\) and \(|x|<1\). Put \(z=1-x^2\) and \(t=y^2\). Acuteness at \(C\) gives \(t>z\), and \(\|C-A\|,\|C-B\|\le2\) gives \(t\le3-2|x|-x^2\le9(1-x^2)=9z\). The circumcenter is \(o=(0,(t-z)/(2y))\), while \(G=(x/3,y/3)\). Direct expansion yields

\[
9\|o-G\|^2=x^2+\frac{(t-3z)^2}{4t}\le 1,
\]

since the last inequality is equivalent to \((t-z)(t-9z)\le0\). This proves the centroid bound. The circumradius is \(D/(2\sin\gamma)\), where \(\gamma\) is the largest angle, opposite the longest side. Since \(\pi/3\le\gamma<\pi/2\), the radius is at most \(D/\sqrt3\), with equality only when every angle is \(\pi/3\). This establishes (2) and its strictness assertion.

**3. Uniform extension bound.** Take \(d=o\) in (1), with \(D=2m\). By (2),

\[
\|A\|\le\max\left\{\frac{2m}{\sqrt3},m\right\}=\frac{2m}{\sqrt3}.
\]

If the triangle is not equilateral and \(m>0\), the radius inequality is strict and the second bound \(m\) is strictly smaller than \(2m/\sqrt3\). Hence the extension inflation is **strictly** smaller than \(2/\sqrt3\) for every non-equilateral pair \((u,v)\).

**4. Sharpness and all equality cases.** In \(\ell_2^2\), take \(u=(1,0)\) and \(v=(1/2,\sqrt3/2)\), for which \(m=1\) and \(0,2u,2v\) form an equilateral triangle of side two. Their centroid \(G\) is also their circumcenter, with circumradius \(2/\sqrt3\). For every \(d\), the quadratic identity

\[
\frac13\sum_{j=0}^2\|d-P_j\|^2=\|d-G\|^2+\frac13\sum_{j=0}^2\|P_j-G\|^2\ge\frac43
\]

implies \(\max_j\|d-P_j\|\ge2/\sqrt3\). Taking \(d=G\) gives equality, including the fourth term in (1), which is zero. This proves sharpness. For any other equilateral \((u,v)\) the same identity, scaled by \(m\), gives equality. Conversely, the strictness argument in step 3 forces equilateral geometry in every equality case. In one-dimensional target spaces no nondegenerate equilateral triangle is possible; ordinary real Hahn–Banach extends each functional with unchanged norm. \(\square\)

## Verification

The included standalone script `checks/verify.py` performs 18,002 finite numerical assertions for acute, nearly collinear, and near-equilateral target configurations. It recomputes a least-enclosing-ball center, verifies both geometric inequalities and the extension bound, and tests exact sharpness numerically in the equilateral example. These diagnostics do not certify the universal theorem; steps 1–4 above provide its proof. Run with `python3 checks/verify.py` using the Python standard library.

## Relationship to prior work

Pariente-Martín and Tradacete's 2026 paper identifies POE-\(p\) as the structural extension condition appearing in a characterization of order continuity of maps between free Banach lattices. Its Theorem 1.3 is qualitative and does not give this exact finite-dimensional optimal POE-2 factor or the extremizing maps. The original free-Banach-lattice framework of Oikhberg, Taylor, Tradacete and Troitsky likewise develops the abstract extension property; this theorem supplies a quantitative example in the smallest nontrivial ambient dimension.

A previously published exact Euclidean Banach–Mazur distance \(2/\sqrt3\) for the same zero-sum hexagonal plane is a distinct invariant: it compares norms on the plane rather than computing simultaneous Hilbert-valued extensions across the specified ambient inclusion. Equality of the two numerical values alone proves neither implication. Existing results on projection constants, metric Lipschitz extensions, and generalized hexagonal norm constants concern different optimization problems. The particular linear extension inequality and its equality classification were compared by their mathematical implications, not only by terminology.

## Limitations

This is a real finite-dimensional inclusion result. It gives no exact constants for other hyperplanes or target exponents, and its source comparison cannot rule out every classical formulation of a Hilbert-valued extension theorem. In particular, a more general historical operator extension result may imply the sharp bound under different language; publication priority remains to be independently checked. Finite diagnostics do not replace the proof, and independent mathematical audit has not been performed.

## References

1. R. E. Pariente-Martín and P. Tradacete, *Order continuity of induced homomorphisms between free Banach lattices*, arXiv:2611.00451v1, first public 2026-10-30. https://arxiv.org/html/2611.00451v1 .
2. T. Oikhberg, M. A. Taylor, P. Tradacete and V. G. Troitsky, *Free Banach lattices*, J. Eur. Math. Soc. 28 (2026), 4387–4514; arXiv:2210.00614 (2022). https://arxiv.org/abs/2210.00614 .
3. Related public mathematical records on the same zero-sum plane: *Exact Euclidean distortion of the real zero-sum \(\ell_p^3\) plane*, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-euclidean-distortion-of-the-real-zero-sum-ell-p-3-plane--65a2dd83e419 . Its asserted invariant is the Banach–Mazur distance, not the linear extension factor proved here.
