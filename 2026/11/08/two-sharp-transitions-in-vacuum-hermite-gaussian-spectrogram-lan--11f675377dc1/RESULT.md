# Two sharp transitions in vacuum–Hermite Gaussian spectrogram landscapes

## Finding

Fix an integer \(m\ge3\) and \(a>0\). On the complex plane define
\[
H_{m,a}(z)=e^{-|z|^2}|1+a z^m|^2.
\]
This is, up to an irrelevant positive normalization and a rotation, the Gaussian-window spectrogram of the two-Hermite-mode signal \(h_0+b h_m\), where \(a=|b|/\sqrt{m!}\), in the dimensionless Bargmann coordinate. Define
\[
a_{\mathrm{fold}}(m)=\frac1{2(m-2)^{(m-2)/2}}.
\]
Let \(t_m\) be the unique point of \((m-2,m)\) satisfying
\[
2\log\frac{m}{m-t_m}=t_m,
\qquad
 a_{\mathrm{global}}(m)=\frac1{t_m^{(m-2)/2}(m-t_m)}.
\]
Then \(0<a_{\mathrm{fold}}(m)<a_{\mathrm{global}}(m)\), and the following is a **complete critical-point and global-maximizer classification**.

For \(0<a<a_{\mathrm{fold}}\) there is one strict local maximum (at \(z=0\)), exactly \(m\) nondegenerate saddle points, and exactly \(m\) nondegenerate minima, which are the zeros of \(1+a z^m\). At \(a=a_{\mathrm{fold}}\), exactly \(m\) additional degenerate critical points appear on the constructive rays (in addition to the origin, the \(m\) destructive-ray saddles, and \(m\) zeros). For \(a>a_{\mathrm{fold}}\), there are exactly \(m+1\) strict local maxima (the origin and \(m\) outer constructive-ray maxima), \(2m\) nondegenerate saddles, and \(m\) nondegenerate minima.

For \(0<a<a_{\mathrm{global}}\), the origin is the unique global maximum; at \(a=a_{\mathrm{global}}\), precisely the origin and all \(m\) outer maxima tie globally; for \(a>a_{\mathrm{global}}\), precisely the \(m\) outer maxima attain the global maximum. In particular, the interval \((a_{\mathrm{fold}},a_{\mathrm{global}})\) contains \(m\) genuine off-center local maxima that are **not** global.

Finally, the separation between the thresholds grows exponentially in the Hermite order:
\[
\frac{a_{\mathrm{global}}(m)}{a_{\mathrm{fold}}(m)}
\sim\frac{2e^{m/2}}{em}\qquad(m\to\infty).
\]

## Assumptions and scope

The Hermite functions use the standard Gaussian-normalized Bargmann convention \(\mathcal B h_k(z)=z^k/\sqrt{k!}\). The Gaussian-window STFT intensity at the scaled phase-space point \(z\) equals \(e^{-|z|^2}|\mathcal B f(z)|^2\) [1, Eq. (2.4)]. A complex nonzero coefficient \(b\) is reduced to positive \(a=|b|/\sqrt{m!}\) by an angular rotation; the prefactor from normalizing \(f\) is positive and changes neither critical positions nor types. The claims hold for each integer \(m\ge3\) and every finite \(a>0\), on the entire unbounded plane. All critical-point counts refer to distinct real critical points of the two-variable intensity \(H_{m,a}\); the zeros of its analytic factor are included as minima. No assertion is made for \(m=1,2\) or for a general Hermite superposition.

## Proof

Write \(z=\sqrt t e^{i\theta}\), \(t>0\). Directly,
\[
H_{m,a}(z)=e^{-t}\bigl(1+a^2t^m+2at^{m/2}\cos(m\theta)\bigr).
\]
The angular derivative forces \(\sin(m\theta)=0\) away from the origin. Therefore all nonzero critical points lie on the \(m\) constructive rays \(e^{im\theta}=1\) or the \(m\) destructive rays \(e^{im\theta}=-1\); no unexamined off-ray critical points exist. (Zeros also lie on destructive rays.) At the origin, \(H_{m,a}(z)=1-|z|^2+O(|z|^3)\), so its Hessian is negative definite for \(m\ge3\).

On a constructive ray, the radial profile is \(P_+(t)=(1+at^{m/2})^2e^{-t}\). Its stationary equation is
\[
a t^{(m-2)/2}(m-t)=1,\qquad 0<t<m.
\]
The function \(t^{(m-2)/2}(m-t)\) has its sole positive maximum at \(t=m-2\), with height \(2(m-2)^{(m-2)/2}\). Hence the constructive rays have zero, one degenerate, or two nonzero radial critical radii according as \(a\) lies below, equals, or lies above \(a_{\mathrm{fold}}\). Above threshold denote the squared radii by \(t_-<m-2<t_+\). The radial derivative changes signs \(-,+,-\); the angular second derivative is strictly negative. Thus \(t_-\) gives \(m\) saddles, \(t_+\) gives \(m\) strict local maxima. At threshold the radial first derivative has a quadratic zero, the radial second derivative of intensity vanishes, and the third is nonzero: these are \(m\) degenerate fold points. Expansion of the scalar equation also gives, for fixed \(m\) and \(\varepsilon\downarrow0\),
\[
t_{\pm}=m-2\ \pm\sqrt{\frac{8(m-2)}{m}}\sqrt\varepsilon+O_m(\varepsilon),
\quad a=a_{\mathrm{fold}}(1+\varepsilon).
\]

On a destructive ray, the profile is \(P_-(t)=(1-at^{m/2})^2e^{-t}\). It has the zero \(t_0=a^{-2/m}\), yielding a nondegenerate minimum because the analytic factor has a simple root. Its only other nonzero radial stationary point satisfies
\[
a t^{(m-2)/2}(t-m)=1,\qquad t>m.
\]
The left side increases strictly from zero to infinity on \((m,\infty)\), hence there is exactly one such radius. There the radial profile is at a strict maximum while the angular profile is at a strict minimum, giving exactly \(m\) saddles for every \(a>0\). These cases exhaust all critical points, proving the Morse-count classification, including the degenerate boundary.

Since \(H_{m,a}(z)\to0\) as \(|z|\to\infty\), every global maximum is one of the listed local maxima. At an outer constructive-ray maximum, its stationary equation gives \(a t_+^{m/2}=t_+/(m-t_+)\), so the height is
\[
P_+(t_+)=\left(\frac{m}{m-t_+}\right)^2 e^{-t_+}.
\]
As \(a\) increases above \(a_{\mathrm{fold}}\), \(t_+\) increases strictly from \(m-2\) to \(m\). The logarithm of the displayed height has derivative \(2/(m-t_+)-1>0\). At \(t_+=m-2\), it is \(2\log(m/2)-(m-2)<0\), by \(\log x<x-1\) for \(x>1\); as \(t_+\uparrow m\), it tends to infinity. Thus it crosses the origin height \(H_{m,a}(0)=1\) exactly once, at the unique root \(t_m\) defining \(a_{\mathrm{global}}\). All global-maximizer statements follow, with strict inequalities elsewhere.

For the large-order ratio put \(d_m=m-t_m\). The crossing identity gives
\[
d_m=m e^{-m/2}e^{d_m/2}.
\]
Because \(t_m>m-2\), \(0<d_m<2\), so \(d_m\sim m e^{-m/2}\). Therefore \(a_{\mathrm{global}}(m)\sim(e/m)^{m/2}\). Also \((m-2)^{(m-2)/2}\sim e^{-1}m^{(m-2)/2}\), giving \(a_{\mathrm{fold}}(m)\sim em/(2m^{m/2})\) and the claimed ratio.

## Verification

The standalone file `husimi_checks.py` performs finite independent checks of the threshold inequalities, the unique crossing relation, critical-radius equations, Cartesian gradients against centered finite differences, local radial types, exact normalization, global-height transitions, and the large-order ratio. Run `python husimi_checks.py` using Python 3. The packaged replay reported `HUSIMI_TWO_THRESHOLD_CHECKS_PASS 2207`. These checks corroborate the analytical identities; no finite sample of orders or parameters establishes the universal theorem. The universal conclusions are proved by the monotonicity and sign arguments above.

## Relationship to prior work

Abreu [1] establishes the Gaussian-STFT/Bargmann correspondence and analyzes expected critical-point densities of random Gaussian entire spectrograms (Theorem 1) and their value distributions (Theorem 2); neither theorem classifies deterministic two-mode coefficient thresholds. Chabaud, Markham and Grosshans [2] establish the stellar-function identity and classify finite stellar rank through zeros, but do not classify the nonzero gradient critical points, the two distinct thresholds, or global maxima of this family. Khan [3] analyzes Husimi maxima for individual number states and coherent-state orbit superpositions, rather than the vacuum-plus-number-state interference family. Mundarain and Stephany [4] study phase-space interference in displaced and squeezed number-state statistics, not this bifurcation of the Gaussian spectrogram. The general relation between critical points and the Chern connection is prior [1]; the claimed contribution is the exact all-orders **two-threshold deterministic morphology** and its exponentially separated parameter scales.

## Limitations

The classification is for one specific two-term Hermite family and a Gaussian analysis window. It says nothing about generic or random spectrograms, reconstruction from sampled data, arbitrary polynomial Bargmann signals, or physical dynamical hysteresis. Thresholds depend on the explicit dimensionless coordinate and coefficient convention stated above. The deterministic all-orders phase portrait may have appeared implicitly in classical Husimi/coherent-state discussions; priority remains subject to further literature checking and independent expert assessment.

## References

[1] L. D. Abreu, “Local maxima of white noise spectrograms and Gaussian Entire Functions,” arXiv:2210.06721v1, first submitted 2022-10-13, https://arxiv.org/html/2210.06721v1 (Secs. 2–4, esp. Eq. (2.4), Proposition 1, Theorems 1–2).

[2] U. Chabaud, D. Markham, F. Grosshans, “Stellar representation of non-Gaussian quantum states,” arXiv:1907.11009v1, first submitted 2019-07-25, https://arxiv.org/abs/1907.11009 (stellar function and Eq. (3), main text and supplement).

[3] M. N. Khan, “Getting coherent state superpositions to stay put in phase space: Q functions and one dimensional integral representations of generator eigenstates,” arXiv:1911.09966, first submitted 2019-11-22, https://arxiv.org/abs/1911.09966 (Introduction and Sec. IV.1).

[4] D. F. Mundarain and J. Stephany, “Husimi's Q(alpha) function and quantum interference in phase space,” arXiv:quant-ph/0311151v2, original submission 2003-11-21, https://arxiv.org/html/quant-ph/0311151v2 (Secs. 1–3).
