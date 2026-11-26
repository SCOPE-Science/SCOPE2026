# Prescribed Jordan-product fibers in the four-by-four niltriangular algebra

## Finding
Let \(k\) be an arbitrary field, and let \(N=\mathfrak n_4(k)\) be the six-dimensional associative algebra of strictly upper-triangular \(4\times4\) matrices. Consider the Jordan-product map \(\Phi:N\times N\to N\), \(\Phi(X,Y)=XY+YX\). Its image lies in the three-dimensional ideal \(W=\langle E_{13},E_{24},E_{14}\rangle\). All points \(T=uE_{13}+vE_{24}+wE_{14}\in W\) occur. Write \(F_T\) for the **reduced** fiber of \(\Phi\) above \(T\), and \(\mathbb L=[\mathbb A^1_k]\) in the Grothendieck ring of reduced finite-type \(k\)-varieties. Then

\[
[F_T]=\begin{cases}
\mathbb L^7(\mathbb L^2-1),&(u,v)\ne(0,0),\\
2\mathbb L^7(\mathbb L^2-1),&u=v=0,\ w\ne0,\\
\mathbb L^7(2\mathbb L^2+\mathbb L-2),&u=v=w=0.
\end{cases}
\]

For \((u,v)\ne(0,0)\), \(F_T\) is geometrically irreducible of dimension \(9\). For \(u=v=0\), it has **exactly two** geometrically irreducible components, both of dimension \(9\). In particular, for every finite field \(k=\mathbb F_q\), replacing \(\mathbb L\) by \(q\) in the displayed expressions yields the exact number of ordered solutions to \(XY+YX=T\). The results hold in every characteristic, including characteristic two, when this product equals the commutator.

## Assumptions and scope
Every assertion holds for each field \(k\) and each triple \((u,v,w)\in k^3\). The matrices \(X,Y\) are **labeled and ordered**; the fibers are not quotiented by conjugation or automorphisms. We use the matrix units \(E_{ij}\) and coordinates

\[
X=aE_{12}+bE_{13}+cE_{14}+dE_{23}+eE_{24}+fE_{34},\quad
Y=AE_{12}+BE_{13}+CE_{14}+DE_{23}+EE_{24}+FE_{34}.
\]

Capital \(E\) is a coordinate of \(Y\), distinct from the matrix units \(E_{ij}\). The assertions about irreducible components are geometric, i.e. persist after extending \(k\) to an algebraic closure. We make no assertion that the unreduced scheme-theoretic fiber is reduced.

## Proof
Direct multiplication gives the three defining equations

\[
u=aD+dA,\qquad v=dF+Df,\qquad w=aE+bF+Ae+Bf.
\]

The coefficients \(c,C\) are free. Fixing \(X\), the linear map \(Y\mapsto XY+YX\) has matrix, for the ordered variables \((A,B,C,D,E,F)\),

\[
\begin{pmatrix}
d&0&0&a&0&0\\
0&0&0&f&0&d\\
e&f&0&0&a&b
\end{pmatrix}.
\]

The following exhaustive stratification is by the coordinates \((a,d,f,b,e)\) of \(X\); the sixth coordinate \(c\) is always free. If a target belongs to the image of this linear map, the \(Y\)-fiber is an affine space of dimension \(6-r\), where \(r\) denotes its rank.

| Stratum | Rank | Image condition on \((u,v,w)\) | Contribution to \([F_T]\) |
|---|---:|---|---|
| \(d\ne0,\ (a,f)\ne(0,0)\) | 3 | arbitrary target | \((\mathbb L-1)(\mathbb L^2-1)\mathbb L^6\) |
| \(d\ne0,\ a=f=0\) | 2 | \(dw=eu+bv\) | see below |
| \(d=0,\ (a,f)\ne(0,0)\) | 2 | \(fu=av\) | see below |
| \(d=a=f=0,\ (b,e)\ne(0,0)\) | 1 | \(u=v=0\) | \((\mathbb L^2-1)\mathbb L^6\) |
| \(d=a=f=b=e=0\) | 0 | \(T=0\) | \(\mathbb L^7\) |

For the second stratum, at \(T=0\) the contribution is \((\mathbb L-1)\mathbb L^7\); it is zero for a nonzero central target; and for \((u,v)\ne(0,0)\) it is \((\mathbb L-1)\mathbb L^6\), because the nonzero linear equation \(eu+bv=dw\) selects an affine line in the \((b,e)\)-plane. For the third stratum the contribution is \((\mathbb L^2-1)\mathbb L^7\) if \(u=v=0\), and \((\mathbb L-1)\mathbb L^7\) if \((u,v)\ne(0,0)\), since \((a,f)\) must be a nonzero scalar multiple of \((u,v)\). These strata are disjoint, and all their parameterizations are products of affine spaces and tori or affine-line bundles, so the indicated classes are identities in the Grothendieck ring, not merely numerical interpolation.

Adding the five contributions yields the three displayed fiber classes. Surjectivity is explicit: choosing \(X=E_{12}+E_{23}\) and \(Y=uE_{12}+vE_{34}+wE_{24}\) gives \(XY+YX=T\).

For the component classification, consider the open locus \(U\subset F_T\) where \(d\ne0\) or \(D\ne0\). On the subopen \(d\ne0\), eliminate \(A=(u-aD)/d\) and \(F=(v-fD)/d\), and replace \(B,E\) by the invertible affine coordinates \(\widetilde B=B-Db/d\), \(\widetilde E=E-De/d\). The remaining equation is

\[
a\widetilde E+f\widetilde B+(bv+eu)/d=w.
\]

If \((u,v)\ne(0,0)\), solve for one of \(b,e\); the patch is geometrically irreducible of dimension \(9\). If \(u=v=0\), the hypersurface equation \(a\widetilde E+f\widetilde B=dw\) is also geometrically irreducible of dimension \(9\): as a degree-one polynomial in \(\widetilde E\) over the polynomial ring in the remaining coordinates, its coefficient \(a\) is relatively prime to \(f\widetilde B-dw\), even when \(w=0\); Gauss's lemma applies. The same holds on \(D\ne0\) after swapping \(X\) and \(Y\). The two patches intersect for every target (choose \(d=D=a=1\), \(f=b=e=B=0\), then choose \(A,F,E\) to realize the three target coordinates), so \(U\) is geometrically irreducible and its closure has dimension \(9\).

The complementary closed locus \(Z=F_T\cap\{d=D=0\}\) is empty for \((u,v)\ne(0,0)\). For \(u=v=0\) it is given in affine \(10\)-space by the single equation

\[
aE+bF+Ae+Bf=w.
\]

This polynomial is geometrically irreducible: it is primitive of degree one in \(E\), since \(a\) is relatively prime to \(bF+Ae+Bf-w\). Thus \(Z\) is irreducible of dimension \(9\). It cannot be contained in the closure of \(U\), since two irreducible closed subsets of the same dimension would then coincide, although the closure of \(U\) contains points with \(d\ne0\). As \(F_T=U\cup Z\), its two maximal irreducible closed subsets are precisely \(\overline U\) and \(Z\). For noncentral targets \(F_T=U\) is irreducible. All reasoning remains valid after an arbitrary extension of the field.

## Verification
A standalone C11 program `verify.c` enumerates the coefficient-linear-system rank and consistency for every prescribed target over \(\mathbb F_2\), \(\mathbb F_3\), \(\mathbb F_4\), \(\mathbb F_5\), and \(\mathbb F_7\), using an explicit degree-two polynomial-field multiplication table for \(\mathbb F_4\). It additionally exhausts all ordered input pairs directly over the first three fields. Compile with `cc -O2 -std=c11 -Wall -Wextra verify.c -o verify` and run `./verify`. All five fields pass; the program reports `VERIFY_OK_NILTRIANGULAR_JORDAN_FIBERS`. The direct tests contain \(4{,}096\), \(531{,}441\), and \(16{,}777{,}216\) ordered pairs, respectively. These checks are independent corroboration of the symbolic proof, not a replacement for it.

## Relationship to prior work
Commutation in unitriangular groups is a well-developed subject. Soffer (arXiv:1411.5389) establishes bounds on their number of conjugacy classes; Kumar and Prajapati (arXiv:1601.04133) investigate maximal noncommuting sets in particular upper-unitriangular groups; Kaur, Sharma, and Singh (arXiv:2006.01493) give branching rules and commuting-probability calculations for triangular and unitriangular matrices. Those results motivate a finer fixed-output question, but the inspected texts concern commuting equations, conjugacy or centralizers, rather than the complete reduced fibers of the **Jordan-product map** on the associative niltriangular algebra in all characteristics. In characteristic two this map is the Lie commutator, so the zero target overlaps the standard commuting problem; no priority is claimed for older commuting counts or generic linear-algebra techniques. The additional prescribed noncentral outputs, Grothendieck classes and geometric component transition form the present combined statement. An equivalent formulation as a word-map distribution or bilinear incidence problem might exist elsewhere, so literature completeness is not asserted.

## Limitations
The target belongs to \(W\); outside \(W\) the fiber is empty. The geometric classification concerns **reduced** fibers only, and does not determine their scheme-theoretic nilpotents, singularities or all intersection multiplicities. The theorem does not cover larger matrix sizes or simultaneous conjugacy classes. The independent finite checks are not infinite proofs. The cited literature search does not certify absolute historical priority; equivalent statements in less obvious presentations could have been overlooked.

## References
- Andrew Soffer, *Upper bounds on the number of conjugacy classes in unitriangular groups*, arXiv:1411.5389, first publicly posted 2014-11-19, https://arxiv.org/abs/1411.5389.
- C. P. Anil Kumar and S. K. Prajapati, *Maximal Non-commuting Sets in Certain Unipotent Upper-triangular Linear Groups*, arXiv:1601.04133, first publicly posted 2016-01-16, https://arxiv.org/abs/1601.04133.
- Dilpreet Kaur, Uday Bhaskar Sharma and Anupam Singh, *Branching rules and commuting probabilities for Triangular and Unitriangular matrices*, arXiv:2006.01493, first publicly posted 2020-06-02, https://arxiv.org/abs/2006.01493.
