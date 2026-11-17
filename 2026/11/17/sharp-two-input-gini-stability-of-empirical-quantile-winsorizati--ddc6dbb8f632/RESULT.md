# Sharp two-input Gini stability of empirical-quantile Winsorization

## Finding
For integers \(n\ge2\) and \(1\le a<b\le n\), let \(W_{a,b}\) replace values below the sample \(a\)-th order statistic by that statistic and values above the sample \(b\)-th order statistic by that statistic. Let
\[
G_n(z)=\sum_{1\le i<j\le n}|z_i-z_j|.
\]
Then its **sharp two-input** seminorm Lipschitz coefficient is
\[
\boxed{L_{n,a,b}=\frac{\max\{a(n-a),(n-b+1)(b-1)\}}{n-1}.}
\]
This supremum is attained for every allowed \((n,a,b)\) by an arbitrarily small perturbation of one coordinate of a strictly ordered data vector. Although \(G_n(W_{a,b}x)\le G_n(x)\) for each individual input, \(L_{n,a,b}>1\) except precisely for \((a,b)=(1,n),(1,2),(n-1,n)\) (allowing repetitions of these pairs in the smallest dimensions).

For symmetric Winsorization trimming \(t\ge0\) observations from each tail with \(2t+2\le n\), the exact constant simplifies to
\[
L_{n,t+1,n-t}=\frac{(t+1)(n-t-1)}{n-1}.
\]
Consequently, if \(t/n\to\alpha\in(0,1/2)\), then \(L_{n,t+1,n-t}/n\to\alpha(1-\alpha)\). Thus a fixed positive trimming fraction gives linear growth in the worst-case perturbation modulus despite decreasing dispersion on each input.

## Assumptions and scope
All inputs are real \(n\)-vectors, the ranks are integers, and order statistics use weak increasing order, so ties are unambiguously defined. Set
\[
(W_{a,b}x)_i=\min\{\max\{x_i,x_{(a)}\},x_{(b)}\},\qquad
G_n(x)=\sum_{i<j}|x_i-x_j|.
\]
The quotient is restricted to inputs with \(G_n(x-y)>0\), since \(G_n\) vanishes on constants. Translation equivariance \(W_{a,b}(x+c\mathbf1)=W_{a,b}(x)+c\mathbf1\) guarantees that constant differences also map to constant differences. The Gini mean difference normalized by \(2/[n(n-1)]\) gives the identical Lipschitz ratio.

## Proof
**1. A replication lemma.** Consider a deterministic map \(r:\{1,\ldots,n\}\to\{1,\ldots,n\}\) and its linear coordinate-copying operator \((B_r z)_i=z_{r(i)}\). Define \(m_j=|r^{-1}(j)|\), so \(\sum_jm_j=n\). We claim
\[
\|B_r\|_{G_n\to G_n}=\frac{1}{n-1}\max_jm_j(n-m_j).
\]
For an indicator \(\mathbf1_S\) of a nonempty proper set \(S\), write \(s=|S|\) and \(u=\sum_{j\in S}m_j\). The input and output Gini variations are respectively \(s(n-s)\) and \(u(n-u)\). Define \(\phi(v)=v(n-v)\). We show
\[
\frac{\phi(u)}{s(n-s)}\le\frac{\max_j\phi(m_j)}{n-1}.
\]
If any multiplicity \(m_j\ge n/2\), take whichever of \(S\) and its complement contains that index. The corresponding mass \(u'\) is at least \(m_j\), hence \(\phi(u')\le\phi(m_j)\), as \(\phi\) decreases on \([n/2,n]\). Also \(s(n-s)\ge n-1\), proving the desired inequality.

Otherwise every \(m_j<n/2\). Replace \(S\) by its complement if needed so \(u\ge s\), possible since the two masses total \(n\) and the two cardinalities total \(n\). Some \(j\in S\) then has \(m_j\ge u/s\), so monotonicity of \(\phi\) on \([0,n/2]\) yields \(\phi(m_j)\ge\phi(u/s)\). Direct multiplication gives
\[
(n-u/s)(n-s)-(n-u)(n-1)=n(s-1)(u/s-1)\ge0,
\]
so \(\phi(u/s)/(n-1)\ge\phi(u)/[s(n-s)]\). This proves the indicator inequality.

The discrete coarea identity \(|v_i-v_j|=\int_{\mathbb R}|\mathbf1_{v_i>t}-\mathbf1_{v_j>t}|\,dt\) holds for every real vector. Because copying coordinates commutes with thresholding, integration extends the indicator inequality to every \(z\). Conversely, taking \(z=\mathbf1_{\{j\}}\) gives ratio \(m_j(n-m_j)/(n-1)\), attaining the maximum. This establishes the lemma, including the constant-output case.

**2. Local linearization of Winsorization.** On every open strict-order chamber \(x_{\pi(1)}<\cdots<x_{\pi(n)}\), the map \(W_{a,b}\) is linear: each of the first \(a\) output coordinates copies the \(a\)-th ordered input, each of the last \(n-b+1\) copies the \(b\)-th input, and each intermediate coordinate copies itself. The nonzero multiplicities are \(a\), \(n-b+1\), and \(b-a-1\) copies of the value \(1\). (If a multiplicity coincides with the other anchor only when \(a=b\), which is excluded.) The replication lemma gives the exact chamber norm
\[
\max\left\{\frac{a(n-a)}{n-1},\frac{(n-b+1)(b-1)}{n-1}\right\}.
\]
The singleton terms of multiplicity \(1\), when present, have ratio \(1\). They do not enlarge this maximum since \(a(n-a)\ge n-1\) and \((n-b+1)(b-1)\ge n-1\) for the permitted ranks.

**3. Global upper bound.** Winsorization is continuous and piecewise linear across the finite strict-order-chamber decomposition. For any input segment that crosses chamber boundaries generically, the output difference is the integral of its chamberwise linear derivatives. The seminorm triangle inequality and the preceding uniform bound yield \(G_n(W_{a,b}x-W_{a,b}y)\le L_{n,a,b}G_n(x-y)\). Approximation by generic segments extends this to all ties; if the input difference is constant, translation equivariance covers the zero-denominator case.

**4. Exact attainment.** Choose any base vector with strictly increasing, well-separated coordinates. If the first branch is maximal, perturb only the coordinate of rank \(a\) by a sufficiently small positive amount; otherwise perturb rank \(b\). In the same chamber, the output difference is the indicator of exactly \(a\) or \(n-b+1\) coordinates times the perturbation size, whereas the input difference is a singleton. The resulting quotient equals the corresponding branch, so the global upper bound is attained.

**5. Nonexpansivity and one-input contrast.** For integers \(1\le m\le n-1\), \(m(n-m)\ge n-1\), with equality exactly for \(m=1\) or \(m=n-1\). Because the two anchor multiplicities sum to at most \(n\), the only rank pairs yielding \(L_{n,a,b}=1\) are those listed in the finding. Independently, on a fixed dataset \(x\), clipping by its two common scalar thresholds is a \(1\)-Lipschitz scalar map, so \(|(W_{a,b}x)_i-(W_{a,b}x)_j|\le|x_i-x_j|\) for all coordinate pairs; summing proves \(G_n(W_{a,b}x)\le G_n(x)\).

## Verification
The accompanying standalone exact-rational checker enumerates every possible integer multiplicity vector with total \(n\) for \(2\le n\le7\), all nontrivial indicator cuts, and both sides of the replication lemma. It also checks every rank pair for \(2\le n\le10\), including exact strict-chamber attaining pairs, and 10,800 independent rational two-input inequalities. Successful diagnostics are printed by running `python winsor_gini_check.py` from the extracted package. Finite tests only corroborate the proof above; the proof, not these tests, establishes all dimensions and rank pairs.

## Relationship to prior work
Winsorization and trimming are classical robust-statistics procedures. Dey, Dhara, Karmakar, and Sengupta (arXiv:1211.4262v1, 2012) analyze Winsorized dispersion in control charts. Bieniek's 2014 open-access trimean paper analyzes population-bias bounds for order-statistic estimators. Bieniek's separately indexed 2016 work concerns sharp bias bounds for Winsorized means. Those questions are distributional/estimator-bias questions rather than the deterministic two-input stability of the full sample-to-sample Winsorization transformation in pairwise variation. Published work on sorting stability or Gini statistics does not directly supply the coordinate-replication lemma above. An earlier unindexed equivalent formulation is not excluded.

## Limitations
The result concerns unweighted complete-graph pairwise absolute-difference variation and rank-threshold Winsorization, not arbitrary weighted graph variation, quantile interpolation conventions, random thresholds or multivariate depth-based Winsorization. Exact individual-signal contraction does not imply pairwise contraction.

## References
Dey, K. K., Dhara, K., Karmakar, B., Sengupta, S., *Univariate and data-depth based multivariate control charts using trimmed mean and winsorized standard deviation*, arXiv:1211.4262v1, 18 November 2012. Full text: https://arxiv.org/html/1211.4262v1.

Bieniek, M., *Sharp bounds on the bias of trimean*, Statistical Papers, online 31 December 2014, DOI:10.1007/s00362-014-0641-3. Full text: https://link.springer.com/article/10.1007/s00362-014-0641-3.

Bieniek, M., *Comparison of the bias of trimmed and Winsorized means*, Communications in Statistics—Theory and Methods, accepted manuscript online 21 January 2016, DOI:10.1080/03610926.2014.963620. Full text was not accessible in the literature comparison; published abstract and metadata were checked.
