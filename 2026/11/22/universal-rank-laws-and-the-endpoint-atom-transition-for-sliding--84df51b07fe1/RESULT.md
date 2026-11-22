# Universal rank laws and the endpoint-atom transition for sliding order-statistic plateaus

## Finding
For independent continuous observations, moving order-statistic plateaus have a distribution-free, *exact finite-window* law for every rank. Fix \(w\ge2\) and rank \(1\le r\le w\), where rank one means the largest. Let \(Y_t^{(r)}\) be the rank-\(r\) largest value among \(X_t,\ldots,X_{t+w-1}\). Define a plateau start by \(E_0=\{Y_{-1}^{(r)}\ne Y_0^{(r)}\}\), and conditional on \(E_0\), let \(L_{w,r}\) be the number of consecutive values starting with \(Y_0^{(r)}\) that equal that value. All probabilities below are conditioned on \(E_0\) when they involve \(L_{w,r}\).

For integers \(1\le\ell\le w\), put \(N=w+\ell-1\) and
\[
S_{w,r}(\ell)=\frac{w-\ell+1}{N!}\sum_{k=0}^{r-1}\binom{\ell-1}{k}\binom{w-\ell}{r-1-k}(r-1+k)!(N-r-k)!.
\]
Binomial coefficients with invalid lower indices are zero, and set \(S_{w,r}(w+1)=0\). The complete lifetime law is
\[
\Pr(L_{w,r}\ge\ell)=\frac{S_{w,r}(\ell)-S_{w,r}(\ell+1)}{p_{w,r}},\qquad
p_{w,r}=\frac{2r(w-r+1)}{w(w+1)},\qquad 1\le\ell\le w.
\]
The expected lifetime is \(\mathbb E L_{w,r}=w(w+1)/[2r(w-r+1)]\).

For every fixed positive rank \(r\), with \(w\to\infty\),
\[
\Pr(L_{w,r}/w\ge t)\longrightarrow T_r(t):=\frac{(1-t)^{r-1}}{(1+t)^{r+1}},\qquad 0<t<1.
\]
For \(r=1\) the limit has density \(2/(1+t)^3\) for \(0<t<1\) and an atom of mass \(1/4\) at \(t=1\). For every fixed \(r\ge2\), the limit is continuous, with density \(2(r-t)(1-t)^{r-2}/(1+t)^{r+2}\) on \((0,1)\), and no endpoint atom. The exact finite-width endpoint mass is
\[
\Pr(L_{w,r}=w)=\frac{\binom{w-1}{r-1}(2r-2)!(2w-2r)!}{(2w-1)!p_{w,r}};
\]
for fixed rank it is asymptotic to \(C_r w^{1-r}\), where \(C_r=(2r-2)!/[(r-1)!2^{2r}r]\). In particular the rank-two limit has survival \((1-t)/(1+t)^3\) and no endpoint atom, unlike the running maximum.

## Assumptions and scope
There is a bi-infinite sequence of independent and identically distributed real random variables with a common continuous cumulative distribution function. Ties among finitely many observations occur with probability zero. A plateau is a maximal consecutive run of *exactly equal output values*, not an excursion above a threshold. Width \(w\) and rank \(r\) are arbitrary finite integers in the stated range; the asymptotic holds for a *fixed upper rank* as width grows. Reverse the observation order to obtain the identical law for any fixed rank from the bottom.

## Proof
**1. Repeated-rank event.** The event \(Y_0^{(r)}=\cdots=Y_{\ell-1}^{(r)}\) requires the common output to be the value of exactly one observation that belongs to all \(\ell\) windows. There are \(w-\ell+1\) eligible positions. Write its probability-transform value as \(u\in(0,1)\), so that other observations independently exceed it with probability \(1-u\). The \(\ell-1\) positions in the left-only region leave the moving window one at a time, while the right-only positions enter in matched order. To have exactly \(r-1\) exceeding observations at every time, each leaving/exiting pair must have matching exceedance indicators. Suppose \(k\) of these \(\ell-1\) pairs exceed the candidate, and \(h=r-1-k\) of the remaining \(w-\ell\) common positions exceed it. There are \(\binom{\ell-1}{k}\binom{w-\ell}{h}\) choices. Across all \(N=w+\ell-1\) observations, precisely \(h+2k=r-1+k\) values exceed the candidate. Integrating \(u^{N-1-(r-1+k)}(1-u)^{r-1+k}\) over \((0,1)\) gives \((N-r-k)!(r-1+k)!/N!\). Summing proves the formula for \(S_{w,r}(\ell)\). This is valid for every allowed rank, and \(S_{w,r}(1)=1\).

**2. Entry identity and the lifetime law.** An exact application of the preceding sum at \(\ell=2\) simplifies to \(1-S_{w,r}(2)=2r(w-r+1)/[w(w+1)]\). Stationarity shows
\[
\Pr(E_0,\ Y_0^{(r)}=\cdots=Y_{\ell-1}^{(r)})
=S_{w,r}(\ell)-S_{w,r}(\ell+1).
\]
The removed event in the difference is exactly equality from the preceding time \(-1\) through \(\ell-1\). Divide by \(p_{w,r}\) to obtain the conditional tail. Telescoping over \(\ell\) gives \(\mathbb E L_{w,r}=S_{w,r}(1)/p_{w,r}=1/p_{w,r}\). Equality cannot persist beyond \(w\) windows because their index intersection is empty and all inputs are distinct.

**3. Fixed-rank limit away from endpoints.** For \(r\) fixed and \(\ell/w\) in a compact subinterval of \((0,1)\), expand the *finite* factorial sum in powers of \(1/w\), treating \(\ell/w\) as a real argument. Its \(k\)-th summand is \(O(w^{-k})\), uniformly with smooth rational coefficient functions. Thus
\[
S_{w,r}(\ell)=s_r(\ell/w)+w^{-1}g_r(\ell/w)+O(w^{-2}),\quad
s_r(t)=\bigl((1-t)/(1+t)\bigr)^r,
\]
with the remainder uniform and smooth on the compact interval, and \(g_r\) a smooth rational function. Taking adjacent differences yields \(w[S_{w,r}(\ell)-S_{w,r}(\ell+1)]\to -s'_r(t)=2r(1-t)^{r-1}/(1+t)^{r+1}\). Because \(wp_{w,r}\to2r\), the stated conditional survival follows. This also yields the density on \((0,1)\).

**4. Endpoint analysis.** At \(\ell=w\), only the summand \(k=r-1\) survives, yielding the displayed exact mass. Stirling-free fixed-\(r\) products give the coefficient \(C_r\) and order \(w^{1-r}\). It tends to \(1/4\) when \(r=1\), and to zero when \(r\ge2\). Since \(T_r(0+)=1\) and \(T_r(1-)=0\) for \(r\ge2\), the latter limiting measures have no endpoint atoms. For \(r=1\), \(T_1(1-)=1/4\), agreeing with the finite exact mass. These facts complete weak convergence, including boundaries.

## Verification
Run the accompanying standalone Python checker using `python3 verify_rank_plateaus.py`. It uses exact rational arithmetic and enumerates all rank orderings at small widths; it also checks the finite entry formula, finite lifetime normalization, strict tail decrease, and endpoint identities at widths through 25. The checker passed 1,678 assertions. This finite verification does not prove the all-width or limiting claims; the proof above uses exact integration, stationarity, and rational asymptotics.

## Relationship to prior work
Bücher and Haufs (first posted 20 February 2025) treat the top-two statistics of sliding blocks and study asymptotic inference, with their Theorem 4.9 and proof in Appendix B.2 focused on estimator convergence and covariance. They do not state run-length laws for exactly repeated sliding order statistics. Raykov (2023) gives efficient deterministic algorithms for updating order statistics; his theorem is about running-time complexity, not the stochastic distribution of output plateaus. A previously available distribution-free result establishes the special rank-one, sliding-maximum duration law, including its quarter-mass endpoint; the rank-one instance is credited, not claimed as the new contribution. The complete all-ranks finite law and the discontinuous endpoint-atom hierarchy for every higher fixed rank are the mathematical contribution here.

## Limitations
Only continuous iid inputs and fixed sliding widths are covered. The fixed-rank limit does not cover ranks growing proportionally with the window width; neither serial dependence nor discrete ties are addressed. The result describes one typical plateau conditional on its entry and does not establish independence between successive plateau lengths or improvement of a particular statistical estimator. Potential implicit coverage in historical rank-pattern enumeration literature remains a priority risk; novelty was checked against accessible relevant sources, not certified independently.

## References
1. A. Bücher and E. Haufs, *Extreme Value Analysis based on Blockwise Top-Two Order Statistics*, arXiv:2502.15036, first posted 20 February 2025, https://arxiv.org/abs/2502.15036. Relevant Sections 4.2 and B.2.
2. P. Raykov, *An Optimal Algorithm for Sliding Window Order Statistics*, LIPIcs ICDT 2023, doi:10.4230/LIPIcs.ICDT.2023.5, https://doi.org/10.4230/LIPIcs.ICDT.2023.5.
3. *Exact plateau lifetimes and a quarter-atom limit for sliding sample maxima*, previously available rank-one result (2026), opaque identifier `704d29c1-2dc2-4668-a533-b867764fe7c2`.
