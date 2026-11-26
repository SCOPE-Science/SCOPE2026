# Three components of the three-dimensional nilpotent left-symmetric dialgebra variety

## Finding

For the four left-symmetric dialgebra identities displayed by Rikhsiboev [1, Definition 2.1], the reduced variety of labelled nilpotent structures on a three-dimensional vector space over an algebraically closed field has exactly **three** irreducible components of dimensions **10, 9 and 8**, in every characteristic. The dimension-10 component is the locus \(S^3=0,\ \dim S^2\le 1\). The other components are the closures of the two loci with \(S^3\ne 0\), distinguished by whether the products agree modulo \(S^3\).

The additional identity \(x\vdash(y\dashv z)=x\vdash(y\vdash z)\) cuts out, on the reduced nilpotent variety, precisely the union of the dimension-10 and dimension-9 components. This explains why the two-component answer holds for a stronger condition but not for the four published identities alone.

For \(P=q^2+q+1\), the exact number of labelled structures satisfying the four published identities over any finite field \(\mathbb F_q\) is
\[
1+P(q^8-1)+P(q+1)(q-1)q^2(q^3-1)+P(q+1)q^3(q-1)^2+P(q^2-1)(q^2-q).
\]
For the locus subject also to the additional identity, omit the fourth summand \(P(q+1)q^3(q-1)^2\). At \(q=2,3\) the counts for the four identities alone are 2584 and 115857, versus 2416 and 110241 with the additional identity.

## Assumptions and scope

Write \(S^r\) for the span of all length-\(r\) products with arbitrary binary bracketing and arbitrary choices of the two bilinear operations on the fixed labelled vector space \(S\). Nilpotent means \(S^r=0\) for all sufficiently large \(r\). The four identities are
\[
\begin{aligned}
x\dashv(y\dashv z)&=x\dashv(y\vdash z),\\
(x\dashv y)\vdash z&=(x\vdash y)\vdash z,\\
x\dashv(y\dashv z)-(x\dashv y)\dashv z&=y\vdash(x\dashv z)-(y\vdash x)\dashv z,\\
x\vdash(y\vdash z)-(x\vdash y)\vdash z&=y\vdash(x\vdash z)-(y\vdash x)\vdash z.
\end{aligned}
\]
In particular, the first term of the fourth identity has inner operation \(\vdash\). Replacing this inner operation by \(\dashv\) does not give an equivalent four-identity presentation. The formulas concern actual bilinear maps, not isomorphism classes or the structure of a nonreduced scheme.

## Proof

**1. Intrinsic flag and all possible tables.** The powers are descending, by contracting one innermost multiplication to a single element. If \(S^2=S\), all powers equal \(S\); if \(S^3=S^2\ne0\), multiplying by \(S\) on both sides with both operations shows inductively that \(S^r=S^2\) for all \(r\ge2\). Thus for a nilpotent structure with \(S^3\ne0\) one has \(\dim S^2=2,\dim S^3=1\). Multiplication of an arbitrary element on either side of \(S^3\) is an endomorphism of this line; any nonzero scalar action could be iterated indefinitely. Hence \(S^3\) annihilates \(S\) on both sides for both operations.

In a basis adapted to \(S^3=\langle e_3\rangle\subset S^2=\langle e_2,e_3\rangle\), write the remaining potentially nonzero entries as
\[
\begin{array}{ll}
e_1\dashv e_1=a e_2+u e_3,&e_1\vdash e_1=b e_2+v e_3,\\
e_1\dashv e_2=c e_3,&e_1\vdash e_2=\ell e_3,\\
e_2\dashv e_1=d e_3,&e_2\vdash e_1=f e_3,\\
e_2\dashv e_2=h e_3,&e_2\vdash e_2=j e_3.
\end{array}
\]
At least one of \(a,b\) is nonzero. The third and fourth identities on \((e_1,e_2,e_1)\) give \(aj=bj=0\). The third identity on \((e_2,e_1,e_1)\) and \((e_1,e_1,e_2)\) gives \(ah=(a-b)h=0\). So \(h=j=0\) and \(S^4=0\). After this vanishing only \((e_1,e_1,e_1)\) can contribute a nonzero identity evaluation. The equations from that triple are equivalent to
\[
(a-b)c=(a-b)f=0,\qquad a(c-\ell)+(b-a)d=0.
\]
Indeed, the first two identities give the first two equalities; the third gives the last, and the fourth repeats \((a-b)f=0\).

There are two disjoint possibilities, each giving valid tables and the stated intrinsic flag:

- **Equal leading products:** \(a=b\ne0,\ c=\ell,\ (c,d,f)\ne(0,0,0)\), with \(u,v\) arbitrary.
- **Unequal leading products:** \(a\ne b,\ c=f=0,\ \ell\ne0,\ d=a\ell/(b-a)\), with \(u,v\) arbitrary.

For example \(e_1\vdash e_1=e_2,\ e_1\vdash e_2=e_3\), all other products zero, is in the second locus and violates the additional identity. It works in every characteristic and is the algebra \(F_2\) of [1, Theorem 4.1] over \(\mathbb C\). The ordinary product difference \((x\dashv y)-(x\vdash y)\) in the equal-leading-product locus takes values in \(S^3\); the example and the general second table have \(x\vdash(y\dashv z-y\vdash z)=(a-b)\ell e_3\ne0\) at \(x=y=z=e_1\).

For comparison, replacing the inner \(\vdash\) of the fourth identity by \(\dashv\) does not change the preceding deductions that \(h=j=0\). It changes the equation on \((e_1,e_1,e_1)\) to \((a-b)(\ell-f)=0\). Together with the first two identities, if \(a\ne b\) this forces \(c=f=\ell=0\) and then the third identity gives \(d=0\), contrary to \(S^3\ne0\). The resulting non-two-step locus is therefore exactly the equal branch; the two-step locus is unchanged. In this dimension and nilpotent regime the altered four identities cut out exactly the same reduced locus as the published four plus the additional identity.

**2. Incidence, closures and the remaining orbit.** The nilpotent locus is closed, because the preceding bound and the two-step case show that nilpotency is equivalent here to the finitely many length-four product identities \(S^4=0\). The rank-at-most-one two-step locus \(Z=\{S^3=0,\dim S^2\le1\}\) is the proper incidence image from the rank-eight vector bundle over \(\mathbb P(S)\) parametrizing two maps \((S/L)^{\otimes2}\to L\). The line is unique on the nonzero locus, and its recovery there is regular by the constant-rank image map. Thus \(Z\) is irreducible of dimension \(2+8=10\).

Each of the two non-two-step loci maps to the complete flag variety by its intrinsic powers. The map is regular, since these powers are the images of constant-rank product maps. Local frames on the flag variety give the above parameter spaces as local products with the base. The equal branch has fiber \(\mathbb G_m\times\mathbb A^2\times(\mathbb A^3\setminus0)\) of dimension six. The unequal branch has fiber \(\{(a,b):a\ne b\}\times\mathbb G_m\times\mathbb A^2\) of dimension five. Adding the flag dimension three gives irreducible closures \(Y_=,Y_{\ne}\) of dimensions nine and eight.

Every rank-two two-step table factors via two outputs on the one-dimensional quotient \(S/S^2\); any ordered basis of the image plane gives the same orbit under a labelled change of basis. This orbit lies in \(Y_=\): in a fixed basis take
\[
e_1\dashv e_1=e_2+e_3,\quad e_1\vdash e_1=e_2,\quad
e_2\dashv e_1=e_2\vdash e_1=t e_3,
\]
all other entries zero. For \(t\ne0\) it lies in the equal branch, while \(t=0\) gives the required rank-two two-step orbit. Thus the nilpotent locus is the union of \(Z,Y_=,Y_{\ne}\). Each \(Y\) contains a non-two-step point, so neither is contained in \(Z\); dimension rules out containment of \(Z\) in either \(Y\), and of \(Y_=\) in \(Y_{\ne}\). Conversely \(Y_=\) satisfies the additional polynomial identity everywhere by closedness, and \(Y_{\ne}\) does not, so \(Y_{\ne}\) is not contained in \(Y_=\). This proves the component claims. The additional identity holds automatically in the two-step case and exactly on the equal branch in the non-two-step case, proving the stated description of its reduced locus.

**3. Counting.** There are \(P\) lines and \(P(q+1)\) complete flags. Each nonzero point of \(Z\) has a unique image line and contributes to \(P(q^8-1)\); the zero point is counted separately. Each intrinsic flag contributes \((q-1)q^2(q^3-1)\) equal-branch and \(q(q-1)(q-1)q^2\) unequal-branch tables. A rank-two two-step table over a fixed image plane is an ordered pair of independent outputs after a quotient generator is fixed, giving \((q^2-1)(q^2-q)\) choices per plane. These are disjoint strata; summing gives both formulas.

## Verification

Run `python3 checks/verify.py` with the Python standard library. This enumerates the ten-coordinate candidate tables for a fixed flag over the prime fields of sizes two and three, allows both \(e_2\)-square coefficients before testing, and evaluates the identities on basis triples for both versions of the fourth identity. It checks the separate flag counts and both labelled formulas at those orders. The general characteristic-independent geometry and counts are established by the proof, not by extrapolation from those calculations.

## Relationship to prior work and limitations

The complex isomorphism-class theorem of [1, Theorem 4.1] already supplies representatives in both non-two-step regimes; it asks for geometric classification in its concluding remarks. The present claims are about irreducible components of the labelled variety, not new orbit representatives. The open problems for diassociative and dendriform varieties in [2] concern other identities. No classification of individual degenerations or of other dimensions is claimed. The point-count argument is about labelled structures over finite fields, not a count of rational or geometric isomorphism classes.

## References

1. I. M. Rikhsiboev, *The algebraic classification of three-dimensional nilpotent left-symmetric dialgebras*, arXiv:2611.23945v1, Definition 2.1, Theorem 4.1 and concluding remarks. https://arxiv.org/abs/2611.23945
2. I. M. Rikhsiboev, *Classification problems for diassociative and dendriform algebras: a survey*, arXiv:2611.19249v1, §2.5 and Problem 7.4. https://arxiv.org/abs/2611.19249
