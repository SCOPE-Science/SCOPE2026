# Exact stationary RMS shell and crossing rigidity for the classical Sprott B flow
## Finding
For the classical Sprott B system
\[
\dot x=yz,\qquad \dot y=x-y,\qquad \dot z=1-xy,
\]
every compactly supported invariant Borel probability measure \(\mu\) obeys the two fiberwise stationary laws
\[
\mathbb E_\mu[x\mid y]=y,\qquad \mathbb E_\mu[xy\mid z]=1.
\]
In particular,
\[
\mathbb E_\mu[y^2]=1,
\]
so the \(y\)-coordinate has an exact state-independent root-mean-square amplitude equal to \(1\). The same identities give the exact nonnegative activity defect
\[
\mathbb E_\mu[x^2]-1
=\mathbb E_\mu[(x-y)^2]
=\mathbb E_\mu[\dot y^2].
\]
Writing \(m=\mathbb E_\mu[x]=\mathbb E_\mu[y]\), one also has
\[
\operatorname{Var}_\mu(y)=\operatorname{Cov}_\mu(x,y)=1-m^2,
\qquad
\operatorname{Var}_\mu(x)-\operatorname{Var}_\mu(y)=\mathbb E_\mu[\dot y^2].
\]
The defect vanishes exactly for invariant measures supported on the two equilibria \(E_\pm=(\pm1,\pm1,0)\). Any other compact stationary state assigns positive mass to each of the open regions \(|y|<1\) and \(|y|>1\). Therefore every nonconstant periodic orbit crosses the level set \(|y|=1\) at least twice in each least period.

## Assumptions and scope
The vector field is the parameter-free classical case B from Sprott's 1994 catalogue, not the different thermostatic system later given the same name in other literature. The measure \(\mu\) is assumed to be a Borel probability measure invariant under the Sprott B flow and to have compact support. Compact support ensures that all polynomial observables used below are integrable and that the generator identities can be applied without tail conditions.

The statement is conditional on such a compact invariant measure. It does not assert that every initial condition is bounded, nor does it prove existence or uniqueness of a chaotic invariant measure.

## Proof
Let
\[
F(x,y,z)=(yz,\;x-y,\;1-xy)
\]
be the vector field and let \(L\phi=\nabla\phi\cdot F\) be its generator. Invariance of \(\mu\) gives
\[
\int L\phi\,d\mu=0
\]
for every continuously differentiable observable \(\phi\) on a neighborhood of the compact support.

Take \(\phi(x,y,z)=G(y)\), where \(G\) is continuously differentiable. Then
\[
0=\int G'(y)(x-y)\,d\mu.
\]
On the compact projection of the support to the \(y\)-axis, every continuous test function can be written as a derivative \(G'\). Hence
\[
\mathbb E_\mu[x-y\mid y]=0,
\]
which is the first fiberwise law \(\mathbb E_\mu[x\mid y]=y\).

Likewise, with \(\phi(x,y,z)=H(z)\),
\[
0=\int H'(z)(1-xy)\,d\mu
\]
for all continuously differentiable \(H\), and therefore
\[
\mathbb E_\mu[xy\mid z]=1.
\]
Integrating this identity gives \(\mathbb E_\mu[xy]=1\). Multiplying the first conditional law by \(y\) and integrating gives
\[
\mathbb E_\mu[xy]=\mathbb E_\mu[y^2].
\]
Thus \(\mathbb E_\mu[y^2]=1\).

The mean of \(\dot y=x-y\) vanishes under an invariant measure, so \(\mathbb E_\mu[x]=\mathbb E_\mu[y]=m\). Therefore
\[
\operatorname{Var}_\mu(y)=1-m^2,
\qquad
\operatorname{Cov}_\mu(x,y)=\mathbb E_\mu[xy]-m^2=1-m^2.
\]
Finally,
\[
\mathbb E_\mu[(x-y)^2]
=\mathbb E_\mu[x^2]-2\mathbb E_\mu[xy]+\mathbb E_\mu[y^2]
=\mathbb E_\mu[x^2]-1,
\]
and since \(x-y=\dot y\), this is the activity-defect identity. Subtracting \(\operatorname{Var}_\mu(y)\) from \(\operatorname{Var}_\mu(x)\) yields the displayed variance defect.

If the defect is zero, then \(x-y=0\) on the support of \(\mu\). The support of an invariant measure is flow-invariant. Along any trajectory in that support, \(y\) is therefore constant. Because \(y'=x-y=0\), one has \(x=y\); because \(x'=yz\), any point with \(y\neq0\) must have \(z=0\); and invariance of \(z=0\) then requires \(z'=1-y^2=0\). Points with \(y=0\) lie on the orbit \(x=0\), \(z'=1\), which cannot remain in a compact invariant support. Thus only \(E_+\) and \(E_-\) can occur. Conversely, every probability mixture supported on \(E_+\) and \(E_-\) is invariant and has zero defect.

For the crossing statement, suppose a compact stationary state assigns zero mass to either \(|y|<1\) or \(|y|>1\). Since \(\mathbb E_\mu[y^2]=1\), in either case one must have \(y^2=1\) almost surely. Flow invariance and continuity then force the support to lie on \(E_+\cup E_-\), by the preceding tangency argument. Hence every non-equilibrium-supported stationary state has positive mass on both sides of \(|y|=1\). A nonconstant periodic orbit carries its normalized orbit measure, and continuity around the periodic time circle then forces at least two crossings of \(|y|=1\) per least period.

## Verification
The proof was reconstructed directly from the printed vector field. The two conditional laws were checked from the invariant-measure generator identity with arbitrary one-variable test functions; the global moment and variance identities then follow by exact algebra. The equality case was checked using invariance of the support and tangency of the vector field. No numerical experiment is used as a substitute for an infinite-time argument.

The original 1994 paper was inspected through its full text: its table lists the classical case B and its discussion identifies the associated strange attractor and the two equilibria. A later full-text mathematical study of the Sprott BC family explicitly writes the same Sprott B equations and classifies that work under primary MSC \(34C05\) and \(34C45\). Searches of that full text for invariant-measure, stationary, moment, average, mean-square, and RMS statements found no matching result.

## Relationship to prior work
Sprott introduced the classical case B in 1994 as one of the algebraically simple chaotic flows. Mota and Oliveira later embedded it as the \(\alpha=1\), \(\beta=0\) endpoint of the Sprott BC family and studied equilibria, Hopf bifurcation in the family, dynamics at infinity, and Darboux-type integrability. Those results do not imply the stationary RMS shell, activity defect, or crossing rigidity proved here.

A distinct 2024 paper also uses the name “Sprott B” for the thermostatic system \(\dot x=y\), \(\dot y=-x-yz\), \(\dot z=x^2+y^2-a\). That vector field is not equivalent to the classical case B considered here, so results for it do not cover this finding. Indexed exact-RMS and stationary-shell results for other chaotic flows likewise concern different vector fields and do not imply the present identities.

## Limitations
The result concerns compactly supported invariant probability measures only. It does not control unbounded trajectories or basin geometry, and it does not quantify how often a non-equilibrium trajectory visits the two sides of \(|y|=1\) beyond the positive-mass statement and the periodic-orbit crossing consequence. Literature and database searches cannot establish absolute novelty; obscure or unindexed prior derivations remain a residual risk.

## References
J. C. Sprott, “Some simple chaotic flows,” *Physical Review E* **50** (1994), R647–R650. DOI: 10.1103/PhysRevE.50.R647. Published 1 August 1994.

M. C. Mota and R. D. S. Oliveira, “Dynamic aspects of Sprott BC chaotic system,” *Discrete and Continuous Dynamical Systems - B* **26** (2021), 1653–1673. DOI: 10.3934/dcdsb.2020177.

F. Verhulst and T. Bakri, “The Sprott B system,” *Chaos* **34** (2024), 103116. DOI: 10.1063/5.0212565. This reference is used only to disambiguate a later, different system carrying the same name.
