# The low-support spectrum and inverse rigidity of three-tap cross-STFTs on prime cycles

## Finding
Let \(p\ge 7\) be prime, and let \(f,g:\mathbb Z_p\to\mathbb C\) each be supported at exactly three positions. Use the unnormalized short-time Fourier transform (STFT)
\[
V_gf(x,k)=\sum_{t\in\mathbb Z_p}f(t)\overline{g(t-x)}e^{-2\pi i kt/p}.
\]
Write \(S(f,g)=|\operatorname{supp}V_gf|\). Then the complete portion of the support spectrum strictly below \(6p-3\) is
\[
\boxed{\{S(f,g):S(f,g)<6p-3\}=\{5p-4,5p-3,5p-2,5p-1,5p\}.}
\]
Every one of the five values occurs. No support size from \(5p+1\) through \(6p-4\) occurs, while \(6p-3\) itself occurs. In particular, a growing forbidden gap separates the lowest five support levels from the next possible level.

The **inverse assertion** is that every pair with \(S(f,g)<6p-3\) has both three-point supports equal to arithmetic progressions with the same nonzero step, allowing independent translations. More precisely, after translating both supports and scaling their common step to one, write their nonzero entries as \((a_0,a_1,a_2)\) and \((b_0,b_1,b_2)\) at sites \(0,1,2\). Put \(\mu_p=\{e^{2\pi i j/p}:0\le j<p\}\), and define
\[
\begin{aligned}
r_-&=-\frac{a_0\overline{b_1}}{a_1\overline{b_2}},
& r_+&=-\frac{a_1\overline{b_0}}{a_2\overline{b_1}},\\
P(z)&=a_0\overline{b_0}+a_1\overline{b_1}z+a_2\overline{b_2}z^2,
& h&=|\{z\in\mu_p:P(z)=0\}|.
\end{aligned}
\]
The exact, coefficient-dependent support formula is
\[
\boxed{S(f,g)=5p-\mathbf1_{\{r_-\in\mu_p\}}-\mathbf1_{\{r_+\in\mu_p\}}-h,\qquad 0\le h\le2.}
\]
Thus a pair minimizes support, giving \(5p-4\), **if and only if** both displayed ratios are \(p\)-th roots of unity and \(P\) has two distinct \(p\)-th roots. Furthermore, a pair has support \(5p-3\) **if and only if** both ratios are sampled roots of unity and \(P\) has a double root in \(\mu_p\).

The numerical lower bound \(5p-4\) for two three-supported functions is already contained in the published work of Krahmer, Pfander and Rashkov. The claims here concern the complete low spectrum, the large intervening support gap, the sharp second-level onset, the inverse support geometry and the coefficient-level equality classification, **not** rediscovery of that known numerical bound.

## Assumptions and scope
The group is \(\mathbb Z_p\) for every prime \(p\ge7\). Both supports have cardinality exactly three and the six coefficients on their supports are nonzero. No assumption of equal coefficients or a self-window \(f=g\) is made. Frequency normalization does not affect support counts. The theorem is invariant under independent translations of the supports, simultaneous invertible dilation of their common step, and multiplication of either input by a nonzero scalar. Coefficient formulas use a normalization with both supports at \(\{0,1,2\}\); the resulting support count does not depend on the normalization.

## Proof
**1. Sharp separation by the number of active delays.** Set \(F=\operatorname{supp}f\), \(G=\operatorname{supp}g\), and \(D=F-G\). For each \(x\in D\), let \(k_x=|F\cap(x+G)|\). The frequency row \(V_gf(x,\cdot)\) is the discrete Fourier transform of a nonzero vector supported on exactly \(k_x\) points. The prime-order Fourier uncertainty theorem (equivalently, nonsingularity of all square minors of the prime Fourier matrix) gives this row at least \(p+1-k_x\) nonzero frequencies. Since every ordered pair from \(F\times G\) contributes to exactly one delay, \(\sum_{x\in D} k_x=|F||G|=9\). Hence
\[
S(f,g)\ge\sum_{x\in D}(p+1-k_x)=|D|(p+1)-9.
\]
Cauchy–Davenport yields \(|D|\ge\min(p,3+3-1)=5\). If \(|D|\ge6\), then
\[
S(f,g)\ge6(p+1)-9=6p-3.
\]
Therefore every pair below this threshold must have \(|F-G|=5\).

**2. Inverse geometry of the five-delay case.** Because \(p\ge7\), the equality \(|F-G|=5=|F|+|G|-1\le p-2\) is in the inverse range of Vosper's theorem. It follows that \(F\) and \(-G\) are length-three arithmetic progressions with a common nonzero step (the sign of a step may be reversed without changing a three-point progression). Thus \(F\) and \(G\) are progressions with a common unoriented step. Independent support translations and multiplication of indices by the step's inverse reduce to \(F=G=\{0,1,2\}\). These operations only permute STFT rows/frequencies and multiply their entries by unimodular factors, so they preserve \(S(f,g)\).

**3. Exact five-row computation.** Put \(z=e^{-2\pi i k/p}\). Apart from one overall nonzero phase factor in each row, the five potentially nonzero rows indexed by \(x=-2,-1,0,1,2\) are
\[
\begin{aligned}
x=-2 &: a_0\overline{b_2},\\
x=-1 &: a_0\overline{b_1}+a_1\overline{b_2}z,\\
x=0 &: P(z)=a_0\overline{b_0}+a_1\overline{b_1}z+a_2\overline{b_2}z^2,\\
x=1 &: z(a_1\overline{b_0}+a_2\overline{b_1}z),\\
x=2 &: a_2\overline{b_0}z^2.
\end{aligned}
\]
The two outer rows each have \(p\) nonzeros. The adjacent rows each lose exactly one nonzero frequency if and only if their unique roots \(r_-\), respectively \(r_+\), belong to \(\mu_p\). The central row loses precisely \(h\in\{0,1,2\}\) frequencies. Summation proves the boxed formula and the complete five-value upper-and-lower range. In particular, minimum support \(5p-4\) occurs exactly under the simultaneous two-ratio/two-central-root condition.

The stronger characterization at level \(5p-3\) follows from Vieta's formula. If \(z_1,z_2\) are the roots of \(P\) counted with multiplicity, then
\[
\boxed{z_1z_2=\frac{a_0\overline{b_0}}{a_2\overline{b_2}}=r_-r_+.}
\]
If the central polynomial has two **distinct** roots in \(\mu_p\), then their product belongs to \(\mu_p\), so membership of either adjacent-row root forces the other root into \(\mu_p\). Conversely, if both adjacent-row roots belong to \(\mu_p\) and the central polynomial has one sampled root, then the second algebraic root must also belong to \(\mu_p\). Thus a total of exactly three cancellations cannot arise from two distinct central roots and one adjacent cancellation: it necessarily consists of both adjacent cancellations and a single distinct central root of algebraic multiplicity two. The converse is immediate from the exact formula.

**4. Every level and the first next level occur.** Let \(\zeta=e^{2\pi i/p}\), \(r=2\cos(2\pi/p)>0\), and display coefficient triples \((a_0,a_1,a_2)\) and \((b_0,b_1,b_2)\) for both supports \(\{0,1,2\}\):

| Number of zero STFT samples in the five active rows | \((a_0,a_1,a_2)\) | \((b_0,b_1,b_2)\) | Support count |
| --- | --- | --- | --- |
| 0 | \((1,1,1)\) | \((1,1,1)\) | \(5p\) |
| 1 | \((1,1,1)\) | \((1,-1,2)\) | \(5p-1\) |
| 2 | \((1,-1,1)\) | \((1,1,1)\) | \(5p-2\) |
| 3 | \((1,-\sqrt2,1)\) | \((1,\sqrt2,1)\) | \(5p-3\) |
| 4 | \((1,-\sqrt r,1)\) | \((1,\sqrt r,1)\) | \(5p-4\) |

For the zero-cancellation example, the adjacent roots are \(-1\notin\mu_p\), and \(1+z+z^2\) has no sampled roots because \(p\ne3\). For the one-cancellation example, the central polynomial is \(1-z+2z^2\) and has no unit-circle root at an odd-order root of unity: equality \(|1+2z^2|=|z|=1\) would force \(z^2=-1\), impossible for odd \(p\). Its other row has exactly one sampled root. The remaining cases have central polynomials \(1-z+z^2\), \((1-z)^2\), and \(1-rz+z^2\), respectively, with adjacent-row cancellations as predicted. In the last case the central roots are \(\zeta,\zeta^{-1}\), both sampled and distinct. Thus all five low support levels are realized.

Finally, to realize \(6p-3\), take \(f\) supported on \(\{0,1,2\}\) with values \((1,-1,1)\), and \(g\) supported on \(\{0,1,3\}\) with values \((1,1,-1)\). There are exactly six delay rows, with overlap sizes \((1,1,2,2,2,1)\). The three two-overlap rows each vanish exactly once, at frequency zero, and the three one-overlap rows never vanish. Hence \(S(f,g)=6p-3\), proving sharpness of the threshold. Together with steps 1–3 this completes the classification.

## Verification
The accompanying standalone `verify.py` directly constructs the complex STFT for primes \(7,11,13,17,23,31\) and verifies the five explicit support levels, their five-row zero counts, and the sharp six-row onset. It also exhaustively enumerates all ordered pairs of three-point support sets for primes \(7,11,13\), checks the lower-bound geometry, and confirms Vosper's common-step conclusion in every five-delay case. Running `python3 verify.py` prints `THREE_TAP_CROSS_STFT_PASS`. The experiments are finite consistency checks; Cauchy–Davenport, Vosper, the prime Fourier uncertainty theorem and the five-row algebra constitute the proof for every prime \(p\ge7\).

## Relationship to prior work
Krahmer, Pfander and Rashkov, *Uncertainty in time-frequency representations on finite Abelian groups and applications* (2006 preprint, 2008 journal), Proposition 4.4, already establish the numerical lower bound \(5p-4\) for a pair of exactly three-supported signals/windows on a prime cyclic group. Their proof uses active-translation counting and prime Fourier uncertainty. The result here does not claim that numerical bound or that row-counting mechanism as new. It adds the precise low support spectrum, a growing gap above it, the exact first subsequent attainable level, the inverse common-progression geometry, and a complete algebraic characterization of every low-level support count and the minimizers.

Nicola, *The uncertainty principle for the short-time Fourier transform on finite cyclic groups: cases of equality*, arXiv:2204.14176 (first posted 29 April 2022), classifies equality at the global \(p\)-point STFT support minimum. It does not identify low strata for exactly three-supported pairs. Fernández, Galbis and Martínez (2014) study localization operators and different global discrete STFT uncertainty statements, not this fixed-sparsity five-row classification.

The published result *Parity-rigid ambiguity-support spectra for primitive three-tap cyclic signals* determines the self-window subcase \(f=g\) on common progressions; for odd orders it allows only \(5p,5p-2,5p-4\). The independent cross-window problem here admits both previously excluded adjacent levels \(5p-1\) and \(5p-3\), and the inverse statement covers all three-point support pairs rather than assuming progression geometry. A separate two-sparse STFT trichotomy concerns pairs of two-supported functions and cannot imply this six-coefficient classification.

## Limitations
The classification requires prime order at least seven and exactly three nonzero entries in **both** inputs. It does not describe support counts at or above \(6p-3\) beyond showing that the threshold is sharp. The inverse conclusion relies on Vosper's theorem and need not hold for general composite cyclic groups. The original published numerical bound is not new. Unindexed specialist results may contain equivalent support-spectrum formulations; no claim of exhaustive historical priority or independent verification is made.

## References
1. F. Nicola, *The uncertainty principle for the short-time Fourier transform on finite cyclic groups: cases of equality*, arXiv:2204.14176 (first posted 2022-04-29), *Journal of Functional Analysis* 284 (2023), 109924. Primary MSC2020 setting: 42B10.
2. F. Krahmer, G. E. Pfander and P. Rashkov, *Uncertainty in time-frequency representations on finite Abelian groups and applications*, arXiv:math/0611493 (first posted 2006-11-16), *Applied and Computational Harmonic Analysis* 25 (2008), 209–225; especially Proposition 4.4.
3. T. Tao, *An uncertainty principle for cyclic groups of prime order*, arXiv:math/0308286 (2003), *Mathematical Research Letters* 12 (2005), 121–127.
4. A. G. Vosper, *The critical pairs of subsets of a group of prime order*, *Journal of the London Mathematical Society* 31 (1956), 200–205.
5. C. Fernández, A. Galbis and E. Martínez, *Localization operators and an uncertainty principle for the discrete short time Fourier transform*, 2014, available as an open-access research article.
6. *Parity-rigid ambiguity-support spectra for primitive three-tap cyclic signals*, published research record (2026), exact self-window progression support classification.
7. *Exact support trichotomy for two-sparse prime cyclic STFTs*, published research record (2026), two-sparse pair classification.
