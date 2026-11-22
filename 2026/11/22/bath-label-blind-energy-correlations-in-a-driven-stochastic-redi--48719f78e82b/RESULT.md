# Bath-label-blind energy correlations in a driven stochastic redistribution star

## Finding

Let \(N=2m\ge2\), \(r>0\), \(T>|\Delta|\ge0\), \(T_+=T+\Delta\), and \(T_-=T-\Delta\). At stationarity of the stochastic-energy redistribution star defined below, denote hub energy by \(E_0\) and leaf energies by \(E_i\). Write \(\sigma_i=+1\) for the first \(m\) leaves and \(\sigma_i=-1\) for the other \(m\), and set
\[
 a=\frac{2r}{1+2r},\qquad D=(1+2r)^2(N+2r+1).
\]
Then
\[
\begin{aligned}
 \mathbb E E_0&=T,&\mathbb E E_i&=T+\sigma_i a\Delta,\\
 \operatorname{Cov}(E_0,E_i)&=\frac{\Delta^2}{(1+2r)(N+2r+1)},
 &\operatorname{Cov}(E_i,E_j)&=\frac{\Delta^2}{D}\quad(i\ne j),\\
 \operatorname{Var}(E_0)&=T^2+\left(\frac{2r}{1+2r}+\frac{2(r+1)}D\right)\Delta^2,\\
 \operatorname{Var}(E_i)&=T^2+2\sigma_i Ta\Delta+\left(\frac{4r}{1+2r}-a^2+\frac2D\right)\Delta^2.
\end{aligned}
\]
The equal leaf–leaf covariance is independent of both bath labels, including whether they match. It is strictly positive for every \(\Delta\ne0\), and at fixed \(r>0\) all distinct-site covariances vanish like \(N^{-1}\), whereas the limiting hub variance is \(T^2+2r\Delta^2/(1+2r)\), strictly larger than its equilibrium exponential-energy value when \(\Delta\ne0\).

## Assumptions and scope

For each of the \(N\) star edges, an independent rate-one Poisson clock rings. When edge \((0,i)\) rings, take an independent uniform \(U\in[0,1]\) and replace \((E_0,E_i)\) by \((U(E_0+E_i),(1-U)(E_0+E_i))\). Each leaf also has an independent rate-\(r\) bath clock; when its clock rings, replace \(E_i\) by a fresh independent exponential variable of mean \(T_{\sigma_i}\), leaving every other energy unchanged. Bath temperatures are positive, every Poisson clock and its marks independent, and the hub has no direct bath. All times are continuous. This definition, including the independent leaf bath refresh mechanism, is essential: neither the closed microcanonical KMP star nor instantaneous boundary thermalization is asserted to obey the same finite-rate formulas.

## Proof

**Stationarity and uniqueness.** Couple two copies using identical clocks, uniforms and bath samples. Edge updates are nonexpansive in the \(\ell^1\) energy distance, and bath updates erase the difference at their own leaf. In a fixed block there is a strictly positive probability that each leaf is first bath-refreshed, that the hub then interacts once with that leaf with \(U\in[1/4,3/4]\), and that the leaf is again refreshed before any other edge event. On this event all initial leaf discrepancies are erased, and the hub discrepancy is multiplied by at most \((3/4)^N\). Hence the finite-block coupling contracts expected \(\ell^1\) distance by a strict factor below one. The affine updates have finite moments of every fixed order because the bath marks are exponential and each exchange is a convex redistribution. Iterating from the zero state and using the coupling proves existence and uniqueness of a stationary law with finite first and second moments. The same coupling supplies uniqueness of stationary moments, so solving the moment equations suffices.

**First moments.** The generator on \(E_0\) and \(E_i\), respectively, yields
\[
0=\frac12\sum_i(\mathbb EE_i-\mathbb EE_0),\qquad
0=\frac12(\mathbb EE_0-\mathbb EE_i)+r(T_{\sigma_i}-\mathbb EE_i).
\]
Summing the second equations and using equal populations gives \(\mathbb EE_0=T\), followed by \(\mathbb EE_i=T+\sigma_i a\Delta\).

**Second-moment system.** Write \(M_{ij}=\mathbb E(E_iE_j)\), \(\mu_i=\mathbb E E_i\). The uniform mark identities \(\mathbb E U^2=1/3\), \(\mathbb E[U(1-U)]=1/6\), and the exponential bath identity \(\mathbb E B_i^2=2T_{\sigma_i}^2\) give, for every leaf \(i\),
\[
\begin{aligned}
0&=\sum_i(M_{ii}+2M_{0i}-2M_{00}),\\
0&=(M_{00}+2M_{0i}-2M_{ii})/3+r(2T_{\sigma_i}^2-M_{ii}),\\
0&=(M_{00}+M_{ii}+2M_{0i})/6-M_{0i}
 +\tfrac12\sum_{j\ne i}(M_{ij}-M_{0i})
 +r(T_{\sigma_i}\mu_0-M_{0i}),\\
0&=(M_{0i}+M_{0j})/2-(1+2r)M_{ij}
 +r(T_{\sigma_i}\mu_j+T_{\sigma_j}\mu_i)\quad(i\ne j).
\end{aligned}
\]
The first line has an immaterial common factor \(1/3\). The last three lines are the exact stationary generator identities on leaf-square, hub–leaf, and distinct-leaf products. They close at degree two; no mean-field factorization is used.

**Exact solution and positivity.** Substitute \(\mu_0=T\), \(\mu_i=T+\sigma_i a\Delta\), and the moment expressions \(M_{ij}=\mu_i\mu_j+\operatorname{Cov}(E_i,E_j)\), \(M_{ii}=\mu_i^2+\operatorname{Var}(E_i)\) from the Finding into these identities. Every identity becomes exactly zero for arbitrary real \(m\ge1\), \(r>0\), \(T>|\Delta|\). A symbolic reduction for all eleven inequivalent monomial types is in `symbolic_check.py`; an independent rational Markov-generator checker is in `verify.py`. The uniqueness argument therefore proves the formula for all allowed \(N\) and continuous parameters. Positivity follows because \(D>0\). The limiting hub variance follows by direct passage \(N\to\infty\), without claiming a complete limiting joint law.

## Verification

Execute `python symbolic_check.py` (requires SymPy) to check eleven generator-identity classes symbolically for general \(m,r,T,\Delta\). Execute `python verify.py` (standard Python only) to check all degree-zero, -one and -two monomials in independent exact rational arithmetic for \(N\in\{2,4,6,8,10\}\), four bath rates, and three pairs of bath temperatures. This checker verifies 2,400 exact rational generator identities. Finite instances alone are not the proof; the symbolic general-parameter identities together with the stationary moment closure and uniqueness establish the all-size theorem.

## Relationship to prior work

Kipnis, Marchioro and Presutti (1982) introduced stochastic redistribution of energy along a one-dimensional chain; this dynamics is a foundation, not a new model invented here. Carinci et al. (arXiv:1507.01478v1, 6 July 2015) treat asymmetric stochastic transport and KMP duality; it is the earliest source used here with a verified full first-public calendar date. Franco (arXiv:1601.04042v1) considers slow/fast reservoirs but studies macroscopic behavior on a *one-dimensional chain*, not the uniform finite-star, bath-label-blind covariance. Gilbert (arXiv:1703.01240v1) gives high-order nonequilibrium covariance on *one-dimensional chains*. De Masi, Ferrari and Gabrielli (arXiv:2310.01672v1) prove a broad, previously known hidden-temperature mixture representation on arbitrary finite graphs with boundaries and explicitly discuss direct bath replacement; the present theorem does not claim invention of that representation, positivity on arbitrary networks, or the general existence of stationary correlations. Their structural theorem could be specialized and further calculated, but no explicit finite-rate two-bath star identity independent of both bath labels, or the displayed exact large-degree nonthermal variance, was located in the material examined. Thus novelty is restricted to these explicit star identities and their sign-and-scale consequences, with residual historical-priority uncertainty.

## Limitations

The graph must be a uniform-rate star with a balanced number of hot and cold leaves. The result does not assert label blindness for unequal bath populations, different edge exchange laws, nonlinear reservoir responses, or arbitrary networks. Equilibrium \(\Delta=0\) yields zero, not positive, pair covariances. The result is an exact statement about stationary moments, not a new complete stationary distribution or an infinite-volume convergence theorem. Historical priority cannot be fully certified from bounded accessible literature; in particular, the complete 1982 original article was not accessible through lawful full-text paths, and more specific unindexed graph specializations may exist.

## References

- C. Kipnis, C. Marchioro, E. Presutti, *Heat flow in an exactly solvable model*, Journal of Statistical Physics 27 (1982), 65–74. DOI: https://doi.org/10.1007/BF01011740.
- G. Carinci, C. Giardinà, F. Redig, T. Sasamoto, *Asymmetric stochastic transport models with Uq(su(1,1)) symmetry*, arXiv:1507.01478v1 (first posted 2015-07-06): https://arxiv.org/abs/1507.01478.
- T. Franco, *Phase transition in the KMP model with slow/fast boundaries*, arXiv:1601.04042v1 (2016): https://arxiv.org/abs/1601.04042.
- T. Gilbert, *Heat conduction and the nonequilibrium stationary states of stochastic energy exchange processes*, arXiv:1703.01240v1 (2017): https://arxiv.org/abs/1703.01240.
- A. De Masi, P. Ferrari, D. Gabrielli, *Hidden temperature in the KMP model*, arXiv:2310.01672v1 (2023): https://arxiv.org/abs/2310.01672.
