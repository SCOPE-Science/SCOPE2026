# Seven exact Jordan strata for a three-axis squarefree complete intersection over odd finite fields

## Finding

Let \(q\) be any odd prime power, let \(k=\mathbb F_q\), and set
\[
A=k[x,y,z]/(x^2,y^2,z^2),\qquad \mathfrak m=(x,y,z)\subset A.
\]
For every \(f\in\mathfrak m\), let \(\lambda(f)\) be the partition of \(8\) specifying the nilpotent Jordan blocks of the \(k\)-linear map \(M_f:A\to A\), \(a\mapsto fa\). The complete multiplicity distribution \(N_\lambda(q)=\#\{f\in\mathfrak m:\lambda(f)=\lambda\}\) is:

| Jordan partition \(\lambda\) | Multiplicity \(N_\lambda(q)\) | Characteristic |
|---|---:|---|
| \((1,1,1,1,1,1,1,1)\) | \(1\) | all odd |
| \((2,1,1,1,1,1,1)\) | \(q-1\) | all odd |
| \((2,2,1,1,1,1)\) | \(q(q^3-1)\) | all odd |
| \((2,2,2,2)\) | \(3(q-1)q^3\) | all odd |
| \((3,2,2,1)\) | \(3(q-1)^2q^3\) | all odd |
| \((3,3,1,1)\) | \(3(q-1)^2q^4\) | all odd |
| \((3,3,2)\) | \((q-1)^3q^4\) | characteristic \(3\) |
| \((4,2,2)\) | \((q-1)^3q^4\) | characteristic at least \(5\) |

All unlisted multiplicities are zero. Exactly seven partitions occur for each odd characteristic, and the listed multiplicities add to \(q^7=|\mathfrak m|\). For arbitrary \(a_0\in k\), multiplication by \(a_0+f\) has the same block sizes, all with eigenvalue \(a_0\); consequently the full algebra's eigenvalue-resolved distribution has the displayed multiplicity for every prescribed \(a_0\).

The nonlinear boundary is explicit: conditioned on exactly one of the three linear coefficients of \(f\) being nonzero, the probability that \(M_f\) has partition \((3,2,2,1)\), rather than the initial linear form's \((2,2,2,2)\), is exactly \(1-q^{-1}\). The generic partition is \((3,3,2)\) in characteristic \(3\) and \((4,2,2)\) in every odd characteristic at least \(5\). The complete finite-field counts, including the nonlinear rank jump, are the assertion; the known generic Lefschetz block at larger characteristic is not claimed as new.

## Assumptions and scope

The field is finite of odd characteristic; no restriction on its extension degree is imposed. The algebra is associative, commutative, unital and eight-dimensional, with basis \(1,x,y,z,xy,xz,yz,xyz\). Each radical element has a unique expression
\[
f=a_1x+a_2y+a_3z+b_{12}xy+b_{13}xz+b_{23}yz+cxyz,
\]
with coefficients in \(k\). A partition such as \((2,2,1,1,1,1)\) denotes the sizes of nilpotent Jordan blocks, with zeros omitted. All counts are for individually labeled elements \(f\), not orbit counts.

## Proof

**1. Degree at least two.** When \(a_1=a_2=a_3=0\), write \(f=u+cxyz\) with \(u=b_{12}xy+b_{13}xz+b_{23}yz\). The element \(f\) has square zero. If \(u\ne0\), its multiplication image is the span of \(f\) and \(xyz\): multiplication of \(u\) by a suitable linear generator gives a nonzero multiple of \(xyz\), while all products by quadratic terms vanish. Hence \(\operatorname{rank}M_f=2\). If \(u=0\) and \(c\ne0\), the rank is \(1\), and at zero it is \(0\). This gives respectively \(q(q^3-1)\), \(q-1\), and \(1\) elements and the first three relevant partitions.

**2. Unit and automorphism reductions.** Suppose a linear coefficient is nonzero; permute the three variables so that \(a_1\ne0\). With \(B=k[y,z]/(y^2,z^2)\), express \(A=B\oplus xB\) and
\[
f=xu+v,\quad u=a_1+b_{12}y+b_{13}z+cyz\in B^\times,\quad v=a_2y+a_3z+b_{23}yz\in B.
\]
Multiplying by the unit \(u^{-1}\) preserves the ranks of every power of the regular multiplication operator: \(M_{u^{-1}f}^j=M_{u^{-j}}M_f^j\), with invertible \(M_{u^{-j}}\). Thus the Jordan type equals that for \(x+w\), where \(w=v/u=\alpha y+\gamma z+\delta yz\) and \(\alpha=a_2/a_1\), \(\gamma=a_3/a_1\). If either \(\alpha\) or \(\gamma\) is nonzero, an automorphism of \(B\) of the form \(y\mapsto y+t yz\) or \(z\mapsto z+t yz\) kills \(\delta yz\). These maps are automorphisms because each transformed generator still squares to zero and its linear part is invertible. Rescaling generators then reduces \(f\), up to unit multiplication and algebra automorphism, to \(x+y\) or \(x+y+z\), according as exactly two or all three linear coefficients are nonzero. If only \(a_1\ne0\), the reduced form is \(x+\delta yz\), where \(\delta=b_{23}/a_1\).

**3. One nonzero linear coefficient.** For \(w=\delta yz\), one has \(w^2=0\). In the decomposition \(A=B\oplus xB\), multiplication by \(x+w\) sends \((b,c)\mapsto(wb,b+wc)\). Its kernel consists exactly of the pairs \((-wc,c)\), with arbitrary \(c\in B\). Thus its rank is \(4\). Moreover
\[
(x+\delta yz)^2=2\delta xyz,\qquad (x+\delta yz)^3=0.
\]
Since the characteristic is odd, the rank sequence \((\operatorname{rank}M_f,\operatorname{rank}M_f^2,\operatorname{rank}M_f^3)\) is \((4,0,0)\) if \(b_{23}=0\), and \((4,1,0)\) otherwise. These correspond to partitions \((2,2,2,2)\) and \((3,2,2,1)\).

**4. At least two nonzero linear coefficients.** For \(f=x+y\), tensoring multiplication by \(x+y\) on \(k[x,y]/(x^2,y^2)\) with the two-dimensional factor \(k[z]/(z^2)\) shows that the rank sequence is \((4,2,0)\). Hence the partition is \((3,3,1,1)\). For \(f=x+y+z\), the induced multiplication map between degrees one and two, in suitable ordered bases, has matrix
\[
\begin{pmatrix}1&1&0\\1&0&1\\0&1&1\end{pmatrix}
\]
with determinant \(-2\), nonzero in every odd characteristic. Combined with the nonzero maps from degree zero to one and from degree two to three, this gives \(\operatorname{rank}M_f=5\). The element \(f^2=2(xy+xz+yz)\) gives \(\operatorname{rank}M_f^2=2\), while \(f^3=6xyz\) gives \(\operatorname{rank}M_f^3=0\) in characteristic three and \(1\) in characteristics at least five. The resulting partitions are \((3,3,2)\) and \((4,2,2)\), respectively.

**5. Count disjoint cases.** There are \(3(q-1)\) possible linear coefficient triples with support exactly one, \(3(q-1)^2\) with support exactly two, and \((q-1)^3\) with support three. For support one, \(b_{23}=0\) permits \(q^3\) choices of the two remaining quadratic coefficients and \(c\); \(b_{23}\ne0\) permits \((q-1)q^3\). Each support-two or support-three linear triple permits all \(q^4\) higher-degree coefficient choices. Combining these counts with Step 1 gives the table. The sum is
\[
1+(q-1)+q(q^3-1)+3(q-1)q^3+3(q-1)^2q^3+3(q-1)^2q^4+(q-1)^3q^4=q^7.
\]
Finally, since nilpotent Jordan blocks are determined by the ranks of successive powers, all the displayed block partitions follow from the calculated rank sequences. This completes the classification.

## Verification

A supplied standalone checker constructs the eight-by-eight multiplication matrices in the squarefree monomial basis, computes the ranks of the first four powers by finite-field Gaussian elimination, and reconstructs the Jordan partition from successive rank differences. It exhaustively enumerates \(3^7=2187\) radical elements over \(\mathbb F_3\) and \(5^7=78125\) over \(\mathbb F_5\), recovering the two full tables. It separately tests the characteristic-two boundary exhaustively over \(\mathbb F_2,\mathbb F_4\) (not part of the assertion) and samples 50,000 elements each over \(\mathbb F_7\) and \(\mathbb F_{11}\); the samples check allowed types but are not count certificates. Run `python3 checker.py`. The exact output from a run is in `checker_output.txt`. The finite experiments serve only as checks; Steps 1–5 prove all odd prime-power cases.

## Relationship to prior work

Harima–Migliore–Nagel–Watanabe (2002), arXiv:math/0208201, establishes key Lefschetz results for Artinian complete intersections in characteristic zero, rather than enumerating all multiplication-Jordan fibers of the specified algebra over finite fields. Lundqvist–Nicklasson (first public version 2016), arXiv:1604.06820, gives characteristic-dependent strong Lefschetz criteria for monomial complete intersections; its Theorem 3.8 correctly anticipates the generic characteristic-three obstruction but does not give the present all-element multiplicities or the nonlinear support-one jump. Iarrobino–Macias Marques–McDaniel (first public version 2018), arXiv:1802.07383, explicitly records the familiar partition \((4,2,2)\) for \(x+y+z\) in this same algebra and discusses the characteristic-two exception. That generic case is acknowledged as known. The present claim is the complete odd-characteristic finite-field census, not a rediscovery of those linear or generic cases.

A semantic comparison with published finite-field Jordan censuses for \(k[x,y]/(x^3,y^3)\) and \(k[x,y]/(x^2,y^n)\) finds different algebras: those results neither specialize to the three-variable squarefree quotient nor count its distinguished nonlinear stratum. The exterior-algebra and characteristic-two elementary-abelian-group-algebra calculations use different multiplication laws or a different characteristic. An unindexed equivalent all-element table is still possible; searches alone cannot establish historical uniqueness.

## Limitations

The proof and census are confined to odd finite fields and this exact eight-dimensional algebra. No assertion is made for three or more generators with other truncation degrees, and the characteristic-two boundary is excluded from the theorem. The displayed generic partitions and Lefschetz implications are known, while the exact multiplicity table and nonlinear transition are the new asserted content. The verification is a reproducible finite check, not an independent mathematical audit or proof of originality. Priority could be affected by older unindexed enumerations.

## References

1. T. Harima, J. Migliore, U. Nagel and J. Watanabe, *The Weak and Strong Lefschetz Properties for Artinian K-Algebras*, arXiv:math/0208201 (first public 2002-08-26), https://arxiv.org/abs/math/0208201 .
2. S. Lundqvist and L. Nicklasson, *On the structure of monomial complete intersections in positive characteristic*, arXiv:1604.06820 (first public 2016-04-22), https://arxiv.org/abs/1604.06820 .
3. A. Iarrobino, P. Macias Marques and C. McDaniel, *Artinian algebras and Jordan type*, arXiv:1802.07383 (first public 2018-02-21), https://arxiv.org/abs/1802.07383 .
