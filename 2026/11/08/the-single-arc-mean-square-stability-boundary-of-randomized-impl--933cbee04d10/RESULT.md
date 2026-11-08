# The single-arc mean-square stability boundary of randomized implicit RK2

## Finding

For the randomized implicit two-stage Runge–Kutta methods in [1], the complete mean-square stability region of the scalar test equation is a single bounded Jordan domain, with **exactly one admissible imaginary-frequency interval at every fixed negative real part**. Its boundary has fourth-order contact with the imaginary axis and quadratic contact with the negative-real endpoint.

More precisely, let \(z=h\lambda\), and let each independent step multiply the numerical solution by
\[
R(z,U)=1+\frac{z}{1-Uz},\qquad U\sim\mathrm{Uniform}[0,1].
\]
Define
\[
\Phi(x,y)=\begin{cases}
-\log((1+x)^2+y^2)+\dfrac{x^2+y^2}{y}\arctan\!\dfrac{y}{1+x},&y>0,\\[4pt]
\dfrac{x^2}{1+x}-2\log(1+x),&y=0,
\end{cases}
\quad x\ge0,\quad y\ge0.
\]
There is a unique \(X>\sqrt2\) with \(\Phi(X,0)=0\), numerically
\[
X=4.03361046935773630689\ldots.
\]
For every \(x\in(0,X)\) there is precisely one \(B(x)>0\) with \(\Phi(x,B(x))=0\), and the **entire** mean-square stable set is
\[
\mathcal R_{\mathrm{MS}}=\{-x+iy:0<x<X,\quad |y|<B(x)\}.
\]
The function \(B\) is smooth on \((0,X)\), extends continuously with \(B(0)=B(X)=0\), and satisfies the sharp endpoint laws
\[
B(x)\sim (12x)^{1/4}\quad(x\downarrow0),
\qquad
B(x)\sim C\sqrt{X-x}\quad(x\uparrow X),
\]
where
\[
C=\sqrt{\frac{3(X^2-2)(1+X)}{X(3+2X)}}
=2.19708243699294003\ldots.
\]
In the same weakly damped limit, the corresponding frequency boundary for the earlier randomized *explicit* RK2 method [2] is \((6x)^{1/4}(1+o(1))\). Hence the implicit method has the exact asymptotic frequency-width ratio \(2^{1/4}\), not an unbounded advantage near the imaginary axis.

## Assumptions and scope

The test equation is \(v'=\lambda v\) with \(v(0)\ne0\) and complex \(\lambda\). The step parameter is \(z=h\lambda\) with fixed \(h>0\). At each step a **fresh independent** uniform random variable \(U\in[0,1]\) is used. Both schemes (S1) and (S2) in [1] have the above identical scalar multiplier. Mean-square stability means \(\mathbb E|v_n|^2\to0\) as \(n\to\infty\), equivalent to \(\mathbb E|R(z,U)|^2<1\). The theorem makes no claim about nonlinear stability or other distributions of \(U\).

## Proof

**1. Exact moment.** For \(z=-x+iy\) with \(x\ge0\) and \(y\ge0\), write \(q=y^2\) and \(t=U\). Then
\[
|R(-x+iy,t)|^2
=\frac{(1-x(1-t))^2+q(1-t)^2}{(1+xt)^2+qt^2}.
\]
The identity \(R=1+z/(1-tz)\) and differentiation of \(\log((1+xt)^2+qt^2)\) give
\[
\mathbb E|R|^2-1
=-\log((1+x)^2+y^2)
+(x^2+y^2)\int_0^1\frac{dt}{(1+xt)^2+y^2t^2}=\Phi(x,y).
\]
The last integral is \(\arctan(y/(1+x))/y\) for \(y>0\), with its continuous limit \(1/(1+x)\) at \(y=0\).

**2. Strict monotonicity across imaginary-frequency slices.** Differentiate the exact fraction with respect to \(q\). A cancellation gives
\[
\frac{\partial}{\partial q}|R(-x+i\sqrt q,t)|^2
=\frac{1-2t+2xt(1-t)}{((1+xt)^2+qt^2)^2}.
\]
Put \(w(t)=((1+xt)^2+qt^2)^{-2}\). For \(x,q\ge0\), \(w\) is nonincreasing, and
\[
\int_0^1(1-2t)w(t)\,dt
=\int_0^{1/2}(1-2t)(w(t)-w(1-t))\,dt\ge0.
\]
Moreover \(2x\int_0^1t(1-t)w(t)dt>0\) if \(x>0\); when \(x=0\), the first integral is strictly positive whenever \(q>0\). Consequently \(q\mapsto\Phi(x,\sqrt q)\) is strictly increasing on \([0,\infty)\) for each \(x\ge0\), even though its derivative is zero at \((x,q)=(0,0)\).

**3. The real-axis cutoff and complete region.** Set \(g(x)=\Phi(x,0)=x^2/(1+x)-2\log(1+x)\). Then
\[
g'(x)=\frac{x^2-2}{(1+x)^2},\qquad g(0)=0,\qquad g(x)\to\infty.
\]
Thus \(g\) is negative exactly for \(0<x<X\), with exactly one nonzero root \(X>\sqrt2\). For any fixed \(x>0\), \(\Phi(x,y)\to+\infty\) as \(y\to\infty\); strict monotonicity then gives precisely the claimed interval \(|y|<B(x)\). At \(x=0\), \(\Phi(0,0)=0\) and \(\Phi(0,y)>0\) for \(y>0\). At \(x\ge X\), all values are nonnegative.

No point with \(\operatorname{Re}z\ge0\) is mean-square stable: for every \(t\in[0,1]\) where the fractions exist, the products of the two squared-amplitude ratios at \(t\) and \(1-t\) satisfy
\[
|R(z,t)|^2|R(z,1-t)|^2
=\frac{|1+zt|^2|1+z(1-t)|^2}{|1-zt|^2|1-z(1-t)|^2}\ge1.
\]
The inequality follows from \(|1+zs|\ge|1-zs|\) for \(s\in[0,1]\) and \(\operatorname{Re}z\ge0\). Arithmetic–geometric mean applied to the two paired ratios yields \(\mathbb E|R|^2\ge1\); real positive poles produce infinite moments. This closes the classification globally. The two positive-frequency arcs meet only at the two real endpoints, so they form one Jordan boundary. The implicit function theorem gives smoothness of \(B\) in the open interval.

**4. Endpoint laws.** As \((x,q)\to(0,0)\), Taylor expansion of the exact expression yields
\[
\Phi(x,\sqrt q)=-2x+\frac{q^2}{6}+O(x^2+xq+q^3).
\]
Since \(B(x)\to0\), its boundary equation forces \(B(x)^4\sim12x\). In the plane this is fourth-order tangency \(\operatorname{Re}z=-|\operatorname{Im}z|^4/12+o(|\operatorname{Im}z|^4)\), not a singular cusp. At the other endpoint,
\[
\left.\frac{\partial\Phi(x,\sqrt q)}{\partial q}\right|_{q=0}
=\frac{x(3+2x)}{3(1+x)^3}>0\quad(x>0),
\]
while \(g'(X)=(X^2-2)/(1+X)^2>0\). The implicit function theorem in \((x,q)\) gives \(B(x)^2\sim C^2(X-x)\), with the constant above.

**5. Explicit comparison.** The mean-square multiplier of the randomized explicit RK2 method in [2, Eq. (73)] is
\[
1+2\operatorname{Re}z\left(1+\frac{|z|^2}{2}\right)
+2(\operatorname{Re}z)^2+\frac{|z|^4}{3}.
\]
For \(z=-x+iy\), the local mean-square boundary near the origin has \(y^4\sim6x\). Comparing it with the preceding implicit boundary yields the ratio \(2^{1/4}\).

## Verification

Run `python check_stability.py` with dependencies in `requirements.txt`. It checks the multiplier derivative factorization, cancellation identities, the real-axis and imaginary-axis Taylor coefficients, the transverse derivative, thousands of exact rational monotonic-weight test instances, and high-precision boundary values against independent numerical quadrature. Its accompanying `verification_output.txt` is the recorded successful execution. The global inequalities and endpoint limits are proved above and do not rely on a finite search.

## Relationship to prior work

Bochacik and Przybyłowicz [1] introduce the two randomized implicit RK2 variants and derive the same exact mean-square moment expression. Their Facts 2–6 prove left-half-plane containment, boundedness, the real-axis cutoff and a formula for the pointwise stability test. The contribution here is **not** that formula or its numerical real cutoff: it is the global strict imaginary-frequency monotonicity, the one-arc characterization and the two sharp endpoint contact laws. Bochacik and coauthors [2] derive the explicit scheme's moment polynomial; the fourth-root comparison is an analytic consequence added here. Bochacik [3] analyzes different randomized Taylor schemes; Eisenmann and coauthors [4] study a different, per-realization algebraically stable randomized SDIRK method.

## Limitations

The source's exact pointwise formula is strong prior coverage, so the claim concerns the nontrivial analytic geometry deduced from it, **not** discovery of the basic stability function. The geometric conclusions require uniform, independent random stage selection. The boundary does not describe almost-sure stability (which can hold in the whole open left half-plane), nonlinear contractivity, multi-step or correlated sampling, or the newer SDIRK construction in [4]. Further indexing or specialist literature could contain equivalent boundary-shape arguments; this is a residual originality risk. The symbolic verifier is supplemental and does not constitute independent scientific validation.

## References

[1] T. Bochacik and P. Przybyłowicz, *Convergence and stability of randomized implicit two-stage Runge–Kutta schemes*, arXiv:2404.19059 (first submitted 2024-04-29), especially Section 3.2, Facts 2–6, equations (16), (19), and Fact 5; revised arXiv version dated 2025-01-14. https://arxiv.org/abs/2404.19059

[2] T. Bochacik, M. Goćwin, P. M. Morkisz, and P. Przybyłowicz, *Randomized Runge–Kutta method — stability and convergence under inexact information*, arXiv:2006.12131 (first submitted 2020-06-22), Section 5.1, equation (73). https://arxiv.org/abs/2006.12131

[3] T. Bochacik, *A note on the probabilistic stability of randomized Taylor schemes*, arXiv:2205.10908 (first submitted 2022-05-22), Section 3. https://arxiv.org/abs/2205.10908

[4] M. Eisenmann, M. Jans, R. Kruse, and H. Podhaisky, *Error Bound and Stability Analysis for a Randomized Singly Diagonally Implicit Runge–Kutta Method*, arXiv:2607.18928 (2026-07-21). https://arxiv.org/abs/2607.18928
