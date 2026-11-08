# The unique rank-one Jacobian class in a reciprocal genus-three family over \(\overline{\mathbb F}_5\)

## Finding

Let \(k=\overline{\mathbb F}_5\). For each \((a,b)\in k^2\) with
\[
\Delta(a,b)=(2a-b-2)^2(2a+b+2)^2(a^2-4b+8)^4\ne0,
\]
let \(C_{a,b}\) denote the smooth projective completion of
\[
y^2=x^8+ax^6+bx^4+ax^2+1.
\]
Here the displayed discriminant omits the harmless unit \(256=1\) in characteristic five. Define
\[
\lambda_+=a^2+2b+2a,\qquad \lambda_-=a^2+2b-2a,\qquad
\lambda_0=2a^2+b^2+2.
\]
Writing \(f_5(C)\) for the geometric \(5\)-rank of its Jacobian and \(a(C)\) for its Cartier \(a\)-number, the complete stratification is
\[
f_5(C_{a,b})=\mathbf1_{\lambda_+\ne0}+\mathbf1_{\lambda_-\ne0}
 +\mathbf1_{\lambda_0\ne0},\qquad a(C_{a,b})=3-f_5(C_{a,b}).
\]
The ranks are exactly \(1,2,3\) on the smooth parameter surface, and rank zero never occurs. The locus of rank one is the **reduced** three-point subscheme
\[
\{(0,0),(2,0),(-2,0)\}.
\]
All three resulting smooth curves are isomorphic over \(k\), so their image in the unmarked genus-three moduli space consists of one geometric point, represented by \(y^2=x^8+1\). The three coefficient points are not claimed to be three distinct geometric isomorphism classes.

## Assumptions and scope

All fields in the theorem have characteristic exactly \(5\); all parameter pairs range over the algebraic closure \(k\), not just finite subfields. The discriminant condition is necessary and sufficient for squarefreeness of the monic octic; hence the projective normalization has genus \(3\) with two smooth points over infinity. The \(5\)-rank is the dimension of the stable image of Frobenius acting on first cohomology, equivalently the rank of the étale part of the Jacobian's \(5\)-torsion. The \(a\)-number is the dimension of the kernel of Cartier on regular differentials.

These curves have the commuting involutions \((x,y)\mapsto(-x,y)\) and \((x,y)\mapsto(1/x,y/x^4)\). The statement classifies a fixed, naturally normalized two-parameter coefficient family; it does not assert a census of all genus-three curves or of all possible normal forms under automorphisms.

## Proof

**(1) Smoothness.** Set \(f(x)=x^8+ax^6+bx^4+ax^2+1\). The exact polynomial discriminant over \(\mathbb Z[a,b]\) factors as
\[
\operatorname{Disc}_x f=256(2a-b-2)^2(2a+b+2)^2(a^2-4b+8)^4.
\]
Its reduction modulo \(5\) is the defining product above. Since \(2\) is invertible, nonzero discriminant makes the double cover of \(\mathbb P^1\) geometrically smooth. Riemann–Hurwitz with eight distinct branch points gives genus \(3\).

**(2) Cartier calculation.** The basis of regular differentials is
\[\omega_1=dx/y,\quad\omega_2=x\,dx/y,\quad\omega_3=x^2\,dx/y.\]
Write \(f(x)^2=\sum_{m=0}^{16}c_mx^m\). In characteristic \(5\), the Cartier–Manin coefficient matrix is \(H_{ij}=c_{5i-j}\) for \(1\le i,j\le3\), up to inverse-Frobenius of its coefficients. Direct expansion gives
\[
H=\begin{pmatrix}
a^2+2b&0&2a\\
0&2a^2+b^2+2&0\\
2a&0&a^2+2b
\end{pmatrix}.
\]
The constant invertible change of basis with columns \((1,0,1),(1,0,-1),(0,1)\), all defined over \(\mathbb F_5\), makes \(H\) diagonal with entries \(\lambda_+,\lambda_-,\lambda_0\). Because this change of basis is fixed by fifth power, the inverse-Frobenius semilinear Cartier operator is diagonal in the same basis; a nonzero diagonal entry produces a one-dimensional bijective semilinear summand, while a zero entry gives a zero summand. Every iterate has the same nonzero coordinates. Thus the stable Cartier rank, hence the Jacobian \(5\)-rank, equals the number of nonzero \(\lambda\)'s. Its immediate Cartier rank gives \(a(C)=3-f_5(C)\).

**(3) Independent geometry of the three summands.** The three involution quotients have function fields with explicit quartic genus-one models, using the indicated \(t\) and \(Y\):
\[
\begin{aligned}
E_0:&\quad Y^2=t^4+at^3+bt^2+at+1,&&(t,Y)=(x^2,y),\\
E_+:&\quad Y^2=t^4+(a-4)t^2+(b-2a+2),&&(t,Y)=(x+x^{-1},y/x^2),\\
E_-:&\quad Y^2=t^4+(a+4)t^2+(b+2a+2),&&(t,Y)=(x-x^{-1},y/x^2).
\end{aligned}
\]
The assertions follow by multiplying the last two defining equations by \(x^4\); their quotients are nonsingular of genus one on \(\Delta\ne0\). The invariant field for the full Klein four-group is rational: \(u=y/x^2\) and \(s=x^2+x^{-2}\) satisfy \(u^2=s^2+as+b-2\). Since the group order four is prime to characteristic five, the usual idempotent decomposition of differentials and Jacobians identifies the three elliptic contributions to \(5\)-rank. The coefficient of \(t^4\) in each quotient quartic squared is respectively \(\lambda_0,\lambda_-,\lambda_+\). This agrees independently with the Cartier diagonalization; a genus-one quotient is ordinary precisely when its displayed Hasse coefficient is nonzero.

**(4) Classification and reducedness of the exceptional locus.** Rank one means at least two of \(\lambda_+,\lambda_-,\lambda_0\) vanish. Since \(\lambda_+-\lambda_-=4a\), the common zero of \(\lambda_+\) and \(\lambda_-\) is just \((a,b)=(0,0)\); there \(\lambda_0=2\). To solve \(\lambda_+=\lambda_0=0\), substitute \(b=2a^2+4a\) and obtain the identity over \(\mathbb F_5\)
\[
\lambda_0(a,2a^2+4a)=-(a+2)(a-1)^3.
\]
The root \(a=-2\) yields \((-2,0)\), which is smooth; \(a=1\) yields \((1,1)\), which is excluded by the discriminant. Similarly \(\lambda_-=\lambda_0=0\) entails \(b=2a^2+a\) and
\[
\lambda_0(a,2a^2+a)=-(a-2)(a+1)^3.
\]
The root \(a=2\) yields \((2,0)\); \(a=-1\) yields excluded \((-1,1)\). The three surviving pairs have \(\Delta\ne0\) and exactly one nonzero eigenvalue, so they give precisely all rank-one curves. There are no common zeros of all three eigenvalues on the smooth locus (indeed anywhere).

Scheme-theoretically the rank-at-most-one determinantal ideal after diagonalization is generated by the pairwise products \(\lambda_+\lambda_-\), \(\lambda_+\lambda_0\), \(\lambda_-\lambda_0\). At each of the above points, exactly one eigenvalue is a unit, so the local ideal is generated by the other two eigenvalues. Their Jacobian determinants in coordinates \((a,b)\) at \((0,0),(2,0),(-2,0)\) are respectively \(3,4,1\) in \(\mathbb F_5\); hence every local scheme is a single reduced point.

**(5) One geometric isomorphism class.** Let \(g_c(z)=z^8+cz^6+cz^2+1\). In characteristic five,
\[
(z-1)^8+(z+1)^8=2g_{-2}(z).
\]
Therefore the fractional-linear substitution \(x=(z-1)/(z+1)\), accompanied by \(Y=(z+1)^4y\) and scaling \(Y\) by a square root of \(2\) in \(k\), identifies the smooth projective curves \(y^2=x^8+1\) and \(Y^2=g_{-2}(z)\). Finally \(g_{-2}(2z)=g_2(z)\) in \(\mathbb F_5[z]\), proving all three exceptions are geometrically isomorphic. No claim is made that these isomorphisms descend to \(\mathbb F_5\).

**(6) Attainment of the other ranks.** The smooth pairs \((1,3)\) and \((0,1)\) have eigenvalue patterns respectively \((4,0,3)\) and \((2,2,3)\), and so exhibit ranks two and three. Together with the three rank-one pairs, these realize all asserted strata.

## Verification

Run `python3 verify_howe_rank.py` with SymPy installed. This checks the Cartier matrix, diagonalization, exact discriminant factorization, three quotient function-field identities, pairwise polynomial elimination, reducedness, geometric isomorphisms, and independent point-count identities for all smooth \(\mathbb F_5\)-parameters. Expected terminator:

`HOWE5_RANK_STRATIFICATION_PASS eigenvalues=3 rank1=3 reduced=3 classes=1 GF5= {1: 3, 2: 6, 3: 4}`

Run `python3 verify_field25.py` (only the standard Python library). It independently enumerates all \(625\) coefficient pairs over \(\mathbb F_{25}\), checks smoothness and predicted rank, and verifies the degree-one point counts of the three elliptic quotients against those of the genus-three curve. Expected terminator:

`HOWE5_GF25_INDEPENDENT_PASS smooth= 553 rank_counts= {1: 3, 2: 60, 3: 490} rank_one= [(0, 0), (2, 0), (3, 0)]`

The finite-field enumerations are corroboration, **not** proofs of the assertions over the algebraic closure. Those assertions follow from the identities and elimination in Steps (1)–(5). The scripts use no unavailable files, external mathematical databases or proprietary software.

## Relationship to prior work

Howe curves, decomposed Richelot isogenies, and elliptic quotient decompositions are established tools. Moriya–Kudo (2022, §§4–5) give explicit genus-three Howe models and enumerate **superspecial** examples, including the absence of superspecial hyperelliptic Howe curves in characteristic five; that absence and the quotient construction are not claimed as new here. Ohashi (2021) studies maximality of superspecial hyperelliptic Howe curves, not the present rank-one coefficient scheme. Borówka–Shatsila (2023) classify complex genus-three hyperelliptic curves with multiple involutions and their quotients; the existence of involutions and the form of a reciprocal equation are not claimed as new. Frei (2017) studies genus-three hyperelliptic Cartier \(a\)-numbers in small characteristic. The additional specific claim here is the complete characteristic-five arithmetic stratification of the displayed two-parameter family, the reduced three-point rank-one coefficient locus, and its collapse to one geometric isomorphism class. No assertion of global novelty is deduced merely from unsuccessful searches.

## Limitations

This is not a classification of all Howe curves, all genus-three hyperelliptic curves, or all curves of \(5\)-rank one. The reduced rank-one subscheme is a subscheme of the **fixed coefficient parameter space**; it must not be confused with the full moduli-theoretic rank-one locus or its multiplicity. Distinct twists over a nonalgebraically closed field are not classified. Hasse–Witt matrices are semilinear; an untwisted matrix rank would not ordinarily suffice for \(p\)-rank, and the constant diagonalization here is essential. The three rank-one curves have \(a\)-number two but are not superspecial. General results or earlier computations could implicitly contain some of the special formulas; the available literature comparison is not an independent priority certification.

## References

1. T. Moriya and M. Kudo, *Some explicit arithmetics on curves of genus three and their applications*, arXiv:2209.02926v1 (first posted 7 September 2022), §§4–5. https://arxiv.org/abs/2209.02926
2. P. Borówka and A. Shatsila, *Hyperelliptic genus 3 curves with involutions and a Prym map*, arXiv:2308.07038v1 (14 August 2023). https://arxiv.org/abs/2308.07038
3. R. Ohashi, *On the maximality of hyperelliptic Howe curves of genus 3*, arXiv:2112.11152v1 (21 December 2021). https://arxiv.org/abs/2112.11152
4. S. Frei, *The \(a\)-number of hyperelliptic curves*, arXiv:1703.03516v1 (10 March 2017). https://arxiv.org/abs/1703.03516
