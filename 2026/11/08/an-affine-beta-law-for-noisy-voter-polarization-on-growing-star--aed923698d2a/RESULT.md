# An affine beta law for noisy-voter polarization on growing star networks

## Finding
Let \(S_n=K_{1,n}\) be a star with one hub and \(n\ge2\) leaves. Consider the continuous-time noisy voter model with strictly positive spontaneous flip rate \(a\) and neighbor-copy rate \(h\) at each vertex. Under its unique stationary distribution, write \(H_n\in\{0,1\}\) for the hub state and \(F_n\) for the fraction of leaves in state one. Set
\[
\lambda=2a+h,\qquad u=\frac a\lambda,\qquad v=\frac{a+h}\lambda,\qquad
\alpha=\frac{2a(a+h)}{\lambda^2}.
\]
For every fixed \(a,h>0\), as \(n\to\infty\),
\[
(H_n,F_n)\ \Longrightarrow\ (H,u+(v-u)Y),
\qquad Y\sim\operatorname{Beta}(\alpha,\alpha),\qquad
\Pr(H=1\mid Y=y)=y.
\]
In particular \(0<\alpha<1/2\): the limiting leaf-fraction density is strictly U-shaped throughout the open interval \((u,v)\), without an interior Gaussian or point-mass limit at any fixed positive finite noise rate.

The finite-star stationary variance is also exact:
\[
\operatorname{Var}(F_n)=
\frac{8a(a+h)+h^2(n+1)}
{4\{8a(a+h)n+h^2(n+1)\}},
\qquad
\lim_{n\to\infty}\operatorname{Var}(F_n)
=\frac{h^2}{4[8a(a+h)+h^2]}>0.
\]
The nonzero limit is a persistent macroscopic polarization fluctuation produced by a single interacting hub, rather than a finite-sample noise effect.

## Assumptions and scope
The state of each vertex \(i\) is \(\eta_i\in\{0,1\}\). Its rates are
\[
0\to1:\ a+\frac h{\deg(i)}\sum_{j\sim i}\eta_j,\qquad
1\to0:\ a+\frac h{\deg(i)}\sum_{j\sim i}(1-\eta_j).
\]
All clocks are continuous-time exponential clocks, with rates as above. The parameters \(a,h\) are fixed, finite, and strictly positive as \(n\) grows. The model is irreducible on the finite state space, so its stationary distribution is unique. No claims are made at \(a=0\), \(h=0\), or when parameters scale with \(n\).

## Proof
**1. Exact lumped generator.** The pair \((H_n,K_n)\), where \(K_n=nF_n\), is Markov. Conditional on \((H_n,K_n)=(z,k)\), its transitions are
\[
\begin{aligned}
k\to k+1 &: (n-k)(a+hz),\\
k\to k-1 &: k(a+h(1-z)),\\
z=0\to1 &: a+hk/n,\\
z=1\to0 &: a+h(1-k/n).
\end{aligned}
\]
For continuously differentiable test functions of the leaf fraction, Taylor expansion of the birth-death part is uniform on the compact state space. Its generator converges to that of a piecewise-deterministic Markov process \((H_t,X_t)\) with drifts
\[
b_0(x)=a-\lambda x,\qquad b_1(x)=a+h-\lambda x
\]
and hub-switching rates \(q_{01}(x)=a+hx\) and \(q_{10}(x)=a+h(1-x)\). Compactness and the uniform generator convergence imply that every subsequential weak limit of the stationary finite-star distributions is stationary for this limiting process.

**2. Limiting joint stationary law.** Define \(y=(x-u)/(v-u)\); here \(v-u=h/\lambda\). Rescale time by \(\lambda\). The two deterministic velocities become \(-y\) and \(1-y\), and the dimensionless switching rates become
\[
\begin{aligned}
q_{01}(y)/\lambda&=\alpha+\beta y,\\
q_{10}(y)/\lambda&=\alpha+\beta(1-y),
\qquad\beta=\frac{h^2}{\lambda^2},\qquad 2\alpha+\beta=1.
\end{aligned}
\]
The interval \([0,1]\) is invariant. Outside this interval, the distance to it decreases at least exponentially along either flow; therefore every invariant distribution is supported on \([0,1]\). Every invariant distribution has no boundary atoms, because no deterministic trajectory from the interior reaches an endpoint in finite time and all hub-switching rates exceed a positive constant. It is absolutely continuous in the interior: conditional on at least one hub switch before time \(t\), the continuously distributed switching time is mapped with nonzero derivative to the final continuous coordinate, whereas the mass of no-switch paths is at most \(e^{-at}\). Let \(f_0,f_1\) be the two stationary interior densities.

Stationary conservation of total probability gives constant net current \(-yf_0+(1-y)f_1\). The zero boundary flux implies that this constant is zero. Consequently, for a nonnegative function \(g\),
\[
f_0(y)=\frac{g(y)}y,\qquad f_1(y)=\frac{g(y)}{1-y}.
\]
The stationarity equation for hub state zero becomes
\[
\frac{g'(y)}{g(y)}=\alpha\left(\frac1y-\frac1{1-y}\right),
\quad\text{hence}\quad g(y)=c\,y^\alpha(1-y)^\alpha.
\]
Normalizing \(f_0+f_1\) gives
\[
f_0(y)=\frac{(1-y)y^{\alpha-1}(1-y)^{\alpha-1}}{B(\alpha,\alpha)},\quad
f_1(y)=\frac{y\,y^{\alpha-1}(1-y)^{\alpha-1}}{B(\alpha,\alpha)}.
\]
This is the unique invariant probability measure: any invariant law must have densities satisfying these equations, and the normalized solution is unique. Hence every subsequential stationary limit coincides with it and the whole sequence converges. The conditional hub probability and the claimed affine beta marginal follow.

**3. Exact finite-size second moments.** Put \(\sigma_i=2\eta_i-1\). By symmetry every stationary single-spin mean vanishes. Let \(A_n=\mathbb E[\sigma_i\sigma_j]\) for two distinct leaves and \(C_n=\mathbb E[\sigma_0\sigma_i]\) for hub and leaf. Applying the finite generator to these products gives the exact linear equations
\[
(4a+2h)A_n=2hC_n,\qquad
(4a+2h)C_n=h\left(1+\frac{1+(n-1)A_n}{n}\right).
\]
Thus
\[
A_n=\frac{h^2(n+1)}{8a(a+h)n+h^2(n+1)},\qquad
C_n=\frac{h(2a+h)(n+1)}{8a(a+h)n+h^2(n+1)}.
\]
Since \(F_n=(n+\sum_{i=1}^n\sigma_i)/(2n)\), it follows that \(\operatorname{Var}(F_n)=[1+(n-1)A_n]/(4n)\), yielding the stated finite formula and its positive limit. Independently, the affine beta law gives \(\operatorname{Var}(X)=(h/\lambda)^2/[4(2\alpha+1)]\), which simplifies to the same limit. Finally \(2\alpha=1-h^2/\lambda^2\), proving \(0<\alpha<1/2\).

## Verification
Run \(`python verify_noisy_star.py`\) using Python with NumPy, SciPy, and SymPy. It checks the limiting stationary forward-equation cancellation and the exact moment identities symbolically, then independently constructs the complete \(2(n+1)\)-state generator and solves its stationary linear system for \(n=2,3,5,9,30,100\) at three distinct positive rate pairs. The direct stationary variances match the proved rational formula to within numerical linear-solve tolerance. Numerical calculations corroborate, but are not the proof of, the infinite-size law.

## Relationship to prior work
Cox, Peres and Steif (arXiv:1408.5122, 2014) explicitly analyze noisy-voter mixing on a star and its lumped hub-plus-leaf-count process. Their star result concerns mixing times, not this stationary affine-beta law or the exact leaf-fraction variance. Carro, Toral and San Miguel (arXiv:1602.06935, 2016) give an annealed approximation for heterogeneous networks and discuss noise-dependent finite-size polarization, but do not evaluate this exact star stationary law. Pymar and Rivera (arXiv:2112.01478, 2021) study Gaussian/Bernoulli limits for a degree-weighted density and explicitly note that their Gaussian star condition fails. Caligiuri and Galla (arXiv:2305.19096, 2023) treat voter populations with exogenously switching environmental parameters/influencers and derive PDMP stationary laws; their environmental switching dynamics differ from the endogenous hub rates \(a+hx\) and \(a+h(1-x)\). The derivation here needs that endogenous feedback and identifies its special beta cancellation.

## Limitations
This is an exact statement for fixed positive rates and the star family; it is not a general theory for arbitrary heterogeneous networks or for jointly vanishing noise. It does not establish a convergence rate of the full stationary distributions, nor any universality outside this model. Previously unpublished or unindexed equivalent specializations remain possible; originality has not undergone independent validation. The two-state PDMP technique itself is established in prior literature.

## References
1. J. T. Cox, Y. Peres, J. E. Steif, *Cutoff for the noisy voter model*, arXiv:1408.5122, first posted 2014-08-21. https://arxiv.org/abs/1408.5122
2. A. Carro, R. Toral, M. San Miguel, *The noisy voter model on complex networks*, arXiv:1602.06935, first posted 2016-02-22. https://arxiv.org/abs/1602.06935
3. R. Pymar, N. Rivera, *Asymptotic behaviour of the noisy voter model density process*, arXiv:2112.01478, first posted 2021-12-02. https://arxiv.org/abs/2112.01478
4. A. Caligiuri, T. Galla, *Noisy voter models in switching environments*, arXiv:2305.19096, first posted 2023-05-30. https://arxiv.org/abs/2305.19096
