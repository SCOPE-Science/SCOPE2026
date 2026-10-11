# A privacy–utility invariant and sharp heterogeneous-budget frontier for product Gaussian private e-values
## Finding
Let \(K\ge 1\). For mutually independent, disjoint data blocks, let \(E_k>0\) be valid e-values for component nulls and suppose \(\log E_k\) has finite positive global sensitivity \(\Delta_k\). Give block \(k\) its own canonical Gaussian differential-privacy parameter \(\mu_k>0\), independently drawing
\[
\xi_k\sim N\!\left(\frac{\Delta_k^2}{2\mu_k^2},\frac{\Delta_k^2}{\mu_k^2}\right),
\qquad
E_k^{\mathrm{DP}}=E_k e^{-\xi_k}.
\]
Publish only the product
\[
E_{\mathrm{prod}}^{\mathrm{DP}}=\prod_{k=1}^K E_k^{\mathrm{DP}}.
\]
Define
\[
V=\sum_{k=1}^K\frac{\Delta_k^2}{\mu_k^2},
\qquad
\Delta_{\max}=\max_{1\le k\le K}\Delta_k.
\]
Then the product is a valid e-value for the intersection null, its total injected log-noise is exactly \(N(V/2,V)\), and the sharp Gaussian-DP parameter of the published product is
\[
\mu_{\mathrm{prod}}=\frac{\Delta_{\max}}{\sqrt V}.
\]
Consequently the expected privacy-induced loss in log evidence, \(L=\mathbb E[\sum_k\xi_k]=V/2\), obeys the allocation-invariant identity
\[
2L\mu_{\mathrm{prod}}^2=\Delta_{\max}^2.
\]
Thus heterogeneous allocations \((\mu_1,\ldots,\mu_K)\) with the same \(V\) give the same conditional law of the released product given the unperturbed product and the same sharp product-level privacy parameter.

There is also a complete design frontier under heterogeneous local privacy caps. If \(0<\mu_k\le b_k\) for every block and the released product must satisfy \(\mu_{\mathrm{prod}}\le \bar\mu\), put
\[
V_0=\sum_{k=1}^K\frac{\Delta_k^2}{b_k^2},
\qquad
T=\frac{\Delta_{\max}^2}{\bar\mu^2}.
\]
The minimum achievable aggregate log-noise variance and minimum expected log-evidence loss are exactly
\[
V^*=\max\{V_0,T\},
\qquad
L^*=\frac{V^*}{2}.
\]
If \(V_0\ge T\), the optimum is attained by \(\mu_k=b_k\) for all \(k\). If \(V_0<T\), choose any index \(j\) and keep \(\mu_k=b_k\) for \(k\ne j\), while setting
\[
\frac{1}{\mu_j^2}=\frac{1}{b_j^2}+\frac{T-V_0}{\Delta_j^2}.
\]
This attains \(V=T\) and hence the frontier exactly.

## Assumptions and scope
The data blocks are mutually independent under the intersection null and disjoint at the individual-record level, so one neighboring global dataset changes at most one block. Each \(E_k\) is strictly positive and its log sensitivity \(\Delta_k\) is a finite positive supremum. The Gaussian perturbations are mutually independent and independent of the data. The parameters \(\mu_k\), the local caps \(b_k\), and the aggregate cap \(\bar\mu\) are fixed independently of the realized private data.

The privacy statement concerns the single published scalar product. It is not a guarantee for a transcript that separately releases the factors, their noises, or other block-level information. Such a richer release requires its own privacy accounting.

## Proof
For validity, the canonical centering gives
\[
\mathbb E[e^{-\xi_k}]
=\exp\!\left(-\frac{\Delta_k^2}{2\mu_k^2}+\frac12\frac{\Delta_k^2}{\mu_k^2}\right)=1.
\]
Independence of blocks and perturbations therefore yields, under the intersection null,
\[
\mathbb E[E_{\mathrm{prod}}^{\mathrm{DP}}]
=\prod_{k=1}^K \mathbb E[E_k]\,\mathbb E[e^{-\xi_k}]
\le 1.
\]
Hence the product is a valid e-value.

Let \(Z=\sum_k\xi_k\). Sums of the independent Gaussian perturbations give
\[
Z\sim N(V/2,V).
\]
The released log statistic is
\[
M(D)=\log E_{\mathrm{prod}}^{\mathrm{DP}}(D)
=\sum_k\log E_k(D_k)-Z.
\]
For neighboring global datasets \(D\sim D'\), disjointness means that only one block, say \(j\), changes, so
\[
|\mathbb E[M(D)]-\mathbb E[M(D')]|=
|\log E_j(D_j)-\log E_j(D'_j)|\le \Delta_{\max}.
\]
Both output laws are Gaussian with common variance \(V\). The trade-off function for two equal-variance Gaussian laws whose means differ by \(d\) is \(G_{d/\sqrt V}\). Therefore all neighboring pairs satisfy \(G_{\Delta_{\max}/\sqrt V}\)-DP. Conversely, by the definition of global sensitivity, for an index whose sensitivity is \(\Delta_{\max}\) there are neighboring block pairs whose log-evidence gaps approach \(\Delta_{\max}\). Embedding those pairs in the global disjoint product makes the GDP parameter approach \(\Delta_{\max}/\sqrt V\). Hence no smaller parameter works uniformly, proving sharpness.

The mean of \(Z\) is \(V/2\), so \(L=V/2\). Combining this with the sharp parameter gives
\[
2L\mu_{\mathrm{prod}}^2
=V\frac{\Delta_{\max}^2}{V}
=\Delta_{\max}^2.
\]
This also shows that the distributional and privacy effects of the heterogeneous allocation enter the released scalar only through \(V\).

For the constrained design problem, each local requirement \(\mu_k\le b_k\) implies
\[
\frac{\Delta_k^2}{\mu_k^2}\ge \frac{\Delta_k^2}{b_k^2},
\]
so \(V\ge V_0\). The aggregate requirement \(\mu_{\mathrm{prod}}\le\bar\mu\) is equivalent to \(V\ge T\). Thus every feasible design has \(V\ge\max\{V_0,T\}\). If \(V_0\ge T\), taking all \(\mu_k=b_k\) attains the lower bound. If \(V_0<T\), the displayed one-coordinate adjustment adds exactly \(T-V_0\) to \(V\), preserves \(\mu_j<b_j\), and attains \(V=T\). This proves both optimality and attainability.

## Verification
The algebraic identities and the two attainment cases can be replayed with `verify_heterogeneous_gdp.py`. It checks the Gaussian exponential moment, the sharp parameter/invariant identity, feasibility of both frontier branches, and randomized positive parameter instances. The script is deterministic and uses only the Python standard library.

The privacy sharpness step is analytic rather than numerical: it is inherited from the equal-variance Gaussian trade-off calculation together with the supremum definition of global log sensitivity.

## Relationship to prior work
Kuang, Gang, and Xia develop canonical Gaussian private e-values. Their general aggregation proposition permits different component GDP parameters and applies generic GDP composition, while their sharper product theorem treats independent disjoint blocks with a common parameter \(\mu\), obtaining
\[
\mu_{\mathrm{prod}}
=\mu\frac{\max_k\Delta_k}{\sqrt{\sum_k\Delta_k^2}}.
\]
Their proof identifies the two structural ingredients used here: product log sensitivity \(\max_k\Delta_k\) and Gaussian noise variance \(\sum_k\Delta_k^2/\mu^2\). Replacing the common parameter by block-specific \(\mu_k\) yields the exact variance \(V\) above. The contribution here is the resulting heterogeneous sharp law together with the privacy–utility invariant and the complete local/aggregate-cap frontier.

Csillag and Mesquita earlier show a product/continuation property for private e-values under Rényi differential privacy, but that statement concerns a different privacy notion and does not give the heterogeneous Gaussian-DP variance law or the optimization frontier above. Dong, Roth, and Su provide the Gaussian-DP trade-off framework and composition background.

Targeted statement-level searches did not reveal the invariant \(2L\mu_{\mathrm{prod}}^2=\Delta_{\max}^2\) or the exact heterogeneous cap frontier. This is not a proof that no equivalent unindexed observation exists.

## Limitations
The result is confined to canonical independent Gaussian log perturbations, independent disjoint blocks, and release of the scalar product alone. Correlated perturbations, overlapping records, data-dependent privacy parameters, non-Gaussian mechanisms, and separate release of factor-level outputs are outside the claim. The utility criterion is the injected log-noise mean/variance, not downstream power or a task-specific loss. Equal \(V\) makes the privacy perturbation of the scalar product equivalent in law conditional on the unperturbed product; it does not make the unreleased factor vector or any richer transcript equivalent.

## References
1. Q. Kuang, B. Gang, and Y. Xia, “Gaussian Differentially Private e-values: Construction, Threshold Calibration, and Multiple Testing,” arXiv:2605.29388, first posted 2026-05-28.
2. D. Csillag and D. Mesquita, “Differentially Private E-Values,” arXiv:2510.18654, first posted 2025-10-21.
3. J. Dong, A. Roth, and W. J. Su, “Gaussian Differential Privacy,” Journal of the Royal Statistical Society: Series B 84(1), 3–37, 2022, DOI:10.1111/rssb.12454.
