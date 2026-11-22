# Rare endpoint witnesses for random interval covering

## Finding
Let \(n\ge1\) and let \(X_1,\ldots,X_n\) be independent uniform points on \([0,1]\). Define the *covering radius* and the event of a boundary witness by
\[
R_n=\max_{x\in[0,1]}\min_{1\le i\le n}|x-X_i|,
\qquad B_n=\{\text{the maximizing location is }0\text{ or }1\}.
\]
The maximum is unique almost surely. The boundary-witness probability is exactly
\[
\boxed{\Pr(B_n)=B(1/2,n)-\frac1n
=\frac{4^n n!(n-1)!}{(2n)!}-\frac1n.}
\]
Here \(B(a,b)=\int_0^1 t^{a-1}(1-t)^{b-1}\,dt\). In particular,
\[
\Pr(B_n)=\frac{\sqrt\pi}{\sqrt n}-\frac1n+O(n^{-3/2}).
\]
Conditionally on \(B_n\), the centered and rescaled covering radius has the distributional limit
\[
\boxed{\Pr(2nR_n-\log n\le y\mid B_n)
\longrightarrow\operatorname{erfc}(e^{-y/2}),\quad y\in\mathbb R,}
\]
where \(\operatorname{erfc}(z)=(2/\sqrt\pi)\int_z^\infty e^{-v^2}\,dv\). The left/right endpoint that witnesses \(B_n\) is a fair coin, independent of \(R_n\) conditional on \(B_n\), for every \(n\ge1\).

The conditional limiting law is different from the classical (unconditional) standard Gumbel law for \(2nR_n-\log n\): an atypically large endpoint gap produces a distinct rare-event profile.

## Assumptions and scope
The sample is iid exactly uniform on a fixed real interval, normalized to \([0,1]\). There are no atoms or repeated points almost surely. The result includes \(n=1\), when \(B_1\) is certain. The conditional limit concerns the full-interval Euclidean covering radius, **not** the longest unweighted spacing, circle coverage, nonuniform sampling, or higher dimensions. The error term is for integer \(n\to\infty\).

## Proof
Write the ordered sample as \(0<X_{(1)}<\cdots<X_{(n)}<1\), with \(n+1\) spacings
\[
D_0=X_{(1)},\quad D_i=X_{(i+1)}-X_{(i)}\ (1\le i<n),
\quad D_n=1-X_{(n)}.
\]
The full interval is covered by the radius \(r\) balls exactly when the two endpoint gaps are at most \(r\) and all interior gaps at most \(2r\). Therefore
\[
R_n=\max\{D_0,D_n,\tfrac12\max_{1\le i<n}D_i\}.
\]
For \(n=1\) the interior maximum is omitted. Continuous spacing density implies all competing maxima are distinct almost surely.

Use the uniform-spacing exponential representation: take independent rate-one exponentials \(E_0,\ldots,E_n\), set \(S=\sum_{i=0}^n E_i\), and take \((D_0,\ldots,D_n)=(E_0/S,\ldots,E_n/S)\) in distribution. Put \(Z=\max(E_0,E_n)\) and \(W=\max_{1\le i<n}E_i\) (with \(W=0\) for \(n=1\)). Then \(B_n=\{W<2Z\}\) and \(R_n=Z/S\) on \(B_n\). The variables \(Z,W\) are independent, with
\[
f_Z(z)=2e^{-z}(1-e^{-z}),\quad
\Pr(W<z)=(1-e^{-z})^{n-1},\quad z>0.
\]
Thus the substitution \(u=e^{-z}\) gives
\[
\Pr(B_n)=2\int_0^\infty e^{-z}(1-e^{-z})(1-e^{-2z})^{n-1}\,dz
=2\int_0^1(1-u)(1-u^2)^{n-1}\,du
=B(1/2,n)-B(1,n).
\]
Using the half-integer Gamma identity yields the displayed factorial formula. The Gamma ratio \(\Gamma(n)/\Gamma(n+1/2)=n^{-1/2}(1+O(n^{-1}))\) gives the stated two leading asymptotic terms.

To establish the conditional limit rather than merely a marginal probability, define the exponential-spacing auxiliary variable \(T_n=ne^{-2Z}\). Changing variables in the joint density of \(Z\) and \(B_n\) gives the following exact *unnormalized* density on \(0<t<n\):
\[
\frac{\Pr(T_n\in dt,B_n)}{dt}=
\frac{1}{\sqrt{nt}}\left(1-\sqrt{\frac tn}\right)
\left(1-\frac tn\right)^{n-1}.
\]
Dividing by \(\Pr(B_n)\), and using \(\sqrt n\Pr(B_n)\to\sqrt\pi\), establishes, by dominated convergence, that
\[
T_n\mid B_n\ \Longrightarrow\ T,
\qquad f_T(t)=\frac{t^{-1/2}e^{-t}}{\sqrt\pi},\ t>0.
\]
Indeed, for \(n\ge2\), \((1-t/n)^{n-1}\le e^{-t/2}\), so the conditional densities admit an integrable dominating function after normalization.

Finally \(S\) is Gamma with shape \(n+1\) and rate one, irrespective of the event. Chebyshev's inequality gives
\[
\Pr\big(|S-(n+1)|>n/(\log n)^2\mid B_n\big)
\le \frac{(n+1)(\log n)^4/n^2}{\Pr(B_n)}\to0.
\]
Since \(2Z=\log n-\log T_n=O_{\Pr(\cdot\mid B_n)}(\log n)\), it follows that
\[
2nR_n-\log n
=(\log n-\log T_n)\frac nS-\log n
=-\log T_n+o_{\Pr(\cdot\mid B_n)}(1).
\]
For \(T\sim\operatorname{Gamma}(1/2,1)\), \(\Pr(-\log T\le y)=\operatorname{erfc}(e^{-y/2})\). Exchanging \(E_0\) and \(E_n\) preserves \(B_n\), \(R_n\), and the other exponential variables, while exchanging which endpoint wins; conditional endpoint fairness and independence follow.

## Verification
The accompanying standalone `check.py` verifies the exact probability against a separate rational inclusion-exclusion calculation for \(1\le n\le40\), numerical quadrature for selected \(n\), positivity of the exact auxiliary density, asymptotic normalization, and seeded independent exponential simulations. Run `python check.py` with the standard Python library. These finite checks are corroboration; the proof above establishes all integer sample sizes and the limiting law.

## Relationship to prior work
Reznikov and Saff, *The Covering Radius of Randomly Distributed Points on a Manifold* (arXiv:1504.03029, initially submitted 12 April 2015), study expected covering radii and their asymptotics, including the expected-radius asymptotic for rectifiable curves in Corollary 3.6 and higher-dimensional cubes in Proposition 3.9; their results do not yield the finite one-dimensional endpoint-witness probability or its conditional marked law. Penrose, *Random Euclidean coverage from within* (arXiv:2101.06306, initially submitted 15 January 2021), develops distributional coverage results with a central focus on higher-dimensional boundary effects, and its Theorem 4.2 includes a strong law for polytopes (including intervals); the inspected full text does not provide the exact marked one-dimensional event here. Classical uniform-spacing and Gumbel results are background, not claimed as discoveries.

## Limitations
No assertion is made for nonuniform point distributions, dependent sites, higher-dimensional regions, or multiple coverage. Priority is not certified: the one-dimensional spacing transformation is classical, and an earlier explicitly equivalent weighted extreme-spacing identity could exist in older coverage literature. No independent mathematical validation has been performed.

## References
- A. Reznikov and E. B. Saff, *The Covering Radius of Randomly Distributed Points on a Manifold*, arXiv:1504.03029 (first posted 2015-04-12), https://arxiv.org/abs/1504.03029.
- M. D. Penrose, *Random Euclidean coverage from within*, arXiv:2101.06306 (first posted 2021-01-15), https://arxiv.org/abs/2101.06306.
- J. Hüsler, *Maximal, non-uniform spacings and the coverage problem*, Journal of Applied Probability 25 (1988), 519–528, https://doi.org/10.2307/3213981 (historical background; only abstract metadata inspected).
