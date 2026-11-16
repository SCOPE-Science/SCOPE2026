# Sharp negative-set length in the first three positive-Fourier Hermite modes

## Finding

For the unitary Fourier transform \(\widehat f(\xi)=\int_{\mathbb R}f(x)e^{-2\pi i x\xi}\,dx\), consider the real Fourier-+1 eigenspace
\[
\mathcal V_8=\operatorname{span}_{\mathbb R}\{e^{-\pi x^2}L_0^{-1/2}(2\pi x^2),\ e^{-\pi x^2}L_2^{-1/2}(2\pi x^2),\ e^{-\pi x^2}L_4^{-1/2}(2\pi x^2)\},
\]
where \(L_j^\alpha\) is the generalized Laguerre polynomial. Among all \(f\in\mathcal V_8\setminus\{0\}\) with \(f(0)=0\), the exact minimum finite length of the nonpositive set is
\[
\boxed{\min |\{x\in\mathbb R:f(x)\leq0\}|=\frac{2}{\sqrt\pi}\sqrt{7-\sqrt{35}}=1.1747723539032928\ldots.}
\]
The unique minimizing ray, up to multiplication by a positive constant, is
\[
\boxed{f_*(x)=e^{-\pi x^2}z^2(z^2-14z+35),\quad z=2\pi x^2.}
\]
Its negative set (apart from isolated zeros, which have zero measure) is precisely
\[
7-\sqrt{14}<2\pi x^2<7+\sqrt{14}.
\]
In particular, the optimum has a double zero at the origin but its negative set does not contain an interval around the origin. This is a finite-dimensional sharp benchmark and an explicit admissible upper bound for the unrestricted one-dimensional definite-set uncertainty problem, not its unrestricted optimum.

## Assumptions and scope

Functions are real-valued, Schwartz, even, and their Fourier transforms satisfy \(\widehat f=f\). Only the three modes of Hermite orders \(0,4,8\) are allowed. Lebesgue length counts all nonpositive points, but finitely many isolated zeros do not change it. The only normalization is \(f(0)=0\); positive scalar multiplication leaves the objective unchanged, whereas negative leading coefficient gives an infinite nonpositive set. We use \(z=2\pi x^2\geq0\), for which the length of a pair of intervals corresponding to \(u<z<v\) is \(\sqrt{2/\pi}(\sqrt v-\sqrt u)\).

## Proof

**1. Fourier eigenfunctions and projective reduction.** The Laguerre-Hermite Fourier identity gives eigenvalue \((-1)^j=+1\) to \(e^{-\pi x^2}L_{2j}^{-1/2}(2\pi x^2)\). The first three such Laguerre polynomials are
\[
L_0^{-1/2}(z)=1,\quad L_2^{-1/2}(z)=\frac{z^2}{2}-\frac{3z}{2}+\frac38,
\]
\[
L_4^{-1/2}(z)=\frac{z^4}{24}-\frac{7z^3}{12}+\frac{35z^2}{16}-\frac{35z}{16}+\frac{35}{128}.
\]
For any nonzero admissible function with a positive degree-eight coefficient, scale that coefficient so that its polynomial is \(L_4^{-1/2}+rL_2^{-1/2}+cL_0^{-1/2}\), and use \(f(0)=0\) to eliminate \(c\). The result is
\[
f_r(x)=e^{-\pi x^2}\frac z{48}q_r(z),\qquad
q_r(z)=2z^3-28z^2+(105+24r)z-105-72r.
\]
The degenerate positive-leading degree-four ray is \(e^{-\pi x^2}z(z-3)\), up to a positive constant; its nonpositive length is \(\sqrt{6/\pi}\), strictly larger than the stated minimum. A negative leading coefficient at either degree has nonpositive values on an unbounded tail, giving infinite measure.

**2. The distinguished parameter.** Put \(r_0=-35/24\). Then
\[
q_{r_0}(z)=2z(z^2-14z+35),\qquad q_r(z)=q_{r_0}(z)+24(r-r_0)(z-3).
\]
The two positive nonzero roots at \(r_0\) are \(7\pm\sqrt{14}\). Thus
\[
\begin{aligned}
m(r_0)&=\sqrt{\frac2\pi}\left(\sqrt{7+\sqrt{14}}-\sqrt{7-\sqrt{14}}\right)\\
&=\frac2{\sqrt\pi}\sqrt{7-\sqrt{35}}.
\end{aligned}
\]
For \(r\leq r_0\), \(q_r\geq q_{r_0}\geq0\) on \([0,3]\) and \(q_r\leq q_{r_0}\) on \((3,\infty)\). Hence its negative-set length is at least \(m(r_0)\), with strict inequality for \(r<r_0\).

**3. Root geometry.** An exact discriminant calculation gives
\[
\operatorname{disc}_z(q_r)=-12F(r),\qquad F(r)=9216r^3-15168r^2+16128r-7105.
\]
The quadratic \(F'(r)\) is strictly positive because its discriminant is negative and its leading coefficient positive. Thus \(F\) has exactly one real zero \(\rho\in(0,1)\). For \(r_0<r<\rho\), the polynomial has exactly three positive simple roots \(0<a(r)<3<b(r)<c(r)\), as follows from \(q_r(0)<0\), \(q_r(3)=12>0\), and the discriminant sign. The nonpositive-set length is
\[
m(r)=\sqrt{\frac2\pi}\left(\sqrt{a(r)}+\sqrt{c(r)}-\sqrt{b(r)}\right).
\]
At \(r=\rho\) the two rightmost roots merge into a positive double root \(t\), while the remaining root is \(a_*=14-2t\in(0,3)\). The double-root condition reduces to
\[
P(t)=2t^3-23t^2+84t-105=0.
\]
There is exactly one positive root of \(P\): its stationary points are at \(3\) and \(14/3\), its values at both are negative, and its leading coefficient is positive. In fact \(14/3<t<\sqrt{35}\) because \(P(\sqrt{35})=-910+154\sqrt{35}>0\). For \(r_0<r<\rho\), the roots satisfy \(3<b(r)<t<c(r)\). At the collision,
\[
m(\rho)^2=\frac{2}{\pi}(14-2t)=\frac4\pi(7-t)>\frac4\pi(7-\sqrt{35})=m(r_0)^2.
\]
For \(r>\rho\), there is only one positive simple root \(a(r)<3\), and \(q_r\) decreases pointwise on \([0,3)\) as \(r\) increases, so its negative interval \([0,a(r))\) grows strictly; hence \(m(r)>m(\rho)\).

**4. Strict concavity prevents a hidden interior improvement.** An implicit differentiation of \(q_r(s(r))=0\) yields, for each moving simple root \(s\),
\[
\frac{d^2}{dr^2}\sqrt{s(r)}
=-\frac{36(s-3)^3H(s)}{s^{3/2}P(s)^3},
\quad H(s)=6s^4-65s^3+261s^2-441s+315.
\]
The polynomial \(H\) is strictly positive for every \(s\geq0\): its exact Bernstein coefficients on \([0,2]\) are \((315,189/2,48,91/2,53)\), on \([2,3]\) are \((53,227/4,63,135/2,72)\), and \(H(3+u)=6u^4+7u^3+18u+72\) for \(u\geq0\). Since \(P<0\) on \([0,t)\) and \(P>0\) on \((t,\infty)\), the functions \(\sqrt{a(r)}\) and \(\sqrt{c(r)}\) have strictly negative second derivative, whereas \(\sqrt{b(r)}\) has strictly positive second derivative. Hence \(m(r)\) is strictly concave throughout \((r_0,\rho)\); its minimum on the closed interval lies at an endpoint. The endpoint \(r_0\) wins strictly by Step 3. Combining all parameter ranges and the degree-four ray proves the sharp minimum and uniqueness. \(\square\)

## Verification

The accompanying `degree8_definite_set_check.py` is standalone and uses SymPy and NumPy. Running `python degree8_definite_set_check.py` checks the exact Laguerre reduction, the independent Hermite-polynomial Fourier transform, discriminant and critical-root algebra, implicit-curvature identity, Bernstein positivity certificates, extremal length, and additional numerical root-interval comparisons. All checks passed. Finite samples are supplemental, not a substitute for the algebraic proof covering all real \(r\).

## Relationship to prior work

Roni Edwin's 2026 work introduces minimization of the nonpositive-set measure for Fourier eigenfunctions (Problem 1.6) and derives a general measure lower bound; it does not identify the exact optimum in this specified three-mode one-dimensional subspace. Gonçalves, Oliveira e Silva, and Steinerberger analyze Hermite Fourier eigenfunctions and a different quantity, the radius of the last sign change. Edwin's earlier paper and Cohn, Dong, and Gonçalves study the usual sign-radius problem, especially high-dimensional behavior, rather than this exact negative-set length. No claim of a solution to the unrestricted minimum is made.

## Limitations

The result is sharp only in the real three-dimensional mode span before imposing its single value constraint. Higher Hermite modes or general Fourier eigenfunctions can change the unrestricted infimum. The source comparison does not eliminate the possibility of an older equivalent finite-degree volume calculation under different terminology. The numerical checker does not prove the infinite-domain statement; exact polynomial arguments do.

## References

1. Roni Edwin, *Fourier inequalities and sign uncertainty II*, arXiv:2611.08224v1 (first public 2026-11-05), https://arxiv.org/html/2611.08224v1.
2. Felipe Gonçalves, Diogo Oliveira e Silva, and Stefan Steinerberger, *Hermite polynomials, linear flows on the torus, and an uncertainty principle for roots*, arXiv:1602.03366, https://arxiv.org/abs/1602.03366.
3. Roni Edwin, *Fourier inequalities and sign uncertainty*, arXiv:2505.15994, https://arxiv.org/abs/2505.15994.
4. Henry Cohn, Dingding Dong, and Felipe Gonçalves, *Sign uncertainty principles and low-degree polynomials*, arXiv:2210.01684, https://arxiv.org/abs/2210.01684.
