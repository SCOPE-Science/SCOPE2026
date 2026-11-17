# Gaussian collision condensation for generalized parking-function polytopes

## Finding
Let \(n\ge2\), let \(\mathbf b=(b_1,\ldots,b_n)\) be a positive integer vector, and let \(P_n(\mathbf b)\subset\mathbb R^n\) be the convex hull of its generalized parking functions. Fix an integer \(r\ge2\). For \(r\) independent directions \(G^{(1)},\ldots,G^{(r)}\sim N(0,I_n)\), let \(C_{n,r}(\mathbf b)\) be the probability that all directions expose **the same vertex**. Define
\[
H_{n,r}=\sum_{j=0}^n\frac{(n)_j}{(j!)^r},\qquad (n)_j=\frac{n!}{(n-j)!}.
\]
Then, for every \(n\ge2\) and all positive integral parameters,
\[
\boxed{\displaystyle
2^{nr}C_{n,r}(\mathbf b)=
\begin{cases}
H_{n,r},& b_1>1,\\[2pt]
H_{n,r}+\dfrac{(n+1)^r-n^r-1}{(n!)^{r-1}},&b_1=1.
\end{cases}}
\]
For \(r=2\) the first expression is the Laguerre value \(H_{n,2}=L_n(-1)\), and the second adds \(2/(n-1)!\).

**Sharp collision hierarchy.** Put \(x_n=n^{1/r}\), and let \(\delta_2=e^{-1/2}\) while \(\delta_r=1\) for every fixed integer \(r\ge3\). For fixed \(r\ge2\), uniformly over arbitrary parameter vectors \(\mathbf b=\mathbf b(n)\),
\[
\boxed{\displaystyle
C_{n,r}(\mathbf b)\sim
\frac{\delta_r\,e^{r n^{1/r}}}{\sqrt r\,(2\pi n^{1/r})^{(r-1)/2}\,2^{nr}}.}
\]
The case \(r=2\) alone retains the nontrivial correction \(e^{-1/2}\) from sampling distinct coordinate positions; that correction disappears at each fixed \(r\ge3\).

If \(J_{n,r}\) is the number of nonunit entries at the common exposed vertex, conditioned on all \(r\) directions selecting it, then
\[
\boxed{\displaystyle
\frac{J_{n,r}-n^{1/r}}{n^{1/(2r)}}\ \Longrightarrow\ N(0,1/r).}
\]
Unconditionally one direction exposes a vertex with a \(\mathrm{Binomial}(n,1/2)\) number of nonunit coordinates when \(b_1>1\); when \(b_1=1\) its probability mass at \(j=n\) is transferred to \(j=n-1\). Thus conditioning on \(r\) simultaneous exposed-vertex coincidences changes a typical rank from order \(n\) to the specific scale \(n^{1/r}\), with a universal Gaussian fluctuation law.

**Antecedent exact cone census.** In the standard coordinate Euclidean metric, the complete finite cone spectrum is already implied by known partial-permutohedron cone-angle formulas: for \(b_1>1\), vertices with \(j\) nonunit coordinates occur with multiplicity \((n)_j\), each with Gaussian cone probability \(2^{-n}/j!\), for \(0\le j\le n\); for \(b_1=1\), the masses agree for \(j\le n-2\), while \(n!\) vertices at \(j=n-1\) each have mass \((n+1)/(2^n n!)\) and \(j=n\) is absent. This finite spectrum and the immediately deduced exact moment sums are **not claimed as independent novelties**. The new assertion is the joint fixed-\(r\) sharp asymptotic hierarchy and conditional central limit for these canonical generalized parking-function polytopes.

## Assumptions and scope
A \(\mathbf b\)-parking function is a positive integer vector whose increasing rearrangement \(\beta'_1\le\cdots\le\beta'_n\) satisfies \(\beta'_i\le S_i\), with \(S_i=b_1+\cdots+b_i\). We use the **standard coordinate Euclidean metric** on \(\mathbb R^n\), with no hyperplane lift, linear rescaling, or changing the normal-direction distribution. Every normalized Gaussian cone mass is the probability that a standard Gaussian objective is maximized at that vertex; radial normalization makes it a spherical normal-cone angle. Ties occur with probability zero. The polynomial parameter \(n\) ranges through integers at least two. The asymptotic comparison allows each \(\mathbf b(n)\) to vary arbitrarily with \(n\), including switching between the two cases.

The known vertex description (Bayer et al.) says that the vertices are all distinct permutations of
\[
 (\underbrace{1,\ldots,1}_{k},S_{k+1},\ldots,S_n),\qquad 0\le k\le n,
\]
with the \(k=0\) and \(k=1\) orbits identified exactly when \(b_1=1\). This geometric description is an antecedent, not a newly claimed result.

## Proof
**1. Exact exposed vertex rule.** Let \(c_{(1)}<\cdots<c_{(n)}\) be the strictly ordered coordinates of a generic objective \(c\), and let \(F_k(c)\) be the maximum scalar product over permutations of the displayed vertex with \(k\) initial ones. The rearrangement inequality gives
\[
F_k(c)=\sum_{i=1}^k c_{(i)}+\sum_{i=k+1}^n S_i c_{(i)},\qquad
F_k(c)-F_{k-1}(c)=(1-S_k)c_{(k)}.
\]
For \(k\ge2\), \(S_k>1\); for \(k=1\), \(S_1>1\) precisely when \(b_1>1\). Consequently \(F_k\) increases as one passes negative coordinates and decreases as one passes positive ones. The maximizer has \(k\) ones exactly when \(k\) objective coordinates are negative, except that when \(b_1=1\) the zero-negative case coalesces into the single-negative vertex orbit. On the \(j=n-k\) positive-coordinate positions, the values \(S_{k+1},\ldots,S_n\) are placed in increasing objective order.

**2. Exact moments from the antecedent cone law.** Gaussian signs are independent unbiased bits. Conditional on any sign pattern, the objective coordinates in the \(j\) positive positions are iid continuous and their ranking is uniform over \(j!\) permutations. Hence a fixed vertex with \(j\) nonunit coordinates has probability \(2^{-n}/j!\), and there are \(\binom nj j!=(n)_j\) such vertices. For \(b_1=1\), each special \(j=n-1\) vertex is exposed either when its unique unit coordinate is the only negative coordinate, or when all coordinates are positive and the unit position is the least positive. The two masses add to
\[
\frac{2^{-n}}{(n-1)!}+\frac{2^{-n}}{n!}=\frac{n+1}{2^n n!}.
\]
Summing \(r\)-th powers of masses gives \(H_{n,r}\) for \(b_1>1\). When \(b_1=1\), the final two contributions \(n^r/(n!)^{r-1}\) and \(1/(n!)^{r-1}\) are replaced by \((n+1)^r/(n!)^{r-1}\), giving the stated correction. The rank law for one direction follows by summing the cone masses of each class. These exact cone calculations also follow from the published partial-permutohedron angular census under the translation and fan identifications described below; their new use here is to analyze the entire fixed-\(r\) asymptotic family.

**3. The all-\(r\) saddle estimate.** Fix \(r\ge2\), write \(x=n^{1/r}\), and compare the finite sum \(H_{n,r}\) with the infinite series
\[
B_{n,r}=\sum_{j=0}^\infty\frac{n^j}{(j!)^r}.
\]
The ratio of consecutive summands of \(B_{n,r}\) is \(n/(j+1)^r\), strictly decreasing in \(j\). It is greater than one below \(x-1\) and less than one above; the tails away from any fixed relative interval about \(x\) are exponentially smaller than the maximal summand, by multiplying those monotone ratios. More precisely, Stirling expansion for \(j=x+y\sqrt x\) with bounded \(y\) gives
\[
\log\frac{n^j}{(j!)^r}=rx-\frac r2\log(2\pi x)-\frac r2y^2+o(1),
\]
uniformly for \(y\) in compact sets. For Gaussian-scale tails, choose \(M\to\infty\) after \(n\to\infty\), and use the decreasing consecutive-term ratios to bound the mass outside \(|j-x|\le M\sqrt x\) by \(O(e^{-c_rM^2})\) times the central sum. Thus the central Riemann sum converges to \(\int_{\mathbb R}e^{-ry^2/2}\,dy\), yielding
\[
\boxed{\displaystyle B_{n,r}\sim\frac{e^{rx}}{\sqrt r\,(2\pi x)^{(r-1)/2}}.}
\]
This same local expansion establishes \((J-x)/\sqrt x\Rightarrow N(0,1/r)\) when the summand weights of \(B_{n,r}\) define the distribution of \(J\).

**4. The collision-specific finite-population correction.** For \(0\le j\le n\), the ratio between the \(j\)-th terms of \(H_{n,r}\) and \(B_{n,r}\) is
\[
q_{n,j}=\frac{(n)_j}{n^j}=\prod_{i=0}^{j-1}\left(1-\frac in\right)\in[0,1].
\]
When \(j=x+O(\sqrt x)\),
\[
\log q_{n,j}=-\frac{j(j-1)}{2n}+O\left(\frac{j^3}{n^2}\right)
=-\frac12n^{2/r-1}+o(1).
\]
The leading value equals \(-1/2\) for \(r=2\), but tends to zero for every fixed \(r\ge3\). The ratio \(q_{n,j}\) is bounded by one and converges to that constant uniformly on the Gaussian central window; the tail estimate of Step 3 therefore gives
\[
\frac{H_{n,r}}{B_{n,r}}\longrightarrow\delta_r,
\qquad \delta_2=e^{-1/2},\quad\delta_r=1\ \text{for }r\ge3.
\]
Furthermore, the change in \(\log q_{n,j}\) across a window of width \(O(\sqrt x)\) is \(O(x^{3/2}/n)=O(n^{3/(2r)-1})=o(1)\). Thus multiplying the \(B_{n,r}\) weights by \(q_{n,j}\) does not alter the limiting normal law for \((J-x)/\sqrt x\). The exceptional \(b_1=1\) correction is superexponentially small compared with \(H_{n,r}\): for fixed \(r\), \((n+1)^r/(n!)^{r-1}=o(B_{n,r})\) by Stirling, and its tail remains negligible under the rank normalization. Consequently both sharp asymptotics and conditional central limits hold uniformly over the choice of \(\mathbf b\). Since \(\sqrt x=n^{1/(2r)}\), the finding follows.

## Verification
Run `python3 verify.py` (standard library). It constructs vertices from the definition and maximizes every signed-rank chamber objective over those vertices for \(n=2,3,4,5\) and three parameter choices in each dimension. Exact chamber counts verify all vertex probabilities and the collision moment identities for \(r=2,3,4\) in all 12 cases. Stable logarithmic summation compares the \(r=2,3,4\) moment sums and conditional rank variances with the proved asymptotics at \(n=100,400,1600,6400\). These finite tests are not substitutes for the all-\(n\), fixed-\(r\) proof.

## Relationship to prior work
Hanada, Lentfer, and Vindas-Meléndez studied two-parameter parking-function polytopes, while Bayer and collaborators established the unrestricted positive-parameter vertex formula. Classical parking-function polytopes shifted by the all-ones vector are **exactly** the partial permutohedra \(\mathcal P(n,n-1)\) (Behrend). All parameter classes have the same coordinate normal fans as \(\mathcal P(n,n-1)\) when \(b_1=1\), or \(\mathcal P(n,n)\) when \(b_1>1\), because their generic support maximizers use identical sign-and-positive-rank patterns. **Crucially, an earlier public exact Gaussian cone-angle spectrum for partial permutohedra already supplies every finite cone mass and hence all finite collision moment sums by raising those masses to powers. This finite part is fully credited as prior coverage.** The present claim is the sharp hierarchy for *every fixed number of simultaneous Gaussian objectives*, including the special \(r=2\) finite-population correction and the conditional normal limit on the \(n^{1/r}\) rank scale. Those asymptotic results do not appear in the inspected complete partial-permutohedron report.

A previous report on classical Gaussian width fluctuations gives a one-direction binomial exposed-vertex layer law, which is also prior. A closely related star graph-associahedron analysis uses a different, fixed-sum coordinate embedding in \(\mathbb R^{n+1}\); its Gaussian normal-cone masses need not agree under the nonisometric affine identification. The present sharp collision hierarchy belongs specifically to the canonical parking-function coordinates.

## Limitations
This work applies to the ordinary ambient Euclidean metric on the convex hull of integral generalized parking functions. A different metric, including the standard fixed-sum graphical-nestohedron embedding, changes Gaussian cone masses. The leading \(r\)-fold collision asymptotic and the conditional Gaussian rank law are proved by a local saddle analysis; no quantitative error bounds uniform in growing \(r\) are claimed. No full large-deviation principle, Berry–Esseen error rate, or result for other random direction distributions is asserted. The original finite vertex classification and the complete finite cone-angle spectrum for related partial permutohedra are prior knowledge; the finite moment identities are straightforward implications and are not separately new. The bibliographic search does not establish absolute historical priority; an unindexed equivalent collision calculation remains possible. Independent mathematical validation has not been performed.

## References
1. M. Hanada, J. Lentfer, A. R. Vindas-Meléndez, *Generalized parking function polytopes*, arXiv:2212.06885, first public 2022-12-13, https://arxiv.org/abs/2212.06885.
2. M. M. Bayer et al., *Combinatorics of generalized parking-function polytopes*, arXiv:2403.07387, first public 2024-03-12, https://arxiv.org/abs/2403.07387. In particular, the vertex description in Theorem 2.3.
3. F. Liu, W. Thawinrak, *Parking Function Polytopes*, arXiv:2512.14199, first public 2025-12-16, https://arxiv.org/abs/2512.14199 (related normal-fan descriptions; not a dated lead source).
4. *Gaussian width fluctuations of classical parking-function polytopes and their exposed vertex layers*, publicly available research report, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-gaussian-width-fluctuations-of-classical-parking-function-polyto--f22c06d75d0e.
5. *Two critical Rényi windows in the angular spectra of star-graph polytopes*, publicly available research report, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-two-critical-r-nyi-windows-in-the-angular-spectra-of-star-graph--e1b409771cb8.

6. D. Heuer, J. Striker, *Partial permutation and alternating sign matrix polytopes*, arXiv:2012.09901, first public 2020-12-17, https://arxiv.org/abs/2012.09901.
7. R. E. Behrend et al., *Partial permutohedra*, arXiv:2207.14253, first public 2022-07-28, https://arxiv.org/abs/2207.14253.
8. *Gaussian normal-cone angles and a third-order width transition for partial permutohedra*, public research report with complete finite cone census, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-gaussian-normal-cone-angles-and-a-third-order-width-transition-f--200e766da27b.
