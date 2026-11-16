# An interior frequency-splitting transition for three-tone Fourier leverage

## Finding

For every real \(d>0\), let
\[
V_d=\operatorname{span}_{\mathbb C}\{1,e^{idt},e^{-idt}\}\subset L^2([-1,1],dt/2),
\qquad L_d(x)=\sup_{0\ne f\in V_d}\frac{|f(x)|^2}{\frac12\int_{-1}^1|f(t)|^2\,dt}.
\]
The exact squared evaluation leverage at every real \(x\) is
\[
L_d(x)=1+\frac{(\cos(dx)-\operatorname{sinc}d)^2}{\frac12(1+\operatorname{sinc}(2d))-(\operatorname{sinc}d)^2}
+\frac{\sin^2(dx)}{\frac12(1-\operatorname{sinc}(2d))},
\quad \operatorname{sinc}u=\frac{\sin u}{u}.
\]
Both denominators are strictly positive for every \(d>0\).

Define \(y=x^2\), \(P(y)=175y^3-115y^2+9y-5\), and
\[
Q(y)=11025y^4-12180y^3-1530y^2+2028y+145.
\]
The removable collision limit and its uniform small-gap expansion for fixed \(x\) in compact sets are
\[
L_d(x)=\frac94(5y^2-2y+1)-\frac{3P(y)}{280}d^2+\frac{Q(y)}{78400}d^4+O_x(d^6).
\]
The polynomial \(P\) has precisely one zero \(y_0\) in \([0,1]\), with
\[
0.645<y_0<0.646,\qquad x_0=\sqrt{y_0}=0.803739422635396\ldots.
\]
This is an **exact sharp interior transition** for the local effect of splitting a triple collision: for \(|x|<x_0\), all sufficiently small positive gaps strictly *increase* leverage above its collision limit; for \(x_0<|x|\le1\), they strictly *decrease* it. At \(|x|=x_0\), the quadratic gap term vanishes but the quartic term is strictly negative, so the collision is still a strict local maximum.

More precisely, put \(R(y)=6675y^2-3246y-5\), so that \(R(y_0)>0\), and
\[
b_0=-\frac{R(y_0)}{98000}<0,\qquad C_0=\frac{525P'(y_0)}{R(y_0)}>0.
\]
There exists \(\varepsilon>0\) such that for every \(y\in(y_0-\varepsilon,y_0)\), the function \(d\mapsto L_d(\sqrt y)\) has exactly one stationary point in a fixed sufficiently small positive-gap neighborhood of zero; it is a strict local maximum at \(d_*(y)\) with
\[
d_*(y)=\sqrt{C_0}\,(y_0-y)^{1/2}+O((y_0-y)^{3/2}),\qquad C_0=61.058112569774\ldots.
\]
Its gain over the collision limit has the sharp quadratic onset
\[
L_{d_*(y)}(\sqrt y)-L_0(\sqrt y)
=\frac{-\big(3P'(y_0)/280\big)^2}{4b_0}\,(y_0-y)^2+O((y_0-y)^3),
\]
where \(L_0(x)=\frac94(5x^4-2x^2+1)\) is defined by continuous extension. The positive prefactor is \(26.0073481851\ldots\). On the other side of the threshold, the collision is strictly locally maximizing for all sufficiently small gaps. These are **local** frequency-gap assertions and make no statement about optimal gaps over the entire half-line.

## Assumptions and scope

The observation inner product uses the probability normalization \(\frac12\int_{-1}^1\); the coefficient field is complex. The three frequencies are \(-d,0,d\), with arbitrary common carrier modulation allowed because it leaves absolute values unchanged. The evaluation location is real; the phase diagram concerns \(|x|\le1\). The limiting space at a triple frequency collision is the polynomial space of degree at most two, and its evaluation norm is interpreted by a limit, not as the norm of the one-dimensional space at \(d=0\). A local frequency-gap maximizer is not asserted to be globally maximizing.

## Proof

**Exact kernel.** For \(d>0\), write \(s=\sin d/d\), \(h=\sin(2d)/(2d)\). The functions \(1\), \(\cos(dt)-s\), and \(\sin(dt)\) form a mutually orthogonal basis of \(V_d\), with squared norms
\[
1,\quad A=\frac{1+h}{2}-s^2,\quad B=\frac{1-h}{2}.
\]
The last two are strictly positive because the corresponding functions are nonzero in \(L^2([-1,1])\). Orthogonal Riesz evaluation yields \(L_d(x)=1+(\cos(dx)-s)^2/A+\sin^2(dx)/B\), with equality attained by a nonzero multiple of its reproducing kernel.

**Exact collision expansion.** Put \(q=d^2\). Substitution of the entire series
\[
s=\sum_{j\ge0}\frac{(-1)^jq^j}{(2j+1)!},\quad h=\sum_{j\ge0}\frac{(-1)^j4^jq^j}{(2j+1)!},\quad
\cos(dx)=\sum_{j\ge0}\frac{(-1)^jy^jq^j}{(2j)!}
\]
into the exact formula shows \(A=q^2/45+O(q^3)\) and \(B=q/3+O(q^2)\). Both evaluation numerators vanish to matching order, so the apparent singularity at \(q=0\) is removable and the quotient is real analytic jointly in \((q,y)\) near \(q=0\). Formal series division through second order yields exactly
\[
L_{\sqrt q}(\sqrt y)=\frac94(5y^2-2y+1)-\frac{3P(y)}{280}q+\frac{Q(y)}{78400}q^2+O(q^3).
\]
All coefficients follow from rational factorial series; the accompanying standalone checker independently reconstructs these coefficients using exact rational arithmetic at several locations. The constant term is also the degree-two Legendre evaluation kernel \(1+3x^2+\frac54(3x^2-1)^2\).

**Unique sharp transition.** For \(0\le y\le1/2\), \(175y^3-115y^2\le-\frac{55}{2}y^2\) and \(9y-5\le-1/2\), so \(P(y)<0\). For \(y\ge1/2\), one has \(P''(y)=1050y-230>0\) and \(P'(1/2)=101/4>0\); hence \(P\) increases strictly and crosses zero exactly once before one, because \(P(1/2)<0<P(1)\). Exact rational substitution gives \(P(645/1000)<0<P(646/1000)\), and also \(P(3/5)<0\). Thus \(3/5<y_0<1\). This proves the asserted sign changes of the \(q\)-coefficient. At \(y_0\), polynomial division gives the exact identity
\[
Q(y)=\left(63y-\frac{141}{5}\right)P(y)-\frac45\big(6675y^2-3246y-5\big).
\]
Since \(R(3/5)>0\) and \(R'(y)>0\) on \([3/5,1]\), it follows that \(Q(y_0)=-4R(y_0)/5<0\). Thus at the critical point the quartic coefficient is strictly negative. Because the \(q\)-expansion is analytic, the sign conclusions apply to all sufficiently small positive gaps at every stated location.

**Emerging optimal gap.** Define \(\Phi(q,y)=\partial_q L_{\sqrt q}(\sqrt y)\) via its analytic continuation. At \((q,y)=(0,y_0)\), \(\Phi=0\), \(\partial_q\Phi=2b_0<0\), and \(\partial_y\Phi=-3P'(y_0)/280<0\). The real-analytic implicit-function theorem gives a unique small stationary branch
\[
q_*(y)=-\frac{-3P'(y_0)/280}{2b_0}(y-y_0)+O((y-y_0)^2)=C_0(y_0-y)+O((y_0-y)^2).
\]
For \(y<y_0\) close enough it is positive and has negative second derivative with respect to \(q\), hence is a strict local maximum also in \(d>0\). For \(y>y_0\), the continued branch is at negative \(q\), so no small positive stationary gap exists and the leverage decreases from collision. Taking square roots proves the \(1/2\)-power onset. Substitution into the analytic series gives the displayed positive quadratic gain. This concludes the proof.

## Verification

Run `python3 CHECK.py`. It performs eight exact Fraction-valued Taylor-coefficient comparisons (three coefficients per location), exact rational bracketing and polynomial identities for the transition, and 96 independent numerical comparisons of the orthogonal-kernel formula with a separate three-dimensional Gram-matrix solver. It does not assert that numerical comparisons prove the universal analytic statements.

## Relationship to prior work

Zhang, *Optimal Extrapolation Bounds for Sparse Fourier Sums*, arXiv:2607.10501 (first posted July 11, 2026), §5.3, studies leverage scores for arbitrary sparse exponential families and derives uniform **exterior** bounds; it does not state the present **interior** frequency-splitting sign threshold or emerging-gap branch. The published result *Sharp endpoint Nikolskii constant for symmetric three-tone Fourier sums* supplies the same orthogonal three-tone basis and a sharp uniform inequality at **\(x=1\)**; it does not contain the interior phase transition at \(\sqrt{y_0}\), the quartic critical sign, or the square-root onset. Erdélyi, *Inequalities for exponential sums* (arXiv:1602.02315, 2016), establishes broad Nikolskii-type inequalities for exponential sums rather than this exact local interior leverage phase diagram. Classical Legendre reproducing kernels determine the collision limit but not the side on which opening a nonzero frequency gap increases leverage.

## Limitations

The result is a complete *local* frequency-gap transition around a threefold collision, not the global supremum over positive gaps and not a theorem for arbitrary non-equispaced triples or arbitrary weight functions. It makes no claim about prediction points outside the observation interval. The identities are exact, but independent mathematical audit and exhaustive bibliographic priority verification have not been performed; differently indexed earlier Christoffel/Gram perturbation calculations could overlap.

## References

1. Ruizhe Zhang, *Optimal Extrapolation Bounds for Sparse Fourier Sums*, arXiv:2607.10501, v1 publicly posted July 11, 2026, especially §5.3; https://arxiv.org/html/2607.10501v2.
2. *Sharp endpoint Nikolskii constant for symmetric three-tone Fourier sums*, published mathematical finding, November 8, 2026; https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-sharp-endpoint-nikolskii-constant-for-symmetric-three-tone-fouri--e11889d28f9d/RESULT.md.
3. Tamás Erdélyi, *Inequalities for exponential sums*, arXiv:1602.02315 (2016), especially Theorem 2.3; https://arxiv.org/pdf/1602.02315.
4. Classical Legendre-polynomial orthogonality and the Christoffel–Darboux evaluation kernel on \([-1,1]\).
