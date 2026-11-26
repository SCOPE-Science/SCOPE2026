# Sharp factor-two gradient barrier for peak proliferation in a saturating run-and-tumble particle

## Finding
A one-dimensional velocity-jump particle with positive saturating speeds and orientation-switching rates has a **sharp universal spatial-gradient barrier** for the appearance of three or more stationary position-density peaks. In the full positive-parameter family defined below, put \(q=g/u\). If \(0<q\le2\), the stationary marginal density has at most two local maxima. Its exact classification is:

\[
\begin{cases}
\text{one central strict maximum},&u v_1^2\le \gamma_0v_1+q\gamma_1v_0,\\
\text{two symmetric strict off-center maxima},&u v_1^2>\gamma_0v_1+q\gamma_1v_0.
\end{cases}
\]

At equality the origin remains a strict (possibly flat) maximum. Conversely, **for every real \(q>2\)** there exist admissible strictly positive speed and switching parameters with ratio \(g/u=q\) for which the stationary marginal density has **at least three strict local maxima**: one at the origin and one on either side, with intervening minima. Thus \(q=2\), not merely \(q=1\), is the sharp universal barrier separating a regime in which more than two peaks are impossible from a regime in which such peak proliferation can occur. The statement does **not** assert that all parameters with \(q>2\) are trimodal, or bound the number of peaks in that region.

An exact noninteger-gradient witness is \(u=v_1=1\), \(v_0=2\), \(g=5/2\), and \(\gamma_0=\gamma_1=21/125\). Its center is a strict peak, and a positive interval has outward-increasing density, forcing two additional strict off-center peaks.

## Assumptions and scope
The particle moves on \(\mathbb R\) with orientations \(+\) and \(-\), with deterministic right/left velocities and orientation-flip intensities
\[
v_\pm(x)=v_0\mp v_1\tanh(ux),\qquad
\gamma_\pm(x)=\gamma_0\pm\gamma_1\tanh(gx).
\]
Assume \(v_0>v_1>0\), \(\gamma_0\ge\gamma_1>0\), and \(u,g>0\). All finite-position velocities are strictly positive and all switching intensities are nonnegative (and strictly positive at finite positions). A *peak* means a strict local maximum of the normalized stationary **marginal position density** \(p=p_++p_-\), not of a single orientation-resolved component. The infinite-line stationary law exists and is integrable for these parameters; its known zero-current formula is recalled below. No translational thermal diffusion, interactions, or boundaries are included.

## Proof
**1. Stationary log-derivative.** The forward equations are
\[
\partial_t p_+=-\partial_x(v_+p_+)-\gamma_+p_++\gamma_-p_-,\quad
\partial_t p_-=\partial_x(v_-p_-)+\gamma_+p_+-\gamma_-p_-.
\]
The normalizable stationary zero-current branch has \(v_+p_+=v_-p_-=K e^{I(x)}\) and
\[
I'(x)=\frac{\gamma_-(x)}{v_-(x)}-\frac{\gamma_+(x)}{v_+(x)}.
\]
Therefore \(p(x)\propto[v_+(x)^{-1}+v_-(x)^{-1}]e^{I(x)}\), with an even, positive, smooth density decaying exponentially as \(|x|\to\infty\) because \(v_0>v_1\) and \(\gamma_0v_1+\gamma_1v_0>0\). Direct differentiation gives, for \(x>0\),
\[
\frac{p'(x)}{p(x)}=
\frac{2\tanh(ux)}{v_0^2-v_1^2\tanh^2(ux)}
\left[uv_1^2\operatorname{sech}^2(ux)-\gamma_0v_1-\gamma_1v_0\frac{\tanh(gx)}{\tanh(ux)}\right].
\]
Set \(y=ux\), \(q=g/u\), \(A=uv_1^2\), \(B=\gamma_1v_0\), \(C=\gamma_0v_1\), and
\[
H_q(y)=\cosh^2 y\left[C+B\frac{\tanh(qy)}{\tanh y}\right],\qquad
H_q(0)=C+Bq.
\]
The prefactors are strictly positive for \(x>0\), so \(\operatorname{sgn}p'(x)=\operatorname{sgn}[A-H_q(ux)]\). The density is even.

**2. Rigorous two-peak ceiling for all \(0<q\le2\).** Write
\[
H_q(y)=C\cosh^2 y+B h_q(y),\qquad
h_q(y)=\frac{\tanh(qy)\cosh^3 y}{\sinh y}.
\]
For fixed \(y>0\), the function \(s\mapsto s/\sinh(2sy)\) is strictly decreasing for \(s>0\), since \(z\cosh z-\sinh z>0\) for \(z>0\). Consequently
\[
\frac{d}{dy}\log h_q(y)=\frac{2q}{\sinh(2qy)}+3\tanh y-\coth y
\ge \frac4{\sinh(4y)}+3\tanh y-\coth y
=\frac{d}{dy}\log h_2(y).
\]
But, writing \(z=\tanh^2 y\),
\[
h_2(y)=\frac{2}{1-z^2},
\]
which is strictly increasing for \(y>0\). Hence \(h_q\), and thus \(H_q\), are strictly increasing for every \(0<q\le2\). Also \(H_q(y)\to\infty\) as \(y\to\infty\). Therefore, if \(A\le H_q(0)\), then \(p'(x)<0\) for every \(x>0\), giving a single strict central maximum. If \(A>H_q(0)\), then \(H_q(ux)=A\) has exactly one positive solution and the derivative changes from positive to negative there, giving precisely two symmetric strict maxima and a strict central minimum. Equality at the origin is included because the strict inequality \(H_q(y)>H_q(0)\) holds for every \(y>0\).

**3. Sharpness: every \(q>2\) permits extra peaks.** As \(y\downarrow0\), Taylor expansion gives
\[
H_q(y)=C+Bq+\left[C+\frac{Bq(4-q^2)}3\right]y^2+O(y^4).
\]
For any fixed real \(q>2\), choose \(u=v_1=1\), \(v_0=L\), \(g=q\), and \(\gamma_0=\gamma_1=b\) with
\[
L>\max\left\{1,\frac{3}{q(q^2-4)}\right\},\qquad b>0.
\]
Then \(A=1\), \(C=b\), \(B=bL\), and \(H_q=bK_q\), where \(K_q(0)=1+Lq\) and the quadratic coefficient of \(K_q\) is strictly negative. Hence some \(y_0>0\) has \(0<K_q(y_0)<K_q(0)\). Choose any
\[
\frac{1}{K_q(0)}<b<\frac{1}{K_q(y_0)}.
\]
It follows that \(H_q(0)>1\), \(H_q(y_0)<1\), and \(\lim_{y\to\infty}H_q(y)=+\infty\). Since \(p'\) is negative immediately to the right of the origin, positive at \(y_0\), and negative for all sufficiently large positive positions, continuity and analyticity yield a strict central maximum, at least one strict positive local minimum, and at least one strict positive local maximum. Evenness supplies the corresponding two negative-side extrema. All these parameter inequalities are strict, so the phenomenon persists under small perturbations. No unproved assertion about *exactly* three peaks is needed.

**4. An exact algebraic witness at \(q=5/2\).** For \(u=v_1=1\), \(v_0=2\), \(g=5/2\), and \(\gamma_0=\gamma_1=21/125\), one has \(A=1\) and \(H_q(0)=126/125>1\). At \(y_0=\operatorname{artanh}(1/3)=\tfrac12\log 2\), the identities \(\tanh y_0=1/3\) and \(\tanh(5y_0/2)=(4\sqrt2-1)/(4\sqrt2+1)\) yield
\[
H_q(y_0)=\frac{43281}{31000}-\frac{1134\sqrt2}{3875}<1,
\]
where the strict inequality follows exactly from \(2\cdot9072^2-12281^2=13779407>0\). Thus the derivative sign pattern in step 3 is verified by an exact inequality for a specific noninteger ratio between the forbidden interval and the previously exhibited \(q=3\) examples.

## Verification
Run `python3 check_peak_threshold.py` with Python 3 standard library. The checker verifies the exact integer algebraic witness and independent numerical evaluations of the stationary log-derivative, of the strictly increasing barrier \(H_q\) for tested \(0<q\le2\), and of sign-changing examples for several \(q>2\), including ratios arbitrarily close to \(2\). The proof above, not numerical sampling, establishes the universal quantifiers. The code does not certify a global upper bound on the number of modes in the \(q>2\) regime.

## Relationship to prior work
Jain and Chatterjee, *Run-and-tumble particle with saturating rates* (first public preprint 2024-05-22; arXiv:2405.13521), derive the stationary density and implicit critical-point equation for this exact positive-parameter family. Their proposed center-curvature classification is conditioned on an assumed upper bound of two peaks; it does not prove that bound generally. The separately published *A sharp unimodal–trimodal–bimodal transition in a two-state run-and-tumble particle* (2026) exhibits a complete three-peak example at \(g=3u\) and proves at most two peaks for \(0\le g\le u\). Its result neither gives the factor-two **sharp universal barrier** nor supplies examples for every \(g/u>2\). The present result establishes that peak proliferation is impossible on the entire additional gradient interval \(u<g\le2u\), and that every ratio just above \(2\) permits it. It credits and does not re-claim either the stationary formula or the earlier concrete \(g=3u\) example. The algebraic witness at \(5u/2\) is supporting evidence, not a separate novelty claim.

## Limitations
The model is an infinite-line two-orientation transport process with the specific hyperbolic-tangent saturating rates. The result classifies **at most two versus the possibility of three or more peaks**, not the exact number or all transition surfaces for \(g>2u\). It does not establish uniqueness or stability of a dynamically evolving density, first-passage statistics, or a result for more general saturating profiles. The publication-priority comparison is limited to the inspected primary source and the accessible published mode classification plus searchable literature; unindexed equivalent gradient inequalities remain a residual risk. Independent scientific validation has not been performed.

## References
1. K. Jain and S. Chatterjee, *Run-and-tumble particle with saturating rates*, arXiv:2405.13521, first posted 2024-05-22; *Physical Review E* 110, 064110 (2024). https://arxiv.org/abs/2405.13521 and https://arxiv.org/html/2405.13521v2
2. *A sharp unimodal–trimodal–bimodal transition in a two-state run-and-tumble particle*, published 2026-11-08, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-a-sharp-unimodal-trimodal-bimodal-transition-in-a-two-state-run--56f6c06bf21b/RESULT.md
3. J. M. Newby and J. P. Keener, *An Asymptotic Analysis of the Spatially Inhomogeneous Velocity-Jump Process*, *Multiscale Modeling & Simulation* (2011), DOI:10.1137/10080676X. General framework; not used as a source of the present exact modality threshold.
