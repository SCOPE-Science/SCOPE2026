# A unique optimal geometric radius for the expected friendship paradox, with two boundary limits

## Finding

For independent uniform points on the \(m\)-dimensional unit torus, connect two points when their maximum circular-coordinate distance is smaller than \(r\in(0,1/2)\). Let \(F_{n,m}(r)\) be the expected *vertex-averaged friendship bias* (defined below). For **each integer \(n\geq3\) and \(m\geq1\)** there is exactly one radius \(r_{n,m}\) maximizing \(F_{n,m}\), and
\[
\frac13<r_{n,m}<\frac12.
\]
The function is strictly increasing before and strictly decreasing after this radius. For every fixed dimension \(m\), the optimum is strictly decreasing in the number of sampled vertices:
\[
r_{n+1,m}<r_{n,m},\qquad \lim_{n\to\infty}r_{n,m}=\frac13.
\]
Moreover, writing \(N=n-1\), \(p_m=(2/3)^m\), and \(\kappa_m=1-(3/4)^m\), its exponentially small displacement is sharp:
\[
r_{n,m}-\frac13\sim
\frac{2\kappa_m}{27(3/4)^{m-1}}
 N(N-1)p_m^2(1-p_m)^{N-2}
\quad(n\to\infty,\ m\text{ fixed}).
\]
In contrast, for each fixed \(n\ge3\), letting \(m\to\infty\), there is a unique \(t_n\in(0,1)\) satisfying
\[
(1-t_n)B_N'(t_n)=B_N(t_n),\qquad
B_N(t)=1-(1-t)^N-Nt(1-t)^{N-1},
\]
and
\[
m\bigl(\tfrac12-r_{n,m}\bigr)\longrightarrow
c_n=-\tfrac12\log t_n>0,\qquad
\max_{0<r<1/2}F_{n,m}(r)\longrightarrow(1-t_n)B_N(t_n).
\]
Thus the two large-parameter limits select *different radius boundaries*: one third for many vertices at fixed dimension, one half for large dimension at fixed vertex count. For example, \(r_{3,1}=3/8\), \(F_{3,1}(3/8)=1/8\), and \(t_3=2/3\).

## Assumptions and scope

Let \(n\ge3\) and \(m\ge1\) be integers. Let \(X_1,\ldots,X_n\) be independent, Haar-uniform on \(\mathbb T^m=(\mathbb R/\mathbb Z)^m\). Let \(A_{ij}=\mathbf1\{d_\infty(X_i,X_j)<r\}\) for \(i\neq j\), \(d_i=\sum_{j\neq i}A_{ij}\), and \(\Delta_i=d_i^{-1}\sum_j A_{ij}d_j-d_i\) when \(d_i>0\), with \(\Delta_i=0\) for \(d_i=0\). Define
\[
F_{n,m}(r)=\mathbb E\left[\frac1n\sum_{i=1}^n\Delta_i\right],\qquad 0<r<\frac12.
\]
There are no large-size assumptions in the finite-parameter uniqueness and strict-ordering statements. Equalities on the geometric distance boundary occur with probability zero. The expected gap is not a typical-vertex or edge-sampled friendship bias, and the theorem concerns its **annealed expectation**, not the random maximizer of a single graph realization.

## Proof

**Step 1: exact mean and the two competing factors.** The exact finite-sample identity, established in Yuan [1, Theorem 1], is
\[
F_{n,m}(r)=[1-\rho(r)^m]B_N(p(r)),\qquad p(r)=(2r)^m,
\]
where
\[
\rho(r)=\begin{cases}
3/4,&0<r\le1/3,\\
(12r^2-6r+1)/(4r^2),&1/3<r<1/2.
\end{cases}
\]
This premise is **prior work**; the radius optimizer and its asymptotics below are not claimed to be the discovery of the factorization. Here \(B_N(p)=\Pr(\operatorname{Bin}(N,p)\ge2)\). The factor \(B_N\) increases with connection probability while the factor \(1-\rho^m\) falls for \(r>1/3\): this is the precise competition to be optimized. The two factors are continuous and positive on the open interval. Since \(B_N(p)\sim\binom N2 p^2\) near \(p=0\), and \(\rho(r)\to1\) as \(r\uparrow1/2\), the expected bias vanishes at both endpoints.

**Step 2: a decreasing elasticity versus increasing geometric penalty.** For \(p\in(0,1)\), direct differentiation gives
\[
B_N'(p)=N(N-1)p(1-p)^{N-2}.
\]
Put \(E_N(p)=pB_N'(p)/B_N(p)\). Dividing the binomial tail by \(p^2(1-p)^{N-2}\) yields the exact identity
\[
E_N(p)=\frac{N(N-1)}{\displaystyle\sum_{k=2}^N\binom Nk(p/(1-p))^{k-2}}.
\]
All denominator coefficients are positive. Hence \(E_N(p)\) is positive and nonincreasing in \(p\), strictly decreasing if \(N\ge3\); \(E_2\equiv2\).

For \(r\in(1/3,1/2)\), define
\[
H_m(r)=\frac{r\rho(r)^{m-1}\rho'(r)}{1-\rho(r)^m},
\qquad \rho'(r)=\frac{3r-1}{2r^3}.
\]
The function \(r\rho'(r)=(3r-1)/(2r^2)\) increases strictly because its derivative is \((2-3r)/(2r^3)>0\). The additional factors \(\rho^{m-1}\) and \((1-\rho^m)^{-1}\) are nondecreasing and positive. Thus \(H_m\) increases strictly, with \(H_m(1/3+)=0\) and \(H_m(1/2-)=+\infty\). Differentiating the two factors gives the *exact derivative-sign equivalence*
\[
\operatorname{sgn}F'_{n,m}(r)=
\operatorname{sgn}\left(E_N((2r)^m)-H_m(r)\right),\qquad 1/3<r<1/2.
\]
The right side is strictly decreasing from a positive value to a negative value, so it vanishes exactly once, changing sign from positive to negative. On \((0,1/3]\), \(\rho\equiv3/4\), and \(B_N((2r)^m)\) strictly increases. The root is therefore the unique global maximizer on \((0,1/2)\), with the claimed strict monotonicity on both sides.

**Step 3: strict decrease with vertex count.** For \(z=p/(1-p)>0\), the same elasticity can be rewritten as
\[
\frac1{E_N(p)}=
\sum_{j=0}^{N-2}\frac{\binom{N-2}{j}}{(j+1)(j+2)}z^j.
\]
For \(N\ge2\), increasing \(N\) strictly raises this sum (because the \(j=1\) coefficient rises), so \(E_{N+1}(p)<E_N(p)\). With \(H_m\) independent of \(N\), the unique crossing shifts strictly left, proving \(r_{n+1,m}<r_{n,m}\).

**Step 4: fixed dimension, large vertex count.** Fix \(m\). For every fixed \(p\in(0,1)\), \(B_N(p)\to1\) and
\[
E_N(p)=\frac{N(N-1)p^2(1-p)^{N-2}}{B_N(p)}\longrightarrow0.
\]
Consequently, for any \(\varepsilon>0\), the unique root eventually lies below \(1/3+\varepsilon\); hence it converges to \(1/3\). Let \(\delta_N=r_{n,m}-1/3\) and \(p_m=(2/3)^m\). The right derivative of \(\rho\) vanishes at \(1/3\), whereas \(\rho''(1/3+)=81/2\). Therefore
\[
H_m(1/3+\delta)=
\frac{27(3/4)^{m-1}}{2\kappa_m}\delta+O_m(\delta^2).
\]
Since \(E_N\) is nonincreasing and \(p(r_{n,m})\ge p_m\), the root equation bounds \(\delta_N=O_m(E_N(p_m))\), an exponentially small quantity. In particular \(N\delta_N\to0\); the explicit formula for \(E_N\) implies
\[
\frac{E_N(p(1/3+\delta_N))}{E_N(p_m)}\longrightarrow1.
\]
Substituting into the root equation, using \(B_N(p_m)\to1\), proves the sharp equivalent in the Finding section.

**Step 5: fixed vertex count, high dimension.** Fix \(N\ge2\), and introduce a boundary-layer variable \(c=m(1/2-r)\). For each fixed \(c>0\), put \(r_m(c)=1/2-c/m\). Direct expansion at \(1/2\) yields
\[
(2r_m(c))^m\to e^{-2c},\qquad
\rho(r_m(c))^m\to e^{-2c},
\]
so
\[
F_{n,m}(r_m(c))\longrightarrow
G_N(c)=(1-e^{-2c})B_N(e^{-2c}).
\]
The limit is positive somewhere and tends to zero as \(c\downarrow0\) or \(c\uparrow\infty\). This convergence is locally uniform on \((0,\infty)\). To rule out maximizers escaping, note that \(F_{n,m}(r)\le B_N((2r)^m)\le\binom N2(2r)^{2m}\le\binom N2e^{-4c}\), so \(c\to\infty\) gives zero uniformly. For \(c\to0\), boundedness of \(\rho'\) near \(1/2\) gives \(1-\rho(r)^m\le m(1-\rho(r))\le Cc\), again forcing zero. The maximizers therefore have \(c\) bounded above and below away from zero and all their limit points maximize \(G_N\).

With \(t=e^{-2c}\in(0,1)\), the stationarity equation for \((1-t)B_N(t)\) is \((1-t)B_N'(t)=B_N(t)\). Equivalently, \(((1-t)/t)E_N(t)=1\). Its left side is strictly decreasing in \(t\), tends to infinity at zero and zero at one. Hence the solution \(t_n\) is unique, and all maximizer subsequences converge to \(c_n=-\frac12\log t_n\). This also proves convergence of the maximal values.

**Step 6: explicit check at three vertices.** For \(n=3,m=1\), \(B_2(p)=p^2\), and on \(1/3<r<1/2\),
\[
F_{3,1}(r)=-8r^2+6r-1,
\]
with maximum \(1/8\) at \(r=3/8\). In the high-dimensional limit at \(n=3\), the equation \(2t(1-t)=t^2\) gives \(t_3=2/3\), so \(c_3=\frac12\log(3/2)\).

## Verification

The included standalone `check.py` uses only the Python standard library. Executing `python check.py` from the extracted package checked 563 finite algebraic and numerical assertions, including exact rational identities for binomial tails, derivative-sign and monotonicity probes across dimensions and graph sizes, and sample parameter-limit comparisons. It prints the exact three-vertex benchmark and representative numerical optimizers. These tests are finite diagnostics; Steps 1–6 above supply the proof for all stated parameter values. No simulation or exhaustive finite enumeration is used to infer the infinite statements.

## Relationship to prior work

Yuan [1, Theorem 1] establishes the **exact mean function** and its piecewise geometric overlap factor, which this result takes as its explicit starting point. The new mathematical claim is the all-size uniqueness and ordering of its maximizing radius, its sharp fixed-dimensional displacement, and its distinct high-dimensional boundary-layer optimizer and value. The fixed-size radius-design problem is not a limit-law or variance question answered by that theorem. Yuan [2] treats the one-dimensional shrinking-radius weak law and does not imply optimization on \((1/3,1/2)\), much less the high-dimensional limit. Published results on geometric graph edge counts and deterministic-network friendship correlations also concern different observables. This is a literature-relative novelty assessment, not a proof of global historical priority.

## Limitations

The result optimizes **expected** bias, not the realized statistic or its variance, nor any graph's detection or epidemiological performance. The torus must have independent uniform points, max-norm connection and integer dimension; Euclidean-ball graphs, other kernels, inhomogeneous sampling and random numbers of vertices are not included. The fixed-\(m\) and fixed-\(n\) limits are separate; no uniform joint \(n,m\) limit is claimed. Historical priority remains open to further independent review, particularly of secondary descriptions and older literature on radius tuning.

## References

1. Mingao Yuan, *Limit laws for the friendship paradox in random geometric graphs*, arXiv:2611.09765v1 (submitted 6 November 2026), especially Theorem 1 and Sections 2.2 and 4, https://arxiv.org/html/2611.09765v1.
2. Mingao Yuan, *The weak law of large numbers for the friendship paradox index*, arXiv:2602.10055v1 (submitted 10 February 2026), https://arxiv.org/html/2602.10055v1.
3. M. Yuan, *Asymptotic distribution of the friendship paradox of a random geometric graph*, Brazilian Journal of Probability and Statistics (2024). Only an abstract and bibliographic information were accessible for this priority comparison; the complete article was not checked.
