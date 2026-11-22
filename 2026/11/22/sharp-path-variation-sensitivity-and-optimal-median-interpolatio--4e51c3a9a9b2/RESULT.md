# Sharp path-variation sensitivity and optimal median interpolation for centred clipping

## Finding

For real data on an open path, coordinatewise clipping to a fixed-width interval centred at a sample median is individually variation diminishing but may be highly unstable for *differences of two inputs*. The sharp coefficient is exactly \(n-1\) for odd sample size. For even sample size, the choice of convention between the two central order statistics produces a sharp, attained stability phase diagram:
\[
K_n(\theta)=\max\{n-2,\;1+(n-2)\max(\theta,1-\theta)\}.
\]
Here \(0\le\theta\le1\), and the coefficient is independent of the positive clipping threshold. The lower/upper order-statistic conventions have \(K_n=n-1\), whereas ordinary midpoint centring has \(K_n=n-2\) for every even \(n\ge4\). The entire minimizer set for even \(n\ge6\) is
\[
\frac1{n-2}\le\theta\le1-\frac1{n-2},
\]
while the unique minimizer at \(n=4\) is \(\theta=1/2\). For two observations, \(K_2=1\) for every \(\theta\).

## Assumptions and scope

Let \(n\ge2\) be an integer, \(\tau>0\), and let \(x=(x_1,\ldots,x_n)\in\mathbb R^n\). Write \(x_{(1)}\le\cdots\le x_{(n)}\) for sorted values, counting repeated values with multiplicity. If \(n=2m+1\), define the centre \(c(x)=x_{(m+1)}\). If \(n=2m\), choose \(\theta\in[0,1]\) and define
\[
c(x)=(1-\theta)x_{(m)}+\theta x_{(m+1)}.
\]
The centred clipping operator is
\[
(Cx)_i=c(x)+\operatorname{clip}_{[-\tau,\tau]}(x_i-c(x))
=\min\{c(x)+\tau,\max\{c(x)-\tau,x_i\}\}.
\]
For any real path vector \(h\), let \(V_n(h)=\sum_{i=1}^{n-1}|h_{i+1}-h_i|\). The quotient is taken only over pairs with positive input-difference variation, so constants are factored out. These definitions impose no monotonicity or boundedness assumption on the data.

## Proof

**1. A local operator-norm reduction.** The map \(C\) is continuous, translation equivariant and piecewise affine. On a strict chamber where the order of observations, clipping decisions and the two relevant order-statistic indices are fixed, its differential \(J\) has, in each row \(i\), either the row \(e_i^\mathsf T\) (unclipped coordinate) or the same centre row \(p^\mathsf T\) (clipped coordinate). For odd \(n\), \(p=e_a\) where \(a\) is the spatial index of the unique median. For even \(n\), \(p=(1-\theta)e_a+\theta e_b\), with \(a\ne b\) the spatial indices of the lower and upper central order statistics, respectively. At an even-size configuration where the two central order statistics lie outside the clipping interval, the same row description still applies: the relevant rows simply use \(p\), rather than \(e_a\) or \(e_b\). Thus there is no requirement to assume that central observations are unclipped for the upper bound. In every case \(J\mathbf1=\mathbf1\).

For each cut \(j\in\{1,\ldots,n-1\}\), define the step \(H^{(j)}_i=\mathbf1_{\{i>j\}}\). Any \(h\) has the decomposition
\[
h=h_1\mathbf1+\sum_{j=1}^{n-1}(h_{j+1}-h_j)H^{(j)}.
\]
Consequently the exact induced \(V_n\)-seminorm of any such row-stochastic affine differential is
\[
\|J\|_{V_n}=\max_{1\le j<n} V_n(JH^{(j)}).
\]
The upper inequality follows by triangle inequality, and each single-step vector attains equality for the maximizing column. The piecewise-affine segment formula, extended by continuity across chamber boundaries, bounds the global two-input coefficient by the largest local differential norm. Conversely, a strict chamber with a maximizing differential and a sufficiently small step perturbation yields actual finite inputs attaining that local norm.

**2. Odd sample sizes.** Every component of \(JH^{(j)}\) is either \(0\) or \(1\), because the centre derivative is a single input coordinate. Therefore its path variation is at most \(n-1\). Place the median input at the first spatial position and choose the step at the first edge. Make positions \(2,4,6,\ldots\) unclipped and positions \(3,5,7,\ldots\) clipped. The resulting step response alternates \(0,1,0,1,\ldots\) and has variation \(n-1\). These strict decisions are feasible by distributing half of the remaining observations strictly below and half strictly above the median, using small absolute deviations for the designated unclipped entries and deviations larger than \(\tau\) for the others.

**3. Even sample sizes: upper bound.** Let the centre response to a cut be \(s=(1-\theta)H^{(j)}_a+\theta H^{(j)}_b\). If both central indices lie on the same side of the cut, then \(s\in\{0,1\}\), and the response is constant on that side. Since that side contains at least two positions, \(V_n(JH^{(j)})\le n-2\). If the central indices straddle the cut, then \(s\in\{\theta,1-\theta\}\). The entries on the left are in \(\{0,s\}\), those on the right are in \(\{s,1\}\). Hence
\[
V_n(JH^{(j)})\le (j-1)s+1+(n-j-1)(1-s)
\le1+(n-2)\max\{\theta,1-\theta\}.
\]
Taking the larger of the two bounds gives the asserted upper coefficient, including \(n=2\).

**4. Even sample sizes: sharpness.** For \(n\ge4\), put the two central-rank observations at spatial positions \(1,2\), make both strictly unclipped, and choose the cut \(H^{(2)}\). Make positions \(3,5,7,\ldots\) unclipped and \(4,6,8,\ldots\) clipped. Its response is \(0,0,1,0,1,0,\ldots\), whose variation is \(n-2\). For the other branch, choose \(H^{(1)}\), put the lower median at position \(1\) and upper median at position \(2\) when \(\theta\le1/2\), and reverse these positions otherwise. Keep both central observations unclipped; alternate unclipped/clipped decisions from the second position onward. The response is
\[
0,1,s,1,s,\ldots,1,\qquad s=\min\{\theta,1-\theta\},
\]
so its variation is \(1+(n-2)(1-s)\). All masks have strict realizing inputs: choose the two central observations sufficiently close, assign exactly \(m-1\) remaining values below both and \(m-1\) above both, and independently choose sufficiently small or sufficiently large magnitudes to realize the specified clipping decisions. A sufficiently small positive step perturbation stays in that chamber. For \(n=2\), a strict all-unclipped input pair attains the coefficient \(1\). The maximum of the two branches is therefore attained at every parameter.

**5. Individual variation and optimality.** For fixed \(x\), the scalar map \(t\mapsto\min\{c(x)+\tau,\max\{c(x)-\tau,t\}\}\) is nondecreasing and 1-Lipschitz, so \(V_n(Cx)\le V_n(x)\). The even-size minimax statement follows directly by solving \(1+(n-2)\max\{\theta,1-\theta\}\le n-2\); for \(n=4\) this forces the midpoint, and for every even \(n\ge6\) it yields exactly the displayed interval. The two-sample case is separately \(K_2=1\).

## Verification

Run `python3 verify_median_centered_clipping.py` using only the Python standard library. The checker exhaustively enumerates all local clipping masks, cut steps and possible median-index locations for \(2\le n\le8\), including five rational interpolation parameters for even lengths; generates strict rational realizing input pairs up to \(n=19\); and tests 1,350 randomly selected rational pairs. Its expected completion markers are `ALL_PIECEWISE_AFFINE_FACE_MASKS_PASS`, `EXACT_STRICT_MEDIAN_RANK_AND_CLIPPING_WITNESSES_PASS`, `RANDOM_RATIONAL_TWO_INPUT_AND_ONE_INPUT_STRESS_PASS`, and `MEDIAN_ANCHORED_CLIPPING_ALL_CHECKS_PASS`. Finite checks are supplementary: the proof above applies to all integer sample sizes, all positive clipping thresholds, and all \(\theta\in[0,1]\).

## Relationship to prior work

The archival median/outlier literature motivates a global centre and robust clipping, but the present operator is distinct from the moving-window *hard replacement* rule with a data-dependent MAD threshold in Pearson–Neuvo–Astola–Gabbouj (2016). The sharp Gini-variation formula for empirical-quantile Winsorization concerns order-statistic cutoffs in a complete-pair dispersion seminorm, not a fixed-distance median band in path variation. The sharp path-variation result for arithmetic-mean-centred clipping likewise does not imply the rank-centred case or the even-sample interpolation phase diagram. These are comparisons of claims, not a guarantee of global historical novelty.

## Limitations

Only real finite open paths and a common positive absolute clipping radius are treated. The location centre is one sample median or an interpolation between the two central order statistics, rather than a MAD-adaptive threshold or moving-window median. Weighted paths, cycles, general graphs, vector data, and discontinuous hard-replacement Hampel filters are not covered. The result provides no statistical-risk or outlier-breakdown guarantee. Historical equivalents outside the inspected literature may exist.

## References

1. R. K. Pearson, Y. Neuvo, J. Astola, and M. Gabbouj, *Generalized Hampel Filters*, EURASIP Journal on Advances in Signal Processing **2016**, article 87 (first published 5 August 2016), https://doi.org/10.1186/s13634-016-0383-6.
2. C. Leys, C. Ley, O. Klein, P. Bernard, and L. Licata, *Detecting outliers: do not use standard deviation around the mean, use absolute deviation around the median*, Journal of Experimental Social Psychology **49** (2013), 764–766, https://doi.org/10.1016/j.jesp.2013.03.013.
3. *Sharp two-input Gini stability of empirical-quantile Winsorization*, public mathematical finding (2026), identifier `ddc6dbb8-f632-4a2c-8c57-031330847d87`.
4. *Sharp path-variation sensitivity of mean-centered clipping*, public mathematical finding (2026), identifier `fa0e6367-54f5-494e-90ff-94be263e3666`.
