# Sharp two-row progress loss under multiplicatively stale residual-power selection

## Finding

For a consistent nonsingular two-row real linear system with unit row normals, fix a power exponent \(p>0\), a multiplicative residual-error budget \(\varepsilon>0\), and a relaxation \(0<\beta<2\). A row is sampled with probability proportional to the \(p\)-th power of a possibly stale residual *magnitude*, but the chosen projection correction uses its **current exact residual**. Each stale magnitude must lie between \(e^{-\varepsilon}\) and \(e^{\varepsilon}\) times the corresponding current magnitude. Compare the expected one-step **squared solution-error decrease** with that of sampling using the current residual magnitudes.

For current residual magnitudes in ratio \(z\in(0,1]\), the smallest possible stale-to-current expected-decrease ratio is exactly
\[
R_{p,\varepsilon}(z)=
\frac{(1+e^{2p\varepsilon}z^{p+2})(1+z^p)}
{(1+e^{2p\varepsilon}z^p)(1+z^{p+2})}.
\]
For every \(p,\varepsilon>0\), this expression has a **unique** global minimum at \(z_*=z_*(p,\varepsilon)\in(0,1)\), characterized by the unique zero
\[
\frac{p}{1+e^{2p\varepsilon}z_*^p}
-\frac{2z_*^2}{1-z_*^2}
-\frac{(p+2)z_*^{p+2}}{1+z_*^{p+2}}=0.
\]
The sharp best-possible uniform competitive factor is \(C(p,\varepsilon)=R_{p,\varepsilon}(z_*)\). In the high-exponent limit,
\[
\boxed{\lim_{p\to\infty}C(p,\varepsilon)=e^{-4\varepsilon}.}
\]
No row angle, relaxation, or selection-only snapshot with the stipulated multiplicative guarantee can worsen these constants. For every fixed pair of independent unit rows, all finite-\(p\) bounds are attained at a suitable current state and stale magnitude vector. Thus even arbitrarily aggressive sampling retains a sharply quantifiable fraction of *one-step progress* when residual errors are multiplicatively controlled; this is **not** a convergence theorem for fully asynchronous updates.

## Assumptions and scope

Let \(A\in\mathbb R^{2\times2}\) have linearly independent unit Euclidean row normals \(a_1^{\mathsf T},a_2^{\mathsf T}\), and let \(Ax_\star=b\) be consistent. At the current iterate \(x\), write \(e=x-x_\star\) and \(r_i=b_i-a_i^{\mathsf T}x=-a_i^{\mathsf T}e\). Assume both magnitudes are nonzero, relabel the equations so \(|r_1|\ge |r_2|\), and write \(z=|r_2|/|r_1|\). The result for a zero current residual is the continuous boundary value: a row with zero residual has zero selection probability for positive \(p\) and no effect on the update.

The selector receives numbers \(\widetilde r_1,\widetilde r_2\), possibly signed, whose **magnitudes** obey \(e^{-\varepsilon}|r_i|\le|\widetilde r_i|\le e^{\varepsilon}|r_i|\) separately. It samples \(I\) from
\[
\Pr(I=i)=\frac{|\widetilde r_i|^p}{|\widetilde r_1|^p+|\widetilde r_2|^p},
\qquad i=1,2.
\]
After sampling, the algorithm rereads the *current* residual and updates \(x^+=x+\beta r_Ia_I\). It does not reuse \(\widetilde r_I\) in the correction, and no other update is committed before this step. The reference selector uses identical correction but replaces the stale selection weights with \(|r_i|^p\). We compare conditional expectations at a fixed \(x\), provided \(e\ne0\); both expected decreases are strictly positive. Nothing here assumes that every magnitude-compatible stale vector is reachable along a prescribed asynchronous trajectory: the uncertainty set is an explicit robust-selection model.

## Proof

**1. The exact progress identity.** For either row \(i\), using \(\|a_i\|_2=1\) and \(a_i^{\mathsf T}e=-r_i\), direct expansion gives
\[
\|e\|_2^2-\|e+\beta r_ia_i\|_2^2
=\beta(2-\beta)r_i^2.
\]
This quantity is positive for each nonzero residual since \(0<\beta<2\). After division by the common \(\beta(2-\beta)|r_1|^2\), the expected decrease under a sampling probability \(s=\Pr(I=2)\) is simply \(1-s+sz^2\). The ideal sampler has \(s_0=z^p/(1+z^p)\), so its normalized expected decrease is \((1+z^{p+2})/(1+z^p)\).

**2. The worst permitted stale selector.** For \(z<1\), the expected decrease \(1-s+sz^2\) strictly decreases in \(s\). The stale odds of selecting row two over row one satisfy
\[
\frac{s}{1-s}=\left(\frac{|\widetilde r_2|}{|\widetilde r_1|}\right)^p
\le e^{2p\varepsilon}z^p.
\]
Equality is realized by \(|\widetilde r_2|=e^{\varepsilon}|r_2|\) and \(|\widetilde r_1|=e^{-\varepsilon}|r_1|\). Write \(U=e^{2p\varepsilon}>1\). The least normalized stale expected decrease is \((1+Uz^{p+2})/(1+Uz^p)\); dividing by the ideal decrease gives the claimed ratio. Elementary subtraction yields the useful exact factorization
\[
1-R_{p,\varepsilon}(z)
=\frac{(U-1)z^p(1-z^2)}{(1+Uz^p)(1+z^{p+2})}.
\tag{1}
\]
For \(0<z<1\) the loss is strictly positive. At \(z=1\), both projection choices decrease squared error equally, so the ratio is exactly one, and as \(z\downarrow0\) it also tends to one. Because \(A\) is invertible, any prescribed real residual pair arises from a unique current error \(e=-A^{-1}r\). A stale iterate with those extremal residuals is likewise algebraically realizable. Hence this is a sharp robust bound for **every** fixed admissible pair of rows, not just for orthogonal rows.

**3. Uniqueness of the worst residual imbalance.** Maximize the positive right-hand side of (1) over \(z\in(0,1)\). Its logarithmic derivative multiplied by \(z\) is
\[
F(z)=\frac{p}{1+Uz^p}
-\frac{2z^2}{1-z^2}
-\frac{(p+2)z^{p+2}}{1+z^{p+2}}.
\]
Every displayed term is strictly decreasing as a function of \(z>0\): the first term decreases, the middle negative term decreases, and the last negative term decreases. Therefore \(F\) is strictly decreasing, with \(F(0+)=p>0\) and \(F(1-)=-\infty\). There is precisely one zero \(z_*\in(0,1)\); the positive loss in (1) increases before it and decreases after it. Thus \(z_*\) is the unique global loss maximum and \(C(p,\varepsilon)=R_{p,\varepsilon}(z_*)\) is the sharp minimum.

**4. The exact high-power barrier.** Set \(a=e^{-2\varepsilon}\in(0,1)\). For any fixed \(z\) with \(a<z<1\), \(z^p\to0\) but \(Uz^p=(z/a)^p\to\infty\). In consequence \(R_{p,\varepsilon}(z)\to z^2\), giving \(\limsup_{p\to\infty}C(p,\varepsilon)\le z^2\). Letting \(z\downarrow a\) proves \(\limsup C\le a^2\).

For the opposite inequality, take an arbitrary sequence \(p_j\to\infty\), let \(z_j\in[0,1]\) realize the minimum (with the continuous endpoint extension), and pass to a convergent subsequence \(z_j\to z_\infty\). If \(z_\infty<a\), then \((z_j/a)^{p_j}\to0\), so the two probabilities of selecting row two both vanish and \(R_{p_j,\varepsilon}(z_j)\to1\ge a^2\). If \(z_\infty\ge a\), the stale normalized expected squared residual lies in \([z_j^2,1]\), while the ideal one is at most one; hence \(R_{p_j,\varepsilon}(z_j)\ge z_j^2\to z_\infty^2\ge a^2\). All convergent subsequences obey the lower bound, and \(C\) is bounded, so \(\liminf C\ge a^2\). Combining gives \(\lim C=a^2=e^{-4\varepsilon}\).

For \(\varepsilon=0\), the two selectors coincide and the ratio is identically one; \(p=0\) also gives identical uniform sampling, with the convention that zero residuals are included. The strict uniqueness assertion concerns only \(p,\varepsilon>0\).

## Verification

A standalone Python 3 standard-library checker is included as \(\texttt{CHECK.py}\). Run \(\texttt{python3 CHECK.py}\) from the extracted package. It computes exact-rational Kaczmarz updates for two nonorthogonal rational unit rows and compares their expected progress ratios to the closed formula over multiple powers, staleness factors, residual ratios and step relaxations; it also checks admissible perturbation corners. Separate numerical checks use monotone bisection for the unique stationary root, a grid of test imbalances, and progressively increasing sampling exponents. All checks passed in the packaged replay, totaling **18,098 assertions**. These finite experiments are corroborative; the proof above covers the full real domain and the infinite exponent limit.

For the reproducible benchmark \(e^{\varepsilon}=3/2\), the limiting sharp factor is \((2/3)^4=16/81\). At exponent \(p=4\), one obtains approximately \(z_*=0.5634495\) and \(C(4,\varepsilon)\approx0.541817\). These are illustrations, not the basis of the proof.

## Relationship to prior work

Coleman's *Adaptive Row Selection Meets Asynchrony in Randomized Kaczmarz* (arXiv:2607.08313) considers residual-power row selection under stale and inconsistent reads and supplies the practical motivation for separating the selection residual from the correction residual. Its experimental concurrency cliff does not state a multiplicative-error robust competitive ratio, a unique worst residual imbalance, or the exact high-power limit. The present result instead isolates **one** corrected read under a prescribed multiplicative envelope; it neither explains the asynchronous interference cliff nor characterizes parallel trajectories.

Steinerberger's *A Weighted Randomized Kaczmarz Method for Solving Linear Systems* (arXiv:2007.02910) studies current-residual weighted sampling and acceleration; Gower, Molitor, Moorman and Needell's *Adaptive Sketch-and-Project Methods for Solving Linear Systems* (arXiv:1909.03604) analyzes adaptive residual-based choices and their convergence. Both provide foundational current-residual comparisons, not the explicit selection-only error uncertainty optimization here. Existing sharp analyses of concurrent two-row Kaczmarz handle simultaneous stale *corrections* (multiple workers add corrections from the same snapshot); their update operator is fundamentally different from the fresh-correction, perturbed-selection model here. Likewise existing exact two-step residual-sampling results compare successive fresh selections rather than multiplicative selection error.

General multiplicative importance-weight comparisons may imply non-sharp safety estimates; the new mathematical statement is the **exact** minimizer for every finite exponent and the attained limiting \(e^{-4\varepsilon}\) frontier in this row-action setting. No claim is made to invent the progress identity, residual-power sampling, or robust probability normalization.

## Limitations

The theorem covers two independent unit rows, consistent equations, a single exact-arithmetic Kaczmarz correction, \(0<\beta<2\), positive residual powers, and relative (not additive) multiplicative errors in row-selection magnitudes. Its worst-case perturbations need not come from a prescribed delay process; a small additive error in a vanishing residual does not satisfy the hypotheses. The sharp constant measures the *fraction of conditional expected squared-error progress* retained relative to a fresh power-weighted selector, not the ratio of residual norms, whole-iteration contraction factors, wall-clock efficiency, or convergence rates for asynchronous histories. A similar sharp robust-sampling formula could exist in older work not indexed or fully accessible; the bibliographic comparison is not independently certified.

## References

1. E. Coleman, *Adaptive Row Selection Meets Asynchrony in Randomized Kaczmarz*, arXiv:2607.08313v1, first posted 2026-07-09. https://arxiv.org/abs/2607.08313
2. S. Steinerberger, *A Weighted Randomized Kaczmarz Method for Solving Linear Systems*, arXiv:2007.02910, first posted 2020-07-06. https://arxiv.org/abs/2007.02910
3. R. M. Gower, D. Molitor, J. D. Moorman and D. Needell, *Adaptive Sketch-and-Project Methods for Solving Linear Systems*, arXiv:1909.03604, first posted 2019-09-09. https://arxiv.org/abs/1909.03604
4. *Sharp stale-batch safety frontier for partially greedy two-row Kaczmarz*, published research record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-sharp-stale-batch-safety-frontier-for-partially-greedy-two-row-k--950481c92526
5. *A sharp concurrency frontier for residual-weighted two-row Kaczmarz*, published research record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-a-sharp-concurrency-frontier-for-residual-weighted-two-row-kaczm--3a196be2a758
6. *Sharp adaptive-sampling stability discontinuity under frozen-snapshot Kaczmarz batches*, published research record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-adaptive-sampling-stability-discontinuity-under-frozen-sna--0ca374658cd7
