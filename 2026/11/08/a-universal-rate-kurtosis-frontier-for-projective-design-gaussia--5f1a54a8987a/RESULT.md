# A universal rate–kurtosis frontier for projective-design Gaussian samplers

## Finding
Let a fresh rank-one orthogonal projector in the plane be drawn at every step from a projective second-moment design as defined below. For a calibrated random-projection affine iteration with independent isotropic Gaussian innovations, every stationary one-dimensional marginal has the correct target variance, yet has the **exact positive excess kurtosis**
\[
\kappa=\frac{3\eta(2-\eta)}{8-3\eta(2-\eta)}
       =\frac{3(1-\rho)}{1+3\rho},
\qquad \rho=1-\eta+\frac{\eta^2}{2}.
\]
This universal law is independent of the number or orientations of design directions. The exact synchronous mean-square difference contracts by \(\rho\) per iteration; hence \(1/2\le\rho<1\). The fastest choice \(\eta=1\) uniquely maximizes the non-Gaussian deviation, giving \(\rho=1/2\) and \(\kappa=3/5\). All stationary laws in the stated nondegenerate range are non-Gaussian, despite having exactly the desired covariance.

## Assumptions and scope
Work in the Euclidean plane. A random matrix \(P\) is a rank-one orthogonal projector, selected independently and identically at every iteration, satisfying for every \(u\in\mathbb R^2\)
\[
\mathbb E P=\tfrac12 I_2,\qquad
\mathbb E(u^{\mathsf T}Pu)^2=\tfrac38\|u\|^4.
\]
These two identities define the required projective second-moment design; they hold for the uniform distribution on three projectors whose lines are separated by \(60^\circ\), including the three pair-difference directions of a three-particle complete graph. They also hold for a uniform random line. Let \(0<\eta<2\), \(s>0\), and write \(b=\eta(2-\eta)\), \(\rho=1-b/2\), and \(q=(1-\rho)s\). Define
\[
X_{n+1}=(I_2-\eta P_n)X_n+\xi_n,
\qquad \xi_n\stackrel{\rm iid}{\sim}N(0,qI_2),
\]
with all projectors and innovations mutually independent and independent of the starting state. The target covariance is \(sI_2\). The finding concerns a discrete randomized projector sampler and its stationary moments, not an exact simulation of a given continuous-time diffusion.

## Proof
**1. Design identities.** Since \(P^2=P\), for \(A=I_2-\eta P\) we have \(A^{\mathsf T}A=I_2-bP\). Consequently for every deterministic \(u\),
\[
\mathbb E\|Au\|^2=\rho\|u\|^2,
\qquad
\mathbb E\|Au\|^4=t_4\|u\|^4,
\qquad t_4=1-b+\tfrac38 b^2.
\]
Here \(0<b\le1\), so \(0<\rho<1\) and \(0<t_4<1\). The nontrivial quartic identity follows by expanding \((\|u\|^2-bu^{\mathsf T}Pu)^2\) and using both design moments.

**2. Existence, uniqueness and exact coupled decay.** Couple two copies with the same \(P_n,\xi_n\). Conditional on their current difference \(D_n\),
\[
\mathbb E(\|D_{n+1}\|^2\mid D_n)=\rho\|D_n\|^2,
\quad\text{hence}\quad
\mathbb E\|D_n\|^2=\rho^n\|D_0\|^2.
\]
The Markov transition therefore contracts \(W_2\) by at most \(\sqrt\rho\), giving a unique invariant probability with finite second moment. The identity
\[
\mathbb E(\|X_{n+1}\|^4\mid X_n=x)
=t_4\|x\|^4+8q\rho\|x\|^2+8q^2
\]
provides a fourth-moment drift bound. In particular the invariant law has finite fourth moment. The additive noise is nondegenerate and centered; the invariant mean is zero. Its covariance is \(sI_2\), since that matrix solves the covariance fixed-point equation
\[
C=\mathbb E[(I_2-\eta P)C(I_2-\eta P)]+qI_2
\]
and uniqueness follows from the same contraction.

**3. Exact directional fourth moments.** For any homogeneous quartic polynomial \(F(u)\), define \((\mathcal TF)(u)=\mathbb E F(Au)\). In the norm \(\sup_{\|u\|=1}|F(u)|\), the design identity gives \(\|\mathcal T\|\le t_4<1\). Let \(M(u)=\mathbb E(u^{\mathsf T}X)^4\) for an invariant \(X\). Gaussian conditioning and the known covariance yield
\[
M(u)=(\mathcal TM)(u)+[6q\rho s+3q^2]\|u\|^4.
\]
The invariant radial quartic \(M(u)=m\|u\|^4\) is the **unique** solution because \(\mathcal T\) strictly contracts quartics. Solving gives
\[
m=\frac{3s^2(1-\rho^2)}{1-t_4}
  =3s^2\frac{8-2b}{8-3b}.
\]
For a unit vector \(u\), the variance of \(u^{\mathsf T}X\) equals \(s\), and thus the fourth cumulant and standardized excess kurtosis are
\[
\operatorname{cum}_4(u^{\mathsf T}X)=\frac{3s^2b}{8-3b}>0,
\qquad \kappa=\frac{3b}{8-3b}.
\]
Every unit direction has the same strictly positive fourth cumulant; hence the invariant law is non-Gaussian. Also \(\mathbb E\|X\|^4=(8/3)m=8s^2(8-2b)/(8-3b)\), whereas the target Gaussian has radial fourth moment \(8s^2\).

**4. Sharp tradeoff.** Since \(b=1-(\eta-1)^2\), the possible rates are exactly \(\rho\in[1/2,1)\). Eliminating \(b=2(1-\rho)\) gives
\[
\kappa=\frac{3(1-\rho)}{1+3\rho},
\]
strictly decreasing in \(\rho\). Thus the unique fastest stepsize \(\eta=1\) has the maximum excess kurtosis \(3/5\), while making the stationary law closer to Gaussian in fourth moment requires a slower synchronous mean-square contraction. This claim does **not** identify the total-variation mixing rate or optimize computational cost.

**5. Three-particle realization.** On the centered subspace \(H=\{x\in\mathbb R^3:x_1+x_2+x_3=0\}\), choose one of the three unordered pairs \(\{i,j\}\) uniformly, and set \(P_{ij}=(e_i-e_j)(e_i-e_j)^{\mathsf T}/2\). The identities \(\sum_{i<j}(x_i-x_j)^2=3\|x\|^2\) and \(\sum_{i<j}(x_i-x_j)^4=(9/2)\|x\|^4\) on \(H\) establish both design properties upon identifying \(H\) isometrically with \(\mathbb R^2\). Calibrated isotropic Gaussian innovations in \(H\) therefore obey the same complete law. For \(s=1,\eta=1\), \(\rho=1/2\), every unit marginal has fourth moment \(18/5\), and \(\mathbb E\|X\|^4=48/5\), compared with \(3\) and \(8\) for the corresponding Gaussian target.

## Verification
Run `python verify.py` with Python 3 and SymPy. The checker expands the three pair projectors in exact rational coordinates on \(H\), verifies both second- and fourth-order design identities symbolically for arbitrary centered vectors and arbitrary \(\eta\), verifies the stationary moment equations and Pareto identity, and tests 21 exact-rational parameter/covariance regimes. Its recorded output is in `verify_output.txt`. The infinite-dimensional ranges of \(\eta\) and \(u\), existence of the invariant law, and uniqueness of the quartic fixed point are certified by the proof above, not by the finite test grid.

## Relationship to prior work
Random-batch interaction methods and invariant-measure approximation are developed by Jin and Li (2021), Jin, Li, Ye and Zhou (2022), and Ye and Zhou (2022). Those works principally establish general stochastic-particle algorithms, ergodicity and error bounds, rather than the exact directional stationary fourth moment of this calibrated planar projector model. Ślęzak, Burnecki and Metzler (2019) already derive stationary fourth moments in **scalar** random-coefficient autoregressions and discuss non-Gaussianity with Gaussian driving noise; that general mechanism is prior art. Grønbech-Jensen (2023) analyzes fourth-moment errors due to **non-Gaussian innovations** in a different Langevin discretization. The specific all-projective-design identity and exact rate–kurtosis frontier are not stated in those inspected treatments. A multivariate random-coefficient moment formula elsewhere could imply this specialization; that remains a publication-precedence risk.

## Limitations
This result assumes independent projector draws, an exact projective second-moment design in dimension two, centered independent **Gaussian** innovations with covariance calibrated as above, and \(0<\eta<2\). It does not cover anisotropic covariance targets, higher-dimensional projective designs, correlated batch selection, fixed uncalibrated noise variance, nonlinear interactions, or a specific continuous-time SDE discretization error. The critical endpoints \(\eta=0,2\) are excluded and do not have the asserted contractive invariant law. The synchronous coupling factor is not asserted to be the sharp convergence factor in every probability metric. Independent mathematical validation and broader publication-precedence review have not been performed.

## References
1. J. Ślęzak, K. Burnecki, R. Metzler, *Random coefficient autoregressive processes describe Brownian yet non-Gaussian diffusion in heterogeneous systems*, arXiv:1904.08737, first posted 2019-04-18, https://arxiv.org/abs/1904.08737.
2. S. Jin and L. Li, *Random Batch Methods for classical and quantum interacting particle systems and statistical samplings*, arXiv:2104.04337, first posted 2021-04-09, https://arxiv.org/abs/2104.04337.
3. S. Jin, L. Li, X. Ye and Z. Zhou, *Ergodicity and long-time behavior of the Random Batch Method for interacting particle systems*, arXiv:2202.04952, first posted 2022-02-10, https://arxiv.org/abs/2202.04952.
4. X. Ye and Z. Zhou, *Error Analysis of Time-Discrete Random Batch Method for Interacting Particle Systems and Associated Mean-Field Limits*, arXiv:2206.02166, first posted 2022-06-05, https://arxiv.org/abs/2206.02166.
5. N. Grønbech-Jensen, *On the Application of Non-Gaussian Noise in Stochastic Langevin Simulations*, arXiv:2301.04821, first posted 2023-01-12, https://arxiv.org/abs/2301.04821.
