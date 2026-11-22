# Primitive-transvection braid representations over finite local rings: two orbits and universal lift multiplicities

## Finding
Let \(R\) be any finite commutative local ring, let \(\mathfrak m\) be its maximal ideal, let \(q=|R/\mathfrak m|\), \(T=|R|\), and let \(n\ge2\). Define the **primitive transvections**
\[
\mathcal T_n(R)=\{I_n+u\phi:\ u\in R^n,\ \phi\in\operatorname{Hom}_R(R^n,R),\ \phi(u)=0,\ u\text{ and }\phi\text{ unimodular}\}.
\]
Here unimodular means that the coordinates generate the unit ideal. Count ordered pairs \((X,Y)\in\mathcal T_n(R)^2\) satisfying the three-strand braid relation \(XYX=YXY\).

There are **exactly two simultaneous \(\operatorname{GL}_n(R)\)-conjugacy orbits** of solutions. Representatives, with all unshown coordinates acting as the identity, are
\[
(X,Y)=(I_n+E_{12},I_n+E_{12})\quad\text{and}\quad
(X,Y)=(I_n+E_{12},I_n-E_{21}).
\]
Writing
\[
P_n(R)=\left(\frac Tq\right)^{2n-2}
\frac{(q^n-1)(q^{n-1}-1)}{q-1},
\]
there are exactly \(P_n(R)\) primitive transvections, \(P_n(R)\) diagonal solutions, and \(P_n(R)T^{2n-3}\) nondiagonal solutions. Consequently
\[
\boxed{\#\{(X,Y)\in\mathcal T_n(R)^2:XYX=YXY\}
=P_n(R)(1+T^{2n-3}).}
\]

The reduction map to the residue field has **constant fiber cardinality on each of the two orbits**: every diagonal field solution has precisely \((T/q)^{2n-2}\) lifts, while every nondiagonal field solution has precisely \((T/q)^{4n-5}\) lifts. These claims apply to nonprincipal local rings and mixed-characteristic rings, not only chain rings. Thus the entire census depends only on \(n,q,T\), not on the local ring's multiplication table.

As \(T\) increases with \(n,q\) fixed, the proportion of commuting-in-the-braid-sense ordered pairs among all primitive-transvection pairs is
\[
\frac{1+T^{2n-3}}{P_n(R)}
\sim \frac{q^{2n-2}(q-1)}{(q^n-1)(q^{n-1}-1)}\,T^{-1}.
\]
Conditioned on the braid relation, the probability of a nondiagonal pair tends to one.

## Assumptions and scope
A finite commutative local ring has identity \(1\ne0\). The integer \(n\) is at least two. The two factors must both be primitive transvections, i.e. rank-one split nilpotent perturbations of the identity with unimodular image generator and covector. They are not arbitrary unipotent matrices or arbitrary braid-group representations. The group acts by simultaneous change of basis. The residue-field cardinality is a prime power, but no coefficient field, principal maximal ideal, characteristic restriction, or equicharacteristic hypothesis is assumed.

The first archival starting point is the preprint of Tuba and Wenzl dated 1999-12-02, which describes the fundamental two-dimensional braid representation and classifies simple low-dimensional representations over algebraically closed fields. This source date is not asserted to be the first-ever appearance of braid representations.

## Proof
**1. Braid equation and its local dichotomy.** Write \(X=I+N\) and \(Y=I+M\), with \(N=u\phi\), \(M=v\psi\), \(\phi(u)=\psi(v)=0\). These maps satisfy \(N^2=M^2=0\), and
\[
NMN=\phi(v)\psi(u)N,\qquad MNM=\psi(u)\phi(v)M.
\]
Set \(t=\phi(v)\psi(u)=\operatorname{tr}(NM)\). Expanding the two triple products gives
\[
XYX-YXY=(1+t)(N-M).
\]
If \(1+t\) is a unit then \(N=M\). Otherwise its residue is zero, so the residue of \(t\) equals \(-1\). The reductions of \(N,M\) cannot be identical, since identical square-zero reductions would give \(t\equiv\operatorname{tr}(N^2)=0\pmod{\mathfrak m}\). Thus \(N-M\) has a unit entry, and \((1+t)(N-M)=0\) forces \(1+t=0\). Conversely \(N=M\) or \(t=-1\) each implies the braid equation. They are disjoint, since \(\operatorname{tr}(N^2)=0\). This is a complete dichotomy over every commutative local ring.

**2. Nondiagonal normal form.** If \(t=-1\), both \(\phi(v)\) and \(\psi(u)\) are units. Choose \(e_1=u\), \(e_2=v/\phi(v)\); then
\[
N(e_1)=0,\quad N(e_2)=e_1,\quad M(e_1)=-e_2,\quad M(e_2)=0.
\]
The restrictions of \(\phi,\psi\) to \(W=Re_1\oplus Re_2\) form an invertible two-by-two pairing matrix. Consequently \(R^n=W\oplus(\ker\phi\cap\ker\psi)\), with the second summand free of rank \(n-2\) because \(R\) is local. Both maps vanish on that complement. The claimed nondiagonal representative follows. On \(W\), \(N,M\) generate the full two-by-two matrix algebra, so their common invertible centralizer is precisely
\[
R^\times\times\operatorname{GL}_{n-2}(R)
\]
acting as a scalar on \(W\) and arbitrarily on its complement.

**3. Diagonal normal form and centralizer.** Any primitive \(N=u\phi\) is conjugate to \(E_{12}\): extend the unimodular generator \(u\) to a basis of \(\ker\phi\), choose \(e_2\) with \(\phi(e_2)=1\), and re-order the basis. Relative to the decomposition \(Re_1\oplus Re_2\oplus R^{n-2}\), the commuting invertible matrices have form
\[
\begin{pmatrix}a&b&c\\0&a&0\\0&d&H\end{pmatrix},
\quad a\in R^\times,\quad b\in R,\quad
c\in R^{1\times(n-2)},\quad d\in R^{(n-2)\times1},\quad H\in\operatorname{GL}_{n-2}(R).
\]
Their number is \(|R^\times|T^{2n-3}|\operatorname{GL}_{n-2}(R)|\). The nondiagonal pair's stabilizer has size \(|R^\times||\operatorname{GL}_{n-2}(R)|\).

**4. Orbit-stabilizer and reduction.** Reduction gives \(\operatorname{GL}_n(R)\twoheadrightarrow\operatorname{GL}_n(\mathbb F_q)\), with kernel size \((T/q)^{n^2}\). Since \(|R^\times|=T(q-1)/q\) and
\[
\frac{|\operatorname{GL}_n(\mathbb F_q)|}{|\operatorname{GL}_{n-2}(\mathbb F_q)|}
=q^{2n-3}(q^n-1)(q^{n-1}-1),
\]
subtracting stabilizer cardinalities yields precisely \(P_n(R)\) diagonal and \(P_n(R)T^{2n-3}\) nondiagonal solutions. Reduction is onto each orbit. Dividing each orbit's size by the size of its residue-field orbit gives the two asserted constant lifting exponents. The asymptotic formulas follow directly from these exact counts.

## Verification
The independent enumeration script `transvection_braid_check.py` constructs primitive transvections as actual outer products, checks the braid relation by full matrix multiplication, and compares with the formula. It passed cases \(n=2\) over \(\mathbb F_2,\mathbb F_3,\mathbb F_5\) and dual-number rings in characteristics two and three, and \(n=3\) over \(\mathbb F_2\) and its dual numbers. To test ring-independence, three nonisomorphic rings of order eight with residue field \(\mathbb F_2\)—\(\mathbb Z/8\mathbb Z\), \(\mathbb F_2[t]/(t^3)\), and \(\mathbb F_2[x,y]/(x,y)^2\)—each gave 48 primitive transvections and 432 braid pairs in dimension two. The script and its exact output accompany this document. Finite computations supplement, but do not substitute for, the general proof.

## Relationship to prior work
Tuba and Wenzl (1999), especially Proposition 2.5, exhibit the two-dimensional irreducible unipotent braid representation in the field setting; its standard two-by-two matrices and the corresponding uniqueness are **not** claimed as new. Humphries, *Representations of Braid Groups via Determinantal Rings*, §2, already uses transvections over arbitrary commutative rings and their cross-pairing coordinates; the algebraic transvection framework is **not** claimed as new. Formanek (1996) provides earlier low-degree complex classification. The new statement is the explicit **two-orbit and orbit-size census over every finite commutative local ring and all ambient dimensions**, with the separate universal lifting degrees, including nonprincipal and mixed-characteristic rings. These ring-sensitive enumerative assertions do not appear in the inspected statements of those references; historical priority is not certified.

## Limitations
This theorem concerns primitive (split rank-one) transvections, not all matrices with square-zero perturbation nor all representations of the braid group. For higher dimension over nonreduced rings a square-zero matrix whose residue has rank one need not itself have split rank one, and it is deliberately excluded. The two-orbit claim is only for solutions inside this restricted locus. Neither exhaustive identification of all historical equivalents nor independent expert audit has been performed. The finite checker exhausts only the specified small models; the proof supplies the general quantifiers.

## References
1. I. Tuba and H. Wenzl, *Representations of the Braid group B3 and of SL(2,Z)*, arXiv:math/9912013, initial preprint 1999-12-02, Proposition 2.5. https://arxiv.org/pdf/math/9912013
2. S. P. Humphries, *Representations of Braid Groups via Determinantal Rings*, introduction and §2 (transvection coordinate formulas and Lemma 2.1). https://www.academia.edu/68130951/Representations_of_Braid_Groups_via_Determinantal_Rings
3. E. Formanek, *Braid Group Representations of Low Degree*, Proc. London Math. Soc. 73 (1996), 279–322. https://doi.org/10.1112/plms/s3-73.2.279
