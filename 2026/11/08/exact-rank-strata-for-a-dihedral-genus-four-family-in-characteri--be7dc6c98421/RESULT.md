# Exact rank strata for a dihedral genus-four family in characteristic seven

## Finding
Let \(k=\overline{\mathbb F}_7\). For \(a,b\in k\), let \(C_{a,b}\) be the smooth projective completion of
\[
 y^2=f_{a,b}(x)=x^9+a x^7+b x^5+a x^3+x,
\]
and restrict throughout to the smooth locus \(\Delta(a,b)\ne0\), where \(\Delta\) is the discriminant of
\(q_{a,b}(T)=T^4+aT^3+bT^2+aT+1\). Define the polynomials in \(\mathbb F_7[a,b]\)
\[
\begin{aligned}
 u&=3a,\\
 v&=3a^2b-a^2+3b^2+3,\\
 w&=3a^3+3ab^2-ab-a,\\
 D&=uw-v=2a^4+2a^2b^2+a^2b-2a^2-3b^2-3,\\
 E&=1+u^7w.
\end{aligned}
\]
Then the Jacobian \(J(C_{a,b})\) has precisely the following strata, with \(\gamma\) its \(7\)-rank and \(\alpha\) its \(a\)-number:

| Condition on a smooth parameter | \(\alpha\) | \(\gamma\) |
| --- | ---: | ---: |
| \(D\ne0\) | 0 | 4 |
| \(D=0,\ E\ne0\) | 2 | 2 |
| \(D=E=0\) | 2 | 0 |

In particular, the Jacobian is ordinary exactly off the plane divisor \(D=0\); no rank-one or rank-three \(7\)-rank and no \(a\)-number one, three or four occur. The \(7\)-rank-zero stratum consists of **exactly 20 distinct geometric parameter pairs** \((a,b)\) on the smooth locus. This is a count of parameter pairs, not an assertion that the corresponding curves represent 20 distinct isomorphism classes.

## Assumptions and scope
The ground field is algebraically closed of characteristic seven. The polynomial \(f_{a,b}=xq_{a,b}(x^2)\) has nine simple roots precisely when \(q_{a,b}\) is squarefree: its constant term is one, and the map \(x\mapsto x^2\) is separable away from zero. Thus \(\Delta\ne0\) makes the projective completion a genus-four hyperelliptic curve. No claim is made at singular parameters, nor about the full Newton polygon or geometric isomorphism classification. The two parameters are retained as labelled equation coefficients.

## Proof
Write \(f_{a,b}^3=\sum_{m=0}^{27}c_mx^m\). In the regular-differential basis \(\omega_j=x^{j-1}dx/y\), \(1\le j\le4\), the Cartier operator has matrix \(M^{(1/7)}\), where \(M_{ij}=c_{7i-j}\). This follows by writing \(1/y=f_{a,b}^3/y^7\) and retaining precisely the monomials with exponent one less than a multiple of seven. Direct coefficient extraction gives
\[
 M=\begin{pmatrix}
 0&u&0&1\\
 w&0&v&0\\
 0&v&0&w\\
 1&0&u&0
 \end{pmatrix}.
\]
After ordering the rows and columns as \((1,3,2,4)\), this is a block-antidiagonal matrix with blocks
\[
 A=\begin{pmatrix}u&1\\v&w\end{pmatrix},\qquad
 B=\begin{pmatrix}w&v\\1&u\end{pmatrix}.
\]
Both determinants equal \(D=uw-v\), so \(\det M=D^2\). Because each block has a unit entry, \(\operatorname{rank}M\) is four when \(D\ne0\) and exactly two when \(D=0\). By the Cartier description of the \(a\)-number, this yields \(\alpha=0\) and \(\alpha=2\), respectively.

The \(7\)-rank is the stable rank of the Cartier iterates. Since Cartier is \(7^{-1}\)-linear, the square of its matrix, after entrywise \(49\)th powers, equals \(M^{(7)}M\), *not* \(MM^{(7)}\). On \(D=0\) we have \(v=uw\), and the two rank-one factors become
\[
 A=\begin{pmatrix}1\\w\end{pmatrix}\begin{pmatrix}u&1\end{pmatrix},\quad
 B=\begin{pmatrix}w\\1\end{pmatrix}\begin{pmatrix}1&u\end{pmatrix}.
\]
Consequently the two diagonal blocks of \(M^{(7)}M\) are zero precisely when \(E=1+u^7w=0\), and otherwise are both rank one. Every successive adjacent product contributes a seventh-power iterate of \(E\). Hence the stable rank is zero if \(E=0\), and two otherwise. Where \(D\ne0\), Cartier is bijective and the stable rank is four. This proves the three strata without assuming that a first Cartier rank equals the \(7\)-rank.

It remains to count the \(7\)-rank-zero parameters, and verify their smoothness. Gröbner elimination over \(\mathbb F_7\), in lexicographic order \(b>a\), gives the **exact reduced Gröbner basis** of the ideal \((D,E)\):
\[
\begin{aligned}
 b+G(a)&=0,\\
 P(a)&=0,
\end{aligned}
\]
where
\[
 G(a)=3a^{20}+2a^{18}+2a^{14}-a^{12}+3a^{10}+3a^8-2a^6+a^4-3a^2+1
\]
and
\[
\begin{aligned}
 P(a)&=a^{22}-3a^{20}-2a^{16}-3a^{12}+a^{10}+a^8-3a^4+2a^2+2\\
 &=(a^2+3)^2(a^4+3a^2-1)(a^6-a^4-2a^2-3)\\
 &\quad\cdot(a^8+3a^6+3a^4-3a^2-2).
\end{aligned}
\]
The final three factors are separable, pairwise coprime, and coprime to \(a^2+3\); in particular \(\gcd(P,P')=a^2+3\), up to a unit. Thus \(P\) has exactly \(2+4+6+8=20\) distinct roots in \(k\), and \(b=-G(a)\) is unique for each. The unit-gcd certificate
\[
 \gcd\!\left(P(a),\,\Delta\bigl(a,-G(a)\bigr)\right)=1
 \quad\text{in }\mathbb F_7[a]
\]
shows every parameter is smooth. Both polynomial reductions and the gcd are recomputed in the supplied verification program. The count is geometric, not merely an enumeration over \(\mathbb F_7\) or \(\mathbb F_{49}\).

## Verification
From the folder containing these files, run `python3 verify_strata.py` (requires SymPy) and `python3 verify_field49.py` (Python standard library only). The first recomputes the Cartier matrix from the cube of the original equation, its determinant, the elimination basis, the factorization, and the smoothness gcd. The second implements independent arithmetic in \(\mathbb F_{49}\), directly cubes all coefficient vectors, checks squarefreeness by a polynomial Euclidean algorithm, and computes twisted matrix ranks on all 2,257 smooth \(\mathbb F_{49}\)-parameter pairs. The latter finds 2 rank-zero, 38 rank-two and 2,217 ordinary pairs over that *smaller* field; these counts are checks, not the justification for the 20 geometric points.

## Relationship to prior work
Ohashi and Kudo's study of automorphism-rich genus-four hyperelliptic curves (arXiv:2312.16858, Section 3.1, equations (3.6)–(3.7)) explicitly identifies the same dihedral normal form and develops enumeration of **superspecial** curves via genus-two quotients. It does not state the present characteristic-seven full rank stratification, the nonordinary divisor or the 20 rank-zero geometric parameter pairs. Kudo and Harashita (arXiv:1607.01114) previously proved that no genus-four curve in characteristic seven is superspecial; this excludes \(a\)-number four but does not exclude rank-zero Jacobians with \(a\)-number two. General Cartier-Manin formulas are standard and not claimed as new. The new assertion is the exact stratification and zero-rank parameter census in this natural symmetric family.

## Limitations
The count is for distinct coefficient pairs \((a,b)\) in this normal form, not for distinct geometric isomorphism classes, and the other nonordinary strata are not counted over arbitrary extension fields. \(7\)-rank zero is not asserted to imply supersingularity. The originality comparison rests on inspected papers and available mathematical-record searches and cannot rule out an unindexed earlier special-case calculation. No independent mathematical audit has been performed.

## References
1. R. Ohashi and M. Kudo, *Computing superspecial hyperelliptic curves of genus 4 with automorphism group properly containing the Klein 4-group*, arXiv:2312.16858 (first posted 2023-12-28), especially Section 2.2 and Section 3.1. https://arxiv.org/abs/2312.16858
2. M. Kudo, T. Nakagawa and T. Takagi, *Efficient Search for Superspecial Hyperelliptic Curves of Genus Four with Automorphism Group Containing C6*, Mathematics in Computer Science **17** (2023), article 21, especially Introduction and automorphism normal forms. https://doi.org/10.1007/s11786-023-00571-w
3. M. Kudo and S. Harashita, *Superspecial curves of genus 4 in small characteristic*, Finite Fields Appl. **45** (2017), 131–169; arXiv:1607.01114. https://arxiv.org/abs/1607.01114
