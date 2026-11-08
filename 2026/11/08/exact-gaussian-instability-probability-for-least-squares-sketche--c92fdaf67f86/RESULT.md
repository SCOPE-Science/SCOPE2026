# Exact Gaussian instability probability for least-squares sketched Hamiltonian reduction

## Finding

**Theorem (exact oscillator-instability probability and sharp sketch-width law).** For every pair of integers \(k\ge2\) and \(N\ge k+1\), and every real \(\gamma>0\), the positive-definite quadratic Hamiltonian and fixed ortho-symplectic two-column basis defined below have a stable exact reduced oscillator. Yet, under an independent Gaussian sketch with \(k\) rows, the least-squares-plus-symmetrization construction of Herkert–Haasdonk–Fehr [1, Section 4.1, equations (18)–(19)] creates an **exponentially unstable reduced Hamiltonian** with the exact probability

\[
 p_k(\gamma)=\frac1\pi\int_0^1
 \left(\frac{\gamma^2 c^2}{1+\gamma^2 c^2}\right)^{(k-1)/2}
 \frac{dc}{\sqrt{c(1-c)}}.
\]

This number lies strictly between zero and one for every finite admissible \(k\) and every positive \(\gamma\). It has the sharp asymptotics

\[
 p_k(\gamma)\sim\frac{\binom{2(k-1)}{k-1}}{4^{k-1}}\gamma^{k-1}
 \quad (\gamma\downarrow0,\ k\text{ fixed}),
\]

\[
 p_k(\gamma)\sim
 \sqrt{\frac{1+\gamma^2}{\pi(k-1)}}
 \left(\frac{\gamma^2}{1+\gamma^2}\right)^{(k-1)/2}
 \quad (k\to\infty,\ \gamma\text{ fixed}).
\]

In particular, symmetrization preserves canonical Hamiltonian structure, but cannot by itself guarantee bounded or elliptic reduced motion, even when the full Hamiltonian is strictly positive definite and the reduced basis is exact. The sharp exponent quantifies the finite-sketch positivity risk in this elementary coupling model.

## Assumptions and scope

Coordinates are ordered as \((q_1,\ldots,q_N,p_1,\ldots,p_N)\), with standard coordinate columns \(e_j\) and canonical matrix \(J_{2N}=\begin{pmatrix}0&I_N\\-I_N&0\end{pmatrix}\). Define

\[
 V=[e_1,e_{N+1}],\qquad
 H_\gamma=I_{2N}+\gamma(e_1e_2^{\mathsf T}+e_2e_1^{\mathsf T})+\gamma^2e_2e_2^{\mathsf T}.
\]

Then \(V^{\mathsf T}V=I_2\), \(V^{\mathsf T}J_{2N}V=J_2\), \(H_\gamma\succ0\), and \(H_r=V^{\mathsf T}H_\gamma V=I_2\). Here \(H_\gamma\succ0\) follows from the positive-definite \(q_1,q_2\) block \(\begin{pmatrix}1&\gamma\\\gamma&1+\gamma^2\end{pmatrix}\) with determinant one, with identity on its orthogonal complement.

Let \(\Theta\in\mathbb R^{k\times 2N}\) have independent \(\mathcal N(0,1/k)\) entries, independently of the fixed basis. Set \(X=\Theta V\), \(Y=\Theta H_\gamma V\), and define the *specified* reduction (exact arithmetic) by

\[
 H_{\mathrm{LS}}=(X^{\mathsf T}X)^{-1}X^{\mathsf T}Y,
 \qquad \widehat H_r=\tfrac12(H_{\mathrm{LS}}+H_{\mathrm{LS}}^{\mathsf T}).
\]

The matrix \(X\) has full column rank almost surely for \(k\ge2\). Instability means that \(J_2\widehat H_r\) has a strictly positive real eigenvalue, so some reduced solution grows exponentially. It does **not** mean that the computed reduced dynamics cease to be Hamiltonian; their quadratic energy is conserved, but the energy can be indefinite.

## Proof

**1. Algebraic reduction and the only dangerous eigenvalue.** Since \(H_\gamma V=V+\gamma e_2(1,0)\), write \(y=\Theta e_2\) and \(z=(X^{\mathsf T}X)^{-1}X^{\mathsf T}y=(z_1,z_2)^{\mathsf T}\). Then

\[
 \widehat H_r=I_2+\gamma
 \begin{pmatrix}z_1&z_2/2\\z_2/2&0\end{pmatrix},
 \qquad
 \lambda_\pm(\widehat H_r)=1+\frac\gamma2(z_1\pm\|z\|_2).
\]

The upper eigenvalue is at least one. Thus \(\widehat H_r\) is indefinite precisely when \(\gamma(\|z\|_2-z_1)/2>1\), apart from a zero-probability equality case. Every real symmetric \(2\times2\) matrix \(M\) has \(\operatorname{tr}(J_2M)=0\) and \((J_2M)^2=-\det(M)I_2\). Therefore this indefiniteness is *equivalent* to a positive real eigenvalue of \(J_2\widehat H_r\), rather than merely to failure of a sufficient stability condition.

**2. Exact Gaussian regression law.** The three columns \(\sqrt{k}\,X_1\), \(\sqrt{k}\,X_2\), and \(\sqrt{k}\,y\) are independent standard \(k\)-variate Gaussian vectors because the coordinate sets \(\{e_1,e_{N+1},e_2\}\) are distinct. Rescaling all columns cancels in \(z\). Let \(S=X^{\mathsf T}X\) after that common rescaling. It is a two-dimensional Wishart Gram matrix with density proportional to \(\det(S)^{(k-3)/2}e^{-\operatorname{tr}S/2}\) on positive-definite symmetric \(S\). Conditional on \(X\), \(z\) is centered Gaussian with covariance \(S^{-1}\). Multiplying the two densities and integrating over \(S\) gives

\[
 f_k(z)\propto\int_{S\succ0}\det(S)^{(k-2)/2}
 \exp\!\left[-\tfrac12\operatorname{tr}\bigl(S(I_2+zz^{\mathsf T})\bigr)\right]dS.
\]

For \(B=I_2+zz^{\mathsf T}\), the congruence \(T=B^{1/2}SB^{1/2}\) contributes the determinant factor \(\det(B)^{-(k-2)/2}\) and the Jacobian \(\det(B)^{-3/2}\) on the three-dimensional real symmetric-matrix space. Hence \(f_k(z)\propto\det(B)^{-(k+1)/2}=(1+\|z\|_2^2)^{-(k+1)/2}\). Polar normalization yields the exact density and radial survival law

\[
 f_k(z)=\frac{k-1}{2\pi}(1+\|z\|_2^2)^{-(k+1)/2},
 \qquad
 \Pr(\|z\|_2>t)=(1+t^2)^{-(k-1)/2}.
\]

This density proof is valid also at the minimal sketch size \(k=2\); the Gaussian Gram matrix is positive definite almost surely and its Wishart density is integrable.

**3. Integrate the unstable angular sector.** Write \(z=r(\cos\theta,\sin\theta)\). The angle is uniform on \([0,2\pi)\) and independent of \(r\). Put \(c=(1-\cos\theta)/2\). Then \(c\) has the arcsine density \([\pi\sqrt{c(1-c)}]^{-1}\) on \((0,1)\), and the instability event becomes \(\gamma r c>1\). Conditional on \(c\), Step 2 gives

\[
 \Pr(\gamma r c>1\mid c)
 =\bigl(1+(\gamma c)^{-2}\bigr)^{-(k-1)/2}
 =\left(\frac{\gamma^2c^2}{1+\gamma^2c^2}\right)^{(k-1)/2}.
\]

Integration over \(c\) is exactly the asserted formula. Its integrand is positive strictly below one almost everywhere, proving \(0<p_k(\gamma)<1\).

**4. Sharp endpoints.** Write \(\nu=k-1\). For fixed \(\nu\), divide the integral by \(\gamma^\nu\) and use dominated convergence as \(\gamma\downarrow0\); the limiting integrand is \(c^\nu\) times the arcsine density. Its integral is \(\binom{2\nu}{\nu}/4^\nu\), proving the small-coupling law.

For fixed \(\gamma\), put \(F(c)=\gamma^2c^2/(1+\gamma^2c^2)\). This is strictly increasing with \(F(1)=\gamma^2/(1+\gamma^2)\) and \((\log F)'(1)=2/(1+\gamma^2)\). The integral is dominated by its endpoint \(c=1\). Writing \(u=1-c\), the exponent has local form \(\frac\nu2\log F(1)-\nu u/(1+\gamma^2)+O(\nu u^2)\), and the arcsine density contributes \(\pi^{-1}u^{-1/2}(1+O(u))\). Endpoint Laplace integration, \(\int_0^\infty u^{-1/2}e^{-\nu u/(1+\gamma^2)}du=\sqrt{\pi(1+\gamma^2)/\nu}\), proves the large-\(k\) law with asymptotic ratio one.

## Verification

The standalone `check_science.py` reconstructs \(H_\gamma,V,J_{2N}\) and the least-squares formula, compares the exact one-dimensional probability integral with direct Gaussian-sketch experiments, checks the small- and large-parameter asymptotic ratios, and verifies the reconstructed reduced eigenvalues. Run from the package directory using `python check_science.py` with NumPy and SciPy. A successful run prints `SCIENTIFIC_CHECKS_OK`. The proof above establishes the infinite families; finite simulations only cross-check identities and do not replace the proof.

For orientation at \(\gamma=3/4\), numerical quadrature gives \(p_2\approx0.324863418\), \(p_3\approx0.151471863\), and \(p_5\approx0.041163205\).

## Relationship to prior work

Herkert–Haasdonk–Fehr [1, Section 4.1] introduced exactly the least-squares symmetrized sketched Hessian studied here, and [1, Lemma 2] established a *sufficient* subspace-embedding and perturbation condition ensuring a positive-definite reduced Hessian. Their Hamiltonian-structure claim is correct and is not contradicted: symmetry ensures canonical Hamiltonian form without ensuring positive energy. The present theorem quantifies the *exact unconditional Gaussian probability of a dynamical stability loss* on an explicit strictly positive-definite family, including its two sharp asymptotic regimes; these claims are not implications of the cited sufficient bounds.

The earlier randomized-symplectic papers [2,3] study randomized basis generation, not this sketched operator-assembly instability law. Balabanov–Nouy [4,5] developed the underlying sketching and least-squares reduced-model framework and sufficient high-probability approximation or quasi-optimality guarantees, not the exact indefinite-Hamiltonian probability for this coupled oscillator. The Wishart and arcsine distributions are standard tools, not claimed as new. Possible precedence from more general exact Gaussian-sketch cone-crossing formulas remains a limitation of the historical comparison.

## Limitations

This is an exact-arithmetic result for a fixed two-dimensional symplectic reduced space, one specific sparse, uniformly SPD full Hessian, independent Gaussian sketches, and the source method's least-squares-plus-symmetrization reconstruction. It does not give the same quantitative law for CountSketch, SRFT, correlated sketches, adaptive bases sharing sketch randomness, multiple reduced modes, or finite precision. The full and exact reduced systems remain bounded; only an event of the randomized *sketched* reduced system is unstable. The theorem does not contradict perturbation guarantees conditioned on sufficiently accurate embeddings, and it is not a general impossibility theorem for stable randomized Hamiltonian assembly.

## References

1. R. Herkert, B. Haasdonk, J. Fehr, *Randomized Symplectic Model Reduction: One-Pass Basis Construction and Sketched Hamiltonian Assembly*, arXiv:2610.39893v1, first posted 2026-10-29. https://arxiv.org/html/2610.39893v1
2. R. Herkert et al., *Error Analysis of Randomized Symplectic Model Order Reduction for Hamiltonian Systems*, arXiv:2405.10465v1, first posted 2024-05-16. https://arxiv.org/html/2405.10465v1
3. R. Herkert et al., *Randomized Symplectic Model Order Reduction for Hamiltonian Systems*, arXiv:2303.04036v1, first posted 2023-03-07. https://arxiv.org/abs/2303.04036
4. O. Balabanov, A. Nouy, *Randomized Linear Algebra for Model Reduction. Part I: Galerkin Methods and Error Estimation*, arXiv:1803.02602. https://arxiv.org/abs/1803.02602
5. O. Balabanov, A. Nouy, *Randomized Linear Algebra for Model Reduction. Part II: Minimal Residual Methods and Dictionary-Based Approximation*, arXiv:1910.14378. https://arxiv.org/abs/1910.14378
