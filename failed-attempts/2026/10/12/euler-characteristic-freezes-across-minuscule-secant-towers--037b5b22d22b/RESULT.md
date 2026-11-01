# Euler characteristic freezes across minuscule secant towers
## Finding
Let \(G\) be a connected complex semisimple algebraic group, let \(V_\lambda\) be a nontrivial irreducible minuscule representation with highest weight \(\lambda\), and let
\[
X=G\cdot[v_\lambda]\subset\mathbb P(V_\lambda)
\]
be its closed homogeneous orbit in the minuscule embedding.

For every
\[
r\ge1,
\]
let
\[
\sigma_r(X)
\]
denote the projective secant variety obtained as the Zariski closure of the union of linear spans of at most \(r\) points of \(X\).

Then
\[
\boxed{
\chi_{\mathrm{top}}(\sigma_r(X))
=
\dim V_\lambda
=
\chi_{\mathrm{top}}(X)
}
\]
for every \(r\).

In particular, ordinary Euler characteristic is constant along the entire secant tower, even after the tower stabilizes at the ambient projective space.

Set
\[
\sigma_0(X)=\varnothing
\]
and define the exact secant-rank layer
\[
B_r=\sigma_r(X)\setminus\sigma_{r-1}(X).
\]
Then
\[
\boxed{
\chi_c(B_1)=\dim V_\lambda
}
\]
and
\[
\boxed{
\chi_c(B_r)=0
\qquad(r\ge2).
}
\]

Thus every higher exact secant-rank layer is invisible to compactly supported Euler characteristic.

## Assumptions and scope
The base field is \(\mathbb C\).

The representation \(V_\lambda\) is irreducible and minuscule: its weights form a single Weyl-group orbit and every weight space is one-dimensional.

The embedding is the projectivization of this minuscule representation. The statement therefore applies to standard minuscule homogeneous families such as ordinary Grassmannians and spinor varieties, as well as the exceptional minuscule examples.

No nondefectivity, smoothness of the secant variety, or expected-dimension hypothesis is required.

The cumulative secant varieties are projective, so ordinary and compactly supported Euler characteristic agree on them. The locally closed layers \(B_r\) use compactly supported Euler characteristic.

## Proof
Fix a maximal torus
\[
T\subset G.
\]
Because \(V_\lambda\) is minuscule, its weight decomposition is
\[
V_\lambda
=
\bigoplus_{\mu\in W\lambda}V_\mu,
\qquad
\dim V_\mu=1.
\]

Choose a cocharacter
\[
\eta:\mathbb C^*\longrightarrow T
\]
such that the integers
\[
\langle\mu,\eta\rangle
\]
are pairwise distinct as \(\mu\) ranges over the finite set \(W\lambda\). Such a cocharacter exists because one need only avoid finitely many proper rational hyperplanes in the cocharacter space.

The fixed locus of this one-parameter subgroup on the ambient projective space is therefore exactly the collection of weight lines:
\[
\mathbb P(V_\lambda)^\eta
=
\left\{
\mathbb P(V_\mu):\mu\in W\lambda
\right\}.
\]

Every one of these weight lines lies on \(X\). Indeed, if
\[
\mu=w\lambda,
\]
choose a representative \(\dot w\in N_G(T)\). Then
\[
\dot w\,v_\lambda
\]
is a nonzero vector in the one-dimensional weight space \(V_\mu\), so
\[
\mathbb P(V_\mu)
=
\dot w\,[v_\lambda]
\in X.
\]

Hence
\[
\mathbb P(V_\lambda)^\eta
\subset X.
\]
Since \(X\subset\sigma_r(X)\subset\mathbb P(V_\lambda)\) and every \(\sigma_r(X)\) is \(T\)-stable, it follows that
\[
\sigma_r(X)^\eta
=
\mathbb P(V_\lambda)^\eta
\]
for every \(r\).

The fixed set therefore has
\[
|W\lambda|
=
\dim V_\lambda
\]
points.

For any complex algebraic variety \(Y\) equipped with an algebraic \(\mathbb C^*\)-action,
\[
\chi_c(Y)=\chi_c(Y^{\mathbb C^*}).
\]
A proof valid for singular varieties is obtained by deleting the fixed locus and applying Rosenlicht stratification to the complement. After refining by stabilizer type, every nonfixed stratum is a Zariski-locally-trivial bundle whose fiber is a finite quotient of \(\mathbb C^*\), hence isomorphic to \(\mathbb C^*\). Since
\[
\chi_c(\mathbb C^*)=0,
\]
all nonfixed strata contribute zero.

Apply this to the projective variety
\[
Y=\sigma_r(X).
\]
Projectivity gives
\[
\chi_{\mathrm{top}}(Y)=\chi_c(Y),
\]
and therefore
\[
\chi_{\mathrm{top}}(\sigma_r(X))
=
\chi_c(\sigma_r(X)^\eta)
=
|W\lambda|
=
\dim V_\lambda.
\]

Taking \(r=1\) gives
\[
\chi_{\mathrm{top}}(X)=\dim V_\lambda.
\]

Finally, additivity for
\[
\sigma_r(X)
=
\sigma_{r-1}(X)\sqcup B_r
\]
gives, for every \(r\ge2\),
\[
\chi_c(B_r)
=
\chi_{\mathrm{top}}(\sigma_r(X))
-
\chi_{\mathrm{top}}(\sigma_{r-1}(X))
=
0.
\]

## Verification
The bundled checker tests the weight-separation mechanism in principal classical minuscule models.

For type \(A\) Grassmannians, it enumerates the \(k\)-subset weights of
\[
\bigwedge^k\mathbb C^n
\]
and verifies pairwise separation by a power-of-two cocharacter.

For half-spin representations, it enumerates the parity-constrained sign weights and verifies separation by a balanced base-\(3\) cocharacter.

For the even-quadric vector representation, it checks the \(\pm e_i\) weights directly.

The checker verifies the expected weight counts
\[
\binom nk,
\qquad
2^{n-1},
\qquad
2n
\]
over a finite parameter range.

These computations are regression evidence only. The theorem for every minuscule representation follows from the abstract Weyl-orbit and multiplicity-one properties.

## Relationship to prior work
Manivel and Michałek study secant and tangential varieties of minimal orbits in minuscule and cominuscule representations. Their setup records the decisive representation-theoretic input used here: for a minuscule highest weight, all weights lie in a single Weyl-group orbit and every weight space is one-dimensional.

Their work focuses on local parametrizations, generalized determinants, equations, and singular geometry of secant and tangential varieties. Targeted full-text searches found no Euler-characteristic, fixed-point, or torus-localization statement.

The present result extracts a global topological consequence of the minuscule weight structure: every cumulative secant variety has exactly the same Euler characteristic as the original homogeneous variety, and all higher exact secant-rank layers have vanishing compactly supported Euler characteristic.

A previously known Segre-secant constancy statement is a special product-type instance of this theorem. The minuscule result is strictly broader: it applies uniformly to Grassmannian, spinor, even-quadric, and exceptional minuscule secant towers through the same representation-theoretic mechanism.

## Limitations
The minuscule hypothesis is essential to this proof. If weight multiplicities exceed one, or if ambient weight lines are not all contained in the closed orbit, the ambient fixed locus can be larger than the fixed locus of \(X\), and the argument no longer forces secant-wise constancy.

The theorem concerns Euler characteristic only. It does not imply that higher secant varieties or exact secant-rank layers have trivial homology, simple singularities, or stable Hodge structure.

Because the proof is short once minuscule weight theory is combined with Euler localization, an unindexed or folklore observation in transformation-group or secant-variety literature remains a residual novelty risk.

## References
Laurent Manivel and Mateusz Michałek, *Secants of minuscule and cominuscule minimal orbits*, arXiv:1401.1956, first submitted 9 January 2014; *Linear Algebra and its Applications* 481 (2015), 288--312, DOI 10.1016/j.laa.2015.04.027.

Anders Skovsted Buch and Matthew J. Samuel, *K-theory of minuscule varieties*, arXiv:1306.5419, first submitted 23 June 2013; *Journal für die reine und angewandte Mathematik* 2016(719), 133--171.
