# Exact Fourier shape Hessian of Gaussian time-frequency localization at a disk

## Finding
Let \(R>0\), and let \(u\in C^2(\mathbb T;\mathbb R)\) have zero angular mean. In the time-frequency plane \(\mathbb R^2\cong\mathbb C\), set
\[
\Omega_\varepsilon=\{z:\;0\le\pi|z|^2<R+\varepsilon u(\arg z)\},
\]
for sufficiently small real \(\varepsilon\). These domains have area exactly \(R\). Let \(\varphi(t)=2^{1/4}e^{-\pi t^2}\), let \(V_\varphi\) be the unitary-normalized Gaussian short-time Fourier transform, and let
\[
\Lambda(\varepsilon)=\|V_\varphi^*\mathbf1_{\Omega_\varepsilon}V_\varphi\|_{L^2(\mathbb R)\to L^2(\mathbb R)}.
\]
Define \(\widehat u(n)=(2\pi)^{-1}\int_0^{2\pi}u(\theta)e^{-in\theta}\,d\theta\), and, for integers \(n\ge1\),
\[
S_n(R)=\sum_{j=1}^{n}\frac{R^j}{j!},\qquad
h_n(R)=1-\frac{R^n}{n!S_n(R)}.
\]
Then the exact area-constrained shape-Hessian formula is
\[
\boxed{\Lambda(\varepsilon)=1-e^{-R}-\varepsilon^2e^{-R}
\sum_{n=2}^{\infty}h_n(R)|\widehat u(n)|^2+o(\varepsilon^2).}
\]
The Fourier weights are strictly increasing:
\[
0=h_1(R)<h_2(R)=\frac{2}{R+2}<h_3(R)<\cdots<1,
\qquad \lim_{n\to\infty}h_n(R)=1.
\]
Thus the real first angular harmonics are **exactly** the nullspace of the area-constrained shape Hessian (they are infinitesimal translations); among all other modes, the second harmonics are the unique least-penalized directions. In particular, with angular probability measure and \(\Pi_{\ge2}\) the projection to the real Fourier frequencies of absolute value at least two,
\[
\boxed{\lim_{\varepsilon\to0}\frac{\Lambda(0)-\Lambda(\varepsilon)}{\varepsilon^2}
\ge \frac{e^{-R}}{R+2}\|\Pi_{\ge2}u\|_{L^2(\mathbb T)}^2,}
\]
and the constant is sharp, with equality precisely for perturbations supported on frequencies \(\pm1,\pm2\); a nonzero second-frequency component demonstrates nontrivial sharpness. For \(u(\theta)=\cos(2\theta)\), the deficit is \(\varepsilon^2e^{-R}/[2(R+2)]+o(\varepsilon^2)\).

The maximizing signal also has an exact first-order response. In the normalized Fock basis \(e_n(z)=\pi^{n/2}z^n/\sqrt{n!}\), let \(F_\varepsilon\) be the normalized leading eigenfunction with \(\langle F_\varepsilon,e_0\rangle>0\). Then
\[
\boxed{F_\varepsilon=e_0+\varepsilon\sum_{n=1}^{\infty}
\frac{R^{n/2}\widehat u(n)}{\sqrt{n!}\,S_n(R)}\,e_n
+O_{R,u}(\varepsilon^2)}
\]
in the Fock norm. The same statement transfers to \(L^2(\mathbb R)\) by the Bargmann transform.

## Assumptions and scope
The Fock space consists of entire functions with norm \(\|F\|^2=\int_\mathbb C|F(z)|^2e^{-\pi|z|^2}\,dA(z)\). The disk area parameter \(R\) is arbitrary but fixed and positive. The function \(u\) is real-valued, twice continuously differentiable, and has mean zero. The boundary description uses the **squared radius** \(s=\pi|z|^2\), not Euclidean radial displacement; this normalization makes the area exactly \(R\) for all admissible \(\varepsilon\). A sign change in the angular coordinate of the STFT/Bargmann convention conjugates Fourier coefficients but leaves the Hessian unchanged.

The second-order expansion is directional for each fixed \(u\), not a uniform nonlinear stability estimate over all boundary profiles. The sharp constant refers to the quadratic form in this squared-radius boundary normalization and after modding out translations.

## Proof
**1. Exact operator matrix and regularity.** Under the Bargmann transform, the concentration operator becomes \(T_\varepsilon=P_{\mathcal F^2}\mathbf1_{\Omega_\varepsilon}\), with matrix entries
\[
\langle T_\varepsilon e_k,e_j\rangle
=\frac{1}{2\pi\sqrt{j!k!}}
\int_0^{2\pi}e^{i(k-j)\theta}
\left(\int_0^{R+\varepsilon u(\theta)}e^{-s}s^{(j+k)/2}\,ds\right)d\theta.
\]
Here the polar area element is \(ds\,d\theta/(2\pi)\). More conceptually, \(T_\varepsilon\) is the integral of rank-one coherent-state projectors over the same region. Since the boundary remains in a compact subinterval of \((0,\infty)\), differentiating the boundary integral twice (or any fixed number of times) is legitimate in the trace-class norm. This justifies applying simple-eigenvalue perturbation theory to the infinite-dimensional operator; finite matrix approximations are not being used to justify this step.

At \(\varepsilon=0\), rotational invariance makes the operator diagonal:
\[
\lambda_n=\int_0^R e^{-s}\frac{s^n}{n!}\,ds
=1-e^{-R}\sum_{j=0}^{n}\frac{R^j}{j!}.
\]
Thus \(\lambda_0=1-e^{-R}\), and \(\lambda_0-\lambda_n=e^{-R}S_n(R)>0\) for all \(n\ge1\). The leading eigenvalue is simple, with an explicit gap \(Re^{-R}\) to the rest of the spectrum.

**2. Shape derivatives.** Differentiating the displayed matrix and using \(\widehat u(0)=0\) gives
\[
\langle T'_0e_0,e_0\rangle=0,\qquad
\langle T'_0e_0,e_n\rangle=e^{-R}\frac{R^{n/2}}{\sqrt{n!}}\widehat u(n).
\]
For the second derivative,
\[
\frac12\langle T''_0e_0,e_0\rangle
=-\frac{e^{-R}}2\int_0^{2\pi}u(\theta)^2\frac{d\theta}{2\pi}.
\]
The classical, justified simple-eigenvalue perturbation formula therefore yields the coefficient of \(\varepsilon^2\) in \(\Lambda(\varepsilon)\):
\[
-\frac{e^{-R}}2\|u\|_2^2
+\sum_{n\ge1}\frac{e^{-2R}R^n|\widehat u(n)|^2}{n!(\lambda_0-\lambda_n)}.
\]
Since \(u\) is real and mean zero, Parseval says \(\|u\|_2^2=2\sum_{n\ge1}|\widehat u(n)|^2\). Substitution of \(\lambda_0-\lambda_n=e^{-R}S_n(R)\) gives exactly \(-e^{-R}\sum_{n\ge1}h_n(R)|\widehat u(n)|^2\). The term \(n=1\) vanishes, proving the first boxed expansion. The first-order eigenvector formula follows from the same reduced resolvent, with phase fixed by its positive \(e_0\)-coordinate.

**3. Strict mode ordering and sharpness.** Set \(q_n=(R^n/n!)/S_n(R)\). Its reciprocal is
\[
\frac{1}{q_n}=\sum_{j=0}^{n-1}\frac{n!}{(n-j)!R^j}.
\]
Every term common to two consecutive sums strictly increases when \(n\) increases, and an additional positive term appears. Hence \(q_n\) strictly decreases, so \(h_n=1-q_n\) strictly increases. We have \(h_1=0\), \(h_2=2/(R+2)\), and \(q_n\to0\) because \(S_n\to e^R-1>0\). Parseval on the frequencies \(\pm2,\pm3,\ldots\) now yields the sharp inequality and its equality cases. A boundary deformation containing only first harmonics has zero second variation, as required by translation symmetry; in the full area-preserving shape manifold the corresponding exact translated disks are indeed maximizers.

## Verification
The companion program `check_shape_hessian.py` checks rational identities for all displayed weights over multiple exact rational areas, verifies strict ordering over a finite set of degrees, and independently computes finite-section Fock matrices using incomplete-gamma radial integration and angular quadrature. These computations compare the top spectral deficit and eigenvector response against the analytic formula for pure and mixed boundary modes. The test result at packaging was `GAUSSIAN_SHAPE_CHECKS_PASS 1035`. This finite checker is corroboration, **not** the proof for arbitrary degree or smooth boundaries. Run with `python check_shape_hessian.py` using Python, NumPy, and SciPy.

## Relationship to prior work
Nicola and Tilli (arXiv:2106.03423, first posted June 7, 2021) established that disks uniquely maximize Gaussian short-time Fourier concentration at fixed area and gave the exact disk value. The present result studies the complete **local shape curvature of the optimized operator norm** and the response of its maximizing signal, rather than proving disk optimality.

Gómez, Guerra, Ramos and Tilli (arXiv:2307.09304, first posted July 18, 2023), especially their Section 5 and Lemma 5.6, calculate a second variation of a **different variational functional**: they perturb the *signal* and allow its maximizing superlevel domain to move. Their global quantitative set-stability result gives bounds rather than the frequency-resolved second shape derivative of the leading localization eigenvalue for a prescribed boundary perturbation. The exact reciprocal gap factors \(S_n(R)^{-1}\), complete shape-Hessian mode ordering, and first-order maximizing-eigenfunction response are the specific assertions distinguished here. These could conceivably be derived by combining earlier perturbation ingredients; historical priority is not asserted absolutely.

Ramos (arXiv:2607.21590, first posted July 23, 2026) studies inverse localization domains and local disk rigidity. Its accessible abstract does not resolve whether a mode-resolved shape Hessian appears in the full manuscript; this remains a documented literature-access risk.

## Limitations
Only planar Gaussian-window localization, smooth real squared-radius perturbations, and the first eigenvalue/eigenfunction are covered. The result does not give a uniform finite-perturbation remainder, best global Fraenkel-asymmetry constant, higher eigenvalue Hessians, or non-Gaussian-window analogues. The analytic proof is self-contained given standard Bargmann unitarity and simple-eigenvalue perturbation theory. An independent mathematical audit and full priority determination have not been performed.

## References
1. F. Nicola and P. Tilli, *The Faber–Krahn inequality for the short-time Fourier transform*, arXiv:2106.03423 (2021); Inventiones Mathematicae 230 (2022), 1–30. https://arxiv.org/abs/2106.03423
2. J. Gómez, A. Guerra, J. P. G. Ramos and P. Tilli, *Stability of the Faber–Krahn inequality for the short-time Fourier transform*, arXiv:2307.09304 (2023); Inventiones Mathematicae 236 (2024), 779–836. https://arxiv.org/abs/2307.09304
3. J. P. G. Ramos, *Eigenfunctions, free boundaries, and time-frequency localization*, arXiv:2607.21590 (2026). https://arxiv.org/abs/2607.21590
4. I. Daubechies, *Time-frequency localization operators: a geometric phase space approach*, IEEE Transactions on Information Theory 34 (1988), 605–612. https://doi.org/10.1109/18.9761
