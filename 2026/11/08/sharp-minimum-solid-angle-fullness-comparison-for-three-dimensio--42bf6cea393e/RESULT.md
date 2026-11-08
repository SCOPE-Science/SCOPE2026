# Sharp minimum-solid-angle/fullness comparison for three-dimensional orthoschemes

## Finding
For any \(a,b,c>0\), define the Euclidean three-dimensional orthoscheme
\[
S(a,b,c)=\operatorname{conv}\{(0,0,0),(a,0,0),(a,b,0),(a,b,c)\}.
\]
Let \(\mu(S)=\operatorname{vol}_3(S)/\operatorname{diam}(S)^3\) be its fullness, and let \(\Omega_{\min}(S)\) be the minimum, among its four vertices, of the usual unnormalized solid angles in steradians. Then
\[
\boxed{\mu(S)>\tfrac16\Omega_{\min}(S)^2.}
\]
The coefficient \(1/6\) is globally optimal on the nondegenerate class: equality never occurs, but the ratio of the left-hand side to the square of the minimum solid angle tends to \(1/6\) on the family \(S(\varepsilon,1,\varepsilon)\) as \(\varepsilon\downarrow0\).

## Assumptions and scope
The three lengths \(a,b,c\) are independently arbitrary strictly positive real numbers. A three-dimensional orthoscheme is a simplex whose consecutive path edges are mutually perpendicular, and the displayed coordinates describe every such simplex up to Euclidean congruence and reversal. The solid angle is the area cut out on the unit sphere by the inward vertex cone, not the probability obtained by dividing by \(4\pi\). The diameter is the longest vertex-to-vertex distance. The statement does not concern general tetrahedra or a universal constant beyond this class.

## Proof
Set
\[
s=\sqrt{a^2+b^2},\quad t=\sqrt{b^2+c^2},\quad L=\sqrt{a^2+b^2+c^2}.
\]
The unique maximal vertex-to-vertex distance is \(L\), so \(\mu(S)=abc/(6L^3)\). Denote the vertices in path order by \(v_0,v_1,v_2,v_3\), and their solid angles by \(\Omega_0,\ldots,\Omega_3\). Computing the determinant and dot products of the three incident edge vectors in the classical trihedral solid-angle identity
\[
\Omega=2\operatorname{atan2}\!\left(\left|\det(u,v,w)\right|,\;\|u\|\|v\|\|w\|+(u\!\cdot\!v)\|w\|+(v\!\cdot\!w)\|u\|+(w\!\cdot\!u)\|v\|\right)
\]
gives the **four exact formulas**
\[
\begin{aligned}
\Omega_0&=2\arctan\frac{bc}{(s+a)(L+s)},\\
\Omega_1&=\arctan\frac cb,\\
\Omega_2&=\arctan\frac ab,\\
\Omega_3&=2\arctan\frac{ab}{(t+c)(L+t)}.
\end{aligned}
\]
All arctangent arguments are positive; the displayed \(\operatorname{atan2}\) denominator is strictly positive in these four cases. For completeness, at \(v_0\) the determinant magnitude is \(abc\), and the dot-product denominator factors as \(a(s+a)(L+s)\); the other endpoint follows by reversing the orthogonal path. At each middle vertex two incident edges are orthogonal and the corresponding arctangent half-angle identity yields the two middle formulas.

Assume first \(a\ge c\), and put \(D=(s+a)(L+s)\). The elementary inequalities \((L+s)^2\ge4Ls\), \(b\le s\), and \(c\le a\) imply
\[
D^2\ge4Ls(s+a)^2\ge4bL^3.
\]
The second inequality follows from \(bL^2\le sL^2\le s(s^2+a^2)\le s(s+a)^2\). Therefore \(aD^2\ge4bcL^3\). Since \(\arctan x<x\) for every \(x>0\),
\[
\Omega_{\min}(S)^2\le\Omega_0^2
<\frac{4b^2c^2}{D^2}
\le\frac{abc}{L^3}=6\mu(S).
\]
If \(c>a\), reverse the orthogonal path, interchanging \(a\) and \(c\), and use the identical argument with \(\Omega_3\). This proves the strict bound for **every** positive triple, with no hidden aspect-ratio restrictions.

For sharpness let \(a=c=\varepsilon\), \(b=1\). Then \(L=\sqrt{1+2\varepsilon^2}\) and
\[
\mu(S)=\frac{\varepsilon^2}{6(1+2\varepsilon^2)^{3/2}}\sim\frac{\varepsilon^2}{6}.
\]
Both middle angles equal \(\arctan\varepsilon\sim\varepsilon\). By the endpoint formula, both endpoint angles satisfy
\[
\Omega_0=\Omega_3=2\arctan\frac{\varepsilon}{(\sqrt{1+\varepsilon^2}+\varepsilon)(\sqrt{1+2\varepsilon^2}+\sqrt{1+\varepsilon^2})}\sim\varepsilon.
\]
Thus \(\Omega_{\min}(S)\sim\varepsilon\) and the ratio converges to \(1/6\). Strictness above excludes finite equality.

## Verification
The included \(\texttt{verifier.py}\) computes solid angles independently from vertex-edge determinant and dot-product data; checks the endpoint and middle closed forms, the algebraic inequality certificate, and the claimed shape ratio on 12,000 deterministic random positive triples spanning broad aspect ratios; and displays ratios along the sharpness family. Run with \(\texttt{python verifier.py}\) using Python's standard library. The recorded run returned \(\texttt{PASS: 12,000 deterministic independent solid-angle and bound comparisons}\). These computations are corroboration only: the uncountable-domain theorem is established by the inequalities in the preceding proof.

## Relationship to prior work
Martin W. Licht, *On solid angles and simplex shape measures*, arXiv:2610.05883, publicly submitted October 5, 2026, Theorem 1.1, proves for all tetrahedra \(\mu\ge\Omega_{\min}^2/(12+3\pi)\). The present result proves the larger **optimal** coefficient \(1/6\) on the orthoscheme subclass, and establishes strictness and sharpness of that coefficient. Neither the general estimate nor its proof yields the stated sharp coefficient. Godland and Kabluchko, *Angle Sums of Schläfli Orthoschemes*, develop angle-sum identities for particular Schläfli orthoschemes, rather than a uniform minimum-solid-angle versus diameter-normalized-volume inequality for all three arbitrary path lengths. Liu and Joe's 1994 *Relationship between tetrahedron shape measures* addresses comparison of tetrahedral quality indicators in general; the available abstract does not give the present sharp orthoscheme coefficient. Prior minimum-angle bounds on the orthoscheme family do not imply the claim, because fullness varies down to zero independently of a uniform upper bound for the minimum angle.

## Limitations
Only three-dimensional orthoschemes and the **unnormalized** spherical-area definition of angle are covered. The optimal constant is approached by degenerate simplices and is not an attained equality case. No optimal constant for arbitrary tetrahedra or higher-dimensional orthoschemes is asserted. The historical literature search cannot exclude an unindexed or differently described equivalent result; in particular the complete 1994 Liu–Joe paper was not available for direct full-text inspection. Independent validation has not been performed.

## References
1. Martin W. Licht, *On solid angles and simplex shape measures*, arXiv:2610.05883, initial public submission 2026-10-05, Theorem 1.1 and Section 4. https://arxiv.org/abs/2610.05883
2. T. Godland and Z. Kabluchko, *Angle Sums of Schläfli Orthoschemes*, *Discrete & Computational Geometry*, DOI:10.1007/s00454-021-00326-z. https://doi.org/10.1007/s00454-021-00326-z
3. A. Liu and B. Joe, *Relationship between tetrahedron shape measures*, *BIT Numerical Mathematics* 34 (1994), 268–287, DOI:10.1007/BF01955874. https://doi.org/10.1007/BF01955874
