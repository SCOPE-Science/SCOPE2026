# Homology-type distribution of square-zero differentials over finite dual numbers

## Finding

Let \(k=\mathbb F_q\), \(R=k[\varepsilon]/(\varepsilon^2)\), and \(n\ge1\). A differential is an \(R\)-linear map \(D\colon R^n\to R^n\) with \(D^2=0\). Its homology is \(H(D)=\ker D/\operatorname{im}D\), a finite \(R\)-module.

Define \(D=A+\varepsilon B\), with \(A,B\in M_n(k)\), and \(r=\operatorname{rank}A\). Set \(h=n-2r\), \(W=\ker A/\operatorname{im}A\), and let \(C\colon W\to W\) be induced by \(B\) (well-defined because \(AB+BA=0\)). Put \(s=\operatorname{rank}C\), \(c=\dim(\ker C\cap\operatorname{im}C)\). Then
\[
H(D)\cong R^{h-s-c}\oplus k^{2c},\qquad \operatorname{rank}_kD=2r+s.
\]
Every \(r,s,c\) satisfying \(0\le r\le\lfloor n/2\rfloor\), \(0\le s\le h\), and \(0\le c\le\min(s,h-s)\) occurs, and its exact labeled multiplicity is
\[
N_{n,q}(r,s,c)={n\brack r}_q{n-r\brack r}_q|\mathrm{GL}_r(q)|q^{2r(n-r)}
{h\brack h-s}_q{h-s\brack c}_q{s\brack s-c}_q q^{(h-s-c)(s-c)}|\mathrm{GL}_s(q)|.
\]
Here \({a\brack b}_q=\prod_{j=0}^{b-1}(q^{a-j}-1)/(q^{b-j}-1)\), \(|\mathrm{GL}_m(q)|=\prod_{i=0}^{m-1}(q^m-q^i)\), and empty products equal one. This gives the joint distribution of the reduction rank, underlying-field rank, and homology isomorphism type. The multiplicity of the residue-field summand in homology is always even.

## Assumptions and scope

The field is arbitrary for the structural homology assertion; finite cardinality \(q\) is needed only for counting. The coefficient ring is precisely \(R=k[\varepsilon]/(\varepsilon^2)\) and the underlying differential module is free of rank \(n\). The homology is a module, not merely a vector space. The condition \(D^2=0\) means composition square zero. No assumption about characteristic is imposed.

## Proof

First, \(D^2=0\) holds if and only if \(A^2=0\) and \(AB+BA=0\). Thus \(\operatorname{im}A\subseteq\ker A\), and for \(v\in\ker A\), \(ABv=-BAv=0\), while for \(w=Av\), \(Bw=-ABv\in\operatorname{im}A\). Consequently \(B\) induces \(C\) on \(W\).

A differential cancellation lemma holds over the local ring \(R\): if a differential matrix has a unit entry, elementary basis changes split off the contractible rank-two summand with differential \(\begin{psmallmatrix}0&1\0&0\end{psmallmatrix}\). Indeed the image of a primitive vector under the differential is primitive; choosing this pair as part of a basis, the identity \(D^2=0\) and row/column adjustments simultaneously clear all other entries in the two corresponding rows and columns. Iterating over the rank-\(r\) reduction gives a direct sum of \(r\) such summands and a free module of rank \(h\) with differential \(\varepsilon C'\). Reduction identifies \(C'\) with \(C\) up to change of basis on \(W\), so the homology is unchanged by replacing \(C'\) with \(C\).

For the residual differential \(\varepsilon C\) on \(R^h\), an element \(x+\varepsilon y\) is a cycle precisely if \(Cx=0\); boundaries are \(\varepsilon\operatorname{im}C\). As \(k\)-spaces the homology has a filtration with subquotients \(\ker C\) and \(k^h/\operatorname{im}C\), hence dimension \(2(h-s)\). Multiplication by \(\varepsilon\) on homology is the map \(\ker C\to k^h/\operatorname{im}C\), whose rank equals
\[
\dim\ker C-\dim(\ker C\cap\operatorname{im}C)=h-s-c.
\]
Every finite module over \(R\) splits as copies of \(R\) and \(k\), and \(\varepsilon\) has rank one on each free copy and zero on each residue-field copy. Thus the free multiplicity is \(u=h-s-c\), and the residue-field multiplicity is \(2(h-s)-2u=2c\). The contractible summands each contribute two to the underlying \(k\)-rank, while \(\varepsilon C\) contributes \(s\); hence \(\operatorname{rank}_kD=2r+s\).

Count choices of the reduction matrix \(A\) of square-zero rank \(r\): choose \(\operatorname{im}A\), choose \(\ker A\supset\operatorname{im}A\), and choose an isomorphism \(k^n/\ker A\to\operatorname{im}A\). This gives \({n\brack r}_q{n-r\brack r}_q|\mathrm{GL}_r(q)|\).

Fix \(A\) and decompose \(k^n=I\oplus W\oplus J\) of dimensions \((r,h,r)\), with \(A\) carrying \(J\) isomorphically onto \(I\). Writing the nine blocks of \(B\), the equation \(AB+BA=0\) sets three blocks to zero, determines the \(J,J\) block as the negative of the \(I,I\) block, and leaves the \(W,W\) block \(C\) arbitrary. The remaining four unconstrained blocks have total dimension \(2r(n-r)\), so every prescribed \(C\) has exactly \(q^{2r(n-r)}\) lifts.

Let \(K=\ker C\), of dimension \(a=h-s\), and \(I_C=\operatorname{im}C\), of dimension \(s\), with \(\dim(K\cap I_C)=c\). Choose \(K\) in \({h\brack a}_q\) ways; choose \(I_C\) meeting \(K\) in dimension \(c\) in
\[
{a\brack c}_q{h-a\brack s-c}_q q^{(a-c)(s-c)}
\]
ways (choose the intersection, then the quotient image, then the graph of a linear map). For fixed \((K,I_C)\), choose the induced isomorphism \(k^h/K\to I_C\) in \(|\mathrm{GL}_s(q)|\) ways. Since \(h-a=s\), this gives the claimed formula. Every allowed flag configuration and isomorphism exists, proving exactness and nonemptiness. No enumeration is substituted for these arguments.

As a distinguishing example at \(n=2\), let \(D_1=\varepsilon\operatorname{diag}(1,0)\) and \(D_2=\varepsilon\begin{psmallmatrix}0&1\0&0\end{psmallmatrix}\). Both are square-zero and have the same Smith invariant factors \((\varepsilon,0)\) and underlying-field rank one. But \(c=0\) for \(D_1\), giving \(H(D_1)\cong R\); for \(D_2\), \(c=1\), giving \(H(D_2)\cong k^2\). Therefore a homology-type census is not implied by the coarser Smith-rank census.

## Verification

The standalone script `verify_dual_homology.py` imports `verify_dual_differentials.py` from the same package and enumerates every \(A,B\in M_n(k)\) satisfying the original equations for the configurations \((n,q)=(1,2),(1,3),(2,2),(2,3),(2,4),(3,2)\). It constructs the full \(2n\times2n\) matrix of \(D\), computes \(\ker D\), \(\operatorname{im}D\), and the action of \(\varepsilon\) on the quotient, and compares each joint type with a separately evaluated Gaussian flag count. The \(q=4\) run uses genuine quadratic-extension-field arithmetic. It also tests the parity constraint and all coefficient formulas for \(n\le8\), \(q\in\{2,3,4,5\}\). The exact output is in `homology_verification.log`. All tests passed. These finite checks are corroboration, not an infinite proof.

## Relationship to prior work

Avramov, Buchweitz and Iyengar (first public arXiv version 2006-02-16) study differential modules and connect square-zero matrices to homology and contractibility; their Section 6 does not state the present joint finite-field homology-isomorphism distribution. Schröer (2002) classifies components for pairs of mutually annihilating nilpotent matrices with both matrices nilpotent; this differs from the unrestricted \(B\) satisfying \(AB+BA=0\). Moreau and Yu (2014) study jets of reduced nilpotent orbit closures over \(\mathbb C\), not the homology-module count over dual numbers. Earlier square-zero dual-number matrix censuses by reduction rank, Smith invariants and geometric components are strictly coarser: the explicit pair \(D_1,D_2\) above has equal such invariants but different homology. This is a statement-level nonimplication, not merely a title comparison.

## Limitations

This result covers dual numbers only, free underlying modules, and one differential, not all finite chain rings of higher nilpotency length or arbitrary commuting families. It classifies homology as an \(R\)-module and jointly counts reduction and field-linear ranks, but does not classify all matrices up to conjugacy. An unlocated general differential-module representation counting theorem could still imply the formula; historical priority has not been independently certified.

## References

- L. L. Avramov, R.-O. Buchweitz, and S. Iyengar, *Class and rank of differential modules*, arXiv:math/0602344 (first posted 2006-02-16), Section 6.
- J. Schröer, *Varieties of pairs of nilpotent matrices annihilating each other*, arXiv:math/0211293 (first posted 2002-11-19).
- A. Moreau and R. W. T. Yu, *Jet schemes of the closure of nilpotent orbits*, arXiv:1411.6427 (first posted 2014-11-24).
