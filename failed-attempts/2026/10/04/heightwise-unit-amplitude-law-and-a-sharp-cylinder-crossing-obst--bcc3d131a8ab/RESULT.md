# Heightwise unit-amplitude law and a sharp cylinder-crossing obstruction in the Sprott C flow
## Finding
Consider the canonical Sprott C system
\[
\dot x=yz,\qquad
\dot y=x-y,\qquad
\dot z=1-x^2.
\]

Every compactly supported invariant probability measure \(\mu\) satisfies the heightwise conditional law
\[
\mathbb E_\mu[x^2\mid z]=1.
\]
It also satisfies the exact derivative-energy partition
\[
\mathbb E_\mu[y^2]+\mathbb E_\mu[(x-y)^2]=1,
\]
or, since \(\dot y=x-y\),
\[
\mathbb E_\mu[y^2]+\mathbb E_\mu[\dot y^{\,2}]=1.
\]

Consequently
\[
0<\mathbb E_\mu[y^2]\le 1.
\]
The endpoint \(\mathbb E_\mu[y^2]=1\) occurs exactly for convex mixtures of the two equilibrium atoms
\[
(1,1,0),\qquad (-1,-1,0).
\]

Every other compact invariant probability measure assigns positive mass to both regions
\[
|x|<1
\qquad\text{and}\qquad
|x|>1.
\]
Hence every nonconstant periodic orbit crosses the cylinder
\[
|x|=1
\]
at least twice in each least period.

## Assumptions and scope
The measure statements concern Borel probability measures invariant under the complete flow and supported on a compact subset of \(\mathbb R^3\). Compact support guarantees integrability of the polynomial generator identities used below.

The equations are Sprott's case C from the 1994 catalogue. Sprott's own public catalogue records exactly
\[
\dot x=yz,\qquad \dot y=x-y,\qquad \dot z=1-x^2.
\]
A later global study embeds cases B and C in the two-parameter Sprott BC family and classifies that work primarily under MSC 34C05 and 34C45.

## Proof
Let \(L\) denote the Lie derivative along the vector field. For an invariant compactly supported probability measure,
\[
\int Lf\,d\mu=0
\]
for every continuously differentiable test function used below.

Take \(f=h(z)\). Then
\[
Lh(z)=h'(z)(1-x^2).
\]
Because the \(z\)-projection of the support is compact, every continuous function \(\phi(z)\) on that projection has a continuously differentiable antiderivative on a containing interval. Hence
\[
\int \phi(z)(1-x^2)\,d\mu=0
\]
for every continuous \(\phi\), which is exactly
\[
\mathbb E_\mu[x^2\mid z]=1.
\]
In particular,
\[
\mathbb E_\mu[x^2]=1.
\]

Next,
\[
L(y^2)=2y(x-y),
\]
so stationarity gives
\[
\mathbb E_\mu[xy]=\mathbb E_\mu[y^2].
\]
Therefore
\[
\begin{aligned}
\mathbb E_\mu[(x-y)^2]
&=\mathbb E_\mu[x^2]-2\mathbb E_\mu[xy]+\mathbb E_\mu[y^2]\\
&=1-\mathbb E_\mu[y^2].
\end{aligned}
\]
Since \(\dot y=x-y\), this is the stated derivative-energy partition.

The lower endpoint cannot occur. If \(\mathbb E_\mu[y^2]=0\), then \(y=0\) almost surely. But
\[
L(xy)=y^2z+x^2-xy,
\]
so stationarity would give
\[
0=\mathbb E_\mu[L(xy)]=\mathbb E_\mu[x^2]=1,
\]
a contradiction. Thus
\[
0<\mathbb E_\mu[y^2]\le1.
\]

Suppose now that \(\mathbb E_\mu[y^2]=1\). Then
\[
\mathbb E_\mu[(x-y)^2]=0,
\]
so the support lies in \(x=y\). The conditional law gives \(\mathbb E_\mu[x^2]=1\), and because \(x=y\), stationarity together with support invariance forces the vector field to be tangent to the plane \(x=y\). On that plane,
\[
\frac{d}{dt}(x-y)=yz.
\]
Any support point with \(y\ne0\) therefore requires \(z=0\). The relation \(x=y\), compact invariance, and \(\dot z=1-x^2\) then force \(x^2=1\). Hence the support is contained in the two equilibria \((1,1,0)\) and \((-1,-1,0)\). Conversely every convex mixture of those two equilibrium atoms is invariant and attains equality.

Finally, suppose a compact invariant measure is not supported on those two equilibria. If \(x^2=1\) almost surely, support invariance would keep each complete support trajectory in the two planes \(x=\pm1\). There \(\dot z=0\); compact completeness and \(\dot y=x-y\) force \(y=x\), and then \(\dot x=yz\) forces \(z=0\). Thus only the two equilibria remain, contrary to assumption. Hence \(x^2-1\) is not almost surely zero.

But
\[
\mathbb E_\mu[x^2-1]=0.
\]
A nonzero integrable function with zero mean cannot have only one sign. Therefore
\[
\mu(|x|<1)>0,\qquad \mu(|x|>1)>0.
\]
For the invariant measure supported on a nonconstant periodic orbit, continuity of \(x^2-1\) then forces at least two zeros on the periodic circle, proving the cylinder-crossing statement.

## Verification
The accompanying checker uses exact sparse-polynomial arithmetic over rational coefficients. It verifies
\[
Lz=1-x^2,
\]
\[
L(y^2)=2y(x-y),
\]
and
\[
L(xy)=y^2z+x^2-xy.
\]
It also verifies algebraically that
\[
x^2-2xy+y^2
=
x^2-y^2-2y(x-y),
\]
the polynomial identity underlying the stationary energy partition.

The stored checker output is `VERIFY_OK`.

The conditional-expectation step is an infinite-dimensional measure argument, not a finite experiment: it uses the generator identity for arbitrary continuous functions of \(z\) through antiderivatives. The equality and cylinder-crossing steps use invariance of the support under the continuous flow.

## Relationship to prior work
Sprott's 1994 paper introduced case C among nineteen algebraically simple chaotic flows. Sprott's public catalogue gives the exact case C equations used here.

Wei and Pehlivan studied a generalized Sprott C family
\[
\dot X=a(Y-X),\qquad
\dot Y=-cY-XZ,\qquad
\dot Z=Y^2-b.
\]
Their full four-page paper states that when \(c=0\) and the remaining parameters satisfy the stated positive relation, the generalized system is topologically equivalent to the original Sprott C system. Their focus is coexistence of chaotic attractors, stable equilibria, Lyapunov exponents, and circuit realization.

Mota and Oliveira later studied the Sprott BC family
\[
\dot x=yz,\qquad
\dot y=x-y,\qquad
\dot z=1-x(\alpha y+\beta x),
\]
which contains Sprott B and C at the ends of its parameter spectrum. Their published abstract emphasizes finite and infinite singularities, Hopf bifurcation, Poincaré compactification, and nonexistence of polynomial/Darboux first integrals.

The final claim is different in implication: it constrains every compact invariant probability measure of the canonical case C, including measures on periodic orbits, invariant tori if present, and more complicated compact recurrent sets. Targeted published-finding corpus searches for Sprott C, its aliases, stationary moments, conditional laws, derivative-energy identities, and the \(|x|=1\) cylinder returned no same-object result implying this theorem.

## Limitations
The theorem is for the canonical Sprott C system, not for the whole generalized Sprott C or Sprott BC parameter families.

The conditional identity does not classify all invariant measures and does not prove existence or uniqueness of a chaotic physical measure. The cylinder statement is a necessary recurrence condition, not a localization theorem for an attractor.

The 2012 Nonlinear Dynamics article with the closest generalized-system title was available only at abstract/metadata level in this run. An authorized institutional retrieval attempt required interactive human input and therefore could not be completed in the non-interactive execution. The separate 2012 Wei–Pehlivan paper was inspected through its public four-page PDF text, including the generalized equations, the equivalence statement, and its conclusion. A page-render attempt timed out, so no claim relies on visual features of that PDF.

Targeted search cannot exclude differently phrased or unindexed older stationary identities.

## References
1. J. C. Sprott, “Some simple chaotic flows,” Physical Review E 50, R647–R650 (1994), DOI 10.1103/PhysRevE.50.R647. Published 1994-08-01.
2. J. C. Sprott, “Simple Chaotic Flow GIF Animations,” public case catalogue, https://sprott.physics.wisc.edu/simplest.htm.
3. Z. Wei and Q. Yang, “Dynamical analysis of the generalized Sprott C system with only two stable equilibria,” Nonlinear Dynamics 68, 543–554 (2012), DOI 10.1007/s11071-011-0235-8.
4. Z. Wei and I. Pehlivan, “Chaos, coexisting attractors, and circuit design of the generalized Sprott C system with only two stable equilibria,” Optoelectronics and Advanced Materials – Rapid Communications 6, 742–745 (2012).
5. M. C. Mota and R. D. S. Oliveira, “Dynamic aspects of Sprott BC chaotic system,” Discrete and Continuous Dynamical Systems - B 26, 1653–1673 (2021), DOI 10.3934/dcdsb.2020177.
