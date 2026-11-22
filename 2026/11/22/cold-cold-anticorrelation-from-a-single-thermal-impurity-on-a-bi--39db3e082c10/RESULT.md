# Cold–cold anticorrelation from a single thermal impurity on a bipartite energy-exchange network

## Finding

Let \(n\ge3\) be an integer and let the graph be the balanced complete bipartite graph \(K_{n,n}\), with shores \(A\) and \(B\). Select a vertex \(H\in A\). On each edge, independently at rate one, replace its endpoint energies \((X_i,X_j)\) by \((U(X_i+X_j),(1-U)(X_i+X_j))\), where \(U\) is uniform on \([0,1]\). Every vertex independently refreshes its energy from an exponential distribution at rate \(g>0\). The mean of the refreshing distribution is \(T+\Delta\) at \(H\) and \(T\) at every other vertex, with \(T>0\) and \(\Delta>0\). All clocks and samples are independent.

There is a unique stationary law. Write \(P,P'\) for distinct vertices in \(A\setminus\{H\}\), and \(Q,Q'\) for distinct vertices in \(B\). All covariances in this finding are in that law. Define

\[
\begin{aligned}
R_n(g)={}&n^3(2n-1)+n^2(8n-3)g+n(6n+1)g^2\\
&-4(n-1)g^3-4g^4,\\
D_n(g)={}&4(g+n)^2(2g+n)^2\big(6g^2+(8n-1)g+2n^2\big).
\end{aligned}
\]

Then

\[
\boxed{\operatorname{Cov}(X_Q,X_{Q'})=\Delta^2\frac{R_n(g)}{D_n(g)}.}
\]

The polynomial \(R_n\) has exactly one positive real root \(g_*(n)\). Consequently, the covariance of two cold vertices in the shore *opposite* the thermal impurity is strictly positive for \(0<g<g_*(n)\), zero at \(g=g_*(n)\), and strictly negative for \(g>g_*(n)\). The threshold has the sharp large-network limit

\[
\boxed{\lim_{n\to\infty}\frac{g_*(n)}{n}=\frac{1+\sqrt3}{2}.}
\]

In contrast, the other two symmetry classes of pairs of cold vertices are strictly positively correlated for **every** \(g>0\):

\[
\operatorname{Cov}(X_P,X_Q)=\Delta^2\frac{S_n(g)}{E_n(g)}>0,
\qquad
\operatorname{Cov}(X_P,X_{P'})=\frac{n}{n+2g}\operatorname{Cov}(X_P,X_Q)>0,
\]

where

\[
\begin{aligned}
S_n(g)={}&128g^6+(476n-88)g^5+(740n^2-164n)g^4\\
&+(638n^3-131n^2+2n)g^3\\
&+(332n^4-85n^3+10n^2)g^2\\
&+(98n^5-39n^4+6n^3)g+12n^6-6n^5,\\
E_n(g)={}&4(g+n)^2(2g+n)(4g+3n)\\
&\quad\cdot\big(6g^2+(8n-1)g+2n^2\big)\\
&\quad\cdot\big(12g^2+(11n-2)g+2n^2\big).
\end{aligned}
\]

All coefficients of \(S_n(g)\) are strictly positive when \(n\ge3\), and both denominators are strictly positive on the stated domain. The sign classification is independent of the positive background bath mean \(T\) and of the magnitude of \(\Delta\).

## Assumptions and scope

The graph has exactly two equal shores of size \(n\), all cross-shore edges present, no within-shore edges, unit edge redistribution rates, common positive bath refresh rate \(g\), one bath of mean \(T+\Delta\), and all remaining baths of mean \(T\). The process has nonnegative unbounded continuous site energies. A covariance always means a *connected equal-time* stationary second moment, for two **distinct** sites. The theorem covers every integer \(n\ge3\) and all real \(g,T,\Delta>0\); it makes no claim about dynamical mixing times or higher cumulants.

## Proof

**Stationary moments and uniqueness.** For the first moments \(m_i=\mathbb E X_i\), the generator gives

\[
0=\frac12\sum_{j\sim i}(m_j-m_i)+g(T_i-m_i).
\]

On the space of degree-two monomials, each edge redistribution is explicitly integrable because \(\mathbb E U=1/2\), \(\mathbb E U^2=1/3\), and \(\mathbb E[U(1-U)]=1/6\). The independent refresh clocks supply finite second moments. For instance the total energy has a strictly negative quadratic drift outside a bounded set. Fixing a deterministic interval and restricting to the positive-probability clock event in which every site refreshes and no edge clock rings gives a state-independent regeneration component, proving uniqueness of the stationary probability law.

**Background-temperature reduction.** For normalized bath labels \(t_H=1\), \(t_i=0\) elsewhere, let \(u_i\) and \(V_{ij}\) be the stationary first and raw second moments with bath means \(t_i\). If the actual bath means are \(T+\Delta t_i\), direct substitution in the linear first- and second-moment stationarity equations gives

\[
\begin{aligned}
m_i&=T+\Delta u_i,\\
\mathbb E(X_iX_j)&=(1+\mathbf1_{i=j})T^2
+(1+\mathbf1_{i=j})T\Delta(u_i+u_j)+\Delta^2V_{ij}.
\end{aligned}
\]

The mixed \(T\Delta\) coefficients vanish in every second-moment equation by the first-moment identities; the \(T^2\) coefficients are the stationary moments of independent mean-\(T\) exponentials. Therefore, for distinct sites,
\(\operatorname{Cov}(X_i,X_j)=\Delta^2(V_{ij}-u_iu_j)\). It suffices to solve the normalized system.

**Symmetry reduction.** Put \(p=u_P\), \(q=u_Q\), and \(h=u_H\). Solving the three first-moment equations yields

\[
\begin{aligned}
h&=\frac{4g^2+4gn+n}{2(g+n)(2g+n)},\\
p&=\frac{n}{2(g+n)(2g+n)},\\
q&=\frac1{2(g+n)}.
\end{aligned}
\]

Use the eight normalized raw moments

\[
(a,b,c,d,e,f,k,\ell)
=(\mathbb E H^2,\mathbb E P^2,\mathbb E Q^2,
\mathbb E HP,\mathbb E HQ,\mathbb E PP',\mathbb E PQ,\mathbb E QQ').
\]

The complete stationary degree-two system, without approximation, is

\[
\begin{aligned}
0&=n(-2a+2e+c)/3+g(2-a),\\
0&=n(-2b+2k+c)/3-gb,\\
0&=(-2nc+2e+2(n-1)k+a+(n-1)b)/3-gc,\\
0&=n(k+e-2d)/2+gp-2gd,\\
0&=(a+c-4e)/6+(n-1)(\ell+d-2e)/2+gq-2ge,\\
0&=n(k-f)-2gf,\\
0&=(b+c-4k)/6+\big((n-1)(\ell-k)+(d-k)+(n-2)(f-k)\big)/2-2gk,\\
0&=e+(n-1)k-(n+2g)\ell.
\end{aligned}
\]

Its coefficient determinant, up to the harmless choice of multiplying equations by negative one, is

\[
\frac{g(g+n)(2g+n)(4g+3n)
\big(6g^2+(8n-1)g+2n^2\big)
\big(12g^2+(11n-2)g+2n^2\big)}{18}>0.
\]

Thus the system has a unique solution. Exact elimination gives \(\ell-q^2=R_n(g)/D_n(g)\) and \(k-pq=S_n(g)/E_n(g)\), with the explicit polynomials stated in the Finding. From the sixth equation \(f=nk/(n+2g)\), while \(p=nq/(n+2g)\), giving \(f-p^2=n(k-pq)/(n+2g)\). This proves all exact covariance identities and positivity of the other two cold-pair classes.

**One transition and its scale.** Written in increasing powers, \(R_n\) has sign pattern \((+,+,+,-,-)\) for every \(n\ge3\). Descartes' rule of signs yields at most one positive zero, while \(R_n(0)>0\) and \(R_n(g)\to-\infty\), proving exactly one. For fixed positive \(c\),

\[
\frac{R_n(cn)}{n^4}\longrightarrow
-2(c+1)^2(2c^2-2c-1).
\]

The limit has one positive root \((1+\sqrt3)/2\), with strictly positive sign below and strictly negative sign above. The unique finite-\(n\) positive root is trapped between any two fixed positive values bracketing this root, proving the asserted convergence.

## Verification

The supplied `verify_symbolic.py` checks the entire eight-orbit determinant and rational identities by cancellation over \(\mathbb Q(n,g)\). Separately, `verify.py` constructs stationary first- and second-moment systems **directly from every vertex pair**, without using the eight-orbit reduction. It solves the resulting rational linear systems for \(n=2,3,4\), each with four positive rational rates, independently checking the two displayed rational covariance formulas. For \(n\ge3\) it also verifies the same-shore versus cross-shore identity; the twelve finite cases passed. The code checks the exact limiting quartic factorization. The proof above, not these finite checks, establishes the infinite-family statements.

For example, at \(n=3\), \(g=5\), and normalized temperature contrast \(\Delta=1\), \(\operatorname{Cov}(X_Q,X_{Q'})=-995/12243712\), whereas \(\operatorname{Cov}(X_P,X_Q)=12777675/12918999808>0\). Numerically \(g_*(3)\approx4.2981207848\).

## Relationship to prior work

Kipnis–Marchioro–Presutti introduced the energy-exchange model (1982); Bertini, Gabrielli and Lebowitz (first arXiv version dated 2005-01-27) study the boundary-driven one-dimensional chain, its large deviations and macroscopic correlations. The distinct graph and bath architecture here are an all-vertex independently thermostatted complete bipartite network with a single hot impurity. De Masi, Ferrari and Gabrielli (first arXiv version 2023-10-02) provide an invariant-measure mixture representation for a finite graph with a designated boundary and specify different boundary-update conventions. Neither work, in the material inspected, gives this graph-specific finite-size cold-pair quartic or the sign separation of the three cold-pair orbits.

The general model, generator integration, and finite-moment methods are standard and are not asserted as inventions. The specific all-rate, all-size covariance classification and sharp \((1+\sqrt3)/2\) threshold are the claims compared with prior research. A broader unpublished or unlocated formula could cover this specialization; no global historical-priority certification is claimed.

## Limitations

Equal shore sizes, independent identical-rate local exponential refresh clocks, one strictly hotter bath, and unit edge redistribution rates are essential stated assumptions. At \(\Delta=0\), all off-site covariances vanish and there is no sign transition. The classification does not establish energy current fluctuations, dynamical correlations, mixing rates, nonbipartite analogues, unequal shore sizes, or nonuniform edge rates. Existing general graph or boundary-reservoir results may contain alternative derivations not located in the inspected material.

## References

1. Kipnis, C., Marchioro, C., Presutti, E., *Heat flow in an exactly solvable model*, Journal of Statistical Physics 27 (1982), 65–74. DOI: https://doi.org/10.1007/BF01011740 . (Historical model origin; only publication year is relied on.)
2. Bertini, L., Gabrielli, D., Lebowitz, J. L., *Large deviations for a stochastic model of heat flow*, arXiv:cond-mat/0501681v1, publicly submitted 2005-01-27. https://arxiv.org/html/cond-mat/0501681v1 .
3. De Masi, A., Ferrari, P. A., Gabrielli, D., *Hidden temperature in the KMP model*, arXiv:2310.01672v1, first submitted 2023-10-02. https://arxiv.org/html/2310.01672v2 .
4. Nándori, P., *Local equilibrium in inhomogeneous stochastic models of heat transport*, arXiv:1603.04960v1, first submitted 2016-03-16. https://arxiv.org/abs/1603.04960 . (Abstract-level contextual comparison only.)
