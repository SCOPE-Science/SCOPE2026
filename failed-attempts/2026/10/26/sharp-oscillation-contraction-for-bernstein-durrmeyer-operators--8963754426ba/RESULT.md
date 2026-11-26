# Sharp oscillation contraction for Bernstein–Durrmeyer operators with arbitrary measures

## Finding

The exact one-step oscillation contraction coefficient of every nondegenerate univariate Bernstein–Durrmeyer operator with an arbitrary positive Borel base measure is determined by its two endpoint posterior distributions. This gives a closed integral expression even for purely atomic, singular, or asymmetric measures.

More precisely, for every integer \(n\geq 1\) and every finite positive Borel measure \(\mu\) on \([0,1]\) with \(\mu((0,1))>0\), write
\[
 A=\int_{[0,1]}(1-u)^n\,d\mu(u),\qquad B=\int_{[0,1]}u^n\,d\mu(u),\qquad
 \theta=\frac{(B/A)^{1/n}}{1+(B/A)^{1/n}}.
\]
Then \(A,B>0\) and, for the operator defined below,
\[
 \boxed{\sup_{f\in C([0,1]),\ \operatorname{osc}(f)>0}
 \frac{\operatorname{osc}(T_{n,\mu}f)}{\operatorname{osc}(f)}
 =\int_{[0,\theta]}\left(\frac{(1-u)^n}{A}-\frac{u^n}{B}\right)\,d\mu(u)
 =:\delta_{n,\mu}<1.}
\]
Here \(\operatorname{osc}(f)=\sup_{[0,1]}f-\inf_{[0,1]}f\). The equality is a sharp supremum, not a claim that a continuous maximizing function always exists. For Lebesgue measure, the exact value simplifies to \(\delta_{n,\mu}=1-2^{-n}\). Moreover, the normalized base measure is stationary for the associated Markov kernel, which contracts total-variation distance at the sharp one-step factor \(\delta_{n,\mu}\).

## Assumptions and scope

Let \(b_{n,k}(x)=\binom{n}{k}x^k(1-x)^{n-k}\), \(0\leq k\leq n\), with the usual endpoint convention. Define \(Z_k=\int_{[0,1]}b_{n,k}(u)\,d\mu(u)\); all \(Z_k\) are strictly positive because the integrands are strictly positive on \((0,1)\). Define the posterior probabilities
\[
 Q_k(E)=\frac{1}{Z_k}\int_E b_{n,k}(u)\,d\mu(u)
\]
for Borel sets \(E\), and the row probability measures
\[
 K_x=\sum_{k=0}^{n}b_{n,k}(x)Q_k,\qquad
 (T_{n,\mu}f)(x)=\int_{[0,1]}f(u)\,K_x(du).
\]
This is a positive, constant-preserving polynomial operator on \(C([0,1])\). Total variation of two probability measures means \(d_{\mathrm{TV}}(P,Q)=\sup_E|P(E)-Q(E)|\), with **no factor of two**. All quantities refer to fixed finite \(n\); no asymptotic approximation assertion is needed.

## Proof

**Step 1: posterior stochastic ordering and single crossings.** Fix \(0\leq i<j\leq n\). On the interior, the likelihood ratio of their densities relative to \(\mu\) is
\[
 \frac{dQ_j/d\mu}{dQ_i/d\mu}(u)
 =\frac{Z_i\binom nj}{Z_j\binom ni}
 \left(\frac{u}{1-u}\right)^{j-i},
\]
which is nondecreasing in \(u\). At the endpoints it has the corresponding zero/infinite conventions; direct inspection of the Bernstein factors gives the same one-crossing sign arrangement. Since each density integrates to one, the signed density of \(Q_i-Q_j\) is nonnegative to the left of a threshold and nonpositive to its right (zero-density regions and ties are permitted). Thus, with \(F_k(t)=Q_k([0,t])\),
\[
 F_i(t)\geq F_j(t)\quad(0\leq t\leq1),\qquad
 d_{\mathrm{TV}}(Q_i,Q_j)=\sup_{t\in[0,1]}(F_i(t)-F_j(t)).
\]
This also follows for measures with atoms: the sign partition remains an initial interval and its complement, and the equal-density atom may be placed on either side.

**Step 2: endpoint posteriors dominate all pairs.** Applying Step 1 to each adjacent pair yields \(F_0\geq F_1\geq\cdots\geq F_n\) pointwise. Consequently, for any \(i<j\),
\[
 d_{\mathrm{TV}}(Q_i,Q_j)
 =\sup_t(F_i(t)-F_j(t))
 \leq\sup_t(F_0(t)-F_n(t))
 =d_{\mathrm{TV}}(Q_0,Q_n).
\]
For arbitrary \(x,y\in[0,1]\), use the probability weights \(b_{n,k}(x)\) and \(b_{n,k}(y)\), and expand
\[
 K_x-K_y=\sum_{i,j=0}^{n} b_{n,i}(x)b_{n,j}(y)(Q_i-Q_j).
\]
Convexity of total variation now gives \(d_{\mathrm{TV}}(K_x,K_y)\leq d_{\mathrm{TV}}(Q_0,Q_n)\). Equality holds for \(x=0\) and \(y=1\), since \(K_0=Q_0\) and \(K_1=Q_n\). Therefore the exact Dobrushin row diameter is the endpoint distance.

**Step 3: evaluate the endpoint distance.** Since \(Z_0=A\) and \(Z_n=B\), the density difference \(Q_0-Q_n\) relative to \(\mu\) is
\[
 h(u)=\frac{(1-u)^n}{A}-\frac{u^n}{B}.
\]
The inequality \(h(u)\geq0\) is equivalent to \(u/(1-u)\leq(B/A)^{1/n}\), hence to \(u\leq\theta\). Its positive mass is exactly \(\int_{[0,\theta]}h\,d\mu\), which equals \(d_{\mathrm{TV}}(Q_0,Q_n)\).

**Step 4: identify the oscillation norm and strict contraction.** For any continuous \(f\) with oscillation one, the signed-measure estimate implies
\[
 |T_{n,\mu}f(x)-T_{n,\mu}f(y)|\leq d_{\mathrm{TV}}(K_x,K_y).
\]
Conversely, bounded indicators of the positive set of \(Q_0-Q_n\) give equality for the endpoint rows. Regularity of finite Borel measures on the compact interval permits approximating this indicator in integral against both endpoint probability measures by continuous functions bounded between zero and one; their endpoint differences converge to the same sharp constant. Because both endpoint posteriors have strictly positive densities with respect to \(\mu\) throughout the interior and \(\mu((0,1))>0\), they share positive common mass. Therefore their total-variation distance is strictly less than one.

**Step 5: stationarity and iteration.** The detailed-balance identity
\[
 d\mu(x)K_x(du)
 =\sum_{k=0}^{n}\frac{b_{n,k}(x)b_{n,k}(u)}{Z_k}\,d\mu(x)d\mu(u)
\]
is symmetric in \(x,u\). Hence \(\pi=\mu/\mu([0,1])\) is stationary. The standard Dobrushin coupling/Jordan-decomposition inequality yields, for all probability measures \(\nu,\eta\) and integers \(m\geq1\),
\[
 d_{\mathrm{TV}}(\nu K^m,\eta K^m)
 \leq\delta_{n,\mu}^{\,m}\,d_{\mathrm{TV}}(\nu,\eta).
\]
The factor is sharp for one step, but no sharpness for higher powers is asserted. Because \(\delta_{n,\mu}<1\), the stationary law is unique.

For the uniform measure, \(A=B=1/(n+1)\), \(\theta=1/2\), and direct integration gives
\[
 \delta_{n,du}=(n+1)\int_0^{1/2}\bigl((1-u)^n-u^n\bigr)du
 =1-2^{-n}.
\]
This completes the proof.

## Verification

The companion standalone `verify.py` uses only the Python standard library and exact rational arithmetic. For every \(n\in\{1,2,3,4,5,6\}\), it tests four finitely supported measures, including asymmetric measures with endpoint atoms, a one-point interior measure, and two-point interior support. It constructs normalized posterior rows, compares **all** posterior pairs with the endpoint distance, checks 25 kernel-row pairs on a fixed five-point grid, verifies stationarity exactly, and checks the uniform-base-measure closed form symbolically in the rationals. Run `python3 verify.py`; the completion marker is `ALL_EXACT_CHECKS_PASSED`.

These finite checks are diagnostic, **not** a substitute for the all-\(n\), all-\(\mu\) proof in the preceding section.

## Relationship to prior work

Diaconis, Khare and Saloff-Coste study the Beta–Binomial Gibbs \(\theta\)-chain, which is the Beta-base-measure specialization of the kernel here. Their explicit eigenvalues and chi-square convergence bounds concern a different invariant than the sharp **one-step** total-variation/oscillation diameter. Berdysheva and Jetter's work on arbitrary-weight Bernstein–Durrmeyer operators and Berdysheva's work on arbitrary-measure convergence establish the operator framework and approximation properties, not an evaluated sharp one-step row diameter in their accessible portions. Gaubert and Qu establish the general equivalence between oscillation contraction and Dobrushin-type coefficients; the additional assertion here is that **for this entire measure-parametrized Bernstein family**, the supremum over every pair of continuous input locations collapses to the two endpoint posteriors and admits the stated single-threshold integral.

## Limitations

This is a univariate fixed-degree result, not a multivariate generalization or an exact multi-step mixing formula. For an arbitrary \(\mu\), the displayed integral is the exact answer and need not reduce to elementary numbers. The strict-contraction claim requires positive mass inside \((0,1)\); endpoint-supported measures fall outside the stated domain. The result is a mathematical deduction with direct proof and finite reproducibility checks, not an independently audited theorem. The full text of the two most relevant older papers on arbitrary-weight/arbitrary-measure Bernstein–Durrmeyer operators was not accessible in accessible sources; their accessible text does not show this sharp coefficient, but undiscovered equivalent coverage is a residual originality risk.

## References

1. P. Diaconis, K. Khare, L. Saloff-Coste, “Gibbs Sampling, Exponential Families and Orthogonal Polynomials,” arXiv:0808.3852 (first submitted 2008-08-28), especially the Beta–Binomial \(\theta\)-chain in §4.1.2.
2. E. E. Berdysheva and K. Jetter, “Multivariate Bernstein–Durrmeyer operators with arbitrary weight functions,” *Journal of Approximation Theory*, DOI: 10.1016/j.jat.2009.11.005 (first online 2009-11-22).
3. E. E. Berdysheva, “Uniform convergence of Bernstein–Durrmeyer operators with respect to arbitrary measure,” *Journal of Mathematical Analysis and Applications* 394 (2012), 324–336, DOI: 10.1016/j.jmaa.2012.03.004.
4. S. Gaubert and Z. Qu, “Dobrushin’s ergodicity coefficient for Markov operators on cones,” arXiv:1307.4649 (2013).
