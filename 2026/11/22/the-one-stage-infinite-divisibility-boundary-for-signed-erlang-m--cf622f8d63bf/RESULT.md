# The one-stage infinite-divisibility boundary for signed Erlang mixtures

## Finding
Let \(k\) be any positive integer, \(0<p<1\), and \(a,b>0\). Let \(B\) be Bernoulli with success probability \(p\), and let \(G_+\sim\operatorname{Gamma}(k,a)\) and \(G_-\sim\operatorname{Gamma}(k,b)\) denote *shape–rate* gamma laws, jointly independent of \(B\). Define the two-sided, sign-randomized Erlang mixture
\[
X=\begin{cases}G_+,&B=1,\\-G_-,&B=0.\end{cases}
\]
Then the law of \(X\) is infinitely divisible **if and only if** \(k=1\), uniformly over all positive rates and nondegenerate sign probabilities.

For \(k=1\), write \(c=p/b-(1-p)/a\), so that \(-1/a<c<1/b\). Its characteristic exponent has zero deterministic finite-variation drift and Lévy density
\[
\frac{d\nu}{dx}(x)=
\begin{cases}
\big[e^{-ax}-\mathbf1_{\{c<0\}}e^{-x/|c|}\big]/x,&x>0,\\
\big[e^{-b|x|}-\mathbf1_{\{c>0\}}e^{-|x|/c}\big]/|x|,&x<0.
\end{cases}
\]
When \(c=0\), the subtracted terms are absent. These densities are nonnegative and integrable against \(1\wedge |x|\).

For every \(k\ge2\), the moment-generating function has an explicitly located complex zero *strictly inside its analyticity strip*, excluding infinite divisibility.

## Assumptions and scope
The distribution is a **mixture**, not the difference of two independent gamma variables. The rates \(a,b\) need not agree, and the two gamma variables need not be instantiated simultaneously: their conditional laws determine \(X\). The integer stage count \(k\ge1\), \(a,b>0\), and \(0<p<1\) are quantified universally. The cases \(p=0\) or \(p=1\) are deliberately excluded: there the law is a one-sided gamma or its reflection and is infinitely divisible for *all* positive shapes. The theorem does not classify noninteger gamma shapes, unequal positive and negative shapes, or other generalized gamma mixtures.

The moment-generating function of \(X\), holomorphic on the open strip \(\mathcal S=\{z\in\mathbb C:-b<\Re z<a\}\), is
\[
M_k(z)=p(1-z/a)^{-k}+(1-p)(1+z/b)^{-k}.
\]

## Proof
**A zero-free property of infinitely divisible laws.** Suppose a real infinitely divisible distribution has exponential moments at all real arguments in an open interval \((\ell,r)\) containing zero. In its Lévy–Khintchine formula, the positive and negative tails of the Lévy measure then have the corresponding exponential moments. The Gaussian, drift, and compensated small-jump terms extend analytically to \(\ell<\Re z<r\). Hence its moment-generating function is the exponential of an analytic function throughout that strip and **has no zeros there**. This standard consequence follows directly by dominated convergence on compact substrips and is the only general infinite-divisibility fact used for the negative result.

**Exclusion for every integer \(k\ge2\).** Put
\[
w=\left(\frac{1-p}{p}\right)^{1/k}e^{i\pi/k},\qquad
z_* =\frac{w-1}{w/a+1/b}=\frac{ab(w-1)}{bw+a}.
\]
Then \(w^k=-(1-p)/p\), \(w\ne0\), and \(\Re w\ge0\). Algebra gives
\[
\frac{1+z_*/b}{1-z_*/a}=w,
\]
so
\[
p(1+z_*/b)^k+(1-p)(1-z_*/a)^k=0.
\]
We must verify that this is a genuine zero **inside** the exponential-moment strip, rather than a pole or a point outside the domain. The explicit inverse fractional-linear map yields
\[
\Re(z_*+b)=\frac{b(a+b)[b|w|^2+a\Re w]}{|bw+a|^2}>0,
\]
\[
\Re(a-z_*)=\frac{a(a+b)[b\Re w+a]}{|bw+a|^2}>0.
\]
Thus \(-b<\Re z_*<a\). In this strip neither denominator of \(M_k\) vanishes, and the displayed numerator identity shows \(M_k(z_*)=0\). By the zero-free property, the mixture cannot be infinitely divisible. This argument is uniform for all stated \(p,a,b\), even very close to a one-sided degeneration.

**Construction for \(k=1\).** Direct simplification yields
\[
M_1(z)=\frac{1+c z}{(1-z/a)(1+z/b)},\quad
c=\frac p b-\frac{1-p}{a}.
\]
Because \(0<p<1\), one has \(-1/a<c<1/b\). The exponential-integral identity
\[
\int_0^\infty(e^{ut}-1)\frac{e^{-\lambda t}}t\,dt
=-\log(1-u/\lambda),\qquad \Re u<\lambda,
\]
shows, with the negative half-line using \(u=-z\), that
\[
\int_{\mathbb R\setminus\{0\}}(e^{zx}-1)\nu(dx)
=\log(1+cz)-\log(1-z/a)-\log(1+z/b)
\]
near the origin, using the analytic logarithm normalized to vanish at zero. If \(c>0\), its reciprocal satisfies \(1/c>b\), so the negative jump density \(e^{-b t}-e^{-t/c}\) is nonnegative. If \(c<0\), \(1/|c|>a\), so the analogous positive jump density is nonnegative. At \(c=0\) both ordinary exponential jump kernels remain. These jump densities have finite \(\int(1\wedge |x|)\nu(dx)\) and hence define a finite-variation infinitely divisible law. The Lévy exponent equals \(\log M_1\) on a neighborhood of zero, establishing equality in distribution. There is no Gaussian part or uncompensated drift. This completes both directions.

## Verification
The executable \`check.py\` uses exact rational arithmetic to compare shape-one moment-generating coefficients, and high-precision arithmetic to verify the constructed zero, strip bounds, Lévy kernel signs, and exponent decomposition over finite test grids. Executing \`python check.py\` with Python 3 and \`mpmath\` produced **1,503 passing checks**. Those finite checks are consistency evidence, *not* a proof for all parameters; all universal quantifiers are established by the preceding analytical argument. In particular, there is no finite-exhaustion assumption.

## Relationship to prior work
The motivation is Kloster's 2026 characterization of Thorin's infinitely divisible class and its closure under **HCM random multiplication**. A Bernoulli sign multiplier is not a positive random variable with an HCM density, and the cited closure result does not decide sign-randomized Erlang **mixtures**.

Çankaya, Bulut, Doğru, and Arslan (2015) introduced a two-sided Bernoulli generalized-gamma mixture and studied distributional properties and estimation. Korolev and Zeifman (2023), particularly Sections 1 and 4–5, distinguish sign-randomized generalized-gamma mixtures from normal variance–mean mixture models. The infinite-divisibility assertions for other mixture types do not imply the present all-integer-stage classification. Classical bilateral gamma laws constructed as *differences of independent gamma variables* are always infinitely divisible; that is a different operation from selecting one of two half-line laws.

Published results on positive gamma rate mixtures, zero-inflated negative-binomial counts, and angular zeros of generalized Stieltjes transforms study different distributions or only a zero-localization property; none of the inspected statements determines both directions of this exact sign-mixture classification for all \(p,a,b\).

## Limitations
Priority is assessed against the indicated accessible sources; no claim of exhaustive historical uniqueness or independent verification is made. A journal PDF of the 2015 generalized-gamma mixture paper was not fully accessible; its substantial available preview and later citations concern construction and statistical estimation, but an unnoticed statement elsewhere is a residual priority risk. The theorem is limited to common **integer** shape, strictly positive rates, and nondegenerate mixture probabilities. It does not imply that gamma sums or differences lack infinite divisibility; those remain infinitely divisible. The complex-zero obstruction is specific to the analyticity strip and is not a test based solely on real characteristic-function zeros.

## References
1. T. K. Kloster, *A characterization and closure property of Thorin's class*, arXiv:2611.01058v1, first submitted 2026-10-31. https://arxiv.org/abs/2611.01058
2. M. N. Çankaya, Y. M. Bulut, F. Z. Doğru, O. Arslan, *A Bimodal Extension of the Generalized Gamma Distribution*, Revista Colombiana de Estadística 38 (2015), 371–384. DOI:10.15446/rce.v38n2.51666. https://revistas.unal.edu.co/index.php/estad/article/view/51666
3. V. Korolev, A. Zeifman, *Quasi-Exponentiated Normal Distributions: Mixture Representations and Asymmetrization*, Mathematics 11 (2023), 3797. DOI:10.3390/math11173797. https://www.mdpi.com/2227-7390/11/17/3797
4. V. Pérez-Abreu, R. Stelzer, *Infinitely divisible multivariate and matrix Gamma distributions*, Journal of Multivariate Analysis 130 (2014), 155–175. DOI:10.1016/j.jmva.2014.04.017. (Background on additive gamma constructions.)
