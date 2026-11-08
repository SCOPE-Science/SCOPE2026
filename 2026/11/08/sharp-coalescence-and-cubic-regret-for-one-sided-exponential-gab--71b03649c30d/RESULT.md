# Sharp coalescence and cubic regret for one-sided exponential Gabor lattices

## Finding

For each integer \(n\ge2\) and every fixed \(\gamma>0\), consider the normalized one-sided exponential window
\[
g_\gamma(t)=\sqrt{2\gamma}\,e^{-\gamma t}\mathbf1_{(0,\infty)}(t)
\]
and the rectangular Gabor lattice \(a\mathbb Z\times b\mathbb Z\) with \(a=\eta/(\gamma n)\), \(b=\gamma/\eta\) and \(\eta>0\). Let \(A_n(\eta)\) and \(B_n(\eta)\) be its sharp lower and upper frame bounds, and \(\kappa_n(\eta)=B_n(\eta)/A_n(\eta)\). Write \(\eta_{A,n}\), \(\eta_{B,n}\), \(\eta_{\kappa,n}\) for the unique maximizer of \(A_n\), minimizer of \(B_n\), and minimizer of \(\kappa_n\), respectively. Their existence and uniqueness are known from the cited Gabor-frame theorem.

Set \(L_n=\log(2n)\). As \(n\to\infty\) through integers,
\[
\eta_{A,n}=L_n-\frac{L_n}{3n}+O\!\left(\frac{L_n^2}{n^2}\right),\qquad
\eta_{\kappa,n}=\operatorname{arsinh}(n)=L_n+O(n^{-2}),\qquad
\eta_{B,n}=L_n+\frac{L_n}{3n}+O\!\left(\frac{L_n^2}{n^2}\right).
\]
In particular, \(\eta_{B,n}-\eta_{A,n}\sim 2L_n/(3n)\) and the corresponding optimal time steps satisfy \(a_{B,n}/a_{A,n}=1+2/(3n)+o(n^{-1})\). The two relative Pareto regrets incurred by using the condition-number-optimal lattice have the same sharp equivalent:
\[
\frac{A_n(\eta_{A,n})-A_n(\eta_{\kappa,n})}{A_n(\eta_{A,n})}
\sim
\frac{B_n(\eta_{\kappa,n})-B_n(\eta_{B,n})}{B_n(\eta_{B,n})}
\sim\frac{L_n^2}{18n^3}.
\]
These are relative losses and therefore do not depend on a common normalization factor in the frame bounds.

## Assumptions and scope

The sharp frame bounds are defined for all \(f\in L^2(\mathbb R)\) by
\[
A_n(\eta)\lVert f\rVert_2^2\le
\sum_{k,\ell\in\mathbb Z}|\langle f,M_{\ell b}T_{ka}g_\gamma\rangle|^2
\le B_n(\eta)\lVert f\rVert_2^2.
\]
All optimizers are over the entire positive aspect parameter \(\eta\), at fixed integer redundancy \(1/(ab)=n\); \(\gamma\) is any fixed positive number. The claimed limits are for \(n\to\infty\), not claims about finite-order equality or a nonintegral redundancy parameter. The mathematical input from the primary source is the exact sharp frame-bound dependence on \(\eta\), together with existence and uniqueness of the three optimizers. The asymptotic locations and regrets are derived below.

## Proof

**1. Exact starting formulas and critical equations.** By dilation it suffices to take \(\gamma=1\). In the cited primary source, the sharp frame bounds have a common positive factor independent of \(\eta\); after dividing by that factor, the two objective functions are
\[
F_n^-(t)=e^{-t/n}\tanh(t/2)\frac{t/n}{\sinh(t/n)},\qquad
F_n^+(t)=e^{t/n}\coth(t/2)\frac{t/n}{\sinh(t/n)}.
\]
In particular, maximizing \(F_n^-\), minimizing \(F_n^+\), and minimizing \(F_n^+/F_n^-\) give exactly the three desired parameters. Differentiating yields the necessary equations for the lower- and upper-bound extrema, respectively,
\[
1+t\operatorname{csch}t=\frac tn+\frac tn\coth(t/n),\tag{1}
\]
\[
1+\frac tn-\frac tn\coth(t/n)-t\operatorname{csch}t=0.\tag{2}
\]
The condition number simplifies to \(\kappa_n(t)=e^{2t/n}\coth^2(t/2)\), whose unique minimum satisfies \(\sinh t=n\). The cited theorem establishes uniqueness of the other two global optima for every positive integer redundancy.

**2. Localization and first correction.** Put \(L=\log(2n)\), \(t=L+\delta\), and \(x=t/n\). Uniformly for \(|\delta|\le 2L/n\), elementary convergent expansions give
\[
t\operatorname{csch}t=\frac tn e^{-\delta}+O\!\left(\frac{t}{n^3}\right),\qquad
x\coth x=1+\frac{x^2}{3}+O(x^4).
\]
After dividing equation (1) by \(t/n>0\), its residual is
\[
e^{-\delta}-1-\frac{t}{3n}+O\!\left(n^{-2}+\frac{L^3}{n^3}\right).
\]
The residual has opposite signs at \(\delta=-2L/n\) and \(\delta=+2L/n\) for all sufficiently large \(n\). The already-known unique root therefore lies in this interval. Substituting \(\delta=O(L/n)\) and expanding the exponential gives
\[
\delta_{A,n}=-\frac{L}{3n}+O\!\left(\frac{L^2}{n^2}\right).
\]
Similarly, equation (2) divided by \(t/n\) reads
\[
1-e^{-\delta}-\frac{t}{3n}+O\!\left(n^{-2}+\frac{L^3}{n^3}\right)=0,
\]
so the unique root is
\[
\delta_{B,n}=\frac{L}{3n}+O\!\left(\frac{L^2}{n^2}\right).
\]
The exact condition-number root is \(\operatorname{arsinh}n=\log(n+\sqrt{n^2+1})=L+O(n^{-2})\). These establish the three location formulas and the time-step ratio.

**3. Sharp relative regret.** Write \(z=e^{-t}\). Uniformly when \(|t-L|\le 2L/n\), Taylor expansion of the exact formulas yields
\[
F_n^-(t)=1-\frac tn+\frac{t^2}{3n^2}-2z+2\frac tn z+2z^2+R_n^-(t),
\]
\[
F_n^+(t)=1+\frac tn+\frac{t^2}{3n^2}+2z+2\frac tn z+2z^2+R_n^+(t),
\]
where the second derivatives of both remainders are \(O(L/n^3+L^2/n^3)\) on this interval (a weaker \(o(n^{-1})\) bound would suffice). Consequently,
\[
(F_n^-)''(t)=-n^{-1}+O(L/n^2),\qquad
(F_n^+)''(t)=n^{-1}+O(L/n^2)
\]
uniformly there. Taylor's theorem at the respective stationary extrema and the location differences already proved give
\[
F_n^-(\eta_{A,n})-F_n^-(\eta_{\kappa,n})
=\frac{L^2}{18n^3}(1+o(1)),
\]
\[
F_n^+(\eta_{\kappa,n})-F_n^+(\eta_{B,n})
=\frac{L^2}{18n^3}(1+o(1)).
\]
Since \(F_n^\pm(\eta_{\cdot,n})\to1\), division by the corresponding optimal value does not change these equivalents. The common frame-bound normalization factor cancels. Dilation restores every \(\gamma>0\).

## Verification

The accompanying `check_one_sided.py` evaluates the exact critical equations by bracketing and bisection and calculates the two normalized regrets directly, using only the Python standard library. At redundancies \(n=20,100,500,1000\), both scaled optimizer gaps approach \(1/3\) and both scaled regret ratios approach \(1\). The code does not replace the analytic expansions, the global uniqueness theorem, or the infinite-order proof. Run `python3 check_one_sided.py` from the directory containing this file.

## Relationship to prior work

Faulhuber and Shafkulovska (2022 preprint; 2023 journal) derive the exact one-sided-exponential frame bounds and prove uniqueness and strict ordering of the three optimizers; their source gives \(\eta_{\kappa,n}=\operatorname{arsinh}n\) exactly. The present result resolves a different, previously unstated quantitative question: the sharp rate at which the two other global optima approach the condition-number optimizer, and the precise relative losses of using a single lattice for both performance objectives. Janssen's earlier frame-bound calculations underlie the source formulas, and an unexamined earlier equivalent asymptotic analysis remains possible.

The two-sided exponential window, treated separately in the same primary paper, has a different large-density optimizer scale; no transfer of an optimizer separation or regret formula from that window to the one-sided window is invoked here. The exact formulas are acknowledged as the published starting point, not presented as new.

## Limitations

No claim is made that the primary source's frame-bound formulas or optimizer uniqueness are new. The new conclusions depend on those known formulas. All asymptotic constants concern positive integer redundancy and rectangular lattices. The result gives leading sharp asymptotic regret, not an exact finite-order regret formula or optimality over nonrectangular sampling sets. Bibliographic completeness is not guaranteed: the full 1996 frame-bound article was not materially inspected, and an older asymptotic treatment could exist. Numerical checks are finite corroboration only.

## References

1. M. Faulhuber and I. Shafkulovska, *Gabor frame bound optimizations*, arXiv:2204.02917, first posted 2022-04-06; Applied and Computational Harmonic Analysis 67 (2023), 101574. Sections 2.3 and 7, especially Theorem 2.6 and equations (7.2)–(7.11). https://arxiv.org/html/2204.02917v2
2. A. J. E. M. Janssen, *Some Weyl-Heisenberg frame bound calculations*, Indagationes Mathematicae 7 (1996), 165–183, DOI 10.1016/0019-3577(96)85088-9 (bibliographic record and abstract checked; full text not inspected).
3. M. Faulhuber and S. Steinerberger, *Optimal Gabor frame bounds for separable lattices and estimates for Jacobi theta functions*, arXiv:1601.02972 (Gaussian window, distinct from the one-sided exponential).
