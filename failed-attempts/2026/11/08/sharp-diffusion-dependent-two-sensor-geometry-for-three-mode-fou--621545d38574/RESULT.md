# Sharp diffusion-dependent two-sensor geometry for three-mode Fourier heat sampling

## Finding
Let \(q=e^{-T}\) with \(T>0\), and put \(h=1+q^2\), \(u=\cos^2(\theta/2)\). For a fixed pair of spatial sensors separated by \(\theta\in[0,\pi]\), the four unweighted complex heat samples at times \(0,T\) determine all three Fourier coefficients exactly when \(0<\theta<\pi\). The squared singular values are the scalar \(4h(1-u)\) and the eigenvalues of
\[
E_q(u)=\begin{pmatrix}4hu&2\sqrt2(1+q)\sqrt{u}\\2\sqrt2(1+q)\sqrt{u}&4\end{pmatrix}.
\]
Define
\[
A(q)=4(1+q^2)^2+2(1+q^2)q^2-(1-q)^2,
\qquad
u_*(q)=\frac{A(q)+\sqrt{A(q)^2-32(1+q^2)^3q^2}}{8(1+q^2)^2}.
\]
Then \(1/2<u_*(q)<1\), and the **unique sharp maximizer of the squared lower singular value** is the sensor separation
\[
\theta_*(T)=2\arccos\sqrt{u_*(e^{-T})}.
\]
Its optimal squared lower singular value is
\[
\Lambda_*(T)=4(1+e^{-2T})\bigl(1-u_*(e^{-T})\bigr).
\]
Uniqueness is modulo simultaneous rotation of both sensors and interchange of the sensors; no condition-number optimality is claimed. The two extreme-time regimes are
\[
\lim_{T\to\infty}\theta_*(T)=\frac{\pi}{3},\quad \lim_{T\to\infty}\Lambda_*(T)=1,
\qquad
\theta_*(T)\sim\frac{1-e^{-T}}{\sqrt3},\quad
\Lambda_*(T)\sim\frac23(1-e^{-T})^2 \quad(T\downarrow0).
\]

## Assumptions and scope
The object is the complex Fourier band \(\mathcal V=\operatorname{span}_{\mathbb C}\{e^{-ix},1,e^{ix}\}\) on the unit circle, with coefficient norm \(\|(a_{-1},a_0,a_1)\|_2\). The heat equation is \(\partial_t f_t=\partial_x^2 f_t\) and initial data \(f_0(x)=\sum_{k=-1}^1a_ke^{ikx}\). The measuring device obtains one complex scalar value at each spatial location at each of the two times \(0,T\), with equal measurement weight and independent equal-variance additive noise if noise is considered. Rotational invariance permits sensor coordinates \(-\theta/2,+\theta/2\); all conclusions concern the raw \(4\times3\) complex analysis matrix, without divided-by-four normalization. The two sampling times are prescribed, not optimized. The theorem holds for every real \(T>0\) and every \(\theta\in[0,\pi]\).

## Proof
**Exact block reduction.** In the original coefficient order \((-1,0,1)\), a sample at \((t,x)\) has row \((e^{-t}e^{-ix},1,e^{-t}e^{ix})\). Apply the unitary even/odd coefficient change \((a_{-1},a_1)\mapsto((a_{-1}+a_1)/\sqrt2,(a_1-a_{-1})/\sqrt2)\) and the orthonormal sum/difference of the measurements at the two sensors independently at each time. The transformed observation matrix splits into an even \(2\times2\) block
\[
M_{\mathrm{even}}=\begin{pmatrix}2\sqrt u&\sqrt2\\2q\sqrt u&\sqrt2\end{pmatrix}
\]
and an odd \(2\times1\) block of modulus entries \(2\sqrt{1-u}\) and \(2q\sqrt{1-u}\) (irrelevant unit-modulus phase factors may be absorbed into rows/columns). Therefore its Gram spectrum is precisely that displayed above. Since \(\det E_q(u)=8u(1-q)^2\), all three Gram eigenvalues are positive exactly when \(0<u<1\), equivalent to \(0<\theta<\pi\).

**Strict minimax crossing.** Write \(\mu_q(u)\) for the smaller eigenvalue of \(E_q(u)\). Its characteristic equation is
\[
\mu^2-4(1+hu)\mu+8u(1-q)^2=0.
\]
For \(0<u\le1\), define \(d=1-q\) and \(\alpha=2d^2/h\). Evaluating this polynomial at \(\alpha\) gives \(\alpha^2-4\alpha<0\), hence \(0<\mu_q(u)<\alpha<2\). Solving for \(u\) yields
\[
u=\frac{\mu(4-\mu)}{8d^2-4h\mu}.
\]
The numerator is strictly increasing on \((0,2)\), the denominator is positive and strictly decreasing on \((0,\alpha)\), so \(\mu_q(u)\) is strictly increasing in \(u\). The odd eigenvalue \(4h(1-u)\) is strictly decreasing. At \(u=0\) the increasing branch is zero and the decreasing branch positive; at \(u=1\) the reverse holds. Their minimum therefore has a unique global maximizer, at their unique crossing.

**Algebraic optimizer.** Substitute \(\mu=4h(1-u)\) into the characteristic equation. Division by a positive scalar gives
\[
P_q(u)=4h^2u^2-A(q)u+2hq^2=0.
\]
One checks \(P_q(1/2)=-(1+q)^2/2<0\) and \(P_q(1)=(1-q)^2>0\), so the crossing is the unique root in \((1/2,1)\), namely the larger quadratic root \(u_*(q)\). At that crossing, \(\mu_q=4h(1-u)\) (rather than the larger eigenvalue) by the preceding unique-minimax crossing argument. This proves both the formula and global uniqueness.

**Endpoint asymptotics.** As \(q\downarrow0\), the crossing polynomial tends to \(4u^2-3u\); its root in \((1/2,1)\) is \(3/4\), hence the limiting angle is \(2\arccos(\sqrt3/2)=\pi/3\), and \(4h(1-u)\to1\). As \(q\uparrow1\), the unique root tends to \(u=1\). The product of the two eigenvalues of \(E_q(u_*)\) is \(8u_*(1-q)^2\); its larger eigenvalue tends to \(12\) (the nonzero eigenvalue of \(E_1(1)\)). Consequently \(\mu_q(u_*)\sim (2/3)(1-q)^2\). Equating it with \(4h(1-u_*)\) gives \(1-u_*(q)\sim(1-q)^2/12\), and the stated angular asymptotic follows from \(2\arccos\sqrt u\sim2\sqrt{1-u}\).

## Verification
The accompanying Python checker `CHECK.py` constructs the full complex \(4\times3\) observation matrix independently of the block formula, compares all its Gram eigenvalues against the analytic spectrum, tests the claimed optimal lower bound against dense competing angles, and checks both asymptotic regimes. It completed with `HEAT_TWO_SENSOR_CHECKS_PASS 1695`. These finite tests are reproducibility checks, not substitutes for the proof of the universal optimization and limiting assertions above.

## Relationship to prior work
Aldroubi, Gröchenig, Huang, Jaming, Krishtal, and Romero developed dynamic space–time sampling and heat-flow reconstruction bounds for bandlimited functions. Their full preprint examines stability, Fourier blind spots, finite-dimensional recovery and Remez-type estimates; its results are not an exact E-optimal two-position design for the specified three-mode periodic heat matrix. Huang, Needell, and Tang analyzed randomized space–time sampling on graphs, not the deterministic sharp two-position angle. Lu and Vetterli earlier established spatial–temporal diffusion trade-offs and sensor-configuration conditions; only the bibliographic record and abstract of that closely related conference paper were accessible here, so an implicit priority overlap cannot be excluded. Related published work on two sensors in graph harmonic frames uses spectral demixing, unlike the raw temporally coupled four-measurement operator analyzed here.

## Limitations
The result is for exactly three complex Fourier modes, exactly two fixed spatial points and the two prescribed times \(0,T\); it is not a universal sensor-design theorem for more bands, unequal measurement weights, spatially varying diffusivity, discrete graphs, or unknown time separation. The result maximizes the smallest **squared** singular value, not the determinant or the condition number. The limiting case \(T\to\infty\) is a limit of finite-time designs, not a finite-time recovery at \(q=0\). A historically equivalent specialized formula could be embedded in older diffusion sensor literature, especially Lu–Vetterli (2009), whose full text was not materially available. There has been no independent audit.

## References
- A. Aldroubi, K. Gröchenig, L. Huang, P. Jaming, I. Krishtal, J. L. Romero, *Sampling the flow of a bandlimited function*, first available April 29, 2020, https://arxiv.org/abs/2004.14032 ; J. Geom. Anal. (2021), https://doi.org/10.1007/s12220-021-00617-0.
- L. Huang, D. Needell, S. Tang, *Robust recovery of bandlimited graph signals via randomized dynamical sampling*, first available September 28, 2021, https://arxiv.org/abs/2109.14079.
- Y. M. Lu, M. Vetterli, *Spatial super-resolution of a diffusion field by temporal oversampling in sensor networks*, ICASSP 2009, https://doi.org/10.1109/ICASSP.2009.4960067 (abstract and bibliographic record inspected; full text not available).
- A. Aldroubi et al., *Reconstructing Graph Signals from Noisy Dynamical Samples*, first available November 19, 2024, https://arxiv.org/abs/2411.12670 (abstract consulted for contextual comparison).
