# Gaussian cut-quality fluctuations among locally stable configurations on wheels

## Finding
For every \(n\ge3\), let \(W_n=K_1\vee C_n\). Under synchronous open-neighborhood binary minority updates with tie retention, choose a fixed configuration uniformly at random and let \(C_n\) be its number of discordant undirected edges. Let \(\rho>1\) be the real root of \(\rho^3-\rho-1=0\), and set
\[
\mu=\frac{\rho+1}{2\rho+3},\qquad
v=\frac{\rho(\rho+1)}{(2\rho+3)^3}>0.
\]
Then
\[
\boxed{\frac{C_n-n(1+\mu)}{\sqrt{nv}}\Longrightarrow N(0,1),}\qquad
\mathbb E[C_n]=n(1+\mu)+o(1),\quad
\operatorname{Var}(C_n)=nv+o(1).
\]
Numerically, the typical stable cut has size \(1.41149558866\ldots n\), with variance \(0.01707962906\ldots n\). Meanwhile the proportion of fixed configurations maximizing the wheel cut size decreases exponentially. This is a sharp fluctuation and typical-quality theorem for a natural equilibrium ensemble, not an original classification of the equilibria or their size-refined counts.

## Exact prior enumerative input
Fix the hub opinion to zero by global complementation. The fixed rim words avoid cyclic `00` and `111`, so the zero vertices form a maximal independent set of the rim cycle. Each such word with \(z\) zeros cuts \(n+z\) edges. It is already known that exactly
\[
2\frac nz\binom{z}{n-2z},\qquad
\lceil n/3\rceil\le z\le\lfloor n/2\rfloor,
\]
labelled fixed configurations have this cut size: see *A sharp equilibrium and efficiency phase transition on weighted wheel networks* (November 8, 2026), which proves the same statement for all positive spoke weights below two, including unit weights. The Perrin count of maximal independent sets of a cycle was known still earlier. In particular the complete cut-size polynomial and optimum classification are **covered inputs**, not new claims.

## Proof of the fluctuation and exponential-scarcity statements
Put a variable \(u\) on each rim zero. On the allowed adjacent-bit states \(01,10,11\), the transfer matrix is
\[
B(u)=\begin{pmatrix}0&u&1\\1&0&0\\0&u&0\end{pmatrix},
\quad\det(tI-B(u))=t^3-ut-u.
\]
Each closed walk of length \(n\) corresponds bijectively to a labelled cyclic word without `00` and `111`, with weight \(u^z\); hence the exact probability generating function for \(Z_n=C_n-n\) is
\[
\mathbb E[u^{Z_n}]=\frac{\operatorname{tr}(B(u)^n)}{\operatorname{tr}(B(1)^n)}.
\]
This reweights the *already known* enumerator; the statistical asymptotics below are the additional assertion.

At \(u=1\), \(B(1)\) is primitive. Its characteristic polynomial has simple dominant root \(\rho\), and the other two eigenvalues have absolute value \(\rho^{-1/2}<\rho\). Analytic perturbation therefore provides a simple dominant eigenvalue \(\lambda(u)\), analytic near \(u=1\), satisfying \(\lambda(u)^3=u(\lambda(u)+1)\), and a uniform spectral gap in a complex neighborhood. For \(t\) near zero,
\[
\log\mathbb E[e^{tZ_n}]
=n[\log\lambda(e^t)-\log\rho]+O(\vartheta^n)
\]
with error and all of its derivatives uniform on a smaller neighborhood, for some \(\vartheta<1\). Differentiating the implicit eigenvalue equation twice gives
\[
\left.\frac{d}{dt}\log\lambda(e^t)\right|_{t=0}=\frac{\rho+1}{2\rho+3}=\mu,
\qquad
\left.\frac{d^2}{dt^2}\log\lambda(e^t)\right|_{t=0}
=\frac{\rho(\rho+1)}{(2\rho+3)^3}=v>0.
\]
The characteristic-function substitution \(t=is/\sqrt{nv}\) and Taylor expansion yield the Gaussian limit \(\exp(-s^2/2)\). Differentiating at zero yields the stated mean and variance, including the \(o(1)\) errors. The global maximum cut is \(n+\lfloor n/2\rfloor\), and the covered exact equilibrium formula gives only four maximizing fixed states for even \(n\), or \(2n\) for odd \(n\). Meanwhile the total number of fixed states is \(2\operatorname{tr}(B(1)^n)=2\rho^n+O(\rho^{-n/2})\). The maximizing fraction is therefore exponentially small. \(\square\)

## Verification, scope, and originality limits
The unchanged `checks/direct_census.py` and `checks/transfer_certificate.py` enumerate finite wheel states and check weighted traces and variance approximations. These finite tests are corroborative, not a proof of the Gaussian limit. The proof needs the primitive transfer matrix and its analytic eigenvalue gap; neither is a simulation assumption. The model concerns fixed points only, not basins or periodic dynamics. The identified November 8 weighted-wheel theorem already proves the complete equilibrium cut histogram, optimality counts, and exact price of anarchy; none is asserted as new. The new subject is the **uniformly sampled equilibrium's distributional fluctuation and explicit constants**, which quantify typical rather than worst-case quality. A general theorem on random maximal independent sets of cycles might imply these asymptotics; historical originality remains best-of-knowledge.

## References
- *A sharp equilibrium and efficiency phase transition on weighted wheel networks*, published November 8, 2026, https://github.com/Resultary/2026/blob/main/2026/11/8/SCOPE-a-sharp-equilibrium-and-efficiency-phase-transition-on-weighted--2af39b916123/RESULT.md .
- R. Bisdorff and J.-L. Marichal, *Counting Non-Isomorphic Maximal Independent Sets of the n-Cycle Graph*, J. Integer Sequences 11 (2008), 08.5.7.
- OEIS Foundation, A001608, Perrin sequence, https://oeis.org/A001608 .
