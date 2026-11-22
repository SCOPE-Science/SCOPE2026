# Composition-centralizer spectra in the smallest odd Heisenberg groups

## Finding

Let \(p\) be an odd prime and \(H_p\) the nonabelian exponent-\(p\) group of order \(p^3\). Write \(M_p=\operatorname{End}(H_p)\) for its composition monoid and \(C_{M_p}(f)=\{g\in M_p:fg=gf\}\). The complete centralizer-size polynomial is

\[
\begin{aligned}
Z_p(X):=\sum_{f\in M_p}X^{|C_{M_p}(f)|}
={}&2X^{p^6}+2(p^2-1)X^{p^3(2p-1)}+(p-2)p^2X^{p^4}\\
&+p(s+j)X^{p^3}+s(p^2-p)X^{p(2p-1)}\\
&+j(p^2-p)X^{2p^2}+gp^2X^{p^2},
\end{aligned}
\]
where
\[
s=p(p+1)(2p-3),\qquad j=2(p^2-1),\qquad
 g=p^4-p-s-j=p^4-2p^3-p^2+2p+2.
\]
All seven displayed centralizer cardinalities are distinct for odd primes. In particular,
\[
\#\{(f,g)\in M_p^2:fg=gf\}=p^8+5p^7-8p^5+3p^3,
\]
\[
\Pr_{f,g\text{ uniform in }M_p}(fg=gf)
=p^{-4}+5p^{-5}-8p^{-7}+3p^{-9},
\]
and the center of \(M_p\) is the two-element set consisting of the trivial group endomorphism and the identity.

## Assumptions and scope

The characteristic is odd; no assertion is made in characteristic two or for higher-rank extraspecial groups. Set \(V=\mathbb F_p^2\), let \(\omega(w,w')=w_1w'_2-w_2w'_1\), and give \(V\times\mathbb F_p\) the group law
\[
(w,z)(w',z')=(w+w',z+z'+\tfrac12\omega(w,w')).
\]
This group is \(H_p\). Matrices act on *column* vectors, and functional parameters are *row* vectors. The composition product means \((fg)(x)=f(g(x))\).

The parameterization of these endomorphisms by a matrix and central functional is known from the extraspecial-group endomorphism classification of Kumar and Pradhan (2019). The new assertion here is the seven-level **composition-centralizer distribution**, its exact frequencies, and their sum. This work does not claim the established parametrization or the total number \(|M_p|=p^6\) as new.

## Proof

**1. Endomorphism normal form and composition.** The central subgroup \(Z(H_p)=[H_p,H_p]\) is characteristic and the induced map on \(H_p/Z(H_p)\cong V\) is linear, say \(A\in M_2(\mathbb F_p)\). The commutator identity forces the central multiplier to be \(\det A\), since \(\omega(Aw,Aw')=(\det A)\omega(w,w')\). Subtracting this central multiplier from the third coordinate leaves an additive linear functional, so each endomorphism is uniquely
\[
 f_{A,u}(w,z)=(Aw,(\det A)z+uw),
 \quad A\in M_2(\mathbb F_p),\ u\in V^*.
\]
Conversely the displayed map respects the group operation. Hence \(|M_p|=p^4p^2=p^6\). For \(\delta=\det A\) and \(\eta=\det B\), composition gives
\[
 f_{A,u}\circ f_{B,v}=f_{AB,uB+\delta v}.
\]
Thus \(f_{A,u}\) and \(f_{B,v}\) commute if and only if
\[
 AB=BA,\qquad v(A-\delta I)=u(B-\eta I).\tag{1}
\]
The linear map \(v\mapsto v(A-\delta I)\) has image the row space \(L\) of \(A-\delta I\), and each nonempty fiber has cardinality \(p^{2-\operatorname{rank}(A-\delta I)}\). This is the only linear-algebra counting input.

**2. Scalar matrices.** If \(A=\lambda I\), then \(\delta=\lambda^2\). For \(\lambda\notin\{0,1\}\), the matrix \(A-\delta I=(\lambda-\lambda^2)I\) is invertible; each of the \(p^4\) matrices \(B\) admits exactly one \(v\), so \(|C_{M_p}(f_{A,u})|=p^4\) for all \(u\). There are \((p-2)p^2\) such maps.

For \(A=0\) or \(A=I\), Equation (1) reduces to \(uB=(\det B)u\), and \(v\) is arbitrary. When \(u=0\), every \(B,v\) works and the centralizer has size \(p^6\). For \(u\ne0\), change basis to put \(u=(1,0)\). Then \(B=\begin{pmatrix}a&0\\c&d\end{pmatrix}\), with \(a=ad\), which has \(p(2p-1)\) solutions in \(B\). The free \(v\) provides a factor of \(p^2\), so the centralizer size is \(p^3(2p-1)\). These strata have multiplicities \(2\) and \(2(p^2-1)\).

**3. Nonscalar matrices.** For any nonscalar \(2\times2\) matrix \(A\), its matrix centralizer is precisely the two-dimensional algebra \(\{xI+yA:x,y\in\mathbb F_p\}\). One proof chooses a vector \(w\) with \(w,Aw\) independent, then notes that any commuting matrix is uniquely determined by its value on \(w\), yielding the two-parameter description. Hence there are exactly \(p^2\) possible \(B\) in Equation (1).

If \(M=A-\delta I\) is invertible, each \(B\) determines one \(v\), giving centralizer size \(p^2\). The only remaining case is \(\operatorname{rank}M=1\). Because \(\det(A-\delta I)=0\), the scalar \(\delta=\det A\) is an eigenvalue of \(A\). Thus its other eigenvalue is either arbitrary nonzero \(t\) when \(\delta=0\), or \(1\) when \(\delta\ne0\). A nonscalar rank-one \(M\) is either (i) diagonalizable with distinct eigenvalues \((0,t)\), \(t\ne0\), or \((1,t)\), \(t\ne0,1\), or (ii) a nontrivial Jordan block with repeated eigenvalue \(0\) or \(1\).

For distinct eigenvalues, choose the two eigenspaces as distinct lines. There are \(p(p+1)\) ordered decompositions into two such lines and \((p-1)+(p-2)=2p-3\) allowed eigenvalue pairs. The total number of matrices is therefore \(s=p(p+1)(2p-3)\). For each eigenvalue \(0\) or \(1\), the nonzero nilpotent \(2\times2\) matrices constitute one similarity class of size \(p^2-1\), giving \(j=2(p^2-1)\) Jordan matrices. There are \(p^4-p-s-j=g\) nonscalar matrices with invertible \(M\).

Fix a rank-one \(M\) and put \(L=\operatorname{row}(M)\). If \(u\in L\), the right-hand side of Equation (1) is always in \(L\) for every \(B=xI+yA\), because \(L\) is \(A\)-invariant. For each of the \(p^2\) choices of \(B\), there are \(p\) solutions \(v\). Thus the centralizer has cardinality \(p^3\). Exactly \(p\) choices of \(u\) lie in \(L\) per rank-one matrix.

If \(u\notin L\), the matrix \(A\) acts on the one-dimensional row quotient \(V^*/L\) by the eigenvalue \(\delta\). Equation (1) is soluble precisely when
\[
 \det(xI+yA)=x+y\delta.\tag{2}
\]
For a diagonalizable rank-one case, Equation (2) is either \(x(x+ty-1)=0\) (eigenvalues \(0,t\)) or \((x+y\delta)(x+y-1)=0\) (eigenvalues \(\delta,1\)). In either case it is the union of two distinct nonparallel affine lines, with exactly \(2p-1\) solutions \((x,y)\). Each of these yields \(p\) choices of \(v\), so the centralizer size is \(p(2p-1)\).

For a Jordan matrix, Equation (2) reduces to \(x(x-1)=0\) at eigenvalue \(0\), or \((x+y)(x+y-1)=0\) at eigenvalue \(1\). The solution set is two parallel lines, with exactly \(2p\) solutions. The centralizer therefore has size \(2p^2\). In both types there are \(p^2-p\) choices of \(u\notin L\) per matrix.

**4. Assemble and sum.** Combining scalar, rank-one and invertible-\(M\) cases yields the seven terms in \(Z_p(X)\). The total coefficient sum simplifies to \(p^6\), checking that every endomorphism is counted once. The weighted sum of exponents gives \(p^8+5p^7-8p^5+3p^3\), because each commuting ordered pair is counted once by its first coordinate. Division by \(|M_p|^2=p^{12}\) gives the probability. Since only two maps have centralizer cardinality \(p^6\), and those maps are the trivial endomorphism and identity, the stated center follows. The seven powers are pairwise distinct for every odd prime, so there is no need to merge frequencies.

## Verification

The standalone `verify.py` implements both the seven-term closed formula and, separately, a direct enumeration of matrix-commutation constraints and linear-fiber solution counts. It exhaustively compares full centralizer histograms at \(p=3,5,7\). It also verifies all homomorphism identities on all pairs of elements of \(H_3\) for every parameterized endomorphism and checks the composition law on the generating set for all ordered parameter pairs at \(p=3\).

| Prime | Centralizer size : multiplicity | Total ordered commuting pairs |
|---|---|---:|
| \(3\) | \(9:234,\ 15:216,\ 18:96,\ 27:156,\ 81:9,\ 135:16,\ 729:2\) | 15,633 |
| \(5\) | \(25:9050,\ 45:4200,\ 50:960,\ 125:1290,\ 625:75,\ 1125:48,\ 15625:2\) | 756,625 |
| \(7\) | \(49:82418,\ 91:25872,\ 98:4032,\ 343:4984,\ 2401:245,\ 4459:96,\ 117649:2\) | 9,749,089 |

Run `python3 verify.py`; the expected terminal assertion is `FINITE_HEISENBERG_ENDOMORPHISM_CENTRALIZERS_PASSED`. The infinite-prime theorem follows from the algebraic case split, not from these finite checks.

## Relationship to prior work

Kumar and Pradhan, *On the Endomorphism Semigroups of Extra-special p-groups and Automorphism Orbits* (first publicly posted 2019-08-01, arXiv:1908.00331), Theorem \(\Omega\), give the general extraspecial endomorphism parametrization and the total endomorphism count. This result **uses** that known parametrization, specializes to the rank-one symplectic quotient, and determines the distinct, additional invariant of the full composition-centralizer spectrum. Their paper's studied invariants include semigroup images and automorphism orbits of **group elements**; it does not state the seven composition-centralizer frequencies or the derived commuting-pair count. Szabó, *Finite Class 2 Nilpotent and Heisenberg Groups* (first posted 2023-01-05, arXiv:2301.01863), gives structural decompositions and embeddings rather than composition-commutant enumeration.

Commuting pairs of **elements inside** an extraspecial group, Reidemeister numbers of group automorphisms, and centralizers of associated Heisenberg Lie-algebra operators are different objects. None of those invariant counts directly supplies the full \(\operatorname{End}(H_p)\)-centralizer histogram. The normal-form calculation is a new enumeration applied to a known algebraic description, not a new classification of all endomorphisms.

## Limitations

The result is limited to odd prime fields and the order-\(p^3\) exponent-\(p\) Heisenberg groups. Neither higher-rank extraspecial groups nor exponent-\(p^2\) groups nor characteristic two are addressed. Computational checks cover only primes \(3,5,7\), while the proof itself covers every odd prime. Originality is assessed against indexed mathematical records and primary literature examined here; lack of a discovered earlier identical formula is not a guarantee of historical priority. Independent verification has not been performed.

## References

1. C. P. Anil Kumar and S. S. Pradhan, *On the Endomorphism Semigroups of Extra-special p-groups and Automorphism Orbits*, arXiv:1908.00331, first public version 2019-08-01. https://arxiv.org/abs/1908.00331
2. D. R. Szabó, *Finite Class 2 Nilpotent and Heisenberg Groups*, arXiv:2301.01863, first public version 2023-01-05. https://arxiv.org/abs/2301.01863
