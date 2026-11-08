# Log-periodic survival and conditioned transitions for slowly oscillating killed chains

## Finding

Let \(E\) be a finite nonempty state space, let \(K\) be a strictly positive substochastic matrix with spectral radius \(0<\lambda<1\), and let \(B\) be a fixed real matrix. Let \(f:\mathbb R\to\mathbb R\) be a real, continuously differentiable periodic function of period \(T>0\). For every sufficiently large integer \(n\), suppose the killed transition matrix is exactly
\[
K_n=K+\frac{f(\log n)}{n}B,
\]
and is strictly positive and substochastic. Arbitrary strictly positive substochastic matrices may be used at the finitely many earlier times.

Choose positive Perron eigenvectors \(KR=\lambda R\), \(LK=\lambda L\), normalized by \(LR=1\). Define
\[
Q(x,y)=\frac{K(x,y)R(y)}{\lambda R(x)},\qquad
\pi(x)=L(x)R(x),\qquad
A(x,y)=\frac{B(x,y)R(y)}{\lambda R(x)},
\]
\[
g=A\mathbf1,\quad \kappa=\pi g,\quad
(I-Q)u=g-\kappa\mathbf1,\quad \pi u=0.
\]
The finite, strictly positive stochastic matrix \(Q\) makes the Poisson equation uniquely solvable. Put
\[
\bar f=\frac1T\int_0^T f(s)\,ds,\qquad
\Psi(t)=\int_0^t(f(s)-\bar f)\,ds.
\]
Then \(\Psi\) is periodic of period \(T\).

**Survival law.** For every fixed starting time \(m\) and live state \(x\), there exists \(c_{m,x}>0\) such that, with \(\zeta\) the killing time,
\[
\boxed{\mathbb P_{m,x}(n<\zeta)
=\lambda^{n-m} n^{\kappa\bar f}e^{\kappa\Psi(\log n)}
 c_{m,x}\bigl(1+O(n^{-1})\bigr)}.
\]
The relative error refers to \(n\to\infty\) with \(m,x\) fixed. When \(\kappa\ne0\) and \(f\) is nonconstant, the positive survival sequence after removing its exponential factor is *not* regularly varying (in the ordinary Karamata sense): the periodic factor cannot be absorbed into a slowly varying multiplier.

**Conditioned transitions.** Conditioning on survival through time \(N\), then sending \(N\to\infty\), defines a Markov law on every fixed finite time horizon. If \(\widehat Q_n\) is its time-\(n\) transition matrix, then uniformly in \(x,y\),
\[
\boxed{\widehat Q_n(x,y)=Q(x,y)+\frac{f(\log n)}{n}
\left[A(x,y)+Q(x,y)\bigl(u(y)-u(x)-\kappa\bigr)\right]
+O(n^{-2}).}
\]
The first-order response is generally oscillatory even though \(K_n\to K\).

**An exact two-state witness.** Take
\[
K=\begin{pmatrix}1/2&1/4\\1/4&1/2\end{pmatrix},\quad
B=\begin{pmatrix}1/8&0\\0&0\end{pmatrix},\quad f(t)=\cos t,
\quad K_n=K+\frac{\cos(\log n)}n B\quad(n\ge1).
\]
Every \(K_n\) is strictly positive and substochastic. Here
\[
\lambda=3/4,\quad Q=\begin{pmatrix}2/3&1/3\\1/3&2/3\end{pmatrix},\quad
\kappa=1/12,\quad u=(1/8,-1/8),
\]
and the conditioned response matrix is exactly
\[
\boxed{C=\begin{pmatrix}1/9&-1/9\\1/18&-1/18\end{pmatrix}.}
\]
Thus every fixed starting state has
\[
\boxed{\mathbb P_{m,x}(n<\zeta)=(3/4)^{n-m}
 c_{m,x}\exp\!\bigl(\sin(\log n)/12\bigr)
 \bigl(1+O(n^{-1})\bigr).}
\]
The ratio to \((3/4)^{n-m}\) has different positive subsequential limits (their extreme ratio is \(e^{1/6}\)), while
\[
\widehat Q_n=Q+\frac{\cos(\log n)}n C+O(n^{-2}).
\]
Both periodic survival fluctuations and the nonzero conditional transition response are therefore realized in one irreducible two-state example, not merely by multiplying an entire transition kernel by a scalar.

## Assumptions and scope

The time index ranges over integers \(n\ge1\). Survival through \(n\) means survival of transitions at \(m,m+1,\ldots,n-1\). Every positive entry of \(K_n\) is a transition to a live state; the row deficit is the one-step killing probability. Strict positivity of \(K\) is imposed to obtain a simple Perron eigenvalue and a uniform mixing contraction; the theorem makes no claim for reducible or periodically supported kernels. The finite early-time kernels are assumed strictly positive and substochastic and only affect \(c_{m,x}\). The periodic profile is continuously differentiable, so both \(f\) and its derivative are bounded. The \(O(\cdot)\) constants can depend on the data and on the fixed starting pair, but the transition expansion is uniform over the finite state space.

The conclusion concerns long survival and its conditioned path law, rather than ordinary stationarity of the original killed process. It does not claim a central limit theorem, an expansion beyond first order for the transformed transitions, or an independent mathematical audit.

## Proof

**1. Perron normalization and a periodic clock.** With \(D_R\) the diagonal matrix of \(R\), conjugate the kernels to
\[
F_n=\lambda^{-1}D_R^{-1}K_nD_R
=Q+\frac{f(\log n)}n A.
\]
For the finitely many early times, use the analogous strictly positive matrices. Write \(s_n=n^{-\kappa\bar f}\exp(-\kappa\Psi(\log n))\). Because \(s_{n+1}/s_n=1-\kappa f(\log n)/n+O(n^{-2})\) and \(f(\log(n+1))/(n+1)=f(\log n)/n+O(n^{-2})\), the positive approximate harmonic vector
\[
\Phi_n(x)=s_n\left(1+\frac{f(\log n)}n u(x)\right)
\]
satisfies, for all sufficiently large \(n\),
\[
F_n\Phi_{n+1}=\Phi_n+O(s_n n^{-2})
\]
componentwise. Indeed, its relative first-order residual is \(f(\log n)(g-\kappa\mathbf1+Qu-u)/n=0\) by the Poisson equation.

**2. A genuinely harmonic function.** For integers \(N>n\), define
\[
h_n^{(N)}=F_nF_{n+1}\cdots F_{N-1}\Phi_N.
\]
All factors are positive. Since \(\Phi_n\) is positive and \(F_n\Phi_{n+1}/\Phi_n=1+O(n^{-2})\) componentwise, iterative comparison bounds all \(h_n^{(N)}/\Phi_n\) between \(\exp(-C/n)\) and \(\exp(C/n)\), uniformly for \(N>n\). The telescoping sum of residuals from \(N\) onward has relative size \(O(1/N)\), again by positivity and these bounds. Consequently \(h_n=\lim_{N\to\infty}h_n^{(N)}\) exists, is positive, and obeys
\[
h_n=F_nh_{n+1},\qquad h_n(x)=s_n(1+O(n^{-1})).
\]
The finitely many earlier values are defined by backward multiplication. The limit of the normalized products is unique with this asymptotic normalization.

**3. First-order spatial shape.** Put \(a_n=\pi h_n>0\) and \(w_n=h_n/a_n-\mathbf1\), so \(\pi w_n=0\). The bound from step 2 gives \(w_n=O(1/n)\). From \(h_n=F_nh_{n+1}\), taking the \(\pi\) component gives
\[
\frac{a_n}{a_{n+1}}=1+\frac{\kappa f(\log n)}n+O(n^{-2}).
\]
Subtracting that component gives, on the zero-mean subspace,
\[
w_n=Qw_{n+1}+\frac{f(\log n)}n(g-\kappa\mathbf1)+O(n^{-2}).
\]
Since \(Q\) is strictly positive, its restriction to \(\{v:\pi v=0\}\) has spectral radius less than one. Moreover \(f(\log(n+1))/(n+1)-f(\log n)/n=O(n^{-2})\). Subtract \(u f(\log n)/n\), iterate the resulting stable recurrence, and sum the geometrically decaying errors. This proves the sharper expansion
\[
\boxed{w_n(x)=\frac{f(\log n)}n u(x)+O(n^{-2}).}
\]
The displayed formula for \(\widehat Q_n\) follows by expanding
\[
\widehat Q_n(x,y)=F_n(x,y)\frac{h_{n+1}(y)}{h_n(x)}
\]
using the two preceding expansions. It is a stochastic kernel because \(F_nh_{n+1}=h_n\).

**4. Survival and finite-path conditioning.** A normalized row distribution propagated by \(F_n\) obeys the recursion \(p_{n+1}=p_nF_n/(p_nF_n\mathbf1)\). Since \(F_n=Q+O(1/n)\) and the strictly positive stochastic \(Q\) contracts probability rows, this recursion yields \(\|p_n-\pi\|=O(1/n)\) for each fixed initial row. Hence, for any fixed positive vector \(v\),
\[
F_m\cdots F_{n-1}v
=\frac{h_m}{s_n}\bigl(\pi v+O(n^{-1})\bigr),
\]
componentwise; replacing \(s_n\mathbf1\) by \(\Phi_n\) changes the terminal product by relative \(O(1/n)\), and the definition of \(h_m\) incurs another \(O(1/n)\). Set \(v(y)=1/R(y)\). From
\[
K_m\cdots K_{n-1}\mathbf1
=\lambda^{n-m}D_R F_m\cdots F_{n-1}(1/R),
\]
we obtain the survival formula with \(c_{m,x}=R(x)h_m(x)\pi[1/R]>0\). Dividing fixed-path survival probabilities by the same expression at time \(n\to\infty\) proves the finite-dimensional conditioned path law and its stated Doob kernel.

**5. Failure of ordinary regular variation.** For nonconstant \(f\), the periodic primitive \(\Psi\) is nonconstant. Choose \(t>0\) such that \(\Psi(z+\log t)-\Psi(z)\) is nonconstant as a function of the phase \(z\). Because \(\log n\) visits every phase modulo \(T\) along subsequences, the ratio of the survival sequence at \(\lfloor tn\rfloor\) and \(n\), after removing \(\lambda\)'s exponential factor and the appropriate power of \(t\), has at least two distinct subsequential limits whenever \(\kappa\ne0\). A regularly varying sequence has a unique such limit, proving the claim. This nonregular variation is a failure of the power-law-times-slowly-varying form, not a failure of the positive harmonic conditioning limit.

**6. Exact two-state computation.** For the stated matrices, \(R=\mathbf1\), \(\pi=(1/2,1/2)\), \(A=B/(3/4)\), and \(g=(1/6,0)\). Hence \(\kappa=1/12\) and the mean-zero Poisson solution is \(u=(1/8,-1/8)\). Substitution gives \(C_{00}=1/9\), \(C_{01}=-1/9\), \(C_{10}=1/18\), \(C_{11}=-1/18\). The profile \(f(t)=\cos t\) has \(\bar f=0\) and \(\Psi(t)=\sin t\), so the survival envelope has the stated form. The cosine and sine phases approach their extrema along integer subsequences of the form \(\lfloor\exp(2\pi j+\theta)\rfloor\), giving the exact limit-ratio factor \(e^{1/6}\).

## Verification

Run `python3 check.py` using Python's standard library. The program verifies the two-state Perron data, Poisson solution, response matrix, stochastic row sums, backward-harmonic finite-horizon approximation, and the convergence of normalized survival amplitudes. It prints `CHECKS_PASSED 63`. The finite computations are supplementary checks; they do not prove any infinite asymptotic. Every analytical step is supplied above.

## Relationship to prior work

Iba, *Finite-State Time-Inhomogeneous Markov Chains Conditioned to Survive* (2026), Theorems 1.2–1.3 and Proposition 2.10, treats a time-independent coefficient \(a/n+b/n^2+O(n^{-3})\). Such an expansion cannot represent a nonconstant \(f(\log n)/n\), so it does not directly yield the periodic survival multiplier or oscillatory first-order conditioned transition law established here. The constant-profile specialization is covered by Iba and is not claimed as new.

Champagnat and Villemonais (2018) establish general stability, limiting survival ratios, and time-inhomogeneous conditioned processes, but their Proposition 3.1 is not a calculation of this explicit periodic endpoint prefactor or the first-order response matrix. Oçafrain (2017) studies periodically moving absorbing sets rather than positive kernels tending to a common kernel with inverse-time log-periodic amplitude. Benzaid and Lutz (1987) provide broad asymptotic representation methods for perturbed linear difference systems: such matrix methods may imply portions of the leading survival formula, and priority of those portions is not settled by the accessible abstract. The specifically identified conditioned-kernel coefficient requires a separate probabilistic normalization calculation here.

No uniqueness of this result in all historical literature is asserted.

## Limitations

The general theorem assumes a finite, strictly positive limiting matrix, a continuously differentiable periodic profile, and a prescribed \(1/n\) perturbation. It does not cover general irreducible periodic kernels or arbitrary bounded oscillations with no differentiability. The leading survival modulation may be inferable from older linear-difference asymptotics; that historical-priority risk is material. A definitive comparison with the full 1987 Benzaid–Lutz paper was not available. No claims are made about independent formal certification, general stochastic modulation, or universal novelty beyond the literature comparisons described above.

## References

1. Kohki Iba, *Finite-State Time-Inhomogeneous Markov Chains Conditioned to Survive*, arXiv:2610.38590v1, first submitted 2026-10-28. https://arxiv.org/html/2610.38590v1
2. Nicolas Champagnat and Denis Villemonais, *Uniform convergence of penalized time-inhomogeneous Markov processes*, ESAIM Probability and Statistics 22 (2018), 129–162, arXiv:1603.07477. https://arxiv.org/abs/1603.07477
3. William Oçafrain, *Quasi-stationarity and quasi-ergodicity for discrete-time Markov chains with absorbing boundaries moving periodically*, arXiv:1707.08419 (2017). https://arxiv.org/abs/1707.08419
4. Z. Benzaid and D. A. Lutz, *Asymptotic Representation of Solutions of Perturbed Systems of Linear Difference Equations*, Studies in Applied Mathematics 77 (1987), 195–221, doi:10.1002/sapm1987773195. https://doi.org/10.1002/sapm1987773195
