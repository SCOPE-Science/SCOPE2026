# Fiberwise amplitude calibration and an outer-height recurrence barrier in the Shimizu–Morioka flow
## Finding
Consider the Shimizu–Morioka system
\[
\dot x=y,
\qquad
\dot y=x(1-z)-\lambda y,
\qquad
\dot z=-\alpha z+x^2,
\]
with
\[
\alpha>0,
\qquad
\lambda>0.
\]

Let \(\mu\) be any compactly supported invariant Borel probability measure. Then
\[
\boxed{\mathbb E_\mu[y\mid x]=0}
\]
and, more importantly,
\[
\boxed{\mathbb E_\mu[x^2\mid z]=\alpha z}.
\]

Thus the squared horizontal amplitude is calibrated separately on every height fiber. The second identity is equivalently the infinite family
\[
\boxed{
\mathbb E_\mu[(x^2-\alpha z)g(z)]=0
}
\]
for every bounded Borel function \(g\).

The corresponding conditional-variance decomposition is
\[
\boxed{
\operatorname{Var}_\mu(x^2)
-
\alpha^2\operatorname{Var}_\mu(z)
=
\mathbb E_\mu[\dot z^2]
}.
\]
The same calibration also fixes the covariance:
\[
\boxed{
\operatorname{Cov}_\mu(x^2,z)
=
\alpha\operatorname{Var}_\mu(z)
}.
\]

A second exact balance is obtained from \(xy\):
\[
\boxed{
\operatorname{Var}_\mu(y)
=
\alpha\mathbb E_\mu[z(z-1)]
}.
\]

These formulas have a geometric consequence. Every compact stationary state is supported in
\[
\boxed{z\ge0}.
\]
If \(\mu\) is not supported on equilibria, then
\[
\boxed{\mu\{z>1\}>0}.
\]
The height \(z=1\) is exactly the common height of the two nonzero equilibria
\[
P_\pm=(\pm\sqrt\alpha,0,1).
\]
Hence every nonconstant periodic orbit spends positive time above the outer-equilibrium height.

There is also a pointwise memory formula. Every bounded complete trajectory satisfies
\[
\boxed{
z(t)
=
\int_0^\infty e^{-\alpha s}x(t-s)^2\,ds
}.
\]
Consequently every bounded complete trajectory other than the origin obeys
\[
z(t)>0
\]
for every \(t\).

For the rigorously studied Lorenz-attractor parameter choice
\[
\alpha=0.45,
\qquad
\lambda=0.9,
\]
the theorem says that every compact invariant probability measure not supported on the three equilibria gives positive mass to the region \(z>1\), while its height fibers satisfy
\[
\mathbb E[x^2\mid z]=0.45z.
\]

## Assumptions and scope
The system is the standard Shimizu–Morioka normalization
\[
\dot x=y,
\qquad
\dot y=(1-z)x-\lambda y,
\qquad
\dot z=-\alpha z+x^2.
\]
The parameters satisfy \(\alpha,\lambda>0\).

Compact support guarantees that all polynomial observables and one-variable antiderivative tests used below are integrable. No ergodicity hypothesis is required. The statement applies to periodic-orbit measures, compact chaotic invariant measures, equilibrium mixtures, and any convex mixture of compact invariant measures.

The three equilibria for \(\alpha>0\) are
\[
O=(0,0,0),
\qquad
P_\pm=(\pm\sqrt\alpha,0,1).
\]

The model was introduced by Shimizu and Morioka in an article dated 31 March 1980. A rigorous same-object mathematical treatment classifies the problem under MSC \(34C23\), among related dynamical-systems codes.

## Proof
Let \(L\) be the generator of the flow.

Take any continuous function \(\phi\) on the compact \(x\)-range of the support and choose an antiderivative \(H\) with
\[
H'(x)=\phi(x).
\]
Then
\[
LH=\phi(x)y.
\]
Invariance gives
\[
\mathbb E_\mu[\phi(x)y]=0
\]
for every \(\phi\), hence
\[
\mathbb E_\mu[y\mid x]=0.
\]
In particular,
\[
\mathbb E[y]=0,
\qquad
\mathbb E[xy]=0.
\]

Now take a continuous function \(\psi\) on the compact \(z\)-range and an antiderivative \(K\) with
\[
K'(z)=\psi(z).
\]
Then
\[
LK
=
\psi(z)(x^2-\alpha z).
\]
Invariance therefore gives
\[
\mathbb E_\mu[\psi(z)(x^2-\alpha z)]=0
\]
for every \(\psi\), so
\[
\mathbb E_\mu[x^2\mid z]=\alpha z.
\]
A monotone-class extension gives the displayed identity for every bounded Borel function of \(z\).

Because the left-hand side is a conditional expectation of the nonnegative random variable \(x^2\),
\[
\alpha z\ge0
\]
for the \(z\)-marginal almost everywhere. Since \(\alpha>0\),
\[
z\ge0
\]
almost surely, and therefore the support of \(\mu\) is contained in the closed half-space \(z\ge0\).

Set
\[
A=x^2,
\qquad
B=\alpha z.
\]
The conditional law says
\[
\mathbb E[A\mid z]=B.
\]
Thus the residual \(A-B\) is orthogonal to every square-integrable function of \(z\), and
\[
\operatorname{Var}(A)
=
\operatorname{Var}(B)
+
\mathbb E[(A-B)^2].
\]
Since
\[
A-B=\dot z,
\]
we obtain
\[
\operatorname{Var}(x^2)
-
\alpha^2\operatorname{Var}(z)
=
\mathbb E[\dot z^2].
\]
Likewise,
\[
\operatorname{Cov}(x^2,z)
=
\operatorname{Cov}(\mathbb E[x^2\mid z],z)
=
\alpha\operatorname{Var}(z).
\]

Next differentiate \(xy\):
\[
\frac{d}{dt}(xy)
=
y^2+x^2-\lambda xy-x^2z.
\]
Stationarity gives
\[
0
=
\mathbb E[y^2]
+
\mathbb E[x^2]
-
\lambda\mathbb E[xy]
-
\mathbb E[x^2z].
\]
The first fiber law gives \(\mathbb E[xy]=0\), while the height calibration gives
\[
\mathbb E[x^2]=\alpha\mathbb E[z]
\]
and
\[
\mathbb E[x^2z]=\alpha\mathbb E[z^2].
\]
Therefore
\[
\mathbb E[y^2]
=
\alpha\bigl(\mathbb E[z^2]-\mathbb E[z]\bigr)
=
\alpha\mathbb E[z(z-1)].
\]
Since \(\mathbb E[y]=0\), this is the stated variance identity.

We now classify the zero case. If
\[
\mathbb E[y^2]=0,
\]
then the invariant support lies in \(y=0\). Every point of the support has a complete bounded trajectory that remains in the support. Along such a trajectory,
\[
\dot x=0,
\]
so \(x\) is constant, and
\[
0=\dot y=x(1-z).
\]
If \(x=0\), then
\[
\dot z=-\alpha z.
\]
A complete bounded trajectory of this scalar equation must have \(z=0\). If \(x\ne0\), then \(z=1\), and the third equation forces
\[
x^2=\alpha.
\]
Hence the support is contained in
\[
\{O,P_+,P_-\}.
\]
Conversely, every measure supported on these equilibria has \(y=0\). Thus
\[
\mathbb E[y^2]>0
\]
exactly when the invariant measure is not equilibrium-supported.

For such a measure,
\[
\mathbb E[z(z-1)]>0.
\]
But \(z\ge0\) almost surely, and
\[
z(z-1)\le0
\]
on \(0\le z\le1\). Positive expectation is therefore impossible unless
\[
\mu\{z>1\}>0.
\]
This proves the outer-height recurrence barrier.

Finally solve the linear third equation along a bounded complete trajectory. For every \(T>0\),
\[
z(t)
=
e^{-\alpha T}z(t-T)
+
\int_0^T e^{-\alpha s}x(t-s)^2\,ds.
\]
Boundedness makes the first term tend to zero as \(T\to\infty\), yielding
\[
z(t)
=
\int_0^\infty e^{-\alpha s}x(t-s)^2\,ds.
\]
The integral is nonnegative. If it vanishes at one time, then \(x\) vanishes on the entire past half-orbit; uniqueness and bounded completeness force the origin trajectory. Thus every other bounded complete trajectory has strictly positive \(z(t)\) for all \(t\).

## Verification
The accompanying checker verifies the pointwise identities
\[
\dot z=x^2-\alpha z
\]
and
\[
\frac{d}{dt}(xy)
=
y^2+x^2-\lambda xy-x^2z.
\]
It also replays the moment substitution
\[
\mathbb E[xy]=0,
\quad
\mathbb E[x^2]=\alpha\mathbb E[z],
\quad
\mathbb E[x^2z]=\alpha\mathbb E[z^2]
\]
to recover
\[
\mathbb E[y^2]
=
\alpha\mathbb E[z(z-1)],
\]
and checks the abstract conditional-variance and covariance decompositions.

The stored checker output is `VERIFY_OK`.

The conditional-expectation statements, support conclusion, equality classification, and outer-height barrier are analytic consequences of invariance and are not inferred from finite numerical trajectories.

## Relationship to prior work
Shimizu and Morioka introduced the model in 1980 as a tractable system exhibiting the symmetric-to-asymmetric limit-cycle bifurcation pattern associated with the Lorenz problem. Their complete four-page article develops perturbative periodic solutions and the bifurcation of those cycles.

Messias, Gouveia, and Pessoa later analyze global dynamics of the exact standard equations through Poincaré compactification, behavior at infinity, and degenerate heteroclinic cycles. Their full author-posted text writes the same system and develops global orbit geometry. Searches of that text found no invariant-measure, moment, or average theorem matching the present conditional law.

Capiński, Turaev, and Zgliczyński give a rigorous computer-assisted proof that the exact Shimizu–Morioka system has a Lorenz attractor for an open parameter set. Their complete open preprint writes the standard equations with \(\alpha,\lambda>0\), includes the representative parameters \(\alpha=0.45\), \(\lambda=0.9\), and classifies the problem under MSC \(34C23\) among related codes. Full-document searches found no `invariant measure`, `conditional`, `covariance`, or `average` formulation matching the accepted result.

Huang, Shi, and Li study the same system from Darboux and differential-Galois integrability viewpoints. Their stated results concern first integrals and integrability, not stationary conditional moments.

The accepted statement is therefore not a claim about existence of the Lorenz attractor, homoclinic bifurcation, integrability, or dynamics at infinity. It is an all-invariant-measures calibration of squared amplitude by height, together with an exact moment identity forcing every non-equilibrium stationary regime above the outer-equilibrium height \(z=1\).

## Limitations
Compact support is assumed. The pointwise memory formula applies to bounded complete trajectories, but the theorem does not classify unbounded solutions.

The conditional law
\[
\mathbb E[x^2\mid z]=\alpha z
\]
fixes only the first conditional moment of \(x^2\), not the complete conditional distribution of \(x\).

The recurrence barrier proves positive stationary mass above \(z=1\); it does not prove that a general non-equilibrium stationary state has positive mass below \(z=1\).

The theorem does not determine entropy, Lyapunov exponents, topological conjugacy, periods, or the parameter boundary of Lorenz-attractor existence.

Because the generator calculation is short, a differently phrased equivalent observation could remain in unindexed literature.

## References
1. T. Shimizu and N. Morioka, “On the bifurcation of a symmetric limit cycle to an asymmetric one in a simple model,” Physics Letters A 76, 201–204 (1980), DOI 10.1016/0375-9601(80)90466-1.
2. M. Messias, M. R. A. Gouveia, and C. Pessoa, “Dynamics at infinity and other global dynamical aspects of Shimizu–Morioka equations,” Nonlinear Dynamics 69, 577–587 (2012), DOI 10.1007/s11071-011-0288-8.
3. M. J. Capiński, D. Turaev, and P. Zgliczyński, “Computer assisted proof of the existence of the Lorenz attractor in the Shimizu-Morioka system,” Nonlinearity 31, 5410–5440 (2018), DOI 10.1088/1361-6544/aae032; arXiv:1711.10404.
4. K. Huang, S. Shi, and W. Li, “Integrability analysis of the Shimizu-Morioka system,” Communications in Nonlinear Science and Numerical Simulation 84, 105101 (2020), DOI 10.1016/j.cnsns.2019.105101.
