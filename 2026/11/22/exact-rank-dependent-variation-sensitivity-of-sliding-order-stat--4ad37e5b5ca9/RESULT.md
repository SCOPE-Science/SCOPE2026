# Exact rank-dependent variation sensitivity of sliding order-statistic filters

## Finding

Let \(r\ge 1\), \(w=2r+1\), \(n\ge 2r+2\), and \(1\le q\le w\) be integers. For a real vector \(x=(x_0,\ldots,x_{n-1})\), extend it constantly beyond both endpoints and let \(Q_{r,q}x\) be the vector of the \(q\)-th **smallest** values in the length-\(w\) centered sliding windows. With \(V(x)=\sum_{i=0}^{n-2}|x_{i+1}-x_i|\), the optimal two-input total-variation Lipschitz factor is

\[
\sup_{V(x-y)>0}\frac{V(Q_{r,q}x-Q_{r,q}y)}{V(x-y)}
=2\min\{q-1,w-q\}+1.
\]

The supremum is attained for every indicated parameter choice, with two inputs separated by an arbitrarily small positive single step. Consequently the end ranks (minimum and maximum) have coefficient \(1\), the central median has coefficient \(w\), and each rank one step away from either extreme has coefficient \(3\), irrespective of the window width.

## Assumptions and scope

The sample set is the finite noncyclic path \(\{0,1,\ldots,n-1\}\). The edge seminorm is unweighted. Endpoint clamping means that out-of-range indices in each window are replaced by \(0\) or \(n-1\), with repetitions retained; this makes each window a multiset of precisely \(w\) entries. The mapping is nonlinear and invariant under adding a common constant. The coefficient concerns **differences of two filtered inputs**, not the variation of each signal alone. The claimed exact formula is for \(n\ge w+1\), not for arbitrary shorter paths.

## Proof

**1. Reduction to rank-selector steps.** On any chamber of input space where unequal sample coordinates are strictly ordered, \(Q_{r,q}\) is linear: the output at center \(i\) equals one selected input coordinate. Clamped repetitions of the same coordinate do not affect this description. Denote the selected index by \(\sigma(i)\). The map is continuous and piecewise linear; consequently its Lipschitz bound in \(V\) follows by integrating the linear selections along the segment joining any two inputs. For a fixed selector \(\sigma\), write any perturbation as

\[
 h=h_0\mathbf1+\sum_{j=1}^{n-1}(h_j-h_{j-1})\mathbf1_{\{j,\ldots,n-1\}}.
\]

The constant term vanishes after taking variation. Thus the induced selector norm is at most the largest number of transitions in the binary string

\[
 b_i=\mathbf1_{\{\sigma(i)\ge j\}},\qquad 0\le i<n,
\]

as the input cut \(j\) ranges from \(1\) to \(n-1\). It suffices to bound the transitions of every such string uniformly over all strict input orderings.

**2. The monotone-rank-count bound.** Fix a cut \(j\), calling original indices below \(j\) *left* and those at least \(j\) *right*. Before the sliding window meets the cut, its selected index is left; after the window has passed the cut, it is right. Throughout the intervening mixed-window region, advancing the window deletes one left entry and inserts one right entry, counting clamped endpoint copies as entries. Let \(c_i\) be the number of right entries among the \(q\) smallest window entries. Deleting left and inserting right cannot decrease \(c_i\), so \(c_i\) is nondecreasing from \(0\) to \(q\).

Within a consecutive block on which \(c_i=k\) for some \(1\le k\le q-1\), write \(A_i(k')\) for the \(k'\)-th smallest left entry and \(B_i(k')\) for the \(k'\)-th smallest right entry. The \(q\)-th smallest is a right entry precisely when

\[
 B_i(k)>A_i(q-k).
\]

As the mixed window moves, its left multiset only shrinks and its right multiset only grows. Therefore \(A_i(q-k)\) is nondecreasing and \(B_i(k)\) is nonincreasing. On each fixed-\(k\) block, \(b_i\) can change only once, from \(1\) to \(0\). The two terminal blocks \(k=0,q\) are constant. At most \(q\) changes occur between successive \(c_i\)-blocks and at most \(q-1\) within them. Hence \(V(b)\le2q-1\). Replacing all input values by their negatives turns the \(q\)-th smallest selection into the \((w+1-q)\)-th smallest selection without changing selected indices; thus also \(V(b)\le 2(w-q)+1\). Combining gives

\[
 V(b)\le 2\min\{q-1,w-q\}+1.
\]

Ties between distinct original coordinates follow by approximation/continuity; within-endpoint repeated copies have the same index and cannot invalidate the count argument. The selector bound and step decomposition prove the desired global upper bound.

**3. A sharp finite construction.** By reversing the sign of all base sample values it suffices to treat \(1\le q\le r+1\). Put \(s=r-q+1\), \(n_0=2r+2\), and take the following permutation of the integers \(0,1,\ldots,2r+1\), with all displayed ranges inclusive:

\[
 z_i=\begin{cases}
 i,&0\le i\le s,\\
 s+2+2(i-s-1),&s+1\le i\le r,\\
 s+1+2(i-r-1),&r+1\le i\le r+q,\\
 i,&r+q+1\le i\le 2r+1.
\end{cases}
\]

For the input cut \(j=r+1\), direct rank counting gives a particularly simple selected-side pattern:

\[
 \mathbf1_{\{\sigma_z(i)\ge r+1\}}
 =\begin{cases}1,&i\in\{2s+1,2s+3,\ldots,2r+1\},\\0,&\text{otherwise}.\end{cases}
\]

Here is a count check for this identity. In increasing value order, the entries \(0,1,\ldots,s\) are on the left; then the sides alternate right, left, right, left, ending with the \(q\)-th right entry; all remaining larger entries are right. At centers \(i\le r\), the window has \(r-i+1\) copies of the smallest left entry, the other \(s\) low left entries, and then the available alternating sequence. Thus the selecting position within the alternating sequence, when it is positive, equals \(i-2s\). At centers \(i\ge r+1\), put \(t=i-r\). The repeated largest right endpoint copies cannot affect rank \(q\), so selection is from the original suffix beginning at \(t\). For \(t\le s+1\), removing the first \(t\) low-left entries again gives alternating-sequence rank \(i-2s\). For \(t=s+1+j\) with \(0\le j\le q-1\), the first \(j\) left entries in that alternating sequence have been deleted; its \(q\)-th surviving element is right exactly when \(q+j=i-2s\) is odd. All cases give the displayed pattern.

The binary output starts at zero and alternates for its final \(2q-1\) edges, so its variation equals \(2q-1\). Now let \(h_i=\mathbf1_{\{i\ge r+1\}}\) and take \(x=z\), \(y=z+\varepsilon h\) with \(0<\varepsilon<1/2\). Because distinct original values differ by at least one, the rank selectors do not change. The input-difference variation is \(\varepsilon\), while its output-difference variation is \(\varepsilon(2q-1)\). For \(q>r+1\), use the negated construction for rank \(w+1-q\). For every longer path, extend the last values of \(z\) and \(h\) constantly; the first \(n_0\) output positions remain exactly those of the clamped length-\(n_0\) construction, giving at least the same gain. The upper bound prohibits any larger gain. This proves equality for every stated \(n,r,q\).

## Verification

Run `python3 CHECKER.py` in the same directory. The standalone script checks the explicit sharp selectors and exact perturbation identities for every radius from \(1\) through \(64\) and every rank; exhaustively enumerates strict rank permutations for smaller paths (up to seven vertices); and performs \(3000\) seeded integer two-input tests. The checker is supplementary: finite testing alone does not prove the statements for unbounded radius or arbitrary real inputs. The proof above supplies those quantifiers.

## Relationship to prior work

The 1987 Maragos–Schafer treatment proves max–min and threshold representations for general order-statistic filters. Those structural identities do not by themselves give the sharp coefficient for the **difference of two filtered signals** in the path-variation seminorm. Restrepo–Chacón's 1994 smoothing result concerns variation of a **single** median-filtered input (under a different finite-endpoint convention). Earlier documented sharp two-input analyses address the central median rank or the two extreme ranks separately. Those are special cases of the present rank-dependent formula and are not claimed here as original; the new point is the complete interpolation across every intermediate rank, including the width-independent amplification at fixed distance from an extreme. No universal assertion about other window shapes or weighted variation is made.

## Limitations

The theorem does not classify shorter paths \(n\le w\), cyclic windows, unequal positional weights, asymmetric windows, vector-valued order statistics, or compositions of different rank filters. Priority relative to unindexed historical signal-processing literature is not independently certified. The proof and checker have not undergone independent external mathematical validation.

## References

1. P. Maragos and R. W. Schafer, *Morphological Filters—Part II: Their Relations to Median, Order-Statistic, and Stack Filters*, technical report TR 87-134 (dated 1987), full scan at https://drum.lib.umd.edu/bitstreams/154a294b-2b9b-4c93-871a-8c68ed6834ff/download ; journal version, IEEE Transactions on Acoustics, Speech, and Signal Processing, 35 (1987), 1170–1184, https://doi.org/10.1109/TASSP.1987.1165254 .
2. A. Restrepo and L. Chacón, *A smoothing property of the median filter*, IEEE Transactions on Signal Processing 42 (1994), 1553–1555, https://doi.org/10.1109/78.286974 ; publicly uploaded manuscript listing (8 October 2015), https://www.researchgate.net/publication/3315273_A_smoothing_property_of_the_median_filter .
3. H. G. Longbotham and A. C. Bovik, *Theory of order statistic filters and their relationship to linear FIR filters*, IEEE Transactions on Acoustics, Speech, and Signal Processing 37 (1989), 275–287, https://doi.org/10.1109/29.21690 .
