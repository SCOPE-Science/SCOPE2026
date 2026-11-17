# Unique variation-optimal symmetric four-knot natural cubic interpolation

## Finding

Let \(r>0\) and put four interpolation knots at \(0,1,1+r,2+r\). For real data \(y=(y_0,y_1,y_2,y_3)\), let \(S_r y\) be the unique natural cubic interpolant (continuous through its first two derivatives, with zero second derivative at the two outer knots). Define discrete and continuous total variations by
\[
 V_d(y)=|y_1-y_0|+|y_2-y_1|+|y_3-y_2|,
 \qquad V_c(s)=\int_0^{2+r}|s'(x)|\,dx.
\]
Set \(D(r)=(r+2)(3r+2)\), and, for \(0\leq v\leq1\),
\[
 F_r(v)=\frac{r^2v(1-v)[3r(1-v)+4-2v]}{D(r)},\quad
 q(r)=\frac{2r+2-\frac13\sqrt{9r^2+18r+12}}{3r+2}.
\]
Define the two explicit branch functions
\[
 O(r)=1+2F_r(q(r))+\frac{4r}{3\sqrt3\,D(r)},\qquad
 C(r)=1+\frac{8}{3\sqrt3\,r(r+2)}.
\]
Then for every \(r>0\),
\[
 \boxed{\sup_{V_d(y)>0}\frac{V_c(S_r y)}{V_d(y)}=\max\{O(r),C(r)\}.}
\]
The outer and central single-jump data attain the two branches, respectively: \((0,1,1,1)\) (or its reflection) attains \(O(r)\), and \((0,0,1,1)\) attains \(C(r)\). The function \(O\) is strictly increasing on \((0,\infty)\), while \(C\) is strictly decreasing. Hence a **unique symmetric four-knot mesh** minimizes the sharp gain: its outer-to-middle interval ratio is \(1:r_*:1\), with \(r_*\) the unique positive solution of \(O(r_*)=C(r_*)\). Exact rational interval evaluation gives
\[
 1.42882553<r_*<1.42882554,\qquad
 \max\{O(r_*),C(r_*)\}=1.314255954773597\ldots .
\]
In contrast, the equally spaced case \(r=1\) has exact gain \(1+8/(9\sqrt3)=1.513200239279667\ldots\). The optimized symmetric placement lowers the worst-case variation gain by approximately \(13.15\%\).

## Assumptions and scope

All data are real, all knot spacings are positive, and the outer two spacing lengths are constrained equal; common positive rescaling and translation of the knot axis do not change variation gain. The only interpolation boundary conditions are \((S_r y)''(0)=(S_r y)''(2+r)=0\). No monotonicity assumption is imposed on input data. This is an operator seminorm on data modulo constant vectors, rather than a pointwise or maximum-norm estimate.

## Proof

**1. Reduction to three steps.** Every data vector is a constant vector plus a combination of three unit steps, with coefficients \(d_j=y_j-y_{j-1}\), \(j=1,2,3\). A natural cubic spline reproduces constants. Total variation is subadditive and homogeneous, so the norm is at most the largest variation of these three spline step responses. Applying a single unit step yields the reverse inequality. Reflection of the symmetric mesh exchanges the first and third steps.

**2. Curvature matrix.** Write \(M_i=(S_r y)''(x_i)\), so \(M_0=M_3=0\). If the three interval slopes are \(s_1=d_1\), \(s_2=d_2/r\), \(s_3=d_3\), the natural cubic matching conditions are
\[
 \begin{pmatrix}2(1+r)&r\\r&2(1+r)\end{pmatrix}
 \binom{M_1}{M_2}=6\binom{s_2-s_1}{s_3-s_2}.
\]
Its determinant is \(D(r)>0\). On an interval of length \(h\), for normalized local coordinate \(t\in[0,1]\), the exact cubic equals
\[
 s(t)=(1-t)y_i+ty_{i+1}+\frac{h^2}{6}\left[M_i((1-t)^3-(1-t))+M_{i+1}(t^3-t)\right].
\]
These equations uniquely determine all three pieces.

**3. Central step.** For \((0,0,1,1)\) the curvature vector is \((0,A,-A,0)\) with \(A=6/[r(r+2)]\). The first and third pieces exhibit, respectively, a negative excursion below zero and a positive excursion above one. Each excursion has depth \(A/(9\sqrt3)\), because \(t-t^3\) maximizes at \(t=1/\sqrt3\). The central piece travels monotonically from zero to one: its normalized derivative is
\[
 1+\frac{r}{r+2}(-1+6t-6t^2)>0\qquad(0\le t\le1).
\]
Its total variation is therefore \(1+4A/(9\sqrt3)=C(r)\).

**4. Outer step.** For \((0,1,1,1)\), \(M_1=-12(r+1)/D(r)\) and \(M_2=6r/D(r)\). The first piece increases from zero to one: its normalized expression is \((1+c)t-ct^3\), with \(c=2(r+1)/D(r)<1/2\). The middle piece has both endpoint values one and rises above one by exactly \(F_r(t)\). On \((0,1)\), the factors \(t\), \(1-t\), and \(3r(1-t)+4-2t\) are positive and strictly log-concave; their product has a unique maximizer. Solving the quadratic derivative equation identifies it as \(q(r)\). The last interval makes a single negative excursion below one of depth \(M_2/(9\sqrt3)\). Summing all three piecewise variations gives \(O(r)\).

**5. Monotonicity and global minimax.** Direct differentiation yields
\[
 \frac{\partial F_r(v)}{\partial r}=\frac{rv(1-v)}{D(r)^2}
 \big[(1-v)(9r^3+48r^2+52r+16)+16r+16\big]>0.
\]
Moreover \(1/3<q(r)<1-1/\sqrt3<1/2\). The derivative of the last additive term in \(O(r)/2\) is \(2(4-3r^2)/(3\sqrt3 D(r)^2)\). For \(r\le2/\sqrt3\) both contributions to the derivative of \(O/2\) are nonnegative, one strictly positive. For \(r>2/\sqrt3\), use \(q(1-q)>2/9\) and \(1-q>1/2\) to obtain
\[
 \left.\frac{\partial F_r(v)}{\partial r}\right|_{v=q(r)}
 >\frac{r^4+(32/9)r^2}{D(r)^2}
 >\frac{2r^2}{\sqrt3 D(r)^2}
 >-\frac{2(4-3r^2)}{3\sqrt3 D(r)^2}.
\]
Since \(F_r'(q(r))=0\), differentiation of \(F_r(q(r))\) needs only its partial derivative. Thus \(O'(r)>0\). The explicit formula shows \(C'(r)<0\). Finally \(O(r)\to1\) as \(r\downarrow0\), while \(C(r)\to\infty\); as \(r\to\infty\), \(C(r)\to1\), while \(O(r)\to\infty\), since \(F_r(1/3)\sim4r/27\). Continuity forces precisely one crossing. The maximum of an increasing and decreasing function decreases before this crossing and increases after it, proving unique optimality.

## Verification

The accompanying `check_natural4.py` is a standalone Python 3 program requiring only the standard library. It independently reconstructs the spline curvature equations and middle cubic identities with exact rational numbers, encloses the minimizer between two rational endpoints using outward-rounded integer-square-root interval arithmetic, and stress-tests arbitrary four-sample inputs against the sharp norm using all real critical points of each cubic segment. The finite stress tests are diagnostic; the complete infinite-parameter claim follows from the analytical proof above. Run `python3 check_natural4.py` from this directory.

## Relationship to prior work

Beatson and Chacko's report *Which Cubic Spline Should One Use?* (dated 30 November 1990; journal 1992) examines several cubic spline boundary conditions, including natural splines, with maximum-norm operator and derivative estimates. Its first derived operator is evaluated in a supremum norm, whereas the theorem above minimizes total continuous variation relative to discrete variation, and isolates the optimal **mesh ratio**, not the choice of end conditions. Kobza (2002) optimizes integral squared-derivative and discrete quadratic energies over spline boundary parameters, with knot locations given; this is not the stated variation minimax. Hall (1973) establishes uniform approximation-error results. An accessible published three-knot natural spline positivity-defect formula concerns a different number of knots, a different norm, and no competing central/outer step amplification. A separate sharp four-node variation-optimal result concerns a **single global cubic Lagrange polynomial**, with a different interpolation operator and free knot geometry; it does not imply the present natural-cubic-spline mesh minimax. No equivalence or implication of the new four-knot mesh optimum was found in the inspected material.

## Limitations

Only the one-parameter symmetric family of four-knot natural cubic interpolants is optimized. There is no claim about unrestricted four-knot geometry, other spline end conditions, more knots, monotone-interpolant construction, or approximation error. The result establishes a deterministic worst-case operator norm, not an average-data-performance criterion. Earlier unpublished or unindexed equivalences cannot be excluded by available searches.

## References

- R. K. Beatson and E. Chacko, *Which Cubic Spline Should One Use?*, University of Canterbury report 59 (dated 30 November 1990), later SIAM J. Sci. Stat. Comput. 13 (1992), 1009–1024. https://ir.canterbury.ac.nz/server/api/core/bitstreams/76c796a1-5524-4a10-8394-a0e93ecc05e5/content ; DOI 10.1137/0913059.
- J. Kobza, *Cubic splines with minimal norm*, Applications of Mathematics 47 (2002), 285–295. https://dml.cz/handle/10338.dmlcz/134498 .
- C. A. Hall, *Natural Cubic and Bicubic Spline Interpolation*, SIAM J. Numer. Anal. (1973). https://doi.org/10.1137/0710088 .
- Published three-knot natural-cubic positivity-defect result (2026). Public record identifier `0b51d8330304`.
- Four-node global cubic Lagrange variation-optimality, 2026, opaque record identifier `068c5a0b-fb03-4b77-a8ac-1a2605b8cf47` (different interpolation operator).
