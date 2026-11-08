# A sharp trace–anisotropy phase law for orthogonal Gaussian sliced quadrature

## Finding

For fixed symmetric real \(2\times2\) matrices \(B,C\), consider the centered Gaussian laws
\[
\mu_\varepsilon=N(0,I+\varepsilon B),\qquad
\nu_\varepsilon=N(0,I+\varepsilon C),
\]
with \(\varepsilon\) sufficiently close to zero that both covariances are positive definite. Let \(U=(\cos\Theta,\sin\Theta)\), where \(\Theta\) is uniform on \([0,2\pi)\), and let \(J\) denote a quarter-turn. Write
\[
G_\varepsilon(u)=W_2^2(u_\#\mu_\varepsilon,u_\#\nu_\varepsilon),
\qquad S_\varepsilon=\mathbb E G_\varepsilon(U).
\]
Here \(S_\varepsilon\) is the **squared** sliced \(2\)-Wasserstein distance. Compare two unbiased two-direction estimators of this quantity:
\[
Q_{\mathrm{ort}}=\tfrac12[G_\varepsilon(U)+G_\varepsilon(JU)],\qquad
Q_{\mathrm{iid}}=\tfrac12[G_\varepsilon(U)+G_\varepsilon(V)],
\]
where \(V\) is independent uniform on the circle. For \(D=B-C\), set
\[
m=\frac{D_{11}+D_{22}}2,\qquad
r=\sqrt{\left(\frac{D_{11}-D_{22}}2\right)^2+D_{12}^2}.
\]

**Sharp local classification.** If \(r>0\), then, as \(\varepsilon\to0\) through nonzero values,
\[
\begin{aligned}
\operatorname{Var}(Q_{\mathrm{ort}})&=\frac{\varepsilon^4r^4}{128}+O(\varepsilon^5),\\
\operatorname{Var}(Q_{\mathrm{iid}})&=\frac{\varepsilon^4r^2(r^2+16m^2)}{256}+O(\varepsilon^5),\\
\frac{\operatorname{Var}(Q_{\mathrm{ort}})}{\operatorname{Var}(Q_{\mathrm{iid}})}
&\longrightarrow\frac{2r^2}{r^2+16m^2}.
\end{aligned}
\]
Consequently, for each such fixed pair \(B,C\) and all sufficiently small nonzero \(\varepsilon\), orthogonal sampling has **greater** variance if \(r>4|m|\), and **smaller** variance if \(0<r<4|m|\). On the boundary \(r=4|m|>0\), the limiting ratio equals one; higher-order terms, not the leading-order criterion, determine its finite-\(\varepsilon\) ordering.

**Exact nonperturbative extremizers.** For any positive \(a\ne b\), put
\[
\mu=N(0,\operatorname{diag}(a,b)),\qquad
\nu=N(0,\operatorname{diag}(b,a)).
\]
Then \(G(Ju)=G(u)\) for every unit vector \(u\), and \(G(U)\) is nonconstant. Thus
\[
\boxed{\operatorname{Var}(Q_{\mathrm{ort}})=2\operatorname{Var}(Q_{\mathrm{iid}})>0.}
\]
The factor two is the maximum variance inflation possible for the mean of two identically distributed summands, so this entire natural Gaussian family attains the universal upper bound exactly.

## Assumptions and scope

The comparison concerns **population** projected squared Wasserstein costs, with randomness solely in the two projection directions. The two centered Gaussian distributions are on \(\mathbb R^2\); their covariances share the identity base and have fixed symmetric perturbations. \(r>0\) excludes a scalar leading covariance difference, whose variance starts at a different order. The estimand is \(\mathrm{SW}_2^2\), not its square root. The limiting statement has quantifiers: for each fixed \(B,C\) with \(r>0\), there is a sufficiently small positive radius of admissible \(|\varepsilon|\), and strict variance comparisons apply away from \(r=4|m|\). No uniform radius over unbounded matrix families is asserted.

## Proof

**1. Projected Gaussian cost and its uniform expansion.** Every one-dimensional projection of \(N(0,\Sigma)\) is centered normal with standard deviation \(\sqrt{u^\top\Sigma u}\). The exact one-dimensional quadratic Wasserstein cost therefore is
\[
G_\varepsilon(u)=\left(\sqrt{1+\varepsilon u^\top Bu}
-\sqrt{1+\varepsilon u^\top Cu}\right)^2.
\]
Since \(B,C\) are fixed and the circle is compact, Taylor expansion of both square roots has a remainder uniform in \(u\); thus
\[
G_\varepsilon(u)=\frac{\varepsilon^2}{4}(u^\top Du)^2+O(\varepsilon^3)
\]
uniformly. The same bound in \(L^2\), together with boundedness of the leading term, makes all resulting variance remainders \(O(\varepsilon^5)\).

**2. Harmonic decomposition.** A real symmetric \(2\times2\) matrix admits a rotated angular coordinate \(\phi=2\Theta-\alpha\) for which
\[
U^\top DU=m+r\cos\phi.
\]
Under a quarter-turn \(J\), \(\cos\phi\) changes sign. Writing \(c=\cos\phi\), the leading integrand is
\[
\frac{\varepsilon^2}{4}\left(m^2+2mr c+r^2c^2\right),
\]
and the leading mean is \(\varepsilon^2(m^2+r^2/2)/4\). The centered leading terms of a single direction and of the orthogonal-pair average are respectively
\[
\frac{\varepsilon^2}{4}\left(2mr c+r^2(c^2-\tfrac12)\right),
\qquad
\frac{\varepsilon^2r^2}{4}(c^2-\tfrac12).
\]

**3. Variance and sharp sign.** A uniform phase satisfies
\[
\mathbb E c=\mathbb E c^3=0,\quad
\mathbb E c^2=\tfrac12,\quad
\mathbb E c^4=\tfrac38.
\]
Hence \(\operatorname{Var}(c^2)=1/8\) and \(\operatorname{Cov}(c,c^2)=0\). Therefore
\[
\operatorname{Var}(G_\varepsilon(U))
=\frac{\varepsilon^4}{128}\left(16m^2r^2+r^4\right)+O(\varepsilon^5),
\]
\[
\operatorname{Var}(Q_{\mathrm{ort}})
=\frac{\varepsilon^4r^4}{128}+O(\varepsilon^5).
\]
Independence gives \(\operatorname{Var}(Q_{\mathrm{iid}})=\operatorname{Var}(G_\varepsilon(U))/2\). Since \(r>0\), the leading independent-sampling variance is positive, giving the displayed limiting ratio. Subtraction has leading coefficient
\[
\operatorname{Var}(Q_{\mathrm{ort}})-\operatorname{Var}(Q_{\mathrm{iid}})
=\frac{\varepsilon^4r^2(r^2-16m^2)}{256}+O(\varepsilon^5),
\]
which proves the two strict regions for sufficiently small nonzero \(\varepsilon\).

**4. Exact factor-two family.** With \(\Sigma_1=\operatorname{diag}(a,b)\) and \(\Sigma_2=\operatorname{diag}(b,a)\), replacing \(u\) by \(Ju\) swaps \(u^\top\Sigma_1u\) and \(u^\top\Sigma_2u\). Squaring the standard-deviation difference is invariant under this swap. At an axial direction \(G=(\sqrt a-\sqrt b)^2>0\), while at a diagonal direction \(G=0\), so \(\operatorname{Var}(G(U))>0\). The orthogonal-pair mean equals \(G(U)\) pointwise, while independent averaging halves its variance. Finally, Cauchy–Schwarz gives \(\operatorname{Var}[(X+Y)/2]\le\operatorname{Var}(X)\) whenever \(X,Y\) share a distribution, establishing universal sharpness of the factor two.

## Verification

The dependency-free `verify.py` evaluates exact rational identities for the leading variance coefficients over a family of rational parameter choices. It also checks the nonlinear projected Gaussian cost on equally spaced angular samples, both near the isotropic limit and for the exactly symmetric, swapped-axis Gaussian pair. Running `python verify.py` produced the saved `verification-output.txt`: 1,471 deterministic checks passed. These checks supplement, rather than replace, the uniform Taylor expansion and the analytic angular-moment proof. No numerical quadrature result is asserted to prove the all-parameter theorem.

## Relationship to prior work

Rowland et al., *Orthogonal Estimation of Wasserstein Distances* (2019), introduced orthogonal estimation and already proved that it need not improve sliced-Wasserstein estimation, using a finite-support comparison; a general counterexample is therefore **not** new here. The present result identifies an explicit sharp local criterion for the variance ordering across all non-scalar planar Gaussian covariance differences and an exact Gaussian family reaching the maximal inflation factor two. Nguyen and Ho's *Sliced Wasserstein Estimation with Control Variates* (2023) uses the one-dimensional Gaussian transport formula to design control variates, rather than deriving an orthogonal-frame covariance phase boundary. Nguyen, Ren and Ho (2023) analyze Markov-dependent projection schemes and their Monte Carlo error, without the stated Gaussian near-isotropic frontier. Nadjahi et al. (2021) study a deterministic high-dimensional Gaussian-projection approximation, a different regime. These are statement-level comparisons, not an assertion that all specialist literature has been exhaustively ruled out.

## Limitations

This is a local perturbation theorem in two dimensions, not a finite-perturbation sign classification for arbitrary Gaussian covariance pairs. At the transition \(r=4|m|\), the first nonzero sign can depend on higher perturbation terms; when \(r=0\), the leading variance formula vanishes and the theorem deliberately gives no ratio. The exactly swapped-axis family is global but is only one covariance subfamily. Data-sampling fluctuations, fitted covariance estimates, nonlinear sliced distances obtained by taking square roots, higher dimensions, and other projection-coupling designs are not covered. The maximal factor two itself follows from a general variance inequality; the content is its Gaussian attainment and the sharp local trace–anisotropy phase law.

## References

1. M. Rowland, J. Hron, Y. Tang, K. Choromanski, T. Sarlos, and A. Weller, *Orthogonal Estimation of Wasserstein Distances*, arXiv:1903.03784 (first submitted 2019-03-09). https://arxiv.org/abs/1903.03784
2. K. Nguyen and N. Ho, *Sliced Wasserstein Estimation with Control Variates*, arXiv:2305.00402 (first submitted 2023-04-30). https://arxiv.org/abs/2305.00402
3. K. Nguyen, T. Ren, and N. Ho, *Markovian Sliced Wasserstein Distances: Beyond Independent Projections*, arXiv:2301.03749 (first submitted 2023-01-10). https://arxiv.org/abs/2301.03749
4. K. Nadjahi, A. Durmus, P. E. Jacob, R. Badeau, and U. Şimşekli, *Fast Approximation of the Sliced-Wasserstein Distance Using Concentration of Random Projections*, arXiv:2106.15427 (first submitted 2021-06-29). https://arxiv.org/abs/2106.15427
