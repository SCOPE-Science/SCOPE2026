# Sharp cubic geodesic-wave positivity and a high-harmonic Legendre cone on \(\mathbb S^2\)

## Finding
Let \(\mathbb S^2\) be the unit round two-sphere, let \(\theta(x,y)=\arccos\langle x,y\rangle\in[0,\pi]\), and let \(a>0\). Consider the real isotropic covariance candidate
\[
K_a(x,y)=e^{-a\theta(x,y)}\cos(3\theta(x,y)).
\]
Then the **exact necessary and sufficient positive-definiteness threshold** is
\[
\boxed{K_a\succeq0\ \text{on every finite subset of }\mathbb S^2\quad\Longleftrightarrow\quad a\ge2\sqrt2.}
\]
Every admissible kernel is strictly positive definite on each finite set of distinct sites. At the sharp endpoint \(a=2\sqrt2\), its constant Legendre (degree-zero) coefficient vanishes but every positive-degree coefficient is strictly positive. For larger \(a\), every Legendre coefficient is strictly positive. Thus its reproducing-kernel Hilbert space is dense in \(C(\mathbb S^2)\) exactly when \(a>2\sqrt2\).

The threshold is governed by a **sharp, independent mixed-product positivity property**: with \(P_n(1)=1\) denoting Legendre polynomials and \(T_3(t)=4t^3-3t\), for every integer \(n\ge2\), \(T_3P_n\) is a convex combination of Legendre polynomials. Conversely, \(T_3P_0\) and \(T_3P_1\) each have a negative Legendre coefficient. Consequently, multiplication by \(\cos(3\theta)\) preserves **every** continuous isotropic positive-definite kernel on \(\mathbb S^2\) whose Schoenberg expansion is supported in degrees \(n\ge2\). The excluded-degree cutoff is sharp.

## Assumptions and scope
Positive semidefiniteness means that for every finite collection \(x_1,\ldots,x_N\in\mathbb S^2\) and every complex vector \(z\in\mathbb C^N\), the Hermitian quadratic form \(\sum_{j,k}\overline{z_j}z_kK_a(x_j,x_k)\) is nonnegative. Strict positive definiteness requires the points to be distinct and the vector to be nonzero. The angle is the intrinsic geodesic angle, not Euclidean chord distance. The cone-preservation statement assumes a continuous real zonal kernel with an absolutely summable Schoenberg expansion \(F(\theta)=\sum_{n\ge2}c_nP_n(\cos\theta)\), with \(c_n\ge0\) and \(\sum c_n<\infty\); its conclusion includes the zero kernel. The damping theorem assumes real \(a>0\). No results for other sphere dimensions, other frequencies, or \(a=0\) are asserted.

## Proof
**1. A mixed Legendre/Chebyshev positive cone.** The ordinary three-term recurrence is
\[
tP_n(t)=\frac{n+1}{2n+1}P_{n+1}(t)+\frac{n}{2n+1}P_{n-1}(t).
\]
Applying it three times and subtracting three times its single application gives, for every integer \(n\ge3\),
\[
\begin{aligned}
T_3(t)P_n(t)={}&\frac{4(n+1)(n+2)(n+3)}{(2n+1)(2n+3)(2n+5)}P_{n+3}(t)\\
&+\frac{3(n+1)}{(2n-1)(2n+1)(2n+5)}P_{n+1}(t)\\
&+\frac{3n}{(2n-3)(2n+1)(2n+3)}P_{n-1}(t)\\
&+\frac{4n(n-1)(n-2)}{(2n-3)(2n-1)(2n+1)}P_{n-3}(t).
\end{aligned}
\]
All four rational coefficients are strictly positive. At \(n=2\), the same formula with its vanishing fourth term omitted is valid: the coefficients of \(P_5,P_3,P_1\) are \(16/21,1/15,6/35\). Evaluating at \(t=1\) shows that each collection of coefficients sums to one. The low-degree exceptions are
\[
T_3P_0=\frac85P_3-\frac35P_1,\qquad
T_3P_1=\frac{32}{35}P_4+\frac27P_2-\frac15P_0.
\]
Both contain a negative coefficient. Schoenberg's theorem identifies the conical hull of normalized Legendre polynomials with the isotropic positive-definite cone on \(\mathbb S^2\). Therefore the nonnegative mixed coefficients at every degree \(n\ge2\), uniform convergence from \(\sum c_n<\infty\), and the negative exceptions prove the claimed sharp high-harmonic preservation law.

**2. Positivity of the geodesic exponential's Legendre moments.** Define
\[
A_n(a)=\int_0^\pi e^{-a\theta}P_n(\cos\theta)\sin\theta\,d\theta,
\qquad n\in\mathbb Z_{\ge0}.
\]
Direct integration yields
\[
A_0(a)=\frac{1+e^{-\pi a}}{a^2+1},\qquad
A_1(a)=\frac{1-e^{-\pi a}}{a^2+4}.
\]
For completeness, set \(E_n=\int_0^\pi e^{-a\theta}P_n(\cos\theta)\,d\theta\). The derivative identity \((2n+1)P_n=P'_{n+1}-P'_{n-1}\), the Legendre differential equation, and integration by parts imply for \(n\ge1\) the two equalities
\[
a(E_{n-1}-E_{n+1})=(2n+1)A_n,\quad
a(nE_{n-1}+(n+1)E_{n+1})=(2n+1)(a^2+n(n+1))A_n.
\]
Solving gives \(E_{n+1}=(a^2+n^2)A_n/a\) and \(E_{n-1}=(a^2+(n+1)^2)A_n/a\). The endpoint case \(E_1=aA_0\) follows by integration by parts as well. Equating the two expressions for \(E_{n+1}\) at consecutive applicable indices now yields
\[
A_{n+2}(a)=\frac{a^2+n^2}{a^2+(n+3)^2}A_n(a)>0,\qquad n\ge0.
\]
Both starting moments are positive for \(a>0\), hence every moment is strictly positive. The recurrence also gives the controlled decay needed below, although absolute coefficient convergence is also a consequence of the positive-definite exponential kernel and Schoenberg's theorem.

**3. Every degree \(n\ge2\) survives cubic modulation.** Define the unnormalized moments
\[
B_n(a)=\int_0^\pi e^{-a\theta}\cos(3\theta)P_n(\cos\theta)\sin\theta\,d\theta.
\]
For \(n\ge2\), substitute the positive Legendre decomposition from Step 1: \(B_n\) is a sum of strictly positive coefficients times corresponding positive \(A_{n+3},A_{n+1},A_{n-1}\), and, when \(n\ge3\), \(A_{n-3}\). It is therefore **strictly positive for every** \(n\ge2\) and every \(a>0\). This establishes all infinitely many high-degree signs without numerical truncation.

**4. The exact low-degree obstruction.** Let \(q=e^{-\pi a}\in(0,1)\). Elementary integration yields, for each positive integer \(k\),
\[
\int_0^\pi e^{-a\theta}\sin(k\theta)\,d\theta=\frac{k(1-(-1)^kq)}{a^2+k^2}.
\]
Using \(\sin\theta\cos3\theta=(\sin4\theta-\sin2\theta)/2\) and \(\sin\theta\cos\theta\cos3\theta=(\sin5\theta-\sin\theta)/4\), we find
\[
\boxed{B_0(a)=\frac{(1-q)(a^2-8)}{(a^2+4)(a^2+16)},\qquad B_1(a)=\frac{(1+q)(a^2-5)}{(a^2+1)(a^2+25)}.}
\]
The degree-\(n\) Schoenberg coefficient has the sign of \((2n+1)B_n/2\). Thus the necessary condition \(B_0\ge0\) is exactly \(a^2\ge8\). It automatically ensures \(B_1>0\), and Step 3 supplies strict positivity at every higher degree. Schoenberg's necessary-and-sufficient criterion proves the exact threshold, including equality.

**5. Strictness and universality.** At all admissible parameters, every even and odd degree \(n\ge2\) has positive Schoenberg coefficient, so the Chen–Menegatto–Sun two-parity criterion gives strict positive definiteness on distinct finite sites. At the threshold the constant coefficient alone is zero. The uniform closure of the spherical reproducing-kernel Hilbert space cannot then contain the constant function, because all its elements have zero surface mean. Above threshold every degree has strictly positive coefficient; finite spherical harmonic sums belong to the RKHS and are uniformly dense in continuous functions on the sphere. This establishes exactly the universality assertions.

## Verification
The standalone `check.py` uses exact symbolic and rational arithmetic to derive the arbitrary-degree four-coefficient recurrence, compare exact polynomial decompositions for degrees \(0\) through \(54\), independently verify the two low-degree moment rational identities, and check both threshold branches. It reports 230 passed assertions. These finite checks are supplementary: positivity for every high harmonic follows algebraically from the symbolic recurrence and strictly positive rational coefficients, while the threshold follows from exact low-degree integrals.

## Relationship to prior work
Schoenberg's characterization and the Chen–Menegatto–Sun strictness criterion supply the spectral framework, not the evaluated cubic modulation cone or its sharp damping threshold. Ge's 2026 study develops even-dimensional spherical positive-definite harmonic theory and motivates scrutiny of the two-sphere specifically, but its main claims concern differentiability and sparse spectra rather than geodesically damped cubic waves. Kahler's nonnegative Jacobi and generalized-Chebyshev linearization theory treats products within a fixed orthogonal family; it does not state the mixed \(T_3P_n\) sign transition used here. A published two-sphere first-harmonic modulation result concerns \(e^{-a\theta}(1+b\cos\theta)\), whose two-frequency coefficient comparison does not imply the present cubic-frequency threshold. Published three-sphere damped cosine classification has the different threshold \(a^2+4\ge3m^2\) for integer wave frequency \(m\), and restriction to a two-sphere gives only a sufficient, nonsharp condition. Related double-frequency signed mixtures on two- and three-spheres involve different spectral coefficients and do not imply the cubic cone-preservation identity.

## Limitations
Only the fixed third angular harmonic and the two-sphere are classified. Neither an all-frequency rule nor an all-dimensional extension is proved. The absence of a known equivalent result in inspected sources is not proof of absolute priority; older mixed-product identities may exist. The checker alone is not an infinite proof; the high-degree positivity relies on the symbolic recurrence for every integer degree.

## References
1. Y. Ge, *Optimal differentiability of isotropic positive definite functions on even-dimensional spheres*, first arXiv version 2026-08-26, arXiv:2608.26092v1. https://arxiv.org/abs/2608.26092
2. I. J. Schoenberg, *Positive definite functions on spheres*, Duke Mathematical Journal 9 (1942), 96–108.
3. T. Gneiting, *Strictly and non-strictly positive definite functions on spheres*, Bernoulli 19 (2013), 1327–1349; first arXiv version 2011-11-30, arXiv:1111.7077v1. https://arxiv.org/abs/1111.7077
4. D. Chen, V. A. Menegatto, X. Sun, *A necessary and sufficient condition for strictly positive definite functions on spheres*, Proceedings of the American Mathematical Society 131 (2003), 2733–2740.
5. S. Kahler, *Nonnegative and Strictly Positive Linearization of Jacobi and Generalized Chebyshev Polynomials*, Constructive Approximation 54 (2021), 207–236; first arXiv version 2018-12-13, arXiv:1812.05542v1. https://arxiv.org/abs/1812.05542
6. *A two-frequency Schoenberg test for cosine-modulated geodesic exponentials on the two-sphere* (2026-10-26). https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-a-two-frequency-schoenberg-test-for-cosine-modulated-geodesic-ex--509c2a9eeeb8
7. *Sharp damping thresholds and a finite Schoenberg test for geodesic waves on the three-sphere* (2026-10-26). https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-sharp-damping-thresholds-and-a-finite-schoenberg-test-for-geodes--543d6b941b9f
8. *A two-sided positivity cone and every-mode staircase for geodesic exponentials on the three-sphere* (2026-11-16). https://github.com/published-finding corpus/2026/tree/main/2026/11/16/SCOPE-a-two-sided-positivity-cone-and-every-mode-staircase-for-geodesi--e9c1c53ae903
