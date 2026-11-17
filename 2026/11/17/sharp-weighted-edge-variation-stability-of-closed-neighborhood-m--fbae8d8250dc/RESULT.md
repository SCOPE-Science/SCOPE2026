# Sharp weighted edge-variation stability of closed-neighborhood medians on stars

## Finding
Let \(S_{k+1}\) be a star with hub \(o\), leaves \(v_1,\ldots,v_k\), integer \(k\ge1\), and arbitrary edge-variation weights \(w_i>0\). On real vertex signals define the **simultaneous closed-neighborhood median filter** \(T\) by taking at each vertex the median of its own value and those of its neighbors. Throughout, the median of an even number of real values is **the arithmetic mean of the two middle order statistics**. Define
\[
V_w(h)=\sum_{i=1}^{k}w_i|h(v_i)-h(o)|,\qquad W=\sum_{i=1}^kw_i,\qquad w_*=\min_iw_i.
\]
Then its exact, attained two-input modulus is
\[
\boxed{\sup_{V_w(f-g)>0}\frac{V_w(Tf-Tg)}{V_w(f-g)}=
\begin{cases}
0,&k=1,\\[2pt]
W/w_*-1/2,&k\ge2\text{ even},\\[2pt]
(W-w_*)/(2w_*),&k\ge3\text{ odd}.
\end{cases}}
\]
The supremum is over arbitrary real pairs, and every value is attained by a pair lying in one local linearity region. By adding a common sufficiently large constant, attaining pairs can also be chosen **nonnegative**.

In particular, with unit weights the exact coefficients are \(0\) for \(k=1\), \(k-1/2\) for even \(k\ge2\), and \((k-1)/2\) for odd \(k\ge3\). Among positive weights of fixed sum, uniform weights uniquely minimize the coefficient when \(k\ge2\) (up to a common factor). The filter is nonexpansive in weighted edge variation **if and only if** \(k=1\), or \(k=3\) with all three weights equal. The substantially different even/odd degree laws arise from changing whether the hub's median window has an odd or even number of samples.

## Assumptions and scope
The graph is a finite simple star and the filter is applied synchronously. Neighborhoods contain the vertex itself; each leaf therefore has a two-sample window and outputs the arithmetic average of its own value and the hub's value. The hub's window has \(k+1\) values. Filter samples have uniform rank weights; the independently specified \(w_i>0\) weight **variation only**, not the order statistics. Signals are real and may contain ties. The ratio excludes zero-denominator pairs. Since \(T(f+c\mathbf1)=Tf+c\mathbf1\), a zero variation difference cannot create nonzero output variation. All formulas concern differences of **two filtered signals**, not variation of one filtered signal.

## Proof
**1. Exact reduction to a median scalar map.** Write \(a=f(o)\) and \(x_i=f(v_i)-a\). Translation equivariance gives the output leaf-to-hub differences
\[
F_i(x):=(Tf)(v_i)-(Tf)(o)=\tfrac12x_i-m(x),
\qquad m(x)=\operatorname{median}(0,x_1,\ldots,x_k).
\]
Consequently \(V_w(f-g)=\|x-y\|_{1,w}\) and \(V_w(Tf-Tg)=\|F(x)-F(y)\|_{1,w}\), where \(\|h\|_{1,w}=\sum_iw_i|h_i|\). Thus it suffices to calculate the globally sharp Lipschitz norm of \(F:\mathbb R^k\to\mathbb R^k\) in this weighted norm. This reduction also makes the quotient by constants exact.

**2. Upper bound on each order-statistic region.** The scalar function \(m\) is continuous and piecewise linear on the finite hyperplane arrangement determined by the comparisons among \(0,x_1,\ldots,x_k\). On any open strict-order region it has a constant gradient \(b=(b_1,\ldots,b_k)\). If \(k\) is even, its \(k+1\) samples number an odd integer and \(b\) is either \(0\) (when the median is \(0\)) or \(e_j\) (when it is a leaf). If \(k\) is odd, the sample count is even and \(b=(e_p+e_q)/2\), interpreting \(e_0=0\), where \(p,q\) are the two central sample indices; in particular each \(b_j\in\{0,1/2\}\).

In either case the local derivative of \(F\) is the matrix
\[
J_{ij}=\tfrac12\mathbf1_{\{i=j\}}-b_j.
\]
Its exact induced weighted \(\ell_1\) norm is the largest weighted absolute column sum:
\[
\|J\|_{1,w\to1,w}=\max_j\frac{\sum_iw_i|\tfrac12\mathbf1_{\{i=j\}}-b_j|}{w_j}.
\]
For \(b_j=0\) this column ratio is \(1/2\); for \(b_j=1\) it is \(W/w_j-1/2\); for \(b_j=1/2\) it is \((W-w_j)/(2w_j)\).

When \(k=1\), both vertices output their common two-point arithmetic mean, so \(F\equiv0\). For even \(k\ge2\), all branch column ratios are bounded by \(W/w_*-1/2\). For odd \(k\ge3\), they are bounded by \((W-w_*)/(2w_*)\); this number is at least \(1\), hence dominates the inactive-column ratio \(1/2\).

**3. Global control, including all ties.** Any line segment \(x+t(y-x)\), \(0\le t\le1\), encounters only finitely many order-comparison breakpoints unless it lies within a comparison hyperplane. On each open subsegment where the ordering is fixed, \(F\) is affine, so its increment has weighted norm bounded by the common maximum branch norm times the weighted norm of the corresponding input increment. Summing with the triangle inequality proves the upper bound for generic segments. Since \(F\) is continuous, approximating any degenerate segment by generic segments gives the same bound for all real \(x,y\), including equal values. No differentiability assumption is made on the input pair.

**4. Sharp input pairs.** Choose a leaf index \(j\) with \(w_j=w_*\), put the hub value \(0\), and set that leaf value to \(1\). If \(k=2m\) is even, assign \(m-1\) other leaves value \(-2\) and the remaining \(m\) leaves value \(3\). In the hub's list of \(2m+1\) values, the selected leaf is the unique middle entry, so its hub median depends with coefficient \(1\) on that leaf. Let \(g\) differ from this input \(f\) solely by adding \(\varepsilon\in(0,1)\) to that leaf. The median stays on the selected leaf throughout the segment. The filtered difference is \(-\varepsilon/2\) across that leaf edge and \(-\varepsilon\) across every other edge. Hence the ratio is exactly \(W/w_*-1/2\).

If \(k=2m+1\ge3\) is odd, assign \(m-1\) other leaves value \(-2\), one other leaf value \(2\), and the remaining \(m\) leaves value \(3\). The hub median is the arithmetic mean of the selected leaf at \(1\) and the leaf at \(2\). Perturbing only the selected leaf by \(\varepsilon\in(0,1)\) keeps those two central positions fixed. The filtered difference vanishes across the selected leaf edge and equals \(-\varepsilon/2\) across every other edge, giving ratio \((W-w_*)/(2w_*)\). The \(k=1\) zero coefficient is attained for any pair with nonzero edge difference. Thus every formula is exact, not merely a limit of derivatives.

**5. Uniform-weight optimality and nonexpansivity.** Since \(W\ge kw_*\) and equality occurs exactly when all weights are equal, both nontrivial formula branches are strictly decreasing functions of \(w_*/W\), with unique uniform-weight minimizers up to scale. For even \(k\ge2\), the sharp norm is at least \(k-1/2>1\). For odd \(k\ge3\), it is at least \((k-1)/2\), which is at most one only at \(k=3\), with equality there precisely for equal weights. Together with \(k=1\) this is the asserted complete classification.

## Verification
The standalone file `verify_star_median.py` uses only Python's standard library and exact rational arithmetic. Running `python verify_star_median.py` exhaustively enumerates all strict center-window orderings for up to six leaves under several positive variation-weight profiles and compares their exact Jacobian column norms with the formula. It also checks attaining signal pairs through thirty leaves, many general two-input rational signal pairs, and the nonexpansivity classification. This tests the implementation and finite boundary cases; Steps 1–5 are the proof for every integer \(k\ge1\) and every positive real weight vector.

## Relationship to prior work
Median filtering and its smoothing motivation are classical. Restrepo and Chacon (1994) proved a **single-input** total-variation smoothing statement for one-dimensional median filtering. Little and Jones (arXiv first public 2010; journal 2011), in Section 4(d) and the appendix of their freely readable primary article, prove the analogous three-point **one-input** path-variation result. Neither statement bounds \(V_w(Tf-Tg)\) for different inputs on a branched star.

The published work *Sharp two-input variation sensitivity of three-point median smoothing on finite paths* (2026) computes a weighted two-input modulus for **endpoint-preserving** three-point path medians, whereas here both leaves and hub always include themselves, even-sized windows use arithmetic midpoint selection, and the graph branches. Its path formulas do not imply the present coefficient (already for a two-leaf star). The published *Sharp finite-order variation amplification by tree majority-median filters* (2026) uses a different odd-window majority convention and proves **one-input** tree variation, explicitly excluding the two-input problem and the closed-neighborhood convention. The published finite-window morphology result (2026) concerns min/max filters on paths, not these median rank selectors on stars. These distinctions compare operators, hypotheses and implications rather than just titles.

## Limitations
This theorem does not treat iterates of the median map, other tie-breaking rules for even windows, weighted order statistics, arbitrary trees, or endpoint-preserving conventions. Its very different even/odd constants **depend on the arithmetic midpoint convention**. The entire result is an exact finite-star family, not a claim of a general theorem on every graph. A short 1994 primary paper on median smoothing was identifiable from its abstract but its full text was not accessible in the checked channels; an implicit older related estimate cannot be wholly excluded. Independent scientific audit has not been performed.

## References
1. M. A. Little and N. S. Jones, *Generalized Methods and Solvers for Noise Removal from Piecewise Constant Signals*, arXiv:1012.5095, initial public version 2010-12-22, https://arxiv.org/abs/1012.5095. Related full primary journal article: *Generalized methods and solvers for noise removal from piecewise constant signals. I. Background theory*, Proc. R. Soc. A **467** (2011), 3088–3114, https://pmc.ncbi.nlm.nih.gov/articles/PMC3191861/ , Section 4(d) and appendix.
2. A. Restrepo and L. Chacon, *A smoothing property of the median filter*, IEEE Trans. Signal Process. **42** (1994), 1553–1555, DOI: 10.1109/78.286974. Bibliographic record and abstract: https://eurekamag.com/research/097/760/097760929.php .
3. E. Arias-Castro and D. L. Donoho, *Does median filtering truly preserve edges better than linear filtering?*, arXiv:math/0612422, initial public 2006-12-14, https://arxiv.org/abs/math/0612422. Background on the classical filter's stability motivation, not a graph variation comparison.
4. *Sharp two-input variation sensitivity of three-point median smoothing on finite paths*, publicly accessible mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-sharp-two-input-variation-sensitivity-of-three-point-median-smoo--5759b99f2a42 .
5. *Sharp finite-order variation amplification by tree majority-median filters*, publicly accessible mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-sharp-finite-order-variation-amplification-by-tree-majority-medi--e16ec3a51444 .
6. *Finite-window morphology: sharp two-input variation and a boundary-weight transition*, publicly accessible mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-finite-window-morphology-sharp-two-input-variation-and-a-boundar--5f5f2cb7d7b2 .
