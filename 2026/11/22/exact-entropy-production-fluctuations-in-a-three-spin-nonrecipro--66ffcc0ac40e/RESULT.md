# Exact entropy-production fluctuations in a three-spin nonreciprocal Ising ring

## Finding
For the continuous-time, single-spin-flip nonreciprocal Glauber–Ising dynamics on the three-cycle, the **entire long-time cumulant-generating function of stationary path entropy production** has a closed square-root expression. In the notation below, for every real counting field \(s\),
\[
\psi(s)=\frac{g_s-1-3h-d+\sqrt{(d+1-g_s-3h)^2+12hd}}{2},\qquad
 g_s=\frac{\cosh((1-2s)\eta)}{\cosh\eta}.
\]
Here \(h=(1-\gamma_e)/2\), \(d=(1+\gamma_e)/2\), \(\eta=\operatorname{artanh}\gamma_o\), and \(|\gamma_e|,|\gamma_o|<1\). This implies \(\psi(s)=\psi(1-s)\) and \(\psi(0)=\psi(1)=0\). In particular, setting \(p=3h/(3h+d)\), stationary mean entropy production and its asymptotic variance rates are
\[
\lim_{T\to\infty}\frac{\mathbb E\Sigma_T}{T}=2p\eta\gamma_o,
\qquad
\lim_{T\to\infty}\frac{\operatorname{Var}(\Sigma_T)}{T}=
4p\eta^2\left(1+\frac{2(1-p)\gamma_o^2}{3h+d}\right).
\]
The second term in parentheses is strictly positive for nonzero directionality and reflects fluctuations of time spent in configurations with two disagreeing neighbors. Consequently, the entropy fluctuations are not those of a simple Poisson difference. The mean is strictly positive for \(\gamma_o\ne0\); when \(\gamma_o=0\), the entropy process vanishes and \(\psi\equiv0\).

## Assumptions and scope
The state is \(\sigma=(\sigma_0,\sigma_1,\sigma_2)\in\{-1,+1\}^3\), with cyclic indices. Every site \(i\) flips independently in continuous time at state-dependent rate
\[
w_i(\sigma)=\frac12\left[1-\frac{\sigma_i}{2}\bigl(\gamma_e(\sigma_{i-1}+\sigma_{i+1})+\gamma_o(\sigma_{i-1}-\sigma_{i+1})\bigr)\right].
\]
All parameters are real with \(|\gamma_e|<1\) and \(|\gamma_o|<1\), ensuring strictly positive rates and a unique stationary probability law \(\pi\). This includes positive and negative reciprocal coupling. For a stationary trajectory on \([0,T]\), define dimensionless total path entropy production
\[
\Sigma_T=\sum_{\text{spin flips }\sigma\to\sigma'}\log\frac{w(\sigma,\sigma')}{w(\sigma',\sigma)}+\log\frac{\pi(\sigma(0))}{\pi(\sigma(T))}.
\]
The boundary term is bounded because the state space is finite. The scaled generating function is \(\psi(s)=\lim_{T\to\infty}T^{-1}\log\mathbb E_\pi[e^{-s\Sigma_T}]\). The theorem is a three-spin statement, not an assertion for arbitrary rings or the full finite-time generating function.

## Proof
1. Let \(A\) denote the two fully aligned configurations, and \(B\) the six configurations having a single minority spin. For \(A\), there are precisely three outgoing flips into \(B\), each at rate \(h\). For \(B\), one flip reaches \(A\) at rate \(d\); the two other flips remain in \(B\) at rates \((1+\gamma_o)/2\) and \((1-\gamma_o)/2\). Their reverse rates are respectively \((1-\gamma_o)/2\) and \((1+\gamma_o)/2\). The overall exit rate from \(B\) is \(d+1\).
2. For the medium-entropy generating function, the tilted generator has the same diagonal as the original generator and off-diagonal transition rate \(w(\sigma,\sigma')^{1-s}w(\sigma',\sigma)^s\). The stationary system-entropy boundary term only conjugates the tilted semigroup by a positive diagonal matrix, so it does not alter the eigenvalues. All tilted rates are positive for real \(s\); irreducibility and Perron–Frobenius for Metzler matrices give a simple, real dominant eigenvalue. The tilt commutes with rotations and simultaneous spin reversal. By uniqueness, its positive dominant eigenvector is invariant under these symmetries, hence constant on each of \(A\) and \(B\).
3. Write \(h_s=h^{1-s}d^s\), \(d_s=d^{1-s}h^s\), and \(g_s=((1+\gamma_o)/2)^{1-s}((1-\gamma_o)/2)^s+((1-\gamma_o)/2)^{1-s}((1+\gamma_o)/2)^s\). The symmetry-reduced tilted operator on a two-orbit row-valued test function is
\[
M_s=\begin{pmatrix}-3h&3h_s\\ d_s&-d-1+g_s\end{pmatrix}.
\]
The product \(h_sd_s=hd\); moreover the stated hyperbolic-cosine expression for \(g_s\) follows because \(\tanh\eta=\gamma_o\). Computing the greater real root of \(\det(M_s-\lambda I)=0\) gives precisely \(\psi(s)\) above, for every real \(s\).
4. At \(s=0\), \(g_0=1\), and the stationary probability of orbit \(B\) is \(p=3h/(3h+d)\). Differentiating the quadratic eigenvalue equation \((\psi+3h)(\psi+d+1-g_s)=3hd\) gives \(\partial\psi/\partial g_s=p\) and \(\partial^2\psi/\partial g_s^2=2p(1-p)/(3h+d)\) at \(g_s=1\). As \(g'_0=-2\eta\gamma_o\) and \(g''_0=4\eta^2\), the displayed first and second cumulants follow. The square-root expression is regular because \(h,d>0\). Symmetry \(g_s=g_{1-s}\) proves the Gallavotti–Cohen relation.

## Verification
Run \(\texttt{python verification.py}\) with Python 3 and NumPy. Its full eight-configuration generator independently enumerates all spin flips and diagonalizes the tilted matrix for a grid of reciprocal parameters, nonreciprocity strengths and counting fields; it compares the leading eigenvalue to the analytic formula. Further checks compare the exact generator stationary law, first two derivatives, and symmetry. Numerical diagonalization is a cross-check; the symbolic two-orbit reduction proves the theorem for all allowed parameters and all real counting fields.

## Relationship to prior work
Weiderpass, Sharma and Sethi (arXiv:2410.23615v1, initially public 2024-10-31) develop the motivating continuous-time nonreciprocal Glauber dynamics and its dynamical correlations and exceptional-point regimes; their companion short paper arXiv:2411.00059v1 gives its overview. Godrèche (arXiv:1102.0141v1) and Godrèche–Luck (arXiv:1503.01661v1) establish the broader directed-Glauber and irreversible Gibbsian dynamics. In particular, the existence of an equilibrium-Gibbs stationary measure despite irreversible transitions is **prior work**, not the finding here. The new assessed object is a tilted path-additive observable, not a one-time or two-time spin correlation. Its entire stationary long-time entropy cumulant sequence does not follow from an un-tilted correlation formula without a separate tilted generator calculation. Classical fluctuation symmetries are not claimed as new; the exact model-specific tilted eigenvalue and non-Poisson variance are the claim.

## Limitations
The model is the minimal three-site ring with single-site flips; no arbitrary-size entropy large-deviation formula or finite-time entropy distribution is claimed. The counting field is real. A generic Markov-chain eigenvalue method is known, and unindexed calculations for this precise rate system could contain the same two-orbit reduction; independent literature verification is outstanding. The independent scientific audit has not been performed.

## References
- G. A. Weiderpass, M. Sharma and S. Sethi, *Solving the Kinetic Ising Model with Non-Reciprocity*, arXiv:2410.23615v1 (2024-10-31), https://arxiv.org/abs/2410.23615.
- G. Weiderpass, M. Sharma and S. Sethi, *An Exact Solution for the Kinetic Ising Model with Non-Reciprocity*, arXiv:2411.00059v1 (2024-10-31), https://arxiv.org/abs/2411.00059.
- C. Godrèche, *Dynamics of the directed Ising chain*, arXiv:1102.0141v1 (2011), https://arxiv.org/abs/1102.0141.
- C. Godrèche and J.-M. Luck, *Single-spin-flip dynamics of the Ising chain*, arXiv:1503.01661v1 (2015), https://arxiv.org/abs/1503.01661.
- *A unifying framework for mean-field theories of asymmetric kinetic Ising systems*, Nature Communications (2021), https://www.nature.com/articles/s41467-021-20890-5 (different parallel-update model).
