# Two components of the three-dimensional nilpotent left-symmetric dialgebra variety

## Finding

Let \(k\) be an algebraically closed field and let \(V\) be a three-dimensional vector space over \(k\). Give \(V\) two bilinear operations \(\dashv,\vdash\), subject to the four left-symmetric dialgebra identities reproduced below (as recalled in [1] and [3]). Call the resulting dialgebra nilpotent if all sufficiently long, arbitrarily bracketed products using either operation are zero. Let \(\mathcal N\) be the **reduced algebraic variety of labelled nilpotent structures** inside
\[
\operatorname{Hom}_k(V\otimes V,V)^{\oplus2}.
\]
Then \(\mathcal N\) has **exactly two irreducible components**, of dimensions \(10\) and \(9\). They are not equidimensional.

Define \(S^1=S\) and, for \(r\ge2\),
\[
S^r=\sum_{i+j=r}\bigl(S^i\dashv S^j+S^i\vdash S^j\bigr),
\]
where sums mean linear spans. The dimension-\(10\) component is precisely the closed locus
\[
Z=\{S:S^3=0,\ \dim_k S^2\le1\}.
\]
The dimension-\(9\) component is \(Y=\overline{U}\), where
\[
U=\{S:S^3\ne0\}.
\]
In particular \(U\) is irreducible and is a dense open subset of \(Y\). Its generic members have \(\dim S^2=2\) and \(\dim S^3=1\). The only stratum not obviously in either component is \(S^3=0\), \(\dim S^2=2\); it is one isomorphism orbit and lies in \(Y\) via an explicit degeneration.

The same normal-form proof gives a **labelled point count over every finite field** \(\mathbb F_q\), with \(q\) any prime power:
\[
\boxed{\begin{aligned}
\#\mathcal N(\mathbb F_q)={}&1+(q^2+q+1)(q^8-1)\\
&+(q^2+q+1)(q+1)(q-1)q^2(q^3-1)\\
&+(q^2+q+1)(q^2-1)(q^2-q).
\end{aligned}}
\]
The three nonconstant summands count respectively the nonzero rank-one-product, non-two-step, and rank-two-two-step strata. For \(q=2\) and \(q=3\), the total counts are \(2416\) and \(110241\).

## Assumptions and scope

The four identities are, for all \(x,y,z\in S\):
\[
\begin{aligned}
 x\dashv(y\dashv z)&=x\dashv(y\vdash z),\\
 (x\dashv y)\vdash z&=(x\vdash y)\vdash z,\\
 x\dashv(y\dashv z)-(x\dashv y)\dashv z
 &=y\vdash(x\dashv z)-(y\vdash x)\dashv z,\\
 x\vdash(y\dashv z)-(x\dashv y)\vdash z
 &=y\vdash(x\vdash z)-(y\vdash x)\vdash z.
\end{aligned}
\]
Here \(S^2\) means the span of values of **both** operations and is not a square under just one operation. All varieties and dimensions refer to labelled structure constants on a fixed \(V\), not to coarse isomorphism-class spaces or the possibly nonreduced defining scheme. The geometric component statement is made over algebraically closed fields; the arithmetic formula counts labelled structures over finite fields without taking isomorphism quotients.

## Proof

**1. The nilpotency bound and structural trichotomy.** By definition of the nilpotency powers, \(S^3=S\dashv S^2+S^2\dashv S+S\vdash S^2+S^2\vdash S\). If \(S^2=S\) or \(S^3=S^2\ne0\), this equality makes a nonzero power persist indefinitely; nilpotency therefore excludes both equalities. Since \(\dim S=3\), every nilpotent \(S\) has \(\dim S^2\le2\). When \(\dim S^2\le1\), necessarily \(S^3=0\). Otherwise \(\dim S^2=2\) and \(\dim S^3\in\{0,1\}\).

Suppose \(S^3\ne0\). Then \(\dim S^2=2\) and \(L=S^3\) is a line. Since \(S^4\subseteq L\), left or right multiplication by any element restricts to a scalar endomorphism of \(L\). Any nonzero such scalar could be iterated to form arbitrarily long nonzero products, contradicting nilpotency. Hence \(L\) annihilates \(S\) on both sides under both operations.

Choose an adapted basis \(e_1,e_2,e_3\) with \(S^2=\langle e_2,e_3\rangle\) and \(S^3=\langle e_3\rangle\). Before imposing the identities, the potentially nonzero products are
\[
\begin{array}{ll}
e_1\dashv e_1=a e_2+u e_3,&e_1\vdash e_1=b e_2+v e_3,\\
e_1\dashv e_2=c e_3,&e_2\dashv e_1=d e_3,\\
e_1\vdash e_2=e e_3,&e_2\vdash e_1=f e_3,\\
e_2\dashv e_2=h e_3,&e_2\vdash e_2=j e_3,
\end{array}
\]
with \((a,b)\ne(0,0)\), all products involving \(e_3\) zero. Evaluate the third and fourth identities on \((e_1,e_2,e_1)\) to obtain \(aj=bj=0\). Evaluate the third identity on \((e_2,e_1,e_1)\) to get \(ah=0\), and on \((e_1,e_1,e_2)\) to get \((a-b)h=0\). Because at least one of \(a,b\) is nonzero, \(h=j=0\), and thus \(S^4=0\).

Evaluate all four identities on \((e_1,e_1,e_1)\); they give
\[
(a-b)c=(a-b)f=(a-b)(e-f)=0,
\qquad a(c-e)+(b-a)d=0.
\]
If \(a\ne b\), these equations force \(c=d=e=f=0\), contradicting \(S^3\ne0\). Therefore \(a=b\ne0\), and the last equation says \(c=e\). Every remaining identity on basis triples is automatically zero, so the complete normal form is
\[
\boxed{\begin{array}{ll}
e_1\dashv e_1=a e_2+u e_3,&e_1\vdash e_1=a e_2+v e_3,\\
e_1\dashv e_2=e_1\vdash e_2=c e_3,&e_2\dashv e_1=d e_3,\\
&e_2\vdash e_1=f e_3,
\end{array}}
\]
where \(a\ne0\), \((c,d,f)\ne(0,0,0)\), and \(u,v\) are arbitrary. Conversely, direct substitution proves every such table satisfies all four identities and has \(S^2=\langle e_2,e_3\rangle\), \(S^3=\langle e_3\rangle\) and \(S^4=0\). This also proves the universal nilpotency-index bound \(S^4=0\) in dimension three.

**2. The component \(Z\).** For each line \(L\subset V\), two bilinear products with values in \(L\), both vanishing whenever either input lies in \(L\), are simply two elements of \(\operatorname{Hom}((V/L)^{\otimes2},L)\). Their parameter space is a rank-\(8\) vector bundle over \(\mathbb P(V)\cong\mathbb P^2\), irreducible of dimension \(2+8=10\). Its incidence image in the affine space of structure constants is closed: the incidence equations are closed in \(\mathbb P(V)\times\operatorname{Hom}(V^{\otimes2},V)^{\oplus2}\), and projection along the projective factor is proper. This image is exactly \(Z\). For a nonzero product, \(L=S^2\) is unique; thus the map is generically one-to-one and \(\dim Z=10\). Every member of \(Z\) is automatically an LSDA, since all triple products vanish.

**3. The component \(Y\).** Every member of \(U\) has a uniquely determined full flag \(S^3\subset S^2\subset V\), of type \((1,2)\). The flag variety has dimension \(3\). Over an adapted local trivialization, the normal form above describes the fibers of \(U\) as the open subset
\[
\{(a,u,v,c,d,f)\in\mathbb A^6:a\ne0,\ (c,d,f)\ne0\}.
\]
Hence \(U\) is irreducible of dimension \(3+6=9\), so its closure \(Y\) is irreducible of dimension \(9\). This conclusion does not require an orbit classification.

**4. The remaining rank-two, two-step stratum.** If \(S^3=0\) and \(\dim S^2=2\), the two products factor through the one-dimensional quotient \(V/S^2\), and their two values on a quotient generator form a basis of \(S^2\). Thus all such algebras are isomorphic under \(\operatorname{GL}(V)\) to the table \(e_1\dashv e_1=e_2\), \(e_1\vdash e_1=e_3\), all other products zero.

Here is an explicit polynomial degeneration from \(U\). In a fixed basis take
\[
 e_1\dashv e_1=e_2+e_3,\quad e_1\vdash e_1=e_2,
 \quad e_2\dashv e_1=e_2\vdash e_1=t e_3,
\]
with all other basis products zero. For \(t\ne0\), this is in \(U\), with \(S^3=\langle e_3\rangle\); for \(t=0\), it is a rank-two, two-step algebra (its two displayed square values are linearly independent). All tables satisfy the identities by the normal form, including at \(t=0\). Thus the single rank-two two-step orbit lies in \(Y\).

Every nilpotent three-dimensional LSDA belongs either to \(Z\), to \(U\), or to that orbit. Therefore \(\mathcal N=Z\cup Y\). Since \(Y\) contains points with \(S^3\ne0\), it is not contained in \(Z\); since \(\dim Z=10>9=\dim Y\), \(Z\) is not contained in \(Y\). These are precisely the two irreducible components. In particular, the nilpotent locus is closed, since in dimension three nilpotency is equivalent to \(S^4=0\).

**5. Counting over finite fields.** Set \(P=q^2+q+1\), the number of lines or planes in \(\mathbb F_q^3\). Rank-at-most-one products with cube zero contribute \(1+P(q^8-1)\), because the zero structure has no distinguished image line and each nonzero one has exactly one. The number of complete flags is \(P(q+1)\), and each unique flag of a non-two-step structure supports \((q-1)q^2(q^3-1)\) normal-form tables. Finally, fixing \(S^2\) as a plane, the rank-two two-step structures are pairs of linearly independent vectors in that plane, giving \((q^2-1)(q^2-q)\) possibilities. Summing the mutually disjoint strata proves the displayed formula.

## Verification

The standalone `checks/verify.py` is executable with Python 3 and has no third-party dependencies. It evaluates all four multilinear identities on basis triples and exhausts the eight-coordinate fixed-flag tables over \(\mathbb F_2\) and \(\mathbb F_3\), obtaining exactly \(28\) and \(468\) admissible non-two-step tables respectively. It also checks the displayed degeneration over both fields, and computes the global formulas at field orders \(2,3,4,5\). Run: `python3 checks/verify.py`. Successful output terminates with `LSDA_TWO_COMPONENT_GEOMETRY_CHECKS_OK`. These finite experiments do not prove the geometric statements; the argument above supplies the all-field proof.

## Relationship to prior work

The survey by Rikhsiboev [1], first publicly posted on 14 November 2026, describes left-symmetric dialgebras as part of the extended Loday diagram and highlights irreducible components and degenerations as natural open geometric-classification questions for two-product algebras (Sections 2.5, 3.6, and 7). Its explicit Problem 7.4 concerns **diassociative and dendriform** varieties, not the entire left-symmetric dialgebra class, so the result here is a motivated analogue, **not a solution of that distinct problem**.

The geometric classification in [2] concerns single-product left-symmetric algebras and superalgebras rather than the two-product LSDA variety. Rikhsiboev [3], first publicly posted 18 November 2026, supplies a three-dimensional nilpotent **algebraic orbit classification** and identifies geometric classification and components as future questions (Section 7). That source is a later priority comparison, while the motivating survey [1] appeared four days earlier; the later article does not calculate the two irreducible components or the finite-field labelled census. The broader geometric theorem [4] concerns unrestricted single-product nilpotent algebras; its single-product irreducibility theorem does not imply the geometry of LSDA pairs. The incidence, flag and degeneration methods themselves are standard and not claimed as new.

## Limitations

The claim classifies irreducible components of the **reduced** nilpotent-structure variety, not scheme-theoretic nilpotents, singular loci, all individual orbit closures, or all degenerations between isomorphism classes. It does not cover nonnilpotent LSDA or dimensions greater than three. The formula counts labelled structure constants, not isomorphism classes. While the proof is characteristic-independent, historical priority against unpublished or unindexed geometric descriptions is not completely decidable from the inspected literature.

## References

[1] I. M. Rikhsiboev, *Classification problems for diassociative and dendriform algebras: a survey*, arXiv:2611.19249, first publicly posted 14 November 2026 (v1); https://arxiv.org/abs/2611.19249 . Sections 2.5, 3.6, 7. The currently rendered version was also checked; the v1 full text could not be retrieved separately.

[2] K. Abdurasulov, N. Daukeyeva and A. Saydaliyev, *The geometric classification of left-symmetric algebras and superalgebras*, arXiv:2607.28254, first posted 30 July 2026, https://arxiv.org/abs/2607.28254 .

[3] I. M. Rikhsiboev, *The algebraic classification of three-dimensional nilpotent left-symmetric dialgebras*, arXiv:2611.23945v1, first posted 18 November 2026, https://arxiv.org/abs/2611.23945 . Sections 2, 4, 6 and 7. This later article is a priority comparison rather than the earliest motivating source.

[4] I. Kaygorodov, M. Khrypchenko and S. A. Lopes, *The geometric classification of nilpotent algebras*, arXiv:2102.10392, first posted 20 February 2021, https://arxiv.org/abs/2102.10392 .
