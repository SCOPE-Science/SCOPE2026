# Sharp integrated BV error and a logarithmic boundary layer for Baskakov sampling

## Finding

Let \(n\ge2\) and define the classical Baskakov point-sampling operator on the observation window \([0,1]\) by
\[
(B_nf)(x)=\sum_{k=0}^{\infty}\binom{n+k-1}{k}\frac{x^k}{(1+x)^{n+k}}f(k/n),\qquad 0\le x\le1.
\]
For bounded, right-continuous real functions \(f\) of finite Jordan variation on \([0,\infty)\), with \(f(0)=f(0+)\), let
\[
C_n=\sup_{\operatorname{Var}(f)>0}\frac{\|B_nf-f\|_{L^1(0,1)}}{\operatorname{Var}_{[0,\infty)}(f)}.
\]
There is an exact finite computation of \(C_n\). Write \(I_z(a,b)\) for the regularized incomplete beta function, and for integers \(1\le j\le n\) define
\[
F_{n,j}(x)=I_{x/(1+x)}(j,n),\qquad
J_{n,j}(x)=x F_{n,j}(x)-\frac{j}{n-1}I_{x/(1+x)}(j+1,n-1),
\]
\[
E_{n,j}(s)=1-s+2J_{n,j}(s)-J_{n,j}(1),\qquad 0\le s\le1.
\]
Then
\[
\boxed{C_n=\max_{1\le j\le n}\max\left\{E_{n,j}((j-1)/n),\ E_{n,j}(j/n)\right\}.}
\]
The first candidate in a cell is a one-sided limit, and need not be attained by a genuine jump at that grid point. The finite formula is a supremum statement, not an all-degree attainment classification.

The exact sharp large-degree law is
\[
\boxed{\lim_{n\to\infty}\sqrt n\,C_n=\frac2{\sqrt\pi}.}
\]
More sharply, take any maximizing pair \((j_n,\mathrm{side}_n)\) in the finite formula and let \(s_n\) be its corresponding lower or upper grid endpoint. Then
\[
\boxed{\lim_{n\to\infty}(1-s_n)\sqrt{\frac n{\log n}}=\sqrt2.}
\]
Thus the finite-interval worst jumps lie *inside* the right boundary and retreat to it on the logarithmically enhanced central-limit scale. The scale coefficient is \(\sqrt2\), reflecting the value \(x(1+x)=2\) of the Baskakov local variance at the observed boundary.

## Assumptions and scope

The input is a genuine right-continuous Jordan-BV function on the half-line, not an arbitrary \(L^1\) equivalence class: point sampling makes its nodal representatives mathematically necessary. Total variation includes every interior jump and no artificial jump at \(0\). The error is Lebesgue-integrated only over \([0,1]\); the input variation is measured over the whole half-line. Constant functions have zero error and are excluded from the quotient. All sums converge absolutely for bounded \(f\). Only integer \(n\ge2\) is asserted.

A *maximizing one-sided grid location* means an endpoint appearing in an attaining pair of the displayed finite maximum; it may correspond to a sequence of admissible jumps approaching a grid node without an actual extremizing input.

## Proof

**Step 1: Exact reduction to single jumps.** Every admissible \(f\) has a signed finite-measure representation \(f(x)=c+\int_{(0,\infty)}\mathbf1_{[s,\infty)}(x)\,d\mu(s)\), with \(|\mu|((0,\infty))=\operatorname{Var}(f)\). Positivity, linearity, and constant preservation of \(B_n\) imply by Tonelli and the triangle inequality that the quotient is at most the supremum of the integrated errors of these single jumps. Conversely, every interior jump of height one is admissible, so this supremum is exactly the sharp coefficient. At a jump position \(s>0\), the sampled tail is \(\Pr(K_x\ge\lceil ns\rceil)\), where \(K_x\) has negative-binomial mass \(\binom{n+k-1}{k}x^k/(1+x)^{n+k}\).

**Step 2: Beta-prime duality and exact endpoints.** For every \(j\ge1\), its sampled tail is \(F_{n,j}(x)\). Differentiation gives
\[
F'_{n,j}(x)=\frac{x^{j-1}}{B(j,n)(1+x)^{n+j}},
\]
so \(F_{n,j}\) is the distribution function of the beta-prime variable \(Y_{n,j}=U_j/V_n\), where \(U_j,V_n\) are independent unit-scale gamma variables of shapes \(j,n\). Beta integration yields \(\int_0^x F_{n,j}(t)dt=J_{n,j}(x)\). On the open cell \(((j-1)/n,j/n)\), the jump response is
\[
\int_0^sF_{n,j}(x)dx+\int_s^1(1-F_{n,j}(x))dx=E_{n,j}(s).
\]
Here \(E'_{n,j}(s)=2F_{n,j}(s)-1\) and \(E''_{n,j}(s)=2F'_{n,j}(s)>0\); hence every cell supremum lies at one of its two endpoints. Right-continuity at a grid point selects the tail with index \(j\), while the value on the right is a genuine one-sided limit with index \(j+1\). For \(s>1\), the error is \(\int_0^1 F_{n,\lceil ns\rceil}(x)dx\), decreasing with the index and bounded by \(E_{n,n}(1)\). This proves the finite formula, including the boundary cases.

**Step 3: A full-line absolute-moment identity.** For \(0\le s\le1\), distribution-function integration on the half-line gives
\[
E_{n,j}(s)=\mathbb E|Y_{n,j}-s|-R_{n,j},\qquad R_{n,j}=\mathbb E[(Y_{n,j}-1)_+].
\]
The moment is finite for \(n\ge2\); in fact \(\mathbb EY_{n,j}=j/(n-1)\). The subtracted tail is the error that would lie beyond the finite observation window. Both terms have explicit incomplete-beta evaluations. The tail \(R_{n,j}\) is nondecreasing in \(j\), by gamma-shape stochastic ordering.

**Step 4: Uniform central limit expansion.** Put \(a=j/n\) and \(\sigma(a)=\sqrt{a(1+a)}\). For every fixed \(\delta>0\), uniformly when \(\delta\le j/n\le1\) and \(|s-j/n|\le1/n\),
\[
\mathbb E|Y_{n,j}-s|=\frac{\sqrt{2/\pi}\,\sigma(a)}{\sqrt n}+O_\delta(n^{-1}).\tag{1}
\]
To justify the error, write \(Y_{n,j}=U_j/V_n\) with gamma variables represented by sums of independent exponentials. The centered numerator \((U_j-j)-a(V_n-n)\), divided by \(\sqrt n\), has variance \(a(1+a)\) and a uniform Wasserstein-\(1\) normal-approximation error \(O_\delta(n^{-1/2})\) by the standard independent-sum Berry–Esseen bound in Wasserstein distance. Replacing the random factor \(n/V_n\) by one contributes \(O_\delta(n^{-1/2})\) to the normalized first absolute moment by Cauchy–Schwarz and bounded inverse-gamma moments; replacing \(s\) by \(a\) has the same order. Dividing back by \(\sqrt n\) gives (1). When \(j/n\to0\), the beta-prime second moment and \(|s-j/n|\le1/n\) show \(\sqrt n\,\mathbb E|Y_{n,j}-s|\to0\). For fixed \(a<1\), \(R_{n,j}\) is exponentially small by gamma concentration.

Choose grid positions with \(1-j/n\to0\) but \((1-j/n)\sqrt n\to\infty\). Then (1) and concentration give \(\liminf\sqrt n C_n\ge\sqrt{2/\pi}\,\sigma(1)=2/\sqrt\pi\). The upper bound follows from (1), the small-index second-moment bound, and \(R_{n,j}\ge0\). Strict growth of \(\sigma(a)\) on \([0,1]\) forces \(j_n/n\to1\) for every maximizing pair.

**Step 5: Precise logarithmic boundary retreat.** Let \(d_n=c\sqrt{\log n/n}\) with fixed \(c>0\), and take \(j/n=1-d_n+O(1/n)\). Applying Stirling's formula to the displayed beta-prime density and Taylor expanding its logarithm in the range \(|y-j/n|\le C\sqrt{\log n/n}\) yields a relative Gaussian-density estimate \(1+O_C((1+\log^{3/2}n)/\sqrt n)\). Gamma Chernoff bounds make the contribution outside a sufficiently large fixed multiple of this window negligible relative to the relevant Gaussian excess tail. Consequently, for \(z_n=d_n\sqrt{n/2}\),
\[
R_{n,j}\sim\sqrt{\frac2n}\bigl[\phi(z_n)-z_n\overline\Phi(z_n)\bigr]
\sim \sqrt{\frac2n}\frac{\phi(z_n)}{z_n^2}
=\frac{2}{c^2\sqrt\pi}\frac{n^{-1/2-c^2/4}}{\log n}(1+o(1)),\tag{2}
\]
where \(\phi\) and \(\overline\Phi\) are the standard Gaussian density and upper tail. At \(c=\sqrt2\), this is \(O((n\log n)^{-1})\). By (1) and the Taylor expansion of \(\sigma(1-d)\), a competitor with \(d=\sqrt{2\log n/n}+O(1/n)\) loses only \(\frac{3}{2\sqrt\pi}\sqrt{2\log n}/n+O(n^{-1})\) from the maximal full-line Gaussian moment.

For any fixed \(\varepsilon>0\), an endpoint with \(d\ge(\sqrt2+\varepsilon)\sqrt{\log n/n}\) has a strictly larger full-moment deficit, by an amount of order \(\sqrt{\log n}/n\), and cannot maximize (the nonnegative tail can only reduce its value). An endpoint with \(d\le(\sqrt2-\varepsilon)\sqrt{\log n/n}\) has, by monotonicity of \(R_{n,j}\) in \(j\), a tail at least as large as the right side of (2) with \(c=\sqrt2-\varepsilon\); this dominates \(\sqrt{\log n}/n\) and excludes it as well. The \(O(n^{-1})\) full-moment remainders are smaller than these strict margins. Since \(\varepsilon\) is arbitrary and the two one-sided endpoints differ by at most \(1/n\), the boxed logarithmic location law follows.

## Verification

The standalone script `check_baskakov.py` evaluates the beta-prime formula against independently evaluated negative-binomial tails and numerical quadrature of the original step response, checks convex endpoint dominance across cells, and computes finite maxima and their normalized asymptotics. On the checked test set it reports 324 independent tail comparisons, 81 quadrature comparisons, and 81 endpoint checks. These are finite consistency tests; the infinite-degree conclusions rest on the proof above, not on extrapolating numerical output.

## Relationship to prior work

Abel, Gupta and Ivan (2002), in their definitions and main theorems, treat *Kantorovich integral averages* of the Baskakov basis and give pointwise convergence rates and discontinuity limits; they explicitly distinguish those averages from the classical Baskakov point-sampling operator. Gupta and Abel (2004), in its introduction and Theorem 2.1, treat a different *Durrmeyer integral* modification of the Baskakov basis and give pointwise BV convergence-rate estimates. Patel and Mishra (first published July 2, 2014) likewise treat a modified integral operator and functions whose derivative has bounded variation. Zeng, Gupta and Agratini (2014) study a Baskakov–Kantorovich Bézier variant. These results motivate the operator setting but do not imply the present point-sampling identity-error norm on a fixed observation window, its finite incomplete-beta maximum, or the \(\sqrt{2\log n/n}\) retreat of a norming jump. This last phenomenon is analogous to, but is not an implication of, the corresponding Poisson/Szász–Mirakjan–Kantorovich window law: the probability kernels, endpoint variances, and point-sampling conventions differ. The 2006 Gupta–Govil study of Baskakov-type operators and other older rate results remain relevant for historical-priority review.

## Limitations

This is not a theorem about the Durrmeyer, Kantorovich, Bézier, weighted-norm, or multidimensional Baskakov variants. The observation window has fixed right endpoint \(1\); replacing it changes the constants. The finite formula does not assert a closed all-degree winner index, strict uniqueness, or actual norm attainment. The moderate-deviation conclusion is asymptotic and supplies no explicit finite-degree error bound. Literature comparison is substantial but cannot prove worldwide novelty; some older potentially relevant primary sources were accessible only through metadata or abstracts.

## References

1. U. Abel, V. Gupta and M. Ivan, *On the rate of convergence of Baskakov–Kantorovich–Bézier operators for bounded variation functions*, Rev. Anal. Numér. Théor. Approx. 31 (2002), 123–133, DOI: 10.33993/jnaat312-716, first published 2002-08-01. Public full-text transcription: https://www.academia.edu/96850757/On_the_rate_of_convergence_of_Baskakov_Kantorovich_Bezier_operators_for_bounded_variation_functions
2. V. Gupta and U. Abel, *Rate of convergence of bounded variation functions by a Bézier–Durrmeyer variant of the Baskakov operators*, International Journal of Mathematics and Mathematical Sciences 2004, 459–468, DOI: 10.1155/S0161171204205038. Accessible full text: https://studylib.net/doc/10449005/rate-of-convergence-of-bounded-variation-functions-by-a-b...
3. P. Patel and V. N. Mishra, *Rate of Convergence of Modified Baskakov-Durrmeyer Type Operators for Functions of Bounded Variation*, 2014, DOI: 10.1155/2014/235480. First published July 2, 2014. https://onlinelibrary.wiley.com/doi/10.1155/2014/235480
4. X.-M. Zeng, V. Gupta and O. Agratini, *Approximation by Bézier variant of the Baskakov-Kantorovich operators in the case \(0<\alpha<1\)*, Rocky Mountain Journal of Mathematics 44 (2014), 317–327, DOI: 10.1216/RMJ-2014-44-1-317. https://ictp.acad.ro/approximation-by-bezier-variant-of-the-baskakov-kantorovich-operators-in-the-case-0-%CE%B1-1/
5. V. Gupta and N. K. Govil, *Rate of convergence for Baskakov type operators on functions of bounded variation*, Journal of Combinatorics, Information and System Sciences 31 (2006), 1–17. Bibliographic description: https://portal.mardi4nfdi.de/wiki/Rate_of_convergence_for_Baskakov_type_operators_on_functions_of_bounded_variation
