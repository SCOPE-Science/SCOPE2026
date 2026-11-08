# Sharp replica and logarithmic strong-law thresholds for stratified endpoint quadrature

## Finding

For fixed real parameters \(0<\alpha<1\) and \(\beta\in\mathbb R\), let
\[
f_{\alpha,\beta}(x)=x^{-\alpha}[\log(e/x)]^{-\beta},\qquad 0<x\le1,
\]
and put \(I=\int_0^1f_{\alpha,\beta}(x)\,dx\), which is finite. For each integer \(n\ge1\), independently draw \(U_{n,j}^{(\ell)}\sim\mathrm{Unif}(0,1)\), for \(j=0,\ldots,n-1\) and \(\ell=1,\ldots,2r-1\), with all draws independent **also across different values of** \(n\). The one-dimensional independently jittered (equivalently, one-dimensional Latin-hypercube) estimates and their sample median are
\[
Q_n^{(\ell)}=\frac1n\sum_{j=0}^{n-1}f_{\alpha,\beta}\!\left(\frac{j+U_{n,j}^{(\ell)}}n\right),\qquad
M_{n,r}=\operatorname{med}\{Q_n^{(1)},\ldots,Q_n^{(2r-1)}\},
\]
where \(r\ge1\) is a fixed integer. Every individual estimate is unbiased. The median need not be unbiased.

**Sharp fixed-error law.** For every fixed \(\varepsilon>0\),
\[
\boxed{\lim_{n\to\infty}
 n^{\frac{r(1-\alpha)}\alpha}(\log n)^{\frac{r\beta}\alpha}
 \Pr(M_{n,r}>I+\varepsilon)
 =\binom{2r-1}{r}\left(\frac{\alpha^\beta}{\varepsilon}\right)^{r/\alpha}.}
\]
This limit is strictly positive and finite. For all the stated parameters, \(\mathbb E|M_{n,r}-I|\to0\), hence the estimator converges in probability.

**Complete almost-sure classification.** The sequence \(M_{n,r}\) converges to \(I\) almost surely **if and only if**
\[
\boxed{\alpha<\frac{r}{r+1},\quad\text{or}\quad
 \alpha=\frac{r}{r+1}\ \text{and}\ \beta>\frac{1}{r+1}.}
\]
In every complementary case,
\[
\Pr\!\left(\liminf_{n\to\infty}M_{n,r}=I\ \text{and}\
\limsup_{n\to\infty}M_{n,r}=+\infty\right)=1.
\]
Thus no fixed odd replication count guarantees almost-sure convergence for all integrable endpoint power singularities, though increasing the count moves the sharp boundary toward \(\alpha=1\).

**Finite-sample moment contrast.** For every fixed \(n\ge1\) and real \(p>0\),
\[
\mathbb E|M_{n,r}|^p<\infty
\quad\Longleftrightarrow\quad
\left(p<\frac r\alpha\right)\ \text{or}\
\left(p=\frac r\alpha\ \text{and}\ \frac{r\beta}\alpha>1\right).
\]
In particular, with three replicas (\(r=2\)), every integrable pure-power case \(0<\alpha<1\), \(\beta=0\) has a finite-variance median at every fixed \(n\), yet the sequence has almost-sure unbounded spikes for \(\alpha\ge2/3\). This distinction is between fixed-sample moment existence and full-sequence strong consistency.

## Assumptions and scope

The samples are exactly uniform, independently randomized within equal-width intervals; separate complete designs at different \(n\) are independent. The replication count \(2r-1\) is fixed as \(n\to\infty\). Only one-dimensional positive power-log endpoint singularities with \(0<\alpha<1\), \(\beta\in\mathbb R\) are addressed. All limits refer to the full integer sequence \(n\to\infty\). Different cross-\(n\) couplings, deterministic nodes, unequal strata, or other integrand classes may have different almost-sure behavior. The integral is understood as a Lebesgue integral; \(f(0)\) is not sampled and need not be assigned a finite value.

## Proof

**1. Uniformly negligible contribution from every stratum except the first.** Write
\[
Q_n^{(\ell)}=Y_n^{(\ell)}+R_n^{(\ell)},\qquad
Y_n^{(\ell)}=n^{\alpha-1}(U_{n,0}^{(\ell)})^{-\alpha}
[\log(en/U_{n,0}^{(\ell)})]^{-\beta}.
\]
The function \(f\) is smooth and has derivative
\[
f'(x)=\frac{f(x)}x\left(-\alpha+\frac{\beta}{\log(e/x)}\right).
\]
The derivative changes sign at most once in \((0,1]\). Consequently its total variation on \([1/n,1]\) is at most \(f(1/n)+O_{\alpha,\beta}(1)\). On each stratum other than the first, a selected function value differs from that stratum's average by no more than its oscillation. Summing interval oscillations therefore gives, *uniformly over every realization* and \(\ell\),
\[
\left|R_n^{(\ell)}-\int_{1/n}^1f(x)\,dx\right|
\le\frac{\operatorname{Var}_{[1/n,1]}(f)}n
=O_{\alpha,\beta}\!\left(n^{\alpha-1}(\log n)^{-\beta}+n^{-1}\right)=o(1).
\]
Also \(\int_0^{1/n}f(x)\,dx=o(1)\), since \(\alpha<1\). Therefore there are deterministic \(d_n\downarrow0\) (take a nonincreasing majorant if necessary) such that
\[
\sup_{\ell,\omega}|R_n^{(\ell)}(\omega)-I|\le d_n.
\]
This bound is pathwise and uses no concentration inequality.

**2. Sharp first-panel excursion.** Put \(s=(1-\alpha)/\alpha>0\). Fix \(\varepsilon>0\), and set
\[
a_n(\varepsilon)=\left(\frac{\alpha^\beta}{\varepsilon}\right)^{1/\alpha}
 n^{-s}(\log n)^{-\beta/\alpha}.
\]
For any fixed \(c>0\), direct substitution into the preceding exact expression gives
\[
Y_n\bigl(ca_n(\varepsilon)\bigr)\longrightarrow\varepsilon c^{-\alpha},
\]
because \(\log(en/[ca_n(\varepsilon)])=(\log n)/\alpha+O_{\alpha,\beta,\varepsilon,c}(\log\log n)\). Moreover \(Y_n(u)\) decreases strictly in \(u\in(0,1)\) for sufficiently large \(n\), because \(\alpha-\beta/\log(en/u)>0\) there. Monotone inversion yields
\[
\Pr(Y_n>\varepsilon)\sim a_n(\varepsilon).
\]
The deterministic remainder bound in step 1 sandwiches \(\{Q_n>I+\varepsilon\}\) between \(\{Y_n>\varepsilon+d_n\}\) and \(\{Y_n>\varepsilon-d_n\}\). Applying the same inversion uniformly for threshold tending to \(\varepsilon\),
\[
q_n(\varepsilon):=\Pr(Q_n^{(\ell)}>I+\varepsilon)
\sim\left(\frac{\alpha^\beta}{\varepsilon}\right)^{1/\alpha}
 n^{-s}(\log n)^{-\beta/\alpha}.
\]
The quantity \(q_n(\varepsilon)\) tends to zero.

**3. Median tail and Borel--Cantelli.** For a median of \(2r-1\) independent continuous estimates, the event of exceeding a threshold requires at least \(r\) component estimates to exceed it. Thus, exactly,
\[
\Pr(M_{n,r}>I+\varepsilon)
=\sum_{j=r}^{2r-1}\binom{2r-1}{j}q_n(\varepsilon)^j[1-q_n(\varepsilon)]^{2r-1-j}.
\]
Since \(q_n\to0\), the leading term is \(\binom{2r-1}{r}q_n^r\); the displayed fixed-error limit follows. The convergence of its series over \(n\) is exactly that of
\[
\sum_{n\ge2}n^{-r(1-\alpha)/\alpha}(\log n)^{-r\beta/\alpha}.
\]
The integral test gives summability when \(r(1-\alpha)/\alpha>1\); divergence when it is smaller; at equality, summability precisely when \(r\beta/\alpha>1\). These are the claimed thresholds. In the summable cases, the first Borel--Cantelli lemma for each positive rational \(\varepsilon\), plus \(M_{n,r}\ge I-d_n\) for all draws, proves \(M_{n,r}\to I\) almost surely.

In the divergent cases, the complete row designs are independent for different \(n\), so the exceedance events are independent across \(n\). The second Borel--Cantelli lemma applied for every positive integer \(\varepsilon\) then proves \(\limsup_nM_{n,r}=+\infty\) almost surely. Simultaneously, the event that all \(2r-1\) first-stratum uniforms lie in \([1/2,1]\) has fixed positive probability \(2^{-(2r-1)}\) at each \(n\) and occurs infinitely often. On that event every \(Y_n^{(\ell)}\) tends uniformly to zero, so the median is \(I+o(1)\). Since \(M_{n,r}\ge I-d_n\) always, \(\liminf_nM_{n,r}=I\) almost surely, as asserted.

**4. Mean convergence and fixed-sample moments.** The individual estimator is unbiased because integrating each uniform stratum recovers that stratum's Lebesgue integral. Moreover,
\[
\mathbb E Y_n=\int_0^{1/n}f(x)\,dx\to0,
\]
so the uniform remainder bound gives \(\mathbb E|Q_n-I|\to0\). Since a median lies between the smallest and largest inputs,
\[
|M_{n,r}-I|\le\max_{\ell}|Q_n^{(\ell)}-I|
\le\sum_{\ell=1}^{2r-1}|Q_n^{(\ell)}-I|,
\]
which yields \(L^1\) convergence.

For fixed \(n\), the other strata have a bounded contribution, while inverse-tail substitution as the threshold \(t\to\infty\) gives
\[
\Pr(Q_n^{(\ell)}>t)\sim n^{-(1-\alpha)/\alpha}\alpha^{\beta/\alpha}
 t^{-1/\alpha}(\log t)^{-\beta/\alpha}.
\]
The same binomial-order-statistic calculation therefore yields
\[
\Pr(M_{n,r}>t)\sim\binom{2r-1}{r}
 n^{-r(1-\alpha)/\alpha}\alpha^{r\beta/\alpha}
 t^{-r/\alpha}(\log t)^{-r\beta/\alpha}.
\]
Because the median is nonnegative, the identity \(\mathbb E M^p=p\int_0^\infty t^{p-1}\Pr(M>t)\,dt\) and the ordinary power-log integral test give precisely the stated moment classification. This completes the proof.

## Verification

A standalone pure-Python program, `verify.py`, checks first-panel exceedance inversion, exact pure-power cases, binomial median probabilities, deterministic variation bounds, and rational representations of the critical exponents. Run `python3 verify.py`; the preserved result is in `verification_output.txt`. The program performs 889 successful checks with deterministic random seeds and no nonstandard dependencies. The passage to infinitely many \(n\), Borel--Cantelli, and the exact boundary are proved in the preceding argument rather than inferred from computation.

## Relationship to prior work

Hofstadler and Rudolf, *Consistency of randomized integration methods* (first released March 31, 2022), prove convergence in mean/probability for integrable functions and an almost-sure theorem for medians of independent Latin-hypercube estimates under a general sufficient integrability-and-replication condition (Proposition 3.4 and Example 3.6). Their conclusion is not the specific necessary-and-sufficient boundary in \((\alpha,\beta,r)\), nor an exact fixed-error tail constant or an almost-sure divergence statement. Their bound is intentionally general; this result is an exact benchmark for a restricted endpoint family, not a replacement for the general theorem.

Loh, *On Latin hypercube sampling* (1996, §3, Theorem 3 and Corollary 3), establishes strong-law rate and square-integrability results for Latin hypercubes. In the present family these cover part of the sufficient regime, in particular the single-estimate \(L^2\) region, but do not give the complete median-replication and power-log critical boundary. Goda and L'Ecuyer, *Construction-free median quasi-Monte Carlo rules* (2022, §§1–3), use medians of independently chosen lattice or polynomial-lattice rules to establish worst-case bounds in smooth function spaces; their sampling objects and function assumptions differ from independent interval jittering of unbounded endpoint functions.

The median binomial probability identity, variation bound, and Borel--Cantelli tools themselves are classical and are not claimed as inventions. The claim assessed here is their complete sharp quantitative synthesis for the specified singular quadrature design. Literature precedence beyond the inspected sources remains possible.

## Limitations

The strong-law failure depends on independently drawing complete quadrature designs across successive \(n\). It is not asserted for nested point sequences, common-random-number couplings, or deterministic refinement. Median estimators are generally biased, even though each underlying quadrature estimator is unbiased. The fixed-replication theorem does not prescribe optimal cost allocation or multivariate quadrature. Logarithmic endpoint corrections are for this explicit power-log family, not for arbitrary slowly varying functions. Independent publication precedence has not been established by a comprehensive historical search.

## References

1. J. Hofstadler and D. Rudolf, *Consistency of randomized integration methods*, arXiv:2203.17010 (first public submission 2022-03-31), Journal of Complexity 76 (2023), 101740. https://arxiv.org/abs/2203.17010
2. W.-L. Loh, *On Latin hypercube sampling*, Annals of Statistics 24 (1996), 2058–2080. DOI: 10.1214/aos/1069362310. https://doi.org/10.1214/aos/1069362310
3. T. Goda and P. L'Ecuyer, *Construction-Free Median Quasi-Monte Carlo Rules for Function Spaces with Unspecified Smoothness and General Weights*, SIAM J. Sci. Comput. 44 (2022), A2765–A2788. https://arxiv.org/abs/2201.09413
4. A. B. Owen and D. Rudolf, *A Strong Law of Large Numbers for Scrambled Net Integration*, SIAM Review 63 (2021), 360–372. https://doi.org/10.1137/20M1320535
