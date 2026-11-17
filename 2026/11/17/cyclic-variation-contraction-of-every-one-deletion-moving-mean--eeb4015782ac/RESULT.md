# Cyclic variation contraction of every one-deletion moving mean

## Finding

For every pair of integers \(n\ge w\ge2\) and every \(1\le r\le w\), let \(F_{n,w,r}\) delete the \(r\)-th order statistic in each length-\(w\) cyclic window and average the other entries. The map has a sharp **two-input cyclic-total-variation contraction** property:

\[
\operatorname{TV}_n(F_{n,w,r}x-F_{n,w,r}y)\le\operatorname{TV}_n(x-y)
\qquad(x,y\in\mathbb R^n).
\]

Its sharp Lipschitz coefficient is zero at \(n=w\), and exactly one for every \(n\ge2w\). Moreover, the centered three-site midrange \(F_{n,3,2}\) has exact coefficient zero at \(n=3\) and exactly one for **all** \(n\ge4\). For other window widths the intermediate sharp coefficients are not classified.

## Assumptions and scope

Write indices modulo \(n\). The length-\(w\) forward window at site \(i\) is \((x_i,x_{i+1},\ldots,x_{i+w-1})\); its ordered values are \(z_{i,(1)}\le\cdots\le z_{i,(w)}\), including repetitions. Define

\[
(F_{n,w,r}x)_i=\frac{1}{w-1}\left(\sum_{j=0}^{w-1}x_{i+j}-z_{i,(r)}\right),
\qquad \operatorname{TV}_n(h)=\sum_{i=0}^{n-1}|h_{i+1}-h_i|.
\]

The map is continuous, piecewise linear, and commutes with addition of constants. The coefficient is the supremum of \(\operatorname{TV}_n(Fx-Fy)/\operatorname{TV}_n(x-y)\) over pairs with positive denominator. The result holds for real scalars and **one filtering pass**; no probabilistic noise model is assumed.

## Proof

**1. Ordered-index interlacing.** Lift a generic input \(x\) periodically to all integer sites and suppose its entries at distinct cyclic sites are different. Fix one chamber of the hyperplane arrangement of input value ties. The derivative \(S\) of \(F\) is obtained by selecting and uniformly averaging \(w-1\) indices from each window. Arrange the selected indices of window \(\{i,\ldots,i+w-1\}\) in **spatial**, not value, order:

\[
a_{i,1}<\cdots<a_{i,w-1},\qquad i+k-1\le a_{i,k}\le i+k
\quad(1\le k<w).
\]

The next window has corresponding spatially ordered indices \(b_{i,k}\), with \(i+k\le b_{i,k}\le i+k+1\). Therefore \(a_{i,k}\le b_{i,k}\) for each \(k\), independent of which rank was deleted.

**2. Positive gradient factorization.** For a spatial index threshold \(j\), let

\[
A_i(j)=\frac{1}{w-1}\#\{k:a_{i,k}\le j\},\qquad
B_i(j)=\frac{1}{w-1}\#\{k:b_{i,k}\le j\},
\]

and define \(q_{i,j}=A_i(j)-B_i(j)\ge0\) by interlacing. Discrete integration by parts gives

\[
(Sh)_{i+1}-(Sh)_i=\sum_{j=i}^{i+w-1}q_{i,j}(h_{j+1}-h_j).
\]

The coefficients are nonnegative and have **unit column sums**: for any integer edge index \(j\),

\[
\sum_{i=j-w+1}^{j}q_{i,j}
=A_{j-w+1}(j)-A_{j+1}(j)=1-0=1.
\]

The first selected window lies entirely at or before \(j\), and the last lies entirely after it. This identity holds on the integer lift and descends to the cyclic quotient even if different lifted windows overlap. Thus the induced matrix on periodic gradients is column-stochastic, and

\[
\sum_{i=0}^{n-1}|(Sh)_{i+1}-(Sh)_i|
\le\sum_{j=0}^{n-1}|h_{j+1}-h_j|.
\]

**3. From chambers to all inputs.** The filter is continuous and piecewise affine on the finitely many order chambers. Along a segment joining two arbitrary inputs its derivative, wherever it exists, is a chamber matrix of the above kind (or a limiting convex combination of such matrices at persistent ties). The variation estimate survives finite segment integration and continuity. This proves the global two-input inequality, not just an inequality for an individual signal.

**4. Sharpness and finite boundary.** At \(n=w\), each window contains the entire cyclic signal and omits the same order statistic, so the output is constant across sites. At \(n\ge2w\), let \(x\) be the indicator of an arc of \(w\) consecutive sites and let \(y=0\). A window entirely inside the arc gives output one, and one entirely outside gives zero. As a cyclic window passes either boundary, the number of ones in it varies monotonically. Deleting a fixed order statistic and averaging the others is coordinatewise nondecreasing, so the output rises monotonically across one boundary and falls monotonically across the other. Hence both the input and output have total variation exactly two, proving sharpness one.

For \(w=3,r=2\), the output is the midrange, i.e. the arithmetic mean of the local minimum and maximum. The case \(n=3\) is constant. At \(n=4\), take \(y=(0,1,3,2)\) and \(x=(0,11/10,31/10,2)\). At \(n=5\), take \(y=(0,1,2,3,4)\) and \(x=(0,1,21/10,3,4)\). Direct substitution yields the exact ratio one in each case. The previous binary-arc construction covers every \(n\ge6\), completing the sharp midrange classification.

## Verification

The standalone `check.py` is standard-library Python 3. Run `python check.py`. It exhaustively checks 925164 chamber/arc configurations for widths three through five at the specified short cycle sizes, verifies exact rational short-cycle and all large-cycle witnesses, tests the positive column-stochastic gradient factor for 500 seeded random chambers, and checks 3000 further exact-rational two-input pairs. These finite checks are corroboration only: the theorem for every admissible window and dimension is proved analytically above.

## Relationship to prior work

Maragos and Schafer (1987) studied morphological and order-statistic filters and explicitly described linear combinations of order statistics. Welk (habilitation thesis submitted 2007, section 3.3, revised in later editions) defined scalar midrange and gave its Chebyshev minimization interpretation. Neither inspected relevant section supplies the two-input cyclic-variation contraction for every deleted rank and window size. Published results for three-point medians establish possible **amplification**, while finite-path morphological results study distinct maps and boundary geometry. These claims concern different derivative selections and do not imply the ordered-index interlacing proved here. Searches did not locate the exact theorem; historical priority is nevertheless provisional.

## Limitations

The theorem uses uniformly spaced cyclic windows with equal weights on the retained entries. Weighted retained entries, noncontiguous windows, two or more deleted entries, general graphs, other boundary conditions and exact finite coefficients for \(w<n<2w\) at arbitrary window widths are not claimed. The 2015 trimmed-mean preprint has a verified first-version timestamp; earlier historical materials are known by year or month but lack a verified original public day in the inspected records. This is **not** a publication-date claim for the theorem. Independent validation has not been performed.

## References

1. P. Maragos and R. W. Schafer, *Morphological Filters—Part II: Their Relations to Median, Order-Statistic, and Stack Filters*, IEEE Transactions on Acoustics, Speech, and Signal Processing 35 (1987), 1170–1184; accessible 1987 technical report: https://drum.lib.umd.edu/items/95ac7d84-40fc-46bd-9e9e-936ef1bbcb34.
2. M. Welk, *Dynamic and Geometric Contributions to Digital Image Processing*, habilitation thesis, November 2007, sections 3.3.1–3.3.3 (edition revised February 2016): https://www.mia.uni-saarland.de/Publications/welk-habil09.pdf.
3. A. Dash and S. K. Sathua, *High Density Noise Removal by Cascading Algorithms*, first public arXiv version 11 April 2015, arXiv:1504.02856. Its trimmed-mean application motivates robustness questions but it does not supply the theorem.
4. *Sharp BV perturbation threshold for cyclic three-point medians* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-sharp-bv-perturbation-threshold-for-cyclic-three-point-medians--59530ef626eb.
5. *Finite-window morphology: sharp two-input variation and a boundary-weight transition* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-finite-window-morphology-sharp-two-input-variation-and-a-boundar--5f5f2cb7d7b2.
