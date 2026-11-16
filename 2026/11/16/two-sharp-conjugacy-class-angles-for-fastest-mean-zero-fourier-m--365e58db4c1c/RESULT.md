# Two sharp conjugacy-class angles for fastest mean-zero Fourier mixing on \(\mathrm{SU}(2)\)

## Finding
Let \(G=\mathrm{SU}(2)\), with normalized Haar measure. For \(0\leq\theta\leq\pi\), let \(\mu_\theta\) be the conjugation-invariant probability measure uniformly distributed on the conjugacy class with eigenvalues \(e^{i\theta}\) and \(e^{-i\theta}\). Write \(T_\theta f(x)=\int_G f(xg)\,d\mu_\theta(g)\), acting on the mean-zero space \(L^2_0(G)\). Then
\[
\min_{0\leq\theta\leq\pi}\|T_\theta\|_{L^2_0\to L^2_0}=\frac14.
\]
The **only** two minimizing angles are
\[
\theta_+=\arccos(1/4),\qquad\theta_-=\arccos(-1/4)=\pi-\theta_+.
\]
At either angle, precisely the irreducible representations of highest weights \(m=1,2\) realize the extremal multiplier magnitude \(1/4\): their multipliers are respectively \(\pm 1/4\) and \(-1/4\). The corresponding Fourier matrix-coefficient dimensions are \(4\) and \(9\). Every highest weight \(m\ge3\) has strictly smaller multiplier magnitude. Moreover, for every integer \(k\ge1\),
\[
\min_{\theta}\|T_\theta^k\|_{L^2_0\to L^2_0}=4^{-k},
\]
with exactly the same two minimizers.

## Assumptions and scope
The sampling law is a **single** fixed conjugacy class, with its natural conjugation-invariant probability distribution. It is not a law supported on finitely many group elements, not a mixture of two or more angles, and not a constraint on total variation convergence from a point mass. The operator norm uses normalized Haar \(L^2\), restricted to the orthogonal complement of constant functions; no trigonometric-polynomial bandwidth cutoff is imposed. The two minimizing angles represent distinct classes of \(\mathrm{SU}(2)\), exchanged by multiplication by its central element \(-I\).

## Proof
Every irreducible representation of \(\mathrm{SU}(2)\) is indexed by a nonnegative integer highest weight \(m\), with dimension \(m+1\). For \(0<\theta<\pi\), the classical character formula is
\[
\chi_m(\theta)=\frac{\sin((m+1)\theta)}{\sin\theta}=U_m(\cos\theta),
\]
where \(U_m\) is the second-kind Chebyshev polynomial. Centrality of \(\mu_\theta\) and Schur's lemma make its Fourier transform on that representation scalar, with multiplier
\[
\lambda_m(\theta)=\frac{\chi_m(\theta)}{m+1}.
\]
Peter--Weyl decomposes \(L^2_0(G)\) into all \(m\ge1\) matrix-coefficient sectors. Therefore
\[
\rho(\theta):=\|T_\theta\|_{L^2_0\to L^2_0}
=\sup_{m\ge1}|\lambda_m(\theta)|.
\]
At the endpoints \(\theta=0,\pi\), the class measures are point masses at central elements and \(\rho=1\).

Put \(c=\cos\theta\) and \(t=|c|\). The first two nonconstant multipliers are
\[
\lambda_1=c,\qquad\lambda_2=\frac{4c^2-1}{3}.
\]
Thus \(\rho(\theta)\ge\max\{t,|4t^2-1|/3\}\). If \(t>1/4\), the first term is greater than \(1/4\). If \(0\le t<1/4\), the second term is \((1-4t^2)/3>1/4\). Consequently any minimizing angle must have \(t=1/4\), and the best possible value is at least \(1/4\).

At \(c=\pm1/4\), the first two multipliers have magnitude exactly \(1/4\). The next multiplier is
\[
\lambda_3=2c^3-c,\qquad|\lambda_3|=\frac7{32}<\frac14.
\]
For every \(m\ge4\), the character formula gives the **uniform infinite-tail bound**
\[
|\lambda_m|\le\frac1{(m+1)|\sin\theta|}
\le\frac4{5\sqrt{15}}<\frac14,
\]
using \(|\sin\theta|=\sqrt{15}/4\). This proves attainment, the exact value, the exclusivity of the two angles, and the complete equality sectors. The matrix-coefficient subspace of dimension \((m+1)^2\) has eigenvalue \(\lambda_m\), giving dimensions \(4\) and \(9\).

Since each \(\lambda_m\) is real and the central convolution operator is self-adjoint, \(\|T_\theta^k\|=\rho(\theta)^k\). The power statement follows by strict monotonicity of the function \(u\mapsto u^k\) on nonnegative reals. Finally \(U_m(-c)=(-1)^mU_m(c)\) shows that multiplication by \(-I\) preserves the norm while exchanging the signs of all odd-weight multipliers.

## Verification
The standalone file `checker.py` evaluates normalized characters directly, tests both optimal angles through highest weight \(25000\), checks the two low-weight equality sectors, validates the center-parity identity through weight \(1499\), checks the sharp lower bound on a thousand-point angle grid, and checks powers. Execute `python3 checker.py` in the directory containing the file. The checker reports `PASS 3523 checks`. The infinite-tail inequality and uniqueness are analytical; no finite scan is used to certify infinitely many weights or an uncountable angle interval.

## Relationship to prior work
Borda (arXiv:2110.00295, first version 2021-10-01), especially Section 5.1, treats operator spectral gaps and harmonic analysis on compact Lie groups in connection with quantitative random-walk convergence. It does not state a fixed-single-conjugacy-class optimization over \(\mathrm{SU}(2)\) angles. Manack (arXiv:1309.2750; 2014) studies normalized-character bounds on **adjoint simple (centerless)** Lie groups, rather than a sharp single-class minimax on \(\mathrm{SU}(2)\); its main hypotheses exclude this nontrivial-center group. The standard \(\mathrm{SU}(2)\) Weyl character formula and Peter--Weyl theory are established background and are not asserted as new.

The spin-one-half sector \(m=1\) is absent from Fourier analysis on the quotient \(\mathrm{SO}(3)\). Consequently a fixed-class optimizer for the quotient cannot imply this result: the objective functions optimize over different collections of representations. This work's claim is the sharp \(\mathrm{SU}(2)\) single-class minimax and full equality classification, not a general compact-group spectral-gap theorem.

## Limitations
Historical priority has not been independently certified. Earlier specialized sharp class-walk optimizations have not been exhaustively ruled out; bibliographic uniqueness is not asserted. Nothing is proved about arbitrary central measures, mixtures of conjugacy classes, noncentral steps, finitely supported approximations to the class distribution, total variation after an individual step, or other \(L^p\) operator norms. The numerical checks are supplemental to the complete analytical proof.

## References
1. B. Borda, *Empirical measures and random walks on compact spaces in the quadratic Wasserstein metric*, arXiv:2110.00295, first public version 2021-10-01, https://arxiv.org/abs/2110.00295 , Section 5.1.
2. C. Manack, *Character estimates of adjoint simple Lie groups*, Journal of Group Theory 17 (2014), 833–850, https://doi.org/10.1515/jgt-2014-0008 .
3. T. Leaser, *Fourier Analysis on SU(2)*, M.S. thesis, East Carolina University, 2012, https://thescholarship.ecu.edu/items/283b8e6c-3ab9-4cdb-bf29-d6afd4208b71 .
