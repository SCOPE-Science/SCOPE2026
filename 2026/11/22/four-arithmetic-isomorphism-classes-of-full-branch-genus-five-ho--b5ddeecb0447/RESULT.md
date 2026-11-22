# Four arithmetic isomorphism classes of full-branch genus-five Howe curves over \(\mathbb F_7\)

## Finding

Partition the eight points \(\mathbb P^1(\mathbb F_7)\) into two unordered four-sets \(A,B\). For a four-set \(S\), put
\[
 F_S(X,Z)=\prod_{a\in S\cap\mathbb F_7}(X-aZ)\,Z^{\mathbf 1_{\infty\in S}}.
\]
For \(\epsilon,\delta\in\{1,3\}\), define \(C_{A,B;\epsilon,\delta}\) to be the smooth projective normalization of the fiber product of the two genus-one double covers \(y^2=\epsilon F_A(X,Z)\) and \(z^2=\delta F_B(X,Z)\). Exchange of \((A,\epsilon)\) and \((B,\delta)\) does not change the marked cover. There are \(35\cdot4=140\) such presentations.

**The 140 curves represent exactly four \(\mathbb F_7\)-isomorphism classes of abstract smooth curves.** Indeed the natural action of \(\mathrm{PGL}_2(\mathbb F_7)\) on the \(140\) presentations, including the induced quadratic-character changes of the two double-cover equations, has four orbits of sizes \(14,14,28,84\). They have distinct Hasse--Weil numerators, so these four projectivity orbits are also precisely the four abstract curve-isomorphism classes. Their stabilizers among base projectivities have respective orders \(24,24,12,4\); these are *not* assertions about full geometric automorphism groups of the curves.

Write \(t_1,t_2\) for the traces of the two genus-one quotients. The complete arithmetic classification is:

| Unordered quotient traces | Presentations per class | Base-projectivity stabilizer | Hasse--Weil numerator |
|---|---:|---:|---|
| \((-4,-4)\) | 14 | 24 | \((1+7T^2)^3(1+4T+7T^2)^2\) |
| \((4,4)\) | 14 | 24 | \((1+7T^2)^3(1-4T+7T^2)^2\) |
| \((-4,4)\) | 28 | 12 | \((1+7T^2)^3(1+4T+7T^2)(1-4T+7T^2)\) |
| \((0,0)\) | 84 | 4 | \((1+7T^2)^5\) |

In particular, the maximal \(84\)-presentation stratum over \(\mathbb F_{49}\) is **one** \(\mathbb F_7\)-isomorphism class, rather than an unknown number of classes. The four classes have respectively \(16,0,8,8\) points over \(\mathbb F_7\); the last has \(120\) points over \(\mathbb F_{49}\), and the first three have \(88\) points there.

## Assumptions and scope

Throughout the base field is \(\mathbb F_7\), with nonsquare representative \(3\) and square set \(\{1,2,4\}\). All eight branch points are rational and exhaust \(\mathbb P^1(\mathbb F_7)\). Choose the four-set containing \(\infty\) as \(A=\{\infty\}\cup U\), with \(U\subset\mathbb F_7\) of size three, and set \(B=\mathbb F_7\setminus U\). This canonical choice gives the \(35\) unordered partitions and twist pairs without duplication. The equations of double covers are interpreted in the total space of \(\mathcal O_{\mathbb P^1}(2)\); changing binary homogeneous coordinates by \(\mathrm{GL}_2\) gives isomorphic curves after the indicated square-class changes.

The double covers are distinct and have disjoint branch sets. Their fiber-product normalization is geometrically connected and smooth of genus \(5\) by the tame \((\mathbb Z/2)^2\) Riemann--Hurwitz formula, or the genus formula for Howe curves with \((g_1,g_2,r)=(1,1,0)\). The claim counts abstract \(\mathbb F_7\)-isomorphism classes *within the specified full rational eight-branch construction*, not all genus-five curves or all Howe curves over \(\mathbb F_7\).

## Proof

**1. The projectivity action, including twists.** Let \(M\in\mathrm{GL}_2(\mathbb F_7)\) represent a projectivity. For each four-set \(S\), the binary quartics \(F_S(M^{-1}(X,Z))\) and \(F_{MS}(X,Z)\) have exactly the same simple geometric roots, so they are proportional by a unique \(k_S(M)\in\mathbb F_7^\times\):
\[
 F_S(M^{-1}(X,Z))=k_S(M)F_{MS}(X,Z).
\]
Thus a quadratic-cover twist by \(\epsilon\) becomes a twist by \(\epsilon k_S(M)\), considered modulo squares. Swapping the two four-sets if necessary to restore the convention \(\infty\in A\) defines a genuine action on \(35\cdot4=140\) states. Scaling \(M\) multiplies each \(k_S\) by a fourth power, hence does not change the action. Every such projectivity furnishes an actual \(\mathbb F_7\)-isomorphism of smooth fiber-product normalizations.

**2. Exhaustive orbit certificate.** A \(2\)-by-\(2\) matrix of nonzero determinant, scaled to put its first nonzero entry equal to one, enumerates every element of \(\mathrm{PGL}_2(\mathbb F_7)\) exactly once, giving \(336\) matrices. On each of the \(140\) states, form the two transformed quartics and compute their nonzero proportionality constants at any rational projective test point not on the transformed branch set. Square status gives the new twist bits. The included standard-library program `scripts/verify_orbits.py` constructs all \(336\) permutations, tests that they biject the \(140\) states, checks the group law for all \(336^2\) ordered pairs, and enumerates the four complete orbits. Their sizes are \(14,14,28,84\), hence their stabilizer orders are \(336/14=24\), \(24\), \(12\) and \(4\). The two bare partition orbits have sizes \(14\) and \(21\); the first splits into twist orbits \(14,14,28\), while the second yields one twist orbit of size \(84\).

For explicit representatives, take \(U=\{0,1,3\}\) and twist pairs \((\epsilon,\delta)=(3,1),(1,3),(1,1)\), giving orbit sizes \(14,14,28\), respectively. Take \(U=\{0,1,2\}\) and \((\epsilon,\delta)=(1,1)\) for the size-\(84\) orbit. Here \(A=\{\infty\}\cup U\) and \(B=\mathbb F_7\setminus U\). The checker directly identifies their trace pairs as in the table.

**3. Independent arithmetic separation.** The genus-three quotient associated with the product of the two involutions is a quadratic twist of \(D:w^2=x^7-x\), since the eight branch points exhaust the rational projective line. Its \(\mathbb F_7\)-point count is eight. Over \(\mathbb F_{49}\), the map \(x\mapsto x^7-x\) has image the seven-element trace-zero subspace and seven-element kernel. Every nonzero trace-zero value \(w\) satisfies \(w^7=-w\), hence \(w^6=-1\) and \(w^{24}=1\), so it is a square in \(\mathbb F_{49}\). Therefore \(\#D(\mathbb F_{49})=7+42\cdot2+1=92\), the Weil upper bound for genus three. Both quadratic twists have the same genus-three numerator \((1+7T^2)^3\): they have trace zero over \(\mathbb F_7\), and all Frobenius eigenvalues square to \(-7\).

For either genus-one double cover \(E:y^2=\epsilon F_S\), its \(\mathbb F_7\)-trace is exactly
\[
 t(E)=-\sum_{[X:Z]\in\mathbb P^1(\mathbb F_7)}\chi(\epsilon F_S(X,Z)),
\]
where \(\chi(0)=0\). The verifier evaluates these eight terms independently for all \(140\) states. The resulting trace-pair frequencies are \(14\) pairs \((-4,-4)\), \(14\) pairs \((4,4)\), \(28\) pairs \((-4,4)\), and \(84\) pairs \((0,0)\). The three nontrivial quotient Jacobians multiply up to the genus-five Jacobian by the standard tame \((\mathbb Z/2)^2\) isogeny relation. Thus the numerator has exactly the product form in the displayed table.

These four rational polynomials are pairwise different. Since isomorphic smooth curves have the same zeta function, distinct projectivity orbits cannot become isomorphic even through an isomorphism that forgets the covering maps. Combined with projective transitivity inside each orbit, this proves **exactly four abstract curve-isomorphism classes**.

## Verification

Run `python3 scripts/verify_orbits.py` using Python 3 without third-party dependencies. It tests all \(336\) projectivities on all \(140\) coefficient-twist states; checks all \(336^2\) group-composition equations; verifies orbit-stabilizer identities; independently enumerates all genus-one quotient trace sums and confirms the four orbit-wise constant trace pairs. Its expected final line begins `HOWE_F7_MODULI_VERIFIED group=336 states=140 partitions=35 orbits=14,14,28,84`. The genus-three quotient factor is proved separately above rather than inferred from finite sample counts. All computations are exhaustive finite checks for the precisely stated \(\mathbb F_7\) domain; no geometric classification outside this family is asserted.

## Relationship to prior work

Kudo's genus-five Howe-curve plane-sextic construction provides the relevant \((1,1,0)\) genus-five geometry, and explicitly describes isomorphism classification as a possible future application rather than giving these four \(\mathbb F_7\) classes. Katsura--Takashima supply the standard genus and isogeny framework; the isogeny itself is not claimed here. A later paper of Kawakita treats particular maximally point-rich twisted generalized Howe curves, primarily with different branch intersection patterns and primes, but does not enumerate this full \(\mathbb F_7\) eight-point configuration. The exact marked-model Weil frequencies, which can also be independently recovered by the included verifier, are arithmetic inputs; the claim's distinguishing contribution is the full projective orbit calculation and its proof that Weil types correspond **exactly** to abstract isomorphism classes. General \(\mathrm{PGL}_2\)-orbit methods and the elliptic point-count formula are standard, not new.

## Limitations

This is a complete classification only for fiber products of the described two elliptic double covers with all eight rational branch points used. The base-projectivity stabilizer orders are not full automorphism group orders. The four classes may have additional unmarked coverings or extra automorphisms; neither is classified. No assertion about a classification over algebraic closures or across finite fields other than \(\mathbb F_7\) is made. The finding has not undergone independent mathematical audit, and unindexed equivalent arithmetic classifications remain a priority risk.

## References

1. M. Kudo, *Explicit construction of a plane sextic model for genus-five Howe curves, II*, arXiv:2401.00760v1, first posted 2024-01-01, especially Sections 1, 2.1 and 5. https://arxiv.org/html/2401.00760v1 .
2. M. Qiu Kawakita, *Generalised Howe curves of genus five attaining the Serre bound*, arXiv:2412.03071, first posted 2024-12-04, especially Sections 2 and 4. https://arxiv.org/abs/2412.03071 .
3. T. Katsura and K. Takashima, *Decomposed Richelot isogenies of Jacobian varieties of hyperelliptic curves and generalized Howe curves*, cited in Kudo, Section 2.1 (standard genus formula and isogeny).
