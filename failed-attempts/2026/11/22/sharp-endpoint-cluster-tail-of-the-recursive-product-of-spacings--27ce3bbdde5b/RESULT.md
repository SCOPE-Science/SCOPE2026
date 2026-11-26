# Sharp endpoint-cluster tail of the recursive product of spacings

## Finding

Let \(n\geq 1\) be a fixed integer, and let \(U_1,\ldots,U_n\) be independent uniform observations on \((0,1)\). The unnormalized recursive product-of-spacings statistic \(R_n\) is exactly that of Eller and Shtembari [1], including the normalization at every recursive level specified below. Put
\[
\alpha_n=\frac{2}{n+1},\qquad b_n=\sum_{j=1}^{n+1}j\log j,\qquad K_n=\frac{n(n+1)}{2}.
\]
For \(v\) in the open \((n-1)\)-simplex \(\Delta_{n-1}=\{v_i>0:\sum_{i=1}^n v_i=1\}\), define the binomial adjacent-window forms
\[
L_{j,i}(v)=\sum_{h=0}^{j}\binom{j}{h}v_{i+h},\quad 0\leq j\leq n-1,\quad1\leq i\leq n-j,
\]
and the finite, strictly positive constant
\[
C_n=2(n-1)!\int_{\Delta_{n-1}}
\prod_{j=0}^{n-1}\prod_{i=1}^{n-j}
L_{j,i}(v)^{-\alpha_n}\,dv_1\cdots dv_{n-1}.
\]
For \(n=1\), the integral over the zero-dimensional simplex has value one.

**Theorem (fixed-sample extreme-null tail).** For every fixed integer \(n\geq1\),
\[
\boxed{\Pr(R_n>t)\sim C_n e^{-\alpha_n t}\qquad(t\to\infty).}
\]
The moment-generating function has the exact finiteness threshold
\[
\boxed{\mathbb E e^{qR_n}<\infty\quad\Longleftrightarrow\quad q<\alpha_n,\qquad q\in\mathbb R.}
\]
For the published bounded statistic \(R_n^*=b_n/R_n\), equivalently,
\[
\boxed{\Pr(R_n^*<x)\sim C_n\exp\!\left(-\frac{2b_n}{(n+1)x}\right)\qquad(x\downarrow0).}
\]
The two endpoint vertices of the spacing simplex contribute equally to the constant; all other boundary configurations are lower order. For \(n=2\), the coefficient is explicit:
\[
\boxed{C_2=2B(1/3,1/3)=\frac{2\Gamma(1/3)^2}{\Gamma(2/3)}=10.5998325017127\ldots.}
\]

## Assumptions and scope

The null cumulative distribution function is fully specified and continuous, so its probability integral transform is uniform. Write the ordered observations as \(U_{(1)}<\cdots<U_{(n)}\), put \(U_{(0)}=0\), \(U_{(n+1)}=1\), and let \(S_i=U_{(i)}-U_{(i-1)}\), \(1\leq i\leq n+1\). Thus \(S\) has the \(\operatorname{Dirichlet}(1,\ldots,1)\) law, with density \(n!\) on its simplex.

Starting with \(S^{(0)}=S\), repeatedly replace a vector by its adjacent pairwise sums normalized to total one, stopping at length one. Define \(R_n\) as the sum, over the levels of lengths \(n+1,n,\ldots,2\), of the negative logarithms of their entries. The omitted final length-one level contributes zero. These conventions exactly match equations (2.1)–(2.4) and Algorithm 1 of [1]. The minimum \(b_n\) and the bounded score \(R_n^*=b_n/R_n\) are those of equations (2.5)–(2.6) of [1].

All limits here hold with \(n\) fixed. There is no claim of uniformity as \(n\to\infty\), no fitted-null parameter adjustment, and no quantitative finite-threshold approximation error.

## Proof

**1. Exact binomial-window representation.** Let \(m=n+1\). Iterating the adjacent-sum map and then normalizing is the same as applying the unnormalized \(j\)-fold map once and dividing by its total:
\[
A_{j,i}(s)=\sum_{h=0}^{j}\binom{j}{h}s_{i+h},\qquad
Z_j(s)=\sum_{i=1}^{m-j}A_{j,i}(s),\qquad
S^{(j)}_i=\frac{A_{j,i}(S)}{Z_j(S)}.
\]
Here \(0\leq j\leq m-2\), and \(Z_0=1\). Therefore
\[
R_n=-\sum_{j=0}^{m-2}\sum_{i=1}^{m-j}\log A_{j,i}(S)
+\sum_{j=0}^{m-2}(m-j)\log Z_j(S).
\]
Every coefficient of \(Z_j\) as a linear form in the coordinates is between \(1\) and \(2^j\). Moreover each \(A_{j,i}\) lies between the plain sum of the \(j+1\) coordinates in its window and \(2^j\) times that sum. Hence \(\exp(R_n)\) is, up to two positive constants depending only on \(n\), the product of reciprocal sums of coordinates over all **proper nonempty consecutive intervals** of \(\{1,\ldots,m\}\).

**2. A simplex integrability lemma.** For a collection \(\mathcal I\) of proper consecutive intervals, write
\[
F_q(s)=\prod_{I\in\mathcal I}\left(\sum_{i\in I}s_i\right)^{-q}.
\]
For the full collection of all proper nonempty intervals, \(F_q\) is integrable on the uniform \((m-1)\)-simplex whenever \(q<2/m\). To see this for \(q\geq0\), partition the simplex into the finitely many sectors in which \(s_{\pi(1)}\leq\cdots\leq s_{\pi(m)}\). Put \(E_j=\{\pi(1),\ldots,\pi(j)\}\) and \(k_j=\#\{I\in\mathcal I:I\subseteq E_j\}\). If the consecutive blocks in \(E_j\) have lengths \(b_1,\ldots,b_r\), then
\[
k_j=\sum_{a=1}^{r}\frac{b_a(b_a+1)}2\leq\frac{j(j+1)}2.
\]
Every interval sum exceeds its largest coordinate. Thus the integrand is bounded by the monomial assigning to \(s_{\pi(j)}\) the exponent \(-q(k_j-k_{j-1})\). Introduce \(x_j=s_{\pi(j)}/s_{\pi(j+1)}\) for \(j<m\). Its simplex Jacobian, up to a denominator bounded above and below by positive constants, is \(\prod_{j=1}^{m-1}x_j^{j-1}\). The monomial therefore has an integrable upper bound proportional to
\[
\prod_{j=1}^{m-1}x_j^{j-1-qk_j}.
\]
Because \(q<2/m\), every exponent exceeds \(-1\). Negative \(q\) cause no difficulty because each normalized spacing is at most one. Conversely, at \(q\geq2/m\), consider a neighborhood of either endpoint vertex with its other \(m-1\) coordinates at common scale \(r\). Exactly \(K_n=m(m-1)/2\) interval forms vanish linearly in \(r\), and the radial volume element is of order \(r^{m-2}dr\). The integral then includes \(\int_0 r^{m-2-qK_n}dr\), which diverges at and above \(q=2/m\). By the bounded-ratio representation in step 1, this proves the asserted exact exponential-moment threshold.

**3. Endpoint scaling and constant.** Near the right endpoint vertex \(e_m\), write
\[
S_i=rv_i\ (1\leq i\leq n),\qquad S_m=1-r,
\qquad v\in\Delta_{n-1},\quad 0<r<\delta.
\]
The joint simplex density times the Jacobian is \(n!r^{n-1}\,dr\,dv\). At recursive level \(j\), the \(n-j\) entries not touching the final coordinate are exactly \(rL_{j,i}(v)\). The remaining entry tends to one. All normalizers \(Z_j\) also tend to one, uniformly in \(v\), because precisely one binomial window contains the final coordinate, with coefficient one. Consequently, uniformly in \(v\),
\[
R_n=K_n\log(1/r)+H_n(v)+O_n(r),\qquad
H_n(v)=-\sum_{j=0}^{n-1}\sum_{i=1}^{n-j}\log L_{j,i}(v).
\]
The function \(e^{\alpha_nH_n(v)}\) is integrable on \(\Delta_{n-1}\): its binomial forms are comparable to ordinary interval sums, and step 2 applies to the smaller \(n\)-coordinate simplex since \(2/(n+1)<2/n\).

For every fixed interior \(v\), the radial measure of the event \(R_n>t\), multiplied by \(e^{\alpha_nt}\), tends to \(e^{\alpha_nH_n(v)}/n\). The uniform \(O_n(r)\) estimate bounds that rescaled radial integral by a fixed multiple of \(e^{\alpha_nH_n(v)}\); dominated convergence therefore yields the right-vertex contribution
\[
(n-1)!e^{-\alpha_nt}\int_{\Delta_{n-1}}e^{\alpha_nH_n(v)}dv\,(1+o(1)).
\]
Reversing the spacings yields the identical left-vertex contribution.

**4. Other boundary strata are smaller.** Fix disjoint small neighborhoods of the two endpoint vertices. On their complement, every possible set of coordinates simultaneously approaching zero is either of size at most \(m-2\), or is the complement of an interior coordinate. For each such set of size \(j\), the number \(k\) of contained consecutive intervals satisfies the strict inequality \((2/m)k<j\). Finiteness of the collection of sets permits a fixed \(q>2/m\) for which \(qk<j\) for every such boundary stratum. The sector-variable bound of step 2, now restricted to this complement, proves \(\mathbb E[e^{qR_n};\ \text{outside the endpoint neighborhoods}]<\infty\). Markov's inequality makes its tail \(O(e^{-qt})=o(e^{-\alpha_nt})\). Adding both endpoint contributions proves the asserted \(C_n\) and the full asymptotic equivalent.

**5. Bounded statistic and explicit example.** Because \(R_n^*=b_n/R_n\) and \(b_n>0\), the lower-tail claim follows by substituting \(t=b_n/x\). For \(n=2\), the angular variable is \(v=(u,1-u)\). The three small-window factors are \(u\), \(1-u\), and \(u+(1-u)=1\). Their integral is \(\int_0^1[u(1-u)]^{-2/3}du=B(1/3,1/3)\), proving the explicit constant. For \(n=1\), the result reduces to the small-score expansion of the exact distribution given in [1, equation (3.1)].

## Verification

The bundled `check_rps.py` can be run using Python 3 and the standard library. It compares the published recursive normalization with the binomial-window representation using exact rational arithmetic over 301 deterministic configurations, verifies the interval-count inequality and the exclusive endpoint maximizers over 8,166 finite subset configurations, checks the explicit three-spacing product in 100 additional configurations, and evaluates the gamma-function formula for \(C_2\). All 8,568 assertions passed. These finite checks support the algebra and boundary combinatorics; they are not substitutes for the all-\(n\) analytic proof above.

A separate direct null Monte Carlo calculation for \(n=2\) used 25,000,000 independent Dirichlet samples and the exact three-spacing product. It gave \(\Pr(e^{-R_2}<10^{-8})/(10^{-8})^{2/3}\approx10.9704\), approaching the proved limiting constant \(10.5998\ldots\). This is a diagnostic only; stochastic error and slow asymptotic convergence prevent treating the estimate as proof.

## Relationship to prior work

Eller and Shtembari [1] introduced the recursively normalized statistic, derived an exact CDF only for \(n=1\), and used simulation-based spline calibration for larger samples; their stated numerical quantile range extends down to roughly \(10^{-7}\). Equations (2.1)–(2.6), Algorithm 1, and sections 3 and 7 were checked in the full open preprint. The present result concerns an exact fixed-sample boundary equivalent, its positive leading coefficient, and exponential-moment threshold, none supplied by that calibration.

Shtembari and Caldwell [2] discuss extensions of goodness-of-fit tests to multivariate models and a different product-of-complementary-spacings statistic. Their null constructions do not entail this endpoint-cluster asymptotic for the recursive adjacent-sum statistic. The result also uses standard Dirichlet spacing geometry and elementary Mellin-type boundary power counting; no claim is made to the originality of those general tools.

## Limitations

The asymptotic is for each fixed \(n\), as \(t\to\infty\) or \(x\downarrow0\). No error bound, finite-\(x\) cutoff, or interchange of the sample-size and tail limits has been established. The integral for \(C_n\) is exact and finite but is not evaluated in elementary form for general \(n\). The null must be completely specified and continuous; fitted parameters, discretization, or dependent observations may change the law. Searches cannot establish universal historical priority, and independent validation has not been undertaken.

## References

[1] P. Eller and L. Shtembari, *A goodness-of-fit test based on a recursive product of spacings*, arXiv:2111.02252 (first public 3 November 2021), Journal of Instrumentation **18** (2023) P03048. https://arxiv.org/pdf/2111.02252 ; https://doi.org/10.1088/1748-0221/18/03/P03048

[2] L. Shtembari and A. Caldwell, *Goodness-of-fit tests for arbitrary multivariate models*, Physical Review D **108** (2023) 123006. https://doi.org/10.1103/PhysRevD.108.123006
