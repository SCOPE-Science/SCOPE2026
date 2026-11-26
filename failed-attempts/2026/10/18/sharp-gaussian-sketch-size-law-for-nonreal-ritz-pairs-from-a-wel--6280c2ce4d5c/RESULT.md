# Sharp Gaussian sketch-size law for nonreal Ritz pairs from a well-conditioned symmetric matrix

## Finding

For the three-dimensional positive-definite matrix \(A=\operatorname{diag}(1,2,3)\) and starting vector \(v=(1,1,1)^\top/\sqrt3\), consider the two-dimensional Krylov trial subspace \(K=\operatorname{span}\{v,Av\}\). Sketch-orthogonal Arnoldi can produce a **nonreal conjugate pair** even though every eigenvalue of \(A\) is positive and real. The probability of this spectral artifact for an independent real Gaussian sketch with \(s\ge2\) rows is exactly

\[
P_s=\frac{s-1}{2\pi}\int_{\mathbb R}\int_{-\infty}^{-(y^2+8)/(4\sqrt2)}(1+x^2+y^2)^{-(s+1)/2}\,dx\,dy.
\]

In particular, \(P_2=0.113224898589\ldots\), while the **sharp oversampling asymptotic** is

\[
\boxed{P_s\sim\sqrt{\frac{3}{2\pi s}}\,3^{-s/2}}\qquad(s\to\infty).
\]

This quantifies how Gaussian sketch size controls loss of real Ritz values. For every finite \(s\), the failure probability is strictly positive; increasing sketch size suppresses it at exact exponential rate \(\tfrac12\log3\), with an additional inverse-square-root factor.

## Assumptions and scope

Let \(s\in\{2,3,\ldots\}\). Draw \(S\in\mathbb R^{s\times3}\) with independent \(N(0,1)\) entries, once per Rayleigh--Ritz extraction. Define the sketch-orthogonal compression using any Euclidean-orthonormal matrix \(Q\in\mathbb R^{3\times2}\) spanning \(K\):

\[
H_S=((SQ)^\top SQ)^{-1}(SQ)^\top SAQ.
\]

The inverse exists almost surely. Changes of the basis \(Q\) act on \(H_S\) by similarity and preserve its eigenvalues. This expression is exactly the matrix represented by the sketch-orthogonal Arnoldi orthogonalization of the same Krylov space in exact arithmetic. The result addresses an extraction stage; no restart or convergence statement is asserted. The ordinary Euclidean compression is symmetric and has real spectrum inside \([1,3]\).

## Proof

**1. Orthogonal Krylov coordinates.** Put

\[
q_1=\frac1{\sqrt3}(1,1,1)^\top,\quad q_2=\frac1{\sqrt2}(-1,0,1)^\top,\quad q_3=\frac1{\sqrt6}(1,-2,1)^\top.
\]

The matrix \(Q=[q_1,q_2]\) spans \(K\); its columns together with \(q_3\) form an orthonormal basis. Direct multiplication gives

\[
Q^\top AQ=\begin{pmatrix}2&\sqrt{2/3}\\\sqrt{2/3}&2\end{pmatrix},\quad q_3^\top AQ=(0,1/\sqrt3).
\]

Thus the Euclidean Ritz values are \(2\pm\sqrt{2/3}\). Since \(AQ=Q(Q^\top AQ)+q_3(q_3^\top AQ)\), define \(W=SQ\), \(z=Sq_3\), and \(\eta=(W^\top W)^{-1}W^\top z=(x,y)^\top\). Then

\[
H_S=\begin{pmatrix}2&\sqrt{2/3}+x/\sqrt3\\\sqrt{2/3}&2+y/\sqrt3\end{pmatrix}.
\]

Its characteristic discriminant is

\[
\Delta_S=(\operatorname{tr}H_S)^2-4\det H_S=\frac{y^2+8+4\sqrt2 x}{3}.
\]

The two Ritz values are nonreal precisely when \(x<-(y^2+8)/(4\sqrt2)\). Equality has probability zero.

**2. Exact Gaussian leakage density.** Orthogonal invariance of an iid Gaussian matrix makes the entries of \(W\in\mathbb R^{s\times2}\) and \(z\in\mathbb R^s\) mutually independent standard normals. Conditional on \(W\), \(\eta\) is Gaussian with covariance \((W^\top W)^{-1}\). Its conditional density is proportional to

\[
\det(W^\top W)^{1/2}\exp(-\eta^\top W^\top W\eta/2).
\]

When integrating over \(W\), right multiplication by \((I_2+\eta\eta^\top)^{1/2}\) gives density proportional to \(\det(I_2+\eta\eta^\top)^{-(s+1)/2}=(1+x^2+y^2)^{-(s+1)/2}\). Radial integration normalizes it to

\[
f_s(x,y)=\frac{s-1}{2\pi}(1+x^2+y^2)^{-(s+1)/2}.
\]

Integration over the negative-discriminant region gives the displayed exact \(P_s\). This region is open and nonempty, so \(0<P_s<1\) for every finite \(s\).

**3. Sharp large-sketch asymptotics.** Parameterize the negative-discriminant region by \(x=-\sqrt2-y^2/(4\sqrt2)-t\), where \(y\in\mathbb R\) and \(t>0\). The unique point minimizing \(1+x^2+y^2\) on the closed region is \((-\sqrt2,0)\), with minimum value three. In these coordinates,

\[
1+x^2+y^2=3+2\sqrt2\,t+\frac32 y^2+\left(t+\frac{y^2}{4\sqrt2}\right)^2
\]

More directly, the exact identity \(1+x^2+y^2=3+2\sqrt2 t+\tfrac32 y^2+(t+y^2/(4\sqrt2))^2\) follows immediately by expanding the square. The nonnegative remainder establishes global strict minimality. As \(s\to\infty\), with \(t=u/s\) and \(y=w/\sqrt s\),

\[
\left(\frac{1+x^2+y^2}{3}\right)^{-(s+1)/2}\longrightarrow \exp\left(-\frac{\sqrt2}{3}u-\frac14w^2\right).
\]

The nonnegative quadratic remainder, integrable polynomial tails, and uniqueness of the minimizer justify localization and dominated convergence (e.g., split into \(|w|+u\le R\) after rescaling and its complement). The Jacobian is \(s^{-3/2}\); using the density prefactor \((s-1)/(2\pi)\) and integrating the limiting exponential yields

\[
\frac{s-1}{2\pi}s^{-3/2}3^{-(s+1)/2}\cdot\frac3{\sqrt2}\cdot2\sqrt\pi\sim\sqrt{\frac3{2\pi s}}3^{-s/2}.
\]

This proves the exact exponential rate and leading constant.

## Verification

A standalone verifier in `verify.py` checks the three orthonormal directions, the compression, the exact discriminant, a deterministic nonreal-eigenvalue witness, and the formula for \(H_S\) against direct Gaussian linear-algebra computations for multiple sketch sizes. It independently evaluates the one-dimensional incomplete-beta representation of the exact integral, tests specific numerical values and the approach to the asymptotic constant. The recorded deterministic output is in `verification_output.txt` and dependencies in `requirements.txt`. These computations corroborate but do not replace the all-\(s\) density and Laplace arguments.

## Relationship to prior work

The 2024 randomized Arnoldi analysis of de Damas and Grigori (arXiv:2407.03208v1, sections 2.4, 3.2, and 5) defines the same sketch-orthogonal projection and investigates randomized eigenvalue extraction. The distinct contribution here is an **exact probability integral and sharp oversampling asymptotic** for a particular symmetric positive-definite input, not a general convergence guarantee. Palitta, Schweitzer and Simoncini (2025, section 3 and conclusions) discuss spurious sketched Ritz values outside the original spectral region and explain their possible limited effect on matrix-function evaluation; the existence of such spectral artifacts is therefore not claimed as generally new. Shao (2026, sections 3--5) studies a different randomized Ritz extraction using complex Gaussian test spaces and eigenpair convergence, without the real-Gaussian two-step event distribution above. The Gaussian regression density and saddle-point method are classical tools. The result is a sharp, method-specific quantification, not a claim of globally unique spectral pollution.

## Limitations

The theorem concerns exactly one well-conditioned \(3\times3\) example, two Krylov vectors, iid **real** Gaussian sketches, exact arithmetic, and the sketch-orthogonal extraction stage. The result does not establish failure of restarted algorithms, nor does it quantify quality of final Ritz vectors, matrix-function evaluations, or floating-point effects. The asymptotic does not apply unchanged to complex Gaussian or structured sketches. Related but differently phrased formulas in older random Petrov--Galerkin literature remain an originality risk. Independent scientific audit has not been performed.

## References

1. J.-G. de Damas and L. Grigori, *Randomized Implicitly Restarted Arnoldi method for the non-symmetric eigenvalue problem*, arXiv:2407.03208v1 (2024), sections 2--5, https://arxiv.org/html/2407.03208v1.
2. D. Palitta, M. Schweitzer, and V. Simoncini, *Sketched and Truncated Polynomial Krylov Methods: Evaluation of Matrix Functions*, Numerical Linear Algebra with Applications 32 (2025), e2596, DOI: 10.1002/nla.2596, especially sections 3--5.
3. N. Shao, *Stabilizing the Rayleigh--Ritz procedure by randomization*, arXiv:2604.01037v1 (2026), sections 3--5, https://arxiv.org/html/2604.01037v1.
