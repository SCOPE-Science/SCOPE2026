# A sharp exposure-allocation transition for Gaussian and first-Hermite ambiguity inversion

## Finding

Let \(h_0(t)=2^{1/4}e^{-\pi t^2}\) and \(h_1(t)=2\sqrt\pi\,t h_0(t)\), both normalized in \(L^2(\mathbb R)\). For \(T>0\), let \(\Omega_T=\{(x,\xi)\in\mathbb R^2:\pi(x^2+\xi^2)\le T\}\). Define the centered ambiguity function
\[
\mathcal A g(x,\xi)=\int_{\mathbb R}g(t+x/2)\overline{g(t-x/2)}e^{-2\pi i\xi t}\,dt.
\]
An exposure fraction \(a\in[0,1]\) is allocated to the first-Hermite window, and \(1-a\) to the Gaussian window. The data-to-ambiguity *linear multiplier* is
\[
\mathcal M_{T,a}F(x,\xi)=\big(\sqrt{1-a}\,\overline{\mathcal Ah_0(x,\xi)}F(x,\xi),\ \sqrt a\,\overline{\mathcal Ah_1(x,\xi)}F(x,\xi)\big).
\]
It acts from \(L^2(\Omega_T)\) to \(L^2(\Omega_T;\mathbb C^2)\). This exposure convention models *two prewhitened channels with noise precision proportional to exposure*; it is not the same as scaling an unwhitened spectrogram window. Define its squared lower stability margin
\[
C(T,a)=\inf_{F\ne0}\frac{\|\mathcal M_{T,a}F\|_2^2}{\|F\|_2^2}
=\min_{0\le s\le T}e^{-s}\big(1+a(s^2-2s)\big),\quad s=\pi(x^2+\xi^2).
\]
Then the *complete sharp optimal-exposure law* is as follows.

1. For \(0<T<2\), \(C(T,a)\) is uniquely maximized by \(a=0\), with optimum \(e^{-T}\).
2. For \(T=2\), every \(a\in[0,1/2]\) and only these exposures maximize \(C(2,a)=e^{-2}\).
3. For each \(T>2\), there is a unique optimizer \(a_T\in(1/2,1)\). Let \(x_T\in(1,2)\) be the unique solution of
\[
2(x_T-1)e^{T-x_T}=(T-1)^2+1-(x_T-2)^2.
\]
Then
\[
a_T=\frac1{2-(x_T-2)^2},\qquad
C(T,a_T)=\frac{2(x_T-1)e^{-x_T}}{2-(x_T-2)^2}.
\]
At the unique optimum, the worst-case radius \(s=x_T\) and the outer boundary \(s=T\) have *exactly equal* squared stability margins. Moreover,
\[
1-a_T\sim e^{1-T}(T-1)^2,\qquad C(T,a_T)\sim e^{-T}(T-1)^2
\quad(T\to\infty).
\]
Thus the sharp large-aperture improvement in *squared* lower stability relative to the single Gaussian channel is asymptotically \((T-1)^2\). For illustration, at \(T=4\), \(1-a_T\approx0.3559367955\) and \(C(T,a_T)\approx0.1126870715\), compared with the pure Gaussian value \(e^{-4}\approx0.0183156389\).

## Assumptions and scope

The two Hermite windows are fixed and have unit \(L^2\) norm. Measurements are continuous, the admissible ambiguity region is the closed disk \(\Omega_T\), the same scalar exposure fraction applies at every point, and the two Fourier-domain data channels are normalized by their noise standard deviations. The ambient input \(F\) is an *unrestricted* complex \(L^2\) field on the disk; the result is not a theorem on the nonlinear phase-retrieval map or on recovery of arbitrary signals from finitely sampled spectrograms. The squared lower multiplier bound \(C(T,a)\), rather than an unweighted \(L^1\) combination of ambiguity magnitudes, is the exact conditioning objective. Physical spectrogram data imply this multiplication identity after applying the two-dimensional Fourier transform, but the theorem concerns only the stated linear step.

## Proof

**1. Exact radial multiplier.** Gaussian Fourier integration gives
\[
\mathcal Ah_0=e^{-s/2},\qquad \mathcal Ah_1=e^{-s/2}(1-s).
\]
For the second identity, substitute \(h_1(t)=2\sqrt\pi\,t h_0(t)\) into the centered ambiguity integral. The Gaussian product is proportional to \(e^{-2\pi t^2}e^{-\pi x^2/2}\); differentiating its Fourier transform twice in \(\xi\) yields precisely the factor \(1-\pi(x^2+\xi^2)\). Thus at radius \(s\), the unique nonzero squared singular value of the column multiplier is
\[
f_a(s):=e^{-s}\big((1-a)+a(1-s)^2\big)=e^{-s}(1+a(s^2-2s)).
\]
For scalar multiplication into a two-component field, the lower bound is the essential infimum of the pointwise squared singular value, which equals its minimum by continuity on the compact disk. The minimum is sharp: choose \(L^2\) functions supported in progressively smaller neighborhoods of a minimizing radius (or a thin outer annulus at the boundary). This justifies the exact formula for \(C(T,a)\) including boundary attainment in the essential-infimum sense.

**2. The first two regimes.** For \(0\le s\le2\), \((1-s)^2\le1\), with strict inequality at \(s=T\) for \(0<T<2\). Therefore, any positive \(a\) reduces the multiplier at \(s=T\) below \(e^{-T}\), while \(a=0\) has minimum \(e^{-T}\). At \(T=2\), \(f_a(2)=e^{-2}\) for all \(a\). Direct differentiation gives
\[
f_a'(s)=e^{-s}\left[-1+a\left(2-(s-2)^2\right)\right].
\]
For \(a\le1/2\), the bracket is nonpositive on \([0,2]\), hence the minimum equals \(e^{-2}\). For \(a>1/2\), there is a strict local minimum at \(s_-(a)=2-\sqrt{2-1/a}\in[1,2)\), with \(f_a(s_-(a))<f_a(2)\). Consequently the optimizer set at \(T=2\) is exactly \([0,1/2]\).

**3. The sharp transition for \(T>2\).** If \(a\le1/2\), \(f_a\) is nonincreasing on the entire nonnegative half-line, so \(C(T,a)=f_a(T)\), strictly increasing in \(a\) because \(T(T-2)>0\). For \(a\in(1/2,1]\), the derivative has precisely two nonnegative roots
\[
s_-(a)=2-\sqrt{2-1/a},\qquad s_+(a)=2+\sqrt{2-1/a},
\]
with local minimum at \(s_-\) and local maximum at \(s_+\). Since \(s_-<2<T\) and \(f_a(0)=1>f_a(T)\), the global minimum on \([0,T]\) is
\[
C(T,a)=\min\{L(a),E_T(a)\},\quad
L(a)=f_a(s_-(a)),\quad E_T(a)=e^{-T}(1+aT(T-2)).
\]
The inequality \(f_a(T)<1\) follows from \(f_a(T)\le e^{-T}\max\{1,(T-1)^2\}<1\), valid for \(T>2\). The boundary value \(E_T\) increases *strictly* with \(a\). Conversely, by the stationary-point identity,
\[
L'(a)=e^{-s_-(a)}s_-(a)(s_-(a)-2)<0
\]
for \(1/2<a<1\); continuity supplies the endpoint values. At \(a=1/2\), \(L(1/2)=f_{1/2}(2)>f_{1/2}(T)\), since \(f_{1/2}\) decreases strictly to the right of \(2\). At \(a=1\), \(L(1)=f_1(1)=0<E_T(1)\). Hence exactly one crossing of \(L\) and \(E_T\) occurs in \((1/2,1)\). On either side, the minimum of these two branches is strictly smaller. This proves existence and uniqueness of the optimal exposure over the entire interval \([0,1]\).

**4. Parametric formula and uniqueness of its root.** At a local minimum \(x=s_-(a)\), the derivative equation gives \(a=1/[2-(x-2)^2]\); substituting in \(f_a(x)=f_a(T)\) and cancelling the positive denominator yields
\[
2(x-1)e^{T-x}=(T-1)^2+1-(x-2)^2.
\]
The crossing proved above gives exactly one solution \(x\in(1,2)\); no extraneous roots arise, because the map \(a\mapsto s_-(a)\) is a continuous strictly decreasing bijection from \((1/2,1)\) to \((1,2)\). Substituting back gives the stated sharp value. Note also that the left-minus-right side at \(x=1\) is negative and at \(x=2\) equals \(2e^{T-2}-(T-1)^2-1>0\) for \(T>2\) by the positive cubic and higher terms in the exponential series; this independently brackets the root.

**5. Large-radius law.** At the optimum, \(L(a_T)=E_T(a_T)\le e^{-T}(T-1)^2\to0\). Since \(L(a)>0\) for \(a<1\) and \(L\) is strictly decreasing to zero as \(a\uparrow1\), this forces \(a_T\to1\), hence \(x_T\to1\). Put \(w_T=1-a_T\). Differentiating the stationary-point equation near \(a=1\) gives \(x_T=1+w_T/2+O(w_T^2)\). Taylor expansion gives \(L(a_T)=e^{-1}w_T(1+O(w_T))\), while \(E_T(a_T)=e^{-T}[(T-1)^2+O(w_TT^2)]\). Equating these expressions yields \(w_T\sim e^{1-T}(T-1)^2\); reinserting in \(E_T\) yields \(C(T,a_T)\sim e^{-T}(T-1)^2\). These are asymptotics for fixed window types and varying disk radius, not claims about arbitrary windows.

## Verification

Run `python check.py` from this directory with Python 3, NumPy, SciPy, and mpmath installed. The checker directly integrates both centered Hermite ambiguity functions at selected points, compares the exact minimizer with dense radial and weight grids, runs a separate bounded numerical maximization, tests the radius-two equality interval, verifies equioscillation, and samples the long-radius asymptotics. On the recorded execution it returned `TWO_HERMITE_AMBIGUITY_CHECKS_PASS 17175`. These finite checks corroborate the exact proof but do not establish a global continuous optimization independently of the arguments above.

## Relationship to prior work

Alaifari and Yang (first publicly posted 2024-10-07) develop multi-window direct STFT phase retrieval using Hermite ambiguity functions and annular nonzero regions. Their Algorithm 2 partitions frequency-plane coverage among windows, and their Lemma 3.9 bounds noise error using a threshold in each region; their inspected sections do not give the present globally joint, exposure-weighted \(L^2\)-multiplier minimax design or its sharp transition. The Hermite-Laguerre ambiguity identity is pre-existing and is not claimed as new. Grohs, Liehr and Rathmair (2022) establish lattice uniqueness using windows assembled from Gaussian and first-Hermite components; those uniqueness criteria do not imply the present disk-dependent sharp squared lower multiplier bound. Cakrak and Loughlin (1998) optimize Hermite-spectrogram weights against a target time-varying Wigner spectrum, a different target from worst-case ambiguity inversion. Earlier classical minimax and two-branch equioscillation arguments are recognized as tools rather than claimed innovations. What is proposed as the contribution is the complete radius-dependent allocation theorem for the specified two-channel ambiguity multiplier. No claim of exhaustive historical priority is made.

## Limitations

The result is exact only for these two fixed windows, an ideal continuum of phase-space data, homogeneous whitened channel errors, and exposures constant across the disk. It does not optimize other Hermite degrees, mixtures in a single window, spatially varying exposures, or the statistical noise propagation of a complete nonlinear phase-retrieval estimator. Fourier-domain noise induced from intensity measurement can be correlated or nonwhite; the theorem's squared margin is then not the full physical noise sensitivity without additional hypotheses. The exact minimax expression is elementary once the specialized multiplier model is fixed, and equivalent special-purpose formulations could predate this analysis.

## References

1. R. Alaifari and Y. Yang, *Multi-Window Approaches for Direct and Stable STFT Phase Retrieval*, arXiv:2410.05486, first posted 2024-10-07; subsequently SIAM J. Appl. Math. 85 (2025), 2376–2398, DOI:10.1137/24M1701332. https://arxiv.org/abs/2410.05486
2. P. Grohs, L. Liehr and M. Rathmair, *Multi-window STFT phase retrieval: lattice uniqueness*, arXiv:2207.10620, first posted 2022-07-21. https://arxiv.org/abs/2207.10620
3. F. Cakrak and P. J. Loughlin, *Multiple Window Non-Linear Time-Varying Spectral Analysis*, IEEE ICASSP (1998). https://dihana.cps.unizar.es/proceedings/ICASSP/1998/pdf/author/ic982036.pdf
