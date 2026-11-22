# A unique covariance-sign reversal under local thermalization on a complete energy-exchange network

## Finding

Fix an integer \(N\ge3\). The complete graph \(K_N\) supports nonnegative stochastic energies \(X_1,\ldots,X_N\). Every unordered edge, independently at rate one, replaces \((X_i,X_j)\) by \((U(X_i+X_j),(1-U)(X_i+X_j))\), with fresh uniform \(U\) on \([0,1]\). Every vertex independently, at rate \(g>0\), replaces its energy by an independent exponential variable with mean \(T_i\). Assume \(T_1=T+\Delta\) and \(T_j=T\) for \(j\ge2\), with \(T>0\), \(\Delta>0\).

Define
\[
D_N(g)=(N+2g)^2(N+3g)(12g^2+11Ng+2N^2+N),
\]
\[
\begin{aligned}
P_N(g)={}&12g^4+(4N+2)g^3+(-6N^2-2N+4)g^2\\
&+(-2N^3-7N^2+5N+2)g-2N^3+N^2+N,
\end{aligned}
\]
\[
Q_N(g)=10g^3+(18N-4)g^2+(11N^2-5N-2)g+2N^3-N^2-N.
\]
For distinct cold sites \(j,k\ge2\), the unique stationary distribution obeys
\[
\operatorname{Cov}(X_1,X_j)=-\frac{\Delta^2P_N(g)}{D_N(g)},\qquad
\operatorname{Cov}(X_j,X_k)=\frac{\Delta^2Q_N(g)}{D_N(g)}.
\]
There is exactly one positive critical refresh rate \(g_c(N)\), defined by \(P_N(g_c(N))=0\). Hot–cold covariance is positive below and negative above it, while cold–cold covariance is strictly positive for every \(g>0\). Its size dependence is
\[
\lim_{N\to\infty}\frac{g_c(N)}{N}=\frac1{\sqrt2}.
\]

## Assumptions and scope

The model uses independent rate-one Poisson clocks on each unordered edge, not rate-one total per site; local reservoirs refresh energies at rate \(g\) independently and completely, with exponential second moment \(2T_i^2\). All parameters and site numbers have the ranges stated above. The theorem concerns stationary *equal-time* covariances of energies and the complete graph with precisely one temperature impurity. The limiting scaling holds when the edge rates remain one as \(N\) increases.

## Proof

**Existence and moment uniqueness.** Since all sites refresh to nondegenerate exponentials at positive rates, the finite-site process admits a unique invariant distribution by a common-clock coupling: for two initial conditions, use identical edge fractions and identical refresh draws, then each difference contracts in expectation, because edge redistribution preserves the sum of absolute coordinate differences at most, while full-site refresh removes that coordinate difference. On each interval, the expected total absolute difference satisfies a strict contraction from independent refreshes. The total energy's exchange component is conserved and the reservoir component is a linear negative drift, giving finite first and second stationary moments by quadratic Lyapunov bounds. Thus the first- and second-degree stationary generator equations uniquely determine the needed moments.

Let \(H=X_1\) and \(C_j=X_j\) for \(j\ge2\). Denote their means by \(m_H,m_C\), their second moments by \(h=\mathbb E H^2\), \(c=\mathbb E C_j^2\), and the two off-diagonal moments by \(p=\mathbb E[H C_j]\), \(q=\mathbb E[C_j C_k]\) for \(j\ne k\). The linear generator equations give
\[
m_H=T+\frac{(1+2g)\Delta}{N+2g},\qquad
m_C=T+\frac{\Delta}{N+2g}.
\]
Uniform redistribution has \(\mathbb E U^2=1/3\), \(\mathbb E[U(1-U)]=1/6\), so stationarity of \(H^2,C_j^2,HC_j,C_jC_k\) gives exactly
\[
\begin{aligned}
0={}&(N-1)[(h+c+2p)/3-h]+g[2(T+\Delta)^2-h],\\
0={}&[(h+c+2p)/3-c]+(N-2)[(2c+2q)/3-c]+g[2T^2-c],\\
0={}&(h+c)/6-2p/3+(N-2)(q-p)/2+g[(T+\Delta)m_C+Tm_H-2p],\\
0={}&c/3-2q/3+(p-q)+2g[Tm_C-q].
\end{aligned}
\]
These four equations form a linear system in \((h,c,p,q)\). Its coefficient determinant is
\[
\frac{g(N+3g)(12g^2+11Ng+2N^2+N)}9>0.
\]
Solving by elimination and subtracting products of means yields precisely \(p-m_Hm_C=-\Delta^2P_N(g)/D_N(g)\) and \(q-m_C^2=\Delta^2Q_N(g)/D_N(g)\). This is an identity in the freely varying parameters; the accompanying symbolic checker independently reconstructs and solves the linear equations.

**Signs and critical scaling.** For \(N\ge3\), all four coefficients of \(Q_N\) are strictly positive. The nonleading coefficients of \(P_N\), in descending order, have signs \(+,+,-,-,-\), since \(-6N^2-2N+4<0\), \(-2N^3-7N^2+5N+2<0\), and \(-2N^3+N^2+N<0\). Descartes' rule gives at most one positive root; \(P_N(0)<0\) and the leading coefficient is positive, so there is exactly one positive root and the asserted signs follow. For fixed \(s>0\),
\[
N^{-4}P_N(Ns)\longrightarrow 2s(3s+1)(2s^2-1).
\]
Its unique positive zero is \(s=1/\sqrt2\), with negative sign below and positive above. The uniqueness of \(g_c(N)\), together with sign convergence at two fixed ratios straddling this zero, proves \(g_c(N)/N\to1/\sqrt2\).

## Verification

Run `python verify.py` with Python 3 and SymPy installed. The checker constructs the four independent generator-moment equations, solves them algebraically, and verifies the rational covariance identities as polynomial identities in \(N,g,T,\Delta\), rather than inferring the general theorem from finite samples. It additionally checks exact finite-dimensional equations at several parameter combinations. The analytic Descartes argument and asymptotic polynomial limit establish the all-size sign statements.

## Relationship to prior work

The KMP uniform-energy redistribution process was introduced by Kipnis, Marchioro and Presutti (1982). Bertini, Gabrielli and Lebowitz (2005) address nonequilibrium energy fluctuations and large deviations for a one-dimensional boundary-driven chain, rather than the all-site thermostatting of the complete graph examined here. De Masi, Ferrari and Gabrielli (2023) establish a general stationary hidden-temperature representation for finite graphs with boundaries; its applicability is broader structurally, but the inspected full text does not state the present one-impurity complete-graph pair-covariance formula, unique sign transition, or linear-size critical rate. Capanna, Gabrielli and Tsagkarogiannis (2024) consider thermodynamic transport and solvable mass-exchange classes, not this finite complete-graph covariance threshold. These distinctions support an originality assessment, not definitive historical-priority certification.

## Limitations

No assertion is made for a fixed total edge-event rate, non-exponential reservoirs, heterogeneous edge weights, multi-impurity temperatures or time-lagged covariance. The complete-graph process has nontrivial microscopic rate normalization. Broader general-graph stationary representations might allow the formula to be derived indirectly; prior complete-graph specializations not found in the checked sources remain a historical risk. The result has not undergone independent scientific audit.

## References

- Kipnis, C., Marchioro, C., Presutti, E. (1982), *Heat flow in an exactly solvable model*, Journal of Statistical Physics **27**, 65–74. DOI: `10.1007/BF01011740`.
- Bertini, L., Gabrielli, D., Lebowitz, J. L. (2005), *Large deviations for a stochastic model of heat flow*, initial preprint 2005-01-27, https://arxiv.org/abs/cond-mat/0501681.
- Gilbert, T. (2017), *Heat conduction and the nonequilibrium stationary states of stochastic energy exchange processes*, https://arxiv.org/abs/1703.01240.
- De Masi, A., Ferrari, P. A., Gabrielli, D. (2023), *Hidden temperature in the KMP model*, initial preprint 2023-10-02, https://arxiv.org/abs/2310.01672.
- Capanna, M., Gabrielli, D., Tsagkarogiannis, D. (2024), *On a Class of Solvable Stationary Non Equilibrium States for Mass Exchange Models*, https://doi.org/10.1007/s10955-024-03240-9.
