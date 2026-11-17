# Global greedy independent-set selection and exact extinction rates in hierarchical May–Leonard chains

## Finding
Let \(n\ge1\), \(r>d>0\), and let \(p_1,\ldots,p_{n-1}>0\). For every nonzero initial state \(x(0)\) in the population simplex \(\{x_i\ge0:\sum_i x_i\le1\}\), the vacancy-limited directed hierarchical chain
\[
\dot x_1=x_1(r(1-S)-d),\qquad
\dot x_i=x_i\big(r(1-S)-d-p_{i-1}x_{i-1}\big)\quad(2\le i\le n),\qquad S=\sum_{j=1}^n x_j
\]
converges exponentially to **one specific equilibrium**, selected solely by which coordinates were initially positive. Set \(\sigma_0=0\) and recursively
\[
\sigma_i=\mathbf 1_{\{x_i(0)>0\}}(1-\sigma_{i-1}),\qquad I=\{i:\sigma_i=1\}.
\]
Exactly the indices in \(I\) have strictly positive limiting densities. The selected set is a maximum-cardinality independent set of the path graph **induced by initially positive indices**: within every uninterrupted run of initially positive species, the first, third, fifth, and so on are selected. For fully positive initial data, the survivors are exactly species \(1,3,5,\ldots\), numbering \(\lceil n/2\rceil\).

Write \(K=1-d/r\), let \(m\) be the smallest initially positive index, and define \(R_m=1\). For \(i>m\) in \(I\), define the positive, convergent integral weight
\[
R_i=\frac{x_i(0)}{x_m(0)}\exp\!\left(-p_{i-1}\int_0^\infty x_{i-1}(t)\,dt\right).
\]
Then the unique selected equilibrium has
\[
X_i=\begin{cases}K R_i/\sum_{j\in I}R_j,&i\in I,\\0,&i\notin I.\end{cases}
\]
For every initially positive but unselected \(i\), its exact logarithmic extinction exponent is
\[
\lim_{t\to\infty}\frac{\log x_i(t)}t=-p_{i-1}X_{i-1}<0.
\]
There is in addition a finite strictly positive asymptotic extinction prefactor, described in the proof. All convergence is exponential for each fixed admissible instance and initial state; no parameter-uniform rate is asserted.

## Assumptions and scope
All species have the same reproduction coefficient \(r\) and mortality coefficient \(d\); consecutive competitive interactions have arbitrary strictly positive strengths \(p_i\). The state dimension is any finite \(n\ge1\). The model is deterministic and spatially homogeneous. Exactly zero initial coordinates are permanent absences. The all-zero state is excluded from the theorem because it stays extinct. All claims are forward-time statements on the closed invariant simplex, including boundary faces.

An independent set of the initially occupied path has no two consecutive occupied vertices. 'Maximum-cardinality' refers to cardinality within this induced path, not to stability against reintroduction of initially absent species.

## Proof
**Invariance and the uniform root bound.** The coordinate hyperplanes are invariant. On \(S=1\) one has \(\dot S=-d-\sum_{i=2}^n p_{i-1}x_{i-1}x_i<0\), so the simplex is forward invariant. Put \(a=r-d>0\) and let \(m\) be the first initially positive index. Since every coordinate before \(m\) remains zero, \(\dot x_m=x_m(a-rS)\). For \(i>m\) with \(x_i(0)>0\), the exact quotient identity is
\[
\frac{d}{dt}\log\frac{x_i(t)}{x_m(t)}=-p_{i-1}x_{i-1}(t).
\tag{1}
\]
The ratios are nonincreasing (and identically zero if initially zero). Thus \(S(t)\le Cx_m(t)\) where \(C=S(0)/x_m(0)\ge1\), and
\[
\dot x_m\ge ax_m-rCx_m^2.
\]
Scalar logistic comparison shows
\[
x_m(t)\ge q:=\min\{x_m(0),K/C\}>0 \qquad(t\ge0).
\tag{2}
\]
All coordinates remain at most one.

**Induction and exact survivor selection.** Begin at \(i=m\), which is persistent by (2). Induct from left to right. If \(x_i(0)=0\), then \(x_i(t)=0\) and \(i\) is not selected. If \(x_i(0)>0\) and its predecessor is persistent, then the exact ratio (1), with \(x_{i-1}(t)\) bounded uniformly below by a positive constant, shows \(x_i(t)\le C_i e^{-\beta_i t}\) for positive constants; this species becomes extinct exponentially. If its predecessor is absent or exponentially extinct, then \(\int_0^\infty x_{i-1}(t)\,dt<\infty\), and (1) yields a positive limiting quotient \(x_i(t)/x_m(t)\to R_i>0\). Bound (2) therefore makes species \(i\) persistent. These exhaustive cases establish precisely the binary recursion in the finding and the exponential extinction of every unselected, initially occupied species. Every selected species has a positive lower bound. Within a maximal consecutive block of initially occupied indices of length \(\ell\), the recursion takes its first, third, and later odd positions, selecting \(\lceil\ell/2\rceil\), the maximum possible independent-set cardinality. Different blocks are separated by absent vertices; their independent-set counts add.

**Exponential convergence to one equilibrium.** Summing the equations gives the exact scalar identity
\[
\dot S=aS-rS^2-P(t),\qquad P(t)=\sum_{i=2}^n p_{i-1}x_{i-1}(t)x_i(t)\ge0.
\tag{3}
\]
No two adjacent species are selected, so at least one member of every product in \(P\) is identically absent or exponentially extinct. Hence \(P(t)=O(e^{-\beta t})\) for some \(\beta>0\), with \(P\equiv0\) allowed. Writing \(h(t)=S(t)-K\), identity (3) becomes
\[
\dot h=-rS(t)h-P(t).
\tag{4}
\]
Since \(S(t)\ge x_m(t)\ge q\), variation of constants gives \(h(t)=O(e^{-\gamma t})\) for any fixed \(0<\gamma<\min(rq,\beta)\). If \(P\equiv0\), any \(0<\gamma<rq\) works. For each persistent species the ratio in (1) approaches its positive \(R_i\) exponentially because the predecessor is absent or exponentially extinct; unselected quotients approach zero exponentially. The identity \(S=x_m\big(1+\sum_{i>m}x_i/x_m\big)\) now yields \(x_m\to K/\sum_{j\in I}R_j\) exponentially, and gives the stated exponential convergence of each coordinate to \(X_i\). Thus this fixed point is the actual omega limit, rather than merely one feasible stationary configuration.

**Exact extinction clock.** If \(x_i(0)>0\) but \(i\notin I\), then necessarily \(i-1\in I\). Integrating (1), and using \(x_m(t)\to X_m>0\), gives
\[
\log x_i(t)=\log x_m(t)+\log\frac{x_i(0)}{x_m(0)}-p_{i-1}\int_0^t x_{i-1}(s)\,ds.
\]
The exponential convergence \(x_{i-1}(t)\to X_{i-1}>0\) implies the asserted logarithmic exponent. Indeed, the stronger prefactor is
\[
\lim_{t\to\infty}e^{p_{i-1}X_{i-1}t}x_i(t)
=X_m\frac{x_i(0)}{x_m(0)}
\exp\!\left(-p_{i-1}\int_0^\infty\big[x_{i-1}(s)-X_{i-1}\big]ds\right)\in(0,\infty).
\]
This also identifies the exact exponential rate independently of any linearization at an equilibrium. \(\square\)

## Verification
The companion `check_selection.py` uses SymPy to verify the exact total-mass identity (3) and five quotient identities (1) for a six-species instance. It also solves nine representative eight-species systems with positive and absent coordinates, tests the greedy support, checks the total limiting mass against \(K\), and compares finite-time logarithmic exponents against their theoretical values. Its executed output was:

`VERIFY_OK exact_ratio_identities=5 exact_total_identity=1 finite_support_patterns=9 maximal_independent_selection=1`

The rigorous proof above, not finite numerical integration, establishes all-dimensional and infinite-time claims. The checker needs Python 3, NumPy, SciPy and SymPy.

## Relationship to prior work
Samanta, Dawn, Jahiruddin, Bhattacharyya, Hens, and Nag Chowdhury (2026, arXiv:2609.09027) introduced and analyzed this hierarchical May–Leonard directed-predation family, including equilibrium feasibility and independent-set restrictions, with stochastic simulation. The present statement takes that family as given; the independent-set **admissibility condition itself is not new**. Its additional contribution is an explicit **global selection rule from every nonzero simplex initial state**, including boundary faces, uniqueness of the selected asymptotic equilibrium, exponentially quantified disappearance, and exact limiting density ratios. Merely knowing which supports are allowable at equilibrium does not imply which allowable support any given orbit chooses, or that the orbit converges.

Cheon's 2003 ecological hierarchy model (arXiv:cond-mat/0301619) instead models a trophic predator benefiting from prey consumption and evolutionary adjustment of aggression coefficients. Its equilibrium stability mechanisms and equations differ from the common-vacancy, one-sided predation-loss chain here. Classical cyclic May–Leonard models also differ from an acyclic directed chain. The algebraic quotient and global comparison proof supplies the stated stronger claim, but comprehensive historical priority remains provisional.

## Limitations
Assumptions of identical intrinsic reproduction and mortality are essential to the cancellation in (1). The assertion does not cover heterogeneous intrinsic coefficients, feedback or cyclic predation, finite-population stochastic extinction, diffusion, or the persistence of species introduced later from exactly zero density. Exponential constants can become extremely small when selected populations are initially rare; no uniform transient cutoff is claimed. The exact equilibrium weights depend on trajectory integrals and are not generally closed-form functions of the initial state. Independent mathematical review has not been performed.

## References
1. R. Samanta, S. Dawn, S. Jahiruddin, S. Bhattacharyya, C. Hens, and S. Nag Chowdhury, *Selection Rules for Species Coexistence in a Hierarchical May–Leonard Model* (public September 8, 2026), arXiv:2609.09027, https://arxiv.org/abs/2609.09027.
2. T. Cheon, *Evolutionary Stability of Ecological Hierarchy* (2003), arXiv:cond-mat/0301619, https://arxiv.org/abs/cond-mat/0301619.
