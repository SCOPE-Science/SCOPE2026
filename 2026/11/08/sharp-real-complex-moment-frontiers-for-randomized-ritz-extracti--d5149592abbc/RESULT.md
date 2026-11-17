# Sharp real-Gaussian Ritz error tails and a first-moment obstruction for an interior eigenpair

## Finding

Let
\[
 A=\operatorname{diag}(-1,0,1),\quad v=e_2,\quad
 p=(e_1+e_3)/\sqrt2,\quad q=(e_1-e_3)/\sqrt2,
 \quad W_\theta=[\cos\theta\,v+\sin\theta\,p,\ q],\qquad 0<\theta<\pi/2.
\]
Draw **one real** \(3\times2\) matrix \(\Omega\) with independent standard real Gaussian entries, and retain this draw while \(\theta\downarrow0\). Consider the real square randomized Petrov–Galerkin Ritz problem
\[
 \Omega^{\mathsf T}AW_\theta y_\theta
 =\mu_\theta\Omega^{\mathsf T}W_\theta y_\theta.
\]
Almost surely the Ritz eigenvalue nearest zero is unique for all sufficiently small positive \(\theta\), and its eigenvector has a unique normalization \(y_\theta=(1,z_\theta)^\mathsf T\) with \(z_\theta\to0\). Define
\[
 \Theta_\theta=\angle(v,W_\theta y_\theta),\qquad
 \rho_\theta=\frac{(W_\theta y_\theta)^\mathsf T A(W_\theta y_\theta)}{\|W_\theta y_\theta\|_2^2}.
\]
**Theorem (real-field first-order laws).** These three normalized magnitudes converge almost surely and have the following exact *marginal* limiting distributions. With \(Z\) a standard real Cauchy variable,
\[
 \frac{|\mu_\theta|}{\theta}\Rightarrow |Z|,\qquad
 \frac{\Theta_\theta}{\theta}\Rightarrow\sqrt{1+Z^2},\qquad
 \frac{|\rho_\theta|}{\theta^2}\Rightarrow 2|Z|.
\]
The three uses of \(Z\) describe equality of marginal laws, **not** a common joint limit or independence. For \(t>0\), the first and third limiting tails are
\[
 \Pr(|Z|>t)=\frac2\pi\arctan\frac1t,\qquad
 \Pr(2|Z|>t)=\frac2\pi\arctan\frac2t;
\]
for \(t\ge1\), the limiting angle-inflation tail is
\[
 \Pr\bigl(\sqrt{1+Z^2}>t\bigr)=\frac2\pi\arcsin\frac1t.
\]
Each limiting magnitude has a finite positive absolute moment of order \(p\) **if and only if** \(0<p<1\). Moreover, for each of the three corresponding normalized *finite-angle* errors and every \(p\ge1\), its \(p\)-th moment tends to \(+\infty\) as \(\theta\downarrow0\). Thus square **real-Gaussian** testing does not permit a uniform expected-absolute-error bound at the nominal first-order eigenvector or second-order refined-value scale, even for this fixed simple Hermitian interior eigenpair.

The comparable sharp complex-Gaussian first-order law, including the complex tails and the \(p=2\) moment threshold, was **already obtained** in the earlier result *Sharp joint complex-Cauchy error law for two-dimensional randomized Rayleigh–Ritz* (November 2, 2026); those complex claims are not part of the new theorem. In particular, the sharp contrast is that real testing already loses the first normalized absolute moment, whereas the known complex limiting laws retain all moments of order \(p<2\). This does **not** claim uniform finite-angle complex moment bounds.

## Assumptions and scope

The field of the theorem is strictly \(\mathbb R\); the random test matrix is square with exactly two real rows after projection and no oversampling. The selected eigenpair is the almost-sure locally analytic branch nearest the target interior eigenvalue. The same realization is coupled across angles only to express almost-sure limits; independent fresh testing at each angle gives the same weak limits. The angle is the acute subspace/eigenvector angle and \(\rho_\theta\) is the *ordinary* Rayleigh quotient, not the randomized eigenvalue. No joint independence is asserted and no moment convergence below order one is asserted.

## Proof

Set \(a=\Omega^{\mathsf T}v\), \(b=\Omega^{\mathsf T}p\), \(c=\Omega^{\mathsf T}q\), independent standard two-dimensional real Gaussian vectors by orthogonality of \(v,p,q\). For two columns \(x,y\), put \(D_{xy}=\det[x,y]\). Since \(Av=0\), \(Ap=-q\), and \(Aq=-p\), the compressed pencil has, up to multiplication by a nonzero overall sign, determinant
\[
 F(\mu,\theta)=\sin\theta D_{cb}
 +\mu\cos\theta D_{ab}
 +\mu^2(\cos\theta D_{ac}+\sin\theta D_{bc}).
\tag{1}
\]
Almost surely \(D_{ab}D_{ac}\ne0\). At \(\theta=0\) the two eigenvalues are the simple root zero and the nonzero root \(-D_{ab}/D_{ac}\). The real analytic implicit-function theorem therefore selects a unique branch \(\mu_\theta\to0\) and its normalized null vector \((1,z_\theta)^\mathsf T\) with \(z_\theta\to0\). Differentiation of (1) gives
\[
 \mu'_0=-\frac{D_{cb}}{D_{ab}}.
\tag{2}
\]
Differentiating the compressed null-vector equation
\[
 \sin\theta c+\mu_\theta(\cos\theta a+\sin\theta b)
 +z_\theta(b+\mu_\theta c)=0
\]
at zero gives \(c+\mu'_0a+z'_0b=0\), whence
\[
 z'_0=-\frac{D_{ac}}{D_{ab}}.
\tag{3}
\]
Condition on any nonzero \(b\). The real scalars \(D_{cb}\) and \(D_{ab}\) are independent centered Gaussians with equal variance \(\|b\|_2^2\), so their quotient in (2) is standard Cauchy. Similarly, condition on any nonzero \(a\): \(D_{ac}\) and \(D_{ab}\) have independent equal-variance Gaussian laws, so (3) is also standard Cauchy. The two quotients need not be independent.

The orthonormality of \(W_\theta\) gives the exact geometrical identities
\[
 \sin^2\Theta_\theta=\frac{\sin^2\theta+z_\theta^2}{1+z_\theta^2},\qquad
 \rho_\theta=-\frac{2\sin\theta\,z_\theta}{1+z_\theta^2}.
\tag{4}
\]
Equations (2)–(4) yield the almost-sure scalar limits
\[
 \mu_\theta/\theta\to\mu'_0,\quad
 \Theta_\theta/\theta\to\sqrt{1+(z'_0)^2},\quad
 \rho_\theta/\theta^2\to-2z'_0.
\]
Each limiting marginal is the transformation of a standard real Cauchy variable stated above. Its density \(1/[\pi(1+x^2)]\) gives \(\Pr(|Z|>t)=2\arctan(1/t)/\pi\), from which the remaining two tails follow exactly. Since each is asymptotic to a positive multiple of \(t^{-1}\), all their positive moments exist exactly for \(0<p<1\).

For each error separately, apply Fatou's lemma to the corresponding nonnegative normalized \(p\)-th power along an arbitrary sequence \(\theta\downarrow0\). When \(p\ge1\), the limit has infinite expectation, and therefore the finite-angle expectations tend to \(+\infty\) in the extended-real sense. This argument does not infer finite-angle distributions or uniform lower-order moment bounds. \(\square\)

## Verification and limitations

The retained standalone `verify_ritz.py` checks the determinant and eigenvector equations, angle and refined-Rayleigh identities, and real-Gaussian tail frequencies using seeded samples. Its additional complex-field checks concern an **already published** comparison, not an additional originality claim. No finite set of random simulations proves the moment divergence: that conclusion follows from the exact Cauchy law and Fatou's lemma.

The result is specifically about the real field, the displayed three-dimensional Hermitian interior eigenpair, a two-dimensional trial plane, one square real-Gaussian sketch, and a small-angle limit. Larger test spaces, oversampling, exterior eigenpairs, finite-angle low-order moment control and general eigensolver behavior remain outside scope.

## Relationship to previous mathematics

The November 2, 2026 result *Sharp joint complex-Cauchy error law for two-dimensional randomized Rayleigh–Ritz* establishes, in a stronger general two-dimensional Hermitian setting, the full joint **complex** law and on this very example the complex marginal Ritz, angle and refined-quotient tails with critical moment exponent two. Consequently those complex laws cannot be claimed as new here. That result expressly restricts its random testing to the complex field and does not imply the distinct real Cauchy \(t^{-1}\) tails or first-moment nonintegrability. The present contribution is their explicit selected-eigenpair derivation and sharp **real** boundary, which is mathematically relevant to choosing the Gaussian testing field.

N. Shao's *Stabilizing the Rayleigh–Ritz procedure by randomization* (arXiv:2604.01037, April–October 2026) introduces the Petrov–Galerkin algorithm and the same deterministic stress-test geometry; its high-probability estimates do not replace a real-field first-moment lower obstruction. Classical Cauchy ratio results (Pillai, 2016) are used as mathematical input, not asserted as new. The real-field conclusion is a specialization of Gaussian-ratio methods, and older numerical-linear-algebra literature may contain an equivalent statement. No absolute publication-priority guarantee is made.

## References

1. *Sharp joint complex-Cauchy error law for two-dimensional randomized Rayleigh–Ritz*, published November 2, 2026, https://github.com/Resultary/2026/tree/main/2026/11/2/SCOPE-sharp-joint-complex-cauchy-error-law-for-two-dimensional-randomi--629c63caaa73 .
2. N. Shao, *Stabilizing the Rayleigh–Ritz procedure by randomization*, arXiv:2604.01037, https://arxiv.org/abs/2604.01037 .
3. N. S. Pillai, *Ratios and Cauchy Distribution*, arXiv:1602.08181, https://arxiv.org/abs/1602.08181 .
4. D. Gu, *On The Quotient of Centralized and Non-Centralized Complex Gaussian Random Variables*, Journal of Research of NIST 125 (2020), https://www.nist.gov/publications/quotient-centralized-and-non-centralized-complex-gaussian-random-variables .
