# A sharp two-to-one gradient threshold for stationary modes of a saturating run-and-tumble particle

## Finding
For the spatially saturating one-dimensional two-orientation run-and-tumble process of Jain and Chatterjee, the dimensionless **ratio of tumbling-gradient steepness to speed-gradient steepness** has an exact universal boundary at \(g/u=2\). The boundary concerns the *possibility of more than two stationary position-density modes* over the full physical parameter family, rather than a particular finite-dimensional parameter slice.

For every \(v_0>v_1>0\), \(\gamma_0\ge\gamma_1>0\), \(u>0\), and \(0\le g\le 2u\), the unique normalized stationary marginal density has **exactly one** strict local maximum (at zero) if
\[
 u^2v_1^2\le u\gamma_0v_1+g\gamma_1v_0,
\]
and **exactly two** strict local maxima (at symmetric nonzero positions) if the inequality is reversed. There are no further stationary local extrema on either open half-line. At equality the origin is a strict, quartically flat maximum, not an extra pair of peaks.

This restriction on the spatial gradients is sharp: **for each real number \(\rho>2\)** there are strictly admissible positive physical parameters with \(g/u=\rho\) for which the stationary marginal has **at least three strict local maxima**, including one at the origin and a symmetric off-center pair. The result does not claim a complete mode count for arbitrary parameters when \(g>2u\).

## Assumptions and scope
The process moves on \(\mathbb R\), with a right-moving state having velocity \(v_+(x)=v_0-v_1\tanh(ux)>0\) and a left-moving state having velocity \(-v_-(x)\), where \(v_-(x)=v_0+v_1\tanh(ux)>0\). Right-to-left and left-to-right switch intensities are respectively \(\gamma_+(x)=\gamma_0+\gamma_1\tanh(gx)\) and \(\gamma_-(x)=\gamma_0-\gamma_1\tanh(gx)\). There is no independent Brownian noise, no absorbing boundary, and no interaction between particles. All stated rates are strictly positive at finite positions, including when \(\gamma_0=\gamma_1\). The stationary *marginal* position density means the sum of the two orientation-resolved densities. A mode means a strict local maximum of that marginal.

The stationary zero-current density is the normalizable even function
\[
 p(x)=\frac1Z\frac{2v_0}{v_0^2-v_1^2\tanh^2(ux)}
 \exp\!\left[-2\int_0^x
 \frac{\gamma_0v_1\tanh(uy)+\gamma_1v_0\tanh(gy)}{v_0^2-v_1^2\tanh^2(uy)}\,dy\right].
\]
Here \(Z\) is the positive normalizing integral. Its existence for the stated bounded-rate model also follows directly from the exponentially decreasing tails: with \(v_0>v_1\) and \(u>0\), the exponent's integrand has a strictly positive limiting magnitude on each outward half-line because \(\gamma_0v_1>0\).

## Proof
**Step 1: exact sign reduction.** Set \(t=ux>0\), \(\rho=g/u\), and
\[
 A=uv_1^2,\quad B=\gamma_0v_1>0,\quad C=\gamma_1v_0>0.
\]
Direct differentiation of the displayed normalized stationary formula gives
\[
 \frac{p'(x)}{p(x)}=\frac{2\tanh t}{v_0^2-v_1^2\tanh^2t}\left[A\operatorname{sech}^2t-B-C\frac{\tanh(\rho t)}{\tanh t}\right].
\]
All factors outside the square bracket are strictly positive for \(x>0\). After multiplication by \(\cosh^2t>0\), the sign of \(p'(x)\) is therefore the sign of \(A-F_\rho(t)\), where
\[
 F_\rho(t)=B\cosh^2t+C K_\rho(t),\qquad
 K_\rho(t)=\cosh^2t\frac{\tanh(\rho t)}{\tanh t},
\]
with \(K_0(t)=0\) and \(K_\rho(0+)=\rho\).

**Step 2: monotonicity up to the exact steepness ratio two.** For \(0<\rho\le2\), logarithmic differentiation yields the exact identity
\[
 \frac12\frac{d}{dt}\log K_\rho(t)
 =\tanh t+\frac{\rho}{\sinh(2\rho t)}-\frac1{\sinh(2t)}.
\]
For fixed \(t>0\), the function \(a\mapsto a/\sinh(2at)\) is strictly decreasing for positive \(a\), since \(z\cosh z>\sinh z\) for \(z>0\). Hence \(\rho/\sinh(2\rho t)\ge2/\sinh(4t)\). The preceding logarithmic derivative is bounded below by
\[
 \tanh t+\frac2{\sinh(4t)}-\frac1{\sinh(2t)}
 =\tanh t\left(1-\frac1{\cosh(2t)}\right)>0.
\]
Thus \(K_\rho\) is strictly increasing on \((0,\infty)\) for every \(0<\rho\le2\); for \(\rho=0\) it vanishes identically. Because \(B>0\), the function \(F_\rho\) is strictly increasing for every \(0\le\rho\le2\), with
\[
 F_\rho(0+)=B+C\rho,\qquad \lim_{t\to\infty}F_\rho(t)=+\infty.
\]
Consequently \(p'\) is negative throughout \((0,\infty)\) when \(A\le B+C\rho\). When \(A>B+C\rho\), it is positive until a **unique** positive zero and negative afterward. Symmetry gives exactly the stated one-mode/two-mode dichotomy. Multiplying the center inequality by \(u\) gives the original displayed physical-parameter criterion.

At equality, the origin remains a strict maximum, and its quadratic derivative vanishes: \(\cosh^2t=1+t^2+O(t^4)\) and
\[
 K_\rho(t)=\rho+\frac{\rho(4-\rho^2)}3t^2+O(t^4)
\]
for \(0<\rho\le2\) (with \(K_0\equiv0\)). Since \(B>0\), the coefficient of \(t^2\) in \(F_\rho(t)-F_\rho(0+)\) is strictly positive. Therefore \(\log p(x)-\log p(0)\) has a strictly negative quartic leading term. This includes the endpoint \(\rho=2\).

**Step 3: sharpness beyond two.** Fix any real \(\rho>2\). For \(b\in(0,1)\) set
\[
 v_0=1,\quad v_1=b,\quad \gamma_0=\gamma_1=1,\quad
 u=\frac{\rho}{b^2},\quad g=\rho u.
\]
These parameters are admissible. They give \(A=\rho\), \(B=b\), \(C=1\). For \(s=\tanh^2(ux)\in(0,1)\), the derivative sign is that of
\[
 M_b(s)=\rho(1-s)-b-R_\rho(s),\qquad
 R_\rho(s)=\frac{\tanh\!\bigl(\rho\operatorname{artanh}\sqrt{s}\bigr)}{\sqrt{s}}.
\]
The analytic expansion at \(s=0\) is
\[
 R_\rho(s)=\rho-\frac{\rho(\rho^2-1)}3s+O(s^2),
 \quad M_b(s)=-b+\frac{\rho(\rho^2-4)}3s+O(s^2).
\]
Because \(\rho>2\), there exists \(s_0\in(0,1)\) for which \(M_0(s_0)>0\). Taking \(0<b<\min\{1,M_0(s_0)\}\), we have \(M_b(0+)=-b<0\), \(M_b(s_0)>0\), and \(M_b(1-)=-b-1<0\). The stationary density therefore decreases initially from a strict central maximum, rises on a nonempty interval and eventually decreases again. Analyticity and the sign changes yield at least one strict off-center local maximum on \((0,\infty)\), and by symmetry another on \(( -\infty,0)\). Thus every ratio strictly greater than two admits at least three modes. This is an existence statement, not an assertion of exactly three modes for all such parameters.

A fully rational worked witness is \(\rho=3\), \(b=1/10\), \(u=300\), \(g=900\). In this case \(R_3(s)=(3+s)/(1+3s)\), and the derivative sign numerator becomes \((-1+47s-90s^2)/[10(1+3s)]\). Its two positive roots are exactly \(s=1/45\) and \(s=1/2\), with signs negative, positive, negative. Thus this particular density has exactly three strict modes, while the *universal threshold claim* above is substantially broader than the single-ratio example.

## Verification
The standalone standard-library script `check_modality.py` evaluates the derivative identity against independent quadrature of the stationary density, tests the strict hyperbolic inequality and monotonicity on many parameter points, and validates the rational three-mode witness exactly. Running `python3 check_modality.py` produced `PASS: 688 deterministic assertions; analytic proof remains necessary.` The general infinite-parameter theorem and the assertion for every real \(\rho>2\) are proved by the inequalities and Taylor argument above; finite arithmetic sampling cannot establish either universally.

## Relationship to prior work
Jain and Chatterjee introduced exactly these spatially saturating rates, derived the normalized stationary law, and proposed the center-curvature criterion for a one/two-mode transition under the explicit assumption that at most two peaks occur. Their equations (7), (14), and (15) are the starting identities, not new contributions. A subsequently published analysis proved a sharp trimodal window on one \(g=3u\) subfamily and a general two-mode upper bound only for \(0\le g\le u\). That work shows a three-peak phase is possible at one ratio above two, but does not establish (a) the full mode dichotomy throughout \(u<g\le2u\), or (b) three-peak *existence for every* real \(g/u>2\). The present result joins those two missing implications into a sharp, physical-parameter-independent gradient-ratio boundary. General velocity-jump models with time-varying coefficients or different boundary conditions are not equivalent mode-count theorems for this spatially varying family.

## Limitations
This result proves a complete stationary mode classification only for \(0\le g/u\le2\) and the possibility of at least three modes for every ratio above two. It does not classify the number or locations of all modes for arbitrary \(g/u>2\), nor address relaxation, transient densities, extra thermal diffusion, experiment, or interactions. The original stationary formula is reused with attribution. A separate independent publication-priority audit has not been performed; an equivalent as-yet-unindexed theorem remains possible.

## References
1. K. Jain and S. Chatterjee, *Run-and-tumble particle with saturating rates*, arXiv:2405.13521, first publicly submitted **2024-05-22**, *Physical Review E* **110**, 064110 (2024). https://arxiv.org/abs/2405.13521 ; full text https://arxiv.org/html/2405.13521v2
2. *A sharp unimodal–trimodal–bimodal transition in a two-state run-and-tumble particle*, published mathematical result, 2026-11-08. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-sharp-unimodal-trimodal-bimodal-transition-in-a-two-state-run--56f6c06bf21b
3. L. Angelani and R. Garra, *Probability distributions for the run-and-tumble models with variable speed and tumbling rate*, arXiv:2001.02487 (2020). https://arxiv.org/abs/2001.02487
4. M. Guéneau and L. Touzo, *Relating absorbing and hard wall boundary conditions for a one-dimensional run-and-tumble particle*, arXiv:2312.13200 (2023). https://arxiv.org/abs/2312.13200
