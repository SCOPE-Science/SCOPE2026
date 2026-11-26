# Critical polynomial-tail selection and a logarithmic survival threshold for an absorbed birth–death walk

## Finding

For the absorbed homogeneous birth–death walk defined below, every critical-ratio initial law of the form \(m_i=C_\beta\rho^i i^{-\beta}\), with any fixed real \(\beta\le2\), selects the **minimal** quasi-stationary distribution in total variation. Its survival probability exhibits an explicit sharp three-regime exponent: \(t^{-(\beta+1)/2}\) for \(\beta<2\), \(t^{-3/2}\log t\) at \(\beta=2\), and the previously known \(t^{-3/2}\) for \(\beta>2\). Only the first two regimes and their selection claim are asserted as the new contribution; the last is included for comparison.

Precisely, let \(a>b>0\), \(\rho=\sqrt{b/a}\), \(c=2\sqrt{ab}\), \(\lambda=a+b-c\), and
\[
C_\beta=\biggl(\sum_{i=1}^\infty\rho^i i^{-\beta}\biggr)^{-1}.
\]
For fixed \(\beta<2\), define
\[
H_\beta(z)=\frac{2^{1-\beta/2}\Gamma(1-\beta/2)}{\sqrt{2\pi}}z^{-(\beta+1)/2},
\]
and for \(\beta=2\), define
\[
H_2(z)=\frac{\log z}{\sqrt{2\pi}\,z^{3/2}},\qquad z>1.
\]
Then for every fixed \(j\ge1\), as \(t\to\infty\),
\[
\mathbb P_{m}(X_t=j,T>t)\sim C_\beta j\rho^j H_\beta(ct)e^{-\lambda t},
\]
and, **with convergence of the entire mass function in \(\ell^1\)**,
\[
\mathbb P_{m}(T>t)\sim C_\beta\frac{\rho}{(1-\rho)^2}H_\beta(ct)e^{-\lambda t}.
\]
In particular,
\[
\lim_{t\to\infty}\left\|\mathcal L_m(X_t\mid T>t)-q^*\right\|_{\rm TV}=0,
\qquad q^*_j=(1-\rho)^2j\rho^{j-1}.
\]
The normalization \(H_\beta(ct)\) explicitly includes the time scale \(c\); the displayed constants are exact.

## Assumptions and scope

The state space is \(\{0,1,2,\ldots\}\). From each positive state \(i\), the continuous-time process jumps to \(i+1\) at constant rate \(b\) and to \(i-1\) at constant rate \(a\); state \(0\) is absorbing, and \(T\) is its first hitting time. The rates are arbitrary fixed real numbers \(a>b>0\). The initial distribution \(m\) is supported on the positive integers and has the exact probability masses \(C_\beta\rho^i i^{-\beta}\). Every real \(\beta\le2\) is allowed; no finite weighted initial moment is assumed. The convergence and constants are for \(t\to\infty\) with \(a,b,\beta\) fixed. The result does not claim a uniform rate as parameters vary, or a classification of all initial laws with tail ratio \(\rho\).

## Proof

**1. Exact reduction to a symmetric killed heat kernel.** Let \(z=ct\) and \(k_z(n)=e^{-z}I_{|n|}(z)\), where \(I_n\) is the modified Bessel function. Thus \(k_z(n)\) is the mass function of a continuous-time simple symmetric walk on \(\mathbb Z\) whose total jump rate is \(c\). The method of images and diagonal similarity give the exact absorbed transition kernel
\[
p_{ij}(t)=e^{-\lambda t}\rho^{j-i}K_z(i,j),\qquad
K_z(i,j)=k_z(i-j)-k_z(i+j)\quad(i,j\ge1).
\]
This identity also follows directly by checking the initial condition, the birth–death forward equations and the absorbing boundary. Consequently,
\[
e^{\lambda t}\mathbb P_m(X_t=j,T>t)
=C_\beta\rho^jF_{\beta,z}(j),\qquad
F_{\beta,z}(j)=\sum_{i\ge1}i^{-\beta}K_z(i,j).
\]

**2. A local heat-kernel estimate with a uniform tail bound.** The Fourier representation is
\[
k_z(n)=\frac1{2\pi}\int_{-\pi}^{\pi}e^{-z(1-\cos\theta)}e^{-in\theta}\,d\theta.
\]
Rescale \(\theta\) by \(z^{-1/2}\), bound the complement of a neighborhood of zero using \(1-\cos\theta\gtrsim\theta^2\), and apply dominated convergence. Uniformly for \(|n|\le R\sqrt z\) with any fixed \(R\),
\[
k_z(n)=\frac1{\sqrt{2\pi z}}e^{-n^2/(2z)}+o_R(z^{-1/2}).
\]
An explicit global bound is also needed. Exponentially tilting the Fourier integral by \(\theta>0\) gives
\[
k_z(n)\le \frac{C}{\sqrt{z\cosh\theta}}
\exp\{z(\cosh\theta-1)-\theta|n|\},\qquad z\ge1.
\]
To see the prefactor, the absolute value of the tilted integral is at most \((2\pi)^{-1}\int e^{-z\cosh\theta(1-\cos u)}du\le C(z\cosh\theta)^{-1/2}\). Take \(\theta=\min(|n|/(2z),1)\); since \(\cosh\theta-1\le(\cosh1-1)\theta^2\) for \(0\le\theta\le1\), there exist absolute \(A,\eta>0\) such that
\[
0\le k_z(n)\le \frac{A}{\sqrt z}
\exp\{-\eta\min(n^2/z,|n|)\},\qquad z\ge1.
\]
These are local-limit and tail estimates proved directly from the exact Fourier integral, not extrapolations from finite experiments.

**3. The reflected-kernel first difference.** The Bessel recurrence \(I_{n-1}(z)-I_{n+1}(z)=2nI_n(z)/z\) telescopes to the exact identity
\[
K_z(i,j)=\frac2z\sum_{h=0}^{\min(i,j)-1}
\bigl(|i-j|+2h+1\bigr)k_z\bigl(|i-j|+2h+1\bigr).
\]
The coefficients in this sum add to \(ij\). It follows from the preceding heat-kernel bounds that
\[
0\le K_z(i,j)\le \frac{A'ij}{z^{3/2}}
\exp\{-\eta'\min((i-j)^2/z,|i-j|)\}.
\]
For each fixed \(L>0\), the same identity and Gaussian local limit yield, uniformly for integers \(1\le j\le L\log z\), after summation against \(i^{-\beta}\),
\[
F_{\beta,z}(j)\sim
\frac{2j}{\sqrt{2\pi}\,z^{3/2}}
\sum_{i\ge1}i^{1-\beta}e^{-i^2/(2z)}.
\tag{1}
\]
Here are the necessary uniformity details. Split the \(i\)-sum into \(i\le2L\log z\), \(2L\log z<i\le R\sqrt z\), and \(i>R\sqrt z\). The first is bounded by \(A'jz^{-3/2}\sum_{i\le2L\log z}i^{1-\beta}\), negligible relative to the right-hand side of (1), for each fixed \(\beta<2\), and of order \(jz^{-3/2}\log\log z\) if \(\beta=2\). On the middle range the coefficient indices differ from \(i\) by at most \(j\), and the local-limit formula applies uniformly. For \(\beta<2\), the remaining contribution above \(R\sqrt z\), divided by \(jz^{-(\beta+1)/2}\), is bounded by a constant times \(\int_R^\infty x^{1-\beta}e^{-\eta'x^2}dx+o(1)\), which vanishes as \(R\to\infty\); the part above \(z\) decays exponentially. For \(\beta=2\), the contribution above \(R\sqrt z\) is \(O_R(jz^{-3/2})\) and is negligible beside the logarithmic main term. At \(\beta=2\), to recover its full coefficient rather than only a comparison, use the subrange \(2L\log z<i\le\sqrt z/\log z\), where \(k_z(i+O(j))=(1+o(1))/\sqrt{2\pi z}\) uniformly, and the harmonic sum is \((\tfrac12+o(1))\log z\); the omitted intermediate range contributes at most \(O(jz^{-3/2}\log\log z)\). This establishes (1) for every fixed \(\beta\le2\).

**4. Critical exponents and exact constants.** For \(\beta<2\), an ordinary Riemann sum and Gaussian tail domination give
\[
\sum_{i\ge1}i^{1-\beta}e^{-i^2/(2z)}
\sim 2^{-\beta/2}\Gamma(1-\beta/2)z^{1-\beta/2}.
\]
At the borderline \(\beta=2\), direct comparison with the harmonic series gives
\[
\sum_{i\ge1}\frac{e^{-i^2/(2z)}}i\sim\tfrac12\log z.
\]
Substituting into (1) proves \(F_{\beta,z}(j)\sim jH_\beta(z)\), uniformly for \(1\le j\le L\log z\), with precisely the announced constants. Combined with Step 1 this proves the fixed-\(j\) joint-mass statement.

**5. Control of the infinitely many target states.** The symmetric reflected kernel has the probabilistic interpretation \(F_{\beta,z}(j)=\mathbb E_j[S_z^{-\beta};\tau_0>z]\), where \(S\) is the symmetric walk of total rate one, evaluated at time \(z\), and \(\tau_0\) its hitting time of zero. If \(\beta\ge0\), then \(0\le F_{\beta,z}(j)\le1\). If \(\beta<0\), each path has \(S_z\le j+N_z\), where \(N_z\) is Poisson with mean \(z\); hence \(F_{\beta,z}(j)\le\mathbb E(j+N_z)^{-\beta}\le B_\beta(j+z+1)^{-\beta}\). For any fixed \(\beta\le2\), choose \(L\) so large that the geometric tail \(\sum_{j>L\log z}\rho^jF_{\beta,z}(j)\) is \(o(H_\beta(z))\). On the remaining \(j\)'s Step 4 holds uniformly. Thus
\[
\sum_{j\ge1}\left|\frac{e^{\lambda t}\mathbb P_m(X_t=j,T>t)}{C_\beta H_\beta(ct)}-j\rho^j\right|\longrightarrow0.
\]
Finally \(\sum_{j\ge1}j\rho^j=\rho/(1-\rho)^2\). Summation yields the stated survival equivalent, and normalization gives total-variation convergence to \(q^*\). This proves every claim.

## Verification

The standalone `check_critical_tail.py` performs two independent finite-time kernel reconstructions: Poissonization of exact reflected binomial path counts, and a truncated generator matrix exponential. It also verifies the modified-Bessel telescoping identity and the exact minimal-QSD harmonic identity in finite truncations. On the recorded numerical environment it passed **1,262 numerical and combinatorial assertions**. Leading-order ratios were printed for representative values of \(\beta\) and increasing \(t\). These checks test the normalization and formulas; the infinite-time theorem is proved analytically in Steps 1–5, not inferred from the finite computations. Run `python check_critical_tail.py` with Python, NumPy and SciPy.

## Relationship to prior work

Pollett's November 2026 paper [1] gives the complete QSD family, the fixed-transition Bessel kernel, a nonminimal-domain theorem for \(r>\rho\), and a minimal-domain sufficient moment condition. Its Remark 4.2 and Section 7 explicitly identify \(m_i\propto\rho^i i^{-\beta}\) and establish \(\beta>2\), while leaving the divergent-moment critical regime unresolved. The new claim addresses exactly \(\beta\le2\), with exact asymptotic prefactors and total-variation selection; it does not reclaim the known kernel or the \(\beta>2\) result.

Pollett's earlier spectral-edge paper [2] proves fixed-state transition asymptotics, which cannot directly be interchanged with the infinite initial-state sum in the critical regime: the dominant starting sites have order \(\sqrt{t}\). Brownian half-line drift results [3,4] are related continuous-state analogues, but do not imply the lattice-specific constants or the stated countable-state \(\ell^1\) limit without a new uniform kernel argument. Earlier classical finite-support birth–death results [5] do not cover this infinite-support critical class.

## Limitations

The initial law is exactly proportional to \(\rho^i i^{-\beta}\); general slowly varying or oscillating critical factors, a full necessary-and-sufficient domain criterion, and variable birth/death rates are not addressed. No uniformity in \(a\), \(b\), or \(\beta\) is asserted. Numerical checks are finite and do not certify an asymptotic theorem. Accessible bibliographic comparisons support novelty relative to inspected statements; comprehensive historical priority and independent validation have not been established.

## References

1. Phil. Pollett, *Domains of attraction of quasi-stationary distributions for an absorbed random walk*, arXiv:2611.17791v1, first posted 2026-11-13. https://arxiv.org/html/2611.17791v1
2. Phil Pollett, *Polynomial Decay in Absorbing Continuous-Time Markov Chains*, arXiv:2609.27335, first posted 2026-09-23. https://arxiv.org/html/2609.27335v2
3. SangJoon Lee and Iddo Ben-Ari, *Quasi-Limiting Behavior of Drifted Brownian Motion*, arXiv:2001.04523 (2020). https://arxiv.org/abs/2001.04523
4. S. Martínez, P. Picco and J. San Martín, *Domain of attraction of quasi-stationary distributions for the Brownian motion with drift*, Advances in Applied Probability 30 (1998), 385–408. https://doi.org/10.1239/aap/1035228075
5. E. A. van Doorn, *Quasi-stationary distributions and convergence to quasi-stationarity of birth and death processes*, Advances in Applied Probability 23 (1991), 683–700. https://doi.org/10.2307/1427670
