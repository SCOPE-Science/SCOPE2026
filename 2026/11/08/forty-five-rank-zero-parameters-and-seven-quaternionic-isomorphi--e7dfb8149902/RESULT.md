# Forty-five rank-zero parameters and seven quaternionic isomorphism classes in characteristic eleven

## Finding
Let \(k=\overline{\mathbf F}_{11}\). For every \(a\in k\) with \(a^2\ne4\), let \(H_a\) be the smooth projective hyperelliptic curve
\[
 H_a:\qquad y^2=x(x^4-1)(x^4+a x^2+1)=x^9+a x^7-a x^3-x.
\]
Every \(H_a\) has genus \(4\) and Jacobian \(a\)-number exactly \(2\). Define
\[
 G(a)=a^{45}-2a^{23}+a^{11}-4a\ \in\mathbf F_{11}[a].
\]
The geometric \(11\)-rank of the Jacobian equals \(0\) if \(G(a)=0\) and \(2\) otherwise. The polynomial \(G\) has exactly \(45\) distinct roots, none equal to \(\pm2\). Precisely \(42\) of these root parameters have full geometric automorphism group \(Q_8\); they represent exactly **seven** geometric isomorphism classes. The other three root parameters are \(a\in\{0,6,-6\}\), mutually isomorphic, with enhanced automorphism group \(C_{16}\rtimes C_2\). Thus the rank-zero locus consists of eight geometric isomorphism classes in the entire coefficient-marked family, seven with exact quaternion automorphism group. In particular none of these curves is superspecial, since their \(a\)-number is \(2\), not \(4\).

## Assumptions and scope
All statements are over the algebraic closure of the prime field of characteristic \(11\). The smoothness condition \(a^2\ne4\) is necessary and sufficient for the nine roots of the right-hand polynomial to be distinct. The Jacobian's \(11\)-rank is the stable rank of semilinear Frobenius on its first cohomology, and its \(a\)-number is \(4\) minus the rank of the Cartier operator on regular differentials. "Parameters" refers to coefficients \(a\); "isomorphism classes" refers to geometric isomorphisms of smooth curves, not to \(\mathbf F_{11}\)-rational model counts. The automorphism/isomorphism classification quoted in the proof applies because \(11\ge7\).

## Proof
Let \(F_a(x)=x^9+a x^7-a x^3-x\). For \(a^2\ne4\), the factors \(x\), \(x^4-1\), and \(x^4+a x^2+1\) are separable and pairwise coprime: a common root of the last two would require \(a=\pm2\). Hence the smooth double cover of \(\mathbf P^1\) branched at the nine finite roots and infinity has genus \(4\), by Riemann--Hurwitz.

Write \(F_a(x)^5=\sum_s c_s x^s\). In the differential basis \((dx/y,x\,dx/y,x^2\,dx/y,x^3\,dx/y)\), the Cartier--Manin coefficient matrix is \(M_{ij}=c_{11i-j}\) for \(1\le i,j\le4\), with the usual inverse-Frobenius semilinearity. Exact multiplication in \(\mathbf F_{11}[a,x]\) gives
\[
 M=\begin{pmatrix}
0&A&0&B\\ C&0&D&0\\0&-D&0&-C\\-B&0&-A&0
\end{pmatrix},\qquad
\begin{aligned}
 A&=a^2, & B&=-5a,\\
 C&=1-5a^2-3a^4, &D&=2a+a^3+5a^5.
\end{aligned}
\]
The polynomial identity \(AC-BD=0\) in characteristic \(11\) makes both checkerboard \(2\)-by-\(2\) blocks singular. They each have rank at least one: if \(a\ne0\), then \(B\ne0\); if \(a=0\), then \(C=1\). Thus \(\operatorname{rank}(M)=2\) at every smooth parameter, and the Jacobian \(a\)-number is \(4-2=2\).

Write \(M^{(11)}\) for entrywise eleventh powers. A second polynomial-ring multiplication, without specializing \(a\), establishes
\[
 M M^{(11)}=G(a)\,T(a),
\]
where
\[
T(a)=\begin{pmatrix}
-3a&0&5a^{12}&0\\
0&a^{11}-5a^{13}-3a^{15}&0&4a^4+3a^2-5\\
4a^4+3a^2-5&0&a^{11}-5a^{13}-3a^{15}&0\\
0&5a^{12}&0&-3a
\end{pmatrix}.
\]
The two checkerboard blocks of \(T\) have zero determinant identically, and each is everywhere nonzero: at \(a\ne0\) an entry \(-3a\) is nonzero; at \(a=0\) an entry \(-5\) is nonzero. Thus \(\operatorname{rank} T(a)=2\) for all \(a\). If \(G(a)=0\), the second semilinear iterate vanishes, so the geometric \(11\)-rank is zero. Otherwise each Frobenius-twisted pair of consecutive Cartier matrices has rank \(2\), because \(G(a^{11^j})=G(a)^{11^j}\ne0\). Since each one-step matrix also has rank \(2\), the rank of every longer iterate is \(2\): the map at each step is an isomorphism between the successive two-dimensional images. This proves the dichotomy \(0\) versus \(2\).

The formal derivative of \(G\) in characteristic \(11\) is \(G'(a)=a^{44}-2a^{22}-4\). Subtracting \(aG'(a)\) from \(G(a)\) gives \(a^{11}\). Hence \(\gcd(G,G')=1\): zero is a simple root since \(G'(0)=-4\), and a common nonzero root would force \(a^{11}=0\). Thus there are exactly \(45\) distinct roots over \(k\). Direct evaluation yields \(G(2)=-1\), \(G(-2)=1\), so all correspond to smooth curves.

For the isomorphism classification we invoke Taniguchi--Ohashi--Takagi, Theorem 3.1 and Corollary 3.1 (References). For \(a\ne\pm2\), the full automorphism group is \(\mathrm{SL}_2(\mathbf F_3)\) if \(a^2=-12\), the enhanced group \(C_{16}\rtimes C_2\) if \(a\in\{0,\pm6\}\), and \(Q_8\) otherwise. Exact Euclidean polynomial computations yield
\[
 \gcd(G,a^2+12)=1,\qquad \gcd(G,a(a^2-36))=a(a^2-36).
\]
Thus exactly the three enhanced parameters are rank-zero and no rank-zero parameter has \(\mathrm{SL}_2(\mathbf F_3)\) automorphisms. The same theorem identifies all isomorphic coefficient-marked curves by
\[
 b\in\left\{\pm a,\ \pm\left(2-\frac{16}{a+2}\right),\ \pm\left(2+\frac{16}{a-2}\right)\right\}.
\]
All six expressions are distinct for a parameter with automorphism group exactly \(Q_8\), and the three enhanced parameters constitute one orbit. Hence the remaining \(45-3=42\) rank-zero parameters form exactly \(42/6=7\) isomorphism classes, and together with the enhanced orbit give eight classes.

## Verification
Run both standard-library Python scripts in the same directory:

```sh
python3 verify_coefficients.py
python3 verify_frobenius.py
```

The first independently multiplies the defining polynomial to recover all Cartier coefficients. The second verifies every entry of the identity \(MM^{(11)}=GT\), the rank-two block identities, squarefreeness, excluded-point evaluations, polynomial greatest common divisors for enhanced groups, and that all six published isomorphism transforms preserve the zero set \(G=0\). Both were executed successfully. Their exact symbolic identities apply to all geometric parameter values; this is not a finite-field sampling argument.

## Relationship to prior work
Ohashi and Kudo (2023, arXiv:2312.16858) develop algorithms for **superspecial** genus-four hyperelliptic curves with extra involutions. Taniguchi, Ohashi, and Takagi (2025, arXiv:2505.00241, particularly Proposition 3.1, Theorem 3.1, Corollaries 3.1 and 3.2) introduce the same quaternion normal form, derive general Cartier coefficients, classify isomorphisms and automorphism groups, and count **superspecial** quaternion curves. Those normal-form and group assertions are used and credited here. The distinction is the geometric *stable* Cartier rank: in characteristic eleven the Cartier matrix is always rank two, but its square vanishes at 45 marked parameters, yielding seven non-superspecial rank-zero quaternion isomorphism classes. The cited work does not state that rank-zero parameter polynomial or the associated rank stratification.

## Limitations
The result is specific to characteristic \(11\), although the curve family exists in many odd characteristics. It counts geometric curve isomorphism classes only inside the stated quaternionic family, as already parametrized by the cited group-classification theorem. Neither the Newton polygons nor Ekedahl--Oort types beyond the stated rank and \(a\)-number are determined. A missing older article with an equivalent change of parameter remains a historical-priority possibility; search failure alone cannot prove novelty. No independent mathematical audit has been performed.

## References
1. R. Ohashi and M. Kudo, *Computing superspecial hyperelliptic curves of genus 4 with automorphism group properly containing the Klein 4-group*, arXiv:2312.16858, first version 2023-12-28, https://arxiv.org/abs/2312.16858.
2. T. Taniguchi, R. Ohashi, and T. Takagi, *Enumeration algorithm for genus-4 superspecial hyperelliptic curves with automorphism group \(Q_8\)*, arXiv:2505.00241, first version 2025-05-01, https://arxiv.org/abs/2505.00241, particularly Theorem 3.1 and Corollaries 3.1--3.2.
