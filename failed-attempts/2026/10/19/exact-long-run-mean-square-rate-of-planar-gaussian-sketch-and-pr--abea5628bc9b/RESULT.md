# Exact long-run mean-square rate of planar Gaussian sketch-and-project

## Finding

Let \(H\in\mathbb R^{2\times2}\) be symmetric positive definite, with eigenvalues \(0<\mu\le L\), and fix any nonzero deterministic initial error \(x_0\in\mathbb R^2\). At each iteration draw a fresh independent standard Gaussian vector \(z_k\in\mathbb R^2\) and apply the exactly solved one-dimensional subspace-Newton (equivalently Gaussian sketch-and-project) update
\[
x_{k+1}=x_k-z_k\frac{z_k^{\mathsf T}Hx_k}{z_k^{\mathsf T}Hz_k}.
\]
Set \(F(x)=\tfrac12x^{\mathsf T}Hx\), \(\kappa=L/\mu\), and
\[
q=\frac{\sqrt\kappa-1}{\sqrt\kappa+1}\in[0,1).
\]
Then **for every** such \(H\) and \(x_0\), the exact exponential rate of expected quadratic error is
\[
\boxed{\lim_{k\to\infty}\left(\frac{\mathbb E F(x_k)}{F(x_0)}\right)^{1/k}
=\rho_\infty(\kappa)
:=\frac{3+q^2+\sqrt{1+14q^2+q^4}}8.}
\]
This limit is independent of the nonzero starting error. The sharp one-step worst-initial-state factor is instead
\[
\boxed{\rho_1(\kappa)=\sup_{x\ne0}\frac{\mathbb E F(x_1)}{F(x)}
=\frac{1+q}{2}=\frac{\sqrt\kappa}{1+\sqrt\kappa}.}
\]
For every finite \(\kappa>1\), \(\rho_\infty(\kappa)<\rho_1(\kappa)\); equality holds at \(\kappa=1\). As \(\kappa\to\infty\),
\[
\rho_\infty(\kappa)=1-\frac{3}{2\sqrt\kappa}+O(\kappa^{-1}),
\qquad
\rho_1(\kappa)=1-\frac1{\sqrt\kappa}+O(\kappa^{-1}).
\]
Thus the asymptotic mean-square spectral gap is \(3/2\) times the leading gap supplied by the sharp all-iterations one-step contraction.

The entire expected-error sequence is computable by powers of a fixed \(2\times2\) matrix. In an orthonormal eigenbasis of \(H\), put \(y_k=H^{1/2}x_k\) and \(d_k=(\mathbb E[y_{k,1}^{2}],\mathbb E[y_{k,2}^{2}])^{\mathsf T}\). Then
\[
d_{k+1}=M(q)d_k,\qquad
M(q)=\frac18\begin{pmatrix}
3+4q+q^2&1-q^2\\
1-q^2&3-4q+q^2
\end{pmatrix},\qquad
\mathbb E F(x_k)=\frac12(1,1)M(q)^k d_0.
\]
For example, if \(\kappa=9\), the exact asymptotic factor is \((13+\sqrt{73})/32\approx0.6732501170\), strictly better than the worst one-step factor \(3/4\).

## Assumptions and scope

The dimension is exactly two, \(H\) is fixed real symmetric positive definite, the Gaussian sketches are independent across steps and of the initial error, and every reduced quadratic problem is solved exactly in exact arithmetic. Scaling a Gaussian sketch does not change the update. An equivalent least-squares instance is obtained by taking the system matrix \(A=H\), the energy metric \(B=H\), right-hand side zero, and a one-row Gaussian sketch in the standard sketch-and-project formula. The objective is an exact quadratic, so the same direction step is an exact one-dimensional Gauss–Newton subproblem; this does not automatically extend to finite trust regions or step rejections.

## Proof

**1. Energy-space projectors.** Orthogonal diagonalization and rotational invariance of the Gaussian law reduce to \(H=\operatorname{diag}(a^2,b^2)\) with \(0<a\le b\). Write \(z_k\) as a Haar-uniform direction \((\cos\theta_k,\sin\theta_k)\), because its length cancels. In energy variables \(y=H^{1/2}x\), the update is the Euclidean orthogonal projector
\[
y_{k+1}=P_k y_k,\qquad
P_k=I-\frac{H^{1/2}z_kz_k^{\mathsf T}H^{1/2}}{z_k^{\mathsf T}Hz_k}=n_kn_k^{\mathsf T},
\]
where
\[
n_k=\frac{(-b\sin\theta_k,\ a\cos\theta_k)^{\mathsf T}}
{\sqrt{a^2\cos^2\theta_k+b^2\sin^2\theta_k}}.
\]
The unit vector \(n_k\) is independent of the preceding error.

**2. Exact angular moments.** If \(\phi\) is the angle of \(n_k\), the direction density, after a change of variables from a uniform circle angle, is
\[
p(\phi)=\frac{ab}{2\pi(a^2\cos^2\phi+b^2\sin^2\phi)}
=\frac1{2\pi}\frac{1-q^2}{1-2q\cos(2\phi)+q^2},
\qquad q=\frac{b-a}{b+a}.
\]
For \(0\le q<1\), the Poisson-kernel Fourier expansion (absolutely convergent for \(q<1\)) yields \(\mathbb E\cos(2j\phi)=q^j\) and \(\mathbb E\sin(2j\phi)=0\) for every integer \(j\ge1\). Consequently,
\[
\begin{aligned}
\mathbb E n_1^2&=(1+q)/2, &\mathbb E n_2^2&=(1-q)/2,\\
\mathbb E n_1^4&=(3+4q+q^2)/8,&\mathbb E n_2^4&=(3-4q+q^2)/8,\\
\mathbb E n_1^2n_2^2&=(1-q^2)/8,&\mathbb E n_1^3n_2&=\mathbb E n_1n_2^3=0.
\end{aligned}
\]

**3. Closed second-moment dynamics.** Given a symmetric error second-moment matrix \(C_k=\mathbb E[y_ky_k^{\mathsf T}]\), independence yields \(C_{k+1}=\mathbb E[P_k C_k P_k]\). Since \(P=nn^{\mathsf T}\), its diagonal components depend only on the diagonal of \(C_k\), with the explicitly stated matrix \(M(q)\). The off-diagonal entry independently multiplies by \((1-q^2)/4\), and cannot influence the trace. This establishes the formula for every finite \(k\ge0\), not just an asymptotic approximation.

**4. Exact spectral radius and initial-state independence.** The two eigenvalues of \(M(q)\) are
\[
\rho_\pm(q)=\frac{3+q^2\pm\sqrt{1+14q^2+q^4}}8.
\]
For \(0\le q<1\), all entries of \(M(q)\) are strictly positive, its dominant eigenvalue is the simple positive \(\rho_+(q)\), and its right and left dominant eigenvectors have strictly positive entries. The initial diagonal vector \(d_0=(y_{0,1}^2,y_{0,2}^2)^{\mathsf T}\) is nonnegative and nonzero. Thus the coefficient of \(\rho_+^k\) in \((1,1)M^kd_0\) is strictly positive; every other eigenvalue has smaller modulus. Taking \(k\)-th roots proves the claimed common rate for every nonzero initial error, including eigenaxis starts and \(\kappa=1\).

**5. One-step boundary and strict gap.** The matrix \(\mathbb E P\) is \(\operatorname{diag}((1+q)/2,(1-q)/2)\), so its maximal Rayleigh quotient gives \(\rho_1=(1+q)/2\), attained for a lower-curvature eigenvector. For \(0<q<1\), both sides in the comparison are positive and
\[
(1+4q-q^2)^2-(1+14q^2+q^4)=8q(1-q^2)>0.
\]
This proves \(\rho_+(q)<(1+q)/2\). Taylor expansion at \(q=1\), using \(1-q=2/(1+\sqrt\kappa)\), gives the two displayed large-condition-number expansions.

## Verification

Run `python verify.py` with `sympy` installed (see `requirements.txt`). The standalone verifier checks the exact symbolic characteristic polynomial, the strict-gap polynomial identity, the worked \(\kappa=9\) matrix and eigenvalues, and the exact quadratic step decrease. It also compares eight smooth periodic angular integrals with the derived first/fourth moments using deterministic midpoint quadrature. These numerical checks corroborate, but do not prove, the Fourier-integral identities or the theorem for all \(\kappa\).

## Relationship to prior work

Dereziński and Rebrova [1] introduced sharp expected-projection spectral analysis for Gaussian sketch-and-project and its connection to randomized SVD. Their one-step spectral rate (in particular the all-time uniform bound derived from it) does not determine the exact exponential decay constant for each fixed initial error. The present result uses a fourth-moment transfer operator instead and resolves that distinction in the first anisotropic dimension. Stich, Müller and Gärtner [2] analyzed Random Pursuit under exact and approximate line search; Stich et al. [3] further studied metric choices and one-step progress. Cartis, Fowkes and Shao [4] analyzed randomized subspace Gauss–Newton with a trust region. These establish the algorithmic families, not the specific anisotropic \(2\times2\) fourth-moment spectral law obtained here. An equivalent specialized planar second-moment analysis could exist under another terminology; independent priority certification has not been performed.

## Limitations

Only planar positive-definite quadratics, iid Gaussian directions, exact subproblems and expected **quadratic energy** are addressed. The result is neither a statement about sample-path Lyapunov exponents nor a worst-case iteration complexity improvement for the standard uniform-in-time guarantee (which is sharp at one step). It does not extend the closed \(2\times2\) transfer matrix to higher dimensions, dependent sketches, finite trust regions, or noisy implementations. Published-priority uncertainty remains outside the inspected sources.

## References

[1] M. Dereziński and E. Rebrova, *Sharp Analysis of Sketch-and-Project Methods via a Connection to Randomized Singular Value Decomposition*, arXiv:2208.09585 (first public version 2022-08-20), SIAM J. Math. Data Sci. 6 (2024), 127–153; especially Sections 1, 3 and 4.

[2] S. U. Stich, C. L. Müller and B. Gärtner, *Optimization of Convex Functions with Random Pursuit*, arXiv:1111.0194 (2011), SIAM J. Optim. 23 (2013), 1284–1309; Sections 2–5 and appendix.

[3] S. U. Stich, C. L. Müller and B. Gärtner, *Variable Metric Random Pursuit*, arXiv:1210.5114 (2012); Sections 3–5 and appendix.

[4] C. Cartis, J. Fowkes and Z. Shao, *A Randomised Subspace Gauss-Newton Method for Nonlinear Least-Squares*, 2020 ICML Workshop on Beyond First Order Methods in ML Systems; arXiv:2211.05727 (2022), Sections 2–4.
