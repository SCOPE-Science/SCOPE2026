# Three-chord crossing-count tomography of Euclidean triangles

## Finding

Let \(T\) be any nondegenerate Euclidean triangle, with side lengths \(a_1,a_2,a_3\), perimeter \(P\), and \(p_i=a_i/P\). For each of three independent chords, draw its two endpoints independently from normalized arclength on \(\partial T\) and join them. Count only intersections of two segments that occur in the *open interior* of \(T\); a chord lying along a side contributes no such intersection. Write \(C_3\in\{0,1,2,3\}\) for the number of properly intersecting unordered chord pairs, and set

\[
e_2=p_1p_2+p_2p_3+p_3p_1,\qquad e_3=p_1p_2p_3,\qquad q=2e_2^2,
\]
\[
\eta=\frac{20}{9}e_2^3-\frac43e_3^2-4e_2^4.
\]

**Exact moments and inverse theorem.** The first two moments of the crossing count are

\[
\boxed{\mathbb E C_3=3q,\qquad \operatorname{Var}(C_3)=3q(1-q)+6\eta.}
\]

Conversely, these two population moments uniquely determine the *unordered* normalized side-length triple, hence the similarity class of \(T\). Explicitly, from the measured moments recover

\[
q=\frac{\mathbb E C_3}{3},\quad
\eta=\frac{\operatorname{Var}(C_3)-3q(1-q)}6,\quad
e_2=\sqrt{q/2},
\]
\[
\boxed{e_3=\sqrt{\frac34\left(\frac{20}{9}e_2^3-4e_2^4-\eta\right)}.}
\]

The three roots (with multiplicity) of

\[
\boxed{z^3-z^2+e_2z-e_3=0}
\]

are exactly \(p_1,p_2,p_3\). The radicand is strictly positive for every nondegenerate triangle. If \(P\) is also known, the two moments determine the triangle up to congruence.

**Minimality.** For only two chords, the entire crossing-count distribution is Bernoulli with parameter \(q=2e_2^2\), and does not determine triangle shape. For instance, the distinct normalized triples \((4/15,4/15,7/15)\) and \((2/5,2/5,1/5)\) each have \(e_2=8/25\), hence the identical two-chord intersection law \(\operatorname{Bernoulli}(128/625)\), although their side products differ. Thus three is the minimum number of independently sampled chords for which the first two moments of the proper crossing count determine triangle shape.

## Assumptions and scope

The triangle has strictly positive area; equivalently, \(0<p_i<1/2\) and \(p_1+p_2+p_3=1\). Endpoint draws are mutually independent and uniform by **physical boundary arclength**, not by an invariant-line measure, not by choosing edges equally, and not by drawing points uniformly in the triangle's interior. Chords sharing boundary sides can overlap there with positive probability, but boundary coincidences are explicitly excluded from \(C_3\). The result requires exact probability moments; finite data permit estimation, not exact reconstruction.

## Proof

**1. Alternation and the conditional crossing probability.** Orient the triangle boundary and label its edges cyclically \(1,2,3\). Put \(h(c,d)=1\) if chords \(c,d\) cross properly in the triangle's interior, and \(0\) otherwise. A chord with both endpoints on the same edge has \(h(c,d)=0\) for all \(d\). Two chords joining distinct edges cross properly exactly when their four endpoints alternate in cyclic boundary order. This remains true even if endpoints lie on a common edge, provided neither chord is itself contained in a single edge.

Consider a first chord with one endpoint at fractional position \(x\in(0,1)\) on edge \(i\) and the other at fractional position \(y\in(0,1)\) on the next edge \(j\), both measured in cyclic orientation. Write \(k\) for the remaining edge. Let \(g(c)=\mathbb E[h(c,D)\mid c]\), where \(D\) is an independent second chord. Enumerating the three possible different-edge pairs for \(D\) gives

\[
\begin{split}
g_{ij}(x,y)=2\big[&p_ip_j\big((1-x)(1-y)+xy\big)\\
 &+p_ip_k(1-x)+p_jp_k y\big].
\end{split}
\]

The factor of two accounts for the ordering of the two sampled endpoints of \(D\). Endpoints of \(D\) on a common edge cannot contribute to an interior crossing. With \(\alpha=p_ip_j\), \(\beta=p_ip_k\), and \(\gamma=p_jp_k\), the centered expression is

\[
g_{ij}(x,y)-e_2
=4\alpha(x-1/2)(y-1/2)-2\beta(x-1/2)+2\gamma(y-1/2).
\]

Because \(x,y\) are independent uniform variables on \((0,1)\), their centered variances are \(1/12\) and all the mixed terms vanish. Consequently,

\[
\mathbb E[g_{ij}(x,y)]=e_2,
\qquad
\operatorname{Var}(g_{ij}(x,y))=
\frac{\alpha^2}{9}+\frac{\beta^2+\gamma^2}{3}.
\]

**2. Global first and second conditional moments.** The first chord uses a specified unordered pair of distinct edges \(i,j\) with probability \(2p_ip_j\). It lies along one edge otherwise, when \(g=0\). Therefore

\[
\mathbb E[g]=\sum_{i<j}2p_ip_j e_2=2e_2^2=q.
\]

For the second moment, multiply the conditional second-moment expression by \(2p_ip_j\) and sum over the three edge pairs. To make the simplification explicit, write \(r_1=p_1p_2\), \(r_2=p_2p_3\), \(r_3=p_3p_1\). Their elementary symmetric functions are \(\sum r_i=e_2\), \(\sum_{i<j}r_ir_j=e_3\), and \(r_1r_2r_3=e_3^2\). Hence

\[
\begin{split}
\mathbb E[g^2]
&=2e_2^3+\frac29\sum r_i^3
   +\frac23\sum_i r_i\!\sum_{j\ne i}r_j^2\\
&=\frac{20}{9}e_2^3-\frac43e_3^2.
\end{split}
\]

Thus \(\operatorname{Var}(g)=\mathbb E[g^2]-q^2=\eta\). This variance is strictly positive: a first chord lies along one edge with positive probability and has \(g=0\), whereas a first chord joining different edges has strictly positive \(g\).

**3. Three-chord crossing count.** For three independent chords \(D_1,D_2,D_3\), put \(I_{ij}=h(D_i,D_j)\) and \(C_3=I_{12}+I_{13}+I_{23}\). Every indicator has mean \(q\) and variance \(q(1-q)\). Any two distinct indicators share exactly one sampled chord, and conditional on it their other chords are independent. The law of total covariance gives

\[
\operatorname{Cov}(I_{12},I_{13})=
\mathbb E[g(D_1)^2]-q^2=\eta.
\]

The same value applies to the other two covariances. Summing three variances and six ordered covariance contributions proves the two displayed moment identities.

**4. Reconstruction and optimality.** Since \(e_2>0\) and \(e_3>0\), the explicit inverse chooses the positive square root, so both elementary symmetric polynomials are uniquely recovered from the two moments. The monic cubic has exactly the three normalized side lengths as its multiset of roots by Viète's formulas; no other unordered triple is possible. For two chords there is only one indicator, hence only the scalar \(q\). Both explicit triples in the finding satisfy the strict triangle inequalities; they have the same \(e_2\) but distinct \(e_3\), proving failure of two-chord identifiability and the sharp minimality assertion.

## Verification

The standalone file `verify_chord_tomography.py` implements the model using a cyclic endpoint-order crossing criterion; it explicitly excludes chords whose endpoints share an edge. It independently integrates the conditional crossing probability and its square with tensor-product three-point Gauss quadrature, which is exact for the relevant bivariate polynomials up to floating-point roundoff. Exact rational checks cover five side-ratio triples, including the two-chord ambiguity pair; the inverse elementary symmetric quantities are reconstructed. Independent Monte Carlo checks of the complete three-chord crossing-count mean and variance use \(360000\) independent three-chord trials over three valid triangle shapes. The analytic derivation, not the simulations, establishes the theorem for all nondegenerate triangles. The reproducibility script uses the Python standard library only.

## Relationship to prior work

Acan's 2015 treatment of uniformly random chord diagrams studies pairings of distinct points on a circle and their intersection graphs. Bortolotto and Ramos (2025) analyze crossing probabilities for arbitrary atomless endpoint measures on a *circle*. Those models do not have positive-probability same-edge boundary chords and do not imply the shape-dependent mean, covariance, or inverse theorem here. Gates (1982) treats moments of intersections of random chords to a circle under an invariant-line chord measure; that model also differs, and only its abstract was available for inspection. The relevant overlap is the general use of crossing counts and their joint moments, not the particular triangular arclength sampling and minimal three-chord tomography statement.

## Limitations

The result determines **similarity**, not scale; congruence needs the additional perimeter. It presumes independent endpoint-pair sampling, proper interior crossings, and exact population moments. It gives no finite-sample confidence bounds or noise-stability rates. The literature comparison does not constitute a definitive historical priority determination; an unindexed theorem for polygonal endpoint measures could subsume the identity. In particular, the full text of Gates's 1982 circle-chord article could not be obtained during this comparison.

## References

- H. Acan, *On a uniformly random chord diagram and its intersection graph*, arXiv:1501.01489v1, 7 January 2015, especially Sections 1–2. https://arxiv.org/abs/1501.01489
- C. Bortolotto and J. P. G. Ramos, *On extremal problems associated with random chords on a circle*, Mathematika (2025), DOI:10.1112/mtk.70024, especially Theorem 1.2 and Section 2. https://doi.org/10.1112/mtk.70024
- J. Gates, *The number of intersections of random chords to a circle—third and fourth moments*, Journal of Applied Probability **19** (1982), 355–372, DOI:10.2307/3213487 (abstract inspected; full text not obtained). https://doi.org/10.2307/3213487
- W. Hoeffding, *A Class of Statistics with Asymptotically Normal Distribution*, Annals of Mathematical Statistics **19** (1948), 293–325, DOI:10.1214/aoms/1177730196 (general background on U-statistics; not needed for the finite three-chord proof).
