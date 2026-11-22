# Distribution-free overlap calibration and multiscale limits for reciprocal nearest neighbors

## Finding

Let \(n\ge5\) and let \(q\ge2\) be fixed. On each of \(q\) independent occasions, sample \(n\) independent uniform positions on the unit circle and assign the same distinct labels \(1,\ldots,n\) to the sampled points. Define \(M_i\) as the set of unordered label pairs whose members are each other's unique geodesic nearest neighbor in occasion \(i\). Put \(R_i=|M_i|\) and \(H_{ij}=|M_i\cap M_j|\).

**Exact conditional calibration.** More generally, for *any* two independent, label-exchangeable random matchings \(M_1,M_2\) on \([n]\), and \(0\le a,b\le\lfloor n/2\rfloor\), the overlap has the exact conditional probability generating polynomial
\[
\mathbb E[z^{H_{12}}\mid R_1=a,R_2=b]
=\sum_{r=0}^{\min(a,b)}
\frac{2^r(a)_{\underline r}(b)_{\underline r}}
{r!(n)_{\underline{2r}}}(z-1)^r.
\]
Here \((t)_{\underline r}=t(t-1)\cdots(t-r+1)\), and the formula applies only to size pairs having positive conditioning probability. Consequently, conditional upper-tail probabilities are exactly computable without knowing the geometric dimension, point density, or other features of the independent label-exchangeable matching procedures. No asymptotic approximation is required for such a null calibration.

**Circular model.** For the independent uniform-circle samples above,
\[
\mathbb E R_i=\frac n3,\qquad
\operatorname{Var}(R_i)=\frac{2n}{45},\qquad
\mathbb E H_{ij}=\frac{2n}{9(n-1)}.
\]
For distinct \(i,j,k\),
\[
\operatorname{Cov}(H_{ij},H_{ik})=
\frac{8n}{405(n-1)^2}>0.
\]
If \(\{i,j\}\) and \(\{k,l\}\) are disjoint, \(H_{ij}\) and \(H_{kl}\) are independent for every \(n\).

**Simultaneous multiscale law.** As \(n\to\infty\),
\[
\left(\left(\frac{R_i-n/3}{\sqrt n}\right)_{1\le i\le q},
(H_{ij})_{1\le i<j\le q}\right)
\ \xrightarrow{d}\
\left((G_i)_{1\le i\le q},(Z_{ij})_{1\le i<j\le q}\right),
\]
where *all* variables on the right are mutually independent,
\(G_i\sim N(0,2/45)\), and \(Z_{ij}\sim\operatorname{Poisson}(2/9)\). Thus overlap counts involving the same sample have strictly positive finite-size covariance, yet all pairwise overlaps become jointly independent in the limit and decouple from the Gaussian fluctuations of each sample's matching size.

## Assumptions and scope

A matching is a set of disjoint unordered two-vertex edges on a labelled set. *Label-exchangeable* means the distribution is unchanged by every simultaneous permutation of vertex labels. Each replicate must be independent, including independently resampled geometry. Ties in nearest-neighbor distances occur with probability zero for the continuous uniform circle model. The exact conditional law holds for arbitrary independent exchangeable matching-valued random variables on \([n]\), including reciprocal-nearest-neighbor matchings generated from independent, identically labelled point clouds in any Euclidean dimension with almost-sure uniqueness. The explicit moments and joint limit are asserted for uniform points on the circle and fixed \(q\), with \(n\ge5\) for the moment identities. No growing-\(q\) limit is claimed.

## Proof

**1. Conditional uniformity and factorial moments.** Relabelling acts transitively on the finite set of all matchings with a specified size \(a\); hence a label-exchangeable matching conditional on \(|M|=a\) is uniform on that set. Independence of the original matchings implies conditional independence given their sizes. For any fixed matching of size \(a\), the probability that a uniform size-\(b\) matching contains a specified collection of \(r\) disjoint edges is
\[
\frac{\#\{\text{size-}\!b\text{ matchings containing those edges}\}}
{\#\{\text{size-}\!b\text{ matchings}\}}
=\frac{2^r(b)_{\underline r}}{(n)_{\underline{2r}}}.
\]
Counting ordered choices of \(r\) edges from the first matching gives
\[
\mathbb E[(H_{12})_{\underline r}\mid R_1=a,R_2=b]
=\frac{2^r(a)_{\underline r}(b)_{\underline r}}
{(n)_{\underline{2r}}}.
\]
The finite binomial identity \(z^h=\sum_r (h)_{\underline r}(z-1)^r/r!\) proves the generating polynomial. Its coefficients give an exact conditional null distribution; for example, when \(n=6\) and \(a=b=2\), probabilities for \(H=0,1,2\) are respectively \(34/45,10/45,1/45\).

**2. Cyclic nearest-neighbor minima.** Uniform cyclic spacings have the Dirichlet \((1,\ldots,1)\) distribution and can be represented as \((E_j/\sum_hE_h)_{j=1}^n\) with independent \(E_j\sim\operatorname{Exp}(1)\). The gap between the points at cyclic positions \(j\) and \(j+1\) forms a reciprocal nearest-neighbor pair precisely when its gap is smaller than both neighboring gaps; therefore
\[
R_i=\sum_{j=1}^n I_j,\qquad
I_j=\mathbf1\{E_j<E_{j-1},\ E_j<E_{j+1}\},
\]
with cyclic subscripts. The indicators are stationary and two-dependent away from the cyclic seam. Direct integration (or counting the relative ranks of five independent exponentials) gives
\[
\mathbb E I_j=\frac13,\quad
\operatorname{Cov}(I_j,I_{j+1})=-\frac19,\quad
\operatorname{Cov}(I_j,I_{j+2})=\frac1{45};
\]
nonoverlapping triples are independent. Summing these covariances around the cycle yields \(\mathbb E R_i=n/3\) and \(\operatorname{Var}(R_i)=2n/45\), valid for \(n\ge5\). The classical bounded two-dependent central limit theorem, applied to the linearized indicators (only a bounded number of seam terms differ), gives
\[
\frac{R_i-n/3}{\sqrt n}\xrightarrow{d}N(0,2/45).
\]
Independent occasions yield independent Gaussian coordinates.

**3. Finite replicate dependence.** By exchangeability, a given unordered label pair belongs to sample \(j\)'s matching with probability \(2\mathbb E R_j/[n(n-1)]=2/[3(n-1)]\). Conditional on \(M_i\), the random overlap counts \(H_{ij}\) and \(H_{ik}\) are independent because samples \(j,k\) are independent. Their conditional means both equal \(2R_i/[3(n-1)]\), so the law of total covariance gives
\[
\operatorname{Cov}(H_{ij},H_{ik})
=\left(\frac{2}{3(n-1)}\right)^2\operatorname{Var}(R_i)
=\frac{8n}{405(n-1)^2}.
\]
Averaging the two-replicate conditional mean \(2R_iR_j/[n(n-1)]\) gives \(\mathbb E H_{ij}=2n/[9(n-1)]\). Pairs involving disjoint occasions are independent outright.

**4. Joint rare-overlap law.** First condition on deterministic sizes \(s_1,\ldots,s_q\) with \(s_i/n\to\rho_i\in(0,1/2]\). For any fixed family of nonnegative integers \(r_{ij}\), expand
\(\mathbb E\prod_{i<j}(H_{ij})_{\underline{r_{ij}}}\) by choosing ordered prescribed label edges in each pairwise overlap. The dominant choices have mutually vertex-disjoint edges across *all* pair types. For an edge required in one specified matching, the exact inclusion probability for an entire disjoint set of \(d\) edges is \(2^d(s_i)_{\underline d}/(n)_{\underline{2d}}\). There are asymptotically \((n^2/2)^T\) choices of the \(T=\sum r_{ij}\) ordered, mutually disjoint label edges, and the probability factor tends to the product of \((2\rho_i/n)^{d_i}\), where \(d_i=\sum_{j\ne i}r_{ij}\). This yields
\[
\mathbb E\prod_{i<j}(H_{ij})_{\underline{r_{ij}}}
\longrightarrow\prod_{i<j}(2\rho_i\rho_j)^{r_{ij}}.
\]
The discarded configurations contribute \(O(n^{-1})\) for each fixed multi-index, uniformly for size ratios in a compact subset of \((0,1/2]\): sharing a label vertex reduces the number of choices by at least one power of \(n\); reusing exactly the same edge in different pair-types requires at least three matching replicates and also incurs at least one extra power of \(n^{-1}\). Two copies of an edge in the *same* falling factorial are excluded by definition. These are the factorial moments of mutually independent Poisson variables, and the Poisson laws are moment-determinate.

For the geometric samples, \(s_i/n=R_i/n\to1/3\) in probability. The factorial-moment estimates are uniform for size ratios in a compact subset of \((0,1/2]\), and the associated Poisson intensities \(2(s_i/n)(s_j/n)\) therefore converge in probability to \(2/9\). The conditional overlap law consequently converges in probability to the fixed independent Poisson product law. Taking expectations jointly with any bounded continuous function of the normalized \(R_i\), and using the independent Gaussian limit from step 2, proves the claimed full Gaussian–Poisson product limit.

## Verification

The accompanying `verify.py` independently enumerates every matching of each size on up to seven labels, checks the exact conditional overlap distribution against direct pairwise matching enumeration, and checks label-exchangeability, circle matching means and variances, and three-replicate overlap covariance. Circular finite configurations are enumerated by independent cyclic label order and spacing rank permutations for \(n=5,6\), involving respectively 2,880 and 86,400 configurations. The checker passes 75 exact-rational distribution/moment/frequency assertions. These tests validate finite formulas and modeling conventions; the limit theorem is established by the factorial-moment and bounded-dependence arguments above, not by extrapolating finite enumeration.

## Relationship to prior work

Enns, Ehlers and Misi studied clusters determined by one-dimensional reciprocal nearest-neighbor relations. Bahadır and Ceyhan proved one-sample moments, exact recurrences, and central limit behavior of reciprocal and shared nearest neighbors on an interval; their one-sample results are not claimed as new. Later general perfect-matching work, including Deng's multivariate Poisson approximation, substantially covers classical *marginal* random-matching overlap asymptotics, so an isolated Poisson marginal is not claimed as a new contribution here. The claim under assessment is the exact conditional, distribution-free partial-matching calibration coupled with the simultaneous independent-replicate Gaussian–Poisson law and the explicit finite positive covariance between overlapping replicate pairs. The cited results do not state this combined conditional and multiscale conclusion; a previously unnoticed reduction from more general matching theorems remains a historical-priority risk.

## Limitations

The geometric moment constants require independent uniform-circle samples and the particular reciprocal *nearest*-neighbor definition. For nonuniform geometries the conditional matching-overlap polynomial remains valid under independent label exchangeability, but the uniform-circle asymptotic parameter and Gaussian variance need not. This is an independent-replicate null, not a model for longitudinal point clouds with shared latent geometry. The argument does not establish a universal total-variation rate for the joint limit, growing-replicate thresholds, or independence at finite size. A full independent review and exhaustive bibliographic priority determination have not been performed.

## References

- E. G. Enns, P. F. Ehlers and T. Misi, “A cluster problem as defined by nearest neighbours,” *Canadian Journal of Statistics*, DOI: https://doi.org/10.2307/3316135. (Earlier one-sample reciprocal-neighbor study; exact original online day not established.)
- S. Bahadır and E. Ceyhan, “On the Number of Reflexive and Shared Nearest Neighbor Pairs in One-Dimensional Uniform Data,” arXiv:1605.01940, first submitted 2016-05-06. https://arxiv.org/abs/1605.01940
- B. Deng, “Deranged Perfect Matchings on complete graph and balanced complete r-partite graph,” arXiv:2505.13799, first submitted 2025-05-20. https://arxiv.org/abs/2505.13799
