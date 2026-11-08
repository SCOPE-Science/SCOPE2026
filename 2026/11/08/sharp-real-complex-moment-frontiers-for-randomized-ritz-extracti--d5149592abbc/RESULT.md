# Sharp real–complex moment frontiers for randomized Ritz extraction on an interior eigenpair

## Finding

Fix the real symmetric matrix
\[
A=\operatorname{diag}(-1,0,1),\qquad v=e_2,
\]
and the orthonormal trial plane
\[
p=(e_1+e_3)/\sqrt2,\quad q=(e_1-e_3)/\sqrt2,\quad
W_\theta=[\cos\theta\,v+\sin\theta\,p,\ q],\qquad 0<\theta<\pi/2.
\]
Here \(\angle(v,\operatorname{range}W_\theta)=\theta\). Choose either the real field \(\mathbb F=\mathbb R\) or complex field \(\mathbb F=\mathbb C\), and draw a single \(3\times2\) matrix \(\Omega\) with independent standard real normal entries or independent circular standard complex normal entries, respectively. Hold \(\Omega\) fixed as \(\theta\downarrow0\). Apply the square Gaussian Petrov–Galerkin randomized Rayleigh–Ritz procedure:
\[
\Omega^*AW_\theta y_\theta=\mu_\theta\Omega^*W_\theta y_\theta.
\]
Almost surely, for all sufficiently small positive \(\theta\) there is a unique randomized Ritz eigenvalue nearest zero. Normalize its eigenvector as \(y_\theta=(1,z_\theta)^\mathsf T\), and define the actual eigenvector angle and refined Ritz value
\[
\Theta_\theta=\angle(v,W_\theta y_\theta),\qquad
\rho_\theta=\frac{(W_\theta y_\theta)^*A(W_\theta y_\theta)}{\|W_\theta y_\theta\|^2}.
\]

**Theorem (exact first-order and refined-error laws).** On a probability-one event, the three normalized errors converge as \(\theta\downarrow0\). Each scalar coefficient of \(\mu_\theta/\theta\) and \(z_\theta/\theta\) has the standard ratio-of-independent-Gaussians law over \(\mathbb F\), though these coefficients are not asserted independent. If \(Z\) has that common law, then the three limiting *marginal* magnitudes are
\[
\frac{|\mu_\theta|}{\theta}\longrightarrow |Z|,\qquad
\frac{\Theta_\theta}{\theta}\longrightarrow\sqrt{1+|Z|^2},\qquad
\frac{|\rho_\theta|}{\theta^2}\longrightarrow 2|\operatorname{Re}Z|.
\]
The use of one symbol \(Z\) expresses equality of marginal laws, not joint equality. These laws have the following exact survival functions, for \(t>0\) in the first and third columns and \(t\ge1\) in the middle column:

| Field | \(\Pr\{|Z|>t\}\) | \(\Pr\{\sqrt{1+|Z|^2}>t\}\) | \(\Pr\{2|\operatorname{Re}Z|>t\}\) |
|---|---|---|---|
| Real | \(\frac2\pi\arctan(1/t)\) | \(\frac2\pi\arcsin(1/t)\) | \(\frac2\pi\arctan(2/t)\) |
| Complex | \(\frac1{1+t^2}\) | \(t^{-2}\) | \(1-t/\sqrt{t^2+4}\) |

Thus each normalized limiting error has a finite absolute moment of order \(p>0\) **if and only if** \(p<1\) for real Gaussian testing, or \(p<2\) for circular complex Gaussian testing. In particular, for each of the three actual finite-angle errors, the expected normalized \(p\)-th power diverges to infinity as \(\theta\downarrow0\) when \(p\ge1\) in the real case or \(p\ge2\) in the complex case. No uniform mean-square linear eigenvector bound or mean-square quadratic refined-value bound exists even on this fixed three-dimensional Hermitian example.

## Assumptions and scope

The field is real or complex with isotropic standard Gaussian testing. The problem is exactly the displayed \(3\times3\) Hermitian interior simple eigenvalue, the trial dimension is exactly two, and the same random matrix is coupled across decreasing \(\theta\). The selected eigenpair is the near-zero analytic branch, equivalently the unique eigenvalue of smallest magnitude for sufficiently small \(\theta\), almost surely. Limits are almost sure in this coupling, so their laws also describe weak limits for independently resampled tests at each \(\theta\). The theorem concerns marginal laws and moment obstructions, not moments of the finite-angle errors at each fixed angle, nor joint independence of the errors.

## Proof

Let \([x,y]\) denote the \(2\times2\) matrix with columns \(x,y\), and \(D_{xy}=\det[x,y]\). Define
\[
a=\Omega^*v,\qquad b=\Omega^*p,\qquad c=\Omega^*q.
\]
Because \([v,p,q]\) is orthogonal/unitary, \(a,b,c\) are mutually independent standard Gaussian two-vectors over the chosen field. The identities \(Av=0\), \(Ap=-q\), \(Aq=-p\) yield the exact pencil determinant
\[
F(\mu,\theta)=\det\big[\sin\theta\,c+\mu(\cos\theta\,a+\sin\theta\,b),\ b+\mu c\big]
=\sin\theta\,D_{cb}+\mu\cos\theta\,D_{ab}
+\mu^2(\cos\theta\,D_{ac}+\sin\theta\,D_{bc}).
\]
The random determinants \(D_{ab}\) and \(D_{ac}\) are nonzero almost surely. Thus \(F(\mu,0)=\mu(D_{ab}+\mu D_{ac})\) has a simple root at zero and a distinct, nonzero other root. The analytic implicit-function theorem gives exactly one eigenvalue branch tending to zero. Differentiating at zero gives
\[
\mu'_0=-\frac{D_{cb}}{D_{ab}}.
\]
The associated right eigenvector can be normalized as \((1,z_\theta)^\mathsf T\), where \(z_0=0\). Differentiating the two-column null-vector equation
\[
\sin\theta\,c+\mu_\theta(\cos\theta\,a+\sin\theta\,b)
+z_\theta(b+\mu_\theta c)=0
\]
produces \(c+\mu'_0a+z'_0b=0\), hence
\[
z'_0=-\frac{D_{ac}}{D_{ab}}.
\]
These formulas are valid in the complex case as ordinary complex-analytic perturbation in the *real* parameter \(\theta\) with each Gaussian realization held fixed.

Conditional on any nonzero \(b\), the two determinants \(D_{cb}\) and \(D_{ab}\) are independent centered real Gaussians or circular complex Gaussians with the same variance \(\|b\|^2\). Similarly, conditional on any nonzero \(a\), the determinants \(D_{ac}\) and \(D_{ab}\) have the same independent Gaussian structure. Therefore both derivative coefficients are standard Gaussian ratios over \(\mathbb F\). In the real case this is the ordinary Cauchy density \(1/[\pi(1+x^2)]\). In the complex case the planar density is
\[
f_Z(x+iy)=\frac1{\pi(1+x^2+y^2)^2},
\]
obtained by the Jacobian \(|y|^2\) for the change of variables from two independent circular complex Gaussians \((X,Y)\) to \((X/Y,Y)\). Integrating radially gives \(\Pr(|Z|>t)=1/(1+t^2)\). The marginal density of \(\operatorname{Re}Z\) is \(1/[2(1+x^2)^{3/2}]\). These facts give the first and third survival columns, with the ordinary real Cauchy formula in the real case.

Since the columns of \(W_\theta\) are orthonormal, direct geometry gives
\[
\sin^2\Theta_\theta=\frac{\sin^2\theta+|z_\theta|^2}{1+|z_\theta|^2},
\qquad
\rho_\theta=\frac{-2\sin\theta\operatorname{Re}z_\theta}{1+|z_\theta|^2}.
\]
Dividing and passing to the limit proves the angle and refined-value laws. Their survival formulas follow by the transformations \(\sqrt{1+|Z|^2}\) and \(2|\operatorname{Re}Z|\). In particular, the complex eigenvector inflation factor has the **exact Pareto tail** \(t^{-2}\) for every \(t\ge1\), whereas its real counterpart has tail \(2\arcsin(1/t)/\pi\).

The real Gaussian ratios have asymptotic absolute tails proportional to \(t^{-1}\), and the complex ratios have tails proportional to \(t^{-2}\); the real components of complex ratios have the same exponent two. Consequently, \(\mathbb E|X|^p<\infty\) for each displayed limiting magnitude exactly for \(0<p<d\), where \(d=1\) (real) or \(d=2\) (complex). For example the complex limiting inflation factor has the explicit moment \(\mathbb E(1+|Z|^2)^{p/2}=2/(2-p)\) for \(0<p<2\).

Finally, each finite-angle normalized magnitude converges almost surely to its displayed infinite- or finite-moment limiting magnitude. For \(p\ge d\), Fatou's lemma applied to an arbitrary sequence \(\theta\downarrow0\) gives
\[
\liminf_{\theta\downarrow0}\mathbb E\left(\frac{|\mu_\theta|}{\theta}\right)^p
=\liminf_{\theta\downarrow0}\mathbb E\left(\frac{\Theta_\theta}{\theta}\right)^p
=\liminf_{\theta\downarrow0}\mathbb E\left(\frac{|\rho_\theta|}{\theta^2}\right)^p
=+\infty,
\]
where the three equalities to \(+\infty\) are separate assertions, not an equality of finite expectations. This proves the claimed failure of uniform moment-rate bounds. \(\square\)

## Verification

The companion artifact `verify_ritz.py` is a standalone Python 3 checker (standard library only): run `python3 verify_ritz.py`. It verifies the determinant and eigenvector equations for real and complex finite-angle instances, checks exact angle and Rayleigh identities, and compares reproducible Gaussian samples against all six analytic tail formulas. Random samples are finite sanity checks, not demonstrations of infinite-moment or almost-sure statements; those are proved by the Gaussian-ratio calculation and Fatou's lemma above.

## Relationship to prior work

Shao's *Stabilizing the Rayleigh–Ritz procedure by randomization* (arXiv:2604.01037v1, first public April 1, 2026), Section 2 Example 1, uses this very Hermitian interior-eigenpair geometry to show failure of ordinary Ritz-vector convergence. Its Algorithm 1 introduces complex Gaussian Petrov–Galerkin testing; Lemma 3 and Theorems 2–3 establish high-probability error rates, and Section 5.3 gives an empirical sharpness discussion for a failure-probability factor. The present theorem does **not** claim the Gaussian ratio identity, or high-probability convergence of the algorithm, as new. It supplies exact selected-eigenpair error distributions, a real-versus-complex moment threshold, and rigorous absence of uniform mean-square bounds for both the vector and refined value on the canonical stress test. Those precise moment conclusions are not contained in the inspected version of the source.

The Cauchy law for real Gaussian quotients is classical (see Pillai, 2016). Gaussian-ratio distributional questions in the complex field have also been studied by Gu (2020). These general distributions alone do not state the first-order Ritz eigenvector selection and refined-Rayleigh mapping, which are computed here. Older Gaussian Petrov–Galerkin perturbation and later revisions of the motivating preprint remain priority risks.

## Limitations

This is a first-order small-angle distribution and moment-obstruction result for a single, explicitly fixed interior eigenpair and a two-dimensional trial plane. No uniform \(L^p\) convergence is asserted for \(p\) below the displayed thresholds. The three limiting errors are not shown jointly independent. This says nothing about exterior eigenvalues, larger trial spaces, nonsquare oversampling, algorithmic runtime, or full eigensolver convergence. The motivating preprint has later versions (including a publicly listed October 26, 2026 revision) that were not fully retrievable in this inspection; the exact priority of the moment formulation against those later revisions remains uncertain.

## References

1. N. Shao, *Stabilizing the Rayleigh–Ritz procedure by randomization*, arXiv:2604.01037v1 (public April 1, 2026), https://arxiv.org/html/2604.01037v1 .
2. N. S. Pillai, *Ratios and Cauchy Distribution*, arXiv:1602.08181 (2016), https://arxiv.org/abs/1602.08181 .
3. D. Gu, *On The Quotient of Centralized and Non-Centralized Complex Gaussian Random Variables*, Journal of Research of NIST 125 (2020), https://www.nist.gov/publications/quotient-centralized-and-non-centralized-complex-gaussian-random-variables .
4. Y. Nakatsukasa, *Sharp error bounds for Ritz vectors and approximate singular vectors*, Mathematics of Computation 89 (2020), https://arxiv.org/abs/1810.02532 .
