# Charge-conserving three-to-five zero transition for the first-Hermite two-tone spectrogram

## Finding
For any \(\sigma,\omega>0\), analyze the equal-amplitude two-tone signal with the first Hermite (Gaussian-derivative) window defined below. On each fundamental time-frequency cylinder, the complete spectrogram zero set undergoes one and only one bifurcation at the dimensionless separation \(\sigma\omega=1\). There are three distinct zeros for \(\sigma\omega\le1\) and five for \(\sigma\omega>1\). The transition is a signed-index-conserving pitchfork: two positive-charge zeros split off the center while the central charge changes from positive to negative. Explicit scalar equations locate every zero, including the two exterior negative-charge zeros present at all separations.

## Assumptions and scope
Choose arbitrary real numbers \(\sigma>0\), \(\omega>0\), let \(f(s)=e^{i\omega s}+e^{-i\omega s}=2\cos(\omega s)\), and let \(h_\sigma(u)=u\exp[-u^2/(2\sigma^2)]\). Define the absolutely convergent short-time Fourier transform
\[
V(t,\xi)=\int_{\mathbb R}f(s)h_\sigma(s-t)e^{-i\xi s}\,ds,\qquad(t,\xi)\in\mathbb R^2.
\]
The signal is bounded and tempered, not square-integrable; the Hermite window is Schwartz, so this integral is well-defined. Window normalization does not affect zeros. Under \(t\mapsto t+\pi/\omega\), \(V\) is multiplied by a nonzero unimodular factor. We therefore count distinct zeros on \(\mathcal C=(\mathbb R/(\pi/\omega)\mathbb Z)\times\mathbb R\). Local index means the winding number of the complex-valued function on an anticlockwise small loop in the oriented chart \((t,\xi)\) with orientation \(dt\wedge d\xi\). The spectrogram \(|V|^2\) and the complex transform have precisely the same zeros; charge refers to the complex STFT, not to the Jacobian of its squared modulus.

Put \(c=\sigma^2\omega^2\), and write \(\operatorname{arcoth}(v)=\frac12\log\frac{v+1}{v-1}\) for \(v>1\).

**Theorem.** For every \(c>0\), there is exactly one \(v_c>1\) satisfying \(\operatorname{arcoth}(v_c)=cv_c\). Exactly two exterior zeros occur, at \(\big(\pi/(2\omega),\pm\omega v_c\big)\), and both have index \(-1\). There is always a central zero at \((0,0)\). If \(0<c<1\) it is regular with index \(+1\); if \(c=1\) it is isolated but degenerate with cubic frequency tangency and index \(+1\); if \(c>1\) it is regular with index \(-1\). Exactly when \(c>1\), the unique \(u_c\in(0,1)\) solving \(\operatorname{artanh}(u_c)=cu_c\) produces two additional regular index-\(+1\) zeros at \((0,\pm\omega u_c)\). There are no others. Thus the number of distinct zeros is \(3\) for \(c\le1\) and \(5\) for \(c>1\), and the total of all local indices is \(-1\) for every \(c>0\).

The split pair obeys \(u_c=\sqrt{3(c-1)}\,[1+O(c-1)]\) as \(c\downarrow1\). As \(c\to\infty\), both \(1-u_c\) and \(v_c-1\) are asymptotic to \(2e^{-2c}\); as \(c\downarrow0\), \(v_c\sim c^{-1/2}\).

## Proof
**1. Reduction to two real amplitudes.** For real \(k\), differentiation of the Gaussian Fourier integral gives
\[
\int_{\mathbb R}u e^{-u^2/(2\sigma^2)}e^{-iku}\,du=-i\sqrt{2\pi}\sigma^3 k e^{-\sigma^2k^2/2}.
\]
Consequently, with real smooth functions
\[
A(\xi)=(\xi-\omega)e^{-\sigma^2(\xi-\omega)^2/2},\qquad
B(\xi)=(\xi+\omega)e^{-\sigma^2(\xi+\omega)^2/2},
\]
we have
\[
V(t,\xi)=-i\sqrt{2\pi}\sigma^3e^{-i(\xi+\omega)t}J(t,\xi),\qquad
J(t,\xi)=A(\xi)e^{2i\omega t}+B(\xi).
\]
The prefactor never vanishes and multiplies the real Jacobian at a zero by a positive determinant, so zeros and their signed indices are those of \(J\). At \(\xi=\pm\omega\) exactly one of \(A,B\) vanishes and the other does not. All zeros therefore obey \(|A|=|B|>0\), and their time phase is \(e^{2i\omega t}=+1\) inside \((-\omega,\omega)\), where \(AB<0\), or \(-1\) outside, where \(AB>0\).

**2. All interior zeros.** Set \(u=\xi/\omega\) for \(|u|<1\). The ratio of magnitudes is
\[
\frac{|A(\xi)|}{|B(\xi)|}=\frac{1-u}{1+u}e^{2cu},
\]
so equality is equivalent to \(\operatorname{artanh}(u)=cu\). The central solution \(u=0\) always exists. For \(0<u<1\), the function \(\operatorname{artanh}(u)/u=\sum_{n\ge0}u^{2n}/(2n+1)\) is strictly increasing from \(1\) to infinity. Thus noncentral solutions occur if and only if \(c>1\), with exactly one positive \(u_c\), one negative \(-u_c\), and only the phase \(t=0\pmod{\pi/\omega}\).

**3. All exterior zeros.** Let \(v=\xi/\omega>1\). The magnitude equation becomes \(\operatorname{arcoth}(v)=cv\). The function \(\operatorname{arcoth}(v)/v\) is strictly decreasing from infinity to zero, since its numerator is positive and strictly decreasing. Hence exactly one \(v_c>1\) exists for any \(c>0\). The modulus equation at negative frequencies is equivalent by symmetry, giving \(-v_c\). The phase is exactly \(t=\pi/(2\omega)\pmod{\pi/\omega}\). This proves the exhaustive zero count.

**4. Signed indices.** At any zero with \(\xi\ne\pm\omega\), let \(r(\xi)=|A(\xi)|/|B(\xi)|\). Differentiating the real and imaginary parts of \(J\) at the corresponding real phase gives
\[
\det D_{(t,\xi)}(\Re J,\Im J)=-2\omega B(\xi)^2\frac{d}{d\xi}\log r(\xi).
\]
Inside the central band, the logarithmic derivative is
\[
\frac d{d\xi}\log r(\xi)=2\omega\left(\sigma^2-\frac1{\omega^2-\xi^2}\right).
\]
At \(\xi=0\), it has the sign of \(c-1\). At \(\xi=\pm\omega u_c\), the strict inequality \(\operatorname{artanh}(u_c)/u_c<1/(1-u_c^2)\) follows term-by-term from the positive power series, so this derivative is strictly negative. Outside the central band, the logarithmic derivative is
\[
\frac d{d\xi}\log r(\xi)=2\omega\left(\sigma^2+\frac1{\xi^2-\omega^2}\right)>0.
\]
The stated regularity and signs of all noncritical zeros follow.

**5. Critical local degree.** At \(c=1\), put \(u=\xi/\omega\). Along \(t=0\) the ratio of positive interior amplitudes obeys
\[
\log r(\omega u)=\log\frac{1-u}{1+u}+2u=-\frac23u^3+O(u^5).
\]
Thus \(\Re J(0,\omega u)=\frac23\omega e^{-1/2}u^3+O(u^4)\), while \(\partial_t\Im J(0,0)=-2\omega^2e^{-1/2}<0\), and \(\partial_t\Re J(0,0)=0\). The implicit-function theorem resolves the local zero equation \(\Im J=0\) into a smooth curve \(t=t(\xi)\), with \(t(\xi)=O(\xi^2)\) (in fact identically zero near the center). Along that curve \(\Re J\) has the sign of \(\xi^3\). Hence the isolated critical zero has winding index \(+1\), even though its ordinary Jacobian vanishes. Summing the indices gives \(+1-1-1=-1\) at and below criticality, and \(-1+1+1-1-1=-1\) above it.

**6. Scaling.** Expanding \(\operatorname{artanh}(u_c)/u_c=1+u_c^2/3+O(u_c^4)\) yields the square-root law. The logarithmic formulas for the interior and exterior equations imply \(1-u_c\sim2e^{-2c}\) and \(v_c-1\sim2e^{-2c}\) at large \(c\). The large-\(v\) expansion \(\operatorname{arcoth}(v)/v=v^{-2}+O(v^{-4})\) yields the small-\(c\) exterior law.

## Verification
Running `python CHECK.py` (Python 3 standard library) solves the independent scalar root equations at eight values of \(c\), evaluates the exact prefactor-free STFT at every predicted zero, checks the noncritical Jacobian signs using finite differences, and independently integrates the original Gaussian-derivative STFT numerically at three nonzero locations per parameter. The checker terminates with `ALL_FIRST_HERMITE_CHECKS_PASSED`. Numerical tests are not used to prove the global zero count or critical local degree; those follow from Steps 2–5.

## Relationship to prior work
Bellourak, Meignen, Polisano, and Nahon (2026) introduce the charge decomposition of Hermite-window spectrogram zeros and analyze their random spatial statistics for complex white noise. The present theorem instead concerns deterministic two-tone data, computes the entire zero set for every tone separation, and describes a nonregular charged collision. Poinas and Bardenet (2025) find exact zeros for two parallel chirps analyzed with a **Gaussian** window; their noiseless zeros lie on one line. The earlier Balazs–Bayer–Jaillet–Søndergaard example also uses a Gaussian window for two complex exponentials. Neither the Gaussian two-tone zero line nor the stochastic Hermite-window formulas yields the five-zero transition for the first Hermite window as a stated conclusion. These are comparisons of hypotheses and implications, not assertions that no older equivalent computation exists.

## Limitations
The theorem concerns equal-amplitude opposite tones and the order-one Hermite window; it does not classify arbitrary multitone signals, unequal amplitudes, higher-order Hermite windows, or stochastic zero processes. The signal is tempered rather than square-integrable. The signed sum is a computed finite-cylinder invariant, not a general conservation theorem for arbitrary windows. Novelty remains subject to independent literature verification, especially specialist discussions of Gaussian-derivative windows.

## References
1. C. Bellourak, S. Meignen, K. Polisano, and M. Nahon, *Zeros of the Spectrogram of White Noise with Hermite Windows*, arXiv:2610.13531v1 (first posted 2026-10-09), https://arxiv.org/abs/2610.13531.
2. J. Poinas and R. Bardenet, *On two fundamental properties of the zeros of spectrograms of noisy signals*, arXiv:2507.13829, https://arxiv.org/abs/2507.13829.
3. P. Balazs, D. Bayer, F. Jaillet, and P. Søndergaard, *The pole behavior of the phase derivative of the short-time Fourier transform*, Applied and Computational Harmonic Analysis, DOI:10.1016/j.acha.2015.10.001.
4. R. Alaifari and Y. Yang, *Multiwindow Approaches for Direct and Stable STFT Phase Retrieval*, SIAM Journal on Applied Mathematics 85 (2025), DOI:10.1137/24M1701332.
