# The component geometry and finite-field census of strongly quasi-nil-clean matrices

## Finding

Let \(n\ge 1\), let \(K\) be algebraically closed, and define \(\mathcal Q_n(K)\subseteq M_n(K)\) to consist of all matrices with a **strongly quasi-nil-clean decomposition** \(A=uE+N\), where \(u\in K^\times\), \(E^2=E\), \(N\) is nilpotent, and \(EN=NE\). The zero quasi-idempotent \(uE=0\) is permitted. For each \(1\le r\le n\), set

\[
\mathcal D_r(K)=\bigl\{A\in M_n(K):\det(tI-A)=t^{n-r}(t-u)^r\text{ for some }u\in K\bigr\}.
\]

**Geometric classification.** Each \(\mathcal D_r\) is a closed irreducible algebraic subvariety of dimension \(n^2-n+1\). The \(n\) sets \(\mathcal D_1,\ldots,\mathcal D_n\) are exactly the irreducible components of \(\mathcal Q_n(K)\). For distinct indices \(r,s\), their intersection is exactly the nilpotent cone \(\mathcal N_n(K)\), which has dimension \(n^2-n\):

\[
\mathcal Q_n(K)=\bigcup_{r=1}^{n}\mathcal D_r(K),\qquad
\mathcal D_r(K)\cap\mathcal D_s(K)=\mathcal N_n(K)\quad(r\ne s).
\]

In particular the components all have the same dimension and share precisely one common codimension-one nilpotent locus. The intersection assertion is vacuous at \(n=1\).

**Finite-field specialization (derived from classical fixed-characteristic-polynomial counts).** For a prime power \(q\ge2\), write \(Q_{n,q}\) for the number of strongly quasi-nil-clean elements of \(M_n(\mathbb F_q)\), and denote the Gaussian binomial coefficient by \({n\brack r}_q\). Then

\[
\boxed{Q_{n,q}=q^{n^2-n}\left[1+(q-1)\sum_{r=1}^{n}{n\brack r}_q\,q^{-r(n-r)}\right].}
\]

For every fixed \(q\ge2\), with \(c_q=\prod_{j=1}^{\infty}(1-q^{-j})>0\), the resulting probability obeys

\[
\boxed{\frac{Q_{n,q}}{q^{n^2}}=\frac{q-1}{c_q}\,nq^{-n}+O_q(q^{-n})\quad(n\to\infty).}
\]

This is a count of individual matrices possessing a commuting quasi-idempotent--nilpotent decomposition, **not** the assertion that the full matrix ring has this property for all its elements.

## Assumptions and scope

A quasi-idempotent in a unital ring is an element \(B\) with \(B^2=vB\) for some central unit \(v\). In \(M_n(F)\) over any field, central units are precisely nonzero scalar matrices, so \(B=uE\), \(u\ne0\), \(E^2=E\). A strongly quasi-nil-clean element is a sum of such a \(B\) and a commuting nilpotent \(N\). No commutativity of the ambient matrix ring is assumed. The geometry is over **arbitrary algebraically closed fields, in all characteristics**; the counting formula is over **all finite fields**, not just prime fields. For dimension zero no claim is made. For \(n\ge1\), zero and every nilpotent matrix belong to the locus by choosing \(E=0\).

## Proof

**1. Polynomial criterion and unique nonnilpotent label.** If \(A=uE+N\), \(EN=NE\), then \(F^n=\ker E\oplus\operatorname{im}E\) is stable under \(A\). On the respective summands \(A\) acts as nilpotent \(N\) and as \(uI+N\). Thus its characteristic polynomial has the form \(t^{n-r}(t-u)^r\), with \(r=\operatorname{rank}E\). Conversely, if \(u\ne0\) and the characteristic polynomial has that form, the primary decomposition for the coprime factors \(t^{n-r}\) and \((t-u)^r\) gives an \(A\)-stable direct sum of generalized \(0\)- and \(u\)-eigenspaces. Let \(E\) project to the latter along the former, and take \(N=A-uE\). This \(N\) is nilpotent and commutes with \(E\). A characteristic polynomial \(t^n\) means \(A\) is nilpotent, so \(E=0\) works. For nonnilpotent \(A\), the nonzero eigenvalue \(u\) and its algebraic multiplicity \(r\) are unique. An equivalent finite-field check is

\[
A\in\mathcal Q_n(\mathbb F_q)\quad\Longleftrightarrow\quad
A^n(A-uI)^n=0\text{ for some }u\in\mathbb F_q^\times.
\]

The converse of the displayed criterion follows from the annihilating polynomial having only the two coprime linear factors, and the same primary decomposition argument; the test also includes nilpotents.

**2. Closedness and irreducibility of each component.** Let \(\chi:M_n(K)\to K^n\) be the polynomial map taking a matrix to the non-leading coefficients of its characteristic polynomial. Fix \(r\ge1\). The morphism from the affine line sending \(u\) to the coefficients of \(t^{n-r}(t-u)^r\) has closed image \(C_r\): its coordinate subalgebra contains \((-u)^r\), so \(u\) is integral over that subalgebra, making the map finite onto its image. Therefore \(\mathcal D_r=\chi^{-1}(C_r)\) is closed.

For irreducibility, consider upper triangular matrices with the **prescribed** ordered diagonal consisting of \(n-r\) zeros and \(r\) copies of \(u\), with all above-diagonal entries free. Together with \(u\in K\) and \(g\in\operatorname{GL}_n(K)\), they form an irreducible parameter space. Conjugation \((g,T,u)\mapsto gTg^{-1}\) maps it *onto* \(\mathcal D_r\): each matrix is triangularizable over \(K\), and a composition flag can be chosen to realize any prescribed order of its eigenvalues, including repeats. An image of an irreducible space is irreducible in its subspace topology. Thus \(\mathcal D_r\) is irreducible.

**3. Dimensions.** For a fixed monic split characteristic polynomial of degree \(n\), the set of matrices realizing it has dimension \(n^2-n\). Indeed, assigning an invariant complete flag with the prescribed ordered diagonal uses a flag variety of dimension \(n(n-1)/2\), and the matrix entries above that diagonal contribute another \(n(n-1)/2\). Thus the fiber dimension is at most \(n^2-n\). For the reverse inequality, a companion matrix is cyclic, so its centralizer has dimension exactly \(n\) and its conjugacy orbit dimension is \(n^2-n\). The curve \(C_r\) is one-dimensional, and its nonzero-parameter fibers have this dimension; hence \(\dim\mathcal D_r=n^2-n+1\). The zero fiber is the nilpotent cone, so the same argument gives \(\dim\mathcal N_n=n^2-n\).

**4. Exactly \(n\) components; exact intersections.** The polynomial criterion gives \(\mathcal Q_n=\bigcup_{r=1}^n\mathcal D_r\). The parameter value \(u=0\) yields precisely all nilpotent matrices for every \(r\), so \(\mathcal N_n\) lies in all of them. If \(A\) is not nilpotent, its characteristic polynomial has one unique nonzero root and a unique multiplicity. Therefore it cannot belong to \(\mathcal D_r\cap\mathcal D_s\) for \(r\ne s\). Moreover each \(\mathcal D_r\) contains nonnilpotent matrices with nonzero eigenvalue of multiplicity \(r\), which are outside all other \(\mathcal D_s\). Thus no component is contained in another, and these are all the irreducible components.

**5. Exact finite-field count.** Fix \(u\in\mathbb F_q^\times\) and \(r\in\{1,\ldots,n\}\). A matrix with characteristic polynomial \(t^{n-r}(t-u)^r\) has a unique ordered decomposition into generalized eigenspaces of dimensions \(n-r\) and \(r\). There are \({n\brack r}_q\) choices for the \(r\)-space and exactly \(q^{r(n-r)}\) complementary \((n-r)\)-spaces. For each decomposition the restrictions are independently a nilpotent matrix and \(uI\) plus a nilpotent matrix. By the classical Fine--Herstein nilpotent-matrix enumeration, the number of nilpotent endomorphisms of an \(s\)-dimensional vector space is \(q^{s^2-s}\), including the convention that it equals \(1\) at \(s=0\). Hence this fixed \((r,u)\) stratum contains

\[
{n\brack r}_q q^{r(n-r)}q^{r^2-r}q^{(n-r)^2-(n-r)}
= q^{n^2-n}{n\brack r}_q q^{-r(n-r)}
\]

matrices. These strata are disjoint as \((r,u)\) varies with \(r\ge1\), and the remaining nilpotent matrices contribute \(q^{n^2-n}\) once. Summing proves the exact formula. Although the geometry was described over an algebraic closure, its \(\mathbb F_q\)-rational points have \(u\in\mathbb F_q\): Frobenius must fix the unique nonzero root. Thus no foreign-field eigenvalues are inadvertently counted.

**6. Large-dimension asymptotic.** Set \(c_m=\prod_{j=1}^{m}(1-q^{-j})\) and \(c_0=1\). Direct cancellation in the Gaussian coefficient gives

\[
{n\brack r}_q q^{-r(n-r)}=\frac{c_n}{c_r c_{n-r}}.
\]

As \(c_m=c_q(1+O_q(q^{-m}))\), the difference between this expression and \(1/c_q\) is \(O_q(q^{-r}+q^{-(n-r)})\), uniformly for \(0\le r\le n\). Summing this bound shows

\[
\sum_{r=1}^{n}{n\brack r}_q q^{-r(n-r)}=\frac{n}{c_q}+O_q(1).
\]

Substitution in the finite-field count yields \(Q_{n,q}=q^{n^2-n}((q-1)n/c_q+O_q(1))\), hence the probability formula. The result makes no assertion about simultaneous limits in which \(q\) varies with \(n\).

## Verification

The accompanying standalone `verify.py` uses exact integer arithmetic and direct matrix multiplication modulo **prime** fields. It enumerates all matrices for \((q,n)=(2,1),(2,2),(2,3),(2,4),(3,2),(3,3),(5,2)\), tests the annihilating-polynomial criterion for each matrix, and compares the raw counts against an independently evaluated Gaussian-binomial formula. The direct counts are respectively \(2,14,352,32512,51,6399,245\), all agreeing with the theorem. The output is recorded in `verification_output.txt`.

The proof covers all finite prime powers, while this small verification program only tests prime fields and small dimensions. Finite enumeration does not establish the general count or the geometric claims; those follow from the arguments above.

## Relationship to prior work

Das and Kar (2026, arXiv:2606.03526) introduced the quasi-nil-clean and strongly quasi-nil-clean decomposition notions and studied structural ring conditions, particularly commutative quotients. Their definition, rather than a new notion here, supplies the motivating invariant. The complete accessible arXiv HTML was inspected, including the definitions and substantive sections on strongly quasi-nil-clean rings, commutative quotients, amalgamated algebras, and group rings. No element-by-element matrix-locus component geometry is established there.

Abyzov, Chekhlov, Danchev and Tapkin (2026, arXiv:2606.13048), particularly Section 3 and Theorems 3.6--3.7, classify *ring-wide existence* of certain quasi-\(k\)-nil-clean decompositions, without the commuting requirement used here for individual elements. The accessible article text was examined around its definitions, matrix examples, and theorems. It does not give the component geometry, exact cardinalities, or fixed-field asymptotic of the strongly quasi-nil-clean element locus. For example, the unrestricted quasi-2-nil-clean property for \(M_n(\mathbb F_2)\) must not be confused with this strict subset: at \(n=3\), the present strongly decomposable locus has \(352\) of \(512\) matrices.

Fine--Herstein (1958) and Gerstenhaber (1961) supply the classical nilpotent-matrix count. Reiner (1961) and Gerstenhaber (1961) also count matrices with *any prescribed characteristic polynomial*, which **already implies the exact finite-field census above once the characteristic-polynomial characterization is known**. Therefore neither the fixed-polynomial count nor the resulting finite-field enumeration is asserted to be independently novel. Su, Liu, and Ou (2026) address nil-quasi-cleanness of entire matrix rings without requiring commuting summands, and Su and Liu (2026) classify noncommuting nil-quasi-clean companion matrices. Their accessible abstracts do not imply the irreducible-component structure of the stricter commuting-element locus; full-text inspection of these two papers was not available. Related records on strongly nil-clean matrices over dual numbers count a distinct, fixed-idempotent locus. The originality claim concerns the **complete algebraic-geometric decomposition into exactly \(n\) closed irreducible equidimensional components with their precisely shared nilpotent intersection**, applied to the newly defined commuting quasi-idempotent--nilpotent element locus; the finite-field formula and asymptotic are useful classical-method consequences, not separate historical novelty claims.

## Limitations

Originality is assessed against accessible records and literature, not established as historical priority by an independent bibliographic audit. The Das--Kar article was inspected in the available full HTML. Full text of two relevant Su--Liu matrix papers was not recovered, and a result under alternative terminology in older matrix-variety literature may still exist. Reiner’s general fixed-characteristic-polynomial census dominates the finite counting formula as a corollary; the novelty claim is therefore restricted to the algebraic-geometric component result. The finite-field asymptotic holds at fixed \(q\). Only commuting decompositions are counted; no statement is made about the larger locus of noncommuting quasi-nil-clean decompositions or about entire matrix rings having the property. The geometric component description concerns reduced algebraic sets, not an assertion about scheme-theoretic multiplicities or transverse intersections. No independent mathematical review or formal verification has been performed.

## References

1. S. Das and S. Kar, *On Quasi-Nil Clean Rings*, arXiv:2606.03526 (first submitted June 2, 2026), https://arxiv.org/abs/2606.03526.
2. A. N. Abyzov, A. R. Chekhlov, P. V. Danchev and D. T. Tapkin, *Rings with Clean-Like Properties: Endomorphism, Matrix and Structural Theorems*, arXiv:2606.13048 (June 11, 2026), https://arxiv.org/abs/2606.13048.
3. N. J. Fine and I. N. Herstein, *The probability that a matrix be nilpotent*, Illinois J. Math. 2 (1958), 499--504.
4. M. Gerstenhaber, *On the number of nilpotent matrices with coefficients in a finite field*, Illinois J. Math. 5 (1961), 330--333, https://doi.org/10.1215/ijm/1255629831.
5. I. Reiner, *On the number of matrices with given characteristic polynomial*, Illinois J. Math. 5 (1961), 324--329, https://projecteuclid.org/euclid.ijm/1255629830.
6. H. Su, S. Liu, and Y. Ou, *Nil-quasi-clean matrix rings*, J. Algebra Appl., 2026, article 2750155, DOI:10.1142/S0219498827501556.
7. H. Su and S. Liu, *Nil-quasi-clean companion matrices*, Algebra Discrete Math. 41 (2026), 270--280, DOI:10.12958/adm2466.
