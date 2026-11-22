# An exact finite-rate correlation maximum in boundary-driven symmetric inclusion

## Finding

The symmetric inclusion process on the balanced complete bipartite graph \(K_{n,n}\), with each shore coupled at every site to a different particle reservoir, exhibits a **unique optimum of stationary cross-shore occupation covariance** as the bulk hopping rate varies. In contrast, the magnitude of the mean particle current increases strictly throughout.

Write \(\Delta=\rho_A-\rho_B\). For all \(n\ge2\), \(\kappa,\gamma>0\), \(v\ge0\), and \(\rho_A,\rho_B>0\), the stationary occupation covariance of any site \(i\) in shore \(A\) and any site \(j\) in shore \(B\) is

\[
C_{AB}=\frac{\gamma v(\gamma+\kappa v)\Delta^2}{2(\gamma+2\kappa v)^2\,[n(\gamma+2\kappa v)+v]}.
\]

For two distinct sites of either shore, \(C_{AA}=C_{BB}=\kappa v C_{AB}/(\gamma+\kappa v)\). For \(\Delta\ne0\), the cross-shore covariance is strictly positive at every finite \(v>0\) and has one global maximum. Writing \(x=\kappa v/\gamma\), the optimal \(x_*\) is the unique positive root of

\[
(2\kappa n+1)x_*^2(2x_*+3)=\kappa n.
\]

The signed stationary A-to-B particle current across all bulk edges is

\[
J=\frac{n\kappa v\gamma\Delta}{\gamma+2\kappa v}.
\]

It increases in magnitude with \(v\) for unequal reservoirs, whereas \(C_{AB}\to0\) for \(v\to\infty\). Furthermore, \(x_*\to(\sqrt3-1)/2\) as \(n\to\infty\).

## Assumptions and scope

The graph is \(K_{n,n}\) with shores \(A,B\) of size \(n\ge2\). A state is \(\eta\in\mathbb N_0^{2n}\), with \(\eta_i\) indistinguishable particles at site \(i\). Every oriented bulk edge \(i\to j\) fires at rate \((v/n)\eta_i(\kappa+\eta_j)\), moving one particle from \(i\) to \(j\). Here \(\kappa>0\) measures the free-walk contribution to the inclusion rate, and \(v\ge0\) is the bulk coupling.

Every site \(i\) on shore \(X\in\{A,B\}\) receives independent reservoir births at rate \(\lambda_X(\kappa+\eta_i)\) and deaths at rate \((\gamma+\lambda_X)\eta_i\), where \(\lambda_X=\gamma\rho_X/\kappa\), \(\gamma>0\), and \(\rho_X>0\). The reservoir-only equilibrium mean at such a site is \(\rho_X\). A single reservoir acts at **every** site, not merely at two distinguished boundary vertices.

For all parameter choices the process is irreducible and positive recurrent: the total particle number \(N\) has drift \(\gamma[n(\rho_A+\rho_B)-N]\). The generator applied to \(N^2\) has a strictly negative quadratic leading term, implying stationary finite second moments. The stationary distribution is unique and invariant under separate permutations of the two shores.

## Proof

**1. Mean occupations.** Let \(\mu_A,\mu_B\) be the stationary occupation means. Bulk drift for a vertex of shore \(A\) is \(\kappa v(\mu_B-\mu_A)\), while the reservoir drift is \(\gamma(\rho_A-\mu_A)\), with the analogous identity on \(B\). Solving gives

\[
\mu_A+\mu_B=\rho_A+\rho_B,\qquad
\delta:=\mu_A-\mu_B=\frac{\gamma\Delta}{\gamma+2\kappa v}.
\]

The signed current across \(A\to B\) is the number \(n^2\) of edges multiplied by the per-edge mean net rate \((v/n)\kappa(\mu_A-\mu_B)\), establishing the stated current formula.

**2. Closed second-moment equations.** Write \(a=\operatorname{Var}(\eta_i)\) on shore \(A\), \(b\) for shore \(B\), \(c\) for covariance of any two distinct sites on the same shore, and \(e\) for any cross-shore covariance. At first, use \(c_A,c_B\), with each satisfying the same stationary equation; hence they coincide. Set

\[
T=\kappa(\mu_A+\mu_B)+2\mu_A\mu_B,
\qquad
B_X=\gamma\rho_X+\gamma(1+2\rho_X/\kappa)\mu_X.
\]

For a cross-edge the simultaneous jumps change the product of its endpoint occupations with quadratic variation \(-(v/n)[\kappa(\eta_i+\eta_j)+2\eta_i\eta_j]\). Each site has reservoir quadratic variation with mean \(B_X\). Applying the generator to centered squares and centered products yields the exact equations

\[
\begin{aligned}
0&=-2(\gamma+\kappa v)a+2\kappa v e+v(T+2e)+B_A,\\
0&=-2(\gamma+\kappa v)b+2\kappa v e+v(T+2e)+B_B,\\
0&=-2(\gamma+\kappa v)c+2\kappa v e,\\
0&=-2(\gamma+\kappa v)e+\frac{\kappa v}{n}\big(a+b+2(n-1)c\big)-\frac{v}{n}(T+2e).
\end{aligned}
\]

These equations also hold at \(v=0\). The third gives \(c=\kappa v e/(\gamma+\kappa v)\), and elimination of \(a,b,c\) gives

\[
2\gamma[n(\gamma+2\kappa v)+v]e
=v\left[\frac{\kappa(B_A+B_B)}{2}-\gamma T\right].
\]

Using \(\mu_A+\mu_B=\rho_A+\rho_B\), the bracket divided by \(\gamma\) simplifies to

\[
\rho_A\mu_A+\rho_B\mu_B-2\mu_A\mu_B
=\frac{\delta(\Delta+\delta)}2
=\frac{\gamma(\gamma+\kappa v)\Delta^2}{(\gamma+2\kappa v)^2}.
\]

Substitution yields the announced rational formula for \(e=C_{AB}\) and \(c=C_{AA}=C_{BB}\). The linear system has no ambiguity because \(\gamma>0\) makes each displayed denominator positive.

**3. Unique rate optimum.** With \(x=\kappa v/\gamma\), the covariance becomes

\[
e(x)=\frac{\Delta^2}{2\kappa}\,
\frac{x(1+x)}{(1+2x)^2\,[n+(2n+1/\kappa)x]}.
\]

For \(\Delta\ne0\) its derivative has the sign of

\[
\kappa n-(2\kappa n+1)x^2(2x+3).
\]

The second term increases strictly from zero to infinity on \(x>0\), so the derivative changes sign exactly once, from positive to negative. The end limits are zero, proving the unique global maximum. Dividing the optimality equation by \(n\) and sending \(n\to\infty\) gives \(2x^2(2x+3)=1\), whose unique positive root is \((\sqrt3-1)/2\). By contrast, the derivative of \(v/(\gamma+2\kappa v)\) is positive, proving strict growth of current magnitude for \(\Delta\ne0\).

## Verification

`CHECK.py` independently constructs the **unsymmetrized**, full \(2n\)-site degree-at-most-two polynomial generator, solves all first- and second-moment stationary equations over exact rational numbers, and compares every cross-shore and within-shore covariance against the claimed formulas. It checks four parameter choices with \(n=2,3\), including unequal and equal baths, and a variety of \(\kappa,\gamma,v\). This checks the reduction, not an infinite-size theorem. Replay with `python CHECK.py` (Python 3 with SymPy); the all-size proof is the generator calculation above.

## Relationship to prior work

Giardinà, Redig and Vafayi (2009), Sections 2 and 8, introduce the inclusion generator and show positivity of boundary-driven stationary correlations for a chain with reservoirs at its ends. Floreani, Redig and Sau (2020), Sections 2 and 5, prove a universal reservoir-contrast factorization for stationary cumulants in general graphs contacted by two distinguished reservoirs. Neither of these explicit statements gives the rational cross-shore covariance for the present all-site reservoir geometry, its universal within-shore ratio, nor the unique finite-rate optimizer. Kim and Sau (2026) study spectral gaps for nonconservative inclusion networks rather than this stationary covariance and its optimum.

These prior works supply foundations and broad qualitative constraints. The exact formula here is consistent with their positive-correlation and squared-reservoir-contrast laws, rather than claiming those facts as original. Any earlier equivalent closed calculation, particularly for bipartite all-site reservoir networks, would supersede the claimed novelty.

## Limitations

This is an equal-time second-moment result for a symmetric inclusion process with homogeneous complete bipartite hopping, fixed positive inclusion parameter, and sitewise linear birth/death reservoirs. The stationary distribution itself, higher cumulants, non-bipartite geometries, arbitrary reservoir heterogeneity, and nonstationary correlations are not determined. The exact finite rate optimum is specific to the cross-shore covariance observable; its claim is not extended to every other covariance or current statistic. This is a mathematical stochastic model, not a calibrated experimental transport prediction. Historical priority is subject to further independent literature verification.

## References

1. C. Giardinà, F. Redig and K. Vafayi, *The inclusion process: duality and correlation inequalities*, arXiv:0906.4664, first public 2009-06-25. https://arxiv.org/abs/0906.4664
2. S. Floreani, F. Redig and F. Sau, *Orthogonal polynomial duality of boundary driven particle systems and non-equilibrium correlations*, arXiv:2007.08272, 2020. https://arxiv.org/abs/2007.08272
3. S. Kim and F. Sau, *One- and Two-Particle Spectral Gap Identities for the Symmetric Inclusion Process and Related Models*, Communications in Mathematical Physics 407 (2026), article 225. https://doi.org/10.1007/s00220-026-05728-9
