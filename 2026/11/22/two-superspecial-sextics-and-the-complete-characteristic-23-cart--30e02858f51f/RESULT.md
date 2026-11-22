# Two superspecial sextics and the complete characteristic-23 Cartier stratification

## Finding
Over an algebraically closed field \(k\) of characteristic \(23\), let \(C_t\) be the coefficient-marked plane sextic
\[
C_t:\quad X^6+Y^6+Z^6+t(X^3Y^3+Y^3Z^3+Z^3X^3)=0.
\]
It is smooth exactly for \(t\notin\{2,-2,-1\}\), and every smooth member has genus \(10\). Its Jacobian has the following **complete geometric** \(23\)-rank and \(a\)-number stratification. Define polynomials over \(\mathbb F_{23}\):
\[
\begin{aligned}
Q(t)&=(t+4)(t+10)(t-11)(t-9)(t-5)\\
&\quad\cdot(t^2+3t-9)(t^2+8t-1),\\
R(t)&=(t+8)(t+10)(t+11)(t-4)(t^2+2t+2).
\end{aligned}
\]
Here all coefficient arithmetic is modulo \(23\). For smooth \(t\), the complete classification is
\[
\begin{array}{c|c|c|c}
\text{parameter condition}&\text{number of geometric parameters}&23\text{-rank}&a\text{-number}\\ \hline
 t\in\{0,-10\}&2&0&10\\
 R(t)=0,\ t\ne-10&5&2&8\\
 Q(t)=0,\ t\ne-10&8&6&4\\
 \text{all remaining smooth }t&\text{open complement}&8&2.
\end{array}
\]
In the second and third rows the roots are understood geometrically over \(k\). In particular **precisely two smooth members are superspecial**: the classical Fermat sextic \(C_0\) and the distinct Hessian-group sextic \(C_{-10}\). The latter has automorphism group \(\operatorname{Hess}_{216}\), whereas the Fermat sextic has group \((\mathbb Z/6\mathbb Z)^2\rtimes S_3\), as characterized in the source literature for characteristic greater than \(21\).

Of the \(20\) smooth \(\mathbb F_{23}\)-rational parameter values, exactly \(2,3,4,11\) have ranks \(0,2,6,8\), respectively; the smooth rank-zero parameters are \(0\) and \(13=-10\).

## Assumptions and scope
The displayed curve and its parameter are fixed, without quotienting by changes of projective coordinates. The base field may be any algebraic closure of \(\mathbb F_{23}\). The \(23\)-rank is the stable rank of the semilinear Frobenius action on \(H^1(C_t,\mathcal O_{C_t})\); the \(a\)-number is the kernel dimension of Cartier on holomorphic differentials, so \(a=10-\operatorname{rank}H\) for a Hasse--Witt matrix \(H\). Superspecial means \(a=10\) for this genus-ten curve, equivalently Cartier equal to zero. No isomorphism-class count is claimed for the full marked family.

## Proof
**Smooth locus.** Put \(u=X^3\), \(v=Y^3\), \(w=Z^3\). Since \(3\) and \(6\) are nonzero in characteristic \(23\), the three partial derivatives are \(3X^2(2u+t(v+w))\) and its cyclic analogues. For \(XYZ\ne0\), the coefficient matrix of the linear system in \((u,v,w)\) has eigenvalues \(2-t\) (twice) and \(2+2t\) (once). Such a critical projective point exists for \(t=2,-1\). With exactly one coordinate zero, the remaining two derivatives have a nonzero common solution exactly when \(t^2=4\), yielding \(t=2,-2\); no coordinate vertex is critical. Euler's identity \(6F_t=XF_X+YF_Y+ZF_Z\) puts every projective critical point on the sextic. Therefore the excluded set is exactly \(\{2,-2,-1\}\). The plane-degree genus formula gives \(g=10\).

**Hasse--Witt matrix.** Order the ten triples \((i,j,k)\) with \(i,j,k\ge0\) and \(i+j+k=3\) lexicographically, indexed \(0,\ldots,9\), and put \(\alpha=(i+1,j+1,k+1)\). The Čech-cohomology basis of \(H^2(\mathbb P^2,\mathcal O(-6))\cong H^1(C_t,\mathcal O_{C_t})\) indexed by positive degree-six exponent triples gives the coefficient formula
\[
H_{ab}=[X^{23\alpha_{a,1}-\alpha_{b,1}}Y^{23\alpha_{a,2}-\alpha_{b,2}}Z^{23\alpha_{a,3}-\alpha_{b,3}}]F_t^{22}.
\]
It follows by taking the Frobenius power of a reciprocal monomial, multiplying by \(F_t^{22}\), and projecting to the Čech monomials with strictly negative exponents. Transposing this matrix changes neither the ranks nor the vanishing assertions.

The multinomial theorem, applied to the six terms of \(F_t\), gives exactly twelve nonzero entries of the symbolic matrix. The only values are
\[
\begin{aligned}
A(t)&=5t(t+2)^4Q(t),\\
B(t)&=5t(t-2)^{12}Q(t),\\
U(t)&=-t(t+2)^4(t-2)^{11}R(t),
\end{aligned}
\]
with positions
\[
\begin{array}{c|l}
\text{entry value}&\text{row,column positions}\\ \hline
A&(0,5),(3,5),(9,5)\\
B&(5,0),(5,3),(5,9)\\
U&(1,4),(4,1),(2,6),(6,2),(7,8),(8,7).
\end{array}
\]
Every other entry is identically zero over \(\mathbb F_{23}[t]\). A direct way to reproduce each coefficient is to sum the multinomial weights \(22!/(n_0!\cdots n_5!)\) with \(\sum n_i=22\) and with the three exponent constraints
\[
\begin{aligned}
6n_0+3n_3+3n_4&=23\alpha_{a,1}-\alpha_{b,1},\\
6n_1+3n_3+3n_5&=23\alpha_{a,2}-\alpha_{b,2},\\
6n_2+3n_4+3n_5&=23\alpha_{a,3}-\alpha_{b,3};
\end{aligned}
\]
each term contributing the power \(t^{n_3+n_4+n_5}\). The standalone verifier enumerates **all one hundred** matrix entries and checks these factorizations directly, without symbolic interpolation from sample fields.

**Stable rank.** The coordinate subspace with indices \(1,4,2,6,7,8\) decomposes into three two-dimensional swap blocks of scalar \(U\), giving stable rank six if \(U\ne0\) and zero otherwise. On the complementary subspace spanned by \(e_0,e_3,e_9,e_5\), let \(s=e_0+e_3+e_9\). The map sends \(e_5\mapsto As\) and \(s\mapsto3Be_5\), killing two independent differences between the first three basis vectors. Since \(3\ne0\), when \(AB\ne0\) the \(\langle s,e_5\rangle\) summand is invertible, even upon all Frobenius coefficient twists; when \(A=B=0\) this summand vanishes. On the smooth locus, \(t\ne\pm2\) implies \(A=0\iff B=0\iff tQ(t)=0\), and \(U=0\iff tR(t)=0\). Hence for every geometric smooth parameter the Hasse--Witt rank **and its stable Frobenius rank** are both
\[
f(C_t)=2\,\mathbf1_{tQ(t)\ne0}+6\,\mathbf1_{tR(t)\ne0}.
\]
The same block decomposition gives \(a(C_t)=10-f(C_t)\).

**Exact parameter counts.** The two degree-two factors in \(Q\) and the degree-two factor in \(R\) each have discriminant \(-1\) times a nonzero square in \(\mathbb F_{23}\), and are irreducible (indeed their discriminants reduce to \(-1,-1,-4\)). All displayed factors are pairwise distinct within each polynomial, and \(\gcd(Q,R)=t+10\). None of the zeros of \(tQ(t)R(t)\) is a singular parameter. Thus the two zero sets of \(tQ\) and \(tR\) have sizes \(10\) and \(7\) with intersection \(\{0,-10\}\). The four ranks therefore occur at exactly \(2\), \(7-2=5\), and \(10-2=8\) exceptional geometric parameters, and at every other smooth point on the parameter line. The greatest common divisor of the three matrix-entry polynomials is, up to a unit,
\[
\gcd(A(t),B(t),U(t))=t(t+10).
\]
This proves that there are exactly two smooth Cartier-zero members. Finally, the linear factors account for the \(\mathbb F_{23}\)-rational counts; all three quadratic factors are irreducible there, giving the enumerated \(2,3,4,11\) profile.

## Verification
The standalone standard-library Python program `verify_sextic_23.py` reconstructs all one hundred symbolic Hasse--Witt entries by multinomial sums modulo \(23\); independently checks the three factored polynomials via finite-field polynomial multiplication and Euclidean gcd; checks smoothness exclusions, quadratic irreducibility and the rational-parameter rank census; and directly expands \(F_t^{22}\) at five special parameter values as a second coefficient algorithm. It also independently counts \(24\) rational points on each of the two superspecial sextics over \(\mathbb F_{23}\), a useful consistency check for zero Hasse--Witt trace. Run `python3 verify_sextic_23.py` with Python 3 and no dependencies. The verifier prints `VERIFIED_P23_SUPERSPECIAL_2_RANK2_5_RANK6_8_GENERIC_RANK8`.

The infinite algebraic-closure classification follows from factored polynomial identities and the semilinear-block proof, not from the finite-field count or finite tests alone.

## Relationship to prior work
Badr and Bars, *The stratification by automorphism groups of smooth plane sextic curves* (arXiv:2208.12749v1, August 26, 2022), Theorem 2.1 and Table 1, identify the Fermat and Hessian \(216\)-group sextics as two distinct special automorphism classes in characteristic greater than \(21\), but do not classify their Hasse--Witt matrices. Fukasawa, Miura, and Takahashi, *Quasi-Galois points, II: Arrangements* (arXiv:2211.16033v1, November 29, 2022), Section 4 and Theorem 4.3, study quasi-Galois points and automorphisms of the same \(t=-10\) sextic in characteristic zero, not characteristic-\(23\) Cartier arithmetic. The public earlier study *The 5-rank-eight stratum of a symmetric genus-ten plane-sextic family* concerns exactly this coefficient-marked equation **in characteristic five**. Its universal \(5\)-rank formula does not imply a characteristic-\(23\) formula: in characteristic five the special parameter \(-10\) coincides with \(0\), whereas in characteristic \(23\) the two remain distinct. Standard plane-curve Cartier coefficient algorithms (e.g. Kudo--Harashita, arXiv:2203.11801) supply the general method but not the present factored classification. Classical Fermat superspeciality at \(t=0\) is not claimed as new.

## Limitations
This is a complete statement only for the displayed symmetric coefficient-marked pencil in characteristic exactly \(23\). It does not compute Newton polygons, Ekedahl--Oort types beyond \(a\)-number and \(p\)-rank, isomorphism identifications between arbitrary different parameters, or the zeta functions of the curves. The three singular parameters are excluded. No inference about other prime characteristics is made. An equivalent unindexed historical calculation remains a residual priority risk, and independent mathematical validation has not been performed.

## References
1. E. Badr and F. Bars, *The stratification by automorphism groups of smooth plane sextic curves*, arXiv:2208.12749v1, August 26, 2022; Table 1, Theorem 2.1. https://arxiv.org/abs/2208.12749
2. S. Fukasawa, K. Miura, and T. Takahashi, *Quasi-Galois points, II: Arrangements*, arXiv:2211.16033v1, November 29, 2022; Section 4, Theorem 4.3 and Remark 4.4. https://arxiv.org/abs/2211.16033
3. M. Kudo and S. Harashita, *Computing the space of differential forms of a plane curve and its Cartier-Manin matrix*, arXiv:2203.11801, March 22, 2022. https://arxiv.org/abs/2203.11801
4. *The 5-rank-eight stratum of a symmetric genus-ten plane-sextic family*, published November 2, 2026, scientific result and proof in the publicly accessible published-finding corpus repository. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-the-5-rank-eight-stratum-of-a-symmetric-genus-ten-plane-sextic-f--2ab4759fb510
