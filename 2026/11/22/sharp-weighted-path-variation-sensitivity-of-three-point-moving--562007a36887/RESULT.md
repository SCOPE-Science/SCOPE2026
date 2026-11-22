# Sharp weighted path-variation sensitivity of three-point moving median absolute deviation

## Finding

The unscaled median absolute deviation (MAD) of three real observations is the smallest of their three pairwise distances. For every integer \(n\ge 3\), consider the full-window moving MAD map \(M_n:\mathbb R^n\to\mathbb R^{n-2}\),
\[
 (M_nx)_i=\operatorname{med}_{j=i,i+1,i+2}\bigl|x_j-\operatorname{med}(x_i,x_{i+1},x_{i+2})\bigr|,\qquad 1\le i\le n-2.
\]
For positive input edge weights \(w_1,\ldots,w_{n-1}\) and, when \(n\ge4\), positive output edge weights \(v_1,\ldots,v_{n-3}\), write
\[
 V_w(h)=\sum_{j=1}^{n-1}w_j|h_{j+1}-h_j|,\qquad V_v(z)=\sum_{i=1}^{n-3}v_i|z_{i+1}-z_i|.
\]
For \(n=3\), set \(V_v\equiv0\). The exact two-input Lipschitz coefficient in these variation seminorms, attained whenever positive, is zero at \(n=3\). For all \(n\ge4\), with the boundary convention \(v_0=v_{n-2}=0\), it is
\[
 \boxed{\displaystyle
 K_n(w,v)=\max\left\{\frac{v_1}{w_1},\frac{v_{n-3}}{w_{n-1}},
 \max_{2\le j\le n-2}\frac{v_{j-2}+2v_{j-1}+v_j}{w_j}\right\}.}
\]
Here the coefficient is the smallest \(K\) such that \(V_v(M_nx-M_ny)\le K V_w(x-y)\) for every real pair \(x,y\). Consequently, weighted variation nonexpansivity holds **if and only if** every ratio displayed inside the maximum is at most one. At unit weights the exact coefficient is
\[
 \boxed{K_n=0\ (n=3),\quad K_n=2\ (n=4),\quad K_n=3\ (n=5),\quad K_n=4\ (n\ge6).}
\]
Thus this local robust-scale statistic amplifies differences in variation from four input samples onward, and its sharp worst-case gain saturates at six input samples. In contrast to some smooth local-scale mappings, every positive coefficient here is attained by two finite signals differing by a single step.

## Assumptions and scope

All signals are real and all windows consist of exactly three successive observations, without endpoint padding, wrapping or truncated windows; the output has length \(n-2\). The statistic is the **unscaled** MAD, without a Gaussian consistency factor, and all edge weights are strictly positive and fixed independently of the data. The weights \(w,v\) measure variation of input and output perturbations; they are not replicated observation weights inside the median. When a constant calibration factor \(c>0\) is applied to the MAD outputs, all coefficients are multiplied by \(c\). The theorem concerns the variation of the *difference of two outputs*, not merely the variation of each output separately. Translation by a constant is annihilated on both sides.

## Proof

**1. Triple identity.** For a sorted triple \(a\le b\le c\), the deviations about its median are \(b-a,0,c-b\), so their median is \(\min\{b-a,c-b\}\). The minimum pairwise distance among \(a,b,c\) is the same number. If \(d_j=x_{j+1}-x_j\), we therefore have
\[
 (M_nx)_i=F(d_i,d_{i+1}),\qquad
 F(s,t)=\min\{|s|,|t|,|s+t|\}.
\]
Each of the three expressions inside the minimum is \(1\)-Lipschitz separately in each argument. The minimum of finitely many uniformly \(1\)-Lipschitz real functions is \(1\)-Lipschitz, hence, for fixed \(s\) or \(t\), changing the other coordinate by \(\delta\) changes \(F\) by at most \(|\delta|\).

**2. Upper bound on a single input difference.** Fix \(j\in\{1,\ldots,n-1\}\) and change only \(d_j\) by \(\delta\). When \(2\le j\le n-2\), only output coordinates \(j-1\) and \(j\) can change. Denote these changes by \(\alpha\) and \(\beta\). The triple identity gives \(|\alpha|,|\beta|\le|\delta|\), and the difference of the two output sequences has zeros elsewhere. Its weighted variation is precisely
\[
 v_{j-2}|\alpha|+v_{j-1}|\beta-\alpha|+v_j|\beta|
 \le(v_{j-2}+2v_{j-1}+v_j)|\delta|,
\]
where missing end edges carry zero weight. At \(j=1\), only the first output can change, giving \(V_v\le v_1|\delta|\). At \(j=n-1\), only the last output can change, giving \(V_v\le v_{n-3}|\delta|\). For arbitrary input differences \(d,e\), interpolate by changing their coordinates successively, apply the triangle inequality in the output-variation seminorm, and sum these estimates. The result is \(V_v(M_nx-M_ny)\le K_n(w,v)\sum_jw_j|d_j-e_j|\). If the input variation is zero, then \(d=e\) and both MAD outputs agree; thus no exceptional quotient is needed.

**3. Sharpness, with finite witnesses.** Every ratio in the maximum has an attaining pair. Fix an edge \(j\) and prescribe baseline first differences \(d_1,\ldots,d_{n-1}\); any such vector is realized by a real path \(x\) by setting \(x_1=0\) and integrating the differences. Let \(y\) have the same differences except for \(d_j\) increased by \(\varepsilon=1/10\). For the first edge, set \((d_1,d_2)=(1,3)\), and for the last edge set \((d_{n-2},d_{n-1})=(3,1)\), taking all remaining differences to be \(5\). Then the sole affected MAD output increases by exactly \(\varepsilon\), attaining respectively \(v_1/w_1\) or \(v_{n-3}/w_{n-1}\).

For any interior input edge \(2\le j\le n-2\), instead prescribe
\[
 (d_{j-1},d_j,d_{j+1})=(-3/2,1,-3)
\]
and take all remaining differences equal to \(5\). We have, exactly,
\[
 F(-3/2,1)=1/2,\quad F(-3/2,1+\varepsilon)=1/2-\varepsilon,
\]
\[
 F(1,-3)=1,\quad F(1+\varepsilon,-3)=1+\varepsilon.
\]
Thus the two affected outputs change by \(\alpha=-\varepsilon\) and \(\beta=+\varepsilon\). All other outputs are unchanged, and the output-variation gain equals \((v_{j-2}+2v_{j-1}+v_j)\varepsilon\), while the input-variation cost is \(w_j\varepsilon\). Choosing the edge maximizing the stated finite set of ratios gives an actual attaining pair. For \(n=3\), the output consists of one scalar and its variation is identically zero. This proves the formula and attainment.

**4. Dimension thresholds and rigidity of weighted nonexpansivity.** At unit weights, the interior quotient has the successive possible values \(2\) at \(n=4\), \(3\) at \(n=5\), and \(4\) when \(n\ge6\), because precisely then an interior input edge can influence two output entries with three surrounding output-variation edges. Boundary quotients equal one. Since the weighted coefficient was obtained as the maximum of finitely many sharp ratios, \(K_n(w,v)\le1\) is equivalent to each of the listed inequalities, with no hidden regularity or monotonicity assumption on the weights.

## Verification

The accompanying standalone \(\texttt{checks/verify\_mad.py}\) uses exact rational arithmetic to compare the median-of-absolute-deviations definition with the minimum of pairwise distances, checks all boundary/interior attaining patterns for arbitrary positive rational weights, tests thousands of two-input weighted variation inequalities, and checks the four unweighted dimension regimes. Those finite checks corroborate the direct all-length proof; they do not prove the theorem by enumeration.

## Relationship to prior work

The MAD is a classical robust scale statistic, discussed in Rousseeuw and Croux (1993) as an estimator with high breakdown resistance and in Pearson, Neuvo, Astola and Gabbouj (2016) as the local scale used by moving Hampel filters. The latter article analyzes filtering rules, implosion sequences, weighted data replication and signal-recovery performance; its weighted windows change the statistic's input multiplicities rather than weighting the variation seminorm. Neither source establishes the present two-input, all-length, two-family-edge-weight coefficient.

Published analyses of running-median smoothing and finite-window min/max morphology concern different maps: the running median outputs a location statistic, whereas \(M_n\) outputs the least pairwise gap of each triple. Published studies of sliding standard deviation address a smooth quadratic scale and distinct coefficients. In particular, the exact \(2,3,4\) saturation and the independent input/output weight criterion do not follow by changing a normalization factor in these results. The proof explicitly identifies the anti-aligned neighboring MAD derivatives responsible for sharpness; this compatibility requires more than separate scalar Lipschitz bounds.

## Limitations

Only full, nonwrapping length-three windows, real data and positive variation-edge weights are covered. The theorem does not classify longer MAD windows, padded or cyclic boundaries, median-based outlier replacement, unequal observation replication inside the window, missing values or multidimensional data. A finite search of indexed literature cannot certify historical priority; an unindexed equivalent stability formula remains possible. No claim of independent verification is made.

## References

1. P. J. Rousseeuw and C. Croux, “Alternatives to the Median Absolute Deviation,” *Journal of the American Statistical Association* 88 (1993), 1273–1283, DOI: 10.1080/01621459.1993.10476408. Author-hosted full text: https://wis.kuleuven.be/stat/robust/papers/publications-1993/rousseeuwcroux-alternativestomedianad-jasa-1993.pdf.
2. R. K. Pearson, Y. Neuvo, J. Astola and M. Gabbouj, “Generalized Hampel Filters,” *EURASIP Journal on Advances in Signal Processing* 2016, article 87, published 5 August 2016, DOI: 10.1186/s13634-016-0383-6. Full open article: https://link.springer.com/article/10.1186/s13634-016-0383-6.
3. J. Astola, M. Gabbouj, Y. Neuvo and R. K. Pearson, “The Class of Generalized Hampel Filters,” *EUSIPCO* (2015), open conference record deposited 31 August 2015, DOI: 10.5281/zenodo.35878.
