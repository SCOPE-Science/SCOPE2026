# A dimension-three co-location barrier for two Gaussian wildlife detectors

## Finding

Two independent detectors can gain from being separated when their target's location is uncertain. A sharp *spatial-dimension obstruction* changes that conclusion: in an isotropic Gaussian model, the planar case permits beneficial separation at perfect baseline detection for every positive location uncertainty, but in three or more spatial dimensions there is a nonzero range of uncertainty in which **no admissible detector quality can make separation optimal**.

Let the integer spatial dimension be \(d\ge 1\), the prior spatial variance be \(\sigma^2>0\), the common half-normal detection length be \(\ell>0\), the baseline detection probability be \(0<q\le1\), and the two detector locations be \(\pm a e_1\), with \(a\ge0\). Set \(s=\sigma^2/\ell^2\) and
\[
q_c(s,d)=\frac{(1+2s)^{d/2}}{(1+s)^{d/2+1}}.
\]
The **unique** placement maximizing the chance of detection at least once, within this symmetric family, is
\[
a_*(s,d,q)^2=\frac{2\ell^2(1+s)}{1+2s}\left[\log\frac{q}{q_c(s,d)}\right]_+,
\qquad [u]_+=\max\{u,0\}.
\]
In particular, separation is strictly beneficial if and only if \(q>q_c(s,d)\).

For \(d=1,2\), \(q_c(s,d)<1\) at every \(s>0\), so perfect baseline detection \(q=1\) always favors positive separation. For every integer \(d\ge3\), there is exactly one positive \(s_d\) satisfying
\[
(1+2s_d)^d=(1+s_d)^{d+2}.
\]
For the entire interval \(0<s\le s_d\), co-location is optimal for **every** \(0<q\le1\). For \(s>s_d\), separation is optimal exactly when \(q>q_c(s,d)\). The first two spatial thresholds are
\[
s_3=0.63770838850224\ldots,\qquad s_4=\frac{1+\sqrt5}{2}.
\]
Their high-dimensional growth obeys the sharp asymptotic
\[
s_d=2^{d/2}-\frac d4-1+O\!\left(d^2 2^{-d/2}\right)
\quad(d\longrightarrow\infty).
\]

## Assumptions and scope

The target location at a fixed time is a random vector \(X\sim N(0,\sigma^2 I_d)\) on unbounded Euclidean space, and, **conditional on \(X\)**, the two detections are independent Bernoulli variables with probabilities
\[
g_\pm(X)=q\exp\!\left(-\frac{\|X\mp a e_1\|^2}{2\ell^2}\right).
\]
The single scientific objective is \(\mathbb P(\text{at least one detector succeeds})\). All parameters except the nonnegative half-separation \(a\) are held fixed. The Gaussian location prior and the Gaussian distance-response kernel are distinct model assumptions. Detector coordinates must be symmetric about the known prior center. Equality \(a=0\) represents two conditionally independent coincident detectors, not one merged detector. Spatial dimension \(d=3\) is directly relevant to idealized aerial or aquatic animal-location models; dimensions above three describe a mathematical structural extension, not literal physical habitats.

## Proof

**1. Integrating two half-normal responses.** Completing squares in the Gaussian density gives, for any \(z\in\mathbb R^d\),
\[
\mathbb E\exp\!\left(-\frac{\|X-z\|^2}{2\ell^2}\right)
=(1+s)^{-d/2}\exp\!\left(-\frac{\|z\|^2}{2\ell^2(1+s)}\right).
\]
The identity \(\|X-ae_1\|^2+\|X+ae_1\|^2=2\|X\|^2+2a^2\) also gives the exact joint detection expectation. Conditional independence and inclusion-exclusion yield
\[
C_d(a)=\frac{2q}{(1+s)^{d/2}}\exp\!\left(-\frac{a^2}{2\ell^2(1+s)}\right)
-\frac{q^2}{(1+2s)^{d/2}}\exp\!\left(-\frac{a^2}{\ell^2}\right).
\]
This probability lies in \([0,1]\) because it is the expectation of \(g_+(X)+g_-(X)-g_+(X)g_-(X)\).

**2. Exact global optimization and boundary equality.** Write \(t=a^2/\ell^2\ge0\). Direct differentiation, with no asymptotic approximation, gives
\[
\frac{dC_d}{dt}=\frac{q}{(1+s)^{d/2+1}}\exp\!\left(-\frac{t}{2(1+s)}\right)
\left[\frac{q}{q_c(s,d)}\exp\!\left(-\frac{1+2s}{2(1+s)}t\right)-1\right].
\]
The exponential in square brackets is strictly decreasing in \(t\). If \(q\le q_c\), the derivative is strictly negative for all \(t>0\), including when \(q=q_c\). Otherwise, its sign is positive until precisely
\[
t_* =\frac{2(1+s)}{1+2s}\log\frac q{q_c(s,d)}
\]
and negative thereafter. Therefore the asserted maximizer is unique and global; \(t\to\infty\) and \(t=0\) are covered. No other stationary points can occur.

**3. Dimension threshold.** Define \(f_d(s)=\log q_c(s,d)\). Then
\[
f_d(0)=0,\qquad
f_d'(s)=\frac{d/2-1-2s}{(1+s)(1+2s)},\qquad
\lim_{s\to\infty}f_d(s)=-\infty.
\]
For \(d\le2\), this derivative is negative whenever \(s>0\), hence \(q_c<1\). For \(d>2\), it is positive until \(s=(d-2)/4\) and negative thereafter. Because \(f_d\) rises strictly above zero before decreasing to minus infinity, it has exactly one positive zero \(s_d\). For \(s\le s_d\) we have \(q_c\ge1\), so no allowed \(q\le1\) can exceed \(q_c\); for \(s>s_d\) the reverse becomes possible and is characterized exactly by the preceding derivative calculation.

For \(d=4\), taking the positive square root in \((1+2s)^4=(1+s)^6\) gives \((1+2s)^2=(1+s)^3\), or \(s(s^2-s-1)=0\), leaving the unique positive root \((1+\sqrt5)/2\).

**4. High-dimensional scale.** Put \(S_d=2^{d/2}\). Uniformly for \(s\) comparable to \(S_d\), expansion of the exact logarithmic formula gives
\[
f_d(s)=\log\frac{S_d}{s}-\frac{d/4+1}{s}+O\!\left(\frac d{s^2}\right).
\]
For each fixed \(c>0\), \(f_d(cS_d)\to-\log c\). Taking \(c=1/2\) and \(c=2\) brackets the unique positive zero, so \(s_d\sim S_d\). Substitution in the expansion and solving the resulting logarithmic equation gives
\[
s_d=S_d-\left(\frac d4+1\right)+O\!\left(\frac{d^2}{S_d}\right),
\]
which proves the claimed expansion. The error is uniform for sufficiently large integer \(d\); no finite-dimensional numerical fit is used as proof.

## Verification

The included executable `checker.py` uses Python's standard library. Running `python checker.py` completed 86,581 deterministic assertions. They independently integrate three one-dimensional instances by composite Simpson quadrature, evaluate the exact global formula against dense separation grids for dimensions from one through twenty, check stationary-point signs and critical-spread root brackets, test the four-dimensional golden-ratio identity, and probe random parameter ranges. These finite diagnostics **supplement** the analytical proof; they do not establish any continuum assertion by enumeration. The checked Gaussian integrals in dimension one support the normalization convention; the proof supplies the calculation in every dimension.

## Relationship to prior work

The half-normal detection model and detector placement motivation are classical in spatial capture–recapture. Sun, Fuller and Royle (2014) analyze placement and parameter-estimation precision under simulation; Durbach and colleagues (first published 2020) design arrays by approximate population-density estimator precision, which mixes first detections and recaptures. Tracey and colleagues (2014) establish the ecological importance of genuine three-dimensional location models. These published results do not state the dimension-three *impossibility of beneficial separation at any detector quality*, the exact critical spread sequence, or its exponential dimensional scaling. The planar symmetric two-detector formula is not asserted to be new; the qualitative threshold beginning in dimension three is the contribution.

## Limitations

The optimum is only within the reflected two-detector family; it is **not** a result for freely positioned detector pairs, multiple species, arbitrary trap arrays, or full population-density estimation. Assumed conditional independence might fail for colocated real detectors, and real habitats are finite, anisotropic, obstructed and often non-Gaussian. These restrictions prevent immediate field recommendations. The threshold's historical priority remains subject to independent examination of broader sensor coverage and Gaussian-mixture optimization theory; no independent audit has been performed.

## References

1. Sun, C. C., Fuller, A. K., and Royle, J. A. (2014). *Trap Configuration and Spacing Influences Parameter Estimates in Spatial Capture-Recapture Models.* PLOS ONE 9(2), e88025. First published February 5, 2014. https://doi.org/10.1371/journal.pone.0088025
2. Tracey, J. A., et al. (2014). *Movement-Based Estimation and Visualization of Space Use in 3D for Wildlife Ecology and Conservation.* PLOS ONE 9(7), e101205. First published July 2, 2014. https://doi.org/10.1371/journal.pone.0101205
3. Durbach, I., Borchers, D., Sutherland, C., and Sharma, K. *Fast, flexible alternatives to regular grid designs for spatial capture–recapture.* Methods in Ecology and Evolution 12(2), 298–310 (2021); first published October 28, 2020. https://doi.org/10.1111/2041-210X.13517
