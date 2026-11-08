# The seven-ray gap for tensor-generating canonical bundles on smooth toric surfaces

## Finding
Let \(X\) range over smooth complete complex toric surfaces, and write \(r=|\Sigma_X(1)|\) for the number of rays in its complete fan. Then the canonical line bundle \(\omega_X\) is \(\otimes\)-generating, meaning that its integral tensor powers generate \(\operatorname{Perf}(X)\), for some such surface with \(r\) rays **if and only if**
\[
 r\in\{3,4,5,6\}\cup\{8,9,10,\ldots\}.
\]
Equivalently, the possible Picard numbers are precisely \(\rho(X)\in\{1,2,3,4\}\cup\{6,7,8,\ldots\}\). In particular, Picard number \(5\) is the unique missing positive rank. There exist such surfaces with arbitrarily negative canonical self-intersection \(K_X^2=12-r\).

More intrinsically, for every smooth complete toric surface \(X\), the bundle \(\omega_X\) is \(\otimes\)-generating **if and only if** none of its torus-invariant irreducible curves has self-intersection \(-2\). The ray spectrum above is the additional classification of when this simple condition can occur.

## Assumptions and scope
All varieties are split complex toric varieties. The fan \(\Sigma_X\subset\mathbb R^2\) is complete and smooth, with primitive rays \(v_0,\ldots,v_{r-1}\) in cyclic order and \(\det(v_i,v_{i+1})=1\). The corresponding invariant irreducible curves are \(D_i\); subscripts are taken modulo \(r\). The word \(\otimes\)-generating refers to all positive and negative integral tensor powers as generators of the derived category of perfect complexes, not to ordinary global generation of \(\omega_X\).

## Proof
**Categorical-to-numerical reduction.** Ito, Zeng and Zeng prove that on a proper toric variety an invertible sheaf is \(\otimes\)-generating precisely when its restriction to every invariant orbit closure is big or anti-big (their Theorem 1.1). On a complete toric surface, \(-K_X=\sum_iD_i\) is big: its toric polytope \(\{m:\langle m,v_i\rangle\ge-1\ \forall i\}\) is bounded by completeness and contains a neighborhood of the origin. The only remaining positive-dimensional orbit closures are the invariant curves \(D_i\simeq\mathbb P^1\). On such a curve, bigness or anti-bigness of a line bundle means nonzero degree. Adjunction gives \((-K_X)\cdot D_i=2+D_i^2\). Therefore \(\omega_X\) (equivalently \(\omega_X^{-1}\)) is \(\otimes\)-generating exactly when \(D_i^2\ne-2\) for all \(i\).

**Self-intersection calculus.** For every smooth complete fan, \(v_{i-1}+v_{i+1}=-D_i^2v_i\). Blowing up the torus fixed point corresponding to the cone between consecutive rays replaces the cyclic self-intersection string
\[
 (\ldots,a,b,\ldots)\quad\text{by}\quad(\ldots,a-1,-1,b-1,\ldots).
\]
Every smooth complete toric surface is obtained from \(\mathbb P^2\) or a Hirzebruch surface \(\mathbb F_n\), \(n\ge0\), by torus-fixed-point blow-ups (standard toric surface classification; \(\mathbb F_1\) can harmlessly be included as a redundant starting model). Their starting cyclic self-intersection strings are respectively \((1,1,1)\) and \((0,-n,0,n)\).

**No seven-ray example.** A seven-ray smooth complete fan would be obtained from \(\mathbb P^2\) by four such blow-ups or from \(\mathbb F_n\) by three. Exhaustive **symbolic** application of the local rule, reducing strings only by cyclic rotation and reversal, produces \(13\) classes from the first initial string after four operations and \(21\) formal classes from \((0,-n,0,n)\) after three. All \(13\) classes contain an entry \(-2\). For \(n=0,1,2,3,4\), every one of the \(21\) formal classes evaluates to a string containing \(-2\); for every \(n\ge5\), each formal class already has a *constant* entry \(-2\), independent of \(n\). Consequently no seven-ray fan avoids a \((-2)\)-curve. This is a finite exhaustive classification of all relevant blow-up histories, not a sample over bounded \(n\). The included `verify.py` implements exactly this recurrence using affine-in-\(n\) integer pairs, without floating point arithmetic, and independently constructs the fans below.

**The small ray counts.** The fans of \(\mathbb P^2\), \(\mathbb F_0\), and the toric blow-ups of \(\mathbb P^2\) at two and three distinct torus-fixed points have \(r=3,4,5,6\) respectively, and none has an invariant \((-2)\)-curve. Thus each small listed value occurs. (For \(r=5\), blowing up any two different original two-dimensional cones suffices.)

**Eight and nine rays.** The following cyclic primitive vectors specify a smooth complete eight-ray fan:
\[
 (1,0),(3,1),(2,1),(3,2),(1,1),(0,1),(-1,3),(0,-1).
\]
It is obtained from the standard \(\mathbb F_3\) fan with cyclic rays \((1,0),(0,1),(-1,3),(0,-1)\) by subdivisions at zero-based cone indices \(0,0,0,2\) in that order; hence it is complete. Its adjacent determinants are all \(1\), and its cyclic invariant-curve self-intersections are
\[
 (-3,-1,-3,-1,-3,-4,0,3).
\]
Inserting the sum of the fifth and sixth vectors gives a nine-ray fan, with no self-intersection \(-2\). Both have a consecutive triple of self-intersections \((A,-1,B)\) with \(A,B\le-3\).

**Indefinite growth.** Given such a triple, blow up the cone between the \(A\)-curve and the \((-1)\)-curve, then blow up the cone between the resulting \((-2)\)-curve and the original \(B\)-curve. On these curves, the two blow-ups implement
\[
 (A,-1,B)\longmapsto(A-1,-1,-3,-1,B-1).
\]
The resulting fan is again smooth and complete, has two more rays, contains no \((-2)\)-curve, and retains such a triple. Iterating from the eight- and nine-ray fans realizes every ray count \(r\ge8\). Finally, for any smooth complete toric surface, \(K_X^2=12-r\) by Noether's formula and the toric Euler characteristic \(c_2(X)=r\), proving the unboundedly negative self-intersection assertion.

## Verification
Run `python3 verify.py` using only the Python standard library. It verifies the exhaustive symbolic seven-ray analysis, the eight- and nine-ray fan determinants and intersection strings, and twelve two-ray growth steps from each starting fan. The infinite growth claim is proved by the displayed local identity, not by the finite repetitions. The symbolic \(n\)-parameter check is exact and exhausts all \(n\ge0\), rather than checking a finite list of Hirzebruch surfaces.

## Relationship to prior work
Ito, Zeng and Zeng supply the general criterion for \(\otimes\)-generation and discuss anticanonical obstructions on proper toric varieties; that general criterion is used here as a premise, not represented as new. Cox, Little and Schenck give the classification and local fan calculus for smooth complete toric surfaces. Broomhead and Ploog relate smooth toric surface autoequivalences to spherical twists from \((-2)\)-curves, but a derived-autoequivalence generating statement is not a classification of attainable Picard ranks for a tensor-generating canonical bundle. The additional result here is the exact one-gap ray/Picard spectrum and explicit unbounded constructions.

## Limitations
The result is an existence spectrum, not a classification up to isomorphism of all qualifying fans with a given number of rays. It does not assert that the canonical bundle is big, nef, or ample; in fact its self-intersection may be negative. The proof depends on the published toric tensor-generation criterion and the classical smooth toric surface classification. Historical priority is provisional: a full-text comparison with every potentially relevant recent article was not available, and abstract/introductory searches alone cannot certify priority. No independent mathematical validation has been performed.

## References
1. Daigo Ito, Michael R. Zeng, Xiangru Zeng, *Tensor-generating line bundles on toric varieties*, arXiv:2610.22279v1 (first submitted 2026-10-15), Theorem 1.1 and Section 3. https://arxiv.org/abs/2610.22279
2. David A. Cox, John B. Little, Henry K. Schenck, *Toric Varieties*, AMS, 2011, Chapter 10, especially Section 10.4, the classification of smooth toric surfaces and the divisor self-intersection rules. https://www.ams.org/bookstore/pspdf/gsm-124-prev.pdf
3. Nathan Broomhead and David Ploog, *Autoequivalences of toric surfaces*, Proc. Amer. Math. Soc. 142 (2014), 1133–1146; arXiv:1010.1717. https://arxiv.org/abs/1010.1717
