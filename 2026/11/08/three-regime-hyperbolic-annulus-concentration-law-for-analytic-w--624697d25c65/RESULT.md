# Three-regime hyperbolic-annulus concentration law for analytic wavelets

## Finding
Let \(\rho>0\), and let \(A^2_{\rho-1}(\mathbb D)\) be the weighted analytic Bergman space of the unit disk. For \(U>1\) and \(H>0\) consider the **hyperbolic-width annulus**
\[
\Omega_{U,H}=\{z:1-1/U<|z|^2<1-1/(U+H)\},
\]
and its positive Bergman localization operator \(T_{U,H}=P_{\rho-1}M_{1_{\Omega_{U,H}}}\) restricted to the analytic Bergman space. Its operator norm is the best fraction of normalized analytic energy capturable in this annulus. Let \(H=H(U)>0\) vary freely as \(U\to\infty\), and put \(\theta_U=H(U)/U\).

The sharp norm has the following **three-regime boundary law**:

**Thin hyperbolic-width regime:** If \(\theta_U\to0\), then
\[
\boxed{\frac{U}{H(U)}\|T_{U,H(U)}\|\longrightarrow
\frac{\rho^\rho e^{-\rho}}{\Gamma(\rho)}.}
\]
This remains true when \(H(U)\to\infty\), provided \(H(U)=o(U)\).

**Critical-width regime:** If \(\theta_U\to\theta\in(0,\infty)\), define
\[
\kappa_\theta=\rho\frac{(1+\theta)\log(1+\theta)}{\theta}.
\]
Then the optimal fraction converges to the nontrivial gamma interval mass
\[
\boxed{\|T_{U,H(U)}\|\longrightarrow
\frac{1}{\Gamma(\rho)}\int_{\kappa_\theta/(1+\theta)}^{\kappa_\theta}
 t^{\rho-1}e^{-t}\,dt\in(0,1).}
\]

**Wide hyperbolic-width regime:** If \(\theta_U\to\infty\), then
\[
\boxed{\|T_{U,H(U)}\|\longrightarrow1.}
\]
In particular, a radial window can escape to the boundary yet capture asymptotically all energy of an optimally chosen high-degree analytic mode when its hyperbolic width grows faster than its inner-boundary distance scale.

For every regime, a maximizing monomial degree \(n_U\) satisfies
\[
\frac{n_U}{U}\sim
\rho\frac{(1+\theta_U)\log(1+\theta_U)}{\theta_U}.
\]
The exact finite-\(U\) index is governed by the previously known radial beta-eigenvalue difference formula; **the new claim is the complete joint-scaling three-regime norm law**, not the exact finite-index staircase alone.

Under the analytic wavelet-to-Bergman isometry of Ramos and Tilli, the weighted exponent \(\rho-1\) corresponds to their analytic wavelet parameter \(\alpha=\rho/2>0\); maximizing monomials correspond to Laguerre wavelet modes. Thus this law is also a sharp concentration phase diagram for centered pseudohyperbolic wavelet annuli.

## Assumptions and scope
All measures are the standard weighted Bergman area measure, normalized or not (ratios are invariant under an overall constant). Each \(U>1\) and \(H(U)>0\) defines a proper annulus; there are no other assumptions on the growth or regularity of \(H(U)\). The limits are sequential along arbitrary positive sequences satisfying the stated ratio condition. \(\rho\) is fixed. No claim is made for nonradial masks, shifted centers without conjugation, or windows outside the analytic wavelet family.

## Proof
**1. Exact eigenvalue representation and optimizer.** Angular orthogonality diagonalizes the annular compression on normalized monomials. Its eigenvalues are
\[
\lambda_n(U,H)=\frac{\int_{1-1/U}^{1-1/(U+H)}t^n(1-t)^{\rho-1}\,dt}{B(n+1,\rho)},\qquad n\ge0.
\]
They tend to zero as \(n\to\infty\) at fixed \(U,H\), so the norm is their maximum. The elementary beta boundary recurrence, already used in earlier fixed-area annulus spectral work, is
\[
\lambda_{n+1}-\lambda_n=
\frac{a^{n+1}(1-a)^\rho-b^{n+1}(1-b)^\rho}{(n+1)B(n+1,\rho)},
\quad a=1-1/U,\ b=1-1/(U+H).
\]
Thus the maximizing index (or either of two tied consecutive indices) differs by at most one from
\[
\tau_{U,H}=\rho\frac{\log(1+H/U)}{\log(1+H/((U+H)(U-1)))}.
\]
This step supplies the known exact mode selection as an input; it is not by itself the novelty claim.

**2. Scaling of the maximizing index.** Set \(\theta_U=H/U\). Since \(0<\theta_U/(1+\theta_U)<1\), uniformly in its value,
\[
\log\left(1+\frac{\theta_U}{(1+\theta_U)(U-1)}\right)
=\frac{\theta_U}{U(1+\theta_U)}(1+O(U^{-1})).
\]
Hence \(\tau_{U,H}/U=\rho(1+\theta_U)\log(1+\theta_U)/\theta_U\,(1+O(U^{-1}))\). Rounding by at most one proves the stated equivalent degree scale. This tends to \(\rho\) in the thin regime, to \(\kappa_\theta\) at fixed positive width ratio, and to infinity in the wide regime.

**3. Gamma-coordinate probability.** Let \(X_U\sim\operatorname{Beta}(n_U+1,\rho)\) and \(Y_U=U(1-X_U)\). Then
\[
\|T_{U,H}\|=\mathbb P\left(\frac{1}{1+\theta_U}<Y_U<1\right).
\]
The density is explicitly
\[
 p_U(y)=\frac{y^{\rho-1}(1-y/U)^{n_U}}{U^\rho B(n_U+1,\rho)},\quad 0<y<U.
\]
Its normalization satisfies \([U^\rho B(n_U+1,\rho)]^{-1}\sim(n_U/U)^\rho/\Gamma(\rho)\) whenever \(n_U\to\infty\). For \(n_U/U\to c\in(0,\infty)\), the density converges uniformly on compact subsets of \((0,\infty)\) to \(c^\rho y^{\rho-1}e^{-cy}/\Gamma(\rho)\). This also follows from the beta--gamma representation \(X_U=Z_U/(Z_U+V)\) for independent \(Z_U\sim\operatorname{Gamma}(n_U+1,1)\), \(V\sim\operatorname{Gamma}(\rho,1)\).

**4. Thin and critical regimes.** If \(\theta_U\to0\), the interval \((1/(1+\theta_U),1)\) has length \(\theta_U/(1+\theta_U)\sim\theta_U\), and the preceding density convergence is uniform near \(y=1\) with \(c=\rho\). The probability is therefore asymptotic to \(\theta_U\rho^\rho e^{-\rho}/\Gamma(\rho)\). If \(\theta_U\to\theta>0\), the limiting gamma density has rate \(\kappa_\theta\); integrating it over \((1/(1+\theta),1)\), then changing variable \(t=\kappa_\theta y\), gives the critical formula.

**5. Wide regime.** If \(\theta_U\to\infty\), let \(c_U=n_U/U\sim\rho\log(1+\theta_U)\to\infty\). The gamma representation yields \(c_UY_U= n_U V/(Z_U+V)\Rightarrow V\), where \(V\) has the fixed \(\operatorname{Gamma}(\rho,1)\) law. The rescaled observation interval is \((c_U/(1+\theta_U),c_U)\), whose lower endpoint tends to zero and upper endpoint to infinity. Therefore its probability tends to one, proving the wide-regime conclusion.

**6. Wavelet transfer.** The unitary map of Ramos--Tilli transforms the analytic-wavelet energy quotient for the centered pseudohyperbolic annulus into the Bergman quotient of exponent \(2\alpha-1\), and maps Laguerre wavelet modes into monomials. Thus the operator norms and optimizing modes above transfer with \(\rho=2\alpha\).

## Verification
The self-contained Python-standard-library program `check.py` verifies the exact beta gap and maximizing index across multiple annuli, including finite-width ties, and checks the gamma critical-width limit numerically. The proofs of all three asymptotic regimes are analytic and do not depend on finite tests. Run `python check.py`.

## Relationship to prior work
Ramos and Tilli (first public May 16, 2022) establish the analytic wavelet/Bergman unitary correspondence and prove global disk extremality. Abreu and Dörfler (2012), Proposition 1, give monomial diagonalization for radial wavelet-localization operators. Previously known fixed-hyperbolic-area annulus calculations supply the exact beta mode staircase and the special \(H\) fixed vanishing law. The present three-regime result instead allows **arbitrary joint growth** \(H=H(U)\), obtains a positive critical-width gamma mass when \(H/U\) tends to a nonzero constant, and proves a wide-width concentration limit of one. The earlier fixed-\(H\) asymptotic does not give these two latter regimes, and no such general regime theorem was located in the examined primary literature or relevant searches. Potential equivalent radial Toeplitz probability statements remain a priority risk.

## Limitations
The finite-index staircase and beta recurrence are prior mathematical ingredients and are not claimed as original. The claimed new content is the entire joint-scaling norm phase diagram and its wavelet interpretation. The result does not give a uniform error rate as \(H/U\) approaches zero or infinity, nor other window shapes. Historical priority is provisional; a wider parameter-uniform beta-distribution result in the literature could imply it. There has been no independent mathematical audit.

## References
1. J. P. G. Ramos and P. Tilli, “A Faber--Krahn inequality for wavelet transforms,” arXiv:2205.07998, first submitted 2022-05-16, Bulletin of the London Mathematical Society 55 (2023), 2018--2034. https://arxiv.org/abs/2205.07998
2. L. D. Abreu and M. Dörfler, “An inverse problem for localization operators,” arXiv:1202.5841 (2012), Inverse Problems 28 (2012), 115001. https://arxiv.org/abs/1202.5841
3. D. Suárez, “The eigenvalues of limits of radial Toeplitz operators,” arXiv:0710.0797 (2007), Bulletin of the London Mathematical Society 40 (2008), 631--641. https://arxiv.org/abs/0710.0797
