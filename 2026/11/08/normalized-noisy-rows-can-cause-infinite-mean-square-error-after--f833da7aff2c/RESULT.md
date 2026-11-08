# Normalized noisy rows can cause infinite mean-square error after signal averaging

## Finding
Fix any \(0<a<1\). With just one observation, the first-step mean-square error is finite and exactly \(a^{-2}-1\); after averaging any integer \(N\ge2\) independent observations, the signal-averaged relaxed-greedy Kaczmarz first iterate on the explicit unit-row observation model defined below is almost surely finite and converges almost surely to the true solution as \(N\to\infty\), yet
\[
\mathbb E\|x_1^{(N)}-x_*\|_2^2=+\infty
\qquad\text{for every finite }N\ge2.
\]
The true coefficient matrix is symmetric positive definite, \(\kappa_2(A)=1/a\), and the coefficient-noise second moment is \(1-a^2\), which can be made arbitrarily small as \(a\uparrow1\). The row-selection interpolation parameter can be any \(\theta\in[0,1]\). By contrast, changing only the first-step denominator from \(\|v\|_2^2\) to \(\|v\|_2^2+1/N\) makes the resulting one-step mean-square error \(O_a(N^{-1})\). Thus bounded, unit-norm, unbiased observations and arbitrarily good conditioning do not prevent failure of the unregularized full-expectation guarantee.

## Assumptions and scope
Let \(a\in(0,1)\). Put
\[
A=\begin{pmatrix}a&0\\0&1\end{pmatrix},\qquad b=\begin{pmatrix}1\\0\end{pmatrix},\qquad x_*=(1/a,0)^\top.
\]
Independently draw \(\Theta_j\in[0,2\pi)\), \(j=1,\ldots,N\), with the strictly positive bounded density
\[
f_a(t)=\frac{1-a^2}{2\pi(1-2a\cos t+a^2)}.
\]
Write \(u_j=(\cos\Theta_j,\sin\Theta_j)^\top\) and observe
\[
A^{(j)}=\begin{pmatrix}\cos\Theta_j&\sin\Theta_j\\0&1\end{pmatrix},\qquad b^{(j)}=b,\qquad v_N=\frac1N\sum_{j=1}^Nu_j.
\]
Each observed matrix has two rows of norm exactly one, and the observations are independent across \(j\). The Fourier expansion of the Poisson kernel gives \(\mathbb Eu_j=(a,0)^\top\), hence \(\mathbb EA^{(j)}=A\), \(\mathbb Eb^{(j)}=b\), and \(\mathbb E\|A^{(j)}-A\|_F^2=1-a^2\); the right-hand-side noise vanishes. Both the observed matrices and their average are nonsingular almost surely (although uniform lower singular-value bounds do not hold).

Use the exact signal-averaging rule (average the observed row vectors, then divide the selected row update by its squared averaged norm), initialization \(x_0=0\), and any relaxed-greedy interpolation \(\theta\in[0,1]\). The claim concerns one unregularized iteration and the explicitly defined first-step ridge modification, not arbitrary future iterates or a global convergence law.

## Proof
**1. The first row must be chosen.** The averaged rows are \(v_N^\top\) and \((0,1)\); the averaged right-hand side is \((1,0)^\top\). At the initial point only the first row has nonzero residual. Its normalized squared residual is \(\|v_N\|_2^{-2}\); the second is zero. The relaxed-greedy threshold is a convex combination of the maximum normalized residual and the total residual divided by the squared Frobenius norm, hence it is positive and no larger than \(\|v_N\|_2^{-2}\). The admissible set and residual-based row lottery select row one with probability one. Almost surely \(v_N\ne0\), so
\[
x_1^{(N)}=\frac{v_N}{\|v_N\|_2^2},\qquad \|x_1^{(N)}\|_2=\|v_N\|_2^{-1}.
\]

**2. Small-ball lower bounds for every sample count.** Since \(f_a\) has a positive minimum on the circle, it suffices to show a lower bound using open angle configurations. For \(N=2\), choose the second angle within \(O(r)\) of the antipode of the first. This has probability at least \(c_{a,2}r\), and then \(\|v_2\|_2<r\), for all sufficiently small \(r>0\).

For \(N\ge3\), start from the regular-polygon configuration \(t_j^0=2\pi(j-1)/N\), so \(N^{-1}\sum_j (\cos t_j^0,\sin t_j^0)=0\). The Jacobian of the map \((t_1,t_2)\mapsto v_N\), with the other angles fixed, has determinant \(\sin(2\pi/N)/N^2\ne0\). By the inverse function theorem, there are a small fixed neighborhood of the remaining \(N-2\) angles and uniform inverse-chart neighborhoods around the origin in the \(v_N\)-plane. Because the joint angular density is bounded below on their product, integration over the preimages of a radius-\(r\) disc yields
\[
\mathbb P(\|v_N\|_2<r)\ge c_{a,N}r^2
\qquad(0<r<r_{a,N}).
\]
For every \(N\ge2\), conditional on the first \(N-1\) angles, the last continuously distributed angle can make the vector sum zero at at most one prescribed direction; therefore \(\mathbb P(v_N=0)=0\).

**3. The sharp batch-one/batch-two risk transition and almost-sure consistency.** For \(N=1\), \(\|v_1\|_2=1\), so \(x_1^{(1)}=u_1\) and
\[
\mathbb E\|x_1^{(1)}-x_*\|_2^2=1+a^{-2}-2a^{-1}\mathbb E\cos\Theta_1=a^{-2}-1<\infty.
\]
In contrast, the tail-integral identity \(\mathbb EY=\int_0^\infty\mathbb P(Y>t)\,dt\) for nonnegative random variables, with \(Y=\|v_N\|_2^{-2}\), and either lower bound from Step 2 imply \(\mathbb EY=\infty\). Whenever \(\|v_N\|_2<a/2\),
\[
\|x_1^{(N)}-x_*\|_2\ge\|v_N\|_2^{-1}-a^{-1}\ge\frac{1}{2\|v_N\|_2};
\]
its squared expectation diverges. Meanwhile the strong law of large numbers gives \(v_N\to(a,0)^\top\) almost surely; continuity of \(v\mapsto v/\|v\|_2^2\) at that nonzero vector proves \(x_1^{(N)}\to x_*\) almost surely. Finally \(\kappa_2(A)=1/a\) and \(\mathbb E\|u_j-\mathbb Eu_j\|_2^2=1-a^2\).

**4. Quantitative one-step stabilization.** Define \(T_\lambda(v)=v/(\|v\|_2^2+\lambda)\), \(\lambda=1/N\), and \(\tilde x_1^{(N)}=T_\lambda(v_N)\). On \(G=\{\|v_N-(a,0)^\top\|_2\le a/2\}\), the derivative satisfies \(\|DT_\lambda\|_{\rm op}\le4/a^2\) along the line from \((a,0)^\top\) to \(v_N\). Consequently
\[
\mathbb E\big[1_G\|T_\lambda(v_N)-T_\lambda(ae_1)\|_2^2\big]\le\frac{16(1-a^2)}{Na^4}.
\]
Coordinatewise Hoeffding and the unit coordinate bounds give \(\mathbb P(G^c)\le4e^{-Na^2/16}\). Since \(\|T_\lambda(v)\|_2\le(2\sqrt\lambda)^{-1}\) for all \(v\) and \(\|T_\lambda(ae_1)\|_2\le a^{-1}\),
\[
\mathbb E\|T_\lambda(v_N)-x_*\|_2^2
\le\frac{32(1-a^2)}{Na^4}
+8\left(\frac1{2\lambda}+\frac2{a^2}\right)e^{-Na^2/16}
+\frac{2\lambda^2}{a^6}.
\]
This is \(O_a(N^{-1})\). The modification is a standard ridge correction; no claim of priority for regularization itself is made.

## Verification
The accompanying `checks.py` verifies the exact matrix/initial-selection algebra on representative parameters, the regular-polygon Jacobian identity for multiple sample counts, and numerical quadrature of the Poisson-kernel first moment. It additionally checks the displayed deterministic upper bound and a finite-sample simulation for the ridge modification. These tests are supplementary; the inverse-function and tail-integral arguments, not Monte Carlo or bounded enumeration, establish the infinite-expectation assertion.

## Relationship to prior work
Zhang, Zeng and Zhang (2026), Algorithm 2, Assumption 4.1 and Theorem 4.1, give the averaging-before-normalization update and a mean-square bound. The construction satisfies the written unit-row, unbiased, finite-variance and consistency assumptions yet has infinite one-step full-expectation error. It separates almost-sure consistency from mean-square convergence and pinpoints why an inverse-moment/lower-row-norm condition matters.

Classical planar random-walk density and Mellin-moment theory, including Borwein, Straub, Wan and Zudilin (2011), already explains negative-moment singularities for *uniform* angular steps. Our use of a positive-mean biased angular distribution, a full-rank underlying linear system, forced relaxed-greedy selection and a matched ridge rate is the application-specific statement; the random-walk singularity alone is not presented as a new fact. Moorman and coauthors (2020) average complete Kaczmarz updates from fixed data, rather than averaging noisy rows before a single singular denominator. Goldshlager, Hu and Lin (2025) regularize randomized block Kaczmarz updates for a distinct sampled-block regime. Gan and Wu (2026) analyze different doubly-noisy Kaczmarz variants, not this exact signal-averaged, selected-row inverse-moment example. Broad historical ratio-estimator and inverse-moment principles remain relevant priority risks.

## Limitations
The infinite mean square is a statement about the *first* unregularized iterate for \(N\ge2\); the exactly finite first-step risk at \(N=1\) is part of the same sharp batch-size boundary, with strictly positive but potentially very rare near-cancellation events. Every individual iterate is finite almost surely; truncated simulations will typically miss the divergent tail. The ridge bound is for the modified first step, with a constant depending on fixed \(a\), and is not a full multi-iteration guarantee. No claim is made about noisy right-hand sides, all angular noise distributions, or general higher-dimensional matrices.

## References
- Lu Zhang, Jinchuan Zeng, Hui Zhang, *Relaxed Greedy Randomized Kaczmarz with Signal Averaging for Solving Doubly-Noisy Linear Systems*, arXiv:2603.29372 (first public 2026-03-31), https://arxiv.org/abs/2603.29372.
- Jonathan M. Borwein, Armin Straub, James Wan, Wadim Zudilin, *Densities of short uniform random walks*, arXiv:1103.2995 (2011), https://arxiv.org/abs/1103.2995.
- Jacob D. Moorman, Thomas K. Tu, Denali Molitor, Deanna Needell, *Randomized Kaczmarz with Averaging*, arXiv:2002.04126 (2020), https://arxiv.org/abs/2002.04126.
- Gil Goldshlager, Jiang Hu, Lin Lin, *Worth Their Weight: Randomized and Regularized Block Kaczmarz Algorithms without Preprocessing*, arXiv:2502.00882 (2025), https://arxiv.org/abs/2502.00882.
- Yudan Gan, Gang Wu, *On Convergence Behavior of Randomized Kaczmarz-type Methods for Solving Doubly Noisy Linear Systems*, arXiv:2608.22259 (2026), https://arxiv.org/abs/2608.22259.
