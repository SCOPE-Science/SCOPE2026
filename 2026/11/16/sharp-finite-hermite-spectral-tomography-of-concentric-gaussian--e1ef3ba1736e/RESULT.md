# Sharp finite Hermite spectral tomography of concentric Gaussian Gabor masks

## Finding
For every integer \(m\ge 1\), a phase-space observation mask consisting of at most \(m\) centered, pairwise separated annuli is uniquely determined by the first \(2m\) **Hermite-indexed** eigenvalues of its Gaussian-window short-time Fourier localization operator. This number of measurements is sharp: for every mask with exactly \(m\) nondegenerate annuli, retaining only the first \(2m-1\) Hermite-indexed eigenvalues leaves a nonconstant real-analytic one-parameter family of different masks with precisely the same measurements.

Writing the \(2m\) annulus endpoints in normalized squared radius as \(0<x_1<x_2<\cdots<x_{2m}\), the complete measurement Jacobian is a signed, exponentially weighted Vandermonde matrix and its determinant is
\[
\det D\Phi_m(\mathbf x)=(-1)^m\frac{\exp(-\sum_{i=1}^{2m}x_i)}{\prod_{j=0}^{2m-1}j!}\prod_{1\le i<k\le 2m}(x_k-x_i).
\]
Consequently the inverse is locally real analytic in the strict endpoint chamber, with an explicit first-order noise-amplification formula given below. The result concerns *labelled responses to fixed Hermite probes*, not the unordered multiset of operator eigenvalues.

## Assumptions and scope
The normalized analysis window is \(\phi(t)=2^{1/4}e^{-\pi t^2}\). For \(z=(q,p)\in\mathbb R^2\), let
\[
V_\phi f(q,p)=\int_{\mathbb R}f(t)\overline{\phi(t-q)}e^{-2\pi i pt}\,dt,
\qquad \langle L_E f,f\rangle=\int_{\Omega_E}|V_\phi f(q,p)|^2\,dq\,dp,
\]
where \(\Omega_E=\{(q,p):\pi(q^2+p^2)\in E\}\) and \(E=\bigcup_{k=1}^r[a_k,b_k]\) for an integer \(1\le r\le m\) with \(0<a_1<b_1<\cdots<a_r<b_r<\infty\). Endpoints of two masks are regarded as equal if their corresponding radial intervals coincide, not merely if their areas agree. \(L_E=V_\phi^*\mathbf1_{\Omega_E}V_\phi\) is positive, self-adjoint, and diagonal in the standard normalized Hermite basis \((h_j)_{j\ge0}\). The observations are the *indexed* values \(\lambda_j(E)=\langle L_Eh_j,h_j\rangle\), for \(j=0,1,\ldots,2m-1\).

For an exactly \(m\)-annular mask, set \(x_{2k-1}=a_k\), \(x_{2k}=b_k\), and \(\Phi_m(\mathbf x)=(\lambda_0,\dots,\lambda_{2m-1})\). The parameter chamber \(\mathcal C_m\subset\mathbb R^{2m}\) is the open set of strictly increasing positive endpoints.

## Proof
**Step 1: normalized diagonal observations.** By the standard Gaussian/Hermite short-time Fourier identity,
\[
|V_\phi h_j(q,p)|^2=e^{-\pi(q^2+p^2)}\frac{[\pi(q^2+p^2)]^j}{j!}.
\]
Polar coordinates and the substitution \(t=\pi(q^2+p^2)\) give the exact moments
\[
\lambda_j(E)=\frac1{j!}\int_E t^j e^{-t}\,dt
=\frac1{j!}\sum_{k=1}^r\int_{a_k}^{b_k}t^je^{-t}\,dt.\tag{1}
\]
In particular the weight \(e^{-t}\) is strictly positive on the nonnegative axis. Equation (1) is the known Gaussian radial-localization diagonalization, and is an input rather than an originality claim.

**Step 2: global uniqueness from \(2m\) moments.** Suppose \(E\) and \(F\) are each unions of at most \(m\) separated nondegenerate intervals and have \(\lambda_j(E)=\lambda_j(F)\) for every \(0\le j\le2m-1\). Put \(h=\mathbf1_E-\mathbf1_F\). If \(h\ne0\) on a set of positive measure, its consecutive nonzero sign-runs, disregarding intervening zero intervals, alternate in sign. There are at most \(m\) positive runs: two positive runs separated by a negative run must lie in distinct components of \(E\), because the separating negative run is outside \(E\). Similarly there are at most \(m\) negative runs, since they must lie in distinct components of \(F\). Thus the sign-run count is at most \(2m\), with at most \(2m-1\) sign changes. Choose one point between each consecutive opposite-sign run and form a real polynomial \(Q\) with simple zeros at those points, with overall sign selected so that \(Q(t)h(t)>0\) almost everywhere on the support of \(|h|\). Then \(\deg Q\le2m-1\) and
\[
0<\int_0^\infty Q(t)e^{-t}h(t)\,dt=0,
\]
where the final equality follows from (1) and the assumed equality of the first \(2m\) moments. This contradiction implies \(E=F\) up to a null set. Strictly ordered, positive, nonzero-length components then have exactly the same endpoints. In particular, comparison with masks having fewer than \(m\) components is included.

**Step 3: exact Jacobian and local stability.** For exactly \(m\) intervals, differentiating (1) with respect to the endpoints gives, for \(0\le j\le 2m-1\) and \(1\le i\le2m\),
\[
(D\Phi_m)_{j,i}=s_i\,\frac{e^{-x_i}x_i^j}{j!},\qquad s_i=(-1)^i.
\]
Here odd \(i\) are left endpoints and hence have derivative sign \(-1\). Factoring the row factorials and column exponentials from the monomial Vandermonde matrix proves the determinant displayed in the Finding; no sign or factorial factors are omitted. It never vanishes in \(\mathcal C_m\), so \(\Phi_m\) has a real-analytic local inverse at every point. If \(\ell_i(t)=\prod_{k\ne i}(t-x_k)/(x_i-x_k)=\sum_{j=0}^{2m-1}c_{i,j}t^j\) denotes the endpoint Lagrange polynomial, then the *linearized inverse* is exactly
\[
\delta x_i=s_i e^{x_i}\sum_{j=0}^{2m-1}j!\,c_{i,j}\,\delta\lambda_j.
\tag{2}
\]
Therefore \(|\delta x_i|\le e^{x_i}\sum_j j!|c_{i,j}||\delta\lambda_j|\) at first order. The Lagrange denominators explicitly display the instability as two endpoints approach collision.

**Step 4: sharp insufficiency of \(2m-1\) observations.** Delete the last row of \(D\Phi_m\). The remaining \((2m-1)\times2m\) matrix has full row rank: its submatrix on any \(2m-1\) endpoint columns is a weighted Vandermonde with distinct nodes. By the analytic submersion/implicit-function theorem, the common level set of \(\lambda_0,\ldots,\lambda_{2m-2}\) is locally a one-dimensional real-analytic manifold through every \(\mathbf x\in\mathcal C_m\). The nonzero determinant in Step 3 makes the omitted observation \(\lambda_{2m-1}\) vary nontrivially along that level set. A sufficiently short segment stays in the strictly ordered chamber and represents different nondegenerate annular masks. Thus \(2m-1\) first-indexed observations fail to identify every such mask, proving sharpness for all \(m\ge1\).

**Step 5: endpoint equations.** Integration by parts turns the observations into explicit alternating boundary moments. Set \(\lambda_{-1}=0\). Then for every \(0\le j<2m\),
\[
j!\bigl(\lambda_{j-1}-\lambda_j\bigr)
=\sum_{i=1}^{2m}s_i e^{-x_i}x_i^j.
\tag{3}
\]
Thus boundary recovery may be posed as a \(2m\)-equation nonlinear system with signed amplitudes tied to their locations, unlike unconstrained weighted-spike recovery. Global uniqueness of its solutions in the ordered endpoint chamber follows from Step 2; this statement is not a claim of a globally convergent numerical solver.

## Verification
The accompanying `check_inverse_annuli.py` independently computes moment integrals using adaptive quadrature and incomplete-gamma evaluation, and checks the analytical Jacobian determinant against a direct numerical determinant, also confirming the signed endpoint moment identity and the full Jacobian by finite differences. At 70-digit working precision it tested 16 parameter sets across \(m=1,2,3,4\), checked symbolic Vandermonde determinants for \(m=1,2\), and constructed two distinct two-annulus masks sharing the first three moments with a different fourth. Execution produced:

`INVERSE_ANNULAR_STFT_PASS moment_cases=16 symbolic_dimensions=2,4 nonidentifiability_fiber=m2_two_sides boundary_moments=checked finite_difference_jacobian=checked max_integral_error=9.05568e-72 max_det_relative_error=2.54249e-66`

Run `python3 check_inverse_annuli.py` with `mpmath` and `sympy` available. The integrals and computed examples are finite corroboration only; Steps 1–4 constitute the proof for every positive integer \(m\).

## Relationship to prior work
The Gaussian/Hermite radial localization formula (1) is classical (Daubechies, 1988) and appears explicitly in Knutsen (2019, Section 2.3), who analyzes ring and Cantor-type mask eigenvalue *bounds*. Jaming–Speckbacher (2019) investigate STFT sampling inequalities for prescribed measurable sets, not finite inverse recovery of a radial mask from labelled Hermite observations. Dewage–Ólafsson (2021) study Fock Toeplitz eigenvalue functions for quasi-radial symbols, but do not give this sharp finite-endpoint inversion. Batenkov (2009) develops moment inversion for general piecewise D-finite functions, with special attention to unknown jump locations and general unknown piecewise-constant amplitudes, but does not establish the optimal first-\(2m\) exponentially weighted Gaussian Hermite measurements for fixed binary annular masks. Vetterli–Marziliano–Blu (2002) recover finite-rate-of-innovation signals under suitable convolutional sampling; their general arbitrary-weight impulse construction does not directly imply the number of Gaussian *Hermite* moments here or the global uniqueness and minimality of the tied-sign annular endpoint problem. Ramos (2026) develops an inverse free-boundary localization theory from **prescribed eigenfunctions** and eigenvalues, a distinct data model; the explicit finite labelled-spectrum threshold for concentric annuli is not among the main results examined.

## Limitations
The observation labels \(j\) are indispensable; the unordered spectrum is not addressed. The model assumes a centered radial *binary* mask made of at most \(m\) separated positive-radius annuli. It does not include arbitrary nonradial sets, unknown graded masks, or a number of components larger than \(m\). Local inverse conditioning deteriorates when endpoints coalesce or become large; no global noise-robust algorithm, uniform condition number, or stable recovery from noisy unordered spectra is proved. The moment sign argument is a classical variation principle; novelty is assessed for the complete sharp and stable Gaussian localization inverse statement, with historical-priority uncertainty if equivalent finite-moment results have appeared under different terminology.

## References
1. P. Jaming and M. Speckbacher, *Planar sampling sets for the short-time Fourier transform*, arXiv:1906.02964 (first public version 2019-06-07), https://arxiv.org/abs/1906.02964.
2. H. Knutsen, *Daubechies' Time-Frequency Localization Operator on Cantor Type Sets*, arXiv:1907.00848 (first public version 2019-07-01), https://arxiv.org/abs/1907.00848; published in *Journal of Fourier Analysis and Applications* (2020), Section 2.3.
3. V. Dewage and G. Ólafsson, *Toeplitz operators on the Fock space with quasi-radial symbols*, arXiv:2107.01465 (first public version 2021-07-03), https://arxiv.org/abs/2107.01465.
4. M. Vetterli, P. Marziliano and T. Blu, *Sampling Signals With Finite Rate of Innovation*, *IEEE Transactions on Signal Processing* **50** (2002), 1417–1428, https://bigwww.epfl.ch/publications/vetterli0201.pdf.
5. J. P. G. Ramos, *Eigenfunctions, free boundaries, and time-frequency localization*, arXiv:2607.21590 (2026), https://arxiv.org/abs/2607.21590.
6. I. Daubechies, *Time-frequency localization operators: a geometric phase space approach*, *IEEE Transactions on Information Theory* **34** (1988), 605–612.
7. D. Batenkov, *Moment inversion problem for piecewise D-finite functions*, *Inverse Problems* **25** (2009), 105001; arXiv:0901.4665, https://arxiv.org/abs/0901.4665.
