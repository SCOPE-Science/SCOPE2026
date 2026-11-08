# A sharp spectral-spike crossover for Legendre-residual acceleration

## Finding

A Legendre-residual iterative method calibrated to a uniform spectral interval can lose control of a single outlying eigenvector even while its modeled spectral bulk contracts. The two effects have different sharp boundaries: absolute amplification switches at a reflected eigenvalue, whereas relative dominance has a dimension-dependent, nondegenerate chi-square critical window.

Fix real parameters \(0<a<b<c\), and set
\[
 z_0=\frac{a+b}{b-a}>1,\qquad z=\frac{2c-a-b}{b-a}>1,
 \qquad q_0=z_0+\sqrt{z_0^2-1},\quad q=z+\sqrt{z^2-1}.
\]
Write \(P_n\) for the classical Legendre polynomial with \(P_n(1)=1\). Consider the degree-\(n\) residual polynomial
\[
 \pi_n(\lambda)=\frac{P_n((a+b-2\lambda)/(b-a))}{P_n(z_0)}.
\]
For the quadratic iteration with residual \(e_n=\pi_n(H)e_0\), the following two assertions hold.

**Exact reflected-eigenvalue boundary.** On an eigendirection with eigenvalue \(c\), for every integer \(n\ge1\),
\[
 |\pi_n(c)|<1\quad(b<c<a+b),\qquad
 \pi_n(a+b)=(-1)^n,\qquad
 |\pi_n(c)|>1\quad(c>a+b).
\]
Moreover, the outlier factor decays exponentially when \(b<c<a+b\), is exactly of modulus one when \(c=a+b\), and grows exponentially when \(c>a+b\). Specifically,
\[
 |\pi_n(c)|\sim D\left(\frac q{q_0}\right)^n,
 \qquad D=\sqrt{\frac q{q_0}}
 \left(\frac{z_0^2-1}{z^2-1}\right)^{1/4}.
\]

**Sharp high-dimensional takeover window.** For each \(n\), choose an integer \(d_n\ge2\) with \(d_n/n^4\to\infty\). Let \(H_n\) be diagonal with one eigenvalue \(c\) and \(d_n-1\) midpoint-spaced eigenvalues
\[
 \lambda_{j,n}=a+(b-a)\frac{j-1/2}{d_n-1},\qquad 1\le j\le d_n-1.
\]
Initialize the error with \(d_n\) independent standard normal coordinates, and let \(R_n\) be the squared outlier-coordinate error divided by the total squared bulk-coordinate error after the degree-\(n\) iteration. Then
\[
 \boxed{\quad\frac{d_n}{q^{2n}}R_n\ \Longrightarrow\
 A(c;a,b)\,\chi_1^2,\qquad
 A(c;a,b)=\frac{q}{\pi\sqrt{z^2-1}}
 =\frac{2q^2}{\pi(q^2-1)}.\quad}
\]
Here \(\chi_1^2\) is a chi-square variable with one degree of freedom. Thus, if \(d_n/q^{2n}\to\tau\in(0,\infty)\),
\[
 R_n\Longrightarrow \frac{A(c;a,b)}{\tau}\chi_1^2,
\]
and the probability that the single outlier contributes more than half the total squared error converges to
\[
 2\bigl[1-\Phi(\sqrt{\tau/A(c;a,b)})\bigr].
\]
If \(d_n/q^{2n}\to\infty\), then \(R_n\to0\) in probability; if it tends to zero, \(R_n\to\infty\) in probability. These relative-dominance assertions hold even for \(b<c<a+b\), when the isolated outlier itself still contracts.

## Assumptions and scope

All matrices are real symmetric positive definite. The interval parameters satisfy \(0<a<b\), and the outlier is fixed at \(c>b\), independent of \(n\). The method uses the *explicit normalized shifted-Legendre residual family* defined above; no claim is made about all possible polynomial accelerators or about a different weight normalization. The initialization coordinates are independent \(N(0,1)\) variables, independent of the deterministic diagonal matrices. The empirical bulk uses the exact midpoints shown above. The dimension growth condition \(d_n/n^4\to\infty\) is a sufficient condition for the stated discretization argument, not an asserted sharp minimum dimension.

The normalized polynomial is realizable by a three-term first-order recurrence on a quadratic: since \(P_{n+1}(t)=((2n+1)tP_n(t)-nP_{n-1}(t))/(n+1)\), replacing \(t\) by \(z_0-2H/(b-a)\) gives \(e_{n+1}\) from \(e_n\), \(e_{n-1}\), and \(He_n\). All denominators \(P_n(z_0)\) are positive.

## Proof

**1. Exact outlier response.** Legendre parity gives \(P_n(-z)=(-1)^nP_n(z)\), hence
\[
 \pi_n(c)=(-1)^n\frac{P_n(z)}{P_n(z_0)}.
\]
For \(u>1\), the positive-coefficient expansion
\[
 P_n(u)=\sum_{k=0}^{n}\binom nk\binom{n+k}k
 \left(\frac{u-1}{2}\right)^k
\]
shows that \(P_n(u)\) is strictly increasing for \(n\ge1\). Since \(z=z_0\) exactly when \(c=a+b\), the three strict/equality cases follow for every finite \(n\). For fixed \(u>1\), the classical exterior Legendre asymptotic is
\[
 P_n(u)=\frac{(u+\sqrt{u^2-1})^{n+1/2}}
 {\sqrt{2\pi n}\,(u^2-1)^{1/4}}(1+o(1)).
\]
This is also obtainable directly by Laplace's method from
\(P_n(u)=\pi^{-1}\int_0^\pi(u+\sqrt{u^2-1}\cos\theta)^n\,d\theta\): the unique maximum is at \(\theta=0\), and its quadratic expansion gives the displayed constant. Division at \(u=z\) and \(u=z_0\) proves the stated exponential factor \(D\). The equality case is exact rather than asymptotic.

**2. Exact reduction of the random relative error.** Put \(M_n=d_n-1\) and \(t_{j,n}=1-2(j-1/2)/M_n\). Let \(G_0,G_1,\ldots,G_{M_n}\) denote the independent standard normal initial coordinates. Common factors of \(P_n(z_0)^{-2}\) cancel, leaving
\[
 R_n=\frac{G_0^2 P_n(z)^2}{S_n},\qquad
 S_n=\sum_{j=1}^{M_n}G_j^2P_n(t_{j,n})^2.
\]
No independence across successive values of \(n\) is required for the distributional statement.

**3. The bulk denominator concentrates.** Legendre orthogonality gives
\[
 \frac12\int_{-1}^{1}P_n(t)^2\,dt=\frac1{2n+1}.
\]
On \([-1,1]\), \(|P_n|\le1\). Markov's polynomial inequality gives \(\|P_n'\|_\infty\le n^2\); consequently \(\|(P_n^2)'\|_\infty\le2n^2\). The midpoint-rule error for the normalized integral is at most \(O(n^2/M_n)\), so
\[
 \mathbb ES_n=\frac{M_n}{2n+1}
 \left(1+O\left(\frac{n^3}{M_n}\right)\right).
\]
Gaussian fourth moments imply
\[
 \operatorname{Var}(S_n)=2\sum_{j=1}^{M_n}P_n(t_{j,n})^4
 \le2\mathbb ES_n.
\]
Under \(M_n/n^4\to\infty\), Chebyshev's inequality therefore yields
\[
 \frac{S_n}{M_n/(2n+1)}\xrightarrow{\mathbb P}1.
\]

**4. Exact asymptotic critical constant.** Squaring the exterior Legendre asymptotic at \(z\) gives
\[
 (2n+1)P_n(z)^2
 \sim\frac{q^{2n+1}}{\pi\sqrt{z^2-1}}
 =A(c;a,b)q^{2n}.
\]
Combine this with the exact ratio in Step 2 and the denominator concentration in Step 3. Slutsky's theorem proves \((d_n/q^{2n})R_n\Longrightarrow A\chi_1^2\). Scaling and continuity of the chi-square distribution yield the three regimes and the dominance probability. For the zero-ratio regime, positivity of \(\chi_1^2\) almost surely ensures divergence in probability.

## Verification

The companion \(check.py\) uses exact rational Legendre coefficient recurrences to check parity, normalization, and the reflected threshold for multiple degrees and rational parameters. It verifies \(\frac12\int_{-1}^1P_n^2=1/(2n+1)\) by exact polynomial integration; independently checks exterior constants, midpoint quadrature and finite Gaussian bulk concentration. It prints `CHECK_OK 204` on a successful run with Python 3. No finite check is used as a substitute for the limiting proof.

A reproducible example is \(a=1\), \(b=2\), \(c=2.1\): the outlier eigen-direction contracts, but \(q=1.2+\sqrt{0.44}\) determines the exponentially growing dimension required to delay its relative domination. At \(c=3\), the outlier response is exactly \((-1)^n\) at every degree; above \(3\), it amplifies.

## Relationship to prior work

Pedregosa and Scieur (2020, arXiv:2002.04756, especially §6 and §8) develop Legendre-based uniform spectral acceleration and expressly identify modeling outlier eigenvalues as a future issue. Their explicit recurrence and its spectral-density setting motivate the present polynomial; they do not derive the finite-dimensional single-spike chi-square takeover window or its sharp constant. Scieur and Pedregosa (2020, arXiv:2002.04664) prove convergence of average-case method coefficients to Polyak momentum and treat bulk asymptotics, rather than a rare direction's random relative error.

Classical Chebyshev semi-iteration and work on its sensitivity to misestimated spectral endpoints (including X. Li, 1995) cover related worst-case stability questions. The exact reflection boundary is thus interpreted as the Legendre-specific part of the joint theorem, not a claimed invention of spectral stability analysis. Classical exterior Legendre asymptotics supply an essential known lemma; the new synthesis concerns the simultaneous finite-degree reflection phenomenon and the explicit Gaussian high-dimensional critical window. The 1995 paper was available at abstract level only, so equivalent historical specializations remain a publication-precedence risk.

## Limitations

This is a result for exact arithmetic, a fixed SPD diagonal spectrum with evenly spaced bulk and exactly one outlier, Gaussian isotropic initialization, and a specified Legendre recurrence. No assertion is made for empirically estimated spectral endpoints, nonlinear objectives, adaptive/restarted methods, heavy-tailed initialization, several interacting outliers, or noisy gradients. The high-dimensional condition is sufficient, not optimal. The critical chi-square convergence is a limit theorem, not a finite-dimensional error-confidence interval. The source paper's broader use of the term “average-case optimal” is not used here as a hypothesis: the theorem depends only on its explicitly defined Legendre polynomial family. Independent specialist validation and a comprehensive historical precedence assessment have not been performed.

## References

- F. Pedregosa and D. Scieur, *Average-Case Acceleration Through Spectral Density Estimation*, arXiv:2002.04756 (first posted 2020-02-12), ICML/PMLR 119 (2020). https://arxiv.org/abs/2002.04756 ; https://proceedings.mlr.press/v119/pedregosa20a.html
- D. Scieur and F. Pedregosa, *Universal Average-Case Optimality of Polyak Momentum*, arXiv:2002.04664 (2020). https://arxiv.org/abs/2002.04664
- X. Li, *The Convergence Rate of the Chebyshev SIM Under a Perturbation of a Complex Line-Segment Spectrum*, Linear Algebra and its Applications 230 (1995), 47–60, DOI:10.1016/0024-3795(93)00361-3. https://digitalcommons.georgiasouthern.edu/math-sci-facpubs/560/
- NIST Digital Library of Mathematical Functions, §§14.15(iii), 18.15(iii), Legendre exterior/large-degree asymptotics. https://dlmf.nist.gov/14.15 ; https://dlmf.nist.gov/18.15
