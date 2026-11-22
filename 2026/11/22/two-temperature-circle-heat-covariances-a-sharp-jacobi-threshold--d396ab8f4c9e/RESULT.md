# Two-temperature circle heat covariances: a sharp Jacobi threshold, boundary universality loss, and two parity switches

## Finding
Let \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\) and, for \(t>0\), let
\[
H_t(\theta)=\sum_{n\in\mathbb Z}e^{-t n^2}e^{in\theta}.
\]
For \(t,s>0\) and real \(\varepsilon\), define the continuous, real-symmetric, nonstationary kernel
\[
K_{t,s,\varepsilon}(x,y)=H_t(x-y)+\varepsilon H_s(x-y)\cos(x+y).
\]
Positive semidefiniteness means nonnegative Gram quadratic forms on **every** finite set of circle sites, with arbitrary complex coefficients. Strict positive definiteness means positive Gram quadratic forms for nonzero coefficients at pairwise distinct sites. Universality means density of the reproducing-kernel Hilbert space in \(C(\mathbb T)\) in the uniform norm.

For \(\delta>0\), define the bounded self-adjoint tridiagonal operator on \(\ell^2(\mathbb Z)\)
\[
(J_\delta v)_n=e^{-\delta(n-1)^2}v_{n-2}+e^{-\delta(n+1)^2}v_{n+2},
\qquad \rho(\delta)=\|J_\delta\|.
\]
It is the orthogonal direct sum of even-index and odd-index Jacobi blocks \(J_{\delta,0}\) and \(J_{\delta,1}\). Write \(\rho_j(\delta)=\|J_{\delta,j}\|\) for \(j=0,1\); then \(\rho=\max(\rho_0,\rho_1)\).

**Sharp positivity law:** \(K_{t,s,\varepsilon}\) is positive semidefinite on every finite configuration if and only if
\[
\begin{cases}
\varepsilon=0,&0<s<t,\\
|\varepsilon|\le e^{-t},&s=t,\\
|\varepsilon|\le 2e^{-t}/\rho(s-t),&s>t.
\end{cases}
\]
Every admissible kernel is strictly positive definite on every finite set of distinct sites, **including the sharp boundary**. Its reproducing-kernel Hilbert space is universal for every admissible parameter except when \(s>t\) and \(|\varepsilon|=2e^{-t}/\rho(s-t)\): at this boundary there is an explicit nonzero, smooth, annihilating measure, so universality fails despite finite-site strict positive definiteness.

The function \(\rho(\delta)\) is continuous and strictly decreasing on \((0,\infty)\), with limits \(2\) at zero and \(1\) at infinity. Its maximizing parity changes at least **twice**: at the three strictly increasing parameters
\[
\delta_1=\log(24/23),\quad \delta_2=\log(12/11),\quad \delta_3=\log(5/4),
\]
one has, respectively,
\[
\rho_1(\delta_1)>\rho_0(\delta_1),\qquad
\rho_0(\delta_2)>\rho_1(\delta_2),\qquad
\rho_1(\delta_3)>\rho_0(\delta_3).
\]
Consequently at least one parity equality occurs in each open interval \((\delta_1,\delta_2)\) and \((\delta_2,\delta_3)\). No assertion is made about uniqueness or the total number of further crossings.

## Assumptions and scope
All parameters are real with \(t,s>0\), and all sums and Fourier coefficients use the standard period-\(2\pi\) convention. The heat kernel is the periodic heat kernel, **not** the periodically extended function \(e^{-t\theta^2}\). Complex finite measures are allowed in the density/universality criterion. No uniform Gram eigenvalue bound over arbitrary finite configurations is asserted at the critical parameter.

## Proof
**1. Exact normalized Fourier matrix.** Absolute convergence permits the double Fourier expansion
\[
K(x,y)=\sum_{n,m\in\mathbb Z}A_{n,m}e^{inx}e^{-imy},\qquad
A_{n,n}=e^{-tn^2},\quad A_{n,n+2}=\frac{\varepsilon}{2}e^{-s(n+1)^2},
\]
with its Hermitian transpose and all other entries zero. Put \(D_{n,n}=e^{-tn^2/2}\). On finitely supported sequences the congruence \(A=DBD\) has
\[
B=I+\frac{\varepsilon e^t}{2}J_{s-t},
\]
using the same distance-two formula for \(J_\delta\) when \(\delta\le0\), interpreted on finite sequences. Nonnegativity of all finite Gram matrices is equivalent to nonnegativity of all finite Fourier-matrix quadratic forms: one direction uses Riemann sums of the continuous kernel against trigonometric-polynomial densities; the other uses absolute convergence and finite Fourier truncation of each finite atomic Gram quadratic form.

For \(s<t\), the two-by-two minor on Fourier indices \(n-1,n+1\) has normalized offdiagonal modulus \(|\varepsilon|e^t e^{(t-s)n^2}/2\), which exceeds one for large \(|n|\) whenever \(\varepsilon\ne0\). Thus only \(\varepsilon=0\) is admissible. For \(s=t\), each parity block of \(J_0\) is the two-sided free nearest-neighbor adjacency operator, with spectrum \([-2,2]\); hence the cutoff is \(|\varepsilon|\le e^{-t}\). For \(s>t\), \(J_\delta\) is compact because the sum of its squared edge weights is finite, and conjugation by alternating signs on each parity block sends \(J_\delta\) to \(-J_\delta\). Consequently its spectral extremes are \(\pm\rho(\delta)\), proving the third cutoff. The operator's finite truncations approach it in norm, so these are also necessary and sufficient conditions on finite Fourier tests.

**2. Strictness and the change in universality.** For a nonzero finite complex Borel measure \(\mu\), set \(c_n=\int e^{-inx}\,d\mu(x)\) and \(u_n=e^{-tn^2/2}c_n\). These define a nonzero vector \(u\in\ell^2(\mathbb Z)\) by Fourier uniqueness. Its kernel energy is \(\langle u,Bu\rangle\); this identity follows by the absolutely convergent series and the simultaneous index-reversal symmetry of the coefficient matrix. In the strictly subcritical region, \(B\) is bounded below by a positive multiple of the identity, so the energy is positive for every nonzero \(\mu\), implying universality by the Riesz representation theorem and Hahn–Banach. At \(s=t\) and the critical parameter, \(B\) has no nonzero \(\ell^2\) nullvector: the Fourier transform of the free adjacency block is multiplication by \(2\cos\xi\), and its extremal spectral values occur only at isolated points of the frequency circle. The same strict positive energy therefore holds for all nonzero finite measures at the equal-time boundary.

For \(s>t\), take a nullvector \(v\ne0\) of \(B\) at the critical coefficient. It is an eigenvector of \(J_\delta\) with nonzero eigenvalue \(\pm\rho(\delta)\). Iterating its nearest-neighbor recurrence \(m\) times shows, for every fixed positive integer \(m\) and all sufficiently large \(|n|\),
\[
|v_n|\le \left(\frac{2}{\rho(\delta)}\right)^m
\|v\|_\infty\exp\{-m\delta(|n|-2m)^2\}.
\]
Indeed every length-\(m\) path has at most \(2^m\) choices and its edge centers stay within \(2m\) of the starting index. Choose \(m\delta>t/2\). Then \(b_n=e^{tn^2/2}v_n\) decays Gaussian-fast and belongs to \(\ell^1\), in fact to every polynomially weighted \(\ell^1\). Thus \((b_n)\) are the Fourier coefficients of a nonzero smooth complex density \(f\) on \(\mathbb T\), whose associated finite measure \(\mu\) has \(u=v\). Its kernel energy is zero and the kernel is not universal.

Nevertheless, for a finite atomic \(\mu=\sum_{j=1}^r z_j\delta_{x_j}\) with distinct sites and nonzero coefficient vector, a critical zero energy would again force \(u\in\ker B\); the displayed bound would imply \(c_n=e^{tn^2/2}u_n\to0\). This is impossible, since the elementary Cesàro orthogonality formula gives
\[
\lim_{N\to\infty}\frac1{2N+1}\sum_{n=-N}^N|c_n|^2=\sum_{j=1}^r|z_j|^2>0.
\]
Hence every admissible boundary kernel remains strictly positive definite on distinct finite site sets. The case \(\varepsilon=0\) is strictly positive and universal because every heat Fourier coefficient is positive.

**3. Spectral monotonicity and endpoint limits.** For \(\delta>0\), \(J_{\delta,j}\) is a compact irreducible Jacobi operator with strictly positive offdiagonal entries. Its positive top eigenvalue is simple and has a strictly positive eigenvector; analytic perturbation and the Hellmann–Feynman identity show its derivative is strictly negative because at least one edge has nonzero center. The maximum of these two strictly decreasing branches is strictly decreasing. Operator-norm continuity holds locally in \(\delta>0\). Comparison with arbitrarily long blocks of the free adjacency operator proves \(\rho(\delta)\to2\) as \(\delta\downarrow0\), while uniform edge-weight comparison yields \(J_{\delta,1}\to\begin{psmallmatrix}0&1\\1&0\end{psmallmatrix}\) plus zeros and \(J_{\delta,0}\to0\) in norm as \(\delta\to\infty\), proving \(\rho\to1\).

**4. Rigorous parity certificates.** At \(\delta=\log(a/b)\), every Jacobi edge is the rational number \((b/a)^{k^2}\). Restrict the even block to \(n=-L,-L+2,\ldots,L\) and the odd block to \(n=-(L-1),-(L-3),\ldots,L-1\). For either finite nonnegative irreducible Jacobi matrix \(J_L\), any strictly positive rational vector \(v\) gives exact Collatz bounds
\[
\min_i(J_Lv)_i/v_i\le\rho(J_L)\le\max_i(J_Lv)_i/v_i.
\]
The difference between the infinite block and its zero-padded finite truncation has norm at most \(2(b/a)^{(L+1)^2}\) for the even block and \(2(b/a)^{L^2}\) for the odd block, by the maximum absolute row sum. The standalone script `check_two_time_heat.py` constructs rational positive test vectors by high-precision decimal iteration and *then verifies all comparisons exactly with integer fractions*. It verifies the following deliberately coarse strict rational enclosures:

| \((a,b,L)\) | Winning block lower bound | Losing block upper bound |
|---|---|---|
| \((24,23,24)\) | odd \(>1.5254155\) | even \(<1.5254140\) |
| \((12,11,14)\) | even \(>1.3750732\) | odd \(<1.3748651\) |
| \((5,4,10)\) | odd \(>1.1464312\) | even \(<1.1393045\) |

The upper bounds already include the infinite-tail errors. Each row is an exact finite arithmetic certificate, not a floating-point eigenvalue experiment. Continuity and the alternating strict inequalities imply at least two distinct parity crossings.

## Verification
Run `python3 check_two_time_heat.py` using only the Python standard library. It prints the rationally certified finite spectral intervals, the explicit tail bounds and three strict parity comparisons, ending with `Three rational certificates verified; continuity forces at least two parity switches.` The checker uses high-precision decimal arithmetic only to *propose* test vectors; all accepted inequalities are verified using exact `fractions.Fraction` arithmetic, so inaccurate approximate eigenvectors would cause a failing assertion. The infinite phase diagram, strict finite-site positivity and universality distinctions are proved analytically, not inferred from finite computations.

## Relationship to prior work
Buhmann and Jäger's 2021 arXiv preprint, later published in the *Journal of Fourier Analysis and Applications* (2022), studies strict positive definiteness of nonradial kernels through spherical harmonic coefficient blocks, including a section on the circle. Their circle convolutional blocks couple opposite equal-degree harmonics rather than the neighboring same-parity Fourier modes used here, and they do not compute this two-time heat-perturbation cone or its parity-switching branches. The publicly available finding *Exact Fejér–Riesz positivity and universal criticality for sum-modulated circle heat kernels* gives a full polynomial criterion for **a common heat time**. Its all-boundary universality does not imply the present cross-time boundary result; the new loss of universality is precisely caused by decay of the offdiagonal multiplier relative to the diagonal heat spectrum. The published stationary quadratic heat modulation result concerns \(\cos(j(x-y))\) rather than \(\cos(x+y)\), and therefore has diagonal Fourier structure. General harmonizable covariance spectral theory explains the matrix representation but does not determine these thresholds or the three certified parity comparisons.

## Limitations
The spectral radius \(\rho(\delta)\) is characterized as a compact Jacobi norm with explicit convergent finite truncations; no elementary closed form is claimed. The theorem proves at least two parity changes, not exactly two or an infinite family. It does not establish uniform numerical conditioning of finite Gram matrices at criticality. Earlier equivalent results in spectral Jacobi or nonstationary covariance literature may exist; independent verification and definitive priority assessment have not been performed.

## References
1. M. Buhmann and J. Jäger, *Strict positive definiteness of convolutional and axially symmetric kernels on d-dimensional spheres*, arXiv:2105.02586, first public 6 May 2021; journal version *J. Fourier Anal. Appl.* **28** (2022), article 40. https://arxiv.org/abs/2105.02586 ; https://doi.org/10.1007/s00041-022-09913-x.
2. *Exact Fejér–Riesz positivity and universal criticality for sum-modulated circle heat kernels*, published mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/16/SCOPE-exact-fej-r-riesz-positivity-and-universal-criticality-for-sum-m--e633380c7a14.
3. *A countably faceted positivity frontier for quadratically modulated circle heat kernels*, published mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/16/SCOPE-a-countably-faceted-positivity-frontier-for-quadratically-modula--c564b7bcf603.
4. A. Jawaid, A. Karatas and J. Seewig, *Regular Fourier Features for Nonstationary Gaussian Processes*, arXiv:2602.23006 (first public 26 February 2026). https://arxiv.org/html/2602.23006.
