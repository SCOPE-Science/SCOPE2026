# Sharp logarithmic optimizer offsets and Pareto losses for high-redundancy exponential Gabor frames

## Finding

Let \(g(t)=e^{-|t|}\), normalized to have unit \(L^2(\mathbb R)\)-norm, and consider the rectangular Gabor system with time step \(a=\eta/n\) and frequency step \(b=1/\eta\), where \(n\ge2\) is an integer and \(\eta>0\). Write \(A_n(\eta)\) and \(B_n(\eta)\) for its *sharp frame bounds divided by the redundancy* \(n=(ab)^{-1}\), and \(K_n(\eta)=B_n(\eta)/A_n(\eta)\). Let \(\eta_{A,n}\) maximize \(A_n\), let \(\eta_{B,n}\) minimize \(B_n\), and let \(\eta_{K,n}\) minimize \(K_n\). Existence and uniqueness of these three parameters are established in the work cited below. The following sharp high-redundancy conclusions hold:

\[
\begin{aligned}
\eta_{A,n}&=2\log n+\log 6+O((\log n)^2/n^2),\\
\eta_{B,n}&=2\log n+\log 3+O((\log n)^2/n^2),\\
\eta_{K,n}&=2\log n+\log 4+O((\log n)^2/n^2).
\end{aligned}
\]

In particular, the three optimal lattice geometries retain universal nonzero additive separations:
\[
\eta_{K,n}-\eta_{B,n}\longrightarrow\log(4/3),\qquad
\eta_{A,n}-\eta_{K,n}\longrightarrow\log(3/2).
\]

The separation has an exact quantitative performance cost. Define
\[
J_A(s)=\frac23s+4e^{-s},\qquad
J_B(s)=\frac43s+4e^{-s},\qquad
J_K(s)=2s+8e^{-s}.
\]
For every real \(s\), with convergence uniform on compact sets of \(s\),
\[
\begin{aligned}
\lim_{n\to\infty}\frac{n^2}{\log n}\bigl[A_n(\eta_{A,n})-A_n(2\log n+s)\bigr]
&=J_A(s)-J_A(\log6),\\
\lim_{n\to\infty}\frac{n^2}{\log n}\bigl[B_n(2\log n+s)-B_n(\eta_{B,n})\bigr]
&=J_B(s)-J_B(\log3),\\
\lim_{n\to\infty}\frac{n^2}{\log n}\bigl[K_n(2\log n+s)-K_n(\eta_{K,n})\bigr]
&=J_K(s)-J_K(\log4).
\end{aligned}
\]
Each limiting loss is nonnegative and has exactly one zero. At the condition-number-optimal lattice, the unavoidable deficits relative to individually optimizing the lower and upper frame bounds are, respectively,
\[
\boxed{\lim_{n\to\infty}\frac{n^2}{\log n}
\bigl[A_n(\eta_{A,n})-A_n(\eta_{K,n})\bigr]
=\frac13+\frac23\log\frac23>0}
\]
and
\[
\boxed{\lim_{n\to\infty}\frac{n^2}{\log n}
\bigl[B_n(\eta_{K,n})-B_n(\eta_{B,n})\bigr]
=\frac43\log\frac43-\frac13>0.}
\]
Thus choosing the best condition number has a sharp, strictly positive second-scale cost for both individual spectral bounds. This is a limit theorem, not a claim that the errors have the displayed asymptotic values for finite \(n\).

## Assumptions and scope

We use the convention \(M_\omega T_xg(t)=e^{2\pi i\omega t}g(t-x)\), and sum squared analysis coefficients over all \((x,\omega)\in a\mathbb Z\times b\mathbb Z\). With the stated normalized window, the physical sharp bounds are \(n A_n\) and \(n B_n\); the normalization removes a common redundancy factor and leaves all three optimal lattice parameters unchanged. All logarithms are natural. All limits concern integer \(n\to\infty\), with \(g\) fixed, and with the product \(ab=1/n\). No assumption is made on how quickly a chosen compact-range \(s\) varies with \(n\). The results do not concern general nonrectangular lattices, other windows, or noninteger redundancy.

The exact normalized bound formulas, in the notation above, are
\[
\begin{aligned}
A_n(\eta)&=\tanh(\eta/2)\left[\frac{\eta}{n}\operatorname{csch}\!\left(\frac{\eta}{n}\right)-\eta\operatorname{csch}(\eta)\right],\\
B_n(\eta)&=\coth(\eta/2)\left[\frac{\eta}{n}\coth\!\left(\frac{\eta}{n}\right)+\eta\operatorname{csch}(\eta)\right].
\end{aligned}
\]
They follow from the known integer-density Zak-fiber calculation. One direct way to check the normalization is the Walnut-series multiplier, which has the form
\[
\frac{\eta}{n}\sum_{k,\ell\in\mathbb Z}
 e^{-|t-ka|-|t-ka-\ell\eta|}e^{2\pi i\ell\omega},
\qquad 0\le t<a,\quad 0\le\omega<1.
\]
Its maximum at \((t,\omega)=(0,0)\) is \(B_n(\eta)\); its minimum at \((a/2,1/2)\) is \(A_n(\eta)\). The sharp-bound formulas and uniqueness of their lattice optimizers are **inputs** from Faulhuber–Shafkulovska (2022/2023), not new results here.

## Proof

Put \(L=\log n\), \(h=\eta\), \(u=h/n\), and \(v=e^{-h}\). On every fixed strip \(h=2L+s\), \(|s|\le C\), we have \(u=O_C(L/n)\) and \(v=n^{-2}e^{-s}\). Taylor expansions at the origin and exact hyperbolic identities give
\[
\begin{aligned}
u\operatorname{csch}(u)&=1-u^2/6+O(u^4),\\
u\coth(u)&=1+u^2/3+O(u^4),\\
\tanh(h/2)&=1-2v+O(v^2),\\
\coth(h/2)&=1+2v+O(v^2),\\
h\operatorname{csch}(h)&=2hv+O(hv^3).
\end{aligned}
\]
The remainders and their first two derivatives obey uniform bounds on each such strip, since all functions are analytic in the relevant neighborhoods and \(h\) tends to infinity. Substitution into the exact sharp-bound formulas yields the *differentiable* expansions
\[
\begin{aligned}
A_n(h)&=1-\frac{h^2}{6n^2}-2(1+h)e^{-h}+O_C(h^4/n^4),\\
B_n(h)&=1+\frac{h^2}{3n^2}+2(1+h)e^{-h}+O_C(h^4/n^4),\\
K_n(h)&=1+\frac{h^2}{2n^2}+4(1+h)e^{-h}+O_C(h^4/n^4).
\end{aligned}
\]
The derivative of each remainder is \(O_C(h^3/n^4)\), and the second derivative is also \(O_C(h^3/n^4)\). For the quotient \(K_n=B_n/A_n\), this follows because \(A_n=1+O_C(L^2/n^2)\). Differentiating gives
\[
\begin{aligned}
A_n'(h)&=\frac{h}{n^2}\left(-\frac13+2n^2e^{-h}\right)+O_C(h^3/n^4),\\
B_n'(h)&=\frac{h}{n^2}\left(\frac23-2n^2e^{-h}\right)+O_C(h^3/n^4),\\
K_n'(h)&=\frac{h}{n^2}\left(1-4n^2e^{-h}\right)+O_C(h^3/n^4).
\end{aligned}
\]
The leading brackets vanish at \(h_{A,0}=2L+\log6\), \(h_{B,0}=2L+\log3\), and \(h_{K,0}=2L+\log4\), respectively. For a sufficiently large fixed \(C\), the derivatives have the maximizing/minimizing signs at the endpoints \(h_{i,0}\pm1\) for all sufficiently large \(n\).

To pass from these local signs to the *global* optimizer, we use the established global uniqueness and localization from Faulhuber–Shafkulovska: for all sufficiently large \(n\) all three optimizers lie in \(I_n=(\operatorname{arccosh}n,4\operatorname{arccosh}n)\); \(\log A_n\) is strictly concave there, \(B_n\) is strictly convex on \((0,\infty)\), and \(\log K_n\) is strictly convex on \(I_n\). Both endpoints \(h_{i,0}\pm1\) belong to \(I_n\) for large \(n\). Thus the sign changes bracket the respective unique global optimizers, so \(\eta_{i,n}=2L+O(1)\). At the leading root, the derivative remainder is \(O(L^3/n^4)\); the respective second derivatives have nonzero signs with magnitudes asymptotic to \(h/(3n^2)\), \(2h/(3n^2)\), and \(h/n^2\). The mean value theorem therefore improves the bracketing to
\[
\eta_{i,n}-h_{i,0}=O(L^2/n^2)
\]
for each of the three objectives. This proves the universal optimizer offsets and separations.

For the normalized asymptotic losses substitute \(h=2L+s\) in the three differentiable expansions. Uniformly for bounded \(s\),
\[
\begin{aligned}
n^2(1-A_n(2L+s))&=\frac23L^2+LJ_A(s)+O_C(1),\\
n^2(B_n(2L+s)-1)&=\frac43L^2+LJ_B(s)+O_C(1),\\
n^2(K_n(2L+s)-1)&=2L^2+LJ_K(s)+O_C(1).
\end{aligned}
\]
The \(O_C(1)\) errors come from bounded explicit terms \(s^2/6+2(1+s)e^{-s}\), \(s^2/3+2(1+s)e^{-s}\), and \(s^2/2+4(1+s)e^{-s}\) plus terms tending to zero. The derivative formulas establish \(J_A''(s)=4e^{-s}>0\), \(J_B''(s)=4e^{-s}>0\), and \(J_K''(s)=8e^{-s}>0\); their unique minimizers are \(\log6\), \(\log3\), and \(\log4\). Replacing these locations by the actual optimal \(s\)-parameters changes the displayed normalized expressions by \(o(L)\), by the optimizer estimates and uniformity. Subtracting and dividing by \(L\) proves all three limiting loss profiles.

Finally take \(s=\log4\) in the first two loss limits. Algebra gives the stated coefficients, and their strict positivity follows from strict convexity and \(\log4\ne\log6,\log3\). This completes the proof.

## Verification

The accompanying `check_gabor.py` uses high-precision numerical differentiation to locate each optimizer and tests the predicted error rate across five redundancies. It also reconstructs the two extremizing Zak multipliers directly from the doubly infinite Walnut sum using finite truncation in four examples, checks all three high-density expansions and both Pareto-loss coefficients, and reports `GABOR_HIGH_DENSITY_CHECKS_PASS 76` on successful completion. The analytic argument above, not this finite test, proves the limits. The source's sharp-bound equations and optimizer uniqueness are expressly identified as external premises.

Reproduction: with Python 3 and the `mpmath` package installed, run `python check_gabor.py` beside this document. No web access is required.

## Relationship to prior work

Faulhuber and Shafkulovska, *Gabor frame bound optimizations*, arXiv:2204.02917 (first public version 2022-04-06; revised 2023), Section 8, provide the exact frame-bound functions, the existence and uniqueness of three different lattice optimizers, inequalities locating them around \(2\operatorname{arccosh}(n)\), and precise finite-redundancy properties. Those results are not claimed as new. The present theorem supplies a distinct *sharp high-density limiting landscape*: the three universal logarithmic offsets, their exact nonvanishing separations, uniform scaled loss functions and two positive regret constants, none of which are stated in the inspected Section 8.

Kloos and Stöckler, *Zak transforms and Gabor frames of totally positive functions and exponential B-splines*, arXiv:1311.7359 (2013), analyze the same two-sided exponential class but emphasize frame-set properties and lower frame bounds as density tends toward the critical value rather than integer redundancy tending to infinity. Faulhuber and Steinerberger, *Optimal Gabor frame bounds for separable lattices and estimates for Jacobi theta functions*, arXiv:1601.02972 (2016), treat Gaussian rather than exponential windows. Their results do not imply the stated constants without a new analysis of the exponential sharp-bound formulas. The unsearched wider historical literature may contain an equivalent high-redundancy asymptotic under different notation; priority remains provisional.

## Limitations

The theorem relies on previously established sharp-bound formulas and uniqueness/local-convexity results; it does not reprove them. It applies only to integer redundancy and rectangular lattices with the fixed normalized two-sided exponential. The \(O\)-estimates are asymptotic, with no explicit uniform threshold in \(n\); the limiting regret formulas are uniform only for bounded additive offsets \(s\), not for arbitrary unbounded lattice deformations. The numerical reproduction checks cannot rule out competing formulations in the literature. No claim of independence or external certification is made.

## References

1. M. Faulhuber and I. Shafkulovska, *Gabor frame bound optimizations*, arXiv:2204.02917, first version 2022-04-06, revised version 2023-07-27, Section 8. https://arxiv.org/html/2204.02917v2
2. T. Kloos and J. Stöckler, *Zak transforms and Gabor frames of totally positive functions and exponential B-splines*, arXiv:1311.7359, 2013, Sections 4–5. https://arxiv.org/abs/1311.7359
3. M. Faulhuber and S. Steinerberger, *Optimal Gabor frame bounds for separable lattices and estimates for Jacobi theta functions*, arXiv:1601.02972, 2016. https://arxiv.org/abs/1601.02972
