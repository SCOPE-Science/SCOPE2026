# Commuting involution strata in four-by-four unitriangular algebra groups

## Finding

Let \(k=\mathbb F_q\), where \(q\) is any power of two, let \(J\) be the strictly upper-triangular radical of the associative algebra \(T_4(k)\), and let \(G=1+J=\mathrm{UT}_4(k)\). Write
\[
\mathcal I=\{g\in G:g^2=1\},\qquad C_{\mathcal I}(g)=\{h\in\mathcal I:gh=hg\}.
\]
The identity is included in \(\mathcal I\). The precise distribution of the restricted centralizer size \(|C_{\mathcal I}(g)|\) is as follows:

| Number of elements \(g\) | Restricted centralizer size \(|C_{\mathcal I}(g)|\) |
| ---: | ---: |
| \(q^3(q-1)\) | \(q^4\) |
| \(q\) | \(2q^4-q^2\) |
| \(q(q^2-1)\) | \(q^4+q^3-q^2\) |
| \(q^2(q^2-1)\) | \(2q^3-q^2\) |

These four rows describe disjoint structural strata, even when numerical sizes happen to coincide for a particular field. Their populations sum to \(|\mathcal I|=2q^4-q^2\). In particular, the number of ordered commuting pairs of elements with square one is exactly
\[
\boxed{\#\{(g,h)\in\mathcal I^2:gh=hg\}=q^8+2q^7-2q^5.}
\]
Thus the conditional commuting probability is
\[
\boxed{\frac{q(q^3+2q^2-2)}{(2q^2-1)^2}\longrightarrow\frac14\quad(q\longrightarrow\infty\text{ through powers of two}).}
\]
If the word *involution* is reserved for elements of order exactly two, the corresponding number of ordered commuting pairs is
\[
\boxed{q^8+2q^7-2q^5-4q^4+2q^2+1,}
\]
and the number of eligible elements is \(2q^4-q^2-1\). For \(q=2\), these become \(448\) commuting pairs among \(28\) elements of order dividing two, or \(393\) pairs among \(27\) nonidentity involutions.

## Assumptions and scope

The field has characteristic two, with no restriction that it be a prime field. Matrices are labeled in the fixed standard upper-triangular basis; no passage to conjugacy classes is made. The restricted centralizer \(C_{\mathcal I}(g)\) is a subset of the involution locus, not necessarily a subgroup and not the whole group centralizer.

Write any \(N\in J\) uniquely by its superdiagonal coordinates
\[
N= aE_{12}+bE_{23}+cE_{34}+dE_{13}+eE_{24}+fE_{14}.
\]
Because \(\operatorname{char}k=2\), the relation \((1+N)^2=1\) is equivalent to \(N^2=0\). The latter is exactly
\[
 ab=0,\qquad bc=0,\qquad ae+dc=0.
\]
All statements below concern this precise algebraic locus.

## Proof

**Step 1: Count the involution locus.** If \(b\ne0\), the first two equations force \(a=c=0\); the variables \(d,e,f\) are free. This gives \((q-1)q^3\) points. If \(b=0\) and \((a,c)=(0,0)\), the variables \(d,e,f\) are free, giving \(q^3\) points. Finally, if \(b=0\) and \((a,c)\ne(0,0)\), the equation \(ae+dc=0\) forces \((d,e)=t(a,c)\) for a unique \(t\in k\), and \(f\) is free, giving \((q^2-1)q^2\) points. Their total is \(2q^4-q^2\).

**Step 2: Determine commuting constraints.** For \(M=A E_{12}+B E_{23}+C E_{34}+D E_{13}+E E_{24}+F E_{14}\), the equations \(M^2=0\) are
\[
 AB=0,\quad BC=0,\quad AE+DC=0.
\]
Since \([1+N,1+M]=0\) as group elements if and only if \(NM=MN\), the additional equations are
\[
 aB+Ab=0,\qquad bC+Bc=0,\qquad aE+dC+Ae+Dc=0.
\]
The last coordinates \(f,F\) never enter these equations.

**Step 3: Four disjoint restricted-centralizer strata.** When \(b\ne0\), commuting forces \(A=C=0\). Then all \(B,D,E,F\) are free, so \(|C_{\mathcal I}(1+N)|=q^4\). There are \((q-1)q^3\) such \(N\).

When \(a=b=c=d=e=0\), the matrix is \(fE_{14}\), which commutes with every element of \(G\). There are \(q\) such matrices and the restricted centralizer has size \(2q^4-q^2\).

When \(a=b=c=0\) but \((d,e)\ne(0,0)\), consider the two cases \(B\ne0\) and \(B=0\). For \(B\ne0\), the square-zero equations force \(A=C=0\), while \(D,E\) are free, yielding \((q-1)q^2\) choices before the free coordinate \(F\). For \(B=0\), the conditions are \(AE+DC=0\) and \(eA+dC=0\). The latter confines \((A,C)\) to a one-dimensional subspace. At \((A,C)=(0,0)\) there are \(q^2\) choices for \((D,E)\); at each of its \(q-1\) nonzero vectors there are \(q\) choices. Hence there are \(2q^2-q\) choices. Multiplication by the \(q\) choices of \(F\) gives \(q^4+q^3-q^2\) restricted-commuting involutions. There are \(q(q^2-1)\) such matrices \(N\).

In the remaining stratum, \(b=0\), \((a,c)\ne(0,0)\), and \((d,e)=t(a,c)\). Commutation forces \(B=0\). Make the invertible change \(D'=D+tA\), \(E'=E+tC\). In characteristic two the remaining constraints become
\[
 AE'+CD'=0,\qquad aE'+cD'=0.
\]
When \((A,C)\) belongs to the one-dimensional span of \((a,c)\), the constraints are dependent and permit \(q\) choices for \((D',E')\); there are \(q\) vectors in that span. For the remaining \(q^2-q\) vectors \((A,C)\), the two constraints are independent and permit exactly one choice for \((D',E')\). Thus there are \(2q^2-q\) choices before freely selecting \(F\), giving \(2q^3-q^2\) commuting involutions per \(N\). The stratum has \(q^2(q^2-1)\) elements.

**Step 4: Sum and normalize.** Multiply the four centralizer sizes by their respective population counts. This gives
\[
\begin{aligned}
& (q-1)q^3\cdot q^4+q(2q^4-q^2)\\
&\quad+q(q^2-1)(q^4+q^3-q^2)\\
&\quad+q^2(q^2-1)(2q^3-q^2)
=q^8+2q^7-2q^5.
\end{aligned}
\]
Division by \((2q^4-q^2)^2=q^4(2q^2-1)^2\) yields the stated probability and limit. Deleting the identity in both coordinates subtracts \(2|\mathcal I|-1\) ordered pairs, giving the exact-order-two formula.

A structural explanation of the nonzero limiting probability is visible in the square-zero locus: it is the union of the two four-dimensional closed sets \(\{a=c=0\}\) and \(\{b=0,\ ae+dc=0\}\). The first has asymptotic density \(1/2\) inside the involution locus and any two elements in it commute. Generic pairs involving the second component do not commute, so the limit is \((1/2)^2=1/4\). The exact stratification above establishes this rigorously, independently of any geometric irreducibility claim.

## Verification

The standalone script `check.py` constructs \(4\)-by-\(4\) nilpotent matrices directly and tests the equations \(N^2=0\) and \(NM=MN\) by arithmetic in \(\mathbb F_2\) and \(\mathbb F_4\). It does not use the four-stratum counting proof. It exhaustively enumerates respectively \(28^2=784\) and \(496^2=246016\) ordered candidate pairs, obtaining \(448\) and \(96256\) commuting pairs. It also checks the total involution-locus sizes against \(2q^4-q^2\). The recorded run is in `check.out`; run with `python check.py` (Python standard library only). Finite checks are corroborative, not a proof for all \(q\).

## Relationship to prior work

Ekhad and Zeilberger's 1995 preprint determines the cardinality of the single square-zero upper-triangular matrix locus for arbitrary matrix size; it does not count *pairs of commuting members of that locus*. For size four, the single-element count here is a specialization of their theorem and is not claimed original. Their full two-page preprint was inspected.

Melnikov (2000) enumerates Borel-conjugacy orbits on the square-zero locus and their individual orbit sizes; this does not by itself give counts of commuting *pairs* of square-zero elements. Britnell and Wildon (2011) investigate when matrix similarity classes have commuting representatives. Their class-theoretic problem does not impose a fixed upper-triangular flag on *both* matrices and does not state these involution-restricted centralizer populations. Basili's 2016 work investigates geometry and complete-intersection behavior of commuting varieties of upper-triangular matrices; available abstract material does not establish an exact point count for this square-zero intersection. The 2005 work of Isaacs and Karagueuzian studies involutions and characters of upper-triangular matrix groups; its full text was not accessible, so priority relative to any additional counting formula there remains a specific risk.

The new contribution claimed here is only the complete restricted-centralizer distribution and the resulting exact pair count and limiting probability for \(\mathrm{UT}_4\) in characteristic two. No claim is made of a first count of single involutions, of an all-rank formula, or of priority certification.

## Limitations

The result concerns the fourth-order unitriangular algebra group over finite fields of characteristic two. It does not classify arbitrary upper-triangular groups, multiple commuting tuples, ordinary (unrestricted) group centralizers, or fields of odd characteristic. The priority comparison to the inaccessible full text of Isaacs–Karagueuzian and Basili is a remaining limitation; no independent audit has been performed.

## References

1. Shalosh B. Ekhad and Doron Zeilberger, *An Explicit Formula for the Number of Solutions of \(X^2=0\) in Triangular Matrices Over a Finite Field*, arXiv:math/9512224v1, first public 19 December 1995; *Electronic Journal of Combinatorics* 3 (1996), R2.
2. I. M. Isaacs and D. B. Karagueuzian, *Involutions and characters of upper triangular matrix groups*, *Mathematics of Computation* 74 (2005), 2027–2033, DOI:10.1090/S0025-5718-05-01705-9.
3. Anna Melnikov, *B-Orbits in solutions to the equation \(X^2=0\) in triangular matrices*, *Journal of Algebra* 223 (2000), 101–108, DOI:10.1006/jabr.1999.8056.
4. John R. Britnell and Mark Wildon, *On types and classes of commuting matrices over finite fields*, *Journal of the London Mathematical Society* 83 (2011), 470–492, DOI:10.1112/jlms/jdq088.
5. Roberta Basili, *On commuting varieties of upper triangular matrices*, *Communications in Algebra* 45 (2017), 1533–1541, first available 7 October 2016, DOI:10.1080/00927872.2016.1178272.
