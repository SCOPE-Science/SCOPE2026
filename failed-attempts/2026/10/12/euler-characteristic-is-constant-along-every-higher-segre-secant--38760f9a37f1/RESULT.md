# Euler characteristic is constant along every higher Segre secant tower
## Finding
Let
\[
t\ge3,
\]
let \(A_i\) be complex vector spaces of dimensions
\[
a_i\ge2,
\]
and let
\[
X=
\operatorname{Seg}
\left(
\mathbb P A_1\times\cdots\times\mathbb P A_t
\right)
\subset
\mathbb P
\left(
A_1\otimes\cdots\otimes A_t
\right)
\]
be the Segre variety of decomposable tensors.

For every
\[
r\ge1,
\]
let
\[
\sigma_r(X)
\]
be the projective secant variety, equivalently the locus of tensors of border rank at most \(r\).

Then
\[
\boxed{
\chi_{\mathrm{top}}\!\left(\sigma_r(X)\right)
=
\prod_{i=1}^{t}a_i
}
\]
for every \(r\).

In particular, the Euler characteristic does not change anywhere along the higher secant tower, even when the tower eventually stabilizes at the ambient projective space.

Set
\[
\sigma_0(X)=\varnothing
\]
and define the exact border-rank stratum
\[
B_r=
\sigma_r(X)\setminus\sigma_{r-1}(X).
\]
Then compactly supported Euler characteristic satisfies
\[
\boxed{
\chi_c(B_1)=\prod_{i=1}^{t}a_i
}
\]
and
\[
\boxed{
\chi_c(B_r)=0
\qquad(r\ge2).
}
\]

Thus every nontrivial higher border-rank layer is Euler-invisible.

## Assumptions and scope
The base field is \(\mathbb C\). The statement concerns ordinary projective secant varieties, hence border rank rather than tensor rank.

The restriction
\[
t\ge3
\]
isolates the genuine higher-tensor case. For two factors, the secant varieties are ordinary determinantal rank loci and the same fixed-point mechanism specializes to the matrix case.

No nondefectivity assumption is required. The result holds whether a secant variety has the expected dimension, is defective, or already equals the ambient projective space.

For the quasi-projective exact border-rank strata, the invariant used is compactly supported Euler characteristic.

## Proof
Choose a basis
\[
e_{i,0},\ldots,e_{i,a_i-1}
\]
of each \(A_i\). Choose an integer
\[
B>\max_i a_i.
\]
Define a one-parameter subgroup
\[
\lambda:\mathbb C^*\longrightarrow
\prod_{i=1}^{t}\operatorname{GL}(A_i)
\]
by
\[
\lambda(z)e_{i,j}
=
z^{\,jB^{i-1}}e_{i,j}.
\]

A tensor-coordinate basis vector
\[
e_{1,j_1}\otimes\cdots\otimes e_{t,j_t}
\]
has \(\lambda\)-weight
\[
w(j_1,\ldots,j_t)
=
\sum_{i=1}^{t}j_iB^{i-1}.
\]
Because
\[
0\le j_i<B,
\]
uniqueness of base-\(B\) expansion shows that all these weights are distinct.

Therefore the fixed locus of \(\lambda\) on the ambient projective space consists exactly of the coordinate tensor lines
\[
\left[
e_{1,j_1}\otimes\cdots\otimes e_{t,j_t}
\right].
\]
There are
\[
N=\prod_{i=1}^{t}a_i
\]
such points.

Every coordinate tensor is decomposable, so every one of these fixed points already belongs to \(X=\sigma_1(X)\). The Segre variety is preserved by the product linear group, hence each secant variety \(\sigma_r(X)\) is preserved by \(\lambda\). Since a fixed point of the restricted action must be a fixed point of the ambient action,
\[
\sigma_r(X)^\lambda
=
X^\lambda
\]
as sets, and this common fixed locus consists of exactly \(N\) reduced points.

It remains to justify Euler localization without assuming smoothness.

For any complex algebraic variety \(Y\) with an algebraic \(\mathbb C^*\)-action,
\[
\chi_c(Y)=\chi_c(Y^{\mathbb C^*}).
\]
Indeed, remove the fixed locus. By Rosenlicht's theorem and Noetherian induction, the remainder admits a finite constructible stratification on which geometric quotients by \(\mathbb C^*\) exist and the stabilizer type is constant. Every nonfixed stabilizer is finite, so each orbit is isomorphic to
\[
\mathbb C^*/\mu_m\cong\mathbb C^*.
\]
After refining the quotient stratification, each piece is a Zariski-locally-trivial \(\mathbb C^*\)-bundle. Since
\[
\chi_c(\mathbb C^*)=0,
\]
every nonfixed stratum has compactly supported Euler characteristic zero. Additivity proves the localization identity.

Apply this to the projective variety
\[
Y=\sigma_r(X).
\]
Projectivity gives
\[
\chi_c(Y)=\chi_{\mathrm{top}}(Y),
\]
hence
\[
\chi_{\mathrm{top}}\!\left(\sigma_r(X)\right)
=
\chi_{\mathrm{top}}\!\left(\sigma_r(X)^\lambda\right)
=
N
=
\prod_{i=1}^{t}a_i.
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
\chi_{\mathrm{top}}\!\left(\sigma_r(X)\right)
-
\chi_{\mathrm{top}}\!\left(\sigma_{r-1}(X)\right)
=
N-N
=
0.
\]
The \(r=1\) statement is the Euler characteristic of the Segre product itself.

## Verification
The bundled checker verifies the weight-separation construction for every tensor format with
\[
3\le t\le6,
\qquad
2\le a_i\le5.
\]
For each format it constructs the base-\(B\) one-parameter subgroup, enumerates every tensor coordinate, verifies that all weights are distinct, and confirms that the number of ambient fixed points is
\[
\prod_i a_i.
\]

It also checks representative formats in which known secant varieties fill the ambient space; the predicted value agrees with
\[
\chi_{\mathrm{top}}\!\left(\mathbb P^{N-1}\right)=N.
\]

These finite checks only test the combinatorial weight construction. The all-format theorem is proved symbolically by base-\(B\) uniqueness and Euler localization.

## Relationship to prior work
Classical work on secant varieties of Segre varieties studies their dimensions, equations, singularities, and tensor-rank interpretation. In particular, archival sources define the higher secant tower for products with at least three projective factors and emphasize its role in tensor complexity and algebraic statistics.

The two-factor specialization is determinantal and its rank loci are classically well understood. The present statement excludes that case and concerns genuine higher-order tensors.

The new point is topological uniformity across every higher Segre secant tower: all cumulative border-rank loci have the same Euler characteristic, and every exact border-rank layer above rank one has compactly supported Euler characteristic zero.

Targeted searches using Segre secants, tensor border rank, Euler characteristic, fixed points, exact rank strata, and constant secant towers did not locate this statement. Full-text inspection of highly relevant archival papers on Segre secant ideals and tensor border rank found no Euler-characteristic or fixed-point formulation.

## Limitations
Euler characteristic is very coarse. Vanishing of
\[
\chi_c(B_r)
\]
does not imply that the exact border-rank stratum is empty, contractible, or topologically simple.

The theorem is specific to the ordinary Segre embedding. In a Segre--Veronese embedding, ambient coordinate fixed points need not all lie on the embedded variety, so the same proof does not automatically apply.

The proof uses a standard localization property of Euler characteristic together with an elementary separating one-parameter subgroup. Because the argument is short once these ingredients are juxtaposed, an unindexed observation in tensor or transformation-group literature remains a residual novelty risk.

## References
J. M. Landsberg and Laurent Manivel, *On the ideals of secant varieties of Segre varieties*, arXiv:math/0311388, first submitted 21 November 2003; *Foundations of Computational Mathematics* 4 (2004), 397--422.

J. M. Landsberg and Jerzy Weyman, *On the ideals and singularities of secant varieties of Segre varieties*, arXiv:math/0601452, first submitted 18 January 2006; *Bulletin of the London Mathematical Society* 39 (2007), 685--697.

M. V. Catalisano, A. V. Geramita, and A. Gimigliano, *On the ideals of Secant Varieties to certain rational varieties*, arXiv:math/0609054, first submitted 2 September 2006; *Journal of Algebra* 319 (2008), 1913--1931.

Jarosław Buczyński and J. M. Landsberg, *Ranks of tensors and a generalization of secant varieties*, arXiv:0909.4262, first submitted 23 September 2009; *Linear Algebra and its Applications* 438 (2013), 668--689.
