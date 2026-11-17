# Sharp two-input Gini sensitivity of the cyclic three-point median

## Finding
For every integer \(n\ge3\), let \(T_n:\mathbb R^n\to\mathbb R^n\) be the simultaneous three-point median filter on a cycle:
\[
(T_nx)_j=\operatorname{median}(x_{j-1},x_j,x_{j+1}),\qquad j\in\mathbb Z/n\mathbb Z.
\]
Define unweighted complete-pair Gini variation
\[
G_n(x)=\sum_{0\le i<j<n}|x_i-x_j|.
\]
Then the **exact, attained two-input Lipschitz seminorm** is
\[
\boxed{\sup_{G_n(x-y)>0}\frac{G_n(T_nx-T_ny)}{G_n(x-y)}=
\begin{cases}
0,&n=3,\\[2pt]
\frac43,&n=4,\\[2pt]
\frac{3(n-3)}{n-1},&n\ge5.
\end{cases}}
\]
For each \(n\ge4\), equality is achieved by two distinct real inputs differing only in one coordinate. Hence the first amplification occurs at four sites; for \(n\ge5\) the optimal coefficient increases strictly to the unattained all-dimension supremum \(3\).

## Assumptions and scope
The indices are cyclic, so the filtering window has three distinct indices for every \(n\ge3\). All entries and perturbations are real; the median is the middle of three values even when ties occur. The ratio compares *differences of two filtered signals*, and is not the one-input ratio \(G_n(T_nx)/G_n(x)\). Because both \(G_n\) and \(T_n\) are invariant or equivariant under constant shifts, respectively, the quotient defines a seminorm Lipschitz constant on signals modulo additive constants. The finite-dimensional statement is for one simultaneous filtering pass and unweighted *all-pairs*, not adjacent-edge, variation.

## Proof
**1. Strict-order linearization.** On any region where all input coordinates are distinct, each median equals a single input coordinate. Thus \(T_nz=Jz\) on that region, with a selector matrix \(J\) having one \(1\) in each row, all other entries zero. If row \(i\) selects column \(s(i)\), let \(c_j=|\{i:s(i)=j\}|\). Then \(\sum_jc_j=n\), and \(c_j\le3\), because column \(j\) can participate in only the three windows centered at \(j-1,j,j+1\). The filter is continuous and piecewise linear. Segment subdivision through strict-order regions, followed by a continuity approximation for segments lying on tie hyperplanes, gives
\[
\operatorname{Lip}_{G_n}(T_n)=\max_{J\text{ arising from a strict-order region}}\|J\|_{G_n\to G_n}.
\]
Conversely every such selector norm is realized by a sufficiently small perturbation within its strict-order region, so the reduction is an equality, not merely an upper bound.

**2. Exact binary-cut formula for each selector.** For any selector \(J\) and real \(z\), the layer-cake identity \(|u-v|=\int_{\mathbb R}|\mathbf1_{u>t}-\mathbf1_{v>t}|\,dt\) yields
\[
\|J\|_{G_n\to G_n}=\max_{\varnothing\ne S\subsetneq\{0,\ldots,n-1\}}
\frac{c(S)[n-c(S)]}{|S|[n-|S|]},\qquad c(S)=\sum_{j\in S}c_j.
\]
Indeed, the numerator is \(G_n(J\mathbf1_S)\), the denominator is \(G_n(\mathbf1_S)\), and layer-cake plus the triangle inequality extends the cut inequality to every real \(z\). Each cut itself supplies the reverse bound.

**3. Universal sharp bound for \(n\ge5\).** Put \(k=|S|\) and \(t=c(S)\). Complementing \(S\) replaces \((k,t)\) by \((n-k,n-t)\), without changing the quotient, so take \(1\le k\le n/2\). We know \(0\le t\le3k\) and \(0\le t\le n\).

For \(n=5\), the case \(k=1\) gives \(t(5-t)/4\le3/2\), and \(k=2\) gives \(t(5-t)/6\le1\). For \(n=6\), the cases \(k=1,2,3\) give respective bounds \(9/5,9/8,1\). These establish the claimed upper bound in dimensions five and six.

Now assume \(n\ge7\). When \(k\le n/6\), we have \(t\le3k\le n/2\), hence
\[
\frac{t(n-t)}{k(n-k)}\le\frac{3(n-3k)}{n-k}\le\frac{3(n-3)}{n-1}.
\]
The last inequality follows because \((n-3k)/(n-k)\) is strictly decreasing in \(k\) for \(k<n\). When \(k>n/6\), using \(t(n-t)\le n^2/4\) and \(k(n-k)>5n^2/36\) gives the strict bound \(t(n-t)/[k(n-k)]<9/5\). But \(3(n-3)/(n-1)\ge2\) for \(n\ge7\). Thus every strict-chamber selector obeys the displayed sharp bound in every dimension \(n\ge5\).

**4. The two small cycles.** At \(n=3\), every window contains all three sites, so all outputs are their common median and \(G_3(T_3x-T_3y)=0\). At \(n=4\), no input coordinate can be the median in all three containing windows on a strict-order region: relative to the candidate value, those three windows would force each pair of the *other three* values to lie on opposite sides, which is impossible. Hence \(c_j\le2\). For a binary cut, \(k=1\) gives \(t(4-t)/3\le4/3\), and \(k=2\) gives \(t(4-t)/4\le1\). This proves the bound \(4/3\).

**5. Attaining two-input pairs.** At \(n=4\), take \(x=(1,0,2,3)\). Its local selector chooses the coordinate \(x_0\) at precisely output sites \(0,1\). For every sufficiently small \(\varepsilon>0\), set \(y=x+\varepsilon e_0\). Then \(T_4y-T_4x=\varepsilon(1,1,0,0)\), so the quotient is \(4/3\).

For every \(n\ge5\), choose distinct data with \(x_0=1\), \(x_1=-1\), \(x_2=3\), \(x_{n-2}=-2\), \(x_{n-1}=2\), and arbitrary pairwise distinct values greater than \(5\) at all remaining sites. In the three windows containing site \(0\), its value lies strictly between the other two. Thus for sufficiently small \(\varepsilon>0\), the difference \(T_n(x+\varepsilon e_0)-T_nx\) equals \(\varepsilon\) at precisely the sites \(n-1,0,1\) and zero elsewhere. The output variation is \(3(n-3)\varepsilon\), whereas the input variation is \((n-1)\varepsilon\). This attains the bound for every \(n\ge5\). The final assertions on dimension threshold and supremum follow directly.

## Verification
Run `python3 check_median_gini.py` with standard Python 3. It exhaustively evaluates every strict-order permutation and every nontrivial binary cut for \(3\le n\le8\), a total of \(46,230\) orderings. It checks actual attaining two-input pairs at every dimension \(4\le n\le110\) and independently verifies every cut-capacity inequality for \(5\le n\le100\). The exact arithmetic tests passed. None of these finite tests is used as a substitute for Steps 1–5.

## Relationship to prior work
Median filtering has classical threshold-decomposition and variation-smoothing theory (Qiu 1994; Maragos and Schafer 1987; Restrepo and Chacón 1994). Those papers address local optimization, morphology, and one-input variation, rather than the exact global two-input complete-pair Gini modulus here. Arias-Castro and Donoho (arXiv first posted December 14, 2006) analyze asymptotic denoising risk, not this deterministic quotient. A published study of cyclic median \(\ell_p\) perturbation norms establishes selector multiplicity saturation; its \(\ell_p\) equality condition does not provide the nontrivial cut-capacity inequality needed for the Gini seminorm, which vanishes on constants unlike \(\ell_p\). Another published sharp result concerns cyclic adjacent-edge total variation: it has constants \(0,2,3\) across the three dimension regimes, rather than the complete-pair Gini coefficients above. The present result is an exact operator-invariant comparison, not a claim of completely new median-filter methodology.

## Limitations
No coefficient is claimed for larger median windows, noncyclic boundary conventions, unequal pair weights, high-dimensional data, or iterated filters. The historical priority assessment is qualified; indexed and inspected sources do not exclude an older differently phrased equivalent. A 1994 article on variation smoothing and the full 1987 report were not read exhaustively, and archival publication dates of some older context sources are not available to a precise UTC day. The precise date used in accompanying metadata is the earliest verifiable day for the designated dated preprint lead, not a denial of earlier classical literature.

## References
1. E. Arias-Castro and D. L. Donoho, *Does median filtering truly preserve edges better than linear filtering?*, arXiv:math/0612422, v1 posted 2006-12-14, Annals of Statistics 37 (2009), 1172–1206. https://arxiv.org/abs/math/0612422
2. G. Qiu, *Functional Optimization Properties of Median Filtering*, IEEE Signal Processing Letters 1 (1994), 64–65, full author-hosted text: https://people.cs.nott.ac.uk/pszqiu/webpages/Papers/Functional%20Optimisation%20Properties%20of%20Median%20Filtering.pdf
3. P. Maragos and R. W. Schafer, *Morphological Filters—Part 2: Their Relations to Median, Order-Statistic, and Stack Filters*, SRC TR 87-134 (1987), https://drum.lib.umd.edu/items/95ac7d84-40fc-46bd-9e9e-936ef1bbcb34
4. A. Restrepo and L. Chacón, *A Smoothing Property of the Median Filter*, IEEE Transactions on Signal Processing 42 (1994), 1553–1555, DOI:10.1109/78.286974.
5. *Arithmetic saturation of the Lipschitz amplification of cyclic running medians* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-arithmetic-saturation-of-the-lipschitz-amplification-of-cyclic-r--b3edfc2b2f2a
6. *Sharp BV perturbation threshold for cyclic three-point medians* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-sharp-bv-perturbation-threshold-for-cyclic-three-point-medians--59530ef626eb
