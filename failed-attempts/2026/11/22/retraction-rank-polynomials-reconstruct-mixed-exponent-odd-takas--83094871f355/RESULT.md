# Retraction-rank polynomials reconstruct mixed-exponent odd Takasaki quandles

## Finding
Let \(p\) be any odd prime and \(A=C_{p^2}^a\oplus C_p^b\) with \(a,b\ge0\). On the Takasaki (core) quandle \(Q(A)\), put \(x\triangleright y=2y-x\), and define the image-cardinality polynomial
\[
R_A(T)=\sum_{F\in\operatorname{End}(Q(A)),\;F^2=F}T^{|F(A)|}.
\]
Write \(N=2a+b\), and for nonnegative integers \(u,v\) put
\[
\Gamma_p(u,v)=p^{u^2+2uv}|\operatorname{GL}_u(\mathbb F_p)|\,|\operatorname{GL}_v(\mathbb F_p)|,
\qquad |\operatorname{GL}_0(\mathbb F_p)|=1.
\]
Then the entire type-refined enumeration is
\[
\boxed{R_A(T)=\sum_{r=0}^a\sum_{s=0}^b
\frac{\Gamma_p(a,b)}{\Gamma_p(r,s)\Gamma_p(a-r,b-s)}
p^{2(a-r)+b-s}T^{p^{2r+s}}.}
\]
The summand indexed by \((r,s)\) counts precisely retractions whose images are affine copies of \(C_{p^2}^r\oplus C_p^s\). Each such type forms one orbit under the affine automorphism group, so there are \((a+1)(b+1)\) orbits. In particular, for nontrivial \(A\),
\[
\boxed{[T^p]R_A(T)=p^{2N-2}\frac{p^b-1}{p-1}.}
\]
**Reconstruction:** The highest exponent of \(T\) occurring is \(p^N\), and has coefficient one. Its prime-power factorization determines \(p,N\); the displayed coefficient of \(T^p\) then determines \(b\) uniquely because \(1+p+\cdots+p^{b-1}\) strictly increases with \(b\). Thus \(a=(N-b)/2\), and the *univariate retraction-rank polynomial is a complete isomorphism invariant* for all finite abelian groups of odd prime-power order and exponent at most the square of the underlying prime. The trivial group has polynomial \(T\) and is unique as well.

The possible image cardinalities are exactly \(p^{2r+s}\) for \(0\le r\le a\), \(0\le s\le b\). If \(b=0\), only even exponents occur; if \(b\ge1\), the full interval \(p^0,p^1,\ldots,p^N\) occurs. For instance, 
\[
R_{C_9\oplus C_3}(T)=27T+81T^3+27T^9+T^{27},
\]
while
\[
R_{C_9\oplus C_3^2}(T)=81T+2916T^3+1458T^9+324T^{27}+T^{81}.
\]

## Assumptions and scope
All groups are finite additive abelian groups. The operation \(x\triangleright y=2y-x\) uses the right-translation convention; sources using the left-translation convention \(x\triangleright y=2x-y\) are equivalent after exchanging input order. A quandle homomorphism is an arbitrary set map preserving this operation; **additivity is deduced, not assumed**. A retraction is a composition-idempotent endomorphism. Rank means the cardinality of the set image. The theorem is restricted to odd prime-power abelian groups of exponent at most \(p^2\); it makes no assertion for higher exponents, groups with two-primary torsion, or arbitrary Alexander quandles. The empty direct sums are the trivial group.

## Proof
**1. Affine normal form.** Let \(F:Q(A)\to Q(A)\) preserve \(\triangleright\), let \(c=F(0)\), and define \(g(x)=F(x)-c\). The homomorphism equation becomes
\[
g(2y-x)=2g(y)-g(x).
\]
With \(x=0\), \(g(2y)=2g(y)\). With \(y=0\), \(g(-x)=-g(x)\). Since multiplication by \(2\) is a bijection on any odd-order abelian group, every ordered pair \((u,v)\) is \((2y,-x)\) for suitable \(x,y\). Thus \(g(u+v)=g(u)+g(v)\), so \(g\) is additive. Conversely every affine map \(F(x)=e(x)+c\) with additive endomorphism \(e\) preserves \(\triangleright\). Composition gives \(F^2(x)=e^2(x)+e(c)+c\); hence \(F^2=F\) exactly when \(e^2=e\) and \(e(c)=0\).

**2. Direct-sum correspondence.** An additive idempotent \(e\) yields the uniquely ordered internal decomposition
\[
A=\operatorname{im}e\oplus\ker e,
\]
where \(e\) projects onto the first factor. Conversely every such ordered decomposition defines one \(e\). The decomposition theorem for finite abelian groups implies that the image is necessarily \(C_{p^2}^r\oplus C_p^s\) and the kernel \(C_{p^2}^{a-r}\oplus C_p^{b-s}\), for unique \(0\le r\le a\), \(0\le s\le b\). Every ordered decomposition of this isomorphism type is sent to the standard one by some group automorphism, because the sum of isomorphisms on both factors is an automorphism of \(A\).

**3. Automorphism-group order.** Relative to the two cyclic-exponent blocks, an additive endomorphism is given by blocks \(X,Y,Z,W\): \(X\) is an \(a\times a\) matrix over \(\mathbb Z/p^2\); \(Y\) maps \(C_p^b\) to \(C_{p^2}^a\) and has entries divisible by \(p\); \(Z\) and \(W\) are over \(\mathbb F_p\), of sizes \(b\times a\) and \(b\times b\). The endomorphism is invertible precisely when the reductions of \(X\) and \(W\) are separately invertible, since they act invertibly on the corresponding layers of the \(p\)-adic filtration (and the converse follows from the finite-group Nakayama criterion). There are \(p^{a^2}\) lifts of \(X\), \(p^{ab}\) choices each for \(Y,Z\), and the two independent general-linear choices. Hence
\[
|\operatorname{Aut}(C_{p^2}^a\oplus C_p^b)|=
\Gamma_p(a,b)=p^{a^2+2ab}|\operatorname{GL}_a(\mathbb F_p)|\,|\operatorname{GL}_b(\mathbb F_p)|.
\]
By transitivity and orbit–stabilizer, the number of ordered decompositions with image type \((r,s)\) is exactly
\[
D_{r,s}=\frac{\Gamma_p(a,b)}{\Gamma_p(r,s)\Gamma_p(a-r,b-s)}.
\]
The stabilizer is the product of the automorphism groups of the two specified summands: an automorphism preserving each factor is precisely a pair of independent factor automorphisms.

**4. Translations and rank polynomial.** For each projection of type \((r,s)\), the allowed affine translations are exactly the elements \(c\in\ker e\), numbering \(p^{2(a-r)+b-s}\). Each map has image \(c+\operatorname{im}e\) of cardinality \(p^{2r+s}\). Multiplying by \(D_{r,s}\), then summing, proves the displayed polynomial. Moreover a translation conjugates \(F(x)=e(x)+c\) into \(e\), because \(c\in\operatorname{im}(1-e)\). Linear automorphisms conjugate any two projections of the same summand type. Therefore the full affine automorphism group has one orbit per \((r,s)\), and every permitted type actually occurs.

**5. The sharp one-coefficient reconstruction.** Image cardinality \(p\) forces \((r,s)=(0,1)\). For \(b\ge1\), using the general-linear formula,
\[
D_{0,1}=\frac{\Gamma_p(a,b)}{(p-1)\Gamma_p(a,b-1)}
=p^{2a+b-1}\frac{p^b-1}{p-1}=p^{N-1}[b]_p.
\]
The kernel of this rank-\(p\) projection has \(p^{N-1}\) elements, giving \([T^p]R_A(T)=p^{2N-2}[b]_p\). For \(b=0\), no rank-\(p\) decomposition exists, and both sides are zero. Since an idempotent of full image cardinality is bijective and therefore the identity, the top monomial is uniquely \(T^{p^N}\). Prime-power uniqueness gives \(p,N\), and strict monotonicity of \([b]_p\) gives \(b\), then \(a\). Finally the exponent set \(\{2r+s\}\) equals the even integers between \(0\) and \(2a\) when \(b=0\), and equals every integer from \(0\) to \(2a+b\) when \(b\ge1\), completing the support claim.

## Verification
Run `python3 verify.py` from this package, using the Python standard library only. The program enumerates **all additive endomorphisms from images of cyclic generators**, tests \(e^2=e\) at each generator, constructs image subgroups independently, computes the invariant-factor type using \(|\operatorname{im}e|\) and \(|p\,\operatorname{im}e|\), and multiplies each linear retraction by its directly calculated kernel cardinality. It compares every resulting type coefficient to the orbit–stabilizer formula for \((p,a,b)=(3,0,2),(3,2,0),(3,1,1),(5,1,1),(3,1,2)\). All five cases agree exactly; the largest has \(380\) additive projections and \(4780\) affine retractions. As a further independent operation-level check, the program constructs all \(6561\) affine maps of \(C_9\oplus C_3\), tests every ordered pair in the quandle law, and checks composition idempotence directly; exactly \(136\) maps qualify. It finishes with `MIXED_TAKASAKI_CHECKS_PASSED`. This finite verification corroborates, but does not replace, the general proof.

## Relationship to prior work
Saki and Kiani (2020) classify subquandles of odd-order Takasaki quandles as subgroup cosets and prove that the **entire subquandle lattice** determines the underlying abelian group. Their lattice invariant is considerably richer than the single-variable retraction image-size polynomial; the latter's reconstruction of all odd exponent-at-most-square groups from its top degree and one low-rank coefficient is the separate assertion here. A published semisimple Alexander-quandle retraction census determines image ranks in the case of semisimple operators on **elementary-abelian** additive groups, but excludes the \(p^2\)-torsion considered here. A published automorphism classification for finite abelian core quandles determines invertible maps, not the noninvertible idempotent maps and their image-rank coefficients. Classical finite-abelian-group automorphism counts and orbit–stabilizer are ingredients, not novelty assertions. No inspected statement implies the specific low-coefficient reconstruction without the additional decomposition analysis; unindexed and implicit antecedents remain possible.

## Limitations
The family requires \(p\) odd and group exponent at most \(p^2\), and the criterion addresses isomorphism **within that family only**. The same rank polynomial need not distinguish arbitrary quandles. The general formulas draw on classical direct-summand and automorphism-group counting; novelty is asserted only relative to the inspected sources, not certified globally. The finite checker does not exhaust the infinite family. No independent mathematical audit has been performed.

## References
1. A. Saki and D. Kiani, *On the lattice of subquandles of a Takasaki quandle*, *Communications in Algebra* 49 (2021), 99–113; first published online 2020-07-30. DOI: https://doi.org/10.1080/00927872.2020.1797065.
2. *Semisimple Alexander-quandle retractions: a transformation–affine factorization and exact image ranks* (2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-semisimple-alexander-quandle-retractions-a-transformation-affine--117335b68a3e .
3. *Affine-rigidity classification and automorphism counts for finite abelian core quandles* (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-affine-rigidity-classification-and-automorphism-counts-for-finit--e6805a355e92 .
