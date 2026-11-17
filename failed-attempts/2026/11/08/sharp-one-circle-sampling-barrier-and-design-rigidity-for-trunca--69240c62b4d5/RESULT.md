# Sharp one-circle sampling barrier and design rigidity for truncated Bargmann–Fock spaces

## Finding

For every integer \(n\ge2\), let \(\mathcal F_n\) be the space of entire polynomials
\[
F(z)=\sum_{k=0}^{n-1}\frac{c_kz^k}{\sqrt{k!}},\qquad \|F\|_{\mathcal F_n}^2=\sum_{k=0}^{n-1}|c_k|^2.
\]
There is exactly one squared radius minimizing the spectral condition number of *every possible single-circle measurement design*:
\[
x_n=((n-1)!)^{1/(n-1)}.
\]
The sharp minimal singular-value condition number, simultaneously for every measurement count \(m\ge n\), is
\[
K_n=\left(\max_{0\le k<n}\frac{x_n^k}{k!}\right)^{1/2}.
\]
At the minimizing radius, **all** optimal designs are precisely the positive weighted circular quadrature designs whose first \(n-1\) nonconstant angular Fourier moments vanish. For exactly \(n\) observations this forces equally weighted vertices of a rotated regular \(n\)-gon. For more observations the minimizers need not be regular polygons or equally weighted, but their angular Fourier moments must still vanish.

The barrier does not improve as the number of same-radius observations increases. More precisely, as \(n\to\infty\),
\[
K_n=e^{1/4}\exp\!\left(\frac{n-1}{2e}\right)
[2\pi(n-1)]^{(1/e-1)/4}
\left[1+O\!\left(\frac{(\log n)^2}{n}\right)\right].
\]
This exponential limitation concerns relative spectral conditioning, not absolute singular values or signal-to-noise bounds with independently prescribed observation noise.

## Assumptions and scope

Fix integers \(n\ge2\), \(m\ge n\), a squared radius \(x>0\), angles \(\theta_1,\ldots,\theta_m\in\mathbb R\), and positive weights \(a_1,\ldots,a_m>0\) satisfying \(\sum_j a_j=1\). Angles may repeat. The normalized coherent-state sampling map is
\[
(T_{x,\theta,a}F)_j
=\sqrt{a_j}\,e^{-x/2}F(\sqrt{x}\,e^{i\theta_j}).
\]
Use the coefficient Hilbert norm on \(\mathcal F_n\), Euclidean norm on the measured vector, and \(\kappa_2(T)=\sigma_{\max}(T)/\sigma_{\min}(T)\) if \(T\) has full column rank; otherwise \(\kappa_2(T)=+\infty\). The common Gaussian factor and any common scaling of the measurement weights leave the condition number unchanged. Different sampling radii, non-diagonal transformations of data, or sample-dependent noise constraints are outside the optimization domain.

**Theorem.** The global minimum over every specified admissible variable is \(K_n\). Equality occurs exactly if
\[
x=x_n,\qquad \sum_{j=1}^m a_j e^{i\ell\theta_j}=0
\quad(\ell=1,\ldots,n-1).
\]
For \(m=n\), the latter equations imply \(a_j=1/n\), and the unordered phases are \(\{e^{i\phi}e^{2\pi i j/n}:0\le j<n\}\) for one \(\phi\in\mathbb R\). For \(m>n\), the displayed moment criterion (not a uniqueness claim) is the full equality classification. The same optimum and equality classification hold if zero weights are permitted after discarding zero-weight observations, provided positive-weight support has enough points.

## Proof

**1. A design-independent lower bound.** In the monomial orthonormal basis \(z^k/\sqrt{k!}\), \(0\le k<n\), the Gram operator \(G=T^*T\) has entries
\[
G_{k\ell}=e^{-x}\frac{x^{(k+\ell)/2}}{\sqrt{k!\ell!}}
\sum_{j=1}^m a_j e^{i(\ell-k)\theta_j}.
\]
The diagonal is therefore independent of all angles and individual weights:
\[
G_{kk}=e^{-x}w_k(x),\qquad w_k(x)=x^k/k!.
\]
For a positive semidefinite matrix, the largest eigenvalue is at least its largest diagonal entry and the smallest is at most its smallest diagonal entry. Hence, including the rank-deficient case,
\[
\kappa_2(T)^2\ge R_n(x):=
\frac{\max_{0\le k<n}w_k(x)}{\min_{0\le k<n}w_k(x)}.
\]

**2. Unique radial optimum.** Put \(t=n-1\). The sequence \(w_k(x)\) is log-concave in \(k\) because \(w_{k+1}/w_k=x/(k+1)\) strictly decreases in \(k\). In particular, \(\min_k w_k=\min\{w_0,w_t\}=\min\{1,x^t/t!\}\). For \(x<x_n=(t!)^{1/t}\),
\[
R_n(x)=\max_{0\le k<t}\frac{t!}{k!}x^{k-t},
\]
a strictly decreasing function of \(x\), since each of the finitely many displayed functions is strictly decreasing. For \(x>x_n\),
\[
R_n(x)=\max_{1\le k\le t}\frac{x^k}{k!},
\]
a strictly increasing function, since each displayed function is strictly increasing. These two formulas match continuously at \(x_n\) and show it is the **unique** minimizer, with \(R_n(x_n)=\max_k x_n^k/k!\). All endpoints \(x\to0\) and \(x\to\infty\) have unbounded \(R_n\) for \(n\ge2\).

**3. Sharpness and every equality case.** If \(x=x_n\) and
\[
S_\ell:=\sum_j a_j e^{i\ell\theta_j}=0\quad(1\le\ell<n),
\]
then conjugate symmetry gives \(S_{-\ell}=0\), so all off-diagonal Gram entries vanish. Thus \(\kappa_2(T)^2=R_n(x_n)\), attaining the lower bound. Such designs exist for every \(m\ge n\): take \(a_j=1/m\) and phases at the \(m\)th roots of unity.

Conversely, suppose the global bound is attained. Strict radial uniqueness forces \(x=x_n\). The diagonal entries for \(k=0\) and \(k=t\) are then *both* the smallest diagonal value \(e^{-x_n}\). The min–max diagonal argument must have equality throughout, so \(\lambda_{\min}(G)=G_{00}\). Since the Rayleigh quotient of the coordinate unit vector \(e_0\) equals this minimum, \(e_0\) is a smallest-eigenvalue vector of \(G\). Consequently \(G_{0\ell}=0\) for all \(1\le\ell<n\), which is precisely \(S_\ell=0\). This proves necessity of every stated moment equation without any genericity assumption.

For \(m=n\), the square matrix with entries \(V_{jk}=\sqrt{a_j}e^{ik\theta_j}\), \(0\le k<n\), satisfies \(V^*V=I_n\) by these moment identities. Being square, \(V\) is unitary. Its \(j\)th row has squared norm \(na_j=1\); hence \(a_j=1/n\). Newton identities applied to \(u_j=e^{i\theta_j}\) and their zero power sums \(\sum_j u_j^\ell=0\) for \(1\le\ell<n\) show that their monic root polynomial has form \(z^n-c\) with \(|c|=1\). Its roots are exactly one rotated regular \(n\)-gon, and they are distinct. This establishes the complete square-sampling rigidity statement.

**4. Sharp high-dimensional asymptotics.** Since the mode of the finite Poisson-like sequence \(w_k(x_n)\) occurs at \(k\) nearest below \(x_n\), and \(x_n\le n-1\), Stirling's expansion gives, with \(t=n-1\),
\[
x_n=\frac{t}{e}+\frac{\log(2\pi t)}{2e}
+O\!\left(\frac{(\log t)^2}{t}\right).
\]
For \(k=\lfloor x_n\rfloor\), uniformly as \(n\to\infty\),
\[
\frac{x_n^k}{k!}=
\frac{e^{x_n}}{\sqrt{2\pi x_n}}[1+O(1/x_n)].
\]
Substituting the expansion of \(x_n\) and taking a square root gives the displayed asymptotic for \(K_n\), including the constant factor \(e^{1/4}\) and the power \((1/e-1)/4\). This argument is analytic and is not inferred from any finite experiment.

## Verification

The included `check_ring_sampling.py` constructs weighted coherent-state matrices directly and computes their singular values. It compares uniform regular-circle designs with the predicted optimum, tests other radii, perturbed and random angular sets, nonuniform positive weights, unequal-weight unions of regular polygons satisfying all Fourier-moment equations, and large-dimensional Stirling approximations. The script, with `numpy` installed, prints `FOCK_CIRCULAR_SAMPLING_CHECKS_PASS 1010` when all deterministic tests succeed. Finite singular-value checks **do not prove** the universal statements; those follow from the four steps above.

One concrete check: for \(n=3\), \(x_3=\sqrt2\), the sharp condition number is \(K_3=2^{1/4}\) for any \(m\ge3\), attained by weighted angular designs of order two. For \(n=2\), \(x_2=1\) and \(K_2=1\), including the boundary case of exact tightness.

## Relationship to prior work

The **diagonal coherent-state frame spectrum for uniformly spaced points on one circle is prior work**: Calixto, Guerrero, and Sánchez-Monreal (2011), Lemma 3.3 and equation (28), explicitly give \(N e^{-p}p^k/k!\), and their Theorem 3.2 proves reconstruction for truncated Fock states. The present statement does not claim that spectrum or the discrete Fourier reconstruction as new. Its scope is the *joint global optimum over an arbitrary number of angles, arbitrary positive observation weights, and the circle radius*, including an if-and-only-if classification and the sharp all-dimensional exponential barrier. These conclusions are not stated in the inspected 2011 theorem. The radial scalar minimax can indeed be derived from their spectrum in the regular-polygon case, but the all-design lower bound, full equality classification, and oversampling barrier require an additional comparison across nonuniform and weighted designs.

Kuian, Reichel, and Shiyanovskii (2019), especially Theorem 10, establish norm scaling for fixed-polynomial Vandermonde-like matrices at equidistant unit-circle nodes; they do not jointly optimize Gaussian factorial weights, physical circle radius, and all positive weighted angular configurations. Abreu et al. (first posted 2022) develop finite-dimensional Gaussian Gabor sampling on flat tori using a quasi-periodic Bargmann-type space; that is not the classical truncated polynomial Fock space here. Their finite Gaussian sampling framework supplies the focal harmonic-analysis context. Existing unit-circle Fourier quadrature and Vandermonde identities are fully credited.

## Limitations

The barrier applies to **one common radius**, weighted point-evaluation samples, the specific Gaussian/Fock factorial basis, and the usual spectral condition number between the coefficient Hilbert norm and Euclidean measurement norm. Sampling at multiple radii, changing the underlying Hilbert norm, restricting the coefficient class further, or allowing nonlinear/non-unitarily normalized postprocessing are not covered. For a noise model in which variance changes with the number or weighting of samples, condition number alone does not establish a noise-optimal acquisition strategy. Neither independence from all unpublished results nor independent human verification is claimed. The directly relevant 2011 coherent-state spectrum makes priority of its simple radial corollary especially delicate; the new claim is the jointly optimized weighted-angle theorem and sharp resulting barrier.

## References

1. M. Calixto, J. Guerrero, J. C. Sánchez-Monreal, *Almost Complete Coherent State Subsystems and Partial Reconstruction of Wave Functions in the Fock-Bargmann Phase-Number Representation*, arXiv:1109.2171 (first submitted September 9, 2011), §3, especially Theorem 3.2 and Lemma 3.3, https://arxiv.org/abs/1109.2171.
2. M. Kuian, L. Reichel, S. Shiyanovskii, *Optimally Conditioned Vandermonde-Like Matrices*, SIAM J. Matrix Anal. Appl. 40 (2019), 1399–1424, DOI 10.1137/19M1237272, §§4–5, https://www.math.kent.edu/~reichel/publications/optvan.pdf.
3. L. D. Abreu, P. Balazs, N. Holighaus, F. Luef, M. Speckbacher, *Time-frequency analysis on flat tori and Gabor frames in finite dimensions*, arXiv:2209.04191 (first submitted September 9, 2022), §5, https://arxiv.org/abs/2209.04191.
4. S. Kunis, D. Nagel, *On the condition number of Vandermonde matrices with pairs of nearly-colliding nodes*, arXiv:1812.08645 (first submitted December 20, 2018), https://arxiv.org/abs/1812.08645. The latter concerns off-grid collisions rather than Fock-normalized circle design.
