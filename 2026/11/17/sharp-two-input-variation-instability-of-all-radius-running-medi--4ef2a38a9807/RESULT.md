# Sharp two-input variation instability of all-radius running medians on finite paths

## Finding
For every integer \(r\ge1\), put \(k=r+1\). On any path with \(n\ge2k\) vertices, the centered median of \(2r+1\) samples, using repeated endpoint samples outside the path, has the **exact and attained** two-input adjacent-variation Lipschitz coefficient
\[
\sup_{V_n(x-y)>0}\frac{V_n(M_rx-M_ry)}{V_n(x-y)}=2r+1,
\quad V_n(z)=\sum_{i=0}^{n-2}|z_{i+1}-z_i|.
\]
The first possible path length exhibiting gain \(2r+1\) is \(n=2r+2\). Although a running median decreases the variation of a single signal in classical smoothing settings, it can amplify the variation of a *difference* by its full window width.

## Assumptions and scope
All data are real. Write indices as \(0,\ldots,n-1\), and let \(c(i)=\min(n-1,\max(0,i))\). The operator \(M_r\) is defined at every vertex by the order-statistic median
\[
(M_rx)_i=\operatorname{med}\{x_{c(i-r)},\ldots,x_{c(i+r)}\},
\]
with multiplicity when an endpoint is repeated. The seminorm is the sum over the \(n-1\) *noncyclic* adjacent edges. The theorem concerns all \(n\ge2r+2\), with no restriction on the input amplitudes.

## Proof
**1. Universal upper bound.** Let \(x(t)=x+t(y-x)\), with \(h=y-x\). A finite median of affine functions is continuous and piecewise affine in \(t\). At almost every \(t\), each output derivative is \(h_{a_i(t)}\) for some index \(a_i(t)\in[c(i-r),c(i+r)]\); repeated entries at a clamped endpoint represent the same input index. Expand the input difference in the discrete-jump basis:
\[
h=h_0\mathbf1+\sum_{j=1}^{n-1}(h_j-h_{j-1})\mathbf1_{\{i\ge j\}}.
\]
For any fixed admissible selection of indices \(a_i\), the output of a single step \(\mathbf1_{\{i\ge j\}}\) under selection is zero whenever \(i\le j-r-1\) and one whenever \(i\ge j+r\). Only the \(2r+1\) intervening edges can contribute changes, and every change has magnitude at most one. Hence
\[
V_n((h_{a_i})_i)\le(2r+1)V_n(h).
\]
Integrate the piecewise-constant derivatives in \(t\), applying the triangle inequality edge by edge, to get \(V_n(M_ry-M_rx)\le(2r+1)V_n(y-x)\).

**2. Attaining family at minimum length.** Set \(n_0=2k\) and use the baseline
\[
x_i=\begin{cases}2i,&0\le i<k,\\2(i-k)+1,&k\le i<2k.\end{cases}
\]
A direct rank count proves \((M_rx)_i=i\) for every \(0\le i<2k\): at \(1\le i<k\), exactly \(r\) window entries are smaller than the value \(i\), the value \(i\) occurs at its unique interior rank, and the endpoint case \(i=0\) is immediate. The identity on the right half follows by reflecting indices and complementing values, since \(x_{2k-1-i}=2k-1-x_i\).

Set \(h_i=\mathbf1_{\{i\ge k\}}\), so \(V_{n_0}(h)=1\). For every sufficiently small \(\varepsilon>0\), strict separation of the distinct baseline values means the median's selected baseline value remains the same. The baseline values are assigned even numbers in the left half and odd numbers in the right half. Consequently,
\[
(M_r(x+\varepsilon h)-M_rx)_i
=\begin{cases}0,&i\text{ even},\\\varepsilon,&i\text{ odd},\end{cases}
\]
and its adjacent variation is exactly \((2k-1)\varepsilon=(2r+1)\varepsilon\). Therefore the ratio attains \(2r+1\).

**3. Every larger path and minimum length.** For \(n>2k\), append \(n-2k\) copies of the final baseline value \(2k-1\) and append ones to the perturbation \(h\). The first \(2k\) median differences remain alternating: near the former right boundary, the new copies are identical to the clamped endpoint, and all added sample indices lie on the perturbed side. Beyond that position the entire window lies on the perturbed side, so every further difference equals \(\varepsilon\). The input has one jump and the output retains precisely \(2r+1\) jumps. Conversely a path with \(n<2r+2\) has fewer than \(2r+1\) edges; the step-selector bound is at most \(n-1\), and the same jump decomposition and path integration exclude coefficient \(2r+1\). This proves the sharp length threshold.

## Verification
The standalone `check_running_median_bv.py` evaluates every exact median on the constructed baseline and perturbed signal for radii \(1\) through \(40\), checks the full alternating derivative and the extensions, and carries out supplementary deterministic two-input numerical stress tests. It reports `ALL_MEDIAN_VARIATION_TESTS_PASS`. The proof above, not this finite check, supplies all-radius validity.

## Relationship to prior work
Restrepo and Chacón (1994) establish a one-input median variation-smoothing property, which is logically distinct from the two-input Lipschitz coefficient. Maragos and Schafer (1987) describe order-statistic and stack-filter representations without this all-radius sharp two-input statement. Previously documented three-point median (radius-one) results address one fixed window; other cyclic or morphological results use different domains or different operators. The present construction proves a simultaneous law for all radii and the exact first admissible path length. Background unconditionality results for other smoothing operators do not yield the alternating median selector witness.

## Limitations
This is the centered median with **repeated-endpoint** boundaries and noncyclic, unweighted path variation. It is not a claim about cyclic windows, mirror-reflection rules that differ from clamping, weighted edges, arbitrary order statistics, or the exact norm on shorter paths. The originality assessment is provisional because some archival historical articles were available only as abstracts, not full text. No independent audit has been performed.

## References
1. A. Restrepo and L. Chacón, *A Smoothing Property of the Median Filter*, IEEE Transactions on Signal Processing 42 (1994), 1553–1555, DOI: 10.1109/78.286974. Public manuscript posting documented 2015-10-08 at https://www.researchgate.net/publication/3315273_A_smoothing_property_of_the_median_filter.
2. P. Maragos and R. W. Schafer, *Morphological Filters—Part 2: Their Relations to Median, Order-Statistic, and Stack Filters*, archival technical report (1987), https://drum.lib.umd.edu/items/95ac7d84-40fc-46bd-9e9e-936ef1bbcb34.
