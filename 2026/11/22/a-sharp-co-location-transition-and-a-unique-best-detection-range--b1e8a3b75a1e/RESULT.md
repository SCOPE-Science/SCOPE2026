# A unique detection width of maximum optimal spacing for two symmetric Gaussian cameras

## Finding

Let one animal's activity centre be distributed as $X\sim N(0,w^2I_2)$, with $w>0$. Two cameras at $\pm se_1$, $s\ge0$, detect it conditionally independently with probabilities $p\exp(-\|X\mp se_1\|^2/(2r^2))$, where $0<p<1$ is fixed and $r>0$ is the common detection width. For each fixed $r$, let $s_*(r)$ maximize the probability of at least one detection among symmetric placements. We study **the physical spacing $2s_*(r)$ as a function of width**, not the maximum detection probability as a function of width.

Let $k=w^2/r^2$ and $k_0=(1-p+\sqrt{1-p})/p$. The positive-spacing interval is $0<r<r_c=w/\sqrt{k_0}$. On that interval, $2s_*(r)$ is strictly increasing and then strictly decreasing, with exactly one turning point, a global maximum at $r_{\rm peak}=w/\sqrt{k_{\rm peak}}$. Here $k_{\rm peak}>k_0$ is the unique root in that interval of uncertainty ratios of
\[
\log\!\frac{p(1+k)^2}{1+2k}=\frac{2k^2}{2k^2+4k+1}.
\]
The spacing tends to zero as $r\downarrow0$ and as $r\uparrow r_c$, and remains zero for $r\ge r_c$. In the rare-detection limit $p\downarrow0$ at fixed $w$,
\[
k_{\rm peak}\sim\frac{2e}{p},\qquad r_{\rm peak}\sim s_*(r_{\rm peak})\sim w\sqrt{\frac{p}{2e}}.
\]
Thus, at the width of maximum optimal spacing, the physical gap is asymptotically twice the width. For $p=1/2$ and $w=1$, the width is approximately $0.3738449893$, the physical gap there is $0.6796510696$, and the co-location boundary is $r_c\approx 0.6435942529$.

## Fixed-width input (credited)

The same fixed-width solution is part of the all-dimension theorem in [1]: take $d=2$, $q=p$, $\ell=r$, $\sigma=w$, and identify its optimal half-separation with $s_*$. The cut-off and fixed-width optimizer are not asserted as contributions here. For completeness, conditional inclusion–exclusion and planar Gaussian integration give
\[
C(s)=\frac{2pr^2}{r^2+w^2}e^{-s^2/[2(r^2+w^2)]}
-\frac{p^2r^2}{r^2+2w^2}e^{-s^2/r^2}.
\]
For $s>0$ the positive-to-negative term ratio in $C'(s)$ starts at $p(1+k)^2/(1+2k)$ and strictly decreases to zero, since $1/r^2>1/[2(r^2+w^2)]$. Thus the unique maximizer has $s_*=0$ if this initial ratio is at most one, including equality, and otherwise
\[
\frac{s_*^2}{w^2}=\frac{2(1+k)}{k(1+2k)}\log\!\frac{p(1+k)^2}{1+2k}.
\]
The ratio increases strictly in $k>0$; setting it equal to one gives $k_0$.

## Proof of the width law

For $k>k_0$, put $A(k)=2(1+k)/(k(1+2k))$, $L(k)=\log[p(1+k)^2/(1+2k)]$, and $H(k)=s_*^2/w^2=A(k)L(k)$. Then
\[
h=-A'/A=\frac{2k^2+4k+1}{k(1+k)(1+2k)}>0,\quad
L'=\frac{2k}{(1+k)(1+2k)},\quad
T=\frac{L'}{h}=\frac{2k^2}{2k^2+4k+1}.
\]
In particular $H'=Ah(T-L)$. For $J=L-T$ one obtains
\[
J'=\frac{2k(4k^4+8k^3+4k^2-2k-1)}{(1+k)(1+2k)(2k^2+4k+1)^2}.
\]
The quartic has exactly one sign change in its coefficient sequence, is negative at zero, and tends to positive infinity. By Descartes' rule and continuity, $J$ first decreases, then increases on $k>0$. Since $J(k_0)=-T(k_0)<0$ and $J(k)=\log(pk/2)-1+o(1)\to\infty$, there is exactly one crossing on $k>k_0$. Hence $H$ increases and then decreases in $k$; the decreasing map $r=w/\sqrt{k}$ reverses the two branches and preserves their unique maximum. At $k\downarrow k_0$, $L\to0$; at $k\to\infty$, $H\sim\log(pk/2)/k\to0$. This proves strict unimodality and the zero endpoints.

As $p\downarrow0$, $k_0\sim 2/p$ and therefore $k_{\rm peak}\to\infty$. At this root $L=T\to1$ and $L=\log(pk_{\rm peak}/2)+o(1)$, so $p k_{\rm peak}/2\to e$. Because $A(k)\sim1/k$, the peak satisfies $s_*^2/w^2\sim1/k_{\rm peak}=r_{\rm peak}^2/w^2$ in this limit.

## Scope and relationship to other work

The novelty claim is limited to the width peak and rare-detection scaling. Reference [1] optimizes placement with the width fixed and uses its formula to study a dimension-dependent co-location barrier; its large-dimension limit is not the small-$p$ planar width optimization here. Reference [2] optimizes detections on a finite uniform integer path with geometric distance decay and certain detection at the trap site. Spatial capture–recapture design in [3] studies estimator performance, a different objective from expected distinct detections. Reference [4] minimizes expected worst distance to an active sensor in one dimension, not the probability of detecting a random animal under half-normal response. Historical priority for the width law is provisional.

The two identical devices are constrained to be symmetric about the known habitat centre. The model fixes $p$ as $r$ varies and permits independent registrations by co-located sensors. It does not model movement, non-Gaussian habitats, orientation, false positives, or statistical precision in abundance estimation. In fact, for fixed finite $s$, the probability $C(s)$ increases strictly with $r$: each conditional detection probability increases almost surely and the other is less than one. Since the optimum in $s$ is attained for every $r$, the optimal coverage also increases strictly with $r$ by testing the earlier optimizer at the larger width. There is no finite coverage-maximizing width in the stated model. The theorem neither chooses a width by maximizing coverage nor recommends a field placement.

## Verification

The analytic proof applies to all stated widths and baseline probabilities. The unchanged companion `verify.py` and `verification_certificate.json` from the frozen package remain applicable: the script reads no inputs and emits finite diagnostics with standard-library Python. The archived output reports 11,156 assertions, including exact-rational derivative identities, nine spatial quadratures, and finite placement and rare-detection checks. These diagnostics do not prove the general result and were inspected, not rerun, during the independent mathematical review.

## References

1. [A dimension-three co-location barrier for two Gaussian wildlife detectors](https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-a-dimension-three-co-location-barrier-for-two-gaussian-wildlife--e434a32821fc/RESULT.md), Finding, Assumptions and scope, and Relationship to prior work.
2. [Noncommuting detection-range and landscape-size limits for two ecological traps](https://github.com/Resultary/2026/blob/main/2026/10/26/SCOPE-noncommuting-detection-range-and-landscape-size-limits-for-two-e--4b47353a8a35/RESULT.md), Finding and Assumptions.
3. Sun, Fuller and Royle (2014), [Trap Configuration and Spacing Influences Parameter Estimates in Spatial Capture-Recapture Models](https://doi.org/10.1371/journal.pone.0088025), PLOS ONE 9, e88025.
4. Frasca, Garin, Gerencsér and Hendrickx (2014), [Optimal One-Dimensional Coverage by Unreliable Sensors](https://arxiv.org/abs/1404.7711).
