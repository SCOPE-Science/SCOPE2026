# Exact lattice-phase variance for triangular Latin-hypercube quadrature

## Finding

Let \(n\ge2\) be an integer. In the unit square, take a standard independently jittered, randomized two-dimensional Latin hypercube: choose a uniform permutation \(\pi\) of \(\{0,\ldots,n-1\}\), independent uniform variables \(U_i,V_i\in(0,1)\), and sample
\[
(X_i,Y_i)=\bigl((i+U_i)/n,(\pi(i)+V_i)/n\bigr),\qquad 0\le i<n.
\]
For \(c\in[0,2]\), set \(\widehat I_{n,c}=n^{-1}\sum_{i=0}^{n-1}\mathbf1_{\{X_i+Y_i<c\}}\), \(s=\min\{c,2-c\}\), and \(\theta_n=\{ns\}\), the fractional part. Define the polynomials
\[
L(s)=3s^4-8s^3+6s^2,\quad
P(\theta)=-6\theta^5+9\theta^4+2\theta^3-6\theta^2+\theta.
\]
The estimator is unbiased, and its **exact finite-sample variance** at every \(n\ge2\) and every \(c\in[0,2]\) is
\[
\boxed{\operatorname{Var}(\widehat I_{n,c})=
\frac{n^3L(s)+ns\bigl(6\theta_n^2(1-\theta_n)^2-1\bigr)+P(\theta_n)}{12n^3(n-1)}.}
\tag{1}
\]
In particular, at the central diagonal \(c=1\), \(\operatorname{Var}(\widehat I_{n,1})=(n+1)/(12n^2)\).

Define \(V(s)=L(s)/12\) and the third-order centered residual
\[
R_n(c)=n^3\Bigl[\operatorname{Var}(\widehat I_{n,c})-V(s)/n-V(s)/n^2\Bigr].
\]
For every fixed \(c\in[0,2]\), uniformly over \(s\in[0,1]\),
\[
\boxed{R_n(c)=V(s)-\frac{s}{12}+\frac{s}{2}\theta_n^2(1-\theta_n)^2+O(n^{-1}).}
\tag{2}
\]
The lattice phase therefore first affects the variance at order \(n^{-3}\), not in either of its first two asymptotic terms.

For irrational \(s\in(0,1)\), the **complete set** of subsequential limits of \(R_n(c)\) is
\[
\boxed{\left[V(s)-\frac{s}{12},\;V(s)-\frac{s}{12}+\frac{s}{32}\right].}
\tag{3}
\]
For rational \(s=p/q\in(0,1)\) in lowest terms, the complete limit set is the finite set
\[
\left\{V(s)-\frac{s}{12}+\frac{s}{2}\frac{j^2(q-j)^2}{q^4}:0\le j<q\right\}.
\tag{4}
\]
Its minimum is \(V(s)-s/12\), and its maximum exceeds that minimum by \(s/32\) if \(q\) is even and by \(s(1-q^{-2})^2/32\) if \(q\) is odd. For \(s=0\) or \(s=1\), the phase limit set is a singleton. These are claims about exact variance, not about a realized random sampling error.

## Assumptions and scope

The permutation is uniformly distributed over all \(n!\) permutations. All \(2n\) continuous jitter variables are mutually independent, uniform on \((0,1)\), and independent of the permutation. There is one sample in each horizontal and vertical stratum, with equal integration weights. The domain is \([0,1]^2\), the discontinuity is exactly the line \(x+y=c\), and no post-optimization, orthogonal-array constraint, common jitter, or correlation optimization is imposed. Strict versus nonstrict boundary indicators are equivalent because the jitters are continuous.

The triangle has area \(c^2/2\) for \(0\le c\le1\) and \(1-(2-c)^2/2\) for \(1\le c\le2\), which is the expectation of the estimator. Reflection of both coordinates sends the indicator at \(c\) to the complement of the indicator at \(2-c\) almost surely, and preserves the Latin-hypercube sampling law. Consequently the two offsets have equal variance. It suffices to analyze \(c=s\in[0,1]\).

## Proof

Put \(a_{ij}=\Pr(U+V<ns-i-j)\) for independent unit uniforms \(U,V\), with indices \(0\le i,j<n\). Conditional on \(\pi\), the selected-cell indicators are independent Bernoulli variables with success probabilities \(a_{i,\pi(i)}\). For \(n\ge2\), the elementary uniform-permutation variance identity, applied to a real matrix \(a\), reads
\[
\operatorname{Var}_{\pi}\Bigl(\sum_i a_{i,\pi(i)}\Bigr)
=\frac1{n-1}\sum_{ij}(a_{ij}-r_i/n-t_j/n+T/n^2)^2,
\tag{5}
\]
where \(r_i=\sum_j a_{ij}\), \(t_j=\sum_i a_{ij}\), and \(T=\sum_{ij}a_{ij}\). To verify (5), expand its left side and use \(\Pr(\pi(i)=j)=1/n\) and \(\Pr(\pi(i)=j,\pi(k)=\ell)=1/[n(n-1)]\) for distinct rows and columns. The right side results from subtracting row and column means. Law of total variance consequently gives
\[
 n^2\operatorname{Var}(\widehat I_{n,s})
=\frac1n\sum_{ij}a_{ij}(1-a_{ij})
+\frac1{n-1}\left(\sum_{ij}a_{ij}^2-\frac2n\sum_i r_i^2+\frac{T^2}{n^2}\right),
\tag{6}
\]
since the cell matrix is symmetric.

Write \(ns=m+\theta\), with integer \(0\le m\le n\) and \(0\le\theta<1\). The sum of two independent uniforms has triangular distribution. Accordingly \(a_{ij}=1\) when \(i+j\le m-2\), equals \(u=1-(1-\theta)^2/2\) when \(i+j=m-1\), equals \(v=\theta^2/2\) when \(i+j=m\), and is zero otherwise. Out-of-range diagonals are ignored. Their potentially incorrect formal multiplicity at the endpoint \(m=n,\theta=0\) multiplies \(v=0\) and has no effect. Elementary diagonal counting yields
\[
\begin{aligned}
T&=\frac{(m+\theta)^2}{2}=\frac{n^2s^2}{2},\\
\sum_{ij}a_{ij}^2&=\frac{m(m-1)}2+mu^2+(m+1)v^2,\\
\sum_i r_i^2&=\frac{m(m^2-1)}{12}+m\left(\frac m2+\theta\right)^2+\frac{\theta^4}{4}.
\end{aligned}\tag{7}
\]
For the last identity the first \(m\) row sums, in reverse order, are \(j+\theta+1/2\) with \(0\le j<m\), and the only remaining nonzero row sum, when present, is \(\theta^2/2\). The formulas remain valid for \(m=0\) and for \(m=n,\theta=0\).

Substitute (7) into (6), use \(m=ns-\theta\), and collect powers of \(n\). The resulting numerator is precisely
\[
 n^3(3s^4-8s^3+6s^2)+ns[6\theta^2(1-\theta)^2-1]
 -6\theta^5+9\theta^4+2\theta^3-6\theta^2+\theta,
\]
with denominator \(12n^3(n-1)\). This proves (1), including its endpoints by direct substitution. The computation uses exact polynomial identities; it does not infer the formula from sampled \(n\) values.

Since \(L\) and \(P\) are bounded for \(s,\theta\in[0,1]\), divide (1) by \(n-1\) and expand \((1-1/n)^{-1}\) through the needed powers. This gives (2) with a remainder uniformly \(O(n^{-1})\) for the scaled residual. For irrational \(s\), the fractional parts \(\{ns\}\) are dense in \([0,1]\), and \(\theta^2(1-\theta)^2\) maps that interval continuously onto \([0,1/16]\). Every point of this interval occurs along a subsequence, proving (3). For reduced rational \(s=p/q\), the phases cycle through exactly \(0,1/q,\ldots,(q-1)/q\). The maximum occurs nearest \(q/2\), giving (4) and the stated parity-dependent extrema. The reflection argument extends the result from \([0,1]\) to all \([0,2]\).

## Verification

The accompanying `verify_offset.py` uses exact rational arithmetic and two independent finite methods: the complete cell-probability and permutation-covariance formula for many grid sizes and offsets, and explicit enumeration of all permutations for small sizes. It passed 733 exact assertions. In particular, the centered case, reflected offsets, and offsets with phase zero and nonzero were checked. The verifier is a finite consistency test; the all-size and irrational-rotation assertions rely on the proof above, not the computation. Run `python3 verify_offset.py` without nonstandard dependencies.

## Relationship to prior work

Krumscheid and Pettersson, *Sequential Estimation using Hierarchically Stratified Domains with Latin Hypercube Sampling* (arXiv:2305.13421, first posted 2023-05-22), present general LHS variance identities, large-sample additive-residual theory, and a stratified adaptive estimator. Those general identities are acknowledged. They can imply the leading \(n^{-1}\) term here after a separate integrand calculation; the leading term is not claimed novel. Their paper's mathematical methods and numerical tests do not give (1), the first appearance of grid phase at order \(n^{-3}\), or the full arithmetic limit sets (3)-(4).

Liu and Owen, *Pre-integration via active subspaces* (arXiv:2202.02682, first posted 2022-02-06), motivate accurate integration near discontinuities and the effect of smoothing through conditioning, but address a different sampling framework rather than this finite Latin-hypercube phase law. Stein's 1987 large-sample LHS analysis and Owen's 1992 central-limit theorem precede both and are acknowledged as general theory, not rediscoveries. The previously recorded oblique-half-plane *jittered-grid* phase result studies \(n^2\) mutually independent grid samples, not an \(n\)-point random Latin hypercube; its leading \(n^{-3}\) oscillation does not imply the current subleading \(n^{-3}\) variance oscillation. Classical lattice fractional-part density is prior art.

## Limitations

The exact formula applies to the 45-degree threshold family only, with independent within-cell jitters and a uniform coordinate permutation. It does not establish an exact law for arbitrary slopes, adaptive/optimized Latin hypercubes, higher dimensions, or other discontinuities. The phase interval is the set of asymptotic variance residual limits, not a sample-path uncertainty interval. The basic permutation-variance identity and the leading LHS asymptotic are standard; the assessed finding is their exact finite-offset evaluation and sharp third-order arithmetic phase classification. Specialist historical priority remains possible, and no independent audit has been performed.

## References

1. Sebastian Krumscheid and Per Pettersson, *Sequential Estimation using Hierarchically Stratified Domains with Latin Hypercube Sampling*, arXiv:2305.13421, initial version 2023-05-22. https://arxiv.org/abs/2305.13421
2. Sifan Liu and Art B. Owen, *Pre-integration via active subspaces*, arXiv:2202.02682, initial version 2022-02-06. https://arxiv.org/abs/2202.02682
3. Michael Stein, *Large Sample Properties of Simulations Using Latin Hypercube Sampling*, Technometrics 29 (1987), 143–151. https://doi.org/10.1080/00401706.1987.10488205
4. Art B. Owen, *A Central Limit Theorem for Latin Hypercube Sampling*, Journal of the Royal Statistical Society Series B 54 (1992), 541–551. https://doi.org/10.1111/j.2517-6161.1992.tb01895.x
