# Sharp Bernstein curvature-variation error and central hinge localization

## Finding

For every integer \(n\ge1\), the classical Bernstein operator
\[
(B_nf)(x)=\sum_{k=0}^n\binom nk x^k(1-x)^{n-k}f(k/n)
\]
acts on the real curvature-variation class described below. Its sharp Lebesgue-square-error norm is exactly
\[
C_n^2=\max_{0\le t\le1}\int_0^1\bigl(B_nh_t(x)-h_t(x)\bigr)^2\,dx,\quad h_t(x)=(x-t)_+.
\]
All nonaffine extremizers are affine functions plus one nonzero hinge at a maximizing interior knot. The asymptotically sharp constant and optimizer location are
\[
\boxed{\lim_{n\to\infty}n^{3/2}C_n^2=\frac{1-1/\sqrt2}{12\sqrt\pi}=0.01377060859552697\ldots,}\qquad
\boxed{\lim_{n\to\infty}t_n=\frac12.}
\]
Thus \(C_n\sim0.11734823643978197\ldots\,n^{-3/4}\). The location assertion applies to **every sequence of maximizers**; finite-degree uniqueness is not asserted.

## Assumptions and scope

The domain is \([0,1]\) with Lebesgue \(L^2\) norm. A real input belongs to \(W^{1,1}(0,1)\) and has distributional first derivative \(f'\in BV(0,1)\), meaning that \(\mu=D^2f\) is a finite signed Radon measure on \((0,1)\). Its seminorm is \(\mathcal V_2(f)=|\mu|((0,1))\). The quotient disregards affine functions, reproduced exactly by \(B_n\). Functions have their canonical absolutely continuous representatives on \([0,1]\), so point sampling is unambiguous. The displayed supremum is over positive seminorm. The limiting statement concerns positive integer degrees tending to infinity.

## Proof

**1. Exact reduction and extremizer rigidity.** Distributional integration twice yields, for some real \(a,b\),
\[
f(x)=a+bx+\int_{(0,1)}(x-t)_+\,d\mu(t).
\]
Since Bernstein averaging reproduces affines,
\[
(B_n-I)f=\int_{(0,1)}K_{n,t}\,d\mu(t),\quad
K_{n,t}(x)=\mathbb E\bigl[(S_{n,x}/n-t)_+\bigr]-(x-t)_+,
\]
where \(S_{n,x}\) is binomial with parameters \(n,x\). Jensen's inequality gives \(K_{n,t}\ge0\). Minkowski's integral inequality gives
\[
\|(B_n-I)f\|_2\le\left(\max_{t\in[0,1]}\|K_{n,t}\|_2\right)|\mu|((0,1)).
\]
The maximum exists by continuity in \(t\), is positive (for every interior \(t\)), and is not at either endpoint because the endpoint hinges are affine. A unit atom at a maximizing interior point attains it. Equality for a general nonzero signed measure requires all normalized signed Hilbert vectors \(\operatorname{sgn}(d\mu)K_{n,t}/\|K_{n,t}\|_2\) in its support to coincide. Yet distinct knots \(t\ne u\) have noncolinear vectors: their distributional second derivatives, as functions of \(x\), contain respectively \(-\delta_t\) and \(-\delta_u\), while the remaining terms are polynomial and therefore smooth. Consequently equality forces \(\mu=c\delta_t\), giving exactly the stated hinge classification.

For reproducibility, set \(q=\lfloor nt\rfloor\). An exact finite-degree expression is
\[
K_{n,t}(x)=x\,\Pr\{S_{n-1,x}\ge q\}
-t\,\Pr\{S_{n,x}\ge q+1\}-(x-t)_+.
\]
The binomial-tail formula follows from the exact weighted identity \(\frac{k}{n}\binom nk x^k(1-x)^{n-k}=x\binom{n-1}{k-1}x^{k-1}(1-x)^{n-k}\) for positive \(k\).

**2. The Gaussian boundary layer.** Put \(\sigma_t=\sqrt{t(1-t)}\), \(\varphi(s)=(2\pi)^{-1/2}e^{-s^2/2}\), and \(\Phi\) the standard-normal distribution function. For every sequence of interior knots \(t_n\to t_0\in(0,1)\), fix real \(s\) and set \(x_n=t_n+\sigma_{t_n}s/\sqrt n\). The triangular-array binomial CLT, together with uniform bounded second moments, gives
\[
\frac{\sqrt n}{\sigma_{t_n}}K_{n,t_n}(x_n)\longrightarrow
G(s)=\varphi(s)-|s|\Phi(-|s|).
\]
To justify the integration, let \(Y=S_{n,x}/n\). From \(\mathbb E(Y-x)=0\) and the inequality \((z-a)_+\le z^2/(4a)\) for \(a>0\), applied on the appropriate side of the knot, we have
\[
0\le K_{n,t}(x)\le
\min\!\left(\sqrt{\frac{x(1-x)}n},\frac{x(1-x)}{4n|x-t|}\right)
\quad(x\ne t).
\]
After the boundary-layer substitution and for knots in a compact subinterval of \((0,1)\), this bounds the rescaled kernel by \(M\min(1,|s|^{-1})\), whose square is integrable. Dominated convergence therefore proves
\[
\lim_{n\to\infty}n^{3/2}\int_0^1K_{n,t_n}(x)^2dx
=\sigma_{t_0}^3\int_{\mathbb R}G(s)^2ds.
\]

**3. The endpoints cannot compete.** Suppose \(t=t_n\to0\) (the right endpoint follows by reflection). For sufficiently large \(n\), \(t\le1/2\). Split the integral into \([0,t/2]\), \([t/2,2t]\) and \([2t,1]\). On the outer intervals the preceding bound gives respectively \(K_{n,t}(x)\le x/(2nt)\) and \(K_{n,t}(x)\le(1-x)/(2n)\). Their squared integrals are bounded by \(t/(96n^2)\) and \(1/(12n^2)\). On the middle interval, \(x(1-x)\le2t\); writing \(u=x-t\) and using the minimum bound gives
\[
\int_{t/2}^{2t}K_{n,t}(x)^2dx
\le\int_{\mathbb R}\min\!\left(\frac{2t}{n},\frac{t^2}{4n^2u^2}\right)du
=\frac{2\sqrt2\,t^{3/2}}{n^{3/2}}.
\]
Thus \(n^{3/2}\|K_{n,t_n}\|_2^2\to0\) whenever \(t_n\to0\), and similarly at \(1\). This is uniform over arbitrarily fast or slow boundary approaches, including knots depending on \(n\).

**4. Evaluation and global maximum.** Let \(Q(s)=\Phi(-s)\) for \(s\ge0\), and \(A=\int_0^\infty\varphi(s)^2ds=1/(4\sqrt\pi)\). Integration by parts gives
\[
\int_0^\infty s\varphi(s)Q(s)ds=\frac{\varphi(0)}2-A,\qquad
\int_0^\infty s^2Q(s)^2ds=\frac{2\varphi(0)}3-\frac{5A}3.
\]
Consequently
\[
I:=\int_{\mathbb R}G(s)^2ds
=\frac2{3\sqrt\pi}\left(1-\frac1{\sqrt2}\right).
\]
The function \(\sigma_t^3=[t(1-t)]^{3/2}\) has a unique maximum \(1/8\) at \(t=1/2\). Select maximizing knots at every degree; by compactness each subsequence has a convergent subsubsequence. The endpoint estimate rules out boundary limits, and the interior Gaussian limit forces every such limit to maximize \(\sigma_t^3\), hence to equal \(1/2\). Evaluating at \(t=1/2\) gives the matching lower bound. Therefore \(n^{3/2}C_n^2\to I/8=(1-1/\sqrt2)/(12\sqrt\pi)\), and all maximizing knots converge to the midpoint.

## Verification

The attached `checker.py` independently evaluates the exact binomial-tail kernel, tests its elementary properties and degree-one identity, numerically compares scaled errors at several degrees and knots, and evaluates the Gaussian integral against the closed form. It is finite numerical evidence **supporting**, not replacing, the analytical infinite-degree proof. To reproduce, use Python with NumPy and SciPy and run `python checker.py`. Finite-knot maxima need not lie at the midpoint; only their large-degree locations are claimed.

## Relationship to prior work

Bojanic and Cheng (1989) establish pointwise Bernstein asymptotics and estimates for inputs with bounded-variation derivatives, including the diagonal absolute-value kink. Their accessible abstract does not assert the integrated sharp curvature-variation-to-\(L^2\) norm or its global optimizing knots; the complete article was unavailable for comparison, so historical-priority uncertainty remains. Adell and Lekuona (2015), in their complete open article, prove pointwise second-modulus inequalities for positive operators and piecewise-linear inputs, not this global integrated operator norm. Adell, Garrancho and Martínez-Sánchez (2024) give pointwise discontinuity/derivative-jump estimates (in particular their Section 5 and Corollary 5.5), rather than this sharp integrated constant. Gonska and Zhou (1995) study a Bernstein extremal problem for pointwise second moduli; its objective and normalization differ. Related published Bernstein stability, Gaussian sampling and first-order bounded-variation residual calculations do not imply the present second-variation statement from their reported results.

## Limitations

No assertion is made that a maximizing knot is unique for an individual finite degree, or that it equals one-half for every degree; the latter is in fact false at some degrees. The proof does not treat other \(L^p\) exponents, irregular sampling nodes, other smoothers or an arbitrary signed-valued output norm. The originality assessment is based on inspected literature and actual database comparisons, not a proof of historical uniqueness; the full Bojanic–Cheng article could not be obtained. There has been no independent mathematical audit.

## References

1. R. Bojanic and F. Cheng (1989), *Rate of convergence of Bernstein polynomials for functions with derivatives of bounded variation*, J. Math. Anal. Appl. **141**, 136–151, https://doi.org/10.1016/0022-247X(89)90211-4 (abstract examined; full text unavailable).
2. J. A. Adell and A. Lekuona (2015), *Quantitative Estimates for Positive Linear Operators in terms of the Usual Second Modulus*, Abstract Appl. Anal., article 915358, https://doi.org/10.1155/2015/915358 (open full text inspected; first public date May 11, 2015).
3. J. A. Adell, P. Garrancho and F. J. Martínez-Sánchez (2024), *Approximation of discontinuous functions by positive linear operators. A probabilistic approach*, https://arxiv.org/abs/2410.19893 (preprint, full Section 5 and related statements inspected).
4. H. Gonska and X. Zhou (1995), *On an Extremal Problem Concerning Bernstein Operators*, Serdica Math. J. **21**, 137–150, https://www.math.bas.bg/serdica/1995/1995-137-150.pdf (full text inspected).
