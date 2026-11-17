# No prime-two orbits and unconditional endemic Schur stability in one-stage exact-round contagion

## Finding

For the deterministic exact-round competing-risk model of Muñoz, Nuño and Meacci with **one-stage adoption** \(p=1\), positive contact intensity \(\rho\), turnover \(\nu\), and dimensionless round length \(\tau\), **every period-dividing-two point is fixed, for every positive parameter choice**. The disease-free state is globally attracting at or below the known invasion threshold; strictly above it there is precisely one positive equilibrium and that equilibrium is locally exponentially attracting (Schur stable) for *every* finite round length. Neither an endemic flip bifurcation nor a prime-two cycle can occur in this one-stage limit.

The no-two-cycle conclusion holds more generally for the probability-preserving class
\[
F(a,r)=\bigl(ea+H(a)(1-a-r),\ ta+zr\bigr),
\]
acting on \(\mathcal T=\{(a,r):a\ge0,r\ge0,a+r\le1\}\), whenever \(0\le e,z<1\), \(0<t\le1-e\), and \(H:[0,1]\to[0,1]\) is nondecreasing. This structural monotonicity hypothesis is significant: a smooth probability-valued nonmonotone response within the same transition scheme has the exact prime-two orbit \((1/2,9/40)\leftrightarrow(1/5,3/10)\).

## Assumptions and scope

The original population fractions are \((s_0,s_1,a,r)\), summing to one and nonnegative, with \(a\) the adopter fraction and \(r\) the inactive fraction. Write
\[
\kappa=1-e^{-(1+\nu)\tau},\quad e=1-\kappa,\quad z=e^{-\nu\tau},\quad
t=\frac{\kappa}{1+\nu},\quad c=\frac{\rho\kappa}{1+\nu},\quad m=\nu\tau,
\]
and let the competing-risk probability of an adoption attempt be
\[
H(a)=\frac{ca}{ca+m}\left(1-e^{-(ca+m)}\right).
\]
At \(p=1\) the map of the motivating paper is precisely
\[
 a'=ea+H(a)(s_0+s_1),\qquad r'=ta+zr,\qquad
 s_1'=e^{-(ca+m)}s_1,
\]
with \(s_0'=1-s_1'-a'-r'\). Hence \((a,r)\) obeys \(F\) above even when initially \(s_1>0\). In the original model \(0<e,z<1\), \(0<t<1-e\), and \(H\) is smooth, strictly increasing, and strictly between zero and one for positive \(a\).

The already known disease-free linear invasion threshold (Proposition 4 of the motivating paper) is
\[
 \mathcal R_\tau=\frac{\rho}{1+\nu}\frac{1-e^{-\nu\tau}}{\nu\tau}=1.
\]
Our global prime-two obstruction and all-parameter endemic stability are the principal results; the threshold formula itself is not claimed as new. All assertions refer to the deterministic large-population map and to biological simplex states, not to deterministic extinction of the finite-population Markov chain.

## Proof

**(1) Probability preservation and reduction.** For the general class, the three transition probabilities from an adopter are \(e,t,1-e-t\), from an inactive individual \(z,1-z\), and from a susceptible \(H(a),1-H(a)\). They lie in \([0,1]\). Therefore \(F(\mathcal T)\subseteq\mathcal T\). For the original four-class map, \(s_1'=e^{-(ca+m)}s_1\) with a factor no larger than \(e^{-m}<1\). Thus no periodic orbit can have \(s_1>0\), and studying \(F\) already determines all periodic points of order at most two.

**(2) Global obstruction to a prime-two orbit.** Suppose \(F(a_0,r_0)=(a_1,r_1)\) and \(F(a_1,r_1)=(a_0,r_0)\). Subtracting the inactive-fraction equations gives
\[
(1+z)(r_1-r_0)=t(a_0-a_1).
\]
If \(a_0=a_1\), it follows that \(r_0=r_1\); the orbit is fixed. Otherwise exchange indices to arrange \(\Delta=a_0-a_1>0\). With \(s_i=1-a_i-r_i\),
\[
r_1-r_0=\frac{t\Delta}{1+z},\qquad
s_1-s_0=\left(1-\frac{t}{1+z}\right)\Delta.
\]
By subtracting the two adopter equations,
\[
-(1+e)\Delta=H(a_0)s_0-H(a_1)s_1.
\]
Since \(H\) is nondecreasing, \(s_0\ge0\), and \(0\le H(a_1)\le1\), the right side is at least
\[
-H(a_1)(s_1-s_0)\ge-\left(1-\frac{t}{1+z}\right)\Delta.
\]
This contradicts \(1+e>1-t/(1+z)\). No primitive period-two point exists anywhere in \(\mathcal T\), including its boundary; differentiability of \(H\) is not needed.

**(3) The exact competing-risk response, endemic uniqueness, and extinction.** Set \(L=ca\) and \(B=L+m\). Direct differentiation gives
\[
\frac{dH}{dL}=\frac{m(1-e^{-B})}{B^2}+\frac{L e^{-B}}B>0,
\]
whereas
\[
\frac{H(a)}a=c\frac{1-e^{-B}}{B}=c\int_0^1e^{-Bu}\,du
\]
is strictly decreasing for \(a>0\). In particular \(0<aH'(a)<H(a)\) at positive \(a\).

At an equilibrium, \(r=ta/(1-z)\). Put \(C=1+t/(1-z)>1\). Every positive equilibrium has \(0<a<1/C\) and satisfies
\[
\frac{H(a)}a(1-Ca)=1-e.
\]
The left side is strictly decreasing from \(H'(0)\) to zero. Thus there is **exactly one** positive equilibrium if \(e+H'(0)>1\), and none otherwise. Here
\[
H'(0)=\frac{\rho\kappa}{1+\nu}\frac{1-e^{-m}}m,
\]
so this is precisely the known condition \(\mathcal R_\tau>1\). At or below threshold, \(a'\le(e+H'(0))a\), with strict inequality for \(a>0\) at equality. Consequently \(a_n\to0\), then \(r_n\to0\) and \(s_{1,n}\to0\), establishing global attraction to the disease-free point. This extinction argument does not assert a universal exponential rate at equality.

**(4) All-parameter endemic local stability.** At the positive equilibrium let \(h=H(a)>0\), \(\eta=aH'(a)/H(a)\), so \(0<\eta<1\). The planar Jacobian has the form
\[
J=\begin{pmatrix} A&-h\\t&z\end{pmatrix},\qquad
A=e-h+(1-e)\eta.
\]
In particular \(-1<A<1-h\). Its characteristic polynomial satisfies the three strict Schur--Jury inequalities
\[
\begin{aligned}
1-\operatorname{tr}J+\det J&=(1-A)(1-z)+th>0,\\
1+\operatorname{tr}J+\det J&=(1+A)(1+z)+th>0,\\
1-\det J&=1-zA-th>0.
\end{aligned}
\]
For the last inequality, \(zA+th<z+(t-z)h\le\max\{z,t\}<1\). Thus both multipliers lie strictly inside the unit disk. The additional transverse multiplier in the full four-compartment simplex is \(e^{-(ca+m)}\in(0,1)\), so the full endemic equilibrium is locally exponentially attracting. Moreover, at any point where \(H\) is differentiable and nondecreasing, \(\det(I+J)=(1+e-H+H'(a)s)(1+z)+tH>0\), excluding a \(-1\) multiplier even outside equilibria.

**(5) A probability-admissible boundary witness.** Take \(e=1/4\), \(z=1/2\), \(t=3/8\), corresponding to \(\nu=1\) and \(\tau=\log 2\) in the original transition probabilities. Define the smooth bump
\[
B(x)=\begin{cases}\exp(1-(1-x^2)^{-1}),&|x|<1,\\0,&|x|\ge1,\end{cases}
\]
and the deliberately **nonmonotone** incidence law
\[
\widetilde H(a)=\frac9{10}B\bigl(20(a-1/5)\bigr)+\frac3{11}B\bigl(20(a-1/2)\bigr).
\]
Its supports are disjoint; \(0\le\widetilde H\le9/10\), \(\widetilde H(0)=0\), \(\widetilde H(1/5)=9/10\), and \(\widetilde H(1/2)=3/11\). Direct substitution gives
\[
F_{\widetilde H}(1/2,9/40)=(1/5,3/10),\quad
F_{\widetilde H}(1/5,3/10)=(1/2,9/40).
\]
All class-transition probabilities and both states are admissible. This counterexample is **not** a choice of the original exponential competing-risk law; it shows that probability admissibility alone cannot replace monotone incidence.

## Verification

The accompanying standalone script `checks/check_one_stage.py` verifies the exact rational orbit using `fractions.Fraction`, checks the smooth bump values, samples the derivative and nonflip inequalities for 4,000 reproducibly seeded positive parameter configurations, and tests the positive equilibrium equation and strict Jury inequalities on up to 1,200 additional configurations. The script prints a PASS line. Finite numerical tests only check the implementation; the all-parameter conclusions follow from parts (1)--(5).

## Relationship to prior work

Muñoz, Nuño and Meacci (2026), Definition 1 and Propositions 4--5, introduce this finite-round competing-risk map, give the invasion threshold and an equilibrium parametrization, and numerically report a stable one-stage regime. They do not establish a global prime-two exclusion or all-parameter Schur stability of its one-stage endemic state. The already established invasion threshold is used, not re-claimed.

Schreiber, Huang, Jiang and Wang (2021), Theorem 4.1, analyze a *different* exponential-escape discrete SIR recurrence and derive extinction/persistence results and global attraction for a parameter subset; their recurrence does not imply this theorem for the distinct competing-risk map. Zhou, Li and Wang (2014) establish flip bifurcations for an Euler-type incidence update with linear infection probabilities; that update is not the bounded competing-risk map considered here. None of these comparisons constitutes a guarantee against unindexed equivalent earlier theorems.

## Limitations

No exclusion of period three or higher, no global convergence theorem in the supercritical regime, no finite-population survival statement, and no extension to \(p<1\) is asserted. The nonmonotone comparison response is a deliberately modified infection law rather than an instance of the original exponential response. The result has undergone a self-review but no independent mathematical audit.

## References

1. F. J. Muñoz, J. C. Nuño and L. Meacci, *From elementary processes to chaos: a discrete-time two-stage contagion model and its continuous limit*, arXiv:2611.08353v1, 5 November 2026, https://arxiv.org/html/2611.08353v1 .
2. S. J. Schreiber, S. Huang, J. Jiang and H. Wang, *Extinction and Quasi-Stationarity for Discrete-Time, Endemic SIS and SIR Models*, SIAM Journal on Applied Mathematics **81** (2021), 2195--2217, https://doi.org/10.1137/20M1339015 .
3. X. Zhou, X. Li and W.-S. Wang, *Bifurcations for a deterministic SIR epidemic model in discrete time*, Advances in Difference Equations (2014), article 168, https://doi.org/10.1186/1687-1847-2014-168 .
