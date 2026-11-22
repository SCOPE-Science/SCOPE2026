# Local uniform optimality and global majorization failure for cyclic trinomial roughness

## Finding

For every fixed probability vector \(p=(p_1,p_2,p_3)\) in the closed three-category simplex \(\Delta_3\), let \(X^{(N)}\sim\operatorname{Multinomial}(N,p)\). Define the *matched-centered cyclic total variation*

\[
T_{N,p}=\sum_{j=1}^{3}\left|X^{(N)}_{j+1}-X^{(N)}_j-N(p_{j+1}-p_j)\right|,
\quad X^{(N)}_4=X^{(N)}_1,\quad p_4=p_1.
\]

The limiting variance coefficient \(V(p)=\lim_{N\to\infty}N^{-1}\operatorname{Var}(T_{N,p})\) exists and is continuous on \(\Delta_3\). It is invariant under *all* permutations of the three probabilities. With \(u=(1/3,1/3,1/3)\) and any tangent perturbation \(h\in\mathbb R^3\) satisfying \(\sum_jh_j=0\),

\[
V(u+h)=\frac83+\frac{4\sqrt3-12}{\pi}
+\frac{81-16\pi-24\sqrt3}{4\pi}\sum_{j=1}^3h_j^2
+o(\lVert h\rVert^2).
\]

The quadratic coefficient is strictly negative. Thus the uniform law is a **strict local maximizer** of limiting cyclic roughness variance on the full simplex. Nevertheless, for the nonuniform boundary vector \(b=(1/2,0,1/2)\),

\[
V(b)=4\left(1-\frac2\pi\right)
>V(u)=\frac83+\frac{4\sqrt3-12}{\pi}.
\]

Consequently \(V\) is neither Schur-convex nor Schur-concave, and it is not quasi-concave, on the three-category probability simplex. Along the symmetric segment \(p(a)=(a,1-2a,a)\), \(1/3\le a\le1/2\), it has an interior local minimum. These are statements about the variance coefficient, not the uncentered roughness expectation.

## Assumptions and scope

The sample size \(N\) tends to infinity while the three category probabilities are held fixed. Probabilities may be zero, interpreted using the degenerate multinomial and Gaussian limits. The centering in each edge is by its **own exact expectation** \(N(p_{j+1}-p_j)\), not by a common uniform reference vector. No statement is made about finite-sample global optimizers, other numbers of categories, or unequal sample-size/category growth rates. Schur order and quasi-concavity are understood on the usual closed probability simplex.

## Proof

**1. Gaussian variance limit and continuity.** For iid categorical observations, the multivariate central limit theorem gives

\[
N^{-1/2}(X^{(N)}-Np)\ \Longrightarrow\ Z_p,
\qquad Z_p\sim N_3(0,\Sigma_p),\qquad
\Sigma_p=\operatorname{diag}(p)-pp^{\mathsf T}.
\]

The same argument, allowing singular covariance, holds when a coordinate of \(p\) vanishes. The function \(x\mapsto\sum_j|x_{j+1}-x_j|\) is continuous and bounded by \(6\max_j|x_j|\). Its squared value evaluated on the normalized multinomial fluctuation has uniformly bounded second moments: expanding fourth moments of sums of independent bounded centered categorical indicators gives \(\sup_N\mathbb E\lVert N^{-1/2}(X^{(N)}-Np)\rVert^4<\infty\) for fixed \(p\). Therefore its first and second moments converge. Hence

\[
V(p)=\operatorname{Var}\!\left(\sum_{j=1}^3|Z_{p,j+1}-Z_{p,j}|\right).
\]

Couple the Gaussians as \(Z_p=\Sigma_p^{1/2}G\) for standard \(G\in\mathbb R^3\). The positive-semidefinite square root varies continuously with \(p\) on the simplex and its operator norm is bounded there; dominated convergence of the first two moments proves continuity of \(V\) even at the boundary.

**2. Reduction to a Gaussian range.** For any three real numbers, the sum of their three pairwise absolute differences is twice their range:

\[
|z_2-z_1|+|z_3-z_2|+|z_1-z_3|
=2(\max_j z_j-\min_j z_j).
\]

Thus \(V\) is invariant under the full symmetric group acting on probability coordinates, not merely cyclic rotation.

**3. Exact symmetric-ray profile.** Set \(p(a)=(a,1-2a,a)\), initially \(0<a<1/2\). In the centered Gaussian limit define \(S=Z_{p,1}-Z_{p,3}\) and \(M=Z_{p,1}+Z_{p,3}-2Z_{p,2}\). As \(Z_{p,1}+Z_{p,2}+Z_{p,3}=0\) almost surely, \(M=-3Z_{p,2}\). Directly from \(\Sigma_p\),

\[
\operatorname{Var}(S)=2a,\quad
\operatorname{Var}(M)=18a(1-2a),\quad
\operatorname{Cov}(S,M)=0.
\]

The jointly Gaussian \(S,M\) are independent. Since \(|(M+S)/2|+|(M-S)/2|=\max(|M|,|S|)\), the cyclic sum of absolute differences has the exact law

\[
\sqrt{2a}\,\bigl(|G|+\max(|G|,t|H|)\bigr),
\qquad t=3\sqrt{1-2a},
\]

where \(G,H\) are independent standard normals. Let \(W_t=|G|+\max(|G|,t|H|)\) and \(\alpha=\arctan(1/t)\) for \(t>0\). Integrating in polar coordinates on the first quadrant, with the two angular pieces separated at \(\alpha\), yields

\[
\mathbb EW_t=\sqrt{\frac2\pi}(1+\sqrt{1+t^2}),
\qquad
\mathbb EW_t^2=1+t^2+\frac2\pi\bigl((3-t^2)\alpha+3t\bigr).
\]

For clarity, write \((|G|,|H|)=R(\cos\Theta,\sin\Theta)\) with \(\Theta\) uniform on \([0,\pi/2]\), independent of \(R\), and \(\mathbb ER=\sqrt{\pi/2}\), \(\mathbb ER^2=2\). For \(\Theta\le\alpha\), the integrand is \(2\cos\Theta\); for \(\Theta\ge\alpha\), it is \(\cos\Theta+t\sin\Theta\). Integrating those two elementary expressions and their squares proves both displayed moments without assuming independence of the three pairwise contrasts. Therefore

\[
V(p(a))=2aF(t),\qquad
F(t)=1+t^2+\frac2\pi\Bigl((3-t^2)\arctan(1/t)+3t
-(1+\sqrt{1+t^2})^2\Bigr).
\]

The formula extends continuously to \(t=0\), where \(\arctan(1/t)\to\pi/2\).

**4. Full-simplex local maximum.** Differentiate the explicit profile in the interior at \(a=1/3\), where \(t=\sqrt3\). Elementary differentiation (also checked symbolically in `check.py`) gives

\[
V(p(1/3))=\frac83+\frac{4\sqrt3-12}{\pi},\quad
\left.\frac{d}{da}V(p(a))\right|_{a=1/3}=0,
\quad
\left.\frac{d^2}{da^2}V(p(a))\right|_{a=1/3}
=\frac{3(81-16\pi-24\sqrt3)}{\pi}<0.
\]

Because the Gaussian covariance has constant rank two near \(u\), the polar integral representation (equivalently the positive-definite two-dimensional contrast covariance) gives smooth dependence of \(V\) on \(p\) in an interior neighborhood of \(u\). The full permutation symmetry forces the Hessian of \(V\), restricted to the tangent plane \(\sum_jh_j=0\), to be a scalar multiple of the Euclidean quadratic form \(\sum_jh_j^2\). Along \(h=(\delta,-2\delta,\delta)\), this norm squared is \(6\delta^2\), and the second-order Taylor term equals one half of the second derivative above times \(\delta^2\). Hence its scalar coefficient is

\[
\frac{1}{12}\left.\frac{d^2}{da^2}V(p(a))\right|_{a=1/3}
=\frac{81-16\pi-24\sqrt3}{4\pi}<0.
\]

This establishes the claimed full-simplex Taylor expansion and strict local maximality.

**5. Boundary comparison and shape consequences.** At \(a=1/2\), one coordinate is identically zero and the other two form a centered Bernoulli split. The cyclic absolute-difference sum becomes \(2|Z_1-Z_3|\), with \(Z_1-Z_3\sim N(0,1)\). Therefore \(V(b)=4\operatorname{Var}(|G|)=4(1-2/\pi)\). The strict inequality against \(V(u)\) follows from \(\pi>3(\sqrt3-1)\). Any nearby nonuniform vector majorizes \(u\), ruling out Schur-convexity by the strict local maximum; \(b\) majorizes \(u\) while having larger variance, ruling out Schur-concavity. On the segment from \(u\) to \(b\), the value falls immediately below \(V(u)\), then ends above \(V(u)\); therefore the function is not quasi-concave and, by continuity, takes its minimum at some strict interior \(a\in(1/3,1/2)\).

## Verification

Run `python check.py` in the directory containing the embedded files (requires Python 3, SymPy and SciPy). The code independently checks the exact uniform value, first and second derivatives, negative curvature, the boundary limit and strict comparison. It also verifies the polar-integral moment identities at seven parameter values and exhaustively enumerates the trinomial sample probabilities for \(N=90\) and \(N=240\) at three positive probability vectors. The current package passed 26 assertions. These finite checks are supporting consistency checks; the analytical steps above prove the all-\(N\)-limit and simplex statements.

## Relationship to prior work

Banić and Elezović, *Discrete total variation under the multinomial, Part 5: cyclic total variation* (arXiv:2611.14735v1, first public 2026-11-10), introduces the cyclic statistic and states the matched nonuniform Gaussian variance through folded-normal covariances. Its explicit cyclic leading-variance Proposition 5.4 uses at least five bins; it does not state a three-bin symmetric-ray optimization, a full-simplex negative Hessian at uniformity, or a majorization/quasi-concavity counterexample. Its fixed-reference uniform-profile results concern a different normalization and varying bin count.

Banić and Elezović, *Part 4: variance under a general distribution* (arXiv:2611.09592v1), gives the corresponding open-chain nonuniform variance formulas: for three categories its statistic has **two** absolute-difference terms, rather than the three terms of the present cyclic Gaussian range. Thus open-chain three-bin optimizers do not imply this result.

Bonetti, Cirillo and Ogay (2019) give exact finite-sample multinomial order-statistic distributions, including range calculations, and discuss Corrado's (2011) method for arbitrary probabilities. Those algorithms can in principle evaluate finite-sample moments but do not directly supply the present matched-centering, asymptotic local-Hessian and majorization classification. This implication comparison concerns specific proved statements, not title similarity.

## Limitations

No location or uniqueness of a global maximizer or of the interior minimum is asserted. The boundary value is a limit from positive probabilities; no assumption is made about uniform asymptotics when category probabilities themselves vary with \(N\). The full original text of Corrado (2011) could not be inspected, so historical-priority risk remains. No independent mathematical audit or historical novelty certification has been performed.

## References

1. N. Banić and N. Elezović, *Discrete total variation under the multinomial, Part 5: cyclic total variation*, arXiv:2611.14735v1 (first public 2026-11-10), https://arxiv.org/abs/2611.14735.
2. N. Banić and N. Elezović, *Discrete total variation under the multinomial, Part 4: variance under a general distribution*, arXiv:2611.09592v1 (first public 2026-11-06), https://arxiv.org/abs/2611.09592.
3. M. Bonetti, P. Cirillo and A. Ogay, *Computing the exact distributions of some functions of the ordered multinomial counts: maximum, minimum, range and sums of order statistics*, Royal Society Open Science **6** (2019), article 190198, https://doi.org/10.1098/rsos.190198.
4. C. J. Corrado, *The exact distribution of the maximum, minimum and the range of multinomial/Dirichlet and multivariate hypergeometric frequencies*, Statistics and Computing **21** (2011), 349–359, https://doi.org/10.1007/s11222-010-9174-3; primary full text not inspected.
