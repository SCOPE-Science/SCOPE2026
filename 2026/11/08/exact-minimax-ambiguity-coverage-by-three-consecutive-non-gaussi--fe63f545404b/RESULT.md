# Exact minimax ambiguity coverage by three consecutive non-Gaussian Hermite windows

## Finding

Let \(h_1,h_2,h_3\) be the first three positive-order, unit-norm Hermite functions with centered ambiguity functions \(\mathcal A h_j(x,\xi)=e^{-\tau/2}L_j(\tau)\), where \(\tau=\pi(x^2+\xi^2)\), and \(L_j\) is the ordinary Laguerre polynomial. For a nonnegative exposure allocation \(w=(w_1,w_2,w_3)\) with \(w_1+w_2+w_3=1\), define its Gaussian-relative squared ambiguity margin by

\[
 C(w)=\inf_{\tau\ge0}\sum_{j=1}^{3}w_j L_j(\tau)^2.
\]

There is a unique maximizing allocation. Let \(u\in(3/5,2/3)\) be the unique real root of
\[
 u^3-9u^2+24u-12=0,
\]
and put \(c=3-3u+u^2/2\). Then
\[
 \boxed{\max_{w_j\ge0,\;\sum w_j=1}C(w)=(1-u)^2},\qquad
 \boxed{w^*=\left(\frac{c}{1+c},\;0,\;\frac1{1+c}\right)}.
\]
The worst radial parameter is uniquely \(\tau=u\); thus equality in the time-frequency inequality occurs precisely on the circle \(\pi(x^2+\xi^2)=u\). Numerically, \(u\approx0.644698602391879\), \(C(w^*)\approx0.126239083142284\), and \(w_1^*\approx0.5601925600938\). Adding a positive allocation to the intermediate Hermite window \(h_2\) strictly decreases the best achievable margin.

Equivalently, for all real \(x,\xi\),
\[
\sum_{j=1}^3w_j^*|\mathcal A h_j(x,\xi)|^2
\ge (1-u)^2e^{-\pi(x^2+\xi^2)},
\]
with the displayed equality set. The optimization is about the Gaussian-relative multiplier, not a uniform unweighted inverse bound.

## Assumptions and scope

The Hermite functions are normalized in \(L^2(\mathbb R)\), with the time-frequency convention in the cited source. Their ambiguity functions are radial with the common factor \(e^{-\tau/2}\). Explicitly,
\[
 L_1(t)=1-t,\qquad L_2(t)=1-2t+\frac{t^2}{2},\qquad
 L_3(t)=1-3t+\frac{3t^2}{2}-\frac{t^3}{6}.
\]
For multiple ambiguity observations of the form \(Y_j=\mathcal A f\,\overline{\mathcal A h_j}\), the denominator of the weighted pointwise least-squares normal equation is \(\sum_j w_j|\mathcal A h_j|^2\). The objective isolates its loss from *zeros* and Hermite-mode interference relative to the common Gaussian decay. The domain is every real \(t\ge0\), the allocation simplex includes its boundary, and the objective is the infimum of a nonnegative polynomial. For strictly positive weights, the displayed constant is a supremum, not an attained maximum.

## Proof

**1. A uniquely defined contact radius.** Set \(r(z)=z^3-9z^2+24z-12\). Since \(r'(z)=3(z-2)(z-4)\), \(r(2)=8\), \(r(4)=4\), and \(r(0)=-12\), the polynomial has exactly one real zero. Because \(r(3/5)<0<r(2/3)\), that zero is \(u\in(3/5,2/3)\). Direct substitution gives \(L_3(u)=-L_1(u)=-(1-u)\). Moreover,
\[
 L_1(u)^2-L_2(u)^2
 =\frac{u(2-u)(u^2-6u+4)}4>0,
\]
as \(u^2-6u+4>0\) throughout \((3/5,2/3)\).

**2. Universal upper certificate.** Every admissible allocation satisfies
\[
 C(w)\le \sum_{j=1}^3w_jL_j(u)^2
 =(1-u)^2-w_2\big((1-u)^2-L_2(u)^2\big)
 \le(1-u)^2.
\]
This inequality is strict whenever \(w_2>0\).

**3. Exact lower certificate.** Let \(c=3-3u+u^2/2=-L_3'(u)>0\), and set
\[
 B=\frac{3(3u^2-23u+48)}{9-u},\qquad
 D=\frac{1-u}{3(9-u)},\qquad
 E=\frac{39-u-2u^2}{(9-u)^2}.
\]
All denominators are positive; \(D,E>0\) because \(0<u<2/3\). The following exact polynomial identity holds, using only \(r(u)=0\):
\[
\begin{aligned}
 &cL_1(t)^2+L_3(t)^2-(1+c)(1-u)^2\\
 &\quad=(t-u)^2\left[\frac{\big(t^2-(9-u)t+B\big)^2}{36}+Dt^2+E\right].
\end{aligned}
\]
The bracket is strictly positive for every real \(t\). Division by \(1+c\) proves \(C(w^*)=(1-u)^2\); moreover equality is possible only at \(t=u\).

**4. Uniqueness of the allocation.** Step 2 forces \(w_2=0\) for any optimal allocation. With \(w_3=1-w_1\), differentiation at the interior contact \(u\) gives
\[
 \left.\frac{d}{dt}\left(w_1L_1(t)^2+w_3L_3(t)^2\right)\right|_{t=u}
 =2(1-u)(cw_3-w_1).
\]
A differentiable function attaining its global minimum at the interior point \(u\) must have zero derivative there. Hence \(w_1=cw_3\), and the simplex constraint yields exactly \(w^*\). Conversely, the lower certificate already proves that allocation optimal. This completes the proof.

## Verification

Run `python verify.py` with Python 3 and SymPy installed. The checker reduces the exact polynomial identity modulo \(r(u)\), checks the rational isolating interval and positivity inequalities, and supplements the algebra with 5,001 numerical points on \([0,16]\). It prints `HERMITE_123_MINIMAX_CERTIFICATE_PASS 5001` when all assertions succeed. The proof applies to the entire continuous half-line; the finite grid is not its justification.

## Relationship to prior work

Alaifari and Yang, *Multi-Window Approaches for Direct and Stable STFT Phase Retrieval* (arXiv:2410.05486, first publicly posted October 7, 2024), introduce Hermite-window ambiguity coverage and the exact Laguerre ambiguity formula. Their patchwise stability-set construction and noise estimates do not provide the present globally sharp exposure allocation, unique unused middle window, or the algebraic bottleneck radius. Hansson-Sandsten and Sandberg (2010) optimize multitaper spectrogram weights for process-dependent mean-square error, a different functional from the all-radius, Gaussian-relative ambiguity margin studied here. The three-window conclusion is not implied by a two-window optimization restricted to \(h_1,h_2\), since the optimal allocation uses \(h_3\) and excludes \(h_2\).

## Limitations

This is a sharp scalar ambiguity-multiplier guarantee after removal of a Gaussian envelope. It does not assert global uniform invertibility of ambiguity deconvolution without the Gaussian weight, nor quantitative nonlinear phase-retrieval stability for arbitrary signals. Weights are nonnegative and sum to one; an all-strictly-positive design can approximate but cannot attain the optimum. Results for other Hermite orders, alternative normalizations, or finite radial domains are not claimed. Historical novelty is assessed against the named accessible sources and research records; exhaustive priority certification is not claimed.

## References

1. R. Alaifari and Y. Yang, *Multi-Window Approaches for Direct and Stable STFT Phase Retrieval*, arXiv:2410.05486, first publicly available October 7, 2024; publicly accessible 2024 ETH Zürich report, https://www.sam.math.ethz.ch/sam_reports/reports_final/reports2024/2024-30_rev1.pdf .
2. M. Hansson-Sandsten and J. Sandberg, *Optimization of Weighting Factors for Multiple Window Spectrogram of Event-Related Potentials*, EURASIP Journal on Advances in Signal Processing (2010), https://doi.org/10.1155/2010/391798 .
