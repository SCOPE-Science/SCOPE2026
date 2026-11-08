# A sharp two-mechanism positivity frontier for adaptive intolerance dynamics

## Finding

Consider the discrete adaptive-intolerance rule of Johnson and Eisenberg (2024), with a natural positive response-step multiplier \(h\). With intolerance \(x\in[0,1]\), the same-group neighborhood share \(p\in[0,1]\), and conformity \(0<\lambda<1\), define
\[
F_{h,\lambda}(x,p)=x+h x(1-x)(p-x)\left(1-\frac{(p-x)^2}{\lambda^2}\right),\qquad h>0.
\]
The published neutral-media update is precisely \(h=1\). A **universal viability bound** means \(F_{h,\lambda}(x,p)\in[0,1]\) for *every* \(x,p\in[0,1]\). It therefore also guarantees viability under arbitrary changes in neighborhood composition between updates, without any assumption about spatial mixing.

Define
\[
B(\lambda)=\lambda^{-2}-1,\qquad
A(\lambda)=\max_{0\le d\le\lambda}(1-d)d\left(1-\frac{d^2}{\lambda^2}\right).
\]
Then the **exact maximal universally safe step** is
\[
\boxed{H(\lambda)=\frac{1}{\max\{A(\lambda),B(\lambda)\}},\qquad
F_{h,\lambda}([0,1]^2)\subseteq[0,1]\ \Longleftrightarrow\ 0<h\le H(\lambda).}
\]
The maximum in \(A(\lambda)\) occurs at a unique \(d_\lambda\in(0,\lambda)\), characterized by
\[
\lambda^2(1-2d_\lambda)-3d_\lambda^2+4d_\lambda^3=0.
\]
The function \(A\) is strictly increasing, while \(B\) is strictly decreasing. Consequently there is one and only one \(\lambda_*\in(9/10,19/20)\) satisfying \(A(\lambda_*)=B(\lambda_*)\). The universally safe step \(H\) **increases strictly** on \((0,\lambda_*)\), **decreases strictly** on \((\lambda_*,1)\), and has its unique global maximum at \(\lambda_*\). Numerically, for orientation only,
\[
\lambda_*\approx0.914782481915056,\qquad H(\lambda_*)\approx5.128464475906.
\]
Thus the rate-limiting mechanism switches once: below \(\lambda_*\), over-large repulsion drives an intolerance below zero; above \(\lambda_*\), over-large attraction drives it above one. The numerical approximations are not used in the proof.

In particular, for the *printed unit-step update*,
\[
\boxed{F_{1,\lambda}([0,1]^2)\subseteq[0,1]\quad\Longleftrightarrow\quad \lambda\ge1/\sqrt2.}
\]
At \(\lambda=1/4\), the admissible inputs \(x=1/10\) and \(p=1\) instead yield exactly
\[
F_{1,1/4}(1/10,1)=-\frac{21719}{25000}.
\]
For the paper's media-modified map \(F_{1,\lambda,g}(x,p)=(1-g)F_{1,\lambda}(x,p)\), the sharp universal-viability condition for any real \(g\) is
\[
\boxed{g=1\quad\text{or}\quad (0\le g<1\ \text{and}\ \lambda\ge1/\sqrt2).}
\]
In particular, a negative media coefficient never preserves the full interval as stated: already \(F_{1,\lambda,g}(1,p)=1-g>1\). This concerns the **written recurrence**; it makes no claim about an implementation that might impose undocumented clipping, normalization, or different update ordering.

## Assumptions and scope

The state and environmental input are arbitrary real numbers in \([0,1]\); \(\lambda\in(0,1)\); the response step \(h>0\) is fixed, and the ordinary model uses \(h=1\). A uniform guarantee is required for all such states and environmental inputs. The same-group fraction \(p=1\) is attainable in a homogeneous local neighborhood (including the focal agent), and this endpoint is sufficient for the sharp repulsion obstruction. No stochastic or population-level independence hypothesis is required.

The exact step frontier is for **neutral media**, \(g=0\). The additional media corollary concerns the original unit step, \(h=1\), with the paper's multiplicative convention \((1-g)\). It is not a threshold formula for arbitrary positive \(h\) and arbitrary \(g\) simultaneously. The result concerns the scalar update at one time and its ability to preserve the admissible state range, not the existence, stability, or spatial mixing of a full Schelling-model equilibrium.

## Proof

**1. Symmetry and the two failure mechanisms.** Put \(d=p-x\). Direct substitution gives
\[
1-F_{h,\lambda}(x,p)=F_{h,\lambda}(1-x,1-p).
\]
It therefore suffices to consider \(d\ge0\). Because \(p\le1\), we have \(0\le d\le 1-x\). If \(0<d<\lambda\), the factor \(d(1-d^2/\lambda^2)\) is positive and \(F_{h,\lambda}(x,p)\ge x\); the only possible failure is \(F_{h,\lambda}(x,p)>1\). When \(x\in(0,1)\), that is equivalent to
\[
hx d(1-d^2/\lambda^2)>1.
\]
At fixed \(d\), the left-hand coefficient is largest at \(x=1-d\) (hence \(p=1\)). Maximizing over \(0\le d\le\lambda\) gives exactly \(A(\lambda)\). Therefore all attractive updates are bounded above by one precisely when \(hA(\lambda)\le1\). If this inequality fails, take a maximizing \(d_\lambda\), \(x=1-d_\lambda\), and \(p=1\). The resulting next state is strictly greater than one, so the condition is necessary as well as sufficient.

For \(\lambda<d\le1-x\), the scalar force is negative and \(F_{h,\lambda}(x,p)\le x\). Writing \(s=1-x\), nonnegativity requires
\[
hs d(d^2/\lambda^2-1)\le1.
\]
For fixed \(s\ge d>\lambda\), the function of \(d\) on the left increases strictly. It is therefore at most \(h s^2(s^2/\lambda^2-1)\). This expression increases strictly with \(s\in[\lambda,1]\), attaining its supremum \(h(\lambda^{-2}-1)=hB(\lambda)\) as \(s\to1\). Thus \(hB(\lambda)\le1\) guarantees nonnegativity. Conversely, if \(hB(\lambda)>1\), take \(p=1\), \(x>0\) sufficiently small: the factor multiplying \(x\) in \(F_{h,\lambda}(x,1)\) tends to \(1-hB(\lambda)<0\), giving a strict negative output. The cases \(d=0\), \(d=\lambda\), and \(x=0,1\) are fixed or covered by continuity. Reflection handles \(d<0\). This proves the sharp formula for \(H\), including every boundary.

**2. The single crossover and the nonmonotone optimum.** On \(0<d<\lambda<1\), the logarithm of
\[
a_\lambda(d)=(1-d)d(1-d^2/\lambda^2)
\]
is the sum of the logarithms of \(d\), \(1-d\), \(\lambda-d\), and \(\lambda+d\), minus the constant \(2\log\lambda\). Each summand is concave and the sum is strictly concave, with value tending to negative infinity at both endpoints. Thus \(a_\lambda\) has exactly one interior maximizer. Differentiating gives the displayed cubic condition for \(d_\lambda\).

For \(\lambda_2>\lambda_1\), evaluating \(a_{\lambda_2}\) at the positive maximizer for \(\lambda_1\) strictly increases the value, so \(A(\lambda_2)>A(\lambda_1)\). Also \(B\) decreases strictly from infinity to zero. As \(\lambda\to0\), \(A(\lambda)\le\lambda\to0\); as \(\lambda\to1\), \(A(\lambda)>0\). Continuity yields exactly one crossover. For an exact bracket, at \(\lambda=9/10\), partition \(d\in[0,\lambda]\) at \(d=1/4\): on the first part \(a_\lambda(d)\le3/16\), and on the second \(a_\lambda(d)\le299/1296<19/81=B(9/10)\). At \(\lambda=19/20\), testing \(d=3/8\) gives \(A\ge18285/92416>39/361=B(19/20)\). Consequently \(H\), which is the reciprocal of the larger of increasing \(A\) and decreasing \(B\), rises before the crossing and falls afterward, with one strict maximum.

**3. The original unit step.** For \(0<\lambda<1\), \(A(\lambda)\le\max_{0\le d\le1}d(1-d)=1/4<1\). Hence \(H(\lambda)\ge1\) if and only if \(B(\lambda)\le1\), equivalent to \(\lambda^2\ge1/2\). Direct rational substitution yields the stated negative example at \(\lambda=1/4\).

**4. Media multiplier.** If \(g=1\), the next state is identically zero. If \(0\le g<1\) and \(\lambda\ge1/\sqrt2\), the neutral unit-step output is in \([0,1]\), and multiplication by \(1-g\in(0,1]\) preserves it. If \(0\le g<1\) but \(\lambda<1/\sqrt2\), the negative neutral example near \((x,p)=(0,1)\) remains negative. For \(g<0\), use \(x=1\), giving \(1-g>1\); for \(g>1\), take \(x=p=1/2\), giving \((1-g)/2<0\). These cases exhaust the real media parameter.

## Verification

The accompanying standalone Python 3 standard-library program `verify.py` checks 44,939 exact-rational and floating-point test instances and prints `VERIFY_OK` on success. Exact rational grids cover all boundary inputs and multiple safe conformity parameters, demonstrate explicit unsafe conformity cases, and test the frozen-environment sign structure. A separate independent sampling loop tests the sharp variational bound for a range of response steps, including both transition mechanisms and examples just beyond the claimed maximal step. A derivative-independent one-dimensional golden-section search numerically locates the unique crossover; it is a sanity check only, not the proof of uniqueness.

Run in the same directory:

```text
python3 verify.py
```

The universal quantifiers and the unique crossover are proved algebraically above; the finite tests do not replace their proofs. The displayed numerical values may differ in last-place rounding across Python implementations.

## Relationship to prior work

Johnson and Eisenberg (arXiv:2403.02122, first posted 4 March 2024) introduce the exact cubic adaptation rule, multiply it by \(x(1-x)\) to seek bounded intolerance, and add the external media multiplier. Their paper examines integration and segregation through spatial simulation and relates a simulated transition from an initially segregated state to an approximately linear conformity threshold. The present result is **not** a new formulation of that numerical transition or a claim that the full spatial model has the same attractors: it establishes the sharp global range-preservation frontier of the printed single-agent recurrence, the competing overshoot mechanisms, and the nonmonotone maximal admissible step.

Urselmans and Phelps (2018) introduce a distinct adaptive-tolerance Schelling model with explicitly clipped additive tolerance increments; those are structurally different from the cubic multiplier analyzed here. Haw and Hogan (2018) analyze tipping and basins of attraction for a two-population Schelling neighborhood system, rather than this discrete scalar update and its exact step-size frontier. Generic Euler positivity concepts motivate checking range preservation but do not, without the present optimization, give the stated specialized sharp formula and crossover.

## Limitations

This is a deterministic one-step viability theorem for the **printed scalar rule**. It neither asserts that any particular simulation ran outside its stated range nor inspects or rules out additional range clipping in implementations. The sharp step-size formula is for arbitrary real \(x,p\in[0,1]\); actual local shares are discrete fractions depending on neighborhood occupancy. The repulsion extremizer uses the attainable homogeneous-neighborhood value \(p=1\), while the attractive extremizer uses \(p=1\) together with an arbitrary interior \(x\). A restricted subset of states or an implementation with clipping can obey a different threshold.

The media result is only for the published unit-step convention; it is not an all-parameter formula for arbitrary joint step and media strengths. No claim is made about long-term equilibrium, mobility, social policy outcomes, or empirical realism. The exact scientific-priority assessment is based on available literature and mathematical-record searches; unindexed equivalent results remain possible. Independent external validation has not been performed.

## References

1. J. D. Johnson and M. C. Eisenberg, *A Dynamic Model of Integration*, arXiv:2403.02122v1, 4 March 2024. https://arxiv.org/abs/2403.02122
2. L. Urselmans and S. Phelps, *A Schelling Model with Adaptive Tolerance*, PLOS ONE 13(3):e0193950 (2018). https://doi.org/10.1371/journal.pone.0193950
3. D. J. Haw and S. J. Hogan, *A dynamical systems model of unorganised segregation*, arXiv:1709.07568 (2017); *Journal of Mathematical Sociology* 42 (2018), 113–127. https://arxiv.org/abs/1709.07568
