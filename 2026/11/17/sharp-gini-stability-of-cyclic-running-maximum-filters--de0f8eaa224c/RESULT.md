# Sharp Gini stability of cyclic running maximum filters

## Finding

For every integer \(n\ge2\) and window width \(1\le w\le n\), consider the cyclic flat dilation (running maximum)
\[
(M_{n,w}x)_i=\max_{0\le j<w}x_{(i+j)\bmod n},\qquad i\in\{0,\ldots,n-1\},
\]
on arbitrary real signals \(x\in\mathbb R^n\). In the unweighted complete-graph Gini variation seminorm
\[
G_n(x)=\sum_{0\le i<j<n}|x_i-x_j|,
\]
its **exact sharp global two-input Lipschitz constant** is
\[
\boxed{\operatorname{Lip}_{G_n}(M_{n,w})=\frac{w(n-w)}{n-1}.}
\]
Thus for every \(x,y\in\mathbb R^n\),
\[
G_n(M_{n,w}x-M_{n,w}y)\le\frac{w(n-w)}{n-1}\,G_n(x-y).
\]
The constant is attained for every \((n,w)\) by arbitrarily close input pairs. The map is Gini-nonexpansive precisely for \(w=1\), \(w=n-1\), and \(w=n\), with coincidences of these cases for small \(n\). Strict amplification occurs exactly for \(n\ge4\) and \(2\le w\le n-2\); its first instance is \(\operatorname{Lip}_{G_4}(M_{4,2})=4/3\).

At each fixed \(n\), the maximum over window widths is
\[
\boxed{\max_{1\le w\le n}\operatorname{Lip}_{G_n}(M_{n,w})=\frac{\lfloor n^2/4\rfloor}{n-1}},
\]
attained at \(w=\lfloor n/2\rfloor\) and/or \(w=\lceil n/2\rceil\). Consequently the worst possible amplification is \(n/4+O(1)\). This is a two-input statement; it does not assert an analogous factor for one-input variation reduction.

## Assumptions and scope

There are \(n\) distinct sites arranged in a cycle; each forward window includes exactly \(w\) sites, including its starting site. Every input coordinate is real and unrestricted. All unordered pairs of sites carry equal Gini weight, irrespective of cyclic distance. The seminorm vanishes exactly on constant vectors. The Lipschitz modulus is the supremum over pairs with positive input seminorm, and constant differences cannot produce positive output seminorm because the filter commutes with addition of a constant vector. For \(w=n\), all output coordinates equal the input maximum, so the Lipschitz seminorm is zero.

## Proof

**Step 1: reduction to selection branches.** Whenever the input coordinates are strictly ordered, each output maximum is attained at a unique input site. In a neighborhood of that input, \(M_{n,w}\) therefore equals a linear coordinate-selection map \(A\): there is a function \(\phi:\{0,\ldots,n-1\}\to\{0,\ldots,n-1\}\), with \(\phi(i)\in\{i,\ldots,i+w-1\}\bmod n\), such that \((Ah)_i=h_{\phi(i)}\). Along any line segment joining two inputs, the running maximum is a continuous piecewise-affine map of the segment parameter. Hence a uniform bound on the Gini seminorms of every realized selection branch implies the same global two-input bound by summing the increments of the finitely many affine pieces and using the triangle inequality. Ties can be handled by continuity (or by using a consistent maximizing selector on each open affine interval).

**Step 2: exact coarea formula for a coordinate-selection map.** Write \(c_j=\#\{i:\phi(i)=j\}\). Then \(\sum_jc_j=n\). For a subset \(S\) of \(k\) input sites, let \(t=\sum_{j\in S}c_j\). For its indicator \({\bf1}_S\),
\[
G_n({\bf1}_S)=k(n-k),\qquad G_n(A{\bf1}_S)=t(n-t).
\]
Every real \(h\) can be decomposed into a constant plus a nonnegative sum of nested binary superlevel indicators. The pairwise absolute-difference coarea identity gives the sum of their \(k(n-k)\) terms exactly, and the triangle inequality bounds the output by the sum of their \(t(n-t)\) terms. Conversely, binary vectors realize every cut ratio. Therefore
\[
\|A\|_{G_n\to G_n}=\max_{\varnothing\ne S\ne\{0,\ldots,n-1\}}\frac{t(n-t)}{k(n-k)}.
\]

**Step 3: short windows, \(2w\le n\).** A given input site is contained in exactly \(w\) output windows, so \(0\le c_j\le w\). Replace \(S\) by its complement if necessary; the displayed ratio does not change, and now \(1\le k\le n/2\). Always \(t\le kw\). If \(kw\le n/2\), monotonicity of \(u(n-u)\) on \([0,n/2]\) yields
\[
\frac{t(n-t)}{k(n-k)}\le\frac{w(n-kw)}{n-k}\le\frac{w(n-w)}{n-1}.
\]
The second inequality is equivalent to \(n(k-1)(w-1)\ge0\).

If instead \(kw>n/2\), then \(t(n-t)\le n^2/4\). Because \(n/(2w)<k\le n/2\) and \(u(n-u)\) increases to the midpoint,
\[
k(n-k)\ge\frac{n^2(2w-1)}{4w^2}.
\]
Consequently
\[
\frac{t(n-t)}{k(n-k)}\le\frac{w^2}{2w-1}\le\frac{w(n-w)}{n-1}.
\]
The last inequality is exactly \((w-1)(n-2w)\ge0\), which holds here. This proves the asserted branch bound for all short windows, without assuming anything beyond the occupancy cap.

**Step 4: long windows, \(2w\ge n\).** At a strictly ordered input, the unique global-largest site belongs to exactly \(w\) windows and necessarily wins every such window. If a cut \(S\) contains that site, at least \(w\) outputs select from \(S\), so \(t\ge w\); otherwise \(t\le n-w\). In either case \(t\in[0,n-w]\cup[w,n]\), and as \(w\ge n/2\),
\[
t(n-t)\le w(n-w).
\]
Every nontrivial cut satisfies \(k(n-k)\ge n-1\). Thus its ratio is at most \(w(n-w)/(n-1)\). The overlapping boundary \(2w=n\) is covered by either argument, and the full-window case \(w=n\) gives zero.

**Step 5: sharp attainment and classification.** Select any site \(j\), choose an input with \(x_j\) strictly greater than all other mutually distinct coordinates, and let \(y=x+\varepsilon e_j\) for arbitrarily small \(\varepsilon>0\). Exactly the \(w\) windows containing \(j\) change their maximum by \(\varepsilon\), while the other \(n-w\) windows do not change. Hence
\[
G_n(y-x)=\varepsilon(n-1),\qquad G_n(M_{n,w}y-M_{n,w}x)=\varepsilon w(n-w).
\]
This realizes the upper bound exactly. The condition \(w(n-w)\le n-1\) is equivalent, for integer \(1\le w\le n\), to \(w\in\{1,n-1,n\}\). The quadratic \(w(n-w)\) is maximized by the integer(s) nearest \(n/2\), giving the final envelope.

## Verification

The standalone Python 3 script `verify.py` requires no third-party packages. It uses exact rational arithmetic for binary cut ratios and arbitrary input pairs, enumerates all strictly ordered input chambers for \(2\le n\le8\), tests the underlying occupancy and global-maximum inequalities over a large finite parameter grid, and constructs exact maximizing perturbations. To reproduce, execute `python3 verify.py` in the directory containing this file. The output ends in `ALL_CYCLIC_DILATION_GINI_CHECKS_PASSED`. The finite calculations are corroboration only: Steps 1–5 prove the result for all \(n\) and \(w\).

## Relationship to prior work

Flat morphological dilation (local maximum) and its relation to other order-statistic operations are classical; for example Maragos and Schafer (1987) develop the max/min and threshold-stack formalism. Najman and Cousty (arXiv:1404.7748, first posted 30 April 2014) describe the morphology of graph neighborhoods and the grayscale lift. Neither inspected source states the exact perturbation constant for pairwise Gini variation. Published work on finite-path sliding morphology gives weighted **adjacent-edge** variation bounds under truncated boundary windows, not the present complete-graph pairwise seminorm under cyclic windows. A prior result on cyclic max filters obtains a **centered Euclidean** two-input modulus, not this Gini modulus: equivalence of finite-dimensional norms yields estimates, not the exact formula established here.

## Limitations

The theorem assumes a contiguous uniform cyclic window, unweighted Gini variation over *all* unordered pairs, and real scalar data. It does not determine sharp weighted-pairwise variation coefficients, irregular neighborhoods, variable windows, sliding quantile filters, or compositions of dilations of different widths. The originality comparison cannot exclude inaccessible or unindexed historical equivalents; no independent mathematical audit has been performed.

## References

1. P. Maragos and R. W. Schafer, *Morphological Filters—Part II: Their Relations to Median, Order-Statistic, and Stack Filters*, IEEE Transactions on Acoustics, Speech, and Signal Processing **35** (1987), 1170–1184, DOI: 10.1109/TASSP.1987.1165254. Author-hosted full text: https://robotics.ntua.gr/wp-content/uploads/publications/1987_MaragosSchafer_MorphologicFilters-part2_ieeetASSP_+corrections1989.pdf . Author bibliography gives public date 1987-08-01.
2. L. Najman and J. Cousty, *A graph-based mathematical morphology reader*, arXiv:1404.7748, first posted 2014-04-30, https://arxiv.org/abs/1404.7748 . Sections 2–3 describe graph neighborhoods, dilation, and grayscale stack operators.
3. *Finite-window morphology: sharp two-input variation and a boundary-weight transition*, publicly indexed mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-finite-window-morphology-sharp-two-input-variation-and-a-boundar--5f5f2cb7d7b2 ; exact finite-path weighted-adjacent-variation comparison, including its primary-text assumptions.
