# Three area moments reconstruct a triangle from perimeter-uniform random inscribed triangles

## Finding

Let \(T\) be any nondegenerate Euclidean triangle of area \(A>0\), perimeter \(P>0\), and side lengths \(a_1,a_2,a_3\). Choose three points independently using normalized arclength on the **entire** perimeter of \(T\), without forcing the points onto different sides. Let \(S\) be the ordinary, unsigned Euclidean area of their convex hull, and let \(m_j=\mathbb E[S^j]\), for \(j=1,2,3\). Put \(p_i=a_i/P\), \(e_2=p_1p_2+p_1p_3+p_2p_3\), and \(e_3=p_1p_2p_3\). Then

\[
\boxed{m_1=\frac A2e_2,\qquad m_2=\frac{A^2}{6}e_2,\qquad m_3=A^3\left(\frac3{40}e_2-\frac1{60}e_3\right).}
\]

In particular, the first three raw moments determine the parent triangle **up to congruence**, with no previously known scale or perimeter required. Explicitly,

\[
A=\frac{3m_2}{m_1},\quad e_2=\frac{2m_1}{A},\quad e_3=\frac92e_2-\frac{60m_3}{A^3}.
\]

The unordered three numbers \(p_i\) are exactly the roots of \(z^3-z^2+e_2z-e_3=0\); the perimeter, hence the side lengths, is recovered from

\[
P=2\sqrt A\left(\prod_{i=1}^3(1-2p_i)\right)^{-1/4},\qquad a_i=Pp_i.
\]

Three moments are optimal among initial sequences of raw moments: the **first two moments do not determine the shape**. The full (not just moment) distribution of \(S/A\) is an explicit three-component mixture depending on the parent triangle only through \(e_2,e_3\), given below.

The mean and relative second moment have the sharp ranges

\[
\frac18<\frac{\mathbb E S}{A}\le\frac16,
\qquad
2\le\frac{\mathbb E[S^2]}{(\mathbb E S)^2}<\frac83.
\]

The equalities are attained only by equilateral triangles; the other endpoints are sharp unattained limits as the triangle degenerates.

## Assumptions and scope

All three sample points are independent, with each point distributed proportionally to Euclidean arclength on the entire closed polygonal boundary. Vertices are sampled with probability zero; no labels or side assignments are observed. Areas are unsigned. The triangle inequality gives \(0<p_i<1/2\) and \(\sum_i p_i=1\). No regularity or symmetry assumption beyond nondegeneracy is made.

For the distributional statement set \(Z=S/A\), let \(U,V,W\) be independent uniform variables on \([0,1]\), and define the universal CDFs

\[
F_2(t)=\Pr(|U-V|W\le t),\qquad
F_3(t)=\Pr(UV+W(1-U-V)\le t).
\]

For \(0<t<1\), \(F_2(t)=t^2-2t\log t\), and \(F_3\) has the explicit bounded integral representation

\[
F_3(t)=\int_0^1\int_0^1\int_0^1
\mathbf1\{uv+w(1-u-v)\le t\}\,dw\,dv\,du.
\]

The complete law for \(0<t<1\) is

\[
\boxed{\Pr(Z\le t)=
(1-3e_2+3e_3)+3(e_2-3e_3)F_2(t)+6e_3F_3(t).}
\]

The first coefficient is the atom at \(Z=0\), arising when all three sample points lie on one edge. Both CDFs are zero below zero and one from one onward; for \(t=0\), the CDF equals the displayed atom.

## Proof

**1. Conditional geometry.** Fix an ordered side assignment for the three samples. If all points lie on one side, \(Z=0\). If two lie on one side and the third on another, affine barycentric coordinates show that \(Z\) is distributed as \(|U-V|W\): the base occupies a fraction \(|U-V|\) of one full side, and the height of the third point is a uniform fraction of the altitude from the remaining vertex. If the three samples lie on three distinct sides, the barycentric determinant gives \(Z=UV+W(1-U-V)\), up to independent uniform reversals of edge parameters. This quantity is nonnegative because it is also \(UV(1-W)+(1-U)(1-V)W\).

**2. Exact side-assignment probabilities.** The probabilities of all-three-same, exactly-two-same, and all-distinct are, respectively,

\[
\sum_i p_i^3=1-3e_2+3e_3,\quad
3\sum_{i\ne j}p_i^2p_j=3(e_2-3e_3),\quad
6p_1p_2p_3=6e_3.
\]

They sum to one. Conditioning establishes the full mixture law. For \(0<t<1\), integrating the triangular density \(2(1-u)\) of \(|U-V|\) against the independent uniform multiplier yields \(F_2(t)=t^2-2t\log t\).

**3. Conditional moments.** For every positive integer \(k\), direct integration gives

\[
B_k:=\mathbb E[(|U-V|W)^k]=\frac{2}{(k+1)^2(k+2)}.
\]

For three distinct edges, expanding the bounded polynomial under the triple integral gives

\[
C_1=\frac14,\qquad C_2=\frac1{12},\qquad C_3=\frac5{144},
\quad C_k:=\mathbb E[(UV+W(1-U-V))^k].
\]

Consequently, for each \(k\ge1\),

\[
\mathbb E[Z^k]=3B_ke_2+(6C_k-9B_k)e_3.
\]

Substitution for \(k=1,2,3\) yields the three displayed formulas. In particular the \(e_3\) coefficient **vanishes in precisely the first two calculations**. No finite experiment is needed for these identities.

**4. Reconstruction.** Since \(e_2>0\), \(m_1,m_2>0\). Division recovers \(A=3m_2/m_1\), and the first and third equations recover \(e_2,e_3\). Vieta's formulas recover the unordered \(p_i\) as the roots of the displayed cubic. Their positivity and \(p_i<1/2\) are guaranteed for actual triangles. Heron's formula applied to sides \(Pp_i\) gives

\[
A^2=\frac{P^4}{16}\prod_i(1-2p_i),
\]

which determines \(P>0\) uniquely. The three recovered side lengths determine the parent triangle up to Euclidean congruence by side-side-side.

**5. Optimality of three moments.** Consider the distinct normalized side triples

\[
(p_1,p_2,p_3)=\left(\frac4{15},\frac4{15},\frac7{15}\right),
\qquad
(q_1,q_2,q_3)=\left(\frac25,\frac25,\frac15\right).
\]

Both have positive entries less than \(1/2\), sum one and satisfy \(e_2=8/25\), while their triple products differ by \(4/3375\). Scale the two triangles separately so that each has area one. Both give \(m_1=4/25\), \(m_2=4/75\), whereas their third moments are \(1187/50625\) and \(1188/50625\), respectively. Thus two initial raw moments cannot distinguish even these two noncongruent isosceles triangles; the third does.

**6. Sharp normalized moment ranges.** Since \(0<p_i<1/2\) and \(\sum p_i=1\), one has \(\sum_i p_i^2<1/2\); Cauchy–Schwarz gives \(\sum_i p_i^2\ge1/3\), with equality exactly at \(p_1=p_2=p_3=1/3\). Hence \(1/4<e_2\le1/3\). Every intervening value is attained by taking \((p_1,p_2,p_3)=(x,x,1-2x)\) for \(1/3\le x<1/2\). The first and second moment formulas now give the stated ranges and attainment assertions.

## Verification

The standalone `check_area_moment.py` uses only the Python standard library. It recomputes the universal conditional moments by exact rational polynomial integration through order six, verifies the displayed isosceles counterexample and exact moment identities, and independently samples points on actual Euclidean triangle edges to check the geometric interpretation for four parameter triples. Run `python3 check_area_moment.py`; a successful run prints `VERIFY_OK` and the exact first three moments of the two noncongruent examples. Its Monte Carlo tolerances are checks, not a substitute for the analytic proof.

## Relationship to prior work

Koroleva and Nikitin, *U-max-Statistics and Limit Theorems for Perimeters and Areas of Random Polygons* (arXiv:1301.1360v1, publicly posted January 7, 2013), study extreme areas of inscribed random polygons with sample points on a **circle**. Their model and extreme-value results do not imply fixed-triangle perimeter moment reconstruction.

Maesumi, *Triangle Inscribed-Triangle Picking* (arXiv:1804.11007; *College Mathematics Journal* 2019), derives the distribution and moments for **one independent point on each of the three different sides** of a fixed triangle. In that conditioned model the normalized law is independent of side-length ratios; its three-distinct-side conditional moments are incorporated here as \(C_k\). The present unconditional perimeter sampling additionally includes same-edge assignments with shape-dependent weights. Its full three-component mixture, universal first-to-second moment identity, sharp two-moment nonidentifiability and exact three-moment side reconstruction are not statements of that conditioned result.

Daley, Ebert and Swift, *Size distributions in random triangles* (2014), study triangles generated by random **directions of sides**, not boundary-uniform sampling from a fixed parent triangle. This is a different random-triangle model and does not directly imply the present inverse theorem. A fully exhaustive historical priority determination has not been performed.

## Limitations

The theorem gives exact population moments and distributional identities, not finite-sample performance guarantees or quantitative stability under moment estimation error. It assumes precisely three points and a nondegenerate Euclidean triangular boundary; no analogous polygonal reconstruction is claimed. Earlier work already supplies the different-side conditional component, and potential unlocated work on unconstrained perimeter sampling remains a priority risk.

## References

1. E. V. Koroleva and Ya. Yu. Nikitin, *U-max-Statistics and Limit Theorems for Perimeters and Areas of Random Polygons*, arXiv:1301.1360v1, first posted 2013-01-07, https://arxiv.org/abs/1301.1360.
2. A. Maesumi, *Triangle Inscribed-Triangle Picking*, arXiv:1804.11007, first posted 2018-04-30; *The College Mathematics Journal* 50(5), 364–371 (2019), doi:10.1080/07468342.2019.1669383, https://arxiv.org/abs/1804.11007.
3. D. J. Daley, S. Ebert and R. J. Swift, *Size distributions in random triangles*, *Journal of Applied Probability* 51(A), 283–295 (2014), doi:10.1239/jap/1417528481.
