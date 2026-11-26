# Sharp endpoint asymmetry and stochastic shift of a progressively censored exponentiality statistic

## Finding

Let \(0\le r<m\le n\) be integers with \(d=m-r\ge2\). In a general progressively Type-II censored sample of \(n\) independent exponential lifetimes of common scale \(\sigma>0\), the first \(r\) failure times are not observed and there are no removals at those failures. After each observed failure \(i=r+1,\ldots,m\), remove exactly \(R_i\ge0\) survivors uniformly without access to their residual lifetimes, with deterministic \(R_i\) and \(\sum_iR_i=n-m\). For the observed failure times define
\[
S_{r+1}=(n-r)X_{r+1},\qquad
S_i=\left(n-i+1-\sum_{\ell=r+1}^{i-1}R_\ell\right)(X_i-X_{i-1})\quad(i>r+1).
\]
Put \(w_j=1-j/(d-1)\) for \(0\le j<d\), \(c_\ell=(n-r)/(n-\ell)\) for \(0\le\ell\le r\), and
\[
 T=\frac{\sum_{j=0}^{d-1}w_j S_{r+1+j}}{\sum_{j=0}^{d-1}S_{r+1+j}}.
\]
This is the Qin–Yu–Gui normalized spacing statistic. Write \(h_j(c)\) for the complete homogeneous symmetric polynomial defined by \(\prod_{\ell=0}^r(1-c_\ell z)^{-1}=\sum_{j\ge0} h_j(c)z^j\).

At fixed \((n,m,r)\), as \(t\downarrow0\), its two endpoint probabilities satisfy
\[
\begin{aligned}
 \Pr(T\le t)&\sim C_L t^{m-1},&
 C_L&=\frac{n!}{(n-r-1)!(n-r)^{r+1}}\frac{(d-1)^{d-2}}{(d-2)!},\\
 \Pr(T>1-t)&\sim C_R t^{d-1},&
 C_R&=\frac{(d-1)^{d-1}}{(d-1)!}\,h_{d-1}(c).
\end{aligned}
\]
For \(r>0\), the left endpoint probability at distance \(t\) is smaller in order than the right by a factor asymptotic to \((C_L/C_R)t^r\). Also for \(r>0\), the CDF lies strictly below the \(r=0\) benchmark at **every** interior threshold when the benchmark uses the same observed count \(d\). The benchmark is the average of \(d-1\) independent \(\operatorname{Unif}(0,1)\) variables. The scale and the allocation of removals do not enter these results. The claim concerns the sharp paired endpoint behavior and the strict comparison, not the availability of an exact CDF or a new general formula for linear forms of exponential variables.

## Proof

Before and including failure \(r+1\), ordinary exponential increments are independent, with rates \((n-\ell)/\sigma\) at failures \(\ell+1\), \(0\le\ell\le r\). After observation begins, the residual exponential lifetimes of the surviving retained units are independent with the original scale, by lack of memory and noninformative removals. The next failure increment, multiplied by its risk set size, is again exponential with scale \(\sigma\), with conditional law independent of earlier increments. Thus on dividing by \(\sigma\) the normalized spacings have the joint law of
\[
(H,G_1,\ldots,G_{d-1}),\qquad H=\sum_{\ell=0}^r c_\ell E_\ell,
\]
where all the \(E_\ell,G_j\) are independent unit exponentials. This also verifies scale and removal-allocation invariance.

**Left endpoint.** If \(0<t<1/(d-1)\), the only negative coefficient in the contrast for \(T\le t\) is the last spacing with weight zero. In this event \(t G_{d-1}\ge(1-t)H+\sum_{j=1}^{d-2}(w_j-t)G_j\). Conditioning on the right-hand side, the survivor of the unit exponential gives exactly
\[
\Pr(T\le t)=\prod_{\ell=0}^r\frac{t}{t+(1-t)c_\ell}\prod_{j=1}^{d-2}\frac{t}{w_j}.
\]
There are \(m-1\) vanishing factors; \(\prod c_\ell^{-1}=n!/[(n-r-1)!(n-r)^{r+1}]\) and \(\prod_{j=1}^{d-2}w_j=(d-2)!/(d-1)^{d-2}\). This includes the empty second product when \(d=2\).

**Right endpoint.** Put \(k=d-1\) and \(a_j(t)=j/k-t\) for \(1\le j\le k\). The event \(T>1-t\) is \(\sum_{j=1}^k a_j(t)G_j<tH\). For fixed \(H=s\) and \(0<t<1/(2k)\), make the change of variables \(G_j=ts u_j/a_j(t)\) in the probability integral over \(u_j\ge0,\sum_j u_j<1\). Dividing by \(t^k\) gives
\[
\frac{s^k}{\prod_j a_j(t)}\int_{\sum u_j<1,\ u_j\ge0}\exp\left(-ts\sum_j u_j/a_j(t)\right)\,du.
\]
The integral tends to the simplex volume \(1/k!\); the whole quantity is dominated by a fixed constant times \(s^k\), using \(a_j(t)\ge j/(2k)\). Since \(\mathbb EH^k=k!h_k(c)\), the limit can be integrated and gives \(C_R\). The powers and positive constants yield the ratio claim. Distinct powers exclude symmetry about the only possible center, \(1/2\), because the support endpoints are 0 and 1 (positive densities of the spacings permit approaching both extremes).

**Strict shift.** For \(r>0\), couple \(H=E_r+Z\) to the no-initial-missing-failure first spacing \(E_r\), where \(Z=\sum_{\ell<r}c_\ell E_\ell>0\) independently of \(E_r,G\). With the other gaps held fixed, the ratio is strictly increasing in the first gap. To obtain strict CDF inequality at an arbitrary \(u\in(0,1)\), take an open set of \(G\)-values where \(\sum_{j=1}^{d-1} w_jG_j/\sum_j G_j<u\) (for instance, the zero-weight last gap can dominate). For every such \(G\) the first-gap threshold \(s_*=(u\sum_jG_j-\sum_j w_jG_j)/(1-u)\) is positive. The event \(E_r<s_*<E_r+Z\) has positive conditional probability, proving strict dominance at \(u\). In the benchmark, the \(d\) independent unit exponentials normalized by their sum are uniform simplex spacings; summation by parts makes the weighted ratio equal to the average of the \(d-1\) cumulative spacings, which have the law of ordered independent uniforms. Their average is the same as the unordered average in distribution.

## Exact CDF as a classical specialization

For clarity, the full CDF follows directly from the classical simplex halfspace-volume formula in Lasserre [2, Theorem 2.2, Eq. (2.2)], also covered computationally by Huffer and Lin [3]. Divide all \(m\) independent unit exponentials in the spacing representation by their sum to get a uniform simplex vector. The halfspace for \(T\le t\) has one coefficient per raw exponential, namely
\[
 (1-t)c_0,\ldots,(1-t)c_r,\quad w_1-t,\ldots,w_{d-1}-t.
\]
For affine values \(a_i\) at the simplex vertices, the volume fraction of the lower halfspace at zero is \(\sum_{i:a_i<0}(-a_i)^{m-1}/\prod_{j\ne i}(a_j-a_i)\) for distinct values (shift and scale to the convention of [2]). For the present contrast the negative values are distinct. Coinciding nonnegative values and zero coefficients are handled by continuity, since the uniform simplex boundary hyperplane is null for interior \(t\). In particular, defining \(N_t=\{j\ge1:w_j<t\}\), \(P_t=\{j\ge1:w_j>t\}\), and \(b_j=1/(t-w_j)\) for \(j\in N_t\), the halfspace formula gives
\[
 \Pr(T\le t)=\sum_{j\in N_t}
 \left(\prod_{h\in N_t\setminus\{j\}}\frac{t-w_j}{w_h-w_j}\right)
 \left(\prod_{\ell=0}^r\frac{1}{1+b_j(1-t)c_\ell}\right)
 \left(\prod_{h\in P_t}\frac{1}{1+b_j(w_h-t)}\right).
\]
At an interior knot the zero value contributes no summand or factor. The CDF is zero for \(t\le0\) and one for \(t\ge1\). For instance, for \((n,m,r)=(5,3,1)\) it is \(5t^2/(4+t)\) for \(0<t<1\), and for \((10,6,2)\) the endpoint constants are \(405/64\) and \(660241/20250\). Ordinary floating-point evaluation of the signed sum can lose precision. The exact CDF is included for reproducibility, not claimed as a new finite-calibration theorem. The two endpoint constants describe how to set extreme one-sided thresholds; they apply as the respective probability levels tend to zero at fixed sample size, not for growing samples or for alternatives.

## References

1. X. Qin, J. Yu and W. Gui, *Goodness-of-fit test for exponentiality based on spacings for general progressive Type-II censored data*, J. Appl. Stat. 49 (2022), 599–620, first online 2020. https://doi.org/10.1080/02664763.2020.1821613
2. J. B. Lasserre, *Volume of slices and sections of the simplex in closed form*, Theorem 2.2, https://arxiv.org/abs/1412.4617; https://doi.org/10.1007/s11590-015-0898-z.
3. F. W. Huffer and C.-T. Lin, *Computing the joint distribution of general linear combinations of spacings or exponential variates*, Statist. Sinica 11 (2001), 1141–1157, https://www3.stat.sinica.edu.tw/statistica/oldpdf/A11n411.pdf.
