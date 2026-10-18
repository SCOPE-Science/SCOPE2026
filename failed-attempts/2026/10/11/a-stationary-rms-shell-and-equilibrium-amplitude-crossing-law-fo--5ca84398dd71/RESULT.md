# A stationary RMS shell and equilibrium-amplitude crossing law for the Michelson system
## Finding
Consider the Michelson system
\[
\dot x=y,
\qquad
\dot y=z,
\qquad
\dot z=c^2-y-\frac12x^2,
\qquad
c>0.
\]

Let \(\mu\) be any compactly supported invariant Borel probability measure. Then the three coordinate levels satisfy
\[
\boxed{\mathbb E_\mu[y\mid x]=0},
\qquad
\boxed{\mathbb E_\mu[z\mid y]=0},
\]
and
\[
\boxed{\mathbb E_\mu[x^2+2y\mid z]=2c^2}.
\]

In particular,
\[
\mathbb E_\mu[y]=\mathbb E_\mu[z]=0,
\qquad
\boxed{\mathbb E_\mu[x^2]=2c^2}.
\]
Thus every compact stationary state has the same exact root-mean-square \(x\)-amplitude,
\[
\operatorname{RMS}_\mu(x)=\sqrt2\,c.
\]

Writing
\[
m=\int x\,d\mu,
\]
the barycenter is \((m,0,0)\) and
\[
\boxed{\operatorname{Var}_\mu(x)=2c^2-m^2}.
\]
Hence
\[
|m|\le\sqrt2\,c
\]
and
\[
\boxed{\operatorname{Var}_\mu(x)\le2c^2}.
\]

The endpoints are rigid. If \(|m|=\sqrt2c\), then \(\mu\) is the atom at the corresponding equilibrium
\[
p_\pm=(\pm\sqrt2c,0,0).
\]
The variance maximum is sharp and is attained by
\[
\frac12\delta_{p_-}+\frac12\delta_{p_+}.
\]

More strongly, every compact invariant probability measure not supported on the two equilibria satisfies
\[
\boxed{\mu\{|x|<\sqrt2c\}>0}
\]
and
\[
\boxed{\mu\{|x|>\sqrt2c\}>0}.
\]
Thus every genuinely recurrent stationary state straddles the equilibrium amplitude. In particular, every nonconstant periodic orbit spends positive time on both sides of the threshold and crosses
\[
|x|=\sqrt2c
\]
at least twice during each least period.

There is also an exact vertical-speed defect. Define
\[
Q=x^2+2y.
\]
The fiber law gives
\[
\mathbb E_\mu[Q\mid z]=2c^2,
\]
while the differential equation gives
\[
Q-2c^2=-2\dot z.
\]
Therefore
\[
\boxed{\operatorname{Var}_\mu(Q)=4\mathbb E_\mu[\dot z^2]}
\]
and
\[
\boxed{\operatorname{Cov}_\mu(z,Q)=0}.
\]
The speed defect vanishes exactly for invariant measures supported on \(\{p_-,p_+\}\).

## Assumptions and scope
The theorem concerns the reversible three-dimensional Michelson flow associated with the steady Kuramoto–Sivashinsky equation. Compact support is used to justify the polynomial and antiderivative generator tests and to invoke bounded completeness on invariant support.

The original 1986 Michelson article is publicly resolved to February 1986 in the checked journal metadata, not to a day. No day was invented. The structured date field therefore uses 5 December 2006, the earliest checked same-object source with a verified day-level publication date. This leaves the work safely in the archive cohort.

A same-object mathematical bibliographic record classifies the Michelson system under MSC \(34C37\), together with dynamical-systems codes in class \(37\). The present result uses primary MSC \(34C37\).

No ergodicity or symmetry of \(\mu\) is assumed.

## Proof
Let \(L\) be the generator.

For any continuous function \(\phi\) on the compact \(x\)-projection of the support, choose an antiderivative \(H\) with \(H'(x)=\phi(x)\). Then
\[
LH=\phi(x)y.
\]
Invariance implies
\[
\mathbb E[\phi(x)y]=0
\]
for every such \(\phi\), hence
\[
\mathbb E[y\mid x]=0.
\]

The same argument with antiderivatives of \(y\) yields
\[
\mathbb E[z\mid y]=0.
\]
With antiderivatives of \(z\), invariance gives
\[
\mathbb E\!\left[c^2-y-\frac12x^2\mid z\right]=0,
\]
so
\[
\mathbb E[x^2+2y\mid z]=2c^2.
\]

Taking expectations in the first two laws gives
\[
\mathbb E[y]=\mathbb E[z]=0.
\]
Taking expectations in the third therefore gives
\[
\mathbb E[x^2]=2c^2.
\]
For \(m=\mathbb E[x]\),
\[
\operatorname{Var}(x)=2c^2-m^2,
\]
and variance nonnegativity gives \(|m|\le\sqrt2c\).

If \(|m|=\sqrt2c\), then \(\operatorname{Var}(x)=0\), so \(x\) is constant on invariant support. Since \(\dot x=y\), one has \(y=0\); since \(\dot y=z\), one has \(z=0\); and then \(\dot z=0\) gives \(x^2=2c^2\). Hence the measure is the corresponding equilibrium atom.

The equal mixture of the two equilibrium atoms has mean zero and \(x\)-variance \(2c^2\), proving sharpness.

Now suppose a stationary measure is not equilibrium-supported. If
\[
\mu\{|x|<\sqrt2c\}=0,
\]
then \(x^2\ge2c^2\) almost surely. Since its expectation equals \(2c^2\), equality holds almost surely, so support lies in \(x^2=2c^2\). Invariance then forces \(y=z=0\), hence equilibrium support, a contradiction. The same argument with \(x^2\le2c^2\) proves positive mass outside the threshold.

For a nonconstant periodic orbit, the normalized time measure is not equilibrium-supported, so the continuous function \(|x(t)|\) takes values both below and above \(\sqrt2c\). Periodicity and continuity force at least two threshold crossings per least period.

Finally, with \(Q=x^2+2y\),
\[
Q-2c^2=-2\dot z.
\]
The conditional law says \(\mathbb E[Q-2c^2\mid z]=0\), hence the residual is orthogonal to every function of \(z\). Therefore
\[
\operatorname{Var}(Q)=4\mathbb E[\dot z^2]
\]
and
\[
\operatorname{Cov}(z,Q)=0.
\]
If the defect is zero, \(z\) is constant on invariant support. Then bounded completeness and \(\dot y=z\) force \(z=0\); bounded completeness and \(\dot x=y\) then force \(y=0\); finally \(x^2=2c^2\). Thus the measure is equilibrium-supported. The converse is immediate.

## Verification
The accompanying exact checker verifies the pointwise residual relation, the stationary shell algebra, the variance envelope, and the equilibrium-threshold identities using rational arithmetic after treating \(c^2\) as the fundamental positive parameter.

It verifies
\[
\mathbb E[x^2]=2c^2,
\qquad
\operatorname{Var}(x)=2c^2-m^2,
\]
and
\[
Q-2c^2=-2\dot z.
\]
The stored checker output is `VERIFY_OK`.

No finite numerical trajectory is used to prove an invariant-measure statement.

## Relationship to prior work
Michelson's original article derives the steady Kuramoto–Sivashinsky ODE
\[
x'''+x'+\frac12x^2=c^2
\]
and its first-order flow, then studies bounded solutions, periodic branches, invariant tori, asymptotic solutions, and complicated recurrent dynamics. The complete article was inspected. Its statistical discussions concern other averages in the quasi-periodic construction; no all-invariant-measures fixed RMS shell or equilibrium-amplitude straddling theorem was located.

Wilczak's complete 2006 article studies the same Michelson equation at \(c=1\), including two rigorously established odd periodic orbits and infinitely many homoclinic and heteroclinic connections. Its theorems concern covering relations and orbit connections, not stationary moments.

Later rigorous work verifies cocoon bifurcations and classifies the same system under MSC \(34C37\) and related dynamical-systems codes.

Published semantic searches compared direct formulations involving invariant measures, exact RMS amplitude, mean-square \(x\), barycenter variance, conditional expectations, and the equilibrium-amplitude threshold. No checked same-object record implied the accepted shell or crossing law.

## Limitations
The theorem is conditional on compactly supported invariant probability measures. It does not classify which invariant measures exist for a given \(c\).

It fixes only the second moment of \(x\), not the full invariant distribution or the moments of \(y\) and \(z\).

The crossing statement is asserted for nonconstant periodic orbits and the positive-mass straddling statement for invariant probability measures; it is not a claim about arbitrary nonrecurrent complete trajectories.

The original publication has only month-level date resolution in the checked metadata, so a later day-resolved same-object source is used in the structured date field rather than inventing a date.

The exact shell follows from a short invariant-measure calculation, so an equivalent observation could remain in unindexed literature.

## References
1. D. Michelson, “Steady solutions of the Kuramoto–Sivashinsky equation,” Physica D 19, 89–111 (1986), DOI 10.1016/0167-2789(86)90055-2.
2. D. Wilczak, “Symmetric homoclinic solutions to the periodic orbits in the Michelson system,” Topological Methods in Nonlinear Analysis 28, 155–170 (2006).
3. H. Kokubu, D. Wilczak, and P. Zgliczyński, “Rigorous verification of cocoon bifurcations in the Michelson system,” Nonlinearity 20 (2007), DOI 10.1088/0951-7715/20/9/008.
