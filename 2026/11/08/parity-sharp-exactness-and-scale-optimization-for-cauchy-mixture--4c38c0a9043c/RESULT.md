# Parity-sharp exactness and scale optimization for Cauchy-mixture Möbius trapezoids

## Finding

For a nontrivial positive finite mixture of centered Cauchy densities, the zero-phase Möbius-transformed trapezoidal rule has a complete, parity-dependent scale-selection law. Every odd node count admits exactly one transform scale giving zero normalization error. Every even node count instead has a strictly positive normalization error at every scale, and the global error-minimizing scale is unique. The entire even-scale objective is strictly convex in the logarithm of the scale, despite the rational expression in the scale itself.

Both optimizers tend to the geometric mean of the smallest and largest component scales. Their first-order logarithmic shifts depend only on the total masses at these extremal scales. The minimal even-node bias has an explicit sharp exponential equivalent. At two equal-mass scales, the even-node optimizer is exactly the geometric mean at *every* even count, while the unique odd-node exact scales decrease strictly toward that geometric mean with an exponentially small, explicitly quantified displacement.

## Assumptions and scope

Let \(m\ge2\), \(a_j>0\), \(w_j>0\), and \(\sum_{j=1}^m w_j=1\). Assume at least two \(a_j\) are distinct; repeated scales can be combined by adding weights. Define

\[
f(x)=\sum_{j=1}^m\frac{w_ja_j}{\pi(x^2+a_j^2)},\qquad \int_{\mathbb R}f(x)\,dx=1.
\]

For any \(L>0\), use \(x=L\cot(\theta/2)\), with the absolute Jacobian; extend the resulting angular function continuously at \(\theta=0\). It is

\[
g_L(\theta)=\sum_{j=1}^m\frac{w_ja_jL}{\pi\bigl(a_j^2+L^2+(L^2-a_j^2)\cos\theta\bigr)},\qquad g_L(0)=\sum_j\frac{w_ja_j}{2\pi L}.
\]

For **every integer** \(n\ge1\), the prescribed zero-phase rule samples exactly \(\theta_k=2\pi k/n\), \(0\le k<n\), and returns

\[
Q_n(L)=\frac{2\pi}{n}\sum_{k=0}^{n-1}g_L(2\pi k/n).
\]

The rule is a normalization quadrature for the density itself; it is **not** claimed to be exact for general test functions, arbitrary shifts of the angular grid, or non-centered Cauchy components.

Let \(a_-:=\min_j a_j<a_+:=\max_j a_j\), let \(p_-=\sum_{a_j=a_-}w_j>0\) and \(p_+=\sum_{a_j=a_+}w_j>0\), and define

\[
L_0=\sqrt{a_-a_+},\qquad \rho=\frac{\sqrt{a_+}-\sqrt{a_-}}{\sqrt{a_+}+\sqrt{a_-}}\in(0,1).
\]

**Exact finite-node classification.** With \(r_j(L)=(a_j-L)/(a_j+L)\),

\[
\boxed{Q_n(L)=\sum_{j=1}^m w_j\frac{1+r_j(L)^n}{1-r_j(L)^n}.}
\]

For odd \(n\), \(Q_n(L)\) is strictly decreasing in \(L\), with limits \(+\infty\) and \(0\). It therefore equals \(1\) at exactly one scale \(L_n\in(a_-,a_+)\). In particular,

\[
\boxed{L_1=\sum_j w_ja_j.}
\]

For even \(n\), \(Q_n(L)>1\) for all \(L>0\), and \(Q_n(e^t)\) is strictly convex in \(t\in\mathbb R\), with a unique minimizer \(L_n\in(a_-,a_+)\). In particular,

\[
\boxed{L_2=\sqrt{\frac{\sum_j w_ja_j}{\sum_j w_j/a_j}},\quad
\min_{L>0}(Q_2(L)-1)=\sqrt{\Bigl(\sum_jw_ja_j\Bigr)\Bigl(\sum_jw_j/a_j\Bigr)}-1>0.}
\]

**Sharp large-node regime.** For either parity as \(n\to\infty\) along its associated node counts, the unique exact scale (odd) or minimum-bias scale (even) obeys

\[
\boxed{\log\frac{L_n}{L_0}=\frac{a_+-a_-}{4L_0n}\log\frac{p_+}{p_-}+O(n^{-2}).}
\]

For even \(n\), the optimal excess has the sharp equivalent

\[
\boxed{\min_{L>0}\bigl(Q_n(L)-1\bigr)=4\sqrt{p_-p_+}\,\rho^n\bigl(1+O(n^{-1})\bigr).}
\]

Constants implicit in these estimates may depend on the fixed mixture, not on \(n\).

**Balanced two-scale refinement.** If \(m=2\), \(a_1=a<a_2=b\) and \(w_1=w_2=1/2\), then for every even \(n\),

\[
\boxed{L_n=\sqrt{ab},\qquad \min_L(Q_n(L)-1)=\frac{2\rho^n}{1-\rho^n}.}
\]

For odd \(n\),

\[
\boxed{L_1=\frac{a+b}{2}>L_3>L_5>\cdots>\sqrt{ab},\qquad
\log\frac{L_n}{\sqrt{ab}}\sim\frac{2\rho^{n+1}}{n(1-\rho^2)}.}
\]

## Proof

**1. Exact alias identity.** Put \(r=(a-L)/(a+L)\) for one component. Direct algebra gives

\[
2\pi g_{a,L}(\theta)=\frac{1-r^2}{1-2r\cos\theta+r^2}=\sum_{k\in\mathbb Z}r^{|k|}e^{ik\theta},\qquad |r|<1.
\]

(The left side uses the unit-mass component, before weighting.) The Fourier series is absolutely convergent. Averaging it over all \(n\)th roots of unity retains precisely the modes indexed by multiples of \(n\), giving \(1+2\sum_{q\ge1}r^{nq}=(1+r^n)/(1-r^n)\). Summing over the mixture proves the identity. Crucially, the transformed integrand at \(\theta=0\) has the finite, nonzero value specified above; replacing it by zero would change the rule.

**2. Odd node counts.** The derivative of each summand is

\[
\frac{d}{dL}\frac{1+r^n}{1-r^n}=\frac{2n r^{n-1}(-2a/(a+L)^2)}{(1-r^n)^2}.
\]

For odd \(n\), \(r^{n-1}\ge0\). At each \(L\) at least one component has nonzero \(r\), so the mixture derivative is strictly negative. Its limits as \(L\downarrow0\) and \(L\uparrow\infty\) are respectively \(+\infty\) and \(0\). At \(L=a_-\), all nonmatching scales contribute \(r>0\), hence \(Q_n>1\); at \(L=a_+\) the nonmatching scales have \(r<0\), hence \(Q_n<1\). This proves existence, uniqueness and location. When \(n=1\), \((1+r)/(1-r)=a/L\), so the root is the arithmetic mean.

**3. Even node counts and strict log-convexity of the objective.** For even \(n\), every summand is at least one, and equality in all summands would require \(L=a_j\) for all \(j\), forbidden by nontriviality. To prove strict convexity in \(t=\log L\), write \(n=2m\), \(s=t-\log a\), \(u=\tanh(s/2)\), \(y=u^2\in[0,1)\). Since the power is even, the component response equals \(\phi_n(s)=(1+u^n)/(1-u^n)\). Differentiation yields

\[
\phi_n''(s)=\frac n2\frac{(1-u^2)u^{n-2}}{(1-u^n)^3}H_n(y),
\]

where

\[
H_n(y)=(1-y)\left[(n-1)(1+y^m)-2\sum_{k=1}^{m-1}y^k\right].
\]

The bracket is positive for \(0\le y<1\), since it is at least \((2m-1)-2(m-1)=1\). Thus \(\phi_n''\ge0\), with equality only at \(s=0\) when \(n>2\); consequently \(\phi_n\) is strictly convex on \(\mathbb R\). A positive weighted sum of its translates is strictly convex. Every component response grows without bound as \(t\to\pm\infty\), proving existence and uniqueness of the global minimizer. Its derivative at \(L=a_-\) is negative and at \(L=a_+\) positive, proving interior location. For \(n=2\), \(Q_2(L)=\tfrac12[(\sum w_ja_j)/L+L\sum w_j/a_j]\); its unique minimum is the stated geometric mean of the arithmetic and reciprocal means. Strict positivity follows from Cauchy--Schwarz because the component scales differ.

**4. Geometric endpoint localization.** For \(L\in(a_-,a_+)\), the largest absolute alias ratio is

\[
R(L)=\max\left\{\frac{L-a_-}{L+a_-},\frac{a_+-L}{a_++L}\right\}.
\]

The first term increases and the second decreases, so \(R\) has its unique minimizer \(L_0=\sqrt{a_-a_+}\) and value \(\rho\). Components with strictly intermediate scales have strictly smaller absolute alias ratios at \(L_0\). For large even \(n\), bounds \(2w_j|r_j|^n\le 2w_j|r_j|^n/(1-|r_j|^n)\) and a comparison with the candidate \(L_0\) force the minimizer to converge to \(L_0\). For odd \(n\), the exact-root equation balances the strictly negative contributions from scales below \(L\) against positive contributions above \(L\); away from \(L_0\), the unique largest endpoint ratio would dominate this balance exponentially, so its root also converges to \(L_0\).

Write \(u=(L-a_-)/(L+a_-)\), \(v=(a_+-L)/(a_++L)\) near \(L_0\). The other scales are exponentially negligible uniformly there. For odd \(n\), cancellation gives

\[
p_-u^n/(1+u^n)=p_+v^n/(1-v^n)+o(\rho^n),
\]

and for even \(n\), the derivative-zero equation gives

\[
p_-u^{n-1}(1-u^2)/(1-u^n)^2
=p_+v^{n-1}(1-v^2)/(1-v^n)^2+o(\rho^{n-1}).
\]

Both imply \(n\log(u/v)=\log(p_+/p_-)+O(n^{-1})\) after first obtaining \(\log(L/L_0)=O(n^{-1})\). Since

\[
\left.\frac{d}{d\log L}\log(u/v)\right|_{L=L_0}=\frac{4L_0}{a_+-a_-},
\]

the stated \(O(n^{-2})\) log-scale expansion follows. At that scale,

\[
p_-u^n=\sqrt{p_-p_+}\,\rho^n(1+O(n^{-1})),\qquad
p_+v^n=\sqrt{p_-p_+}\,\rho^n(1+O(n^{-1})).
\]

The even bias is twice the sum of the two positive endpoint contributions plus exponentially smaller terms, yielding the coefficient \(4\sqrt{p_-p_+}\).

**5. Balanced two-scale refinement.** For equal masses at scales \(a<b\), reflection \(\log L\mapsto\log(ab)-\log L\) exchanges the two component responses when \(n\) is even. Strict convexity makes \(L=\sqrt{ab}\) the unique even optimum; substituting the two ratios \(\pm\rho\) gives its exact bias.

For odd \(n\), the error at the geometric mean is \(2\rho^{2n}/(1-\rho^{2n})>0\), so its unique root lies to the right. At a root \(L\), write \(u=(L-a)/(L+a)>v=(b-L)/(b+L)>0\). The root identity is \(u^n/(1+u^n)=v^n/(1-v^n)\). Increasing \(n\) by two multiplies the negative term in the odd bias by \(u^2(1+u^n)/(1+u^{n+2})>u^2\), while multiplying the positive term by \(v^2(1-v^n)/(1-v^{n+2})<v^2\). As \(u>v\), the error becomes negative at the previous root, forcing the new root leftward. Finally the error at \(L_0\), divided by the magnitude of its first logarithmic derivative there, is asymptotic to \(2\rho^{n+1}/[n(1-\rho^2)]\). A mean-value argument, using uniform derivative control on the exponentially short root interval, gives the asserted equivalence.

## Verification

The included standalone `verify.py` (Python 3, `mpmath`) evaluates the original transformed integrand at the actual \(n\) angular nodes and independently compares the result with the rational alias identity for three nontrivial mixtures and \(1\le n\le23\). It brackets the odd exact scales and even stationary scales to high precision; checks the exact \(n=1\) and \(n=2\) special cases, strict convexity factor bounds, the equal-weight two-scale identities and monotonic odd scales, and the endpoint large-node asymptotics. Its execution produced `PASS 1898 checks`. These are **finite numerical reproducibility tests**, not substitutes for the preceding all-count proofs.

For example, at equal weights and component scales \(1\) and \(9\), the single-node exact transform scale is \(5\), every even-node optimum is \(3\), and at \(n=2\) the unavoidable excess is \(2/3\). The first distinct odd-node root is approximately \(3.16999344601347\) at \(n=3\), decreasing toward \(3\).

## Relationship to prior work

Suzuki, Hyvönen, and Karvonen (arXiv:2407.13650, first public 18 July 2024) introduce and analyze the Möbius-transformed trapezoidal construction for Schwartz weights; the change of variables is **not novel here**. Hyvönen and Suzuki (arXiv:2604.27758, first public 30 April 2026), especially their Section 4 Proposition 4.1, extend the technique to polynomially decaying weights and prove exactness of certain polynomial test functions for the scale-matched basic Cauchy weight. The single-component matched-scale exactness is therefore **already covered**; it is not the present claim.

Trefethen and Weideman, *The Exponentially Convergent Trapezoidal Rule* (2014), explain the general Fourier aliasing identity underlying the rational formula above. That identity is **prior knowledge**, not claimed new. The present claim is the complete finite-mixture **global scale-selection classification by node parity**, strict logarithmic convexity at every even count, the sharp extremal-mass asymptotics, and the balanced two-scale monotonic odd-root law. These are not stated in the specifically inspected source sections and are not a direct named consequence of their stated theorems without the mixture-specific calculations here.

## Limitations

This theorem concerns only zero-phase equidistant angular nodes and the normalization integral of positive **centered** finite Cauchy mixtures. It does not address arbitrary functions under the density, shifted grids, negative mixture coefficients, nonzero locations, adaptive scale selection from noisy data, or floating-point conditioning for large \(n\). The claims are analytic, but computational checks sample only finite instances. Some specialized conformal or rational-quadrature literature may independently contain equivalent optimizers; no formal publication-priority or independent scientific audit has been performed.

## References

1. Y. Suzuki, N. Hyvönen, T. Karvonen, *Möbius-Transformed Trapezoidal Rule*, arXiv:2407.13650v1 (18 July 2024), https://arxiv.org/html/2407.13650v1 .
2. N. Hyvönen, Y. Suzuki, *Möbius-Transformed Trapezoidal Rule for Polynomial Weights*, arXiv:2604.27758v1 (30 April 2026), https://arxiv.org/html/2604.27758v1 , especially Proposition 4.1.
3. L. N. Trefethen, J. A. C. Weideman, *The Exponentially Convergent Trapezoidal Rule*, SIAM Review 56 (2014), 385–458, https://doi.org/10.1137/130932132 ; open full text https://people.maths.ox.ac.uk/trefethen/publication/PDF/2014_149.pdf .
