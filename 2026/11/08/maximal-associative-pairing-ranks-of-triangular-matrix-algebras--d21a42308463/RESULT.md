# Maximal associative-pairing ranks of triangular matrix algebras: an odd-even counting dichotomy

## Finding

Let \(k=\mathbb F_q\) be any finite field and let \(n\ge 3\). Write \(T_n(k)\) for the upper-triangular matrix algebra, with \(d=n(n+1)/2\). Every associative bilinear form on this algebra has the shape
\[
  \beta_\lambda(X,Y)=\lambda(XY),\qquad \lambda\in T_n(k)^*.
\]
Set \(R_n=\max_\lambda\operatorname{rank}\beta_\lambda\) and \(M_n(q)=\#\{\lambda:\operatorname{rank}\beta_\lambda=R_n\}\). Then
\[
 R_n=\left\lfloor\frac{(n+1)^2}{4}\right\rfloor,\qquad d-R_n=\left\lfloor\frac{n^2}{4}\right\rfloor.
\]
Put \(P_m(q)=\prod_{i=1}^m(1-q^{-i})\). The exact numbers of optimal-rank forms are
\[
 \boxed{\begin{aligned}
 M_{2m-1}(q)&=q^{m(2m-1)}P_m(q) &&(m\ge2),\\
 M_{2m}(q)&=q^{m(2m+1)}P_m(q)(1+q^{-1}-q^{-m-1}) &&(m\ge2).
 \end{aligned}}
\]
In particular, the proportions \(M_n(q)/q^d\) approach two *different* positive limits as \(n\to\infty\) through odd or even integers: respectively \(P_\infty(q)=\prod_{i\ge1}(1-q^{-i})\) and \((1+q^{-1})P_\infty(q)\).

For an arbitrary field \(k\), consider the affine space of linear functionals on \(T_n(k)\). The nonmaximal-rank locus has codimension exactly one for odd \(n\), but exactly two for even \(n\). In the odd case it is an irreducible determinant hypersurface. In the even case it is the union of two distinct codimension-two maximal-minor determinantal loci.

## Assumptions and scope

The algebra has the usual unital matrix multiplication, and \(\beta\) is associative in the sense \(\beta(XY,Z)=\beta(X,YZ)\), with no symmetry assumption. The rank of a bilinear form is the rank of its Gram matrix, equivalently its induced map into the dual space. The stated integer counts use \(q\) a prime power; the maximum rank and codimension assertions hold over arbitrary fields (codimension means that of the corresponding algebraic sets after scalar extension to an algebraic closure). All matrix and form counts are labeled, not isomorphism-orbit counts. Characteristic two is included. The theorem deliberately starts at \(n=3\), since the radical-square-zero two-vertex case is elementary and previously subsumed by broader work.

## Proof

**Every associative form comes from one functional.** If \(1\) is the identity and \(\beta(XY,Z)=\beta(X,YZ)\), define \(\lambda(T)=\beta(1,T)\). Then \(\beta(X,Y)=\beta(1,XY)=\lambda(XY)\). Conversely every such \(\lambda\) is associative, and \(\lambda\mapsto\beta_\lambda\) is injective because \(\beta_\lambda(1,T)=\lambda(T)\). Thus the space of forms has \(q^d\) elements.

**Exact block-rank identity.** In the standard basis \(E_{ij}\) (\(1\le i\le j\le n\)), write \(a_{i\ell}=\lambda(E_{i\ell})\) and \(A=(a_{i\ell})_{1\le i\le\ell\le n}\). Since
\[
 \beta_\lambda(E_{ij},E_{k\ell})=\delta_{jk}a_{i\ell},
\]
permuting rows by right endpoint \(j\) and columns by left endpoint \(k\) makes the Gram matrix block diagonal, with the rectangular block
\[
 H_j=(a_{i\ell})_{1\le i\le j,\ j\le\ell\le n},\quad\text{of size }j\times(n-j+1).
\]
Consequently
\[
 \operatorname{rank}\beta_\lambda=\sum_{j=1}^n\operatorname{rank}H_j
 \le\sum_{j=1}^n\min(j,n-j+1)=\left\lfloor\frac{(n+1)^2}{4}\right\rfloor.
\]
The bound is attained by choosing nonzero entries on the upper-half antidiagonal \(a_{i,n+1-i}\), and zeros elsewhere: the central rectangular blocks have full rank, forcing all the others to have full rank as explained below. This also proves the maximum-rank formula over any field.

**Odd size.** If \(n=2m-1\), the middle block \(H_m\) is an arbitrary \(m\times m\) matrix. It is invertible exactly when all \(H_j\) have full possible rank. Indeed, if it is invertible, for \(j<m\), \(H_j\) contains the first \(j\) independent rows of \(H_m\), and for \(j>m\), \(H_j\) contains the last \(n-j+1\) independent columns of \(H_m\); conversely maximal total rank forces \(H_m\) invertible. Exactly \(m^2\) coefficients occur in \(H_m\), with \(m(2m-1)-m^2=m(m-1)\) other coefficients free. Thus
\[
 M_{2m-1}(q)=q^{m(m-1)}|\mathrm{GL}_m(q)|
 =q^{m(2m-1)}P_m(q).
\]
The nonoptimal set is \(\det H_m=0\), an irreducible codimension-one determinantal hypersurface.

**Even size.** If \(n=2m\), maximal total rank is equivalent to simultaneous full row rank of \(H_m\), of size \(m\times(m+1)\), and full column rank of \(H_{m+1}\), of size \((m+1)\times m\). The implication to all other blocks follows by restricting to their first rows or last columns, as in the odd case. Let \(C\) be their common \(m\times m\) submatrix, \(x\) the extra column of \(H_m\), and \(y\) the extra row of \(H_{m+1}\). These \(m^2+2m\) coefficients are independent; the remaining \(m(m-1)\) coefficients are free.

If \(\operatorname{rank}C=m\), every \(x,y\) works. If \(\operatorname{rank}C=m-1\), the condition is \(x\notin\operatorname{im}C\) and \(y\notin\operatorname{row}C\); hence there are \((q^m-q^{m-1})^2\) choices. For smaller rank no choice works. The number of rank-\((m-1)\) square matrices is
\[
 N_{m-1}(q)={m\brack m-1}_q^2|\mathrm{GL}_{m-1}(q)|.
\]
Therefore
\[
 M_{2m}(q)=q^{m(m-1)}\bigl[q^{2m}|\mathrm{GL}_m(q)|+N_{m-1}(q)(q^m-q^{m-1})^2\bigr].
\]
Using \(|\mathrm{GL}_m(q)|=q^{m-1}(q^m-1)|\mathrm{GL}_{m-1}(q)|\) reduces this expression to the displayed factor \(q^{m(2m+1)}P_m(q)(1+q^{-1}-q^{-m-1})\).

The nonoptimal set in even size is the union of the two loci \(\operatorname{rank}H_m<m\) and \(\operatorname{rank}H_{m+1}<m\). Each is a maximal-minor variety for a completely free \(m\times(m+1)\) or \((m+1)\times m\) matrix, hence irreducible of codimension two. These loci are distinct: taking \(C\) of rank \(m-1\), one can choose \(x\) outside its column space and \(y\) inside its row space, or conversely.

**Limits.** The infinite product \(P_\infty(q)\) converges to a positive number since \(\sum_{i\ge1}q^{-i}<\infty\). The even correction tends to \(1+q^{-1}\), proving the parity-separated limiting proportions. No other cases are left open in the stated scope.

## Verification

The two accompanying independent checker sources use (i) literal Gram matrices defined by multiplication of matrix units, and (ii) direct block ranks. The first exhausts all coefficients over prime fields in ten cases up through \(n=5\), including \((n,q)=(5,2)\), and compares the observed optimal counts with the exact formula. The second exhausts \((n,q)=(2,4)\) and \((3,4)\) over \(\mathbb F_4\) and checks 5,000 independently seeded dimension-four extension-field samples. Representative optimal counts: \(M_3(2)=24\), \(M_3(4)=2880\), \(M_4(2)=528\), \(M_4(3)=45360\), and \(M_5(2)=10752\). Run instructions appear in `VERIFICATION.md`. These computations check finite examples; the all-field proof is the preceding argument.

## Relationship to prior work

Dăscălescu, Iovanov, and Preduţ classify exactly when a structural matrix algebra is Frobenius. In particular, nontrivial upper-triangular matrix algebras admit no nondegenerate associative form. Their theorem is an existence/nonexistence classification and does not give the *maximum attainable degenerate rank*, the number of optimizing functionals over finite fields, or the parity-changing codimension of failure. Dăscălescu, Năstăsescu, and Velicu classify balanced forms on the **dual incidence coalgebra** and co-Frobenius conditions; that is a distinct direction of the bilinear pairing and does not itself give the present counting and codimension claims. The standard finite-field rank-matrix formula is used explicitly in the proof and is not presented as a new lemma. No universal claim of historical priority is made.

## Limitations

This is not a complete generating polynomial for *all* ranks of associative forms. It treats the full upper-triangular algebra, not arbitrary structural matrix algebras or non-field coefficient rings. The codimension statement concerns the algebraic loci over a field, not a direct count of every lower-rank stratum. The result has not undergone independent audit. An unidentified broader orbit/determinantal-enumeration theorem could subsume it; an absence of a search match is not proof of novelty.

## References

1. S. Dăscălescu, M. C. Iovanov, S. Preduţ, “Frobenius Structural Matrix Algebras,” *Linear Algebra and its Applications* 439 (2013), 3166–3172; DOI 10.1016/j.laa.2013.09.007; public full text arXiv:1512.09339v1 (2015-12-31), https://arxiv.org/html/1512.09339v1 .
2. S. Dăscălescu, C. Năstăsescu, G. Velicu, “Balanced bilinear forms and finiteness properties for incidence coalgebras over a field,” *Revista de la Unión Matemática Argentina* 51 (2010), 19–26, https://inmabb.criba.edu.ar/revuma/pdf/v51n1/v51n1a03.pdf .
