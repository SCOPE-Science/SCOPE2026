# A sharp Gaussian trajectory-error law for random-order Lie splitting

## Finding

Let \(d\ge 1\), let \(A,B\in\mathbb R^{d\times d}\) be fixed, and let \(T>0\). At each of \(n\) steps independently choose, with equal probability, the forward or reversed first-order Lie product for the matrix equation \(\dot y=(A+B)y\). Write \(h=T/n\), \(C=A+B\), and \(K=AB-BA\), and define
\[
M_+(h)=e^{hA}e^{hB},\qquad M_-(h)=e^{hB}e^{hA},\qquad
P_n=M_{\varepsilon_n}(h)\cdots M_{\varepsilon_1}(h),
\]
where the \(\varepsilon_j\) are independent, equally likely signs. Then the *trajectory-level* error, regarded as a random real matrix, obeys
\[
h^{-3/2}\bigl(P_n-e^{TC}\bigr)\ \Longrightarrow\
\mathcal G_T:=\frac12\int_0^T e^{(T-s)C}K e^{sC}\,dW_s,
\]
where \(W\) is a standard real Brownian motion and the integral is understood entrywise. Its (possibly singular) matrix-vectorized covariance is
\[
\operatorname{Cov}(\operatorname{vec}\mathcal G_T)
=\frac14\int_0^T\operatorname{vec}(G(s))\operatorname{vec}(G(s))^{\mathsf T}\,ds,
\qquad G(s)=e^{(T-s)C}Ke^{sC}.
\]
Moreover, with the Frobenius norm,
\[
\boxed{\lim_{n\to\infty}h^{-3}\mathbb E\|P_n-e^{TC}\|_F^2
=\frac14\int_0^T\|e^{(T-s)C}Ke^{sC}\|_F^2\,ds.}
\]
The constant is strictly positive **if and only if** \(AB\ne BA\). When \(AB=BA\), every realization is exact for every \(n\). In contrast, even without commutation the mean propagation matrix has second-order accuracy:
\[
\|\mathbb E P_n-e^{TC}\|_F=O(h^2).
\]
Thus mean propagation and typical individual trajectories have different asymptotic accuracies. For the harmonic-oscillator shear splitting
\[
A=\begin{pmatrix}0&1\\0&0\end{pmatrix},\quad
B=\begin{pmatrix}0&0\\-1&0\end{pmatrix},\quad T=1,
\]
the sharp risk constant is \(1/2\):
\[
\lim_{n\to\infty}n^3\mathbb E\|P_n-e^{A+B}\|_F^2=\frac12.
\]

## Assumptions and scope

All matrices are finite-dimensional, fixed real matrices. There is no stability, dissipativity, self-adjointness, or commutation assumption. Time \(T\) is fixed while \(n\to\infty\); the independent unbiased sign is redrawn at every step. Exact matrix exponentials are used. The limit concerns the **random product** itself in the ordinary Frobenius norm, not the ensemble-averaged quantum channel, expectation of a matrix, an approximation of a partial differential equation, or a long-time limit with \(T\to\infty\). The matrix Gaussian may be degenerate and is not claimed to have independent entries.

## Proof

**Step 1: local commutator expansion.** With \(E(h)=e^{hC}\), Taylor multiplication in any submultiplicative norm yields, uniformly for the two signs,
\[
M_\varepsilon(h)=E(h)+\frac{\varepsilon h^2}{2}K+R_\varepsilon(h),
\qquad \|R_\varepsilon(h)\|_F\le c h^3
\]
for \(0<h\le h_0\). Indeed, the coefficient of \(h^2\) in the forward product is \(A^2/2+AB+B^2/2\), whereas the coefficient in \(e^{hC}\) is \((A^2+AB+BA+B^2)/2\); reversal changes the sign of the difference.

**Step 2: a uniform first-order product expansion.** Set \(D_j=M_{\varepsilon_j}(h)-E(h)\). The finite noncommutative product expansion, choosing either \(E\) or \(D_j\) at each index, gives
\[
P_n-E(h)^n=\sum_{j=1}^n E(h)^{n-j}D_jE(h)^{j-1}
+\sum_{\text{terms with at least two }D\text{'s}}\!\text{term}.
\]
Because \(\|D_j\|\le c_1h^2\), \(nh=T\), and the intervening powers of \(E\) are uniformly bounded, the sum of all terms with at least two perturbations is bounded by \(c_2n^2h^4e^{c_3nh^2}=O(h^2)\), **uniformly in all sign choices**. Inserting Step 1 into the single-perturbation sum adds at most \(O(nh^3)=O(h^2)\). Consequently,
\[
P_n-e^{TC}=\frac{h^2}{2}\sum_{j=1}^n\varepsilon_j
 e^{(n-j)hC}K e^{(j-1)hC}+\mathcal R_n,
\qquad\sup_{\varepsilon_1,\ldots,\varepsilon_n}\|\mathcal R_n\|_F=O(h^2).
\]
The bound applies to nonsymmetric and nonnormal matrices and is not a probabilistic heuristic.

**Step 3: Gaussian limit.** Dividing by \(h^{3/2}\), the remainder is uniformly \(O(h^{1/2})\), while the leading sum is exactly
\[
\frac{\sqrt h}{2}\sum_{j=1}^n\varepsilon_j
e^{(T-jh)C}Ke^{(j-1)hC}.
\]
Since \(e^{(T-jh)C}Ke^{(j-1)hC}=G((j-1)h)+O(h)\) uniformly in the index, its replacement by \(G((j-1)h)\) changes this normalized sum by at most \(O(\sqrt h)\) even deterministically. For every real linear functional on the space of \(d\times d\) matrices, the summands are independent and centered, the maximum absolute size is \(O(\sqrt h)\), and their variance sum converges to the corresponding Riemann integral. Lindeberg's central limit theorem and Cramér–Wold yield precisely the stated Gaussian limit with a single common Brownian driver. Singular covariance cases follow by allowing zero-variance linear functionals.

**Step 4: exact leading second moment.** Independence and zero means annihilate cross terms between distinct leading summands, so
\[
\mathbb E\Big\|\frac{h^2}{2}\sum_{j=1}^n\varepsilon_jG((j-1)h)\Big\|_F^2
=\frac{h^4}{4}\sum_{j=1}^n\|G((j-1)h)\|_F^2.
\]
The leading sum has \(L^2\)-norm \(O(h^{3/2})\) and the remainder has \(L^2\)-norm \(O(h^2)\); Cauchy–Schwarz shows all remainder contributions disappear after division by \(h^3\). Riemann convergence proves the boxed formula. Matrix exponentials are invertible, hence \(G(s)=0\) at any \(s\) exactly when \(K=0\); continuity and positive definiteness of the Frobenius norm give the strict positivity equivalence. If \(K=0\), the exponential law for commuting matrices makes each \(M_\pm(h)=e^{hC}\), proving exactness.

**Step 5: second-order mean.** Taking expectations in the uniform expansion of Step 2 eliminates its centered sum; thus \(\|\mathbb E P_n-e^{TC}\|_F\le\mathbb E\|\mathcal R_n\|_F=O(h^2)\). Equivalently, independence implies \(\mathbb EP_n=[(M_++M_-)/2]^n\), whose local difference from \(e^{hC}\) is \(O(h^3)\).

**Oscillator constant.** For the displayed \(2\times2\) pair, \(C\) is skew-symmetric and \(K=\operatorname{diag}(-1,1)\). Therefore both exponentials in \(G(s)\) are orthogonal and preserve Frobenius norm, giving \(\|G(s)\|_F^2=\|K\|_F^2=2\). At \(T=1\), the integral equals \(2/4=1/2\).

## Verification

The standalone `check.py` uses exact symbolic matrix arithmetic to verify the local \(h^2\) coefficient and the oscillator commutator. It then computes the finite-step **exact expectation of squared matrix error** without Monte Carlo, using the deterministic recursion
\[
R_{k+1}=\frac12(M_+^{\mathsf T}R_kM_++M_-^{\mathsf T}R_kM_-),\qquad R_0=I,
\]
and the identity
\[
\mathbb E\|P_n-U\|_F^2
=\operatorname{tr}(R_n)+\|U\|_F^2
-2\operatorname{tr}\bigl(U^{\mathsf T}\overline M^n\bigr),
\quad\overline M=(M_++M_-)/2.
\]
These recurrence-based finite-grid checks approach \(1/2\) for the oscillator, corroborating but not replacing the infinite-dimensional-in-\(n\) proof above. Run `python check.py` with Python 3, NumPy, SciPy and SymPy installed.

## Relationship to prior work

Berger (1984) proved central limit theorems for near-identity random matrix products with \(n^{-1/2}\)-scale stochastic increments and stochastic Lie–Trotter product formulas. That general result does not directly address the **next-order fluctuation around deterministic \(n^{-1}\) drift with random \(n^{-2}\) local commutator perturbations** examined here, though a transformed extension could be relevant. Zhang (2009/2012) analyzed randomized-order Hamiltonian product formulas and bounds on mixed quantum-state error; Childs, Ostrander and Su (2018/2019) established randomized first-order product formulas and an improved order for the **averaged quantum channel**. Both sources explicitly introduce forward/reverse-order averaging and its local commutator cancellation. The present statement **does not claim discovery of that algorithm or its mean-order improvement**; it instead determines the full Gaussian fluctuation law and the sharp nonzero **individual-realization squared-error coefficient** for arbitrary real matrices, together with an exact commutator criterion. Jin and Li (2021) analyze a distinct randomly sampled Hamiltonian-term algorithm with bias/variance bounds, not this fair reversal Gaussian coefficient. Veldman and Zuazua (2021) analyze random time-splitting for control with expected convergence rates, rather than the trajectory law of independently reversed Lie products. These distinctions are about mathematical conclusions, not merely titles.

## Limitations

The theorem is finite-dimensional with bounded matrices and fixed terminal time. It does not assert a dimension-uniform bound, a parabolic unbounded-operator extension, nonlinear flow extension, exact finite-step risk formula for all matrices, optimality among all randomized splitting algorithms, or a rate for the distributional convergence itself. The exact oscillator expectation is a test case, not an independent proof of the universal asymptotic. Closely related general stochastic-product central-limit or randomized splitting results could establish an equivalent specialization; no claim of exhaustive publication precedence or independent validation is made.

## References

1. C. Zhang, *Randomized Algorithms and Lower Bounds for Quantum Simulation*, arXiv:0910.4145, first public 21 October 2009, https://arxiv.org/html/0910.4145v1. Related proceedings paper: *Randomized Algorithms for Hamiltonian Simulation*, Monte Carlo and Quasi-Monte Carlo Methods 2010 (published 2012).
2. A. M. Childs, A. Ostrander, Y. Su, *Faster quantum simulation by randomization*, arXiv:1805.08385, first public 22 May 2018, https://arxiv.org/abs/1805.08385; *Quantum* 3, 182 (2019).
3. S. Jin, X. Li, *A Partially Random Trotter Algorithm for Quantum Hamiltonian Simulations*, arXiv:2109.07987, first public 16 September 2021, https://arxiv.org/abs/2109.07987.
4. D. W. M. Veldman, E. Zuazua, *A framework for randomized time-splitting in linear-quadratic optimal control*, arXiv:2109.13798, first public 28 September 2021, https://arxiv.org/html/2109.13798v2.

5. M. A. Berger, *Central limit theorem for products of random matrices*, Transactions of the American Mathematical Society 285 (1984), 777–803, https://doi.org/10.1090/S0002-9947-1984-0752503-3. Sections 5–6 address random products and stochastic Lie–Trotter limits.
